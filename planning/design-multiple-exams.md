# Several exams, several half-finished sets

How it would work, and why it is shaped this way.

---

## What is single today

Three things, and each one has to change.

| Thing | Today | Where |
|---|---|---|
| Progress | One key, named after the one exam | `saa-c03-recall-board/v1` |
| A half-finished set | Exactly one slot. A new set overwrites the old | `saa-c03-recall-board/v1/session` |
| The export file | No exam identifier, just a display name | `app: "SAA-C03 Recall Board"` |

The mock exam's domain mix (30/26/24/20) is also specific to SAA-C03 and
currently fixed in the code.

---

## The one change that unlocks the rest

**Give a half-finished set an identity.**

Today a set is a slot. Two sets can only replace each other, because there is
nothing to tell them apart. Give each one a short random id when it starts and
three things become possible at once:

1. Several can sit side by side, because they no longer compete for the slot
2. The same set exported and brought back merges instead of appearing twice
3. When two devices have both carried on the same set, the later one can win,
   because we can tell it is the same set

Everything else in this document follows from that. It is worth doing first.

---

## Storage layout

```
recall/v2                          which exams are known, and which was last open
recall/v2/<exam>/progress          one exam's answers, unchanged in shape
recall/v2/<exam>/sessions          a list of half-finished sets, each with an id
recall/v2/settings                 theme, font, size, spacing, ruler
```

Two decisions in there worth stating plainly.

**Progress keeps its current shape.** It is already a lump plus a log of dated
answers, and that works. It just moves under an exam. No migration of the
answers themselves, only of where they live.

**Settings are shared across exams, not per exam.** The theme, the font, the
text size and the reading ruler are about the person. Having to set them again
for a second exam would be a small insult every time.

### A session

```
{
  id:       "k3f9qp",          short, random, made when the set starts
  exam:     "saa-c03",
  kind:     "practice" | "mock" | "drill",
  label:    "Networking",      what to call it in the list
  started:  "2026-10-07T13:08",
  resumed:  "2026-10-07T13:42",
  resumes:  2,
  at:       "2026-10-07T14:18", last worked on
  ids:      [...],             the question ids, in order
  qi:       8,                 how far through
  done:     [...],
  area:     "networking",
  src:      "all",
  mock:     { ends: "...", given: {...} }   only for a mock
}
```

The id is the only new field. Everything else is what a session already holds.

---

## Migration

There is real progress in the existing key — over a thousand answers — and
losing it would be unforgivable. So:

1. On first load of the new version, if `recall/v2` is absent and
   `saa-c03-recall-board/v1` is present, copy it to
   `recall/v2/saa-c03/progress`
2. Turn its single session into a one-item list, giving it a generated id
3. **Leave the old key where it is.** It costs a little space and buys a way
   back if something is wrong. Remove it a few versions later, not now
4. If both exist, the new one wins and the old one is ignored

---

## The export file

```json
{
  "app": "Recall Board",
  "format": 2,
  "exported": "2026-10-07T14:18:00Z",

  "answers": {
    "saa-c03": { "total": 1312, "right": 964, "note": "..." },
    "cca-f":   { "total": 18,   "right": 11,  "note": "..." }
  },

  "exams": {
    "saa-c03": {
      "name": "AWS Solutions Architect Associate (SAA-C03)",
      "dataVersion": "1.8.0",
      "progress": { },
      "sessions": [ { }, { } ]
    },
    "cca-f": { }
  }
}
```

The `answers` block stays at the top as a plain reading of what is below, so
the file explains itself to anyone who opens it. That is already the habit and
it is a good one.

### Reading an older file

A file with no `format` key is an SAA-C03 file, because every file written so
far is. Wrap it and carry on:

```
exams: { "saa-c03": { progress: <the file's progress>,
                      sessions: [ <the file's session> ] } }
```

A session arriving without an id gets one generated at import. This matters:
there are already exported files saved, and they must keep working.

---

## Import: the merge rules

This is the part the question was really about. Nothing is replaced and nothing
is dropped without saying so.

### Answers, per exam

As today. Answers add up, the dated log is combined, and a question the two
devices disagree about goes on the revisit list rather than one answer quietly
winning.

### Half-finished sets, by id

| Case | What happens |
|---|---|
| In the file only | Brought in |
| On this device only | Left alone |
| In both, same id | Keep whichever was worked on later. The other is discarded, because it is the same set and one copy is behind |
| In both, different ids | Keep both |

The confirm box that currently asks "replace it with the one from the file?"
disappears. There is no longer a conflict to settle by choosing, because both
can exist.

### An exam this device has no page for

Merge the answers and keep them. Say so rather than hiding it:

> No page for this exam on this device yet, so the answers are kept and will
> show up when there is one.

Throwing them away would be the wrong call. The person may well open that exam's
page tomorrow.

### What the report says

Per exam, in plain words, as in journey 7 of
[user-journeys.md](user-journeys.md). The report is the only evidence the merge
did what was wanted, so it should be specific rather than reassuring.

---

## How many pages

Two ways to go.

**One page per exam, plus a small home page.** What exists now, extended.

- The download stays the size it is today. Nobody pays for an exam they are not
  studying
- Browser storage is shared across all pages on the site, so the home page can
  list every exam's progress and every open set even though each exam's
  questions live in its own file
- The home page is the natural place for the cross-exam resume list and the one
  export button

**One page holding every exam.** Simpler to move around in, but the download
grows with each exam added and everyone carries all of it. At 2.8 MB each that
gets heavy fast.

**Recommendation: one page per exam, plus a home page.** The deciding factor is
the phone on a train with no signal. Doubling the download to put a second exam
in front of someone who is studying the first is a bad trade.

---

## Per-exam settings that are not settings

Some things look like settings but belong to the exam, and have to move out of
the code and into each exam's data file:

| Thing | SAA-C03 today |
|---|---|
| Mock length | 65 questions |
| Mock time | 130 minutes |
| Pass mark | 720 of 1000 |
| Domain mix | 30 / 26 / 24 / 20 |
| Domain names | the four SAA-C03 domains |
| Areas | networking, storage, security and the rest |

The Claude Certified Architect exam has a different shape, so none of these can
stay fixed.

---

## Order to build it in

Each step is shippable on its own and useful before the next one lands.

1. **Give a session an id**, still one at a time. Invisible to the person, and
   it is the thing everything else needs
2. **Move storage to `recall/v2/<exam>/`**, with the migration above. Still one
   exam, so again nothing visible changes. This is the risky step, so it goes
   early and on its own, while there is only one exam's data to get wrong
3. **Sessions become a list**, with the resume chooser. Now visible: several
   half-finished sets
4. **Export format 2, and an import that merges sessions.** Journeys 7 and 8
   start working
5. **Move the mock shape and domains into the data file.** Still one exam, but
   nothing is exam-specific in the code any more
6. **A home page** listing exams and open sets
7. **Add the second exam** once it has enough questions to be worth opening

Steps 1, 2 and 5 change nothing a person can see. That is the point: the
visible change in step 3 lands on foundations that have already been shipped
and used.

---

## The thing standing in the way

The second exam is not ready. The Claude Certified Architect folder has **12
questions**, all from the official exam guide's samples. That is enough to prove
the machinery works end to end and not enough to study from.

Also worth remembering: that guide is marked confidential in its footer and
this repository is public. The questions parsed from it are in the repository
now. Worth a decision before the exam gets a page of its own and becomes
something people are pointed at.

So steps 1 to 6 are all worth doing regardless, and they stand on their own:
they give several half-finished sets and a merge that loses nothing, which are
useful with one exam. Step 7 waits on material.
