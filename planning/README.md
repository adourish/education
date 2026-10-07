# Planning

Working notes for the study app: what it does today, what the journeys through
it look like, and what is queued next.

These files are for people, not for the build. Nothing here is published to the
site, and no script reads them.

| File | What it holds |
|---|---|
| [features.md](features.md) | What the app does today, feature by feature |
| [user-journeys.md](user-journeys.md) | The paths a person takes through it, start to finish |
| [backlog.md](backlog.md) | What is queued, in the order it makes sense to do it |
| [design-multiple-exams.md](design-multiple-exams.md) | How several exams and several half-finished sets would work |

## How to use the backlog

Items are ordered so that each one can be finished and shipped on its own. An
item near the top is either small and useful, or something later items need.

An item says what the person gets, not what the code does. If an item cannot be
written that way it is probably two items, or housekeeping that belongs in a
commit message rather than here.

## A note on what gets written down

The app is one HTML file per exam with the questions baked in, and it keeps
everything in the browser's own storage. There is no account and no server.
That is deliberate and worth defending: it works on a phone with no signal, it
costs nothing to run, and nothing personal leaves the device.

The cost of it is that moving between devices is a deliberate act. That is why
export and import get as much attention here as the questions do.
