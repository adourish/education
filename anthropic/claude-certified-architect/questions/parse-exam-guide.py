#!/usr/bin/env python3
"""
Read the sample questions out of the Claude Certified Architect exam guide.

The guide publishes a set of sample questions "to illustrate the format and
difficulty level of the exam", each with its options, its answer and the
reasoning behind it. They are the only questions for this exam written by the
people who set it, so they are worth having exactly as published rather than
paraphrased.

    python parse-exam-guide.py <exam-guide.pdf>

Writes exam-guide-samples.json next to this script. Needs PyMuPDF.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "exam-guide-samples.json"

# Which domain each scenario leans on, as the guide states under each one.
# Which subject area each scenario mostly draws on, using the headings exactly
# as they appear in the guide. The guide names six scenarios and puts four of
# them on any given paper; these are the four its sample questions come from.
SCENARIO_AREA = {
    "Customer Support Resolution Agent": "agentic",
    "Code Generation with Claude Code": "claude-code",
    "Multi-Agent Research System": "agentic",
    "Claude Code for Continuous Integration": "claude-code",
    "Developer Productivity with Claude": "claude-code",
    "Document Data Extraction": "prompting",
}


def clean(s: str) -> str:
    """One space between words, and no page furniture."""
    s = re.sub(r"Anthropic, PBC\s*·\s*Confidential Need to Know \(NTK\)\s*", " ", s)
    return re.sub(r"\s+", " ", s.replace("​", "").replace("\xad", "")).strip()


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("give me the path to the exam guide PDF")
    try:
        import fitz
    except ImportError:
        sys.exit("needs PyMuPDF: pip install pymupdf")

    doc = fitz.open(sys.argv[1])
    full = "\n".join(doc[n].get_text() for n in range(doc.page_count))
    full = full.replace("​", "").replace("\xad", "")
    full = re.sub(r"Anthropic, PBC\s*·\s*Confidential Need to Know \(NTK\)\s*", "\n", full)

    body = full[full.find("Sample Questions"):full.find("Preparation Strategies")]
    if not body:
        sys.exit("could not find the sample questions in that file")

    # A scenario heading introduces the questions that come after it. Taking
    # the heading found inside a question block attributes each question to
    # the scenario that follows it rather than the one it belongs to, so the
    # headings are located first and each question takes the last one above it.
    headings = [(m.start(), clean(m.group(1)))
                for m in re.finditer(r"Scenario:\s*([^\n]+)", body)]

    def scenario_at(pos):
        found = ""
        for at, name in headings:
            if at >= pos:
                break
            found = name
        return found

    starts = [m.start() for m in re.finditer(r"(?=Question \d+:)", body)]
    bounds = starts + [len(body)]
    rows = []

    for n, begin in enumerate(starts):
        chunk = body[begin:bounds[n + 1]]
        scenario = scenario_at(begin)

        num = re.match(r"\s*Question (\d+):", chunk).group(1)
        # The stem runs up to the first option marker.
        opt_start = re.search(r"\bA\)\s", chunk)
        ans = re.search(r"Correct Answer:\s*([A-D])", chunk)
        if not opt_start or not ans:
            continue

        stem = clean(chunk[chunk.index(":") + 1:opt_start.start()])
        options_blob = chunk[opt_start.start():ans.start()]
        tail = clean(chunk[ans.end():])

        # Options are run together in one paragraph: "A) ... B) ... C) ... D) ..."
        parts = re.split(r"\s(?=[A-D]\)\s)", clean(options_blob))
        options = []
        for part in parts:
            m = re.match(r"([A-D])\)\s*(.+)", part)
            if m:
                options.append(m.group(1) + ". " + m.group(2).strip())
        if len(options) != 4:
            print(f"  question {num}: found {len(options)} options, skipping")
            continue

        letter = ans.group(1)
        correct = next(o for o in options if o.startswith(letter + "."))

        rows.append({
            "id": "cca-" + num,
            "question": (f"[{scenario}] " if scenario else "") + stem,
            "options": options,
            "answer": correct,
            "explanation": tail,
            "area": SCENARIO_AREA.get(scenario, "unclassified"),
            "domain": "unassigned",     # filled in by the domain rules
            "source": "cca-exam-guide",
            "reviewed": True,           # written by the people who set the exam
        })

    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"read {len(rows)} sample questions into {OUT.name}")
    for r in rows:
        print(f"  {r['id']:8} {r['question'][:78]}")


if __name__ == "__main__":
    main()
