#!/usr/bin/env python3
"""
Re-work out the exam domain for every question already in the bank.

The rules live in domains.py and are shared with build-bank.py, so a question
read today and a question read a year ago are placed the same way.

    python retag-domains.py --dry-run    # show what would change
    python retag-domains.py              # write it

Nothing else about a question is touched: only its "domain" field.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from domains import domain, EXAM_WEIGHTS  # noqa: E402

BANK = HERE / "bank.json"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    bank = json.loads(BANK.read_text(encoding="utf-8"))
    before = Counter(q.get("domain") or "unassigned" for q in bank)
    after = Counter()
    moved = 0

    for q in bank:
        text = " ".join([q.get("question", ""), q.get("answer", ""),
                         " ".join(q.get("options") or [])])
        was = q.get("domain") or "unassigned"
        now = domain(text)
        after[now] += 1
        if now != was:
            moved += 1
            if not args.dry_run:
                q["domain"] = now

    total = len(bank)
    print(f"{'domain':18} {'before':>8} {'after':>8} {'after %':>9} {'exam %':>8}")
    for key in list(EXAM_WEIGHTS) + ["unassigned"]:
        want = EXAM_WEIGHTS.get(key)
        print(f"{key:18} {before.get(key, 0):8} {after.get(key, 0):8} "
              f"{100 * after.get(key, 0) / total:8.1f}% "
              f"{(str(want) + '%') if want else '':>8}")
    print(f"\n{moved} of {total} questions change domain")

    if args.dry_run:
        print("dry run, nothing written")
        return

    BANK.write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {BANK.name}")
    print("next: rebuild with app/build-data.py and app/build-app.py")


if __name__ == "__main__":
    main()
