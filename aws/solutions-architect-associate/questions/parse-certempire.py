#!/usr/bin/env python3
"""
Turn the Cert Empire SAA-C03 PDF into the canonical optioned source format.

Layout of each block in that PDF:

    Question: 12
    <stem, several lines>
    A. <option, possibly wrapped>
    B. ...
    Answer:
    B
    Explanation:
    <prose>
    Why Incorrect Options are Wrong:
    A. <why A is wrong>
    References:
    ...

The per-option analysis under "Why Incorrect Options are Wrong" looks exactly
like the option list, so the block must be cut at "Answer:" BEFORE options are
searched for. Reading the whole block at once picks up the analysis as options
and produces nonsense.

Every page is stamped with the buyer's transaction id and IP address, so the
watermark lines are stripped here and the extracted text is kept out of the
published site.

Usage:
    python parse-certempire.py <pdf-path> [-o sources/certempire.optioned.txt]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

HERE = Path(__file__).parent

WATERMARK = re.compile(
    r'CERT.?EMPIRE|Cert.?Empire|^\{"userId"|'
    r'^[C•E•R•T•M•P•I\s.\-�]+$',
    re.I,
)


def clean(text: str) -> str:
    out = []
    for line in text.replace("\r\n", "\n").split("\n"):
        s = line.strip()
        if not s or WATERMARK.search(s):
            continue
        out.append(s)
    return "\n".join(out)


def parse(text: str) -> dict[int, dict]:
    blocks = re.split(r"(?m)^Question:\s*(\d+)\s*$", clean(text))
    questions: dict[int, dict] = {}

    for i in range(1, len(blocks), 2):
        number, body = int(blocks[i]), blocks[i + 1]

        am = re.search(r"(?m)^Answer:\s*$", body)
        if not am:
            continue
        head, tail = body[: am.start()], body[am.end():]

        # The letters sit on the line after "Answer:", sometimes several.
        lm = re.match(r"\s*([A-E](?:\s*[,&and]*\s*[A-E])*)\s*$", tail.split("\n")[1]
                      if len(tail.split("\n")) > 1 else "")
        if not lm:
            continue
        letters = re.findall(r"[A-E]", lm.group(1))

        opts = list(re.finditer(r"(?m)^([A-E])[.)]\s+(.*)$", head))
        if len(opts) < 2:
            continue

        options: dict[str, str] = {}
        for k, m in enumerate(opts):
            end = opts[k + 1].start() if k + 1 < len(opts) else len(head)
            options[m.group(1)] = re.sub(r"\s+", " ", head[m.start(2): end]).strip()

        stem = re.sub(r"\s+", " ", head[: opts[0].start()]).strip()
        if len(stem) < 40 or not all(l in options for l in letters):
            continue

        why = ""
        em = re.search(r"(?m)^Explanation:\s*$", tail)
        if em:
            stop = re.search(r"(?m)^(Why Incorrect Options|References):", tail[em.end():])
            why = tail[em.end(): em.end() + (stop.start() if stop else 1200)]
            why = re.sub(r"\s+", " ", why).strip()

        questions[number] = {
            "stem": stem, "opts": options, "letters": letters, "why": why[:900]
        }
    return questions


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("-o", "--out", default=str(HERE / "sources" / "certempire.optioned.txt"))
    args = ap.parse_args()

    import fitz
    doc = fitz.open(args.pdf)
    text = "".join(doc[i].get_text() for i in range(doc.page_count))

    questions = parse(text)

    blocks = []
    multi = 0
    for n in sorted(questions):
        q = questions[n]
        if len(q["letters"]) != 1:
            multi += 1
            continue  # the optioned format carries one answer letter
        lines = [f"### {n}", q["stem"]]
        for k in sorted(q["opts"]):
            lines.append(f"{k}. {q['opts'][k]}")
        lines.append(f"ANSWER: {q['letters'][0]}")
        if q["why"]:
            lines.append("WHY: " + q["why"])
        blocks.append("\n".join(lines))

    Path(args.out).parent.mkdir(exist_ok=True)
    Path(args.out).write_text("\n\n---\n\n".join(blocks) + "\n", encoding="utf-8")

    print(f"pages {doc.page_count}")
    print(f"  parsed            {len(questions)}")
    print(f"  single-answer     {len(blocks)}  (written)")
    print(f"  multi-answer      {multi}  (skipped: one letter per record)")
    print(f"  -> {args.out}")


if __name__ == "__main__":
    main()
