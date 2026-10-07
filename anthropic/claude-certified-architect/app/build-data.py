#!/usr/bin/env python3
"""
Build app-data.json for the Claude Certified Architect exam.

This is a stub, and says so on the page. There are twelve questions, all of
them the samples printed in the official exam guide, which is enough to prove
that the app really does hold two exams apart and nowhere near enough to study
from. Everything here is shaped exactly like the AWS exam's data file, because
the page is the same page: one template, one data file per exam.

What is deliberately missing until there is real material:

  - a recall poster worth reading. The few rows below are the themes the
    twelve questions touch, not a syllabus
  - a mock exam shape. The real paper's length, time and pass mark are not
    published anywhere we have, so no mock is offered rather than inventing
    numbers and teaching someone the wrong target
  - diagrams, and a glossary beyond a handful of terms

Usage:
    python build-data.py
    python ../../../aws/solutions-architect-associate/app/build-app.py .
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
QUESTIONS = HERE.parent / "questions" / "exam-guide-samples.json"
OUT = HERE / "app-data.json"

VERSION = "0.1.0"

AREA_TITLES = {
    "agentic": "Agent design",
    "claude-code": "Claude Code",
}

# Enough of a glossary that the "Explain the terms" button has something to
# say. Same contract as the AWS one: say what a thing is and what it is for,
# never which option is right.
GLOSSARY = {
    "Tool use": (r"tool use|tool call|tool_call|calls? a tool",
        "Letting the model ask for a named function to be run and handing it "
        "the result. The model chooses whether and when; your code decides "
        "what is allowed and actually runs it."),
    "System prompt": (r"system prompt",
        "The standing instructions that sit above the conversation. Good for "
        "tone, role and rules of thumb, and weak as a guarantee: the model is "
        "deciding whether to follow it, every time."),
    "Few-shot examples": (r"few-shot|few shot",
        "Worked examples shown to the model so it copies the pattern. They "
        "shift behaviour without changing code, and like a prompt they "
        "persuade rather than enforce."),
    "Programmatic enforcement": (r"programmatic|deterministic|prerequisite",
        "Putting a rule in code rather than in a prompt, so it holds every "
        "time instead of most of the time. The answer whenever being wrong "
        "costs money or breaks a record."),
    "Subagent": (r"subagent|sub-agent",
        "A separate agent given one job and its own context, called by the "
        "main one. Keeps a long side quest out of the main thread."),
    "Context window": (r"context window|context length",
        "How much the model can hold in mind at once. Everything competes for "
        "it: instructions, files read, tool results and the conversation so "
        "far."),
    "MCP": (r"\bMCP\b|Model Context Protocol",
        "A common way to plug tools and data sources into a model, so the same "
        "connector works across different applications."),
    "Hook": (r"\bhook\b|hooks",
        "Code that runs at a fixed point in Claude Code's loop, such as before "
        "a tool runs. Deterministic, so it is how a rule is made to hold "
        "rather than hoped for."),
    "Evaluation": (r"\beval\b|evaluation|test set",
        "A fixed set of cases run against a change so you can tell whether it "
        "helped. Without one, prompt work is guessing."),
    "Guardrail": (r"guardrail|safety check",
        "A check around the model rather than inside it, refusing or altering "
        "what passes. Works whether or not the model co-operates."),
}


def build_sections(rows: list[dict]) -> list[dict]:
    """A poster of the themes the twelve samples touch. Not a syllabus."""
    lines = {
        "agentic": [
            ("A rule that must always hold",
             "Put it in code, not in the prompt",
             "A prompt persuades; code decides. Anything with money or a "
             "record at the end of it gets enforced."),
            ("Tools called in the wrong order",
             "A prerequisite that blocks the later call",
             "Telling the model the order is not the same as the order "
             "holding."),
            ("Too many tools to choose from",
             "Fewer tools, or a router that narrows them first",
             "Choice is the cost. Cutting the list beats describing it better."),
            ("Knowing whether a change helped",
             "A fixed set of cases, run before and after",
             "Without one you are comparing two feelings."),
        ],
        "claude-code": [
            ("Work that must happen every time",
             "A hook, not an instruction",
             "A hook runs at a fixed point whether or not the model thought "
             "of it."),
            ("A long side quest in the middle of a task",
             "A subagent with its own context",
             "Keeps the main thread readable and the context free."),
            ("The same setup on everyone's machine",
             "Checked into the repository, not typed per person",
             "Anything a teammate has to remember will be forgotten."),
            ("Giving the model a tool it does not have",
             "An MCP server",
             "One connector, usable from more than one application."),
        ],
    }
    out = []
    for key, items in lines.items():
        out.append({
            "key": key,
            "title": AREA_TITLES[key],
            "tagline": "Themes the sample questions turn on",
            "notes": [],
            "traps": [],
            "rows": [{
                "id": key + "-" + str(n + 1),
                "cue": cue,
                "ans": ans,
                "alt": "",
                "trap": trap,
                "c": [key],
                "tier": 1,
                "qn": sum(1 for r in rows if r.get("area") == key),
            } for n, (cue, ans, trap) in enumerate(items)],
        })
    return out


def main() -> None:
    rows = json.loads(QUESTIONS.read_text(encoding="utf-8"))

    questions = []
    for r in rows:
        area = r.get("area") or "agentic"
        questions.append({
            "id": r["id"],
            "q": r.get("question", ""),
            "a": r.get("answer", ""),
            "opts": r.get("options", []),
            "why": r.get("explanation", ""),
            "area": area,
            "dom": r.get("domain") or "unassigned",
            "src": "CCA",
            "c": [area],
            "t": [name for name, (pat, _) in GLOSSARY.items()
                  if re.search(pat, r.get("question", "") + " " +
                               " ".join(r.get("options", [])), re.I)],
            "dg": None,
            "dgnow": None,
            "star": bool(r.get("reviewed")),
            "agree": 1,
            "flag": None,
        })

    data = {
        "version": VERSION,
        "built": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "examId": "cca-f",
        "exam": "CCA-F",
        "examName": "Claude Certified Architect (CCA-F)",
        "guide": "Stub build: the twelve samples from the exam guide, no more",
        "sections": build_sections(rows),
        "questions": questions,
        "concepts": {k: {"tier": 1} for k in AREA_TITLES},
        "glossary": {name: what for name, (_, what) in GLOSSARY.items()},
        "sources": {"CCA": "Anthropic exam guide samples"},
        "areaTitles": AREA_TITLES,
        "otherExams": [
            {"id": "saa-c03", "name": "AWS Solutions Architect Associate",
             "href": "../"},
        ],
        "diagrams": {},
        # No mock. The real paper's length, time and pass mark are not
        # something we have, and putting a made-up pass mark in front of
        # someone is worse than offering no mock at all.
        "paper": None,
    }

    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    kb = OUT.stat().st_size // 1024
    print(f"version {VERSION} built {data['built']}  —  STUB")
    print(f"  {len(questions)} questions, all from the exam guide samples")
    print(f"  {sum(len(s['rows']) for s in data['sections'])} recall rows "
          f"in {len(data['sections'])} sections")
    print(f"  {len(GLOSSARY)} glossary terms, no diagrams, no mock exam")
    print(f"  {OUT.name} {kb} KB")


if __name__ == "__main__":
    main()
