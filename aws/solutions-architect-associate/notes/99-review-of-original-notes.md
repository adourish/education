# 99 — Review of the Original Slide Decks

## What I reviewed

Seven PowerPoint files in `G:\My Drive\Resources\Education\AWS\Architect Associate`:

| File | Slides | Notes |
|---|---|---|
| `aws-architect-associate.pptx` | 2 | Earliest version |
| `aws-architect-associate-1.pptx` | 2 | Near-identical to the above |
| `aws-architect-associate-2.pptx` | 3 | Adds S3 Infrequent Access, EBS snapshot CLI |
| `aws-architect-associate-3.pptx` | 7 | Expands |
| `aws-architect-associate-4.pptx` | 7 | Expands |
| `aws-architect-associate-5.pptx` | 8 | Expands |
| `aws-architect-associate-6.pptx` | 8 | **Latest and most complete — marked "V07 – 2018/11/01"** |

Deck 6 is a superset of the others and is the only one worth keeping as a source. The last three slides of deck 6 are empty.

## The headline finding

These notes were written for **SAA-C01**, the exam version retired in 2020. The exam is now **SAA-C03**. The structure of your notes is good — compact, one box per service, which is exactly the right shape for memorizing — but a meaningful number of the facts have since changed, and several large topic areas that SAA-C03 tests heavily are not in the decks at all.

Read the two sections below before you drill anything. Unlearning a wrong number is much harder than learning a new one.

---

## Facts in the decks that are now wrong

| What the decks say | What is correct now | Why it matters |
|---|---|---|
| "5gb per object" (decks 1–5) | **Max object size is 5 TB.** 5 GB is the single-PUT limit. | Deck 6 fixed this to 5 TB. The earlier decks will cost you a mark. |
| "Lambda max execution time = 5 minutes" | **15 minutes (900 seconds).** | Deck 6 lists both the old 5-minute line and the correct 900 seconds, so it contradicts itself. Delete the 5-minute line. |
| "Lambda memory 128 MB to 3008 MB, in 64 MB increments" | **128 MB to 10,240 MB, in 1 MB increments.** | Changed in 2020. |
| "Lambda ephemeral disk 512 MB" | **512 MB default, configurable up to 10,240 MB.** | Changed in 2022. |
| "Max auto scaling group size is 20" | **There is no hard limit of 20** — it is a soft quota you can raise. | This was never right and would lead you to a wrong answer on a scaling question. |
| "Data in Amazon S3 is not encrypted by default" | **SSE-S3 is applied to all new objects automatically** since January 2023. | A current exam answer saying "enable default encryption" may now be phrased differently. |
| "RRS — reduced redundancy storage 99.99%" | **Reduced Redundancy Storage is deprecated.** AWS no longer recommends it and it is not a valid exam answer. | Drop it entirely. |
| "Glacier: low cost storage 50tb" | **There is no 50 TB figure for Glacier.** Glacier is now three storage classes: Instant Retrieval, Flexible Retrieval, Deep Archive. | The whole Glacier box needs rewriting — see `04-storage.md`. |
| "Expedited 1–5 min, standard 5–12 hours" | **Expedited 1–5 minutes, Standard 3–5 hours, Bulk 5–12 hours.** | Your notes merged Standard and Bulk and dropped Bulk. Three tiers, not two. |
| "CloudWatch retention period 14 days to 15 months" (deck 1) and "15 days to 15 months" (deck 6) | Retention is **tiered by resolution**: 1-second data 3 hours, 1-minute 15 days, 5-minute 63 days, 1-hour 455 days. | Neither version of the note is usable. |
| Extensive EC2-Classic detail | **EC2-Classic was fully retired in August 2022.** | Roughly a third of the EC2 box in every deck is about a platform that no longer exists. Delete it and reclaim the space. |
| "Classic ELB can scale proxy servers and backend instances" | Classic Load Balancer is **legacy**. The current three are **ALB (layer 7), NLB (layer 4), Gateway Load Balancer (layer 3)**. | Deck 6 added ALB, which is good, but still gives Classic top billing and omits GWLB. |
| "Multi-AZ deployments (multiregion is not available)" | **Cross-region is available** — RDS cross-region read replicas, and **Aurora Global Database**. | This would make you reject the right answer on a DR question. |
| "Aurora — 64 TB" | **Aurora clusters now grow to 128 TiB.** 64 TiB is the figure for the other RDS engines. | Two different numbers that your notes merged into one. |
| "SNS — note that FIFO queues are not currently supported" | **SNS FIFO topics exist** (since 2020) and deliver to SQS FIFO queues. | Out of date. |
| "Auto scaling: to use a new AMI create a new launch configuration template. One config per auto scaling group" | **Launch configurations are legacy.** Use a **launch template**, which is versioned, so you create a **new version** rather than a whole new object. | The mechanism in the note is the old one. |
| "WLM — can run multi-region or multi-az, for disaster recovery" | **Workload Management is only about query queues and concurrency** in Redshift. It has nothing to do with multi-region or DR. | Two unrelated ideas have been merged into one bullet. |
| "Kinesis Data Analytics" | Renamed **Amazon Managed Service for Apache Flink**. | The old name may still appear, but know both. |
| Origin Access Identity (implied by the CloudFront box) | **Origin Access Control (OAC)** is the current mechanism. | OAI still works but OAC is the exam answer. |
| "Spot block / fixed duration Spot" | **Retired.** Never the right answer. | Not in your decks explicitly, but worth knowing it is gone. |

## Structural problems in the decks

| Problem | Where | Fix |
|---|---|---|
| The word **"Redshift"** is stranded inside the NACL text box | Decks 1 and 6, the NACL box reads "…CIDR — The /32 denotes one IP address… **Redshift** / NACL: Network ACL" | A copy-and-paste slip. It makes the NACL box confusing to revise from. |
| A **VPN fact filed under IAM** | Deck 6, the IAM box ends with "instances that you launch into a VPC can't communicate with your own network… attach a virtual private gateway…" | That belongs in the VPC box, not IAM. |
| **Lambda appears twice** on the same slide | Deck 1, slide 2 has two separate Lambda boxes | Merge them. |
| **AMI appears twice** | Deck 1, slide 2 has "AMI: Amazon Managed Images" twice with identical text | Merge them. |
| **"Technical Tags, Automation, Business, Security"** is attached to the CloudFront box | Decks 1 and 6 | Those are the four **tag categories**. They belong only in the Tags box, where they also correctly appear. |
| **AMI is expanded wrongly** | All decks say "Amazon Managed Images" | It is **Amazon Machine Image**. |
| Typos that will trip you when revising aloud | "contatiners", "eventsi", "scriptf", "oosely coupled", "messages.o", "Datawarehouse" | Minor, but worth cleaning if you keep editing the decks. |

---

## What SAA-C03 tests that the decks do not cover at all

This is the bigger gap. Each of these has appeared on recent exams and none of it is in your notes.

### Networking
- **Transit Gateway** — the transitive hub, and the answer whenever "many VPCs" appears. Peering is in your notes; Transit Gateway is not.
- **AWS PrivateLink / endpoint services** — exposing your own service to another VPC.
- **Global Accelerator** — static anycast IPs, TCP and UDP, and how it differs from CloudFront.
- **Gateway Load Balancer** — layer 3, for third-party appliances.
- **Route 53 Resolver** inbound and outbound endpoints for hybrid DNS.
- **IP-based routing policy** — your notes list seven Route 53 policies; there are now eight.
- **Egress-only internet gateway** for IPv6.

### Security — this is the 30% domain, the largest on the exam
- **AWS Organizations and Service Control Policies**, including the heavily tested fact that **an SCP never restricts the management account**.
- **Control Tower** and **permission boundaries**.
- **Secrets Manager** versus **Systems Manager Parameter Store**.
- **GuardDuty, Inspector, Macie, Security Hub, Detective** — and the distinction between them, which gets tested directly.
- **AWS WAF** and **Shield Standard versus Shield Advanced**.
- **Firewall Manager** and **Network Firewall**.
- **ACM**, and the rule that a CloudFront certificate must live in **us-east-1**.
- **IAM Identity Center**, which replaced AWS SSO.
- The **policy evaluation order**: explicit deny, then allow, then implicit deny.
- **Envelope encryption** and the 4 KB direct-encryption limit on KMS.

### Storage
- **FSx** — all four flavours. Your notes have EFS but no FSx at all, and "SMB or Windows file share" is a guaranteed exam phrase.
- **S3 Object Lock**, **Block Public Access**, **Access Points**, **Storage Lens**, **Batch Operations**, **S3 Select**.
- The **current storage class line-up**, including Intelligent-Tiering, Glacier Instant Retrieval, and Glacier Deep Archive.
- **Same-Region Replication** alongside Cross-Region Replication.
- **gp3**, which is now the default general-purpose volume and is cheaper and faster than gp2.
- **AWS Backup**, **Data Lifecycle Manager**, **DataSync**, **Transfer Family**, **Snowcone**, **Snowmobile**, **Tape Gateway**.

### Databases
- **Aurora Serverless v2**, **Aurora Global Database**, **Backtrack**, **fast cloning**.
- **DynamoDB** depth: **Global Tables**, **TTL**, **transactions**, **point-in-time recovery**, **on-demand versus provisioned capacity**, **LSI versus GSI**, and partition key design. Your notes have four lines on DynamoDB and the exam asks far more.
- **ElastiCache Redis versus Memcached** — a direct comparison question that appears often.
- **Athena**, **Glue**, **Lake Formation**, **OpenSearch**, **Neptune**, **Timestream**, **QLDB**, **DocumentDB**, **Keyspaces**, **MemoryDB**.
- **DMS and the Schema Conversion Tool** for migration questions.

### Application integration
- **EventBridge** — now a very common right answer, and not in your notes.
- **Step Functions** — your notes have SWF, which is the legacy service. Step Functions is what the exam wants.
- **SQS FIFO queues**, **dead-letter queues**, **long polling**, **visibility timeout tuning**. Your notes cover standard queues only.
- **Amazon MQ** for lift-and-shift of AMQP, MQTT, and JMS applications.
- **API Gateway** — your notes only say "can use API gateway" under Lambda.

### Operations and cost
- **AWS Config** — the compliance leg of the CloudWatch / CloudTrail / Config trio. Your notes have the other two.
- **Systems Manager**, especially **Session Manager**, which is the modern answer to "shell access without opening port 22."
- **Compute Optimizer**, **Cost Explorer**, **Budgets**, **Cost Anomaly Detection**, **Savings Plans**.
- **CloudFormation** depth — change sets, StackSets, drift detection, DeletionPolicy. Your notes have two lines.
- **Well-Architected Framework** and the **disaster recovery strategies**. These frame a large share of SAA-C03 questions and are entirely absent.
- **Outposts**, **Local Zones**, **Wavelength**.

---

## What the decks get right and should be kept

Credit where it is due — these are accurate, well-chosen, and exactly the sort of thing the exam asks:

- The **security group versus NACL** comparison, including "security groups control ports on instances, NACLs control which networks reach the subnet." That is a good, memorable framing.
- The **five things a default VPC gives you**. Complete and correct.
- The **Route 53 routing policy** descriptions. Accurate, and only missing IP-based.
- The **Trusted Advisor CPFSS mnemonic**. Still correct, still useful. Keep it.
- The **S3 encryption breakdown** of SSE-S3, SSE-C, and SSE-KMS — correctly describing who holds which key. This is a common point of confusion and your notes have it right.
- **Multi-AZ for durability, read replicas for scalability**, which deck 6 states explicitly in the Terms box. That is the single most-tested database distinction and you have it.
- The **EC2 stop behaviour** list — EBS persists, instance store and RAM are lost, the instance usually moves to a new host. Correct and well worth keeping.
- The **default SSH user names** per AMI. Still accurate and still asked.
- The **CloudWatch default metrics** note that memory and disk need a custom script or agent. Correct, and a classic trap.
- The **volume status check** values of ok, impaired, and insufficient-data, every five minutes.
- The **Volume Gateway cached versus stored** distinction, added in deck 6. Correct.
- **CIDR** `/32` is one address and `/0` is the whole network.
- **SQS at-least-once delivery, order not preserved, 256 KB maximum** — correct for standard queues.

---

## Recommended next steps

1. **Retire decks 1 through 5.** Keep only deck 6 as the historical source. Everything in 1–5 is either duplicated in 6 or superseded by it.
2. **Use the markdown notes in this folder as the working set.** They carry forward everything in the "keep" list above, correct everything in the "now wrong" table, and fill the gaps.
3. **If you want to keep a one-page visual**, rebuild it from `10-decision-triggers.md` rather than from the old slides. The trigger table is the part that earns marks on a scenario exam.
4. **Treat the `.vce` and exam-dump files in that folder with caution.** They are from 2017 to 2019, they target the retired SAA-C01, and dump questions are often wrong even for their own era. They are useful only for getting used to the question *format*, not for the answers. Use the official AWS practice question set and AWS Skill Builder for real practice.
