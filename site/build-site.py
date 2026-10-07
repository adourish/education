#!/usr/bin/env python3
"""
Assemble the published site into docs/, which GitHub Pages serves.

The app is the site. https://adourish.github.io/education/ opens straight into
the drill board, so there is one URL to bookmark and no landing page to click
through. The printable poster sits beside it.

Everything here is generated. Build the app first, then run this.

    python aws/solutions-architect-associate/app/build-data.py
    python aws/solutions-architect-associate/app/build-app.py
    python site/build-site.py

Usage:
    python build-site.py
"""

from __future__ import annotations

import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
SUBJECT = ROOT / "aws" / "solutions-architect-associate"
DOCS = ROOT / "docs"

APP = SUBJECT / "app" / "saa-c03-recall-board.html"

# Other exams published alongside the main one, each at its own path with
# its own page. One page per exam rather than one page holding them all:
# the AWS board is nearly 3 MB and the stub is a fifth of a megabyte, so
# putting both in one file would make everyone download an exam they are
# not studying. They still share one record of progress, because the
# browser keeps storage per site rather than per page.
OTHER_EXAMS = [
    ("cca-f", ROOT / "anthropic" / "claude-certified-architect" / "app"
              / "cca-f-recall-board.html"),
]
POSTER_HTML = SUBJECT / "poster" / "poster.html"
POSTER_PDFS = [
    ("aws-saa-c03-poster.pdf", "18 x 24 in, three columns"),
    ("aws-saa-c03-poster-2col.pdf", "12 x 18 in, two columns"),
    ("aws-saa-c03-poster-phone.pdf", "5 x 34 in, one column, phone"),
]

# A tab icon and a home-screen icon, drawn rather than fetched so the site has
# no external dependency. Cyan ground, "SAA" in white.
ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="96" fill="#00707e"/>
  <text x="256" y="300" font-family="Helvetica,Arial,sans-serif" font-size="150"
        font-weight="700" fill="#ffffff" text-anchor="middle">SAA</text>
  <text x="256" y="390" font-family="Helvetica,Arial,sans-serif" font-size="84"
        font-weight="700" fill="#9fe8f0" text-anchor="middle">C03</text>
</svg>
"""

MANIFEST = """{
  "name": "SAA-C03 Recall Board",
  "short_name": "SAA-C03",
  "description": "Recall poster, practice questions and progress for the AWS Solutions Architect Associate exam.",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#eef3f4",
  "theme_color": "#00707e",
  "icons": [
    { "src": "icon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any maskable" }
  ]
}
"""

# Added to the app's <head> when it is published. Gives the page a home-screen
# icon and a saveable name, which a plain bookmark otherwise lacks on a phone.
HEAD_EXTRAS = """<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon.svg">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#00707e">
<meta name="description" content="Recall poster, practice questions and progress tracking for the AWS Solutions Architect Associate (SAA-C03) exam.">
<meta name="color-scheme" content="light dark">
"""

NOT_FOUND = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Not here</title>
<style>
  body { margin:0; min-height:100vh; display:grid; place-items:center;
         background:#eef3f4; color:#10181b; text-align:center;
         font:16px/1.6 system-ui, -apple-system, "Segoe UI", sans-serif; padding:24px; }
  a { color:#00707e; }
  @media (prefers-color-scheme: dark) { body { background:#0c1417; color:#e8eff1; } a { color:#4fd0e0; } }
</style>
</head>
<body>
  <div>
    <h1>Nothing at this address</h1>
    <p><a href="./">Open the recall board</a></p>
  </div>
</body>
</html>
"""


def main() -> None:
    if not APP.exists():
        raise SystemExit(f"{APP.name} is missing - run build-app.py first.")

    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    # The app becomes index.html, with the icon and manifest links added.
    app = APP.read_text(encoding="utf-8")
    if "</head>" not in app:
        raise SystemExit("the app has no </head> - is it the standalone build?")
    app = app.replace("</head>", HEAD_EXTRAS + "</head>", 1)
    (DOCS / "index.html").write_text(app, encoding="utf-8")

    for slug, src in OTHER_EXAMS:
        if not src.exists():
            print(f"  {slug:24} SKIPPED, {src.name} has not been built")
            continue
        sub = DOCS / slug
        sub.mkdir(parents=True, exist_ok=True)
        page = src.read_text(encoding="utf-8")
        page = page.replace("</head>", HEAD_EXTRAS.replace('"icon.svg"', '"../icon.svg"')
                            .replace('"manifest.webmanifest"', '"../manifest.webmanifest"')
                            + "</head>", 1)
        (sub / "index.html").write_text(page, encoding="utf-8")

    (DOCS / "icon.svg").write_text(ICON_SVG, encoding="utf-8")
    (DOCS / "manifest.webmanifest").write_text(MANIFEST, encoding="utf-8")
    (DOCS / "404.html").write_text(NOT_FOUND, encoding="utf-8")
    # Without this, Pages runs Jekyll and drops anything starting with _.
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    # The poster, as a page and as the three printable sheets.
    if POSTER_HTML.exists():
        shutil.copy2(POSTER_HTML, DOCS / "poster.html")
    copied = []
    for name, _ in POSTER_PDFS:
        src = SUBJECT / "poster" / name
        if src.exists():
            shutil.copy2(src, DOCS / name)
            copied.append(name)

    notes_pdf = SUBJECT / "pdf" / "aws-saa-c03-memorization-notes.pdf"
    if notes_pdf.exists():
        shutil.copy2(notes_pdf, DOCS / notes_pdf.name)

    built = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    version = re.search(r'APP_VERSION = "([^"]+)"', app)
    total = sum(f.stat().st_size for f in DOCS.rglob("*") if f.is_file())

    print(f"site built {built}  app v{version.group(1) if version else '?'}")
    print(f"  docs/index.html          the app, {(DOCS / 'index.html').stat().st_size // 1024} KB")
    print(f"  docs/poster.html         {'yes' if (DOCS / 'poster.html').exists() else 'MISSING'}")
    for slug, _ in OTHER_EXAMS:
        f = DOCS / slug / 'index.html'
        if f.exists():
            print(f"  docs/{slug}/index.html   a second exam, "
                  f"{f.stat().st_size // 1024} KB")
    print(f"  printable sheets         {len(copied)}")
    print(f"  icon, manifest, 404      added")
    print(f"  total                    {total // 1024} KB")
    print()
    print("Pages serves this from the main branch, /docs folder.")


if __name__ == "__main__":
    main()
