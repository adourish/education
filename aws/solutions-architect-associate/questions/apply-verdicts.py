#!/usr/bin/env python3
"""
Merge the adjudicators' verdicts into corrections.json.

The question bank is generated from the raw files in sources/, so corrections
must not be written into bank.json — a rebuild would wipe them. They live here
instead, and build-bank.py applies them on every build:

  drop  the question is removed from the bank entirely
  fix   its answer and explanation are replaced with the corrected ones
  keep  the reviewer was wrong; the flag is cleared and the question stands

Run after the adjudicators have written verdicts/*-verdicts.json.

Usage:
    python apply-verdicts.py
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
VERDICTS = HERE / "verdicts"
OUT = HERE / "corrections.json"

VALID = {"keep", "fix", "drop"}


def main() -> None:
    merged: dict[str, dict] = {}
    problems: list[str] = []

    files = sorted(VERDICTS.glob("*-verdicts.json"))
    if not files:
        raise SystemExit("No verdict files yet — the adjudicators have not finished.")

    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"{path.name}: not valid JSON ({e})")
            continue

        for qid, v in data.items():
            verdict = (v.get("verdict") or "").strip().lower()
            if verdict not in VALID:
                problems.append(f"{qid}: verdict {verdict!r} is not keep/fix/drop")
                continue
            # A fix is only usable if it actually carries the replacement text.
            if verdict == "fix" and not (v.get("answer") and v.get("why")):
                problems.append(f"{qid}: marked fix but has no answer and/or why")
                continue
            if qid in merged:
                problems.append(f"{qid}: adjudicated twice")
                continue

            merged[qid] = {
                "verdict": verdict,
                "truth": (v.get("truth") or "").strip(),
                "reason": (v.get("reason") or "").strip(),
                "exam_relevant": bool(v.get("exam_relevant", True)),
                "importance": (v.get("importance") or "medium").strip().lower(),
            }
            if verdict == "fix":
                merged[qid]["answer"] = v["answer"].strip()
                merged[qid]["why"] = v["why"].strip()

    OUT.write_text(json.dumps(merged, indent=1, ensure_ascii=False), encoding="utf-8")

    counts = Counter(v["verdict"] for v in merged.values())
    print(f"{len(merged)} verdicts merged from {len(files)} files -> {OUT.name}")
    for k in ("keep", "fix", "drop"):
        print(f"  {k:5} {counts[k]:3}")

    irrelevant = [q for q, v in merged.items() if not v["exam_relevant"]]
    if irrelevant:
        print(f"  judged not exam-relevant: {len(irrelevant)} ({', '.join(sorted(irrelevant))})")

    if problems:
        print("\nProblems that need a human eye:")
        for p in problems:
            print("  -", p)

    # Every flagged question should have been adjudicated; say so if not.
    flags_path = HERE / "review" / "flags.json"
    if flags_path.exists():
        flagged = set(json.loads(flags_path.read_text(encoding="utf-8")))
        missing = flagged - set(merged)
        if missing:
            print(f"\n{len(missing)} flagged questions have no verdict: "
                  f"{', '.join(sorted(missing))}")
            print("They keep their warning until one is given.")


if __name__ == "__main__":
    main()
