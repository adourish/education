# 03 — Compute

## EC2 — Elastic Compute Cloud

### Cue → Answer

| Cue | Answer |
|---|---|
| The seven instance states | **pending, running, stopping, stopped, shutting-down, terminated, rebooting** |
| What EC2 charges you for while stopped | **nothing for compute**, but you still pay for **EBS volumes** and any **unattached Elastic IPs** |
| Where instance metadata lives | **http://169.254.169.254/latest/meta-data/** |
| Where user data lives | **http://169.254.169.254/latest/user-data/** |
| Which metadata service version you should prefer | **IMDSv2** — it is session-based and defends against server-side request forgery |
| User data runs when | **once, at first boot**, as root |
| Instance cannot reach the internet — check what | **public IP or Elastic IP present? route table has 0.0.0.0/0 to the internet gateway? security group outbound? NACL both ways?** |
| What determines placement on physical hardware | the **placement group** |
| Status check types | **system status check** (AWS infrastructure) and **instance status check** (your OS/config) |
| A failing system status check means | **AWS's problem** — stop and start the instance to migrate it to new hardware |
| A failing instance status check means | **your problem** — the OS, the network config, a full disk |

### Placement groups

| Type | Shape | Pick it for |
|---|---|---|
| **Cluster** | All instances packed onto one rack in one AZ | **Lowest latency, highest throughput** — HPC, tightly coupled jobs. Single point of failure. |
| **Spread** | Each instance on distinct hardware, up to 7 per AZ | **Maximum isolation** — a small number of critical instances |
| **Partition** | Groups of instances in separate partitions, each on its own rack | **Large distributed systems** — HDFS, Cassandra, Kafka |

> Mnemonic: **Cluster = Close. Spread = Separate. Partition = Pods.**

### Default SSH user names

| AMI | User |
|---|---|
| Amazon Linux / Amazon Linux 2 / AL2023 | `ec2-user` |
| RHEL | `ec2-user` or `root` |
| Ubuntu | `ubuntu` |
| CentOS | `centos` or `ec2-user` |
| Debian | `admin` |
| SUSE | `ec2-user` or `root` |
| Bitnami | `bitnami` |

### Purchasing options — the cost-optimization questions live here

| Option | Pick it when the question says |
|---|---|
| **On-Demand** | Short, unpredictable, cannot be interrupted, first time running this workload |
| **Reserved Instance** | Steady state, known for 1 or 3 years, up to ~72% off. Standard RI = cheapest but locked. Convertible RI = you can change family. |
| **Savings Plans** | Steady spend but you want flexibility across instance family, size, region, and even Fargate and Lambda |
| **Spot Instances** | **Fault-tolerant, stateless, interruptible** — batch, CI, rendering, big data. Up to ~90% off, **2-minute interruption notice** |
| **Dedicated Host** | **Socket or core-based software licence**, or you need visibility of the physical server |
| **Dedicated Instance** | Hardware isolated from other accounts, but AWS still controls placement |
| **Capacity Reservation** | You must be certain capacity exists in a specific AZ, with no term commitment |

> **The cost trap:** if a question mentions "licence tied to physical cores or sockets," the answer is **Dedicated Host**, not Dedicated Instance. If it mentions "cannot tolerate interruption," Spot is wrong no matter how cheap.

### Instance family letters

| Letter | Family | Shape |
|---|---|---|
| **T** | Burstable | Low baseline with CPU credits — dev, small web |
| **M** | General purpose | Balanced CPU and memory |
| **C** | Compute optimized | High CPU — batch, modelling, gaming servers |
| **R**, **X**, **z** | Memory optimized | Big RAM — in-memory databases, caches |
| **I**, **D**, **H** | Storage optimized | High local disk IOPS or throughput — NoSQL, warehouses |
| **P**, **G**, **Inf**, **Trn** | Accelerated | GPU and ML accelerators |

## Auto Scaling

| Cue | Answer |
|---|---|
| The three things every group needs | **minimum, desired, maximum** capacity |
| What defines the instances | a **launch template** (versioned) — launch configurations are legacy |
| To roll out a new AMI | **create a new launch template version**, then refresh the instances |
| Scaling policy types | **target tracking, step scaling, simple scaling, scheduled, predictive** |
| Easiest and most-recommended policy | **target tracking** — "keep average CPU at 50%" |
| For a known traffic pattern, like every Monday at 9am | **scheduled scaling** |
| For a repeating daily or weekly pattern learned from history | **predictive scaling** |
| Default cooldown | **300 seconds** |
| Default health check grace period | **300 seconds** |
| To stop instances being killed before the app is up | **raise the health check grace period** |
| To stop the group flapping up and down | **raise the cooldown** and **widen the CloudWatch alarm threshold** |
| To take an instance out for troubleshooting without it being replaced | put it in **standby** |
| To run a script before an instance is terminated | a **lifecycle hook** |
| Health check that notices the application, not just the OS | **ELB health check** |
| What makes a group resilient to an AZ failure | **span multiple AZs** — the group rebalances automatically |

### What Auto Scaling can scale beyond EC2 (Application Auto Scaling)

EC2 instances, **EC2 Spot Fleets**, **ECS service desired count**, **DynamoDB table and index capacity**, **Aurora read replica count**, and more.

> **The classic scenario:** "Instances are being terminated and replaced in a loop." Cause: the application takes longer to boot than the health check grace period. Fix: increase the grace period, or use an ELB health check pointed at a real readiness endpoint.

## Elastic Load Balancing

| Cue | Answer |
|---|---|
| ALB operates at | **Layer 7** — it can read HTTP paths, hosts, headers, query strings |
| NLB operates at | **Layer 4** — TCP, UDP, TLS |
| Gateway Load Balancer operates at | **Layer 3** — it fronts third-party security appliances |
| Classic Load Balancer | **legacy** — only pick it if the question mentions EC2-Classic |
| Need a **static IP** or an Elastic IP on the load balancer | **NLB** |
| Need **millions of requests per second** and extreme low latency | **NLB** |
| Need to route `/api` to one target group and `/images` to another | **ALB** path-based routing |
| Need to route `api.example.com` separately from `www.example.com` | **ALB** host-based routing |
| Need to load balance **containers with dynamic ports** | **ALB** |
| Need **WebSockets or HTTP/2** | **ALB** |
| Need to authenticate users at the load balancer | **ALB** with Cognito or OIDC |
| Need to send a fixed response or redirect HTTP to HTTPS | **ALB** listener rule |
| Need **UDP** | **NLB** |
| Need to preserve the client's source IP | **NLB** does it natively; **ALB** passes it in `X-Forwarded-For` |
| Sticky sessions are implemented with | a **cookie** — `AWSALB` for ALB, duration-based or application-based |
| Health check sits where | on the **target group** |
| Where SSL/TLS termination happens | on the **listener**, using a certificate from **ACM** |
| To serve multiple certificates on one listener | **SNI** (Server Name Indication) |
| Cross-zone load balancing | **on by default for ALB**, off by default for NLB and Classic |
| Minimum subnets for an internet-facing load balancer | **2 subnets in 2 different AZs** |

## Lambda

| Cue | Answer |
|---|---|
| Max duration | **15 minutes** — if a question needs longer, the answer is **Fargate, ECS, Batch, or Step Functions** |
| Memory | **128 MB to 10,240 MB**; CPU scales with memory |
| How to make a function faster without changing code | **give it more memory** — you get proportionally more CPU |
| How to remove cold starts for a latency-sensitive function | **provisioned concurrency** |
| How to stop one function starving the account | **reserved concurrency** |
| Default regional concurrency | **1,000** |
| What a 429 TooManyRequestsException means | you hit a **concurrency limit** |
| Where failed asynchronous invocations go | a **dead-letter queue** (SQS or SNS) or an **on-failure destination** |
| To share code or dependencies between functions | **Lambda layers** |
| To run Lambda inside a VPC | attach it to **subnets and a security group**; outbound internet then needs a **NAT gateway** |
| Lambda key metrics | **Invocations, Errors, Duration, Throttles, DeadLetterErrors, ConcurrentExecutions** |
| Lambda event sources, common ones | **API Gateway, S3, DynamoDB Streams, Kinesis, SQS, SNS, EventBridge, CloudFront (Lambda@Edge), ALB** |
| Lambda@Edge versus CloudFront Functions | **Lambda@Edge** for heavier logic with network access; **CloudFront Functions** for very light, very fast header and URL rewrites |

## Containers

| Cue | Answer |
|---|---|
| **ECS** | AWS's own container orchestrator |
| **EKS** | Managed Kubernetes — pick it when the question says Kubernetes, kubectl, or "existing on-prem k8s" |
| **Fargate** | **Serverless container compute** — no servers to patch, size, or scale |
| **EC2 launch type** | You manage the container instances — pick it when the question needs **GPU, specific instance types, or host access** |
| **ECR** | The container registry. Images are **region-scoped**, so you must replicate or copy them to another region |
| ECS task role versus task execution role | **Task role** = permissions your container code uses. **Task execution role** = permissions ECS needs to pull the image and write logs. |
| To put a load balancer in front of ECS with dynamic ports | **ALB** |
| To reduce container management overhead | **Fargate** |

## Elastic Beanstalk

| Cue | Answer |
|---|---|
| What it does | Handles **capacity provisioning, load balancing, auto scaling, and health monitoring** from your uploaded code |
| Platforms | **Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker** |
| Environment types | **Web Server environment** and **Worker environment** |
| What a Worker environment is for | pulling from an **SQS queue** for background jobs |
| Deployment policies | **All at once, Rolling, Rolling with additional batch, Immutable, Blue/Green (traffic splitting)** |
| Zero-downtime, safest deployment | **Immutable** or **Blue/Green** |
| Cheapest and fastest but has downtime | **All at once** |
| Who owns the underlying resources | **you do** — Beanstalk creates them in your account and you can see and tune them |

> **Beanstalk versus CloudFormation versus OpsWorks:** Beanstalk = "deploy my app, you figure out the infrastructure." CloudFormation = "build exactly the infrastructure I declared." OpsWorks = "I already use Chef or Puppet."

## AWS Batch versus Lambda versus Fargate

| Cue | Answer |
|---|---|
| Thousands of batch jobs, each possibly hours long | **AWS Batch** |
| Short event-driven function, under 15 minutes | **Lambda** |
| Long-running container, no servers to manage | **Fargate** |
| Needs to coordinate many steps with retries and branching | **Step Functions** |
