# AWS Certified Solutions Architect – Associate (SAA-C03)

Memorization notes for the SAA-C03 exam, plus the build that turns them into a
single printable PDF.

## Exam at a glance

| Item | Value |
|---|---|
| Code | SAA-C03 |
| Questions | 65 (50 scored, 15 unscored) |
| Time | 130 minutes |
| Pass mark | 720 / 1000 |
| Cost | 150 USD |

| Domain | Weight |
|---|---|
| Design Secure Architectures | 30% |
| Design Resilient Architectures | 26% |
| Design High-Performing Architectures | 24% |
| Design Cost-Optimized Architectures | 20% |

## The notes

| File | Contents |
|---|---|
| `notes/00-index.md` | How to drill these, exam shape, study order |
| `notes/01-numbers-and-limits.md` | Every number worth memorizing, in one place |
| `notes/02-mnemonics.md` | List-recall tricks |
| `notes/03-compute.md` | EC2, Auto Scaling, ELB, Lambda, containers, Beanstalk |
| `notes/04-storage.md` | S3, EBS, EFS, FSx, Glacier, Storage Gateway, Snow family |
| `notes/05-databases.md` | RDS, Aurora, DynamoDB, ElastiCache, Redshift |
| `notes/06-networking.md` | VPC, security groups vs NACLs, Route 53, CloudFront |
| `notes/07-security-identity.md` | IAM, STS, KMS, WAF, Shield, GuardDuty, Organizations |
| `notes/08-integration-analytics.md` | SQS, SNS, EventBridge, Step Functions, Kinesis, Athena |
| `notes/09-monitoring-governance.md` | CloudWatch, CloudTrail, Config, CloudFormation, cost |
| `notes/10-decision-triggers.md` | "If the question says X, answer Y" |
| `notes/11-rapid-fire.md` | 150 one-line flashcards |
| `notes/99-review-of-original-notes.md` | Review of the 2018-era slide decks these replace |

## Study order

1. `01` and `02` first. Pure rote. Nothing else sticks until the numbers do.
2. `03` through `09`, one per day. Cover the answer column, say the answer, check.
3. `10`. Highest marks per minute of study — the exam is mostly scenario questions.
4. `11` every morning in the last two weeks. About 12 minutes end to end.

Read `99` early. It lists the facts in the older notes that are now wrong, and
unlearning a stale number is harder than learning a new one.

## Building the PDF

```powershell
cd pdf
.\build-pdf.ps1
```

Produces `pdf/aws-saa-c03-memorization-notes.pdf` — 82 pages, letter size.

Requirements: [pandoc](https://pandoc.org/installing.html) on `PATH`, and either
Google Chrome or Microsoft Edge installed. The script combines every markdown
file in `notes/` in filename order, applies `pdf/print.css`, and prints the
result with headless Chrome.

Options:

| Flag | Effect |
|---|---|
| `-OutFile <name>` | Change the output filename |
| `-KeepHtml` | Keep the intermediate `combined.html` for inspection |

## Design notes

The print stylesheet uses a cyan, magenta, and yellow accent palette. Red and
green are never used as the sole carrier of meaning, so the pages remain
readable with protanopia.
