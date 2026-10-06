#!/usr/bin/env python3
"""
Audit one source's questions in the bank for structural damage.

Parsing a PDF into questions goes wrong quietly: a stem gets glued onto an
option, a letter goes missing, an option comes back empty. None of that raises
an error, and the question still renders — it is just unanswerable. This checks
for each failure mode and reports the ids so they can be fixed or dropped.

    python audit-source.py [--source certempire] [--write]

--write records the ids it would drop into audit-drop.json, which build-bank.py
can then apply. Without it, nothing is changed.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

HERE = Path(__file__).parent
BANK = HERE / "bank.json"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s.lower())).strip()


def letter_of(text: str) -> str | None:
    m = re.match(r"\s*([A-H])[.)]", text)
    return m.group(1) if m else None


def body_of(text: str) -> str:
    return re.sub(r"^\s*[A-H][.)]\s*", "", text).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="certempire",
                    help="one source name, or 'all' to sweep every source")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    bank = json.loads(BANK.read_text(encoding="utf-8"))
    if args.source == "all":
        mine = bank
        others = []
    else:
        mine = [r for r in bank if r.get("source") == args.source]
        others = [r for r in bank if r.get("source") != args.source]
    print(f"auditing {len(mine)} questions from {args.source}\n")

    problems: dict[str, list[str]] = defaultdict(list)

    for r in mine:
        qid, stem = r["id"], r["question"]
        opts = r.get("options") or []
        ans = r.get("answer") or ""
        bodies = [body_of(o) for o in opts]
        letters = [letter_of(o) for o in opts]

        # A question with no options at all is not broken: some sources give
        # only the answer, and the board self-marks those. One lone option is.
        if not opts:
            continue
        if len(opts) < 2:
            problems["only one option"].append(qid)
            continue

        # Letters must run A, B, C... with none missing or repeated.
        expected = [chr(ord("A") + i) for i in range(len(opts))]
        if letters != expected:
            problems["option letters not in sequence"].append(qid)

        # "Yes." and "No." are real options. Only a genuinely blank one is broken.
        if any(len(b) < 2 for b in bodies):
            problems["an option is empty"].append(qid)

        if len(set(norm(b) for b in bodies)) != len(bodies):
            problems["two options are identical"].append(qid)

        # The stem leaking into an option is the failure that produced an
        # unanswerable question: the option carries the question's own words.
        tail = norm(stem)[-120:]
        if tail and any(tail in norm(b) for b in bodies):
            problems["the stem leaked into an option"].append(qid)

        head = norm(stem)[:120]
        if head and any(head in norm(b) for b in bodies):
            problems["the stem leaked into an option"].append(qid)

        # The answer may name several options, separated by a semicolon, and
        # may give the text without a letter. Both are fine. What is not fine
        # is an answer whose text matches nothing on offer.
        parts = [p.strip() for p in re.split(r";\s*", ans) if p.strip()]
        for part in parts:
            pl = letter_of(part)
            text = norm(body_of(part))
            if pl and pl not in letters:
                problems["answer names a letter that is not there"].append(qid)
                break
            if pl:
                target = norm(bodies[letters.index(pl)])
                if target and text and SequenceMatcher(
                        None, target[:200], text[:200]).ratio() < 0.55:
                    problems["answer text contradicts the letter it names"].append(qid)
                    break
            else:
                # No letter: it has to match one of the options by text.
                best = max((SequenceMatcher(None, norm(b)[:200], text[:200]).ratio()
                            for b in bodies), default=0)
                if text and best < 0.55:
                    problems["answer matches none of the options"].append(qid)
                    break

    # Duplicates inside this source, and against everything else.
    seen: dict[str, str] = {}
    for r in mine:
        k = norm(r["question"])[:160]
        if k in seen:
            problems["duplicate of another question in this source"].append(
                f"{r['id']} = {seen[k]}")
        else:
            seen[k] = r["id"]

    other_keys = {norm(r["question"])[:160]: r["id"] for r in others}
    cross = [f"{r['id']} = {other_keys[norm(r['question'])[:160]]}"
             for r in mine if norm(r["question"])[:160] in other_keys]
    if cross:
        problems["duplicate of a question in another source"] = cross

    total = sum(len(v) for v in problems.values())
    if not total:
        print("no structural problems found")
    for name, ids in sorted(problems.items(), key=lambda kv: -len(kv[1])):
        print(f"{len(ids):5}  {name}")
        print(f"       {', '.join(ids[:10])}{' ...' if len(ids) > 10 else ''}")

    # Anything in these buckets cannot be answered correctly, so it is worth
    # dropping rather than leaving in to be got wrong for the wrong reason.
    fatal = ("the stem leaked into an option",
             "answer names a letter that is not there",
             "answer text contradicts the letter it names",
             "answer matches none of the options",
             "only one option",
             "an option is empty",
             "two options are identical",
             "option letters not in sequence")
    drop = sorted({i for k in fatal for i in problems.get(k, [])})
    print(f"\n{len(drop)} of {len(mine)} would be dropped as unanswerable "
          f"({100 * len(drop) / max(len(mine), 1):.1f}%)")

    if args.write:
        out = HERE / "audit-drop.json"
        out.write_text(json.dumps(sorted(drop), indent=1), encoding="utf-8")
        print(f"wrote {out.name}")


if __name__ == "__main__":
    main()
