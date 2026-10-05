# 02 — Mnemonics

> These are for lists you have to produce from a blank page. Learn the trigger word first, then unpack it.

## Well-Architected Framework — six pillars

**"Our Six Pillars Really Cost Something"**

| Letter | Pillar |
|---|---|
| **O** | Operational Excellence |
| **S** | Security |
| **P** | Performance Efficiency |
| **R** | Reliability |
| **C** | Cost Optimization |
| **S** | Sustainability |

## Trusted Advisor — five check categories

**"CPFSS"** — or the sentence **"Cheap Performance Fixes Secure Systems"**

| Letter | Category |
|---|---|
| **C** | Cost Optimization |
| **P** | Performance |
| **F** | Fault Tolerance |
| **S** | Security |
| **S** | Service Limits |

## Route 53 routing policies — eight of them

**"SWF-GLM-GM"** — say it as **"Simple Weighted Failover, Geo Latency Multivalue, Geoproximity, IP-based"**

| Policy | Pick it when |
|---|---|
| **Simple** | One resource serves the whole record |
| **Weighted** | Split traffic by percentage — A/B tests, gradual migration |
| **Failover** | Active-passive disaster recovery |
| **Geolocation** | Route by where the **user** is — compliance, language, content licensing |
| **Geoproximity** | Route by where your **resources** are, with a bias dial to shift traffic |
| **Latency** | Route to the region that answers fastest |
| **Multivalue answer** | Return up to 8 healthy records, health-checked, client picks |
| **IP-based** | Route by the user's CIDR block, for known ISP ranges |

> **The pair people confuse:** Geolocation is about the **user's** location. Geoproximity is about **your resources'** location and lets you shift load with a bias.

## S3 storage classes — cheapest to most expensive access

**"Stand In One Zone, Glacier Instantly Freezes Deeply"**

| Class | Use it when |
|---|---|
| **S3 Standard** | Hot, frequently accessed |
| **S3 Intelligent-Tiering** | Access pattern is unknown or changing — let AWS move it |
| **S3 Standard-IA** | Infrequent access, still need it fast, multi-AZ |
| **S3 One Zone-IA** | Infrequent access, recreatable data, one AZ only, 20% cheaper |
| **Glacier Instant Retrieval** | Archive you still need in milliseconds, accessed once a quarter |
| **Glacier Flexible Retrieval** | Archive, minutes to hours is fine |
| **Glacier Deep Archive** | Compliance retention, 12 to 48 hours is fine, cheapest of all |

## The five things a default VPC gives you

**"I Really Should Note Down"** — Internet gateway, Route table, Security group, Network ACL, DHCP option set

| Item | What it does |
|---|---|
| **I**nternet gateway | Attached, so the VPC can reach the internet |
| **R**oute table | Main table with `0.0.0.0/0` pointing at the internet gateway |
| **S**ecurity group | Default group, allows all outbound and allows inbound from itself |
| **N**etwork ACL | Default NACL, allows all inbound and all outbound |
| **D**HCP option set | The account's default set, associated with the VPC |

Plus: every subnet in a default VPC auto-assigns public IPv4 addresses.

## S3 encryption options

**"3, C, K, K"** — SSE-S3, SSE-C, SSE-KMS, DSSE-KMS, plus client-side

| Option | Who holds the key | Who does the encrypting |
|---|---|---|
| **SSE-S3** | AWS manages everything, AES-256 | S3 |
| **SSE-KMS** | You manage the customer master key in KMS; AWS manages the data key | S3 |
| **SSE-C** | **You** supply the key with every request; AWS never stores it | S3 |
| **DSSE-KMS** | Same as SSE-KMS but applied twice, for strict regimes | S3 |
| **Client-side** | You | Your application, before upload |

> Since January 2023, **SSE-S3 is applied to all new objects by default**. The old note that "S3 is not encrypted by default" is out of date.

## The four EC2 instance lifecycle outcomes

**"Stop, Hibernate, Reboot, Terminate"** — and what survives each

| Action | EBS root volume | Instance store | RAM | Public IPv4 |
|---|---|---|---|---|
| **Reboot** | Kept | **Kept** | Kept | **Kept** |
| **Stop** | Kept | **Lost** | Lost | **Released, new one on start** |
| **Hibernate** | Kept | Lost | **Saved to the root EBS volume** | Released |
| **Terminate** | Deleted if DeleteOnTermination is true | Lost | Lost | Released |

> Reboot is the only action where the instance store and the public IP both survive. That is the exam's favourite distinction here.

## Instance store versus EBS

**"Store is temporary, Block is durable."**

| Instance store | EBS |
|---|---|
| Physically attached to the host | Network-attached |
| Highest possible IOPS | Good, provisioned IOPS |
| **Data lost on stop or terminate** | Data persists |
| Cannot be detached or snapshotted | Detachable, snapshottable |
| Free, included in instance price | Billed separately |
| Buffers, caches, scratch, temporary | Boot volumes, databases, anything you keep |

## Security group versus NACL

**"Groups guard instances. Lists guard subnets."**

| Security group | Network ACL |
|---|---|
| **Instance** level (really the network interface) | **Subnet** level |
| **Stateful** — return traffic is automatically allowed | **Stateless** — you must allow the return traffic explicitly |
| **Allow rules only** | **Allow and deny rules** |
| All rules evaluated together | Rules evaluated **in number order**, first match wins |
| Default: deny all inbound, allow all outbound | Default NACL: allow everything. A **custom** NACL: deny everything. |
| Does not filter traffic between instances in the same subnet when the same SG is used | Does not filter traffic between instances in the same subnet at all |

> Two memory hooks: **stateful = "it remembers"**, and **a custom NACL starts closed while the default NACL starts open.** Both of those get tested.

## Disaster recovery strategies — slowest and cheapest to fastest and dearest

**"Backup, Pilot, Warm, Hot"** — or **"BPWH: Big Problems Won't Hurt"**

| Strategy | RTO / RPO | What is running |
|---|---|---|
| **Backup and restore** | Hours | Nothing — just backups in another region |
| **Pilot light** | Tens of minutes | Core data replicating, servers off |
| **Warm standby** | Minutes | A scaled-down but working copy |
| **Multi-site active-active** | Near zero | Full capacity in both regions, serving traffic |

> RTO = how long you may be down. RPO = how much data you may lose. "R**T**O = **T**ime" and "R**P**O = **P**oint in the past."

## Cloud migration strategies — the 7 Rs

**"Retire, Retain, Relocate, Rehost, Replatform, Refactor, Repurchase"**

| R | Meaning |
|---|---|
| **Retire** | Turn it off, nobody needs it |
| **Retain** | Leave it where it is, for now |
| **Relocate** | Move the hypervisor, as with VMware Cloud on AWS |
| **Rehost** | Lift and shift, unchanged |
| **Replatform** | Lift and reshape — for example self-managed MySQL to RDS |
| **Refactor** | Rewrite it cloud-native |
| **Repurchase** | Drop it and buy SaaS instead |

## The IAM policy evaluation order

**"Deny beats everything, then allow, then default deny."**

1. An **explicit Deny** anywhere always wins.
2. Otherwise, an **explicit Allow** grants access.
3. Otherwise, **implicit deny** — nothing is permitted unless something allowed it.

Plus the guard rails that can only subtract: **SCPs, permission boundaries, and session policies never grant anything; they only limit what an Allow can reach.**

## The four CloudFormation building blocks you must name

**"PMRO"** — Parameters, Mappings, Resources, Outputs. Only **Resources** is required.

## Kinesis family — pick by verb

| Service | Verb |
|---|---|
| **Data Streams** | **Ingest** and keep, with custom real-time processing |
| **Data Firehose** | **Deliver** to S3, Redshift, OpenSearch, Splunk — no code |
| **Managed Service for Apache Flink** | **Query** the stream with SQL or Flink |
| **Video Streams** | **Ingest video** |

> "Streams if I write the consumer. Firehose if AWS writes it for me."
