#!/usr/bin/env python3
"""
Put a fresh progress export into the build, so a new browser starts where you
left off instead of at zero.

    python update-seed.py <exported-progress.json>
    python update-seed.py <file> --dry-run       # show the change, write nothing
    python update-seed.py <file> --keep-unknown  # keep ids no question matches
    python update-seed.py <file> --no-bump       # leave the app version alone

What it does, in order:

  1. Checks the file really is an export from this board
  2. Checks the counts add up, and that nothing went backwards
  3. Drops question ids that no longer match any question in the bank
  4. Writes progress-seed.json, keeping the records shipped before it
  5. Bumps the app version, because what the build ships with has changed
  6. Rebuilds the app and the site

It does not touch git. Commit on a feature branch and open a pull request, the
same as any other change.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SEED = HERE / "progress-seed.json"
DATA = HERE / "app-data.json"
BUILD_APP = HERE / "build-app.py"
BUILD_SITE = HERE.parent.parent.parent / "site" / "build-site.py"

COUNTED = ("concepts", "rows", "sections")

# How many earlier records to keep in the file. A browser works out what is new
# to it by subtracting what it was last given; one that has not been opened for
# a few builds needs the older record in order to subtract it, so a short
# history travels with the build. Five is a long time at this rate.
KEEP_HISTORY = 5


def die(msg: str) -> None:
    sys.exit("stopped: " + msg)


EXAM_ID = json.loads((Path(__file__).parent / "app-data.json")
                     .read_text(encoding="utf-8")).get("examId", "saa-c03")


def load_export(path: Path) -> dict:
    try:
        d = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as e:
        die(f"{path.name} is not readable as JSON ({e})")
    if d.get("app") not in ("Recall Board", "SAA-C03 Recall Board"):
        die(f"{path.name} says it came from {d.get('app')!r}, not the recall board")

    # A format 2 file holds every exam the browser had work for, each under its
    # own id. The seed is this exam's progress, so take that one and leave the
    # rest alone. An older file has only ever been this exam, so it is used as
    # it stands.
    exams = d.get("exams")
    if isinstance(exams, dict):
        want = exams.get(EXAM_ID)
        if not isinstance(want, dict):
            die(f"{path.name} holds {', '.join(exams) or 'no exams'}, "
                f"and this build is {EXAM_ID}")
        prog = want.get("progress")
    else:
        prog = d.get("progress")
    if not isinstance(prog, dict):
        die(f"{path.name} has no progress in it")
    for k in COUNTED:
        if not isinstance(prog.get(k, {}), dict):
            die(f"{k} should be a set of counts")
    for k in ("seen", "right", "wrong"):
        if not isinstance(prog.get(k, 0), int):
            die(f"{k} should be a whole number")
    if prog.get("right", 0) + prog.get("wrong", 0) != prog.get("seen", 0):
        die(f"right ({prog.get('right')}) plus wrong ({prog.get('wrong')}) does not "
            f"equal answered ({prog.get('seen')}) — the export looks damaged")
    return d


def totals(prog: dict) -> dict:
    return {k: sum(v.get("r", 0) + v.get("w", 0) for v in prog.get(k, {}).values())
            for k in COUNTED}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("export", help="a progress JSON exported from the board")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--keep-unknown", action="store_true",
                    help="keep question ids that match nothing in the bank")
    ap.add_argument("--no-bump", action="store_true",
                    help="leave the app version alone")
    args = ap.parse_args()

    new = load_export(Path(args.export))
    prog = new["progress"]
    # An export from the board never carries a history; a seed file does, and
    # it is rebuilt below rather than copied across.
    new.pop("history", None)

    old = json.loads(SEED.read_text(encoding="utf-8")) if SEED.exists() else None
    oldp = (old or {}).get("progress", {})

    if old and old.get("exported") == new.get("exported"):
        print(f"the build already ships this export ({new.get('exported')}), "
              f"so there is nothing to do")
        return

    # ---- nothing may go backwards ------------------------------------------
    # What the build ships only ever grows: a browser works out what is new by
    # subtracting what it was last given, and a count that shrank is ignored
    # rather than taken away, which would quietly lose answers. Say so instead.
    back = []
    for k in COUNTED:
        for key, now in prog.get(k, {}).items():
            was = oldp.get(k, {}).get(key)
            if was and (now.get("r", 0) < was.get("r", 0)
                        or now.get("w", 0) < was.get("w", 0)):
                back.append(f"{k}/{key}: {was} -> {now}")
    for k in ("seen", "right", "wrong"):
        if prog.get(k, 0) < oldp.get(k, 0):
            back.append(f"{k}: {oldp.get(k)} -> {prog.get(k)}")
    if back:
        print("these counts went down, which an export from the same board should "
              "not do — check you picked the newer file:")
        for line in back[:12]:
            print("  " + line)
        if len(back) > 12:
            print(f"  and {len(back) - 12} more")
        die("counts went backwards")

    # ---- question ids that no longer exist ---------------------------------
    known = {q["id"] for q in json.loads(DATA.read_text(encoding="utf-8"))["questions"]}
    unknown = sorted(k for k in prog.get("questions", {}) if k not in known)
    if unknown:
        print(f"{len(unknown)} question id(s) match nothing in the bank, so they are "
              f"{'kept' if args.keep_unknown else 'dropped'}: {', '.join(unknown)}")
        print("  (usually left over from before the ids were given a source prefix)")
        if not args.keep_unknown:
            prog["questions"] = {k: v for k, v in prog["questions"].items() if k in known}

    # ---- what changed ------------------------------------------------------
    t_new, t_old = totals(prog), totals(oldp)
    print()
    print(f"  answered   {oldp.get('seen', 0):5} -> {prog.get('seen', 0)}")
    print(f"  right      {oldp.get('right', 0):5} -> {prog.get('right', 0)}")
    print(f"  wrong      {oldp.get('wrong', 0):5} -> {prog.get('wrong', 0)}")
    for k in COUNTED:
        print(f"  {k:10} {len(oldp.get(k, {})):5} -> {len(prog.get(k, {}))} entries "
              f"({t_old.get(k, 0)} -> {t_new[k]} marks)")
    print(f"  questions  {len(oldp.get('questions', {})):5} -> "
          f"{len(prog.get('questions', {}))} answered by id")
    print(f"  exported   {(old or {}).get('exported', '-')}  ->  {new.get('exported')}")

    if args.dry_run:
        print("\ndry run, nothing written")
        return

    # ---- write and rebuild -------------------------------------------------
    history = []
    if old:
        history.append({"exported": old.get("exported"),
                        "progress": old.get("progress", {})})
        history.extend(h for h in (old.get("history") or [])
                       if h.get("exported") != old.get("exported"))
    new["history"] = history[:KEEP_HISTORY]

    SEED.write_text(json.dumps(new, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nwrote {SEED.name}, keeping {len(new['history'])} earlier record(s) so a "
          f"browser that skipped a build can still work out what is new to it")

    if not args.no_bump:
        src = BUILD_APP.read_text(encoding="utf-8", newline="")
        m = re.search(r'APP_VERSION = "(\d+)\.(\d+)\.(\d+)"', src)
        if not m:
            die("could not find APP_VERSION in build-app.py")
        bumped = f"{m.group(1)}.{m.group(2)}.{int(m.group(3)) + 1}"
        BUILD_APP.write_text(src.replace(m.group(0), f'APP_VERSION = "{bumped}"', 1),
                             encoding="utf-8", newline="")
        print(f"app version now {bumped}")

    for script in (BUILD_APP, BUILD_SITE):
        print(f"\n--- {script.name} ---")
        if subprocess.run([sys.executable, script.name], cwd=script.parent).returncode:
            die(f"{script.name} failed")

    print("\nnext: commit on a feature branch, open a pull request into dev, then "
          "dev into main. Never commit to dev or main directly.")


if __name__ == "__main__":
    main()
