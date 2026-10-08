# Backlog

Ordered so each item can be finished and shipped on its own. Near the top means
either small and useful, or needed by something below it.

Sizes are rough: **small** is an evening, **medium** a day, **large** more than
that or carrying real risk.

Current version: **1.31.0**

---

## Next

### 1. Lift the 900-character cap on explanations
**small** · the biggest single improvement left, and it affects half the bank

518 of 1,020 explanations are cut off at exactly 900 characters, and 514 of
those stop mid-sentence. The cap is at `questions/parse-certempire.py:98`
(`why[:900]`). The part that gets cut is almost always the section at the end
on why the other options are wrong, which is the most useful part.

Found while looking at question ce-520, where the reasoning ends at "D. AWS
Site-to-Site VPN e".

**Blocked on you:** it needs the original source files, which are the
watermarked ones kept locally and never committed. Point me at them and it is
an evening: raise the cap, re-parse, rebuild, check the page is still a sane
size.

### 2. Refuse a broken pattern in the glossary, the way the diagrams do
**small** · a bug that has now happened three times

A pattern written without the `r` prefix turns `\b` into a backspace
character. It still compiles, still runs, and silently matches nothing. The
diagram library refuses to load when that happens; the glossary does not, and
has been bitten twice, most recently the `immutable` term, which matched zero
questions where it should have matched three.

Both times it was caught only by checking the match count by hand. The same
guard belongs in `questions/glossary.py`: no control character in any pattern,
and no doubled backslash either.

### 3. A home page listing exams and open sets
**medium**

Small page, no question data of its own. Lists the exams there is material for,
how far through each one is, and every open set across all of them.

Now that each exam installs separately this also answers "which one am I
installing", and it is the only way to the second exam other than a footer
link.

### 4. Export one exam on its own
**small**

Export covers every exam, which is right as the default. Sometimes you want
only one, for instance to hand the AWS work to someone studying the same exam.
The import side already copes with either, so this is a second button and
nothing more.

### 5. Stop committing the built pages
**small** · housekeeping, but it costs time on every single change

`app.html`, `app-data.json` and the two recall-board files are build output and
are committed. Only `docs/` has to be in git, because that is what Pages
serves. Every squash merge therefore collides with the next branch on files
nobody edits by hand: every pull request today needed a merge and a rebuild
before it would go in.

Keep `docs/`, ignore the rest, and have the build refuse if `docs/` is stale.

---

## Waiting on something

### 6. A real question bank for the Claude Certified Architect exam
**large** · blocked on material and on a decision

Twelve questions, all from the official guide's samples. The page is built,
published, installs as itself and says it is a stub. Enough to prove two exams
stay apart; nowhere near enough to study from.

Also needs a decision: that guide is marked confidential in its footer, this
repository is public, and the samples are served at a public URL. Removing them
is one line in `site/build-site.py` plus the questions file.

### 7. Review the before-pictures
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
| Show the revisit list as its own drill | small | The list exists; there is no way to work through it |
| Keep the area and publisher filter between visits | small | It resets, which is mildly annoying |
| Runs by week, not only a list | small | "Am I getting better" is the question a list of runs nearly answers |
| Say which publisher a question came from on the card | small | Useful when one publisher's answer looks wrong |
| A way to flag a question as wrong while practising | small | Today a correction needs a code change |
| Steady the one flaky test | small | `f2-sets` misses its first question about one run in three, on timing |
| A poster worth reading for the second exam | medium | Eight stub rows today, not a syllabus |
| Explanations that fit the glossary's voice | large | Publisher wording is uneven and sometimes wrong |

---

## Done

### 1.31.0 — installable and offline
| Item |
|---|
| A service worker: real install, reliable offline, update offered rather than forced |
| Each exam installs as itself, with its own manifest, icon, worker and cache |
| The worker's behaviour tested on eleven counts against a stubbed browser |

### 1.30.0 — runs that read properly
| Item |
|---|
| A run row says one thing per line, instead of two pairs of numbers meaning different things |
| The position is read from the set, so a row cannot go stale |
| Carry on from the progress page |
| Elastic Beanstalk deployment policies, traffic splitting, immutable, blue/green |

### 1.28.0 to 1.29.1 — runs, and a button that lied
| Item |
|---|
| A score kept for each run, by category, updated from the first answer |
| In-progress sets shown, including ones begun before runs were recorded |
| "Put this aside" deleted a set; now "Forget this one", and it asks first |
| The progress page folds, with the export at the top |
| Merge from a file, or drop one on the box |
| A file holding only a half-finished set now imports |
| Merging the same file twice no longer double-counts its undated answers |

### 1.27.0 — smaller pictures, device names
| Item |
|---|
| Diagrams drawn at their own size: one filled a phone screen, now 284px of it |
| A set records which device began it |
| Each exam names itself in the heading, tab title and export filename |
| REST against HTTP APIs and what a JWT check needs; warm pool |

### 1.25.0 to 1.26.0 — more than one exam
| Item |
|---|
| Per-exam progress, with the old key migrated and left in place |
| Several half-finished sets, each with an id, and a chooser |
| Import that merges sets by identity instead of replacing one |
| Export covering every exam, and older files still read |
| Reading settings shared across exams rather than held per exam |
| A second exam, stubbed, proving the two stay apart |
| Direct Connect against PrivateLink, with the trap named |

### 1.24.0 — the diagram review
| Item |
|---|
| Pictures matched on what the answer does, not which services it names |
| 14 factual errors corrected in the drawings |
| 20 new pictures; 72 of 73 wrong attachments fixed |
| Before and after pictures on a question |

### Earlier
| Item | Version |
|---|---|
| Resume a half-finished set, with dates | 1.22.0 |
| A set travels in the export | 1.22.0 |
| Reading ruler without a background tint | 1.19.0 |
| Bold that is not so heavy | 1.19.0 |
| Confirm before moving on | 1.18.2 |
