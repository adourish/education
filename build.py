#!/usr/bin/env python3
"""
Build everything, in the order it has to be built, and publish it into docs/.

    python build.py            every exam, then the site
    python build.py --quiet    only the last line of each step

The chain matters. Each exam's questions are assembled into a data file, the
data file is poured into the shared page template, and only then can the site
be put together from the built pages. Running one of those on its own leaves
docs/ describing a version that no longer exists, and docs/ is what is
published, so that is the one mistake worth making impossible.

The built pages are not kept in git. They are nine megabytes that change on
every edit, they conflicted on every merge, and they are remade from what is
kept in a few seconds by running this.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
AWS = ROOT / "aws" / "solutions-architect-associate" / "app"
BUILD_APP = AWS / "build-app.py"

# Each exam: where its data is built, and which folder the page is built into.
EXAMS = [
    ("AWS Solutions Architect Associate", AWS),
    ("Claude Certified Architect",
     ROOT / "anthropic" / "claude-certified-architect" / "app"),
]

SITE = ROOT / "site" / "build-site.py"


def run(label: str, args: list[str], quiet: bool) -> None:
    out = subprocess.run([sys.executable] + args, capture_output=True, text=True)
    if out.returncode != 0:
        print(f"\n{label} FAILED\n")
        print(out.stdout.rstrip())
        print(out.stderr.rstrip())
        raise SystemExit(1)
    lines = [ln for ln in out.stdout.splitlines() if ln.strip()]
    if quiet:
        lines = lines[-1:]
    for ln in lines:
        print("   " + ln)


def main() -> None:
    quiet = "--quiet" in sys.argv

    for name, folder in EXAMS:
        print(name)
        data = folder / "build-data.py"
        if not data.exists():
            raise SystemExit(f"   {data} is missing")
        run(name + " data", [str(data)], quiet)
        # One template, filled per exam, so the page builder is always the
        # same script and the folder says which exam it is building.
        run(name + " page", [str(BUILD_APP), str(folder)], quiet)
        print()

    print("Site")
    run("site", [str(SITE)], quiet)


if __name__ == "__main__":
    main()
