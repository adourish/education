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

### 2. Move the exam's shape fully into its data file
**small** · mostly done

The mock's length, time, pass mark and domain mix already live in each exam's
data file, and an exam with no paper simply offers no mock. What is left is the
remaining SAA-C03 wording in the code, such as the footer line that rewrites
"Exam guide" to "AWS exam guide".

### 3. A home page listing exams and open sets
**medium** · journey 5

Small page, no question data of its own. Lists the exams there is material for,
how far through each one is, and every open set across all of them. Becomes the
natural home for the export button.

### 4. Export one exam on its own
**small**

Export covers every exam, which is right as the default. Sometimes you want
only one, for instance to hand the AWS work to someone studying the same exam.
The import side already copes with either, so this is a second button and
nothing more.

---

## Waiting on something

### 5. A real question bank for the Claude Certified Architect exam
**large** · blocked on material and on a decision

Twelve questions today, all from the official guide's samples. The page is
built and published and says it is a stub. Enough to prove two exams stay
apart; nowhere near enough to study from.

Also needs a decision: that guide is marked confidential in its footer, this
repository is public, and the samples are now served at a public URL. Removing
them is one line in `site/build-site.py` plus the questions file.

### 6. Review the before-pictures
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
| Say which publisher a question came from on the card | small | Useful when one publisher's answer looks wrong |
| A way to flag a question as wrong while practising | small | Today a correction needs a code change |
| Keep the area and publisher filter between visits | small | It resets, which is mildly annoying |
| A poster worth reading for the second exam | medium | Eight stub rows today, not a syllabus |
| Show the revisit list as its own drill | small | The list exists; there is no way to work through it |
| Explanations that fit the glossary's voice | large | Publisher wording is uneven and sometimes wrong |

---

## Done recently

| Item | Version |
|---|---|
| Per-exam progress, with the old key migrated and left in place | 1.25.0 |
| Several half-finished sets, each with an id, and a chooser | 1.25.0 |
| Import that merges sets by identity instead of replacing one | 1.25.0 |
| Export covering every exam, and older files still read | 1.25.0 |
| Reading settings shared across exams rather than held per exam | 1.25.0 |
| A second exam, stubbed, proving the two stay apart | 1.25.0 |
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
