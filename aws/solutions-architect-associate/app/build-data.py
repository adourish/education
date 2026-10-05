#!/usr/bin/env python3
"""
Build app-data.json — the single data file the drill board loads.

Pulls together three things that already exist, so nothing is authored twice:

  ../poster/poster.html      the recall rows, by section
  ../questions/bank.json     the practice questions
  ../questions/yield.json    how often each concept is actually asked

Every row and every question is tagged with the concepts it touches, using the
same regex set yield-report.py counts with. That shared tagging is what lets a
missed question put a cross against the matching rows on the poster.

Usage:
    python build-data.py
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
POSTER = HERE.parent / "poster" / "poster.html"
BANK = HERE.parent / "questions" / "bank.json"
YIELD = HERE.parent / "questions" / "yield.json"
CONCEPTS_SRC = HERE.parent / "questions" / "yield-report.py"
OUT = HERE / "app-data.json"

VERSION = "1.0.0"


def load_concepts() -> dict[str, str]:
    src = CONCEPTS_SRC.read_text(encoding="utf-8")
    block = re.search(r"CONCEPTS: dict\[str, str\] = \{(.*?)\n\}", src, re.S).group(1)
    return dict(re.findall(r'"([^"]+)":\s*r"((?:[^"\\]|\\.)*)"', block))


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    return (s.replace("&middot;", "·").replace("&mdash;", "—").replace("&ndash;", "–")
             .replace("&amp;", "&").replace("&dagger;", "").replace("&asymp;", "")
             .replace("&lo;", "").replace("&nbsp;", " ").replace("&asymp", "")
             .strip())


def main() -> None:
    concepts = load_concepts()
    compiled = {k: re.compile(v, re.I) for k, v in concepts.items()}
    tiers = {r["concept"]: r["tier"] for r in json.loads(YIELD.read_text(encoding="utf-8"))}

    def tag(text: str) -> list[str]:
        return [k for k, rx in compiled.items() if rx.search(text)]

    # ---- poster rows, grouped by the section they sit in --------------------
    html = POSTER.read_text(encoding="utf-8")
    sections = []
    for sm in re.finditer(r'<section class="s-(\w+)">(.*?)</section>', html, re.S):
        key, body = sm.group(1), sm.group(2)
        h2 = re.search(r"<h2>(.*?)(?:<span class=\"tag\">(.*?)</span>)?</h2>", body, re.S)
        title = strip_tags(h2.group(1)) if h2 else key
        tagline = strip_tags(h2.group(2) or "") if h2 else ""

        rows = []
        for rm in re.finditer(
            r'<div class="qa">\s*<div class="q">(.*?)</div>\s*<div class="a">(.*?)</div>\s*</div>',
            body, re.S):
            raw_q, raw_a = rm.group(1), rm.group(2)
            cue, ans = strip_tags(raw_q), strip_tags(raw_a)
            if not cue:
                continue
            ym = re.search(r'class="yq y(\d)"', raw_q)
            rows.append({
                "cue": cue,
                "ans": ans,
                "tier": int(ym.group(1)) if ym else 0,
                "trap": "&dagger;" in raw_q,
                "alt": "&asymp;" in raw_q,
                "c": tag(f"{cue} {ans}"),
            })

        traps = [strip_tags(t) for t in re.findall(r'<div class="trap">(.*?)</div>', body, re.S)]
        notes = [strip_tags(t) for t in re.findall(r'<div class="mn">(.*?)</div>', body, re.S)]

        if rows or notes:
            sections.append({"key": key, "title": title, "tagline": tagline,
                             "rows": rows, "traps": traps, "notes": notes})

    # ---- questions ----------------------------------------------------------
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    questions = []
    for r in bank:
        q = r["question"].strip()
        a = r["answer"].strip()
        questions.append({
            "id": r["id"],
            "q": q,
            "a": a,
            "opts": r.get("options") or None,
            "why": (r.get("explanation") or "")[:520],
            "area": r["area"],
            "dom": r.get("domain", ""),
            "c": tag(f"{q} {a}"),
        })

    data = {
        "version": VERSION,
        "built": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "exam": "SAA-C03",
        "guide": "Exam guide version 1.1",
        "sections": sections,
        "questions": questions,
        "concepts": {k: {"tier": tiers.get(k, 0)} for k in concepts},
        "areaTitles": {
            "compute": "Compute", "storage": "Storage", "database": "Databases",
            "networking": "Networking", "security": "Security & identity",
            "integration": "Integration", "analytics": "Analytics",
            "monitoring": "Monitoring & management", "cost": "Cost optimization",
            "resilience": "Resilience & DR", "unclassified": "Unsorted",
        },
    }

    OUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    rows = sum(len(s["rows"]) for s in sections)
    kb = OUT.stat().st_size // 1024
    print(f"version {VERSION} built {data['built']}")
    print(f"  {len(sections)} poster sections, {rows} rows")
    print(f"  {len(questions)} questions ({sum(1 for q in questions if q['opts'])} with options)")
    print(f"  {len(concepts)} concepts")
    print(f"  app-data.json {kb} KB")


if __name__ == "__main__":
    main()
