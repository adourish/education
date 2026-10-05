# 10 — Decision Triggers

> Most of the exam is scenario questions. This page is the scenario-to-service map. **If you only drill one page, drill this one.**
>
> How to use it: cover the right column. Read the left. Say the service. The exam phrases things almost exactly like this.

## Keyword reflexes

These words, on their own, should produce an instant answer.

| The question says | Reach for |
|---|---|
| "decouple" | **SQS** |
| "fan-out", "notify many subscribers" | **SNS** |
| "event-driven", "filter on event content", "SaaS event" | **EventBridge** |
| "orchestrate", "coordinate steps", "retry and branch" | **Step Functions** |
| "serverless" | **Lambda, API Gateway, DynamoDB, S3, Fargate, Aurora Serverless** |
| "highly available" | **multiple Availability Zones** |
| "disaster recovery", "region outage" | **multiple regions** |
| "durable" | **S3, or an RDS read replica / Aurora's 6 copies** |
| "in-memory", "sub-millisecond", "microsecond" | **ElastiCache, or DAX for DynamoDB** |
| "petabyte-scale analytics", "data warehouse" | **Redshift** |
| "SQL on data in S3", "no infrastructure" | **Athena** |
| "Hadoop", "Spark", "Hive", "HBase", "Presto" | **EMR** |
| "full-text search", "log dashboards" | **OpenSearch Service** |
| "CDN", "cache at the edge", "global users, static content" | **CloudFront** |
| "static IP addresses", "TCP/UDP", "gaming", "VoIP" | **Global Accelerator** |
| "DNS", "route traffic by region or weight" | **Route 53** |
| "dedicated private network connection" | **Direct Connect** |
| "encrypted tunnel over the internet, quickly" | **Site-to-Site VPN** |
| "connect hundreds of VPCs" | **Transit Gateway** |
| "connect two VPCs" | **VPC peering** |
| "private access to S3 from a private subnet" | **S3 gateway VPC endpoint** |
| "private access to another AWS service or a partner service" | **interface VPC endpoint (PrivateLink)** |
| "no bandwidth, petabytes, deadline" | **Snowball / Snowmobile** |
| "ongoing incremental sync from on-premises" | **DataSync** |
| "on-premises app needs cloud storage behind it" | **Storage Gateway** |
| "shared file system, Linux, many instances" | **EFS** |
| "SMB", "Windows file share", "Active Directory" | **FSx for Windows File Server** |
| "HPC shared scratch", "hundreds of GB/s" | **FSx for Lustre** |
| "infrastructure as code", "repeatable environments" | **CloudFormation** |
| "upload my code and let AWS handle the rest" | **Elastic Beanstalk** |
| "Chef or Puppet" | **OpsWorks** |
| "Kubernetes", "kubectl" | **EKS** |
| "containers with no servers to manage" | **Fargate** |
| "who made this API call?" | **CloudTrail** |
| "what was this configuration last week?", "is it compliant?" | **AWS Config** |
| "metrics, alarms, logs" | **CloudWatch** |
| "shell access with no open ports and no SSH keys" | **Session Manager** |
| "rotate database credentials automatically" | **Secrets Manager** |
| "free config store" | **Parameter Store** |
| "SQL injection", "cross-site scripting", "rate limit by IP" | **AWS WAF** |
| "DDoS Response Team", "cost reimbursement during an attack" | **Shield Advanced** |
| "detect unusual API activity, no agents" | **GuardDuty** |
| "scan for CVEs and software vulnerabilities" | **Inspector** |
| "find PII in S3" | **Macie** |
| "single pane of glass for security findings" | **Security Hub** |
| "single-tenant HSM", "FIPS 140-2 Level 3", "we must be the only key holders" | **CloudHSM** |
| "guard rails across all accounts" | **Organizations SCPs** (or **Control Tower** to set it all up) |
| "right-size my resources based on real usage" | **Compute Optimizer** |
| "alert me when spend exceeds a threshold" | **AWS Budgets** |
| "immutable, cryptographically verifiable history" | **QLDB** |
| "multiple parties, no central authority" | **Managed Blockchain** |
| "graph", "relationships", "fraud ring" | **Neptune** |
| "time series", "IoT sensor readings over time" | **Timestream** |
| "virtual desktops" | **WorkSpaces** |
| "stream one application to a browser" | **AppStream 2.0** |
| "data residency", "AWS hardware in my datacentre" | **Outposts** |
| "single-digit millisecond latency to a specific city" | **Local Zones** |
| "5G mobile edge" | **Wavelength** |

## Compute scenarios

| Scenario | Answer |
|---|---|
| Steady, predictable 24/7 workload, lowest cost | **Savings Plans or Reserved Instances** |
| Batch processing that can be interrupted and restarted | **Spot Instances** |
| Spot plus guaranteed baseline capacity | **a mixed-instances Auto Scaling group: On-Demand or RI baseline plus Spot for the rest** |
| Software licensed per physical socket or core | **Dedicated Host** |
| Must be certain capacity exists in an AZ for a launch next week, no commitment | **On-Demand Capacity Reservation** |
| Instances need the lowest possible network latency between them | **cluster placement group** |
| A handful of critical instances must never share hardware | **spread placement group** |
| Large distributed system like Cassandra or HDFS | **partition placement group** |
| A function needs to run for 40 minutes | **not Lambda** — use **Fargate, ECS, or AWS Batch** |
| A Lambda function has slow cold starts and latency matters | **provisioned concurrency** |
| A Lambda function is too slow and the code cannot change | **increase its memory**, which also increases CPU |
| One function is consuming the whole account's concurrency | **reserved concurrency** on that function |
| Instances are terminated and relaunched repeatedly by Auto Scaling | **increase the health check grace period**; point the **ELB health check** at a real readiness endpoint |
| Auto Scaling keeps scaling in and out rapidly | **increase the cooldown** and **widen the alarm threshold** |
| Need to scale for a known Monday 9am spike | **scheduled scaling** |
| Need to scale on a learned daily pattern | **predictive scaling** |
| Need to keep average CPU at a target | **target tracking** |
| Must run a cleanup script before an instance is terminated | **a lifecycle hook** |
| Containers need GPUs or a specific instance type | **ECS or EKS on the EC2 launch type**, not Fargate |
| Want the least operational overhead for containers | **Fargate** |
| Need the same image in two regions | **replicate the ECR repository** — images are region-scoped |

## Storage scenarios

| Scenario | Answer |
|---|---|
| Objects must survive the loss of an Availability Zone | **S3 Standard, Standard-IA, or any Glacier class — not One Zone-IA** |
| Thumbnails that can be regenerated, cheapest storage | **S3 One Zone-IA** |
| Access pattern is unknown or changes over time | **S3 Intelligent-Tiering** |
| Compliance archive, retrieval in 12 to 48 hours is fine, cheapest possible | **Glacier Deep Archive** |
| Archive that must still be readable in milliseconds | **Glacier Instant Retrieval** |
| Records must not be deletable for seven years, even by an administrator | **S3 Object Lock in compliance mode** (plus versioning) |
| Protect against accidental overwrite and delete | **versioning**, and **MFA Delete** for the strong version |
| Must survive a region outage | **Cross-Region Replication** |
| Keep a second copy in the same region for log aggregation or compliance | **Same-Region Replication** |
| Replication is configured but old objects did not copy | **S3 Batch Replication** — replication only applies to new objects |
| Users worldwide upload large files slowly | **S3 Transfer Acceleration** |
| Uploading a 20 GB file | **multipart upload** — required above 5 GB |
| Let an unauthenticated browser upload one file securely | a **presigned URL** |
| Serve a private bucket through CloudFront | **Origin Access Control** |
| Bucket is public and should not be | **S3 Block Public Access** |
| Need to delete 50 million objects older than a year | **lifecycle expiration rule** |
| Incomplete multipart uploads are costing money | **lifecycle rule to abort incomplete multipart uploads** |
| A boot volume that is cheap and fast enough for most workloads | **gp3** |
| A database needing guaranteed 40,000 IOPS | **io2** |
| Sequential throughput for log processing | **st1** |
| Need the same volume attached to two instances | **io1 or io2 with Multi-Attach**, same AZ — or rethink and use **EFS** |
| Move an EBS volume to another AZ | **snapshot, then create a volume from the snapshot in the target AZ** |
| Encrypt an existing unencrypted EBS volume or RDS instance | **snapshot it, copy the snapshot with encryption enabled, restore from the copy** |
| Highest possible IOPS and the data is disposable | **instance store** |
| Backups of many services under one policy, with cross-region copies | **AWS Backup** |
| Retire an on-premises tape library | **Tape Gateway** |
| Shrink the on-premises storage footprint but keep low-latency access to hot data | **Volume Gateway, cached mode** |
| Keep the whole dataset on-premises with async backup to AWS | **Volume Gateway, stored mode** |
| On-premises apps need an NFS or SMB share backed by S3 | **S3 File Gateway** |

## Database scenarios

| Scenario | Answer |
|---|---|
| RDS must survive an AZ failure with automatic failover | **Multi-AZ** |
| Reporting queries are slowing the production database | **a read replica** (and point the reports at it) |
| Reads must scale and the same queries repeat constantly | **ElastiCache** in front, or a read replica |
| Need a read replica in another region for both DR and local reads | **cross-region read replica** |
| MySQL-compatible, needs far more performance and 15 replicas | **Aurora** |
| Cross-region DR with sub-second lag and about a minute to fail over | **Aurora Global Database** |
| Traffic is intermittent, want to pay nothing much when idle | **Aurora Serverless v2** |
| Need a test copy of a 2 TB Aurora database in minutes | **Aurora fast database cloning** |
| Need to undo a bad update on Aurora MySQL in place | **Backtrack** |
| Needs OS-level access or an engine RDS does not support | **run the database on EC2** |
| Single-digit millisecond key-value at any scale, no servers | **DynamoDB** |
| DynamoDB reads must be microseconds | **DAX** |
| Need an active-active DynamoDB table in three regions | **Global Tables** |
| Need to react to every item change in DynamoDB | **DynamoDB Streams plus Lambda** |
| Need to purge old DynamoDB items at no cost | **TTL** |
| DynamoDB throttling with an uneven access pattern | **redesign the partition key for higher cardinality**, or switch to **on-demand** |
| Unpredictable, spiky DynamoDB traffic | **on-demand capacity mode** |
| Need session storage that survives a node failure | **ElastiCache for Redis** with Multi-AZ, or **DynamoDB** |
| Simplest multi-threaded cache, no persistence needed | **ElastiCache for Memcached** |
| Need a leaderboard or sorted set | **ElastiCache for Redis** |
| Complex BI reporting across billions of rows, high concurrency | **Redshift** |
| Occasional ad-hoc SQL over logs already in S3 | **Athena** |
| Query S3 data from an existing Redshift cluster without loading it | **Redshift Spectrum** |
| Short queries are stuck behind long ones in Redshift | **Workload Management (WLM) query queues** |
| Migrate Oracle to Aurora PostgreSQL with minimal downtime | **Schema Conversion Tool plus DMS** |

## Networking scenarios

| Scenario | Answer |
|---|---|
| Private instances need to download OS updates | **NAT gateway in a public subnet**, with a route from the private subnet |
| Private instances need S3 and nothing else | **S3 gateway endpoint** — cheaper than a NAT gateway |
| Block one malicious IP address | **a NACL deny rule** — security groups cannot deny |
| Allow the web tier to reach the app tier | a security group rule on the app tier **referencing the web tier's security group** |
| SSH works outbound but not inbound through a NACL | add the **inbound rule and the outbound ephemeral port range (1024 to 65535)** — NACLs are stateless |
| Instance in a public subnet with a public IP still cannot reach the internet | check the **route table has 0.0.0.0/0 to the internet gateway**, then the security group, then the NACL |
| Need to route `/api` and `/static` to different target groups | **ALB path-based routing** |
| Need a load balancer with a fixed IP for a firewall allow-list | **NLB** |
| Need UDP load balancing | **NLB** |
| Need millions of requests per second with the lowest latency | **NLB** |
| Need to redirect all HTTP to HTTPS without touching the app | **an ALB listener rule** |
| A third-party security appliance must inspect all VPC traffic | **Gateway Load Balancer** |
| Three VPCs must all reach each other | **Transit Gateway** — peering is not transitive |
| Need to expose an internal service to a customer's VPC without peering | **PrivateLink with an NLB** |
| Hybrid link needed within days | **Site-to-Site VPN** |
| Hybrid link needing consistent high bandwidth, cost is fine | **Direct Connect** |
| Highest-resilience hybrid connectivity | **two Direct Connect connections at two locations, with VPN backup** |
| Resolve on-premises hostnames from inside a VPC | **Route 53 Resolver outbound endpoint** |
| Fail over to a static maintenance page during an outage | **Route 53 failover routing to an S3 static website** |
| EU users must be served from the EU for data residency | **geolocation routing** |
| Serve every user from whichever region is fastest for them | **latency routing** |
| Shift 5% of traffic to a new stack | **weighted routing** |
| Reduce latency for a global audience reading the same files | **CloudFront** |
| Reduce latency for a global audience on a TCP game protocol | **Global Accelerator** |
| Restrict video to subscribers | **CloudFront signed URLs or signed cookies** |
| Block a whole country from a CloudFront distribution | **geo-restriction** |
| Rewrite a request header at the edge, very cheaply | **CloudFront Functions** |
| Need to call DynamoDB from edge logic | **Lambda@Edge** |
| Find out why traffic is being dropped in a VPC | **VPC Flow Logs** — look for REJECT |
| Need to capture actual packet contents | **VPC Traffic Mirroring** |

## Security scenarios

| Scenario | Answer |
|---|---|
| An application on EC2 needs to read an S3 bucket | an **IAM role attached via an instance profile** — never access keys in code |
| A partner's AWS account needs limited access | a **cross-account IAM role with a trust policy**, assumed with STS |
| Employees should sign in once for all accounts | **IAM Identity Center** |
| Mobile app users should get temporary AWS credentials | **Cognito identity pools** |
| Nobody in any account may use a region | an **SCP with an `aws:RequestedRegion` condition** |
| Developers must not be able to escalate their own permissions | a **permissions boundary** |
| Database password must rotate every 30 days with no code change | **Secrets Manager with rotation** |
| Need a free place to store non-secret configuration | **Parameter Store** |
| Must prove no one tampered with the audit log | **CloudTrail log file integrity validation**, and **S3 Object Lock** on the log bucket |
| Need to know who deleted an object from a bucket | **CloudTrail data events** for that bucket |
| Need to alarm when the root account is used | a **CloudWatch Logs metric filter on the CloudTrail log group**, plus an SNS alarm |
| Must detect compromised instances mining cryptocurrency | **GuardDuty** |
| Must report on unpatched software across the fleet | **Inspector** (findings) and **Systems Manager Patch Manager** (fixing) |
| Must find credit card numbers accidentally stored in S3 | **Macie** |
| Must stop an application-layer attack on a public web app | **AWS WAF** |
| Must satisfy an auditor asking for AWS's SOC 2 report | **AWS Artifact** |
| Must encrypt data where AWS can never access the keys | **CloudHSM**, or **SSE-C** for S3 |
| Must enforce encryption on every new EBS volume | **account-level EBS encryption by default**, plus an **AWS Config rule** to catch exceptions |
| Must enforce that no S3 bucket is public, across the organization | **S3 Block Public Access at the account level**, an **SCP**, and a **Config rule** |
| Engineers need audited shell access with no open ports | **Session Manager** |

## The tie-breakers

When two answers both technically work, apply these in order:

1. **Managed beats self-managed.** Fargate over EC2 containers. RDS over a database on EC2. Prefer the answer with less for you to patch.
2. **Multi-AZ beats single-AZ** whenever the question mentions availability.
3. **Temporary credentials beat long-term keys.** A role always beats an access key.
4. **An explicit deny or a guard rail beats trusting people.** SCP, boundary, Block Public Access.
5. **Cheaper wins only if all stated requirements are still met.** Spot is wrong the moment the question says "cannot be interrupted."
6. **Serverless wins on "minimal operational overhead."** That phrase is a near-certain signal.
7. **Reject anything retired.** EC2-Classic, Spot block, Classic Load Balancer for new designs, Data Pipeline for new ETL, SWF for new workflows.
8. **Reject anything physically impossible.** A subnet spanning AZs. An EBS volume across AZs. An Alias record to an EC2 instance name. A CNAME at the zone apex. Reading from a Multi-AZ standby.
