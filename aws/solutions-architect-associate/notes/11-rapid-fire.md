# 11 — Rapid Fire

> 150 one-liners. Cover the right column, work down the page, and mark the ones you miss. About 12 minutes end to end. Do it every morning in the last two weeks before the exam.
>
> If you miss three in the same group, go back and reread that service page.

## Foundations (1–15)

| # | Cue | Answer |
|---|---|---|
| 1 | A region contains at least how many AZs | **3** (some older ones have 2; design for 3) |
| 2 | Can a subnet span two AZs | **No** |
| 3 | Can a VPC span two regions | **No** |
| 4 | Name the global services | **IAM, Route 53, CloudFront, Organizations, WAF for CloudFront, Billing** |
| 5 | Which resources are AZ-scoped | **subnets, EC2 instances, EBS volumes, ENIs, NAT gateways** |
| 6 | Which artifacts must be copied to another region | **AMIs, EBS snapshots, RDS snapshots, ECR images, KMS keys** |
| 7 | The six Well-Architected pillars | **Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability** |
| 8 | AWS is responsible for security **of** what | **the cloud** — hardware, infrastructure, managed service software |
| 9 | You are responsible for security **in** what | **the cloud** — your data, IAM, guest OS on EC2, security groups |
| 10 | Who patches the OS on RDS | **AWS** |
| 11 | Who patches the OS on EC2 | **you** |
| 12 | RTO means | **Recovery Time Objective — how long you may be down** |
| 13 | RPO means | **Recovery Point Objective — how much data you may lose** |
| 14 | The four DR strategies, cheapest first | **backup and restore, pilot light, warm standby, multi-site active-active** |
| 15 | The 7 Rs of migration | **retire, retain, relocate, rehost, replatform, refactor, repurchase** |

## EC2 and Auto Scaling (16–40)

| # | Cue | Answer |
|---|---|---|
| 16 | The seven instance states | **pending, running, stopping, stopped, shutting-down, terminated, rebooting** |
| 17 | What survives a reboot that does not survive a stop | **instance store data and the public IPv4 address** |
| 18 | What hibernate saves | **the contents of RAM, written to the root EBS volume** |
| 19 | Metadata endpoint | **169.254.169.254** |
| 20 | Which metadata service version to prefer | **IMDSv2** |
| 21 | When does user data run | **once, at first boot, as root** |
| 22 | Spot interruption notice | **2 minutes** |
| 23 | Spot discount | **up to about 90%** |
| 24 | RI and Savings Plan discount | **up to about 72%** |
| 25 | Needed for a socket-based software licence | **Dedicated Host** |
| 26 | Lowest-latency placement | **cluster placement group** |
| 27 | Maximum isolation placement | **spread placement group** |
| 28 | Placement group for Cassandra or HDFS | **partition** |
| 29 | Default user for an Amazon Linux AMI | **ec2-user** |
| 30 | Default user for an Ubuntu AMI | **ubuntu** |
| 31 | System status check failing means | **AWS's infrastructure** — stop and start to migrate hosts |
| 32 | Instance status check failing means | **your OS or configuration** |
| 33 | Default Auto Scaling cooldown | **300 seconds** |
| 34 | Default health check grace period | **300 seconds** |
| 35 | Simplest recommended scaling policy | **target tracking** |
| 36 | Policy for a known Monday-morning spike | **scheduled scaling** |
| 37 | Legacy versus current instance definition | **launch configurations are legacy; launch templates are current and versioned** |
| 38 | To take an instance out of service for debugging | **standby** |
| 39 | To run a script before termination | **a lifecycle hook** |
| 40 | Besides EC2, name three things Auto Scaling can scale | **ECS service count, DynamoDB capacity, Aurora replica count, Spot Fleet** |

## Load balancing (41–52)

| # | Cue | Answer |
|---|---|---|
| 41 | ALB layer | **7** |
| 42 | NLB layer | **4** |
| 43 | Gateway Load Balancer layer | **3** |
| 44 | Which load balancer gives you a static IP | **NLB** |
| 45 | Which supports UDP | **NLB** |
| 46 | Which does path and host routing | **ALB** |
| 47 | Which can authenticate with Cognito | **ALB** |
| 48 | Minimum AZs for an internet-facing load balancer | **2** |
| 49 | Cross-zone load balancing default on ALB | **on** |
| 50 | Cross-zone load balancing default on NLB | **off** |
| 51 | Where the health check is configured | **on the target group** |
| 52 | How to serve multiple certificates on one listener | **SNI** |

## Lambda and serverless (53–64)

| # | Cue | Answer |
|---|---|---|
| 53 | Lambda max duration | **15 minutes (900 seconds)** |
| 54 | Lambda memory range | **128 MB to 10,240 MB** |
| 55 | Lambda synchronous payload limit | **6 MB** |
| 56 | Lambda asynchronous payload limit | **256 KB** |
| 57 | Lambda `/tmp` default size | **512 MB**, configurable to 10,240 MB |
| 58 | Default concurrency per region | **1,000** |
| 59 | Fix cold starts | **provisioned concurrency** |
| 60 | Stop one function starving the account | **reserved concurrency** |
| 61 | Share dependencies between functions | **layers** |
| 62 | What a 429 from Lambda means | **throttled — concurrency limit hit** |
| 63 | API key plus usage plan is for | **throttling and metering, not authentication** |
| 64 | API Gateway options for auth | **IAM, Lambda authorizer, Cognito user pool, resource policy** |

## S3 (65–85)

| # | Cue | Answer |
|---|---|---|
| 65 | Max object size | **5 TB** |
| 66 | Single PUT limit | **5 GB** |
| 67 | Multipart part size range | **5 MB to 5 GB** |
| 68 | Max parts | **10,000** |
| 69 | Durability | **11 nines** |
| 70 | Consistency model | **strong read-after-write** |
| 71 | Default encryption today | **SSE-S3, applied automatically to new objects** |
| 72 | SSE-C means | **you supply the key with every request; AWS never stores it** |
| 73 | SSE-KMS means | **you control the customer master key; AWS handles the data key** |
| 74 | Requirement for Cross-Region Replication | **versioning on both buckets, plus an IAM role** |
| 75 | Does replication copy existing objects | **no — use S3 Batch Replication** |
| 76 | Minimum days before a Standard-IA transition | **30** |
| 77 | Minimum storage duration for Glacier Deep Archive | **180 days** |
| 78 | Glacier Flexible Retrieval expedited time | **1 to 5 minutes** |
| 79 | Glacier Flexible Retrieval standard time | **3 to 5 hours** |
| 80 | Glacier Flexible Retrieval bulk time | **5 to 12 hours** |
| 81 | How long restored Glacier data stays available | **24 hours** |
| 82 | Which class is single-AZ | **One Zone-IA** |
| 83 | Requirement for MFA Delete | **versioning, and only the root user can enable it, via the CLI** |
| 84 | Make objects undeletable for seven years | **Object Lock in compliance mode** |
| 85 | Current name for CloudFront-to-private-bucket access | **Origin Access Control (OAC)** |

## EBS, EFS, FSx (86–97)

| # | Cue | Answer |
|---|---|---|
| 86 | gp3 baseline | **3,000 IOPS, 125 MB/s** |
| 87 | gp2 IOPS per GB | **3**, capped at 16,000 |
| 88 | io2 max IOPS | **64,000** (Block Express 256,000) |
| 89 | Max EBS volume size | **16 TiB** |
| 90 | Which types cannot be boot volumes | **st1 and sc1** |
| 91 | Which types support Multi-Attach | **io1 and io2**, up to 16 instances, same AZ |
| 92 | Where snapshots live | **S3, incrementally, region-scoped** |
| 93 | Can you shrink an EBS volume | **No** |
| 94 | Encrypt an existing unencrypted volume | **snapshot, copy with encryption on, restore** |
| 95 | EFS protocol and OS | **NFS v4.1, Linux only** |
| 96 | EFS scope | **regional, with mount targets per AZ** |
| 97 | SMB and Active Directory file shares | **FSx for Windows File Server** |

## Databases (98–120)

| # | Cue | Answer |
|---|---|---|
| 98 | Multi-AZ replication type | **synchronous** |
| 99 | Read replica replication type | **asynchronous** |
| 100 | Can you read from a Multi-AZ standby | **No** |
| 101 | Multi-AZ purpose | **availability** |
| 102 | Read replica purpose | **read scaling** |
| 103 | Read replicas per RDS instance | **5** |
| 104 | Read replicas per Aurora cluster | **15** |
| 105 | Default RDS backup retention | **7 days**, range 0 to 35 |
| 106 | RDS point-in-time recovery granularity | **about 5 minutes** |
| 107 | Restoring an RDS snapshot gives you | **a new instance with a new endpoint** |
| 108 | Aurora copies of your data | **6 across 3 AZs** |
| 109 | Max Aurora cluster volume | **128 TiB** |
| 110 | Aurora cross-region DR feature | **Global Database** |
| 111 | Aurora feature to rewind in place | **Backtrack** |
| 112 | DynamoDB max item size | **400 KB** |
| 113 | What 1 RCU buys | **one strongly consistent read/s of up to 4 KB** |
| 114 | What 1 WCU buys | **one write/s of up to 1 KB** |
| 115 | DynamoDB microsecond cache | **DAX** |
| 116 | LSI must be created when | **with the table** |
| 117 | GSI consistency | **eventually consistent only** |
| 118 | DynamoDB cross-region active-active | **Global Tables** |
| 119 | Which ElastiCache engine supports persistence and failover | **Redis** |
| 120 | Which ElastiCache engine is multi-threaded | **Memcached** |

## Networking (121–138)

| # | Cue | Answer |
|---|---|---|
| 121 | VPC CIDR range | **/16 to /28** |
| 122 | Reserved IPs per subnet | **5** |
| 123 | Usable IPs in a /24 | **251** |
| 124 | What makes a subnet public | **a route to an internet gateway** |
| 125 | Security groups are | **stateful, allow-only, instance level** |
| 126 | NACLs are | **stateless, allow and deny, subnet level, evaluated in order** |
| 127 | How to block a single IP | **a NACL deny rule** |
| 128 | NACL rules needed for SSH | **inbound 22 and outbound ephemeral ports 1024–65535** |
| 129 | Default NACL behaviour | **allows everything** |
| 130 | Custom NACL behaviour | **denies everything** |
| 131 | Is VPC peering transitive | **No** |
| 132 | Can peered VPCs overlap CIDRs | **No** |
| 133 | Transitive hub for many VPCs | **Transit Gateway** |
| 134 | Which services use gateway endpoints | **S3 and DynamoDB only** |
| 135 | Alias versus CNAME at the apex | **only Alias works at the zone apex** |
| 136 | Route 53 multivalue returns | **up to 8 healthy records** |
| 137 | CloudFront certificate region | **us-east-1** |
| 138 | CloudFront default TTL | **24 hours** |

## Integration, monitoring, security (139–150)

| # | Cue | Answer |
|---|---|---|
| 139 | SQS max message size | **256 KB** |
| 140 | SQS default and max retention | **4 days default, 14 days max** |
| 141 | SQS default visibility timeout and max | **30 seconds, 12 hours** |
| 142 | SQS long polling max wait | **20 seconds** |
| 143 | SQS standard delivery guarantee | **at-least-once, best-effort ordering** |
| 144 | FIFO queue name suffix | **`.fifo`** |
| 145 | Kinesis shard capacity in and out | **1 MB/s in, 2 MB/s out** |
| 146 | Kinesis default and max retention | **24 hours default, 365 days max** |
| 147 | CloudWatch basic versus detailed interval | **5 minutes versus 1 minute** |
| 148 | Metrics needing the CloudWatch agent | **memory and disk space used** |
| 149 | CloudTrail free event history | **90 days, management events** |
| 150 | Trusted Advisor's five categories | **Cost Optimization, Performance, Fault Tolerance, Security, Service Limits** |
