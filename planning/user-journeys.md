# User journeys

What a person actually does, start to finish. Journeys 1 to 4 work today.
Journeys 5 to 8 are what several exams and several sets would add, and are the
thing to build against.

---

## 1. Twenty minutes on the train

Works today.

1. Open the page. It loads from the phone's cache, with or without signal
2. Practice tab. Area set to networking, because that is the weak one
3. Start. Read, pick, confirm, read the answer
4. On a question with unfamiliar names, tap **Explain the terms**
5. On a question about an arrangement, tap **Show the diagram**
6. Train arrives. Lock the phone mid-question

**What matters:** nothing is lost by walking away, and no step needs signal.

---

## 2. Coming back to it that evening

Works today.

1. Open the page
2. A banner: *You were 8 of 71 through Networking, a moment ago. Started today
   at 13:08. Picked up again today at 13:42, 2 times in all. Last worked on
   today at 14:18*
3. Carry on, and it resumes at question 9 of the same 71

**What matters:** the dates are there so you can tell a set you left an hour
ago from one you abandoned a fortnight ago. One of those is worth resuming.

---

## 3. Sitting a mock

Works today.

1. Practice tab, **Sit a mock exam**. It says what it is: 65 questions, 130
   minutes, pass at 720
2. Confirm. The clock starts and the usual help is withheld
3. Answer, or skip and come back
4. Finish, or let the time run out. Marked out of 1000, with a breakdown by
   domain

**What matters:** it is a dry run of the real thing, so the help goes away.

---

## 4. Moving a week's work to the laptop

Works today.

1. On the phone, Progress tab, **Export progress**. A block of text appears
2. Copy it. Send it to yourself however is easiest
3. On the laptop, Progress tab, paste it into the box, **Merge in the box below**
4. It reports what happened: answers added, questions this device had not seen,
   and any the two devices disagreed about
5. The set you were partway through is offered on the practice page

**What matters:** merging, not overwriting. The laptop may have answers the
phone never saw, and they must survive.

**Where it falls down today:** if the laptop is also partway through a set, it
asks you to pick one and throws the other away.

---

## 5. Studying for a second exam

Does not work yet. See [design-multiple-exams.md](design-multiple-exams.md).

1. Open the page. A home screen lists the exams you have material for, each
   with how far through you are
2. Pick AWS Solutions Architect Associate. Practise for twenty minutes
3. Go back to the home screen. Pick the Claude Certified Architect exam
4. Practise that. The theme, font and reading ruler are as you set them, because
   those are about you and not about the exam
5. Your AWS progress is untouched. Neither exam can affect the other's answers

**What matters:** one person, several exams, no bleed between them, and the
reading settings carry across.

---

## 6. Two half-finished sets at once

Does not work yet.

1. You are 8 of 71 through a networking set
2. You want a quick ten on storage, without losing the networking one
3. Start a storage set. The networking one is put aside, not thrown away
4. Open the page the next day. A list:

```
Pick up where you left off

  Storage · 3 of 20                        AWS SAA-C03
  started yesterday 20:14 · last worked on yesterday 20:22

  Networking · 8 of 71                     AWS SAA-C03
  started yesterday 13:08 · picked up 13:42, 2 times · last worked on 14:18

  Everything · 4 of 12                     Claude Certified Architect
  started yesterday 09:12 · last worked on yesterday 09:20
```

5. Carry on with any of them. Put aside any you are done with

**What matters:** starting something new never destroys something unfinished,
and the list is honest about how stale each one is.

**The awkward case:** a mock exam has a clock. If you leave one for a day,
resuming is not a real mock any more. The row says how much time is left, and
if the clock ran out while you were away it offers to mark it as it stands
rather than pretending.

---

## 7. Bringing in several runs from another device

Does not work yet. This is the journey the question was about.

You have been working on the phone. The laptop has its own history and is
itself partway through a mock. You want everything in one place, losing nothing.

1. On the phone, **Export progress**. One file, covering every exam, with every
   half-finished set in it
2. On the laptop, paste it and merge
3. It reports what happened, per exam:

```
Merged two exams.

AWS Solutions Architect Associate
  312 answers added. 48 questions this device had not seen.
  6 where the two disagreed are on the revisit list.
  2 sets in progress came across. You now have 3.

Claude Certified Architect
  18 answers added.
  No page for this exam on this device yet, so the answers are
  kept and will show up when there is one.
```

4. The laptop's own half-finished mock is still there, alongside the two that
   came in. Nothing was replaced and nothing was silently dropped
5. The resume list now shows all three, newest first

**What matters:** three things, and they are the whole point of the journey.

- Answers merge per exam, and a disagreement is surfaced rather than resolved
  quietly
- Sets merge by identity, not by slot. The same set carried on in two places
  keeps whichever copy was worked on later
- An exam the device has no page for does not lose its answers

---

## 8. Exporting one exam on its own

Does not work yet.

Sometimes you only want to move the AWS work, for instance to hand it to
someone else studying the same exam without passing on everything else.

1. Progress tab. **Export progress** gives everything by default, and says so
2. **Just this exam** gives only the one you are looking at
3. Either file imports the same way. The other end works out what is in it

**What matters:** the person reading the file can tell what is in it without
being told.

---

## Things that must stay true in every journey

These are the standing constraints, not nice-to-haves.

| Constraint | Why |
|---|---|
| Works with no signal once loaded | Most study happens on a phone, in transit |
| Nothing leaves the device unless you export it | No account, no server, nothing to trust |
| Import merges, never overwrites | The other device may hold answers this one has never seen |
| Nothing is lost by closing the tab | Study time is five minutes at a time |
| Never colour on its own to tell you something | Protanopia. Shape, position or words as well |
| Reading settings are about the person, not the exam | They should never need setting twice |
| No uppercase runs, no italics, generous spacing | Dyslexia. This is a reading tool before it is anything else |
