#!/usr/bin/env python3
"""
Assemble app.html from the template and the data file.

Keeps the data out of the hand-edited template, so app.template.html stays
readable and the data can be rebuilt without touching the page.

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

APP_VERSION = "1.0.0"


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

    if "__DATA__" in html or "__APP_VERSION__" in html:
        raise SystemExit("A placeholder was left unreplaced.")

    OUT.write_text(html, encoding="utf-8")

    parsed = json.loads(DATA.read_text(encoding="utf-8"))
    kb = OUT.stat().st_size // 1024
    print(f"app.html written - v{APP_VERSION}, built {build_date}, {kb} KB")
    print(f"  {len(parsed['questions'])} questions")
    print(f"  {sum(len(s['rows']) for s in parsed['sections'])} recall rows "
          f"in {len(parsed['sections'])} sections")
    if kb > 15000:
        print("  WARNING: approaching the 16 MB artifact limit")


if __name__ == "__main__":
    main()
