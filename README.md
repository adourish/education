# education

Study notes, exam preparation material, and course work.

Notes are written in **memorization format** — cue-and-answer tables, numbers
tables, mnemonics, and scenario triggers — rather than as prose. The aim is
recall under time pressure, not first-time learning.

## Contents

| Path | Subject |
|---|---|
| `aws/solutions-architect-associate/` | AWS Certified Solutions Architect – Associate (SAA-C03) |
| `anthropic/claude-certified-architect/` | Claude Certified Architect (CCA-F) — exam-guide samples only so far |
| `site/` | Build script for the published study app |
| `planning/` | What the app does, the journeys through it, and the backlog |

## Layout of a subject folder

```
<subject>/
├── notes/        numbered markdown files, drilled in order
├── pdf/          build script, print stylesheet, and the generated PDF
└── README.md     what the subject covers and how to study it
```

## Branches

| Branch | Purpose | Direct commits |
|---|---|---|
| `main` | Stable, reviewed material | No |
| `dev` | Integration branch | No |
| `feature/*` | New notes and edits — branch from `dev`, pull request back to `dev` | Yes |

Work happens on a `feature/*` branch and reaches `dev` through a pull request.
