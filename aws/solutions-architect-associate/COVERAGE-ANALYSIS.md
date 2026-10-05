# Coverage analysis — what is current, what is missing, what is probably not worth your time

Checked on **5 October 2026** against the official AWS exam guide, downloaded that day.

---

## 1. Which exam are you actually sitting?

**SAA-C03, exam guide version 1.1.** Nothing newer exists.

This matters because searching for "AWS Solutions Architect 2026" turns up several
confident-looking blog posts claiming **SAA-C04 was released in March 2024** and is the
current version. **That is wrong.** Those pages are search-engine filler. The evidence:

| Source | What it says |
|---|---|
| `aws.amazon.com/certification/certified-solutions-architect-associate/` | Links to the **SAA-C03** exam guide |
| The exam guide PDF itself | Header on every page reads **"Version 1.1 SAA-C03"** |
| The older guide, same URL pattern | **"Version 1.0 SAA-C03"** |

So the only real change is **version 1.0 → version 1.1 of the same exam**. If a study
site tells you the exam code changed, stop using that site.

### Exam shape, from the guide

| Item | Value |
|---|---|
| Questions | 65 — **50 scored, 15 unscored** |
| Time | 130 minutes |
| Pass mark | 720 / 1000 |
| Question types | Multiple choice (1 of 4), multiple response (2+ of 5+) |
| Unanswered | Scored as incorrect — **there is no penalty for guessing, so never leave one blank** |

| Domain | Weight |
|---|---|
| Design Secure Architectures | 30% |
| Design Resilient Architectures | 26% |
| Design High-Performing Architectures | 24% |
| Design Cost-Optimized Architectures | 20% |

---

## 2. What changed between guide v1.0 and v1.1

I diffed the in-scope service lists in both PDFs. Five changes, and only one needs you to
do anything.

| Change | What it means |
|---|---|
| **AWS Single Sign-On → AWS IAM Identity Center** | A rename. Notes already use the new name. |
| **AWS Personal Health Dashboard → AWS Health Dashboard** | A rename. Already correct. |
| **AWS VPN → AWS Client VPN + AWS Site-to-Site VPN** | Split into two named services. Both are covered. |
| **AWS Server Migration Service — removed** | Superseded by Application Migration Service (MGN). Notes use MGN. |
| **Amazon Timestream — removed from in-scope** | ⚠️ **The one to act on.** |

**On Timestream:** it was dropped from the in-scope list and was *not* moved to the
out-of-scope list — it simply vanished. It is still a real service and "time series
database" is still a reasonable thing to recognise, so I have kept one line about it, but
do not spend study time there. It is now the lowest priority item in the notes.

---

## 3. Are we missing anything that will be on the test?

I checked all 130 in-scope services from the guide against the notes and the poster.
**19 were not mentioned anywhere.** I have now added the ones that can plausibly carry a
question, and consciously left the rest as recognition-only.

### Added, because these genuinely get asked

| Service | Why it earns a place |
|---|---|
| **AWS Directory Service** | FSx for Windows and WorkSpaces questions depend on it. A real gap. |
| **Migration Hub + Application Discovery Service** | Migration scenarios name them directly. |
| **AWS License Manager** | Turns up in BYOL and Dedicated Host cost questions. |
| **AWS Well-Architected Tool** | The framework is the exam's stated basis. |
| **Managed Grafana / Managed Service for Prometheus** | The modern answer to "managed observability". |
| **AWS X-Ray** | "Trace a request across microservices". |
| **Fault Injection Simulator** | Resilience-testing questions. |
| **Kinesis Video Streams** | Completes the Kinesis family, which is heavily asked. |

### Added as recognition only — know the one-line purpose, nothing more

AppFlow, Data Exchange, Pinpoint, Kendra, Proton, Serverless Application Repository,
ECS Anywhere, EKS Anywhere, EKS Distro, AWS Management Console.

These are on the in-scope list but are almost never the correct answer. Knowing what they
are is enough to eliminate them as distractors, which is all they are usually there for.

---

## 4. What is probably *not* worth your time

This is counted, not guessed. I tagged all **522 questions** in the question bank against
69 concepts and ranked them. Full table in `questions/yield-report.md`.

### The 14 concepts that dominate

| Concept | Questions | Share |
|---|---:|---:|
| ALB vs NLB | 56 | 10.7% |
| Auto Scaling | 52 | 10.0% |
| Lambda | 51 | 9.8% |
| DynamoDB | 30 | 5.7% |
| CloudFront | 29 | 5.6% |
| Aurora | 29 | 5.6% |
| S3 storage classes / lifecycle | 27 | 5.2% |
| Containers (ECS/EKS/Fargate) | 25 | 4.8% |
| API Gateway | 24 | 4.6% |
| Organizations / SCPs | 24 | 4.6% |
| RDS Multi-AZ | 23 | 4.4% |
| SQS | 23 | 4.4% |
| VPC endpoints / PrivateLink | 22 | 4.2% |
| IAM roles / instance profiles | 21 | 4.0% |

**If you are short on time, these fourteen are the exam.** Together they touch roughly
four questions in five.

### Thin in the bank — do not drop them, but do not lead with them

CloudHSM (0 questions), Trusted Advisor (1), OpenSearch (1), DynamoDB Global Tables (1),
S3 presigned URLs (1), Cognito (2), EMR (2), SQS visibility timeout (2),
DMS (2), S3 Transfer Acceleration (2), Step Functions (3), Shield (3),
placement groups (3), EBS snapshots (3), S3 replication (3).

### Two honest warnings about these numbers

**First — the bank is not the exam.** These 522 questions are community-written practice
material, not real exam items. The counts tell you what experienced question-writers
thought mattered, which correlates with the real thing but is not the same as it.

**Second, and more important — the bank badly under-weights security.** Security is
**30% of the real exam**, the single largest domain, yet security concepts score low here:
GuardDuty/Inspector/Macie 6 questions, Secrets Manager 5, WAF 5, STS 4, Shield 3,
CloudHSM 0. That is a **flaw in the question bank, not a signal about the exam.**

> **Do not use the low security counts as permission to skip security.** If anything,
> invert it: the thinner the practice coverage, the more exposed you are. Study security
> to the guide's 30%, not to the bank's 8%.

---

## 5. How the poster marks all of this

Three marks, each one a shape as well as a colour, so they survive a black-and-white
print and do not rely on telling hues apart.

| Mark | Meaning | Where it comes from |
|---|---|---|
| ▮▮▮ / ▮▮▯ / ▮▯▯ | asked a lot / often / thinly | **Counted** from the 522 questions, by `questions/yield-report.py` |
| † | a trap sits next to this fact | Hand-marked — "looks right, is wrong" is a judgement no counter can make |
| ≈ | the exam likes to reword this | Hand-marked, with the rewordings listed in the **Also asked as** block |

Re-run `questions/yield-report.py` then `poster/mark-poster.py` after adding question
sources, and every bar moves with the new data.

---

## 6. On exam dumps

Several of the sources gathered here are labelled "exam dumps". Worth being straight
about this once:

- The GitHub set and the Whizlabs PDF are **community-written practice questions with
  explanations**. They are ordinary study material and fine to use.
- **ExamTopics and Quizlet could not be collected** — ExamTopics serves its content behind
  JavaScript and a paywall, Quizlet returned HTTP 403. I did not work around either.
- Sites that host **genuine leaked exam items** are a different matter. Everyone who sits
  an AWS exam signs a confidentiality agreement covering the questions and the answer
  options. Using leaked items breaches it, and AWS can revoke a certification and bar a
  candidate over it. That is a real consequence for you, not a hypothetical.

The one source worth adding that I could not fetch for you is **AWS Skill Builder's
official practice question set** — it needs your login, it is written by the people who
write the exam, and it is the only practice material with no provenance problem at all.

---

## 7. Changes applied

- Poster rebuilt: **298 recall rows across 22 blocks**, with yield, trap and reword marks.
- New blocks: load balancers in depth, API Gateway, migration and hybrid, the long tail,
  resilience and DR, cost optimization, global/regional/zonal scope, and "Also asked as".
- Three poster sizes: 18×24 in (3 column), 12×18 in (2 column), 5×34 in (1 column, phone).
- `questions/` — 522 questions, tagged by service area and exam domain, answers hidden
  behind a toggle, rebuildable from `sources/` with one script.
- `COVERAGE-ANALYSIS.md` — this document.
