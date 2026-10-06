# 01 — Numbers and Limits

> **Drill rule:** cover the right column. Say the number out loud. These are asked directly, with no scenario wrapper, and they are free marks.

## S3

| Cue | Answer |
|---|---|
| Max object size | **5 TB** |
| Max size in a single PUT | **5 GB** |
| Multipart upload recommended above | **100 MB** |
| Multipart upload required above | **5 GB** |
| Multipart part size range | **5 MB to 5 GB** (last part may be smaller) |
| Max parts in a multipart upload | **10,000** |
| Max objects in a bucket | **Unlimited** |
| Buckets per account (default) | **100** (soft limit, raise to 1,000) |
| Standard durability | **11 nines (99.999999999%)** |
| Standard availability SLA | **99.99%** |
| Read requests per second per prefix | **5,500 GET/HEAD** |
| Write requests per second per prefix | **3,500 PUT/COPY/POST/DELETE** |
| Minimum storage duration — Standard-IA / One Zone-IA | **30 days** |
| Minimum storage duration — Glacier Instant Retrieval | **90 days** |
| Minimum storage duration — Glacier Flexible Retrieval | **90 days** |
| Minimum storage duration — Glacier Deep Archive | **180 days** |
| Minimum billable object size for IA and Glacier classes | **128 KB** |
| Days before a Standard to Standard-IA lifecycle transition is allowed | **30 days** |

## S3 Glacier retrieval times

| Tier | Time | Storage class |
|---|---|---|
| Instant Retrieval | **milliseconds** | Glacier Instant Retrieval |
| Expedited | **1 to 5 minutes** | Glacier Flexible Retrieval |
| Standard | **3 to 5 hours** | Glacier Flexible Retrieval |
| Bulk | **5 to 12 hours** | Glacier Flexible Retrieval |
| Standard | **within 12 hours** | Glacier Deep Archive |
| Bulk | **within 48 hours** | Glacier Deep Archive |

> Mnemonic for Flexible Retrieval: **Express, Standard, Bulk = minutes, hours, half a day.**
> Retrieved data stays available for download for **24 hours**.

## EBS

| Cue | Answer |
|---|---|
| gp3 — baseline included | **3,000 IOPS and 125 MB/s** |
| gp3 — maximum | **16,000 IOPS and 1,000 MB/s** |
| gp2 — IOPS per GB | **3 IOPS per GB**, capped at 16,000 |
| gp2 — burst for small volumes | **3,000 IOPS** |
| io1 / io2 — max IOPS | **64,000** (io2 Block Express: **256,000**) |
| io2 — IOPS-to-size ratio | **500:1** (io1 is 50:1) |
| st1 throughput HDD — max throughput | **500 MB/s** |
| sc1 cold HDD — max throughput | **250 MB/s** |
| Max volume size (gp2, gp3, io1, io2, st1, sc1) | **16 TiB** |
| Minimum size for st1 and sc1 | **125 GiB** |
| Volume status check interval | **every 5 minutes** |
| Where snapshots are stored | **S3**, incrementally, and they are **region-scoped** |
| Multi-Attach support | **io1 and io2 only**, up to **16 instances**, same AZ |

> **Volume type cheat:** gp3 is the general default. io2 means "I need guaranteed IOPS." st1 means "big sequential reads, like a data warehouse or log processing." sc1 is the cheapest, coldest, rarely touched option.

## Lambda

| Cue | Answer |
|---|---|
| Max execution duration | **900 seconds, which is 15 minutes** |
| Memory range | **128 MB to 10,240 MB**, in 1 MB steps |
| Where you get a full vCPU | at about **1,769 MB** of memory |
| `/tmp` ephemeral disk | **512 MB default, up to 10,240 MB** |
| Synchronous payload limit, request and response | **6 MB** |
| Asynchronous (event) payload limit | **256 KB** |
| Deployment package, zipped, direct upload | **50 MB** |
| Deployment package, unzipped | **250 MB** |
| Container image size | **10 GB** |
| Default concurrent executions per region | **1,000** (soft limit) |
| Environment variable total size | **4 KB** |
| Layers per function | **5** |

## SQS

| Cue | Answer |
|---|---|
| Max message size | **256 KB** (use the Extended Client Library plus S3 for up to 2 GB) |
| Default retention | **4 days** |
| Retention range | **60 seconds to 14 days** |
| Default visibility timeout | **30 seconds** |
| Visibility timeout range | **0 seconds to 12 hours** |
| Long polling max wait | **20 seconds** |
| Delay queue max | **15 minutes** |
| FIFO throughput without batching | **300 messages per second** |
| FIFO throughput with batching, 10 per call | **3,000 messages per second** |
| FIFO high-throughput mode | **70,000 or more messages per second** |
| Standard queue throughput | **nearly unlimited** |
| In-flight messages, standard | **120,000** |
| In-flight messages, FIFO | **20,000** |

> **Delivery guarantees:** Standard is at-least-once with best-effort ordering. FIFO is exactly-once with strict ordering. Design for duplicates on standard queues.

## Kinesis

| Cue | Answer |
|---|---|
| Max record size, Data Streams | **1 MB** |
| Per-shard write | **1 MB/s or 1,000 records/s** |
| Per-shard read, shared fan-out | **2 MB/s and 5 read calls/s** |
| Enhanced fan-out | **2 MB/s per shard per consumer** |
| Default retention | **24 hours** |
| Max retention | **365 days** |
| Firehose buffer interval | **60 to 900 seconds** |
| Firehose minimum latency | about **60 seconds** — near-real-time, not real-time |

## DynamoDB

| Cue | Answer |
|---|---|
| Max item size | **400 KB** |
| What 1 RCU buys | **one strongly consistent read per second of up to 4 KB** (or two eventually consistent) |
| What 1 WCU buys | **one write per second of up to 1 KB** |
| Partition key max size | **2,048 bytes** |
| Sort key max size | **1,024 bytes** |
| Local secondary indexes per table | **5**, and they must be created with the table |
| Global secondary indexes per table | **20** (soft limit) |
| Query and Scan result page size | **1 MB** |
| BatchGetItem limit | **100 items or 16 MB** |
| BatchWriteItem limit | **25 items or 16 MB** |
| Transaction limit | **100 items or 4 MB** |
| DynamoDB Streams retention | **24 hours** |
| TTL deletion window | **within 48 hours of expiry** |

## RDS and Aurora

| Cue | Answer |
|---|---|
| Automated backup retention, default | **7 days** |
| Automated backup retention, range | **0 to 35 days** (0 turns it off) |
| Read replicas per RDS instance | **5** (Aurora allows **15**) |
| Max RDS storage, most engines | **64 TiB** |
| Max Aurora cluster volume | **128 TiB** |
| How many copies Aurora keeps | **6 copies across 3 AZs** |
| Aurora write tolerance | survives the loss of **2 copies** |
| Aurora read tolerance | survives the loss of **3 copies** |
| Multi-AZ replication type | **synchronous** |
| Read replica replication type | **asynchronous** |
| Multi-AZ failover time | typically **60 to 120 seconds** |
| Aurora failover time | typically **under 30 seconds** |
| Aurora Global Database cross-region lag | typically **under 1 second** |
| Aurora Global Database secondary regions | up to **5** |

> **The single most-tested RDS distinction:** Multi-AZ is for **availability** — synchronous, a standby you cannot read from, automatic failover. Read replicas are for **scaling reads** — asynchronous, readable, can live in another region, promoted manually.

## VPC

| Cue | Answer |
|---|---|
| VPC CIDR block size range | **/16 (65,536 addresses) down to /28 (16 addresses)** |
| Reserved IPs per subnet | **5** |
| Which five are reserved | network address, VPC router, DNS, reserved for future use, broadcast — the **first four and the last one** |
| Usable IPs in a /24 subnet | **251** (256 minus 5) |
| VPCs per region, default | **5** |
| Subnets per VPC | **200** |
| Security groups per network interface | **5** (raise to 16) |
| Rules per security group | **60 inbound and 60 outbound** |
| Security groups per VPC | **2,500** |
| NACLs per VPC | **200** |
| Rules per NACL | **20** (raise to 40) |
| Route tables per VPC | **200** |
| Routes per route table | **50** |
| Internet gateways per VPC | **1** |
| Elastic IPs per region | **5** |
| NAT gateway bandwidth | scales up to **100 Gbps** |
| NAT gateway simultaneous connections per destination | **55,000** |

> `/32` means exactly one IP address. `/0` means the entire network. `0.0.0.0/0` as a route destination means "everything else."

## Load balancers

| Cue | Answer |
|---|---|
| ALB — OSI layer | **Layer 7, HTTP and HTTPS** |
| NLB — OSI layer | **Layer 4, TCP, UDP, TLS** |
| Gateway Load Balancer — OSI layer | **Layer 3, IP** |
| ALB idle timeout, default | **60 seconds** |
| NLB idle timeout | **350 seconds**, not configurable |
| NLB static addressing | **one static IP per AZ**, and it supports Elastic IPs |
| ALB static addressing | **none** — you must use the DNS name |
| Minimum subnets for an internet-facing load balancer | **2, in 2 different AZs** |
| Subnet size a load balancer needs | **at least /27 with 8 free addresses** |
| ALB rules per listener | **100** |
| Cross-zone load balancing by default | **ALB: on. NLB: off. Classic: off.** |
| Deregistration delay (connection draining), default | **300 seconds**, range 0 to 3,600 |

## CloudWatch

| Cue | Answer |
|---|---|
| Basic monitoring interval | **5 minutes**, free |
| Detailed monitoring interval | **1 minute**, paid |
| High-resolution custom metric interval | **1 second** |
| Metric retention, 1-second data | **3 hours** |
| Metric retention, 1-minute data | **15 days** |
| Metric retention, 5-minute data | **63 days** |
| Metric retention, 1-hour data | **455 days, which is 15 months** |
| Log retention range | **1 day to 10 years, or never expire** |
| Metrics EC2 reports with no agent | **CPU, network, disk I/O, status checks** |
| Metrics that need the CloudWatch agent | **memory, disk space used, swap, per-process** |
| Alarm states | **OK, ALARM, INSUFFICIENT_DATA** |

> **The classic trap:** memory utilization and disk space used are **not** default EC2 metrics. They need the unified CloudWatch agent. Any answer claiming "memory metrics with no agent" is wrong.

## Auto Scaling

| Cue | Answer |
|---|---|
| Default cooldown | **300 seconds** |
| Default health check grace period | **300 seconds** |
| Health check types | **EC2 (default), ELB, custom** |
| Default termination order | oldest **launch template or configuration**, then the instance **closest to the next billing hour**, then random |
| Max instances per group | a **soft limit you can raise** — it is not a hard 20 |
| Launch templates versus launch configurations | **templates are current and versioned; configurations are legacy** |

## EC2 pricing and tenancy

| Cue | Answer |
|---|---|
| Reserved Instance terms | **1 or 3 years** |
| Savings Plans terms | **1 or 3 years** |
| Maximum Reserved Instance or Savings Plan discount | **up to about 72%** |
| Spot discount | **up to about 90%** |
| Spot interruption warning | **2 minutes** |
| Spot block, fixed duration | **retired — never the right answer** |
| On-Demand Capacity Reservation | reserve capacity in one AZ with **no term commitment** |
| Dedicated Instance | hardware isolated **per account** |
| Dedicated Host | you get the **whole physical server**, needed for socket or core-based licences |
| Billing granularity | **per second**, with a 60-second minimum |

## Everything else worth memorizing

| Cue | Answer |
|---|---|
| Snowcone capacity | **8 TB usable HDD, 14 TB SSD** |
| Snowball Edge Storage Optimized | **80 TB usable** |
| Snowmobile capacity | **up to 100 PB** |
| Rough rule for choosing Snow over the network | more than about **10 TB** on a slow link |
| Direct Connect dedicated port speeds | **1, 10, and 100 Gbps** |
| Direct Connect hosted port speeds | **50 Mbps to 10 Gbps** |
| Direct Connect lead time | **weeks to months** — never the answer to an urgent need |
| Site-to-Site VPN tunnels per connection | **2**, for redundancy |
| Site-to-Site VPN throughput per tunnel | about **1.25 Gbps** |
| Route 53 multivalue answer records returned | **up to 8 healthy records** |
| Route 53 health check failure threshold | **3 consecutive failed checks** by default |
| CloudFront default TTL | **24 hours** |
| CloudFront max TTL | **1 year** |
| CloudFront price classes | **All, 200, 100** — 100 is cheapest with the smallest footprint |
| Effect of a Service Control Policy on the management account | **none — SCPs never restrict the management account** |
| KMS automatic key rotation, AWS-managed keys | **once a year** |
| Data size you can encrypt directly with KMS | **up to 4 KB** — above that use envelope encryption |
| IAM roles per account | **1,000** |
| IAM users per account | **5,000** |
| Groups one user can belong to | **10** |
| Managed policies per role, user, or group | **10** (raise to 20) |
