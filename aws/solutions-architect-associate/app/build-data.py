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
import sys

HERE = Path(__file__).parent
POSTER = HERE.parent / "poster" / "poster.html"
BANK = HERE.parent / "questions" / "bank.json"
YIELD = HERE.parent / "questions" / "yield.json"
CONCEPTS_SRC = HERE.parent / "questions" / "yield-report.py"
FLAGS = HERE.parent / "questions" / "review" / "flags.json"
OUT = HERE / "app-data.json"

# The glossary lives with the questions, so import it from there.
sys.path.insert(0, str(HERE.parent / "questions"))
from glossary import GLOSSARY  # noqa: E402
from domains import EXAM_WEIGHTS, DOMAIN_NAMES  # noqa: E402

# Bumped when the question set itself changes, separately from the app.
VERSION = "1.4.0"

# Where each question came from. The short code travels with every question so
# the app can filter by provider; the name and note are for the picker and the
# card, because the sets are not of equal quality and it is worth knowing which
# one you are drilling.
SOURCES = {
    "certempire":              ("CE", "Cert Empire"),
    "ditectrev-saa-c03":       ("DT", "Ditectrev"),
    "saa-c03-optioned":        ("ET", "ExamTopics-format set"),
    "iamrushabhshahh-saa-c03": ("GH", "GitHub dump"),
    "whizlabs-25":             ("WL", "Whizlabs sampler"),
}
UNKNOWN_SOURCE = ("??", "Unrecorded")


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


def check_patterns(named: dict[str, str], what: str) -> None:
    """Catch a word boundary that has turned into a control character.

    A pattern written as \\b matches a word boundary. If a tool ever writes the
    file without the r prefix, or interprets the escape on the way in, the two
    characters become a single backspace character, which matches nothing and
    looks almost identical in an editor. Two patterns sat broken that way for
    weeks, quietly explaining nothing. Nothing here should contain a control
    character, so say so loudly rather than build a file that does less than it
    appears to.
    """
    bad = {k: v for k, v in named.items() if any(ord(c) < 32 for c in v)}
    if bad:
        for k, v in bad.items():
            print(f"  {what} {k!r}: {v!r}")
        raise SystemExit(f"{len(bad)} {what} pattern(s) contain a control character "
                         f"where a word boundary was meant")


def main() -> None:
    concepts = load_concepts()
    check_patterns(concepts, "concept")
    check_patterns({k: v[0] for k, v in GLOSSARY.items()}, "glossary")
    compiled = {k: re.compile(v, re.I) for k, v in concepts.items()}
    tiers = {r["concept"]: r["tier"] for r in json.loads(YIELD.read_text(encoding="utf-8"))}

    def tag(text: str) -> list[str]:
        return [k for k, rx in compiled.items() if rx.search(text)]

    # Glossary terms, matched against the question and every option, so a hint
    # can explain the services a question names without revealing which is right.
    gloss = [(name, re.compile(pat, re.I)) for name, (pat, _) in GLOSSARY.items()]

    def terms_in(text: str) -> list[str]:
        """Matched terms, most specific first.

        A hint is capped at nine entries, and truncating in dictionary order
        could drop the term the question is actually about: one whose whole
        point is Intelligent-Tiering would keep the generic "Amazon S3" and
        lose the specific one. Longer names are the more specific ones, so
        they go first and survive the cut.
        """
        hit = [name for name, rx in gloss if rx.search(text)]
        return sorted(hit, key=lambda n: (-len(n), n))

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
                # Stable id so a row's own score survives a rebuild. Derived from
                # the cue text rather than its position, because inserting a row
                # above would otherwise shift every score below it onto the wrong
                # line.
                "id": key + ":" + re.sub(r"[^a-z0-9]+", "-", cue.lower())[:46].strip("-"),
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
    # The same question appears as gh-N in the option-less dump and q-N in the
    # optioned source, so a flag or verdict against one has to find the other.
    def alias(qid: str) -> list[str]:
        out = [qid]
        for a, b in (("gh-", "et-"), ("et-", "gh-")):
            if qid.startswith(a):
                out.append(b + qid[len(a):])
        return out

    def flag_for(qid: str):
        for a in alias(qid):
            if a in flags:
                return flags[a]
        return None

    # Review findings: questions the fact-checkers judged wrong, stale, or
    # carrying an explanation that cannot be trusted.
    flags = {}
    if FLAGS.exists():
        flags = json.loads(FLAGS.read_text(encoding="utf-8"))

    # A question that has since been adjudicated is no longer suspect: a fix
    # replaced its answer, and a keep means the reviewer was wrong. Either way
    # the warning comes off. Only questions still awaiting a verdict keep one.
    corr_path = HERE.parent / "questions" / "corrections.json"
    if corr_path.exists():
        corrections = json.loads(corr_path.read_text(encoding="utf-8"))
        for qid, c in corrections.items():
            if c["verdict"] in ("fix", "keep"):
                for a in alias(qid):
                    flags.pop(a, None)

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
            "t": terms_in(q + " " + " ".join(r.get("options") or []) + " " + a)[:9],
            "src": SOURCES.get(r.get("source"), UNKNOWN_SOURCE)[0],
            # A star means a person has checked this question, not a scraper.
            "star": bool(r.get("reviewed")),
            # How many independent publishers carry this question. Two or more
            # means separate outfits both think the exam asks it.
            "agree": len(r.get("in_origins") or [r.get("source")]),
            "flag": flag_for(r["id"]),
        })

    # How many questions touch each poster line. A line nothing covers is a gap
    # in the question bank, not evidence the line does not matter, so it is
    # marked rather than removed.
    for sec in sections:
        for row in sec["rows"]:
            row["qn"] = sum(1 for q in questions
                            if any(k in row["c"] for k in q["c"]))
    bare = sum(1 for sec in sections for row in sec["rows"] if not row["qn"])
    print(f"  {bare} poster lines have no question covering them")

    data = {
        "version": VERSION,
        "built": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "exam": "SAA-C03",
        "guide": "Exam guide version 1.1",
        "sections": sections,
        "questions": questions,
        "concepts": {k: {"tier": tiers.get(k, 0)} for k in concepts},
        "glossary": {name: what for name, (_, what) in GLOSSARY.items()},
        "sources": dict(SOURCES.values()),
        # What the real paper is made of, so a mock can be drawn in the same
        # proportions rather than in whatever proportions the question sets
        # happen to hold. Kept apart from "exam", which is the exam's name.
        "paper": {
            "questions": 65,
            "minutes": 130,
            "pass": 720,          # out of 1000, as AWS scores it
            "weights": EXAM_WEIGHTS,
            "domainNames": DOMAIN_NAMES,
        },
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
    print(f"  {sum(1 for q in questions if q['star'])} starred as human-reviewed")
    print(f"  {sum(1 for q in questions if q['agree'] > 1)} carried by two or more publishers")
    print(f"  {sum(1 for q in questions if q['flag'])} flagged by review")
    withterms = sum(1 for q in questions if q["t"])
    avg = sum(len(q["t"]) for q in questions) / max(len(questions), 1)
    print(f"  {withterms} questions have glossary terms, {avg:.1f} on average")
    print(f"  {len(concepts)} concepts")
    print(f"  {OUT.name} {kb} KB")


if __name__ == "__main__":
    main()
