#!/usr/bin/env python3
"""
Turn the review findings into machine-readable flags.

Six reviewers checked all 522 banked questions against current AWS behaviour and
wrote their findings to review/*-findings.md. This reads those files and produces
review/flags.json, which build-data.py folds into the app so a question known to
be wrong warns the reader instead of quietly teaching the wrong thing.

Usage:
    python build-flags.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
REVIEW = HERE / "review"
OUT = REVIEW / "flags.json"

# Heading -> severity. "wrong" means do not trust the answer; "stale" means the
# answer was right once; "explanation" means the answer stands but the reasoning
# under it does not.
KINDS = [
    ("wrong", r"confirmed wrong|wrong answer"),
    ("stale", r"out of date|outdated|stale"),
    ("explanation", r"explanation"),
]

LABELS = {
    "wrong": "The stated answer is wrong",
    "stale": "The stated answer is out of date",
    "explanation": "The explanation below is unreliable",
}


def kind_of(heading: str) -> str | None:
    h = heading.lower()
    for name, pat in KINDS:
        if re.search(pat, h):
            return name
    return None


def main() -> None:
    flags: dict[str, dict] = {}

    for path in sorted(REVIEW.glob("*-findings.md")):
        area = path.name.replace("-findings.md", "")
        kind = None
        qid = None
        buf: list[str] = []

        def flush():
            if not qid or not kind:
                return
            note = " ".join(buf).strip()
            note = re.sub(r"\s+", " ", note)
            note = re.sub(r"\*\*(.+?):\*\*", r"\1:", note)
            # Keep the first two sentences; the full write-up stays in the file.
            note = note[:400].strip()
            prev = flags.get(qid)
            # A question flagged twice keeps the more serious verdict.
            order = {"wrong": 3, "stale": 2, "explanation": 1}
            if prev and order[prev["kind"]] >= order[kind]:
                return
            flags[qid] = {"kind": kind, "note": note, "area": area}

        for line in path.read_text(encoding="utf-8").split("\n"):
            if line.startswith("### "):
                flush()
                buf = []
                m = re.match(r"###\s+((?:gh|wl)-\d+)", line)
                qid = m.group(1) if m else None
            elif line.startswith("## "):
                flush()
                buf = []
                qid = None
                kind = kind_of(line[3:])
            elif qid:
                buf.append(line)
        flush()

    OUT.write_text(json.dumps(flags, indent=1, ensure_ascii=False), encoding="utf-8")

    from collections import Counter
    c = Counter(v["kind"] for v in flags.values())
    print(f"{len(flags)} questions flagged -> {OUT.name}")
    for k in ("wrong", "stale", "explanation"):
        print(f"  {LABELS[k]:38} {c[k]}")


if __name__ == "__main__":
    main()
