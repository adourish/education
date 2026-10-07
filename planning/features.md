# What the app does today

Live at https://adourish.github.io/education/ · version 1.25.0

One HTML file. The questions, the recall poster and the glossary are baked into
it, so it works with no signal once loaded. Everything about your progress is
kept in the browser's own storage on that device. There is no account, no
server and nothing sent anywhere.

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

- **One half-finished set is kept.** Close the tab, come back, and it offers to
  carry on where you were
- It shows when the set was begun, when you last picked it up, how many times,
  and when you last worked on it

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

- **Export** writes a single block of text: every answer with the date it was
  given, the totals, and the set you are partway through
- **Import** merges it in rather than overwriting. Answers add up. Where the
  two devices disagree about a question, it goes on the revisit list
- The half-finished set comes across too, but if this device is already partway
  through one, it asks before replacing it

## What it does not do yet

- **Only one exam.** The storage key, the mock exam's domain mix and the export
  file are all specific to AWS SAA-C03
- **Only one half-finished set.** Starting a second one throws the first away
- **Import replaces a set rather than keeping both**
- **Half the explanations are cut off.** There is a 900-character cap in the
  parser and 518 of 1,020 explanations hit it, nearly all of them stopping
  mid-sentence. The part that gets cut is usually the section on why the other
  options are wrong
- **The before-pictures have not been reviewed** the way the answer pictures
  have. They are matched from the question's own wording, which is looser
