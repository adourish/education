# Backlog

Ordered so each item can be finished and shipped on its own. Near the top means
either small and useful, or needed by something below it.

Sizes are rough: **small** is an evening, **medium** a day, **large** more than
that or carrying real risk.

---

## Next

### 1. Lift the 900-character cap on explanations
**small** · a known bug, and it affects half the bank

518 of 1,020 explanations are cut off at exactly 900 characters, and 514 of
those stop mid-sentence. The cap is at `questions/parse-certempire.py:98`
(`why[:900]`). The part that gets cut is almost always the section at the end
on why the other options are wrong, which is the most useful part.

Found while looking at question ce-520, where the reasoning ends at "D. AWS
Site-to-Site VPN e".

Needs the original source files, which are the watermarked ones kept locally
and never committed. Raise the cap, re-parse, rebuild, and check the page size
is still sane.

### 2. Give a half-finished set an id
**small** · nothing visible changes, and everything below needs it

A short random id, made when a set starts. Still one set at a time. See
[design-multiple-exams.md](design-multiple-exams.md).

### 3. Move storage under an exam
**medium** · the risky one, so do it early and alone

`recall/v2/<exam>/progress` and `recall/v2/settings`, with the migration from
the existing key. Still one exam, so nothing visible changes. Over a thousand
real answers are in that key, so the old one stays in place as a way back.

---

## Then

### 4. Several half-finished sets, with a chooser
**medium** · journey 6

Sessions become a list. Starting a new set puts the old one aside instead of
destroying it. A resume list, newest first, with the dates each row already
carries, and a way to put one aside for good.

Includes the awkward case: a mock exam has a clock, so a resumed mock says how
much time is left, and offers to mark it as it stands if the clock ran out
while you were away.

### 5. Export format 2, and an import that merges sets
**medium** · journeys 7 and 8

Several exams and several sets in one file. Sets merge by id, so nothing is
replaced. Older files keep working. The import report says, per exam, what
actually happened.

Also: export everything by default, with "just this exam" as the other option.

### 6. Move the exam's shape into its data file
**small** · nothing visible changes

Mock length, mock time, pass mark, domain mix, domain names and areas all come
out of the code and into each exam's data file. After this nothing in the code
is specific to SAA-C03.

### 7. A home page listing exams and open sets
**medium** · journey 5

Small page, no question data of its own. Lists the exams there is material for,
how far through each one is, and every open set across all of them. Becomes the
natural home for the export button.

---

## Waiting on something

### 8. A real question bank for the Claude Certified Architect exam
**large** · blocked on material and on a decision

Twelve questions today, all from the official guide's samples. Enough to prove
the machinery, not enough to study from.

Also needs a decision first: that guide is marked confidential in its footer
and this repository is public. The parsed questions are in the repository now.

### 9. Review the before-pictures
**medium** · worth doing, not urgent

The answer pictures were reviewed against 531 sampled judgements and 72 wrong
attachments were fixed. The before-pictures were not: they are matched from the
question's own wording, which is looser, and they went in after that review.

Spot-checking suggests roughly four in five read correctly. The allowlist of
arrangements that may stand for "what they have now" keeps out the worst of it,
but the same thorough pass would settle it.

---

## Smaller things

| Item | Size | Note |
|---|---|---|
| Per-exam poster, not just the SAA-C03 recall sheet | medium | Follows item 6 |
| Say which publisher a question came from on the card | small | Useful when one publisher's answer looks wrong |
| A way to flag a question as wrong while practising | small | Today a correction needs a code change |
| Keep the area and publisher filter between visits | small | It resets, which is mildly annoying |
| Show the revisit list as its own drill | small | The list exists; there is no way to work through it |
| Explanations that fit the glossary's voice | large | Publisher wording is uneven and sometimes wrong |

---

## Done recently

| Item | Version |
|---|---|
| Direct Connect against PrivateLink in the glossary, with the trap named | 1.25.0 |
| Added Client VPN; fixed `AWS CLI` matching "AWS Client VPN" | 1.25.0 |
| Pictures matched on what the answer does, not which services it names | 1.24.0 |
| 14 factual errors corrected in the drawings | 1.24.0 |
| 20 new pictures; 72 of 73 wrong attachments fixed | 1.24.0 |
| Before and after pictures on a question | 1.24.0 |
| Resume a half-finished set, with dates | 1.22.0 |
| A set travels in the export | 1.22.0 |
| Reading ruler without a background tint | 1.19.0 |
| Bold that is not so heavy | 1.19.0 |
| Confirm before moving on | 1.18.2 |
