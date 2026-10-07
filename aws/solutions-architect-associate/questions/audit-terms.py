#!/usr/bin/env python3
"""
Check what the hints actually explain, and what they quietly miss.

Two ways a hint fails, and neither one announces itself:

  Nothing explains it.  A question turns on a service no term matches, so the
  hint lists everything except the thing being asked about.

  The explanation is too narrow.  A term matches the service but describes one
  of its uses, so a question about another use is led away from the answer. The
  Snow Family entry described posting disks of data about, which is no help at
  all on a question about running Kubernetes on a ship.

The first can be found by machine: every service named in the bank is checked
against every term. The second cannot, but the same report narrows where to
look, because a term matching far more questions than it has business matching
is usually one carrying several meanings at once.

    python audit-terms.py                # the summary
    python audit-terms.py --missing 40   # the top gaps, most asked about first
    python audit-terms.py --term "AWS Snow Family"    # what one term matches
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from glossary import GLOSSARY  # noqa: E402

BANK = HERE / "bank.json"

# "Amazon Route 53", "AWS Identity and Access Management", "S3 Glacier Instant
# Retrieval": the shape a service or a named part of one takes in a question.
# Numbers and the small joining words belong inside a name, or it gets cut
# short and then looks unexplained when it is nothing of the sort.
WORD = r"(?:[A-Z][\w-]*|\d+)"
JOIN = r"(?:for|and|of|the)"
SERVICE = re.compile(
    r"\b(?:Amazon|AWS|S3|EC2)\s+" + WORD + r"(?:\s+(?:" + JOIN + r"\s+)?" + WORD + r"){0,3}")

# Words that follow a service name often enough to be swept up with it.
TRAILING = re.compile(
    r"\s+(?:And|Or|The|To|For|In|On|With|That|This|These|Which|When|If|It|A|An|Is|Are|Was|Use|Using"
    r"|Then|From|At|By|As|You|Your|Each|Both|All|Will|Would|Should|Can|Must|Has|Have)$")


def tidy(name: str) -> str:
    before = None
    while before != name:
        before = name
        name = TRAILING.sub("", name).strip(" .,;:")
    return name


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--missing", type=int, default=25,
                    help="how many unexplained services to list")
    ap.add_argument("--term", help="show what one term matches")
    args = ap.parse_args()

    bank = json.loads(BANK.read_text(encoding="utf-8"))
    texts = [" ".join([q.get("question", ""), q.get("answer", ""),
                       " ".join(q.get("options") or [])]) for q in bank]

    terms = [(name, re.compile(pat, re.I)) for name, (pat, _) in GLOSSARY.items()]

    if args.term:
        rx = dict(terms).get(args.term)
        if not rx:
            sys.exit(f"no term called {args.term!r}")
        hits = [bank[n]["id"] for n, t in enumerate(texts) if rx.search(t)]
        print(f"{args.term}: {GLOSSARY[args.term][0]}")
        print(f"matches {len(hits)} of {len(bank)} questions")
        print("  " + ", ".join(hits[:40]) + (" ..." if len(hits) > 40 else ""))
        return

    # ---- how much each term is doing -------------------------------------
    counts = {name: sum(1 for t in texts if rx.search(t)) for name, rx in terms}
    dead = sorted(n for n, c in counts.items() if c == 0)
    broad = sorted(((c, n) for n, c in counts.items() if c > len(bank) * 0.25), reverse=True)

    # ---- services nothing explains ---------------------------------------
    named = Counter()
    for t in texts:
        for raw in SERVICE.findall(t):
            name = tidy(raw)
            if len(name.split()) >= 2:
                named[name] += 1

    # A long name can contain a short one: "S3 Glacier Instant Retrieval" holds
    # "Amazon S3". Counting that as explained is how a gap hides, because the
    # term that matched says nothing about the part being asked about. So a name
    # counts as properly explained only when a term matches most of it.
    unexplained = []
    for name, times in named.items():
        covered = 0
        for term_name, rx in terms:
            m = rx.search(name)
            if m:
                covered = max(covered, len(m.group(0)))
        if covered == 0:
            unexplained.append((times, name, "nothing"))
        elif covered < len(name) * 0.6 and len(name.split()) >= 3:
            unexplained.append((times, name, "only in general"))
    unexplained.sort(reverse=True)

    # ---- questions whose own answer is unexplained ------------------------
    bare = 0
    for n, q in enumerate(bank):
        answer = q.get("answer") or ""
        if answer and not any(rx.search(answer) for _, rx in terms):
            bare += 1

    print(f"{len(GLOSSARY)} terms against {len(bank)} questions")
    print()
    print(f"{len(dead)} term(s) match nothing at all"
          + (": " + ", ".join(dead) if dead else ""))
    print()
    print(f"{len(broad)} term(s) match more than a quarter of the bank, which usually "
          f"means one word doing several jobs:")
    for c, n in broad:
        print(f"  {c:5}  {n}")
    print()
    print(f"{bare} question(s) have an answer that no term explains "
          f"({100 * bare / len(bank):.0f}%)")
    print()
    print(f"{len(unexplained)} named service(s) nothing explains. The most asked about:")
    for times, name, how in unexplained[:args.missing]:
        print(f"  {times:5}  {name:46} explained: {how}")


if __name__ == "__main__":
    main()
