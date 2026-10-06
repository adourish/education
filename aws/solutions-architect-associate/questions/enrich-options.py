#!/usr/bin/env python3
"""
Recover the answer options the first pass threw away.

The Iamrushabhshahh repo ships two files. The text file holds the stated answer
and a worked explanation but NO distractors, which is why the practice test
could only offer real multiple choice on 27 of 522 questions. The companion PDF
holds all 684 questions complete with their A-E options but no answer key.

This joins them: stems and options from the PDF, the correct letter worked out
by matching the text file's stated answer against those options. The result is
written as one canonical source file that build-bank.py parses.

Matching is by question number first, then confirmed by comparing the two
stems. A pair whose stems disagree is dropped rather than guessed at, because a
mismatched join would attach the right answer to the wrong question.

Inputs (paths are arguments so this can be re-run on a fresh download):
    python enrich-options.py <pdf-text> <solutions-text>

Writes:
    sources/saa-c03-optioned.optioned.txt
    enrich-report.txt
"""

from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "sources" / "saa-c03-optioned.optioned.txt"
REPORT = HERE / "enrich-report.txt"

# How alike two stems must be to count as the same question, and how much
# better the winning option must match than the runner-up.
STEM_MIN = 0.55
OPTION_MIN = 0.45
OPTION_MARGIN = 0.08


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", re.sub(r"\s+", " ", s.lower())).strip()


def ratio(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def parse_pdf(text: str) -> dict[int, dict]:
    text = text.replace("\r\n", "\n")
    parts = re.split(r"(?m)^Question #(\d+)\s*$", text)
    out: dict[int, dict] = {}
    for i in range(1, len(parts), 2):
        num = int(parts[i])
        body = re.sub(r"(?m)^Topic \d+.*$", "", parts[i + 1])
        marks = list(re.finditer(r"(?m)^([A-E])\.\s", body))
        if len(marks) < 2:
            continue
        stem = re.sub(r"\s+", " ", body[: marks[0].start()]).strip()
        opts: dict[str, str] = {}
        for k, m in enumerate(marks):
            end = marks[k + 1].start() if k + 1 < len(marks) else len(body)
            opts[m.group(1)] = re.sub(r"\s+", " ", body[m.end(): end]).strip()
        if stem and len(opts) >= 2:
            out[num] = {"stem": stem, "opts": opts}
    return out


def parse_solutions(text: str) -> dict[int, dict]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    chunks = [c.strip() for c in re.split(r"(?m)^-{5,}\s*$", text) if c.strip()]
    out: dict[int, dict] = {}
    for chunk in chunks:
        m = re.match(r"\s*(\d{1,4})\s*[\].)]\s*(.*)", chunk, re.S)
        if not m:
            continue
        num, body = int(m.group(1)), m.group(2)

        answer = None
        am = re.search(r"(?mi)^\s*ans\s*[-:]\s*(.+?)$", body)
        if am:
            answer, rest = am.group(1).strip(), body[am.end():]
        else:
            qm = list(re.finditer(r"(?m)^.*\?\s*$", body))
            if qm:
                tail = body[qm[-1].end():].lstrip("\n")
                first = next((l for l in tail.split("\n") if l.strip()), "")
                if len(first.strip()) >= 12:
                    answer = first.strip()
                    rest = tail[tail.find(first) + len(first):]
            if not answer:
                om = re.search(r"(?m)^\s*([A-E])[.)]\s+(.{15,}?)\s*$", body)
                if om:
                    answer, rest = f"{om.group(1)}. {om.group(2)}", body[om.end():]
        if not answer:
            continue
        out[num] = {
            "answer": answer,
            "stem": re.sub(r"\s+", " ", body[:200]),
            "why": re.sub(r"\n{3,}", "\n\n", rest.strip())[:1600],
        }
    return out


def pick_letter(answer: str, opts: dict[str, str]) -> tuple[str | None, str]:
    """Work out which option the stated answer refers to."""
    # The answer often already names its letter.
    lead = re.match(r"\s*([A-E])[.)]\s*(.*)", answer, re.S)
    if lead and lead.group(1) in opts:
        body = lead.group(2).strip()
        # Trust the letter only if the text behind it also matches that option.
        if not body or ratio(body, opts[lead.group(1)]) >= OPTION_MIN:
            return lead.group(1), "letter stated and text agrees"
        # The letter and the text disagree: believe the text.
        answer = body

    scored = sorted(((ratio(answer, v), k) for k, v in opts.items()), reverse=True)
    best, second = scored[0], (scored[1] if len(scored) > 1 else (0.0, None))
    if best[0] >= OPTION_MIN and (best[0] - second[0]) >= OPTION_MARGIN:
        return best[1], f"matched on text ({best[0]:.2f} vs {second[0]:.2f})"
    return None, f"ambiguous (best {best[0]:.2f}, next {second[0]:.2f})"


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    pdf = parse_pdf(Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace"))
    sol = parse_solutions(Path(sys.argv[2]).read_text(encoding="utf-8", errors="replace"))

    kept, notes = [], []
    stats = {"joined": 0, "no_answer": 0, "stem_mismatch": 0, "ambiguous": 0}

    for num in sorted(pdf):
        q = pdf[num]
        s = sol.get(num)
        if not s:
            stats["no_answer"] += 1
            continue
        if ratio(q["stem"][:220], s["stem"]) < STEM_MIN:
            stats["stem_mismatch"] += 1
            notes.append(f"{num}: stems disagree, not joined")
            continue
        letter, how = pick_letter(s["answer"], q["opts"])
        if not letter:
            stats["ambiguous"] += 1
            notes.append(f"{num}: {how}")
            continue
        stats["joined"] += 1
        block = [f"### {num}", q["stem"]]
        for k in sorted(q["opts"]):
            block.append(f"{k}. {q['opts'][k]}")
        block.append(f"ANSWER: {letter}")
        if s["why"]:
            block.append("WHY: " + s["why"].replace("\n", " ").strip())
        kept.append("\n".join(block))

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n\n---\n\n".join(kept) + "\n", encoding="utf-8")

    lines = [
        "Joining the PDF's options to the text file's answers",
        "",
        f"questions in the PDF          {len(pdf)}",
        f"answers in the solutions file {len(sol)}",
        f"successfully joined           {stats['joined']}",
        f"no answer found               {stats['no_answer']}",
        f"stems disagreed               {stats['stem_mismatch']}",
        f"answer matched no option      {stats['ambiguous']}",
        "",
        "Unjoined questions are left out rather than guessed at: attaching an",
        "answer to the wrong stem would be worse than having fewer questions.",
        "",
    ] + notes
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    for line in lines[:9]:
        print(line)
    print(f"\nwrote {OUT.name} and {REPORT.name}")


if __name__ == "__main__":
    main()
