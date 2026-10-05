# AWS Certified Solutions Architect – Associate (SAA-C03)
## Memorization Notes — Index

These notes are built for **recall under time pressure**, not for first-time learning.
Every page uses one of four shapes:

| Shape | What it looks like | Use it for |
|---|---|---|
| **Cue → Answer** | A two-column table. Cover the right column. | Facts and definitions |
| **Numbers table** | A limit, size, or duration per row | Hard numbers the exam asks directly |
| **Mnemonic** | A word or sentence that unpacks into a list | Lists you must produce from nothing |
| **Trigger** | "If the question says X → answer Y" | Scenario questions (most of the exam) |

### How to drill these

1. **Day 1–2:** Read `01-numbers-and-limits.md` and `02-mnemonics.md` out loud. These are pure rote. Nothing else on this list sticks until the numbers do.
2. **Day 3–7:** One service page per day (`03` through `09`). Cover the answer column, say the answer, uncover, check.
3. **Day 8–9:** `10-decision-triggers.md`. This page is worth the most marks per minute of study. The exam is mostly scenario questions and this page is the scenario-to-service map.
4. **Day 10 onward:** `11-rapid-fire.md` every morning. 150 one-liners, about 12 minutes. If you miss one, go back to its service page.
5. Read `99-review-of-original-notes.md` once, early. It lists the facts in the older slide decks that are **now wrong** — unlearning a stale number is harder than learning a new one, so do it before you drill.

### Exam shape (SAA-C03)

| Item | Value |
|---|---|
| Questions | 65 (50 scored, 15 unscored) |
| Time | 130 minutes |
| Passing score | 720 / 1000 |
| Question types | Multiple choice (1 of 4), multiple response (2+ of 5+) |
| Cost | 150 USD |

### Scored domains — know the weights, they tell you where to spend study time

| Domain | Weight | Mnemonic hook |
|---|---|---|
| 1. Design Secure Architectures | 30% | **S**ecure |
| 2. Design Resilient Architectures | 26% | **R**esilient |
| 3. Design High-Performing Architectures | 24% | **H**igh-performing |
| 4. Design Cost-Optimized Architectures | 20% | **C**ost |

Mnemonic: **"SRHC" — Security Rules, Hardware Costs."**
Security is the biggest single slice. When two answers both work, the more secure one usually wins.

### The six pillars of the Well-Architected Framework

Mnemonic: **"COPS RS"** — or remember the sentence **"Our Six Pillars Really Count, Seriously."**

| Pillar | One-line test |
|---|---|
| **O**perational Excellence | Can we run and improve it? |
| **S**ecurity | Who can touch what, and is it logged? |
| **R**eliability | Does it survive a failure? |
| **P**erformance Efficiency | Is it the right-sized, right-shaped resource? |
| **C**ost Optimization | Are we paying for idle? |
| **S**ustainability | Are we wasting energy? (added 2021 — newer than the old slide decks) |

### File map

| File | Contents |
|---|---|
| `01-numbers-and-limits.md` | Every number worth memorizing, in one place |
| `02-mnemonics.md` | All the list-recall tricks |
| `03-compute.md` | EC2, Auto Scaling, ELB, Lambda, containers, Beanstalk |
| `04-storage.md` | S3, EBS, EFS, FSx, Glacier, Storage Gateway, Snow family |
| `05-databases.md` | RDS, Aurora, DynamoDB, ElastiCache, Redshift |
| `06-networking.md` | VPC, subnets, SG vs NACL, Route 53, CloudFront, Direct Connect |
| `07-security-identity.md` | IAM, STS, KMS, Secrets Manager, WAF, Shield, GuardDuty |
| `08-integration-analytics.md` | SQS, SNS, EventBridge, Step Functions, Kinesis, Athena, EMR, Glue |
| `09-monitoring-governance.md` | CloudWatch, CloudTrail, Config, CloudFormation, Organizations |
| `10-decision-triggers.md` | "If the question says X → answer Y" |
| `11-rapid-fire.md` | 150 one-line flashcards |
| `99-review-of-original-notes.md` | What the older slide decks got wrong, and what they are missing |
