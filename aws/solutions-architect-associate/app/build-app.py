#!/usr/bin/env python3
"""
Assemble the drill board from the template and the data file.

Writes two builds, because they are opened in different places:

  app.html                    for publishing as an Artifact. The publisher wraps
                              it in its own <html><head> skeleton, so this one is
                              a fragment and must NOT carry its own.

  saa-c03-recall-board.html   standalone, for saving to disk and opening straight
                              off a phone or laptop. It needs the full document
                              wrapper: without a doctype the browser parses in
                              quirks mode, where position:fixed misbehaves and
                              the modal lands inline instead of over the page,
                              and without a charset it decodes UTF-8 as Latin-1
                              and every en dash turns into "a EUR".

Run build-data.py first, then this.

Usage:
    python build-app.py
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
TEMPLATE = HERE / "app.template.html"
DATA = HERE / "app-data.json"
OUT = HERE / "app.html"
OUT_STANDALONE = HERE / "saa-c03-recall-board.html"
SEED = HERE / "progress-seed.json"

APP_VERSION = "1.18.0"

# SHA-256 of the board's password. The hash rather than the word, so the
# password is not sitting in the published file in plain text. This is a
# curtain, not a lock: the page and its questions are all client-side.
PASSWORD = "Purple123"

# The wrapper the Artifact publisher would otherwise supply. Mirrors it closely:
# same charset, same viewport with viewport-fit=cover, same safe-area padding on
# :root and the same [hidden] rule the page's own code relies on.
STANDALONE_HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  :root {
    color-scheme: light dark;
    padding-top: env(safe-area-inset-top, 0px);
    padding-bottom: env(safe-area-inset-bottom, 0px);
  }
  html, body { margin: 0; }
  body { font: 14px system-ui, -apple-system, "Segoe UI", sans-serif; }
  img { max-width: 100%; }
  [hidden] { display: none !important; }
</style>
</head>
<body>
"""

STANDALONE_FOOT = """
</body>
</html>
"""


def main() -> None:
    if not DATA.exists():
        raise SystemExit("app-data.json is missing - run build-data.py first.")

    html = TEMPLATE.read_text(encoding="utf-8")
    data = DATA.read_text(encoding="utf-8")

    # The payload sits in a <script type="application/json"> block, so the only
    # sequence that could break out of it is a literal </script>.
    data = data.replace("</script", "<\\/script")

    build_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    html = html.replace("__DATA__", data)
    html = html.replace("__APP_VERSION__", APP_VERSION)
    html = html.replace("__BUILD_DATE__", build_date)

    # Progress shipped with the build. Merged into whatever a browser already
    # has, once, so a new machine or a cleared browser is not back at zero.
    seed = "null"
    if SEED.exists():
        seed = json.dumps(json.loads(SEED.read_text(encoding="utf-8")),
                          separators=(",", ":")).replace("</script", "<\\/script")
    html = html.replace("__SEED__", seed)

    import hashlib
    html = html.replace("__PASS_SHA__", hashlib.sha256(PASSWORD.encode()).hexdigest())

    for left in ("__DATA__", "__APP_VERSION__", "__BUILD_DATE__",
             "__PASS_SHA__", "__SEED__"):
        if left in html:
            raise SystemExit(f"placeholder {left} was left unreplaced")
    if False:
        raise SystemExit("A placeholder was left unreplaced.")

    OUT.write_text(html, encoding="utf-8")
    OUT_STANDALONE.write_text(STANDALONE_HEAD + html + STANDALONE_FOOT, encoding="utf-8")

    parsed = json.loads(DATA.read_text(encoding="utf-8"))
    print(f"v{APP_VERSION}, built {build_date}")
    print(f"  {len(parsed['questions'])} questions, "
          f"{sum(len(s['rows']) for s in parsed['sections'])} recall rows "
          f"in {len(parsed['sections'])} sections")
    for f, what in ((OUT, "artifact fragment"), (OUT_STANDALONE, "standalone, saveable")):
        print(f"  {f.name:30} {f.stat().st_size // 1024:5} KB   {what}")

    if OUT.stat().st_size // 1024 > 15000:
        print("  WARNING: approaching the 16 MB artifact limit")

    # The standalone build is useless without these two, so fail loudly.
    sa = OUT_STANDALONE.read_text(encoding="utf-8")
    for needed in ("<!doctype html>", '<meta charset="utf-8">'):
        if needed not in sa:
            raise SystemExit(f"standalone build is missing {needed}")

    # A stray control character renders as a replacement glyph and, inside
    # script code, breaks the whole page. Two have got in this way, both from a
    # backslash escape that a build step read as a number: once as NUL, once as
    # U+0015 from a CSS escape that began with a backslash and two digits. So
    # check for every control character rather than only the one that bit first.
    for f in (OUT, OUT_STANDALONE):
        for n, line in enumerate(f.read_text(encoding='utf-8').split(chr(10)), 1):
            for ch in line:
                if ord(ch) < 32 and ch not in (chr(13), chr(9)):
                    raise SystemExit(
                        f'{f.name} line {n} holds U+{ord(ch):04X}, a control character. '
                        f'It is almost certainly a backslash escape read as a number on '
                        f'the way in. Write the character itself instead.')


if __name__ == "__main__":
    main()
