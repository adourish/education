#!/usr/bin/env python3
"""
Annotate poster.html with recall marks.

Three marks go onto the cue of each row:

  yield bars   how often the question bank asks about this concept. Driven by
               ../questions/yield.json, so the mark is a count rather than an
               opinion, and it moves when new questions are added.
  dagger       a trap sits next to this fact. Hand-listed in TRAPS below,
               because "this looks right and is not" is a judgement no counter
               can make.
  approx sign  the exam commonly rewords this one. Hand-listed in REWORDED.

The script strips any marks it finds before applying fresh ones, so running it
twice gives the same result as running it once.

Usage:
    python mark-poster.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
POSTER = HERE / "poster.html"
YIELD = HERE.parent / "questions" / "yield.json"
CONCEPTS_SRC = HERE.parent / "questions" / "yield-report.py"

# Facts with a well-known wrong-looking-right neighbour. Matched against the cue.
TRAPS = [
    "Infrequent and re-creatable",
    "Multi-AZ purpose",
    "Read replica purpose",
    "Network ACL",
    "Ephemeral port range",
    "Default vs custom NACL",
    "Block a single malicious IP",
    "Socket or core-based licence",
    "Steady 24/7 vs interruptible batch",
    "Metrics needing the agent",
    "CloudFront certificate must live in",
    "Works at the zone apex, free",
    "Two VPCs vs hundreds",
    "Gateway endpoints work with",
    "Lambda max duration",
    "Default encryption today",
    "Replication requires",
    "SCP effect on the management account",
    "Load a stream to S3 or Redshift, no code",
    "Cross-zone default",
    "EBS scope",
    "RDS gives you OS access",
    "Min duration IA / Glacier / Deep",
]

# Cues the exam likes to dress up in different words.
REWORDED = [
    "Decouple a spiky front end",
    "Multi-AZ purpose",
    "Read replica purpose",
    "Hot / unknown pattern / infrequent",
    "Steady 24/7 vs interruptible batch",
    "Shell access, no open ports, audited",
    "App on EC2 needs S3",
    "Private instances reach the internet",
    "Needs longer than 15 minutes",
    "Faster with no code change",
    "SMB, Windows, Active Directory",
    "Shared files, Linux, many instances",
    "Petabytes, no bandwidth vs ongoing sync",
    "Hybrid in days vs steady bandwidth",
    "Compliance, language, licensing",
    "Fastest region for each user",
    "Policy evaluation order",
    "DynamoDB microsecond reads",
    "Over-sized instances",
    "Everything sitting in S3 Standard",
]


def load_concepts() -> list[tuple[str, int]]:
    """Pair each concept's regex with the tier the count earned it."""
    src = CONCEPTS_SRC.read_text(encoding="utf-8")
    block = re.search(r"CONCEPTS: dict\[str, str\] = \{(.*?)\n\}", src, re.S).group(1)
    patterns = dict(re.findall(r'"([^"]+)":\s*r"((?:[^"\\]|\\.)*)"', block))

    tiers = {r["concept"]: r["tier"] for r in json.loads(YIELD.read_text(encoding="utf-8"))}
    out = []
    for concept, pattern in patterns.items():
        tier = tiers.get(concept, 0)
        if tier:
            out.append((pattern, tier))
    return out


def main() -> None:
    html = POSTER.read_text(encoding="utf-8")

    # Idempotence: remove previously applied marks before adding any.
    html = re.sub(r'<span class="yq y[123]">(?:<i></i>)+</span>', "", html)
    html = re.sub(r'\s*<span class="mk(?: alt)?">(?:&dagger;|&asymp;)</span>', "", html)

    concepts = load_concepts()

    rows = list(re.finditer(
        r'<div class="qa"><div class="q">(.*?)</div><div class="a">(.*?)</div></div>',
        html, re.S))

    marked = {3: 0, 2: 0, 1: 0}
    traps = alts = 0
    out, last = [], 0

    for m in rows:
        cue, ans = m.group(1), m.group(2)
        plain = re.sub(r"<[^>]+>", " ", f"{cue} {ans}")

        tier = 0
        for pattern, t in concepts:
            if t > tier and re.search(pattern, plain, re.I):
                tier = t

        prefix = ""
        if tier:
            prefix = f'<span class="yq y{tier}"><i></i><i></i><i></i></span>'
            marked[tier] += 1

        suffix = ""
        cue_text = re.sub(r"<[^>]+>", "", cue).strip()
        if any(t.lower() in cue_text.lower() for t in TRAPS):
            suffix += '<span class="mk">&dagger;</span>'
            traps += 1
        if any(t.lower() in cue_text.lower() for t in REWORDED):
            suffix += '<span class="mk alt">&asymp;</span>'
            alts += 1
        if suffix:
            suffix = " " + suffix

        new = (f'<div class="qa"><div class="q">{prefix}{cue}{suffix}</div>'
               f'<div class="a">{ans}</div></div>')
        out.append(html[last:m.start()])
        out.append(new)
        last = m.end()

    out.append(html[last:])
    POSTER.write_text("".join(out), encoding="utf-8")

    total = len(rows)
    print(f"{total} rows processed")
    print(f"  yield marks   tier3={marked[3]}  tier2={marked[2]}  tier1={marked[1]}  "
          f"unmarked={total - sum(marked.values())}")
    print(f"  trap daggers  {traps}")
    print(f"  reworded      {alts}")


if __name__ == "__main__":
    main()
