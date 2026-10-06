# 09 — Monitoring, Management, and Governance

## The three that always get confused

| Service | The one-word answer | Question |
|---|---|---|
| **CloudWatch** | **Performance** | "How is it behaving? What are the metrics and logs?" |
| **CloudTrail** | **Audit** | "**Who** did **what**, **when**, and from **which IP**?" |
| **AWS Config** | **Compliance** | "What is the **configuration** now, what was it before, and does it meet our rules?" |

> Memorize this sentence: **"CloudWatch watches performance. CloudTrail trails API calls. Config tracks configuration."**

## CloudWatch

| Cue | Answer |
|---|---|
| What it collects | **metrics, logs, events, and traces (with X-Ray)** |
| Basic versus detailed monitoring | **5 minutes** free, **1 minute** paid |
| High-resolution metrics | down to **1 second** |
| Metric retention | 1-second data **3 hours**; 1-minute **15 days**; 5-minute **63 days**; 1-hour **455 days** |
| Log retention | **1 day to 10 years, or never expire** |
| EC2 metrics available with no agent | **CPUUtilization, NetworkIn/Out, DiskReadOps/WriteOps, StatusCheckFailed** |
| Metrics that **require** the CloudWatch agent | **memory used, disk space used, swap usage, per-process metrics** |
| What the agent is called now | the **unified CloudWatch agent** (it replaced the old CloudWatch Logs agent) |
| Alarm states | **OK, ALARM, INSUFFICIENT_DATA** |
| What an alarm can do | notify **SNS**, trigger **Auto Scaling**, run an **EC2 action** (stop, terminate, reboot, recover), or start a **Systems Manager** action |
| Composite alarm | combines several alarms with AND/OR to cut noise |
| To search and analyse log data with a query language | **CloudWatch Logs Insights** |
| To turn a log pattern into a metric | a **metric filter** — for example, count `ERROR` lines and alarm on them |
| To stream logs onward | a **subscription filter** to Lambda, Kinesis, or Firehose |
| To archive logs cheaply for years | **export to S3**, then lifecycle them to Glacier |
| To see all your dashboards from several accounts | **cross-account cross-region dashboards** |
| To watch an endpoint from outside | **CloudWatch Synthetics canaries** |
| To see real user browser performance | **CloudWatch RUM** |
| To watch container workloads | **Container Insights** |
| To get recommendations on anomalies automatically | **CloudWatch Anomaly Detection** |
| Route 53 health checks integrate with | **CloudWatch** — and a CloudWatch alarm can itself be a health check |

## CloudTrail

| Cue | Answer |
|---|---|
| What it records | **API activity** across the console, SDKs, CLI, and other AWS services — governance, compliance, operational and risk auditing |
| What is on by default | **90 days of Event history** in every region, for management events, at no cost |
| What you must create for anything longer | a **trail** delivering to **S3** (and optionally CloudWatch Logs) |
| Best practice when creating a trail | **apply it to all regions**, so future regions are included automatically |
| Event types | **management events** (control plane, on by default), **data events** (S3 object-level and Lambda invocations, **off** by default and charged), **Insights events** (unusual activity) |
| To know who deleted an S3 object | enable **data events** for that bucket — management events alone will not show it |
| Encryption | log files are **encrypted with SSE-S3 by default**; you can use SSE-KMS |
| To prove logs have not been tampered with | **log file integrity validation**, which produces a digest file |
| To collect trails from every account in one place | an **organization trail**, delivering to a central S3 bucket |
| To search trail data with SQL | **Athena** over the S3 bucket |
| Delivery delay | typically **within 15 minutes** of the API call |

## AWS Config

| Cue | Answer |
|---|---|
| What it does | records the **configuration** of your resources over time and evaluates them against **rules** |
| What a configuration item is | a point-in-time snapshot of a resource's attributes and relationships |
| Managed rules you should recognize | "**S3 bucket must not be public**", "**EBS volumes must be encrypted**", "**root account must have MFA**", "**required tags must be present**", "security groups must not allow unrestricted SSH" |
| Custom rules run on | **Lambda** or **Guard** |
| To fix a non-compliant resource automatically | a **remediation action**, usually a **Systems Manager Automation document** |
| To apply rules across every account | **Config conformance packs** and **aggregators** |
| What it answers that CloudTrail cannot | "**what did this security group look like last Tuesday?**" and "**is this resource compliant right now?**" |

## CloudFormation

| Cue | Answer |
|---|---|
| What it is | **infrastructure as code** in JSON or YAML, creating a **stack** of resources |
| Template sections | **AWSTemplateFormatVersion, Description, Metadata, Parameters, Mappings, Conditions, Transform, Resources, Outputs** |
| The only required section | **Resources** |
| **Parameters** | Values passed in at deploy time |
| **Mappings** | Fixed lookup tables, classically region to AMI ID |
| **Outputs** | Values exported from the stack, importable by another stack |
| **Conditions** | Create a resource only when a test passes, for example only in production |
| To preview what a change will do | a **change set** |
| To stop an update deleting a resource | a **stack policy**, or `DeletionPolicy: Retain` |
| To keep data when the stack is deleted | **`DeletionPolicy: Snapshot`** or **`Retain`** |
| To find out whether someone changed a resource outside the template | **drift detection** |
| To deploy the same stack across many accounts and regions | **StackSets** |
| To reuse a template inside another | **nested stacks** |
| To signal that an EC2 instance finished bootstrapping | a **CreationPolicy** with **cfn-signal** and a **WaitCondition** |
| To define resources in a real programming language | the **AWS CDK**, which synthesizes CloudFormation |
| To offer approved templates to teams in a self-service catalog | **AWS Service Catalog** |
| What happens on a failed create | **automatic rollback** by default |

> **Beanstalk, CloudFormation, and OpsWorks in one line each.** Beanstalk: "deploy my app, you decide the infrastructure." CloudFormation: "build exactly the infrastructure I declared." OpsWorks: "we already use Chef or Puppet, give us managed Chef or Puppet servers."

## Systems Manager (SSM)

| Capability | What it does |
|---|---|
| **Session Manager** | Browser or CLI shell to an instance with **no open inbound ports, no SSH keys, no bastion** — fully logged |
| **Run Command** | Run a script or command across many instances at once |
| **Patch Manager** | Scan and install OS patches on a schedule, with baselines |
| **Parameter Store** | Free hierarchical config store, with SecureString for encrypted values |
| **State Manager** | Keep instances in a defined state |
| **Automation** | Runbooks for repetitive operations, and Config remediation |
| **Inventory** | What software is installed where |
| **Compliance** | Patch and association compliance reporting |
| **Fleet Manager** | Manage instances without logging in |
| **Maintenance Windows** | Scheduled windows for disruptive tasks |

> **The trigger to remember:** "we must not open port 22 and must not manage SSH keys, but engineers need shell access, and it must be auditable" → **Session Manager**.

## Cost management

| Service | Trigger |
|---|---|
| **Cost Explorer** | "visualize and forecast spend", "break down by service, tag, or account" |
| **AWS Budgets** | "**alert me** when spend or usage crosses a threshold", "budget for a Reserved Instance utilization target" |
| **Cost and Usage Report (CUR)** | "the most detailed line-item billing data, delivered to S3" |
| **Cost Anomaly Detection** | "detect unexpected spend automatically with machine learning" |
| **Compute Optimizer** | "**right-size** my EC2, EBS, Lambda, and ECS resources based on real utilization" |
| **Trusted Advisor** | "idle resources, unassociated Elastic IPs, approaching service limits" |
| **Pricing Calculator** | "estimate the cost before we build it" |
| **Billing Conductor** | "show different rates to different internal business units" |

### The classic cost-optimization answers

| Problem | Answer |
|---|---|
| Instances idle at night and weekends | **scheduled Auto Scaling**, or an **Instance Scheduler** on tags |
| Steady 24/7 workload on On-Demand | **Savings Plans or Reserved Instances** |
| Batch jobs that can be interrupted | **Spot Instances** |
| Large NAT gateway data processing bill for S3 traffic | an **S3 gateway VPC endpoint** |
| Storing everything in S3 Standard forever | **lifecycle rules** to IA and Glacier, and **Intelligent-Tiering** when the pattern is unknown |
| Paying for old snapshots and unattached volumes | find them with **Trusted Advisor** or **Config**, then delete, and automate retention with **DLM** or **AWS Backup** |
| High Athena bill | **Parquet, compression, and partitioning** |
| Over-sized instances | **Compute Optimizer** |
| Cross-AZ data transfer charges | keep chatty tiers **in the same AZ**, while still spanning AZs for availability |
| Over-provisioned DynamoDB | **on-demand mode** for spiky traffic, or **auto scaling** on provisioned |

## Service Health and support

| Cue | Answer |
|---|---|
| **AWS Health Dashboard** | Events that affect **your** resources — scheduled maintenance, degraded services |
| **Service Quotas** | View and request increases to limits, in one place |
| **Support plans** | Basic (free), Developer, Business, Enterprise On-Ramp, Enterprise |
| Which plan gives you a **Technical Account Manager** | **Enterprise** (and a pooled TAM on Enterprise On-Ramp) |
| Which plans give full Trusted Advisor | **Business and above** |
| Which plan is the minimum for 24/7 phone and chat with engineers | **Business** |

## Regions, Availability Zones, and resilience

| Cue | Answer |
|---|---|
| **Region** | A geographic area with **at least 3 (usually 3 or more) Availability Zones** |
| **Availability Zone** | One or more discrete datacentres with independent power, cooling, and networking, **tens of kilometres apart** |
| **Local Zone** | An extension of a region placed near a large city for single-digit-millisecond latency |
| **Wavelength Zone** | Inside a telecom provider's 5G network, for mobile edge latency |
| **Outposts** | AWS racks **in your own datacentre**, same APIs — for data residency or very low on-premises latency |
| **Edge location** | A CloudFront point of presence — far more numerous than regions |
| How to survive an **AZ** failure | spread across **at least 2 AZs**, usually 3 |
| How to survive a **region** failure | **multi-region** — cross-region replication, Route 53 failover, Aurora Global Database, DynamoDB Global Tables |
| Which services are **global** | **IAM, Route 53, CloudFront, WAF (for CloudFront), Organizations, Billing** |
| Which services are **regional** | nearly everything else — EC2, S3 buckets, RDS, VPC, DynamoDB tables |
| Which resources are **AZ-scoped** | **subnets, EBS volumes, EC2 instances, ENIs, NAT gateways, RDS instances** |
| Things that must be **copied** to another region | **AMIs, EBS snapshots, RDS snapshots, ECR images, Redshift snapshots, KMS keys (or use multi-Region keys)** |

> **The resilience question in one sentence:** if the question says "**highly available**", the answer involves **multiple Availability Zones**. If it says "**disaster recovery**" or "**region outage**", the answer involves **multiple regions**.
