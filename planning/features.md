# What the app does today

Live at https://adourish.github.io/education/ · version 1.31.0

One HTML file per exam. The questions, the recall poster and the glossary are
baked into it, and a service worker keeps the page itself, so it installs to a
home screen and opens with no signal. Everything about your progress is kept in
the browser's own storage on that device. There is no account, no server and
nothing sent anywhere.

## The three tabs

| Tab | What it is for |
|---|---|
| Poster | The recall sheet. 303 rows in 22 sections, the thing to read before sleep |
| Practice | Questions, one at a time, with the answer and an explanation |
| Progress | How it is going, and the export and import box |

## Questions

- **1,799 questions** from several publishers, 614 of them human-reviewed
- **Filter by area** (networking, storage, security and so on) and by publisher
- **Spaced repetition.** A question answered right is pushed further out: 1, 3,
  7, 14 then 30 days. A question answered wrong comes back to the front
- **Drill my misses** — only the ones you got wrong
- **Mock exam** — 65 questions in 130 minutes, marked out of 1000, pass at 720,
  mixed across the four domains the way the real paper is
- **Confirm before moving on**, so a mis-tap does not count as an answer

## Help on a question

- **Explain the terms** — plain-English definitions of the AWS names in the
  question and all its options. 162 terms, about 5 attached to a typical
  question
- **Show the diagram** — a drawing of the arrangement the answer describes.
  82 shared pictures across 647 questions, drawn in whatever theme you have on
- **What they have now** — where the question describes a setup someone already
  has, a second drawing of that, so the answer reads as a before and an after.
  154 questions have both

## Keeping your place

- **Several half-finished sets are kept**, up to twelve. Starting a new one
  puts the old one aside rather than destroying it. **Forget this one** is the
  only thing that removes one, and it asks first
- Coming back offers every one of them, newest worked on first, each with when
  it was begun, when you last picked it up, how many times, and when you last
  worked on it. **Put this aside** drops one for good
- A set only counts once you have answered something in it, so changing the
  area filter does not leave a trail of sets nobody touched
- A resumed mock says how much time is left, and marks itself as it stands if
  the clock ran out while you were away

## Installing it

- **Add to Home screen** on a phone, and it opens like an app with no browser
  chrome around it
- It opens from its own cache, so it works with no signal once opened once
- A new version is fetched quietly in the background. When one is ready a bar
  offers **Update now** or **Not now**, and nothing changes until you say so,
  because being thrown out of a half-read question is worse than being ten
  minutes behind
- Each exam installs as itself, with its own name, icon and cache

## Runs

- Each go at a set of questions is scored and kept, by category
- A run is scored from its first answer, so the set in hand shows too, not just
  finished ones
- **Recent runs** lists the last five with what, when, which device and how many
  were right. Open one for the category breakdown; the full list expands
- A set still going carries **Carry on**, so it can be picked up from here
- Runs travel in the export and join by identity, so a phone run sits beside a
  laptop run

## More than one exam

- **Two exams**, each its own page: the AWS board, and a stub for the Claude
  Certified Architect exam
- Each keeps its own answers and its own half-finished sets, under its own name
  in the browser's storage. Neither can disturb the other
- Reading settings — theme, font, size, spacing, ruler — are shared, because
  they are about you rather than about an exam
- The footer of each page links the other one

## Settings

Built for reading comfort first, because that is the constraint that matters.

- **Themes** — match my device, light, dark, editor dark, editor light,
  solarized, terminal green, high contrast
- **Fonts** — Atkinson Hyperlegible, Lexend, the device's own, Verdana
- **Text size** — five steps
- **Line spacing** — normal or roomy
- **Width** — normal or wider
- **Bold** — normal or less bold
- **Reading ruler** — marks the line you are on with a bar down the left side.
  No background tint, because light on light is hard to read
- Never colour on its own. A diagram box carries its meaning in its shape as
  well, and nothing uses only a colour pair to tell you something

## Moving between devices

- **Export** writes a file covering **every exam** this browser has work for:
  each one's answers with the date each was given, the totals, every
  half-finished set and every run
- **Merge from a file**, drop one on the box, or paste one in
- **Import** merges rather than overwriting, exam by exam. Answers add up, and
  where two devices disagree about a question it goes on the revisit list
- **Half-finished sets merge by identity, so nothing is replaced.** This
  device's own set survives, the file's sets arrive alongside it, and only the
  same set carried on in both places is reconciled, the later copy winning
- An exam this device has no page for keeps its answers anyway, and the report
  says so
- Files written by the one-exam version still import

## What it does not do yet

- **No home page.** The second exam is reachable from a footer link, not from a
  screen that lists what there is
- **The second exam is a stub** — twelve questions from the official guide's
  samples. Enough to prove two exams stay apart, nowhere near enough to study
- **No mock exam for the second exam.** The real paper's length, time and pass
  mark are not something we have, and a made-up pass mark would teach the wrong
  target, so no mock is offered there
- **Export always covers everything.** There is no "just this exam" option yet
- **Half the explanations are cut off.** There is a 900-character cap in the
  parser and 518 of 1,020 explanations hit it, nearly all of them stopping
  mid-sentence. The part that gets cut is usually the section on why the other
  options are wrong
- **The before-pictures have not been reviewed** the way the answer pictures
  have. They are matched from the question's own wording, which is looser
