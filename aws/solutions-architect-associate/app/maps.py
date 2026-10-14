#!/usr/bin/env python3
"""
The maps: one picture per part of the exam, saying where its questions live.

Each map is a Markdown file in planning/maps/, and that file is the source:
change the words there, run this, build. The file uses a handful of headings
the parser knows:

    # The networking map            the fold's title
    > one line                      the lede under the title
    ## row                          boxes side by side (two across on a phone)
    ## row: edge | hub | home       the same, with a coloured stripe
    ## arrow                        a down-arrow with the next paragraph under it
    ## zone: Your VPC | vpc         a dashed box holding what follows ...
    ## end                          ... up to here. Styles: vpc, sub, home
    ## key                          the grey strip at the bottom
    ## anything else                notes for people; not drawn

Inside a row, a box is a bold line, then its words up to a blank line:

    **NAT gateway**
    match: NAT gateway|NAT instance
    Private subnets out, never in. *One per zone* in production.

Words between single stars are the pick: what a question is after, drawn in
magenta and underlined. In an arrow, double stars make the words bold.

The optional "match:" line is a pattern tried against each question's answer,
so the box can carry a tick-and-cross tally of how those questions went for
you. Without one, the title is used, split on commas, "and" and "or". A
"match: -" line means the box counts nothing.

The maps are written into app.template.html between marker comments, one
fold each, and the page takes them out again for an exam they do not belong
to. Run with --preview <dir> to also write one standalone page per map.
"""
from __future__ import annotations

import html
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "app.template.html"
MAPS = HERE.parent.parent.parent / "planning" / "maps"
ARROW = chr(0x2193)

CSS = """
/* The maps: one picture per part of the exam. Boxes two across at any width,
   so a phone gets the same shape as a desk. */
.netmap { margin: 4px 0 0; }
.netmap *, .netmap *::before { box-sizing: border-box; }
.netmap .lede { font-size: 0.86rem; margin: 0 0 8px; }
.nm-row { display: flex; flex-wrap: wrap; gap: 6px; align-items: stretch; }
.nm-row + .nm-row, .nm-zone + .nm-row, .nm-row + .nm-zone, .nm-zone + .nm-zone { margin-top: 6px; }
.nm-row > * { flex: 1 1 140px; min-width: 0; }
.nm-box { border: 1px solid var(--rule); border-radius: 8px; background: var(--surface);
          padding: 6px 8px; }
.nm-box h4 { margin: 0 0 1px; font-size: 0.9rem; font-weight: 600; line-height: 1.3;
             display: flex; justify-content: space-between; align-items: baseline; gap: 6px; }
.nm-box h4 .tally { font-size: 0.72rem; font-weight: 500; flex: none; }
.nm-box p { margin: 0; font-size: 0.8rem; color: var(--ink-2); line-height: 1.45; }
/* The pick is underlined as well as coloured, so it never rests on colour alone. */
.nm-box .pick { color: var(--magenta); font-weight: 600;
                text-decoration: underline dotted; text-underline-offset: 3px;
                text-decoration-thickness: 1px; }
.nm-box.edge { border-left: 4px solid var(--cyan); }
.nm-box.hub  { border-left: 4px solid var(--magenta); }
.nm-box.home { border-left: 4px solid var(--amber); }
.nm-zone { border: 2px dashed var(--rule); border-radius: 10px; padding: 7px; margin: 0; }
.nm-zone > h3 { margin: 0 0 5px; font-size: 0.86rem; font-weight: 600; color: var(--ink-2); }
.nm-zone.vpc { background: var(--cyan-soft); border-color: var(--cyan); }
.nm-zone.sub { background: var(--surface); border-style: solid; border-color: var(--rule); }
.nm-zone.sub > h3 { color: var(--ink-3); font-size: 0.78rem; margin-bottom: 4px; }
.nm-zone.home { background: var(--amber-soft); border-color: var(--amber); }
.nm-arrow { text-align: center; color: var(--ink-3); font-size: 0.78rem; padding: 2px 0; line-height: 1.35; }
.nm-arrow b { color: var(--ink-2); font-weight: 600; }
.nm-arrow::before { content: "ARROW"; display: block; font-size: 1.05rem; color: var(--cyan); line-height: 1; }
.nm-key { margin: 8px 0 0; padding: 5px 8px; border-radius: 7px; background: var(--surface-2);
          font-size: 0.76rem; color: var(--ink-2); line-height: 1.45; }
.nm-key span { display: inline-block; width: 9px; height: 9px; border-radius: 3px; margin: 0 4px 0 1px; vertical-align: middle; }
""".replace("ARROW", ARROW)

KNOWN = ("row", "arrow", "zone", "end", "key")


def inline(text: str, pick: str = "pick") -> str:
    """Escape, then turn *picks* and **bold** into their spans."""
    s = html.escape(text, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r'<span class="%s">\1</span>' % pick, s)
    return s


def key_line(text: str) -> str:
    s = inline(text)
    for name in ("cyan", "magenta", "amber"):
        s = re.sub(r"\b%s\b" % name,
                   '<span style="background: var(--%s)"></span>%s' % (name, name), s, count=1)
    return s


def parse(md: str) -> dict:
    """The file as a tree: title, lede, and a list of items."""
    title, lede = "", []
    root: list = []
    stack = [root]
    row: list | None = None
    mode = "notes"            # row | arrow | key | notes
    box: dict | None = None
    para: list = []

    def close_box():
        nonlocal box
        if box is not None and row is not None:
            box["body"] = " ".join(box["body"]).strip()
            row.append(box)
        box = None

    def close_row():
        nonlocal row
        close_box()
        if row is not None and row:
            stack[-1].append({"kind": "row", "boxes": row, "cls": row_cls})
        row = None

    def flush_para():
        nonlocal para
        text = " ".join(para).strip()
        if text and mode == "arrow":
            stack[-1].append({"kind": "arrow", "text": text})
        elif text and mode == "key":
            stack[-1].append({"kind": "key", "text": text})
        para = []

    row_cls = ""
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            continue
        if line.startswith("> "):
            lede.append(line[2:].strip())
            continue
        m = re.match(r"^#{2,6}\s+(\w+)\s*:?\s*(.*)$", line)
        if m and m.group(1).lower() in KNOWN:
            close_row(); flush_para()
            word, rest = m.group(1).lower(), m.group(2).strip()
            if word == "row":
                row, row_cls, mode = [], rest, "row"
            elif word == "arrow":
                mode = "arrow"
            elif word == "key":
                mode = "key"
            elif word == "zone":
                name, _, style = rest.partition("|")
                zone = {"kind": "zone", "title": name.strip(),
                        "style": style.strip() or "sub", "items": []}
                stack[-1].append(zone)
                stack.append(zone["items"])
                mode = "notes"
            elif word == "end":
                if len(stack) > 1:
                    stack.pop()
                mode = "notes"
            continue
        if m or line.startswith("#"):
            close_row(); flush_para()
            mode = "notes"
            continue
        if mode == "row":
            b = re.match(r"^\*\*(.+?)\*\*\s*$", line)
            if b:
                close_box()
                box = {"title": b.group(1).strip(), "body": [], "match": None}
            elif not line.strip():
                close_box()
            elif box is not None and line.startswith("match:"):
                box["match"] = line[6:].strip()
            elif box is not None:
                box["body"].append(line.strip())
        elif mode in ("arrow", "key"):
            if line.strip():
                para.append(line.strip())
            else:
                flush_para()
    close_row(); flush_para()
    while len(stack) > 1:
        stack.pop()
    return {"title": title, "lede": " ".join(lede), "items": root}


def pattern(box: dict) -> str:
    """What this box counts: its own pattern, or one made from its title."""
    m = box.get("match")
    if m == "-":
        return ""
    if m:
        re.compile(m)
        if any(ord(c) < 32 for c in m) or "\\\\" in m:
            raise SystemExit(box["title"] + ": a broken match pattern")
        return m
    parts = [p.strip() for p in re.split(r",| and | or ", box["title"]) if p.strip()]
    # A leading boundary only, so "Dedicated Host" also counts "Dedicated Hosts".
    return "|".join(r"\b" + re.escape(p) for p in parts)


def draw(items: list) -> str:
    out = []
    for it in items:
        if it["kind"] == "row":
            cls = (" " + it["cls"]) if it["cls"] else ""
            out.append('<div class="nm-row">')
            for b in it["boxes"]:
                rx = pattern(b)
                attr = (' data-rx="%s"' % html.escape(rx, quote=True)) if rx else ""
                out.append('<div class="nm-box%s"%s><h4><span>%s</span></h4><p>%s</p></div>'
                           % (cls, attr, inline(b["title"]), inline(b["body"])))
            out.append('</div>')
        elif it["kind"] == "arrow":
            out.append('<div class="nm-arrow">%s</div>' % inline(it["text"]))
        elif it["kind"] == "zone":
            out.append('<div class="nm-zone %s"><h3>%s</h3>' % (it["style"], inline(it["title"])))
            out.append(draw(it["items"]))
            out.append('</div>')
        elif it["kind"] == "key":
            out.append('<div class="nm-key">%s</div>' % key_line(it["text"]))
    return "\n".join(out)


def fold(slug: str, tree: dict) -> str:
    body = ['<div class="netmap">']
    if tree["lede"]:
        body.append('<p class="lede">%s</p>' % inline(tree["lede"]))
    body.append(draw(tree["items"]))
    body.append('</div>')
    return "\n".join([
        '    <details class="fold map" id="fold-map-%s" data-fold="map-%s">' % (slug, slug),
        '      <summary>%s<span class="count">one picture</span></summary>' % inline(tree["title"]),
        '      <div class="inner">',
        "\n".join(body),
        '      </div>',
        '    </details>',
    ])


PREVIEW = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<style>
:root { --surface: #fbfcfc; --surface-2: #e3ebed; --ink: #10181b; --ink-2: #46545a;
  --ink-3: #7b888d; --rule: #d3dde0; --cyan: #00707e; --cyan-soft: #d9eef1;
  --magenta: #99206c; --magenta-soft: #f7e3ef; --amber: #8a6508; --amber-soft: #fbf0d5; }
body { margin: 0; padding: 16px; background: var(--surface); color: var(--ink);
       font: 15px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
.netmap .lede { color: var(--ink-2); line-height: 1.45; }
.netmap { max-width: 380px; margin: 0 auto; }
h2 { font-size: 1.05rem; max-width: 380px; margin: 0 auto 6px; }
%s
</style></head><body>
<h2>%s</h2>
%s
</body></html>
"""


def main(argv: list[str]) -> None:
    files = sorted(MAPS.glob("*.md"))
    if not files:
        raise SystemExit("no maps in " + str(MAPS))
    preview = None
    if "--preview" in argv:
        preview = pathlib.Path(argv[argv.index("--preview") + 1])
        preview.mkdir(parents=True, exist_ok=True)

    folds = []
    for f in files:
        slug = re.sub(r"^\d+-", "", f.stem)
        tree = parse(f.read_text(encoding="utf-8"))
        boxes = sum(len(i["boxes"]) for i in walk(tree["items"]) if i["kind"] == "row")
        if not tree["title"] or not boxes:
            raise SystemExit(f"{f.name}: no title or no boxes; check the headings")
        folds.append(fold(slug, tree))
        print(f"  {f.name:24} {boxes:3d} boxes  {tree['title']}")
        if preview:
            body = '<div class="netmap">%s%s</div>' % (
                ('<p class="lede">%s</p>' % inline(tree["lede"])) if tree["lede"] else "",
                draw(tree["items"]))
            (preview / (slug + ".html")).write_bytes(
                (PREVIEW % (tree["title"], CSS, tree["title"], body)).encode("utf-8"))

    raw = TEMPLATE.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    raw = put(raw, nl, "/* MAPS-CSS-START */", "/* MAPS-CSS-END */",
              nl + CSS.replace("\n", nl) + nl,
              ".dectraps li:last-child { margin-bottom: 0; }", before=False)
    raw = put(raw, nl, "<!-- MAPS-HTML-START -->", "<!-- MAPS-HTML-END -->",
              nl + (nl + nl).join(f.replace("\n", nl) for f in folds) + nl,
              '    <div class="board" id="board"></div>', before=True)
    for ch in raw:
        if ord(ch) < 32 and ch not in "\r\n":
            raise SystemExit("a control character crept in")
    TEMPLATE.write_bytes(raw.encode("utf-8"))
    print(f"{len(folds)} maps written into the poster")


def walk(items: list):
    for it in items:
        yield it
        if it["kind"] == "zone":
            yield from walk(it["items"])


def put(text: str, nl: str, start: str, end: str, block: str, anchor: str, before: bool) -> str:
    """Replace what sits between the markers, or add it at the anchor."""
    if start in text:
        a, b = text.index(start), text.index(end) + len(end)
        return text[:a] + start + block + end + text[b:]
    if anchor not in text:
        raise SystemExit("could not find: " + anchor[:40])
    piece = start + block + end
    return text.replace(anchor, (piece + nl + nl + anchor) if before else (anchor + nl + nl + piece), 1)


if __name__ == "__main__":
    main(sys.argv[1:])
