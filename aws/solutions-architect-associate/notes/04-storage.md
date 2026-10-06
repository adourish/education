# 04 — Storage

## The first question to ask on any storage question

| Shape of the need | Service |
|---|---|
| A **single instance** needs a disk | **EBS** |
| **Many instances** need the same files, Linux | **EFS** |
| **Many instances** need the same files, Windows and SMB | **FSx for Windows File Server** |
| **Objects** over HTTP, any size, from anywhere | **S3** |
| **Archive**, retrieval in minutes to days | **S3 Glacier classes** |
| **Temporary scratch** at the highest possible IOPS | **Instance store** |
| **High-performance computing** shared scratch | **FSx for Lustre** |
| **On-premises** apps need cloud storage behind them | **Storage Gateway** |
| Moving **petabytes** with no bandwidth | **Snow family** |

## S3 — Simple Storage Service

### Cue → Answer

| Cue | Answer |
|---|---|
| Object size range | **0 bytes to 5 TB** |
| Single PUT limit | **5 GB** |
| Multipart upload range | parts of **5 MB to 5 GB**, up to **10,000 parts** |
| Namespace scope of bucket names | **globally unique across all AWS accounts** |
| Consistency model | **strong read-after-write consistency** for all operations, since December 2020 |
| Default encryption | **SSE-S3 (AES-256) is applied to all new objects automatically** |
| Durability | **11 nines** |
| To protect against accidental deletes | **versioning** |
| To require MFA before a permanent delete | **MFA Delete**, which needs versioning and can only be enabled by the root user with the CLI |
| To make objects undeletable for a fixed period | **Object Lock** in governance or compliance mode, plus a legal hold. Needs versioning. |
| To copy objects automatically to another region | **Cross-Region Replication (CRR)** |
| To copy objects automatically within a region | **Same-Region Replication (SRR)** |
| What replication requires | **versioning on both buckets**, plus an **IAM role** granting S3 permission to replicate |
| Does replication copy existing objects | **no, only new ones** — use **S3 Batch Replication** for what is already there |
| To move data between classes on a schedule | **lifecycle rules** |
| To let a browser upload straight to S3 | a **presigned URL** or **presigned POST** |
| To serve a static website | **enable static website hosting**; for HTTPS and a custom domain put **CloudFront** in front |
| To stop all public access account-wide | **S3 Block Public Access** |
| The modern way to let CloudFront read a private bucket | **Origin Access Control (OAC)** — Origin Access Identity (OAI) is the legacy name |
| To run SQL against a single object | **S3 Select** |
| To run SQL across many objects and other sources | **Athena** |
| Events S3 can publish | to **SQS, SNS, Lambda, and EventBridge** |
| To speed up uploads from far away | **S3 Transfer Acceleration** — uses CloudFront edge locations |
| To get a report of what is in a bucket | **S3 Inventory** |
| To find out which objects are costing you and how they are accessed | **S3 Storage Lens** and **Storage Class Analysis** |
| To do a bulk operation over millions of objects | **S3 Batch Operations** |
| To find personal data in a bucket | **Amazon Macie** |

### Storage classes

| Class | Availability | AZs | Minimum duration | Retrieval fee | Use |
|---|---|---|---|---|---|
| Standard | 99.99% | 3+ | none | none | Hot data |
| Intelligent-Tiering | 99.9% | 3+ | none | none (small monitoring fee) | Unknown or shifting patterns |
| Standard-IA | 99.9% | 3+ | 30 days | yes | Infrequent, needs multi-AZ |
| One Zone-IA | 99.5% | **1** | 30 days | yes | Infrequent, re-creatable |
| Glacier Instant Retrieval | 99.9% | 3+ | 90 days | yes | Archive, millisecond access |
| Glacier Flexible Retrieval | 99.99% | 3+ | 90 days | yes | Archive, minutes to hours |
| Glacier Deep Archive | 99.99% | 3+ | 180 days | yes | Compliance archive, 12 to 48 hours |

> **The One Zone-IA trap:** it is cheaper because it lives in **one AZ**. If the question says "must survive the loss of an Availability Zone," One Zone-IA is wrong. It is only right for data you could regenerate, like thumbnails or transcodes.

### Lifecycle rule constraints worth memorizing

- Standard to Standard-IA or One Zone-IA: **minimum 30 days** in Standard first.
- You can transition **down** the chain, never **up** — there is no lifecycle transition from Glacier back to Standard. To get it back you **restore** a copy.
- Objects smaller than **128 KB** are not transitioned to IA or Glacier by lifecycle rules.
- You can expire **current** versions, expire **noncurrent** versions, and **clean up incomplete multipart uploads** — that last one is a standard cost-saving answer.

### Who wins on S3 access — policy evaluation

1. An **explicit Deny** in any policy wins — IAM policy, bucket policy, SCP, VPC endpoint policy.
2. **Block Public Access** overrides any bucket policy or ACL that grants public access.
3. Otherwise, an **Allow** in **either** the IAM policy **or** the bucket policy is enough, as long as both accounts are the same. Cross-account needs an Allow on **both** sides.
4. ACLs are **disabled by default** on new buckets and AWS recommends leaving them off.

## EBS — Elastic Block Store

| Cue | Answer |
|---|---|
| Scope | **one Availability Zone** — a volume cannot cross AZs |
| To move a volume to another AZ | **snapshot it, then create a volume from the snapshot in the target AZ** |
| To move to another region | **snapshot, copy the snapshot to the region, create the volume** |
| Attachment | normally **one instance at a time**; **io1 and io2 support Multi-Attach** up to 16 instances in one AZ |
| Replication | **automatically replicated within its AZ** |
| What you can change on a live volume | **type, size, and provisioned IOPS** — elastic volumes, no downtime |
| Can you shrink a volume | **no** — only grow |
| Snapshots are | **incremental**, stored in **S3**, and **region-scoped** |
| CLI command to snapshot | `aws ec2 create-snapshot` |
| To automate snapshot schedules and retention | **Data Lifecycle Manager (DLM)** or **AWS Backup** |
| Encryption | **AES-256 via KMS**; snapshots of an encrypted volume are encrypted; you can encrypt on restore |
| Can you encrypt an existing unencrypted volume in place | **no** — snapshot it, copy the snapshot with encryption on, create a new volume |
| Volume status values | **ok, impaired, insufficient-data**, checked every **5 minutes** |

### Volume types — pick by the phrase in the question

| Phrase in the question | Volume type |
|---|---|
| "general purpose", "cost-effective", default | **gp3** (prefer it over gp2 — cheaper and faster baseline) |
| "sub-millisecond", "guaranteed IOPS", "critical database", ">16,000 IOPS" | **io2** or **io2 Block Express** |
| "large sequential reads", "big data", "log processing", "throughput" | **st1** |
| "lowest cost", "infrequently accessed", "cold" | **sc1** |
| "boot volume" | gp3, gp2, io1, io2 — **st1 and sc1 cannot be boot volumes** |
| "highest IOPS possible, data is temporary" | **instance store**, not EBS |

## EFS — Elastic File System

| Cue | Answer |
|---|---|
| Protocol | **NFS v4.1** |
| Operating systems | **Linux only** |
| Scope | **regional** — mount targets in multiple AZs, so it survives an AZ loss |
| Concurrency | **thousands of instances at once**, shared read-write |
| Capacity | **grows and shrinks automatically**, pay for what you use |
| Storage classes | **Standard**, **One Zone**, **Standard-IA**, **One Zone-IA** |
| To move cold files to IA automatically | **lifecycle management** |
| Performance modes | **General Purpose** (default, lowest latency) and **Max I/O** (higher throughput, higher latency) |
| Throughput modes | **Bursting**, **Elastic**, **Provisioned** |
| Encryption | at rest with **KMS**, in transit with **TLS** |
| Access control | **IAM**, plus **security groups on the mount targets**, plus **EFS Access Points** |

> **EFS versus EBS in one line:** EBS is one disk for one instance in one AZ. EFS is one file system for many instances across many AZs.

## FSx

| Flavour | Pick it when |
|---|---|
| **FSx for Windows File Server** | **SMB**, Windows, Active Directory integration, NTFS permissions, DFS |
| **FSx for Lustre** | **HPC**, machine learning, hundreds of GB/s, and it can link to an **S3 bucket** |
| **FSx for NetApp ONTAP** | You need ONTAP features — snapshots, cloning, multi-protocol NFS and SMB |
| **FSx for OpenZFS** | Moving ZFS workloads, NFS, snapshots |

> If the question says **Windows** or **SMB** or **Active Directory**, it is **FSx for Windows**, never EFS.

## Storage Gateway — hybrid

| Gateway type | What on-premises sees | Where data lands |
|---|---|---|
| **S3 File Gateway** | **NFS or SMB** file share | **S3 objects** |
| **FSx File Gateway** | SMB share with local cache | **FSx for Windows** |
| **Volume Gateway — cached** | **iSCSI** disk | **Primary data in S3**, frequently used data cached locally |
| **Volume Gateway — stored** | **iSCSI** disk | **Primary data stays local**, backed up asynchronously to S3 as EBS snapshots |
| **Tape Gateway** | **Virtual tape library (VTL)** | **S3 and Glacier**, replacing physical tape |

> **Cached versus stored, in one question each.** "We want to shrink our on-premises storage footprint" → **cached**. "We need the whole dataset on site with low latency, backed up to AWS" → **stored**. "We want to retire our tape backup robot" → **Tape Gateway**.

## Snow family and DataSync

| Cue | Answer |
|---|---|
| **Snowcone** | Smallest, 8 TB HDD or 14 TB SSD, rugged, can run edge compute |
| **Snowball Edge Storage Optimized** | **80 TB usable** — the standard bulk transfer answer |
| **Snowball Edge Compute Optimized** | Edge processing with GPU options |
| **Snowmobile** | **Up to 100 PB** in a shipping container — exabyte-scale datacentre evacuation |
| **AWS DataSync** | **Online** transfer and ongoing sync between on-premises NFS/SMB/HDFS/object storage and S3, EFS, or FSx. Needs bandwidth. |
| **AWS Transfer Family** | Managed **SFTP, FTPS, FTP** front door onto S3 or EFS |
| Rule of thumb | If the question stresses **limited or no bandwidth**, or a **hard deadline with petabytes**, pick **Snow**. If it stresses **ongoing, scheduled, incremental sync**, pick **DataSync**. |

## AWS Backup

| Cue | Answer |
|---|---|
| What it is | One place to define **backup plans, schedules, retention, and lifecycle** across services |
| Services it covers | **EBS, EC2, RDS, Aurora, DynamoDB, EFS, FSx, Storage Gateway, S3, DocumentDB, Neptune** |
| Features that answer compliance questions | **cross-region copy, cross-account copy, Backup Vault Lock (write-once-read-many), audit reports** |
| When to pick it over DLM | when the question says **multiple services, central policy, or compliance reporting** |

## AMIs — Amazon Machine Images

| Cue | Answer |
|---|---|
| Scope | **region-scoped** — to use one in another region you must **copy** it there |
| To share with another account | modify the AMI's **launch permissions**; encrypted snapshots also need the **KMS key shared** |
| To standardize and schedule image builds | **EC2 Image Builder** |
| Backing types | **EBS-backed** (can be stopped, persists) and **instance-store-backed** (cannot be stopped) |
