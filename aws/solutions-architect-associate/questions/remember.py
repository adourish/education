#!/usr/bin/env python3
"""
One line to remember for each glossary term: the cue the exam uses, and the
pick. The full entry in glossary.py explains; this is what to memorise.

Written as cue: pick where there is a cue, or as the one fact that decides
questions. Kept to a line each, on purpose.
"""

from __future__ import annotations

REMEMBER: dict[str, str] = {
    # ---------------- compute ----------------
    "Amazon EC2": "A server you patch yourself. The last resort, not the first.",
    "AWS Lambda": "Under 15 minutes, on a trigger, nothing to patch: Lambda. Over 15 minutes: Fargate.",
    "Lambda@Edge": "Change a request at the edge, needs network or time: Lambda@Edge. A tiny tweak: CloudFront Functions.",
    "Lambda container image": "Already a Docker image, finishes in 15 minutes: still Lambda, up to 10 GB.",
    "Choosing where a container runs": "Lambda, then Fargate, then ECS or EKS on EC2. Stop at the first that fits.",
    "Amazon ECS": "Containers, AWS's own way. Pick it unless the question says Kubernetes.",
    "Amazon EKS": "The question says Kubernetes or kubectl: EKS. Otherwise ECS is less to run.",
    "Amazon EKS Anywhere": "Kubernetes on your own servers or a Snowball: EKS Anywhere.",
    "AWS Fargate": "Containers with no servers. Longer than 15 minutes or always on.",
    "Amazon ECR": "Where container images live. Scan on push finds CVEs.",
    "AWS Elastic Beanstalk": "Hand it the app; it builds servers, balancer, scaling. The deployment policy is the mark.",
    "Beanstalk deployment policies": "All at once, rolling, rolling with extra batch, immutable, traffic splitting: rising safety and cost.",
    "Beanstalk traffic splitting": "A slice of real traffic to the new version, least work: traffic splitting.",
    "Immutable deployment": "New instances built beside the old, thrown away if wrong: safest, easiest to undo.",
    "Blue/green deployment": "Two full environments, swap, swap back: blue/green. Quick rollback.",
    "AWS Batch": "Many jobs with an order, hours or days: Batch.",
    "Warm pool": "Instances take too long to boot: a warm pool.",
    "EC2 Auto Scaling": "Min, desired, max, across zones; replaces what dies. Target tracking first.",
    "Amazon Machine Image (AMI)": "A saved disk to launch identical instances. Copy it to use it in another Region.",
    "Spreading Spot across instance types": "Spot capacity keeps failing: more instance types, capacity-optimized allocation.",
    "Spot Instances": "Up to 90% off, taken back with two minutes' warning. Only for work that can stop and restart.",
    "Reserved Instances": "Steady, one instance type, one or three years. Reserve the baseline.",
    "Savings Plans": "Steady spend per hour, instance type may change: Savings Plan.",
    "Dedicated Host": "A licence counted by socket or core: Dedicated Host. Dedicated Instance only keeps others off.",
    "Placement group": "Cluster for speed, spread for safety, partition for big distributed systems.",
    "Cluster placement group": "Tightly coupled HPC, node to node: cluster, one zone, add an EFA.",
    "Spread placement group": "A few critical instances that must not share hardware: spread, 7 per zone.",
    "Partition placement group": "Hadoop, Cassandra, Kafka: partition, 7 partitions per zone.",
    "Instance store": "Fastest disk, wiped on stop. Scratch only.",
    "AWS Outposts": "AWS hardware in your own building, same APIs: Outposts.",
    "AWS Local Zones": "Single-digit milliseconds for users in one city: a Local Zone.",
    "AWS Wavelength": "Inside the phone company's 5G network: Wavelength.",

    # ---------------- storage ----------------
    "Amazon S3": "Objects by URL, unlimited. Static site: S3 behind CloudFront.",
    "S3 storage classes": "How fast you need it back picks the class; how often you read it picks the price.",
    "S3 Standard": "Read often: Standard. No minimum days, no retrieval charge.",
    "S3 Standard-IA": "Kept but rarely read, wanted at once: Standard-IA. 30-day minimum.",
    "S3 One Zone-IA": "Rarely read and you could recreate it: One Zone-IA. Does not survive a zone.",
    "S3 Intelligent-Tiering": "Pattern unknown or varies, no retrieval cost, minimal management: Intelligent-Tiering.",
    "S3 Glacier": "Archive. Instant: milliseconds. Flexible: minutes to 12 hours. Deep Archive: 12 to 48 hours.",
    "S3 Glacier Instant Retrieval": "Read about once a year but needed in milliseconds: Glacier Instant.",
    "S3 Glacier Flexible Retrieval": "Minutes to 12 hours is fine: Flexible. Expedited 1 to 5 minutes, Standard 3 to 5 hours, Bulk 5 to 12.",
    "S3 Glacier Deep Archive": "Cheapest of all, 12 to 48 hours back, 180-day minimum: Deep Archive.",
    "S3 lifecycle policy": "Move after N days, delete after N days, by prefix, tag or size. Clears incomplete uploads.",
    "S3 versioning": "Undo an overwrite or delete: versioning. Needed before replication, MFA Delete, Object Lock.",
    "S3 Object Lock": "Nobody may delete it, not even root, for a period: Object Lock, compliance mode.",
    "S3 Cross-Region Replication": "A copy in another Region, least loss: CRR. Needs versioning both ends.",
    "S3 Transfer Acceleration": "Uploads from far away: Transfer Acceleration, plus multipart.",
    "S3 presigned URL": "One person, one object, a while, no AWS account: a presigned URL.",
    "Multipart upload": "Over 100 MB: multipart. Over 5 GB: required.",
    "Amazon EBS": "One instance, one zone, a disk. Survives a stop, not a zone.",
    "EBS volume types": "gp3 default; io2 over 16,000 IOPS; st1 big sequential and cheap; sc1 cold. HDDs cannot boot.",
    "EBS snapshot": "A backup in S3, incremental, one Region. Copy it to move a volume. DLM schedules them.",
    "EFS throughput mode": "Bursting runs on credit from size; elastic follows the work. A spike nobody can size: elastic.",
    "Amazon EFS": "Many Linux servers, across zones, NFS: EFS. A mount target per zone.",
    "Amazon FSx": "Windows and SMB: FSx for Windows. HPC and training: Lustre. NetApp, SMB plus NFS: ONTAP.",
    "FSx for Windows File Server": "SMB, Active Directory, Windows apps: FSx for Windows. Multi-AZ to survive a zone.",
    "FSx for Lustre": "Sub-millisecond, training, HPC, linked to a bucket: FSx for Lustre.",
    "AWS Storage Gateway": "A family: File (a share into S3), Volume (disks, stored or cached), Tape (a fake tape library).",
    "S3 File Gateway": "A legacy app writes to an NFS or SMB share, files appear in S3: File Gateway.",
    "FSx File Gateway": "A local copy of a Windows file share in FSx: FSx File Gateway.",
    "Volume Gateway": "All data local, backed up to AWS: stored. Hot data local, the rest in S3: cached. iSCSI.",
    "Tape Gateway": "Retire a tape library, keep the backup software, land in Deep Archive: Tape Gateway.",
    "AWS Snow Family": "Too much data for the line, or compute with no connection: a Snow device.",
    "AWS Snowcone": "Small, 8 or 14 TB, battery, runs EC2: Snowcone.",
    "SFTP": "An SFTP server on one EC2 instance is a single point of failure. The fix is Transfer Family.",
    "AWS Transfer Family": "Partners keep SFTP, files land in S3, no server: Transfer Family.",
    "AWS DataSync": "Over the network, repeatedly, only what changed, encrypted: DataSync. Hundreds of GB on 100 Mbps.",
    "AWS Backup": "One plan for every service, retention in years, copy to another Region: AWS Backup.",
    "AWS Snowball Edge": "Storage Optimized moves data; Compute Optimized runs work with no connection.",
    "Snowball Edge Compute Optimized": "Process on site with no connection, even Kubernetes on a ship: Compute Optimized.",

    # ---------------- databases ----------------
    "Amazon RDS": "SQL, joins, an existing app, SQL Server or Oracle: RDS. Multi-AZ for failover, replicas for reads.",
    "Amazon Aurora": "SQL, faster, survives a Region: Aurora. Still relational.",
    "Aurora Serverless": "Load comes and goes, or dev and test: Aurora Serverless v2. Set the max ACUs for the peak.",
    "RDS Multi-AZ": "Failover, no reads. The standby serves nothing.",
    "RDS read replica": "Reads, in Region or across. Promoted by hand, so not a failover.",
    "Amazon DynamoDB": "Key-value, any scale, milliseconds, no joins: DynamoDB. Unpredictable: on-demand.",
    "DynamoDB Accelerator (DAX)": "The same DynamoDB reads, microseconds: DAX. Reads only.",
    "DynamoDB Global Tables": "Two Regions, both writing: global tables. Needs Streams on.",
    "Amazon ElastiCache": "The same reads over and over, sessions: ElastiCache for Redis. The app writes the cache (lazy loading).",
    "Redshift Advisor": "Make a Redshift cluster quicker or cheaper from its own queries: Redshift Advisor.",
    "Amazon Redshift": "Reporting over a great deal of history: Redshift. Files in S3 too: Redshift Spectrum.",
    "Amazon Neptune": "Relationships, graph, fraud rings: Neptune.",
    "Amazon Timestream": "Telemetry, readings over time, IoT: Timestream. Not DynamoDB, not Neptune.",
    "Amazon DocumentDB": "MongoDB wording: DocumentDB.",
    "Amazon QLDB": "A tamper-proof ledger with full history, one owner: QLDB.",
    "AWS DMS": "Move a database while the old one keeps running: DMS. Engine changes too: add SCT.",
    "RDS Proxy": "Too many connections, Lambda opening them: RDS Proxy.",
    "AWS Schema Conversion Tool": "The engine changes (Oracle to PostgreSQL): SCT rewrites the schema, DMS moves the data.",

    # ---------------- networking ----------------
    "Amazon VPC": "Your own network: address range, subnets, routes.",
    "Subnet": "One zone each. Public only if its route table points at an internet gateway.",
    "Security group": "Allow only, stateful, per instance, from another group by id. Cannot deny.",
    "Network ACL": "The only one that can deny. Stateless, per subnet, both directions.",
    "NAT gateway": "Private subnets out, never in. One per zone in production; IPv6 uses egress-only instead.",
    "Internet gateway": "One per VPC, in no zone, in and out. One per zone or per subnet is wrong.",
    "Route table": "Where a subnet's traffic goes. One per private subnet, each to its own zone's NAT.",
    "Shared route table": "A shared route table sends every zone through one NAT gateway. One table per private subnet.",
    "VPC peering": "Exactly two VPCs. Not transitive, stops at 125.",
    "AWS Transit Gateway": "Hundreds of VPCs, many accounts, many sites: transit gateway. A route table per attachment keeps them apart.",
    "AWS PrivateLink": "A private door to one service, not a road. Stay in private address space: PrivateLink. Offer yours: NLB + endpoint service.",
    "VPC endpoint": "S3 and DynamoDB: gateway endpoint, free. Anything else: interface endpoint, by the hour.",
    "AWS Direct Connect": "The road: a private line, steady, never the internet, weeks to install.",
    "AWS Client VPN": "One person's laptop into the VPC: Client VPN.",
    "Site-to-Site VPN": "Encrypted over the internet, this week, cheap: Site-to-Site VPN. Backup for Direct Connect.",
    "Route 53 Resolver endpoints": "Names on premises from the VPC: outbound endpoint + forwarding rule + associate with the VPC.",
    "Route 53 routing policies": "Latency: fastest. Geolocation: by country. Failover: a standby with a health check. Weighted: a share.",
    "Simple against multivalue answer": "Several addresses and health checks, no load balancer: multivalue. Simple checks nothing.",
    "Amazon Route 53": "DNS that answers differently by latency, place, weight or health.",
    "Amazon CloudFront": "Users everywhere, cacheable content: one Region behind CloudFront, not many Regions.",
    "AWS Global Accelerator": "UDP or TCP, gaming, VoIP, fixed IPs, many Regions: Global Accelerator. Caches nothing.",
    "Application Load Balancer (ALB)": "Paths, headers, cookies, WAF, Cognito login: ALB. No fixed IP.",
    "Network Load Balancer (NLB)": "Fixed IP, TCP or UDP, PrivateLink, millions of requests: NLB. WAF cannot attach.",
    "VPC Flow Logs": "Which traffic was allowed or rejected: Flow Logs. Not API calls; that is CloudTrail.",
    "IPv4 and IPv6": "IPv6 is all public: private-but-outbound is the egress-only internet gateway. NAT, gateway endpoint, Elastic IP: IPv4 only.",
    "Elastic IP": "A fixed public IPv4 address you can move between instances.",
    "CIDR block": "/24 is 256 addresses, /16 is 65,536, /32 is one. AWS keeps five per subnet.",

    # ---------------- security ----------------
    "AWS IAM": "Who may do what. An explicit deny always wins.",
    "IAM role": "Assumed, credentials expire. Never an access key on a server.",
    "AWS STS": "Short-lived credentials behind a role: STS. Contractors for a project, custom identity brokers.",
    "AWS Organizations": "Many accounts, one bill, shared discounts, SCPs.",
    "Service Control Policy (SCP)": "A ceiling for every account in an OU. Limits, never grants, skips the management account.",
    "AWS Control Tower": "New accounts with guardrails already in place: Control Tower, not plain Organizations.",
    "Amazon Cognito": "Users of your own app log in: Cognito user pool. AWS credentials for them: identity pool.",
    "AWS KMS": "Keys, not secrets. The data key encrypts the data; rotation changes the outer key only.",
    "AWS CloudHSM": "Hardware only you control, AWS cannot see the keys: CloudHSM.",
    "AWS IAM Identity Center": "Staff with company logins across every account: Identity Center. Not for app users.",
    "AWS Secrets Manager": "A password that must rotate itself: Secrets Manager. Hardcoded credentials: this.",
    "SSM Parameter Store": "A setting, or a secret with no rotation, free: Parameter Store.",
    "AWS Certificate Manager (ACM)": "Free public certificates, DNS validation: ACM. CloudFront needs it in us-east-1.",
    "WAF IP set": "A known list of good or bad addresses: a WAF IP set rule.",
    "AWS Network Firewall": "Filters a VPC's traffic by address, port, domain: Network Firewall. Not web requests.",
    "AWS WAF": "Rules on web requests: WAF. On CloudFront, ALB, API Gateway. Never an NLB.",
    "AWS Shield": "Standard is free and on. Advanced for a big DDoS, a team, an NLB or Elastic IP.",
    "AWS Shield Advanced": "Attacks on an NLB, minimal change, a team to call, bill refunded: Shield Advanced.",
    "Shield Advanced protection group": "Blue/green across two balancers: aggregation Sum. Similar resources: Mean. Different sizes: Max.",
    "Amazon GuardDuty": "Threats: stolen key, mining, odd login: GuardDuty. Act with EventBridge + Lambda.",
    "Amazon Inspector": "Software flaws on instances, containers, Lambda: Inspector.",
    "Amazon Macie": "Personal data in S3: Macie. Continuous: automated discovery. Act on a finding: EventBridge + Lambda.",
    "AWS Security Hub": "Every finding in one place: Security Hub. Finds nothing itself.",
    "Amazon Detective": "Why a finding happened: Detective.",
    "AWS Directory Service": "Join servers and desktops to a domain; FSx for Windows needs it. Not for logging users into a web app.",
    "Multi-factor authentication (MFA)": "Root: MFA on several devices, no daily use. MFA Delete: root only, from the CLI.",

    # ---------------- integration ----------------
    "Amazon SQS": "One sender, one worker, nothing lost: SQS. A surge: API, SQS, Lambda.",
    "SQS FIFO queue": "Order and no duplicates: FIFO. 300 a second, 3,000 in batches.",
    "SQS message deduplication": "Eliminate duplicate orders: FIFO with a MessageDeduplicationId.",
    "SQS message group ID": "Order within a group, parallel across groups: the message group ID.",
    "SQS visibility timeout": "Shorter than the work and the message is done twice. Set it longer than the work.",
    "Dead-letter queue": "After too many failed tries, the message goes here: dead-letter queue.",
    "Amazon SNS": "One message to many places at once: SNS. Both fan-out and a queue: SNS in front of SQS.",
    "Amazon EventBridge": "Route on what is inside the event, schedules, other companies' products: EventBridge.",
    "AWS Step Functions": "Steps, retries, waiting for a person, jobs of many tasks: Step Functions. Map for parallel.",
    "Amazon MQ": "An existing ActiveMQ or RabbitMQ app, moved as it is: Amazon MQ.",
    "Amazon Kinesis": "Data Streams keeps and replays; Firehose delivers to S3 with nothing kept.",
    "Amazon Kinesis Data Streams": "A stream several readers can replay, order within a shard: Data Streams.",
    "Kinesis Data Firehose": "Straight into S3, Redshift, OpenSearch, no code, no replay: Firehose.",
    "Amazon API Gateway": "The front door: keys, caching, limits, auth. Worldwide users: edge-optimized + caching.",
    "API Gateway HTTP API": "Cheaper, faster, JWT built in, nothing else: HTTP API.",
    "API Gateway REST API": "Caching, usage plans, API keys, request validation, WAF: REST API.",
    "JWT": "The caller carries a signed ticket; HTTP API checks it by itself. REST needs an authorizer.",
    "Lambda authorizer": "Your own check on each request, cached: a Lambda authorizer.",
    "API Gateway WebSocket API": "Two-way, live, the server pushes: WebSocket API.",
    "AWS AppSync": "GraphQL, offline sync for mobile: AppSync.",
    "Amazon SES": "Send email at volume, or receive and parse attachments: SES. SNS email is for alerts.",

    # ---------------- analytics ----------------
    "Amazon Athena": "SQL over files in S3, nothing to run, pay per scan: Athena. Parquet cuts the scan.",
    "AWS Glue": "Clean and convert files, and the catalogue Athena reads: Glue.",
    "Amazon EMR": "Spark or Hadoop, a big batch, instances you can see: EMR.",
    "Amazon OpenSearch Service": "Search text and logs with dashboards: OpenSearch.",
    "Amazon QuickSight": "Draw charts and dashboards; it does not query files itself. Athena is not a drawing tool.",
    "Amazon SageMaker": "Machine learning: build, train, run models. Give it permission to the data, not a copy.",

    # ---------------- management ----------------
    "Amazon CloudWatch": "Metrics, logs, alarms. Memory and disk need the agent.",
    "AWS CloudTrail": "Who called which API, when: CloudTrail. Never flow logs.",
    "AWS Config": "What changed and whether it is allowed: Config. A custom rule + Lambda for anything else.",
    "AWS CloudFormation": "Build the same stack again from a template: CloudFormation.",
    "AWS Systems Manager": "Patch, run commands, shell in with no open port: Systems Manager.",
    "Session Manager": "A shell with no SSH key, no open port, no bastion, recorded: Session Manager.",
    "AWS Trusted Advisor": "Cost, performance, fault tolerance, security, service limits checks: Trusted Advisor.",
    "AWS Compute Optimizer": "Where an instance or volume is bigger than it needs to be: Compute Optimizer.",
    "AWS Cost Explorer": "See and forecast spend by service, tag or account: Cost Explorer. Tags must be activated first.",
    "Budget action": "Stop the instances when the budget is passed: a budget action.",
    "Forecasted against actual spend": "Warn before the money is gone: alert on forecasted spend, not actual.",
    "AWS Budgets": "Watch spend against a figure, alert, and act: Budgets.",
    "AWS X-Ray": "Which step of a request is slow: X-Ray.",
    "AWS OpsWorks": "Only when a team already runs Chef or Puppet: OpsWorks.",
    "AWS CLI": "Scripting against the console: the CLI.",
    "AWS Service Catalog": "Only approved templates or AMIs, self-service: Service Catalog.",

    # ---------------- concepts ----------------
    "Availability Zone": "Lose a zone, keep running: spread across zones.",
    "Region": "Lose a Region, keep running: a second Region, by RPO and RTO.",
    "Edge location": "Where CloudFront caches, far more of them than Regions.",
    "High availability": "More than one zone, failover with nobody awake.",
    "Disaster recovery": "RPO is data you may lose, RTO is time you may be down. Lower numbers cost more.",
    "Encryption at rest": "At rest: KMS. In transit: TLS, ACM.",
    "Least privilege": "Only the permissions actually needed. A role, not a key; a condition, not a wide allow.",
    "Decoupling": "A queue or topic between two parts so each can fail or scale alone.",
}


# Every line belongs to a term that exists, and no term is left without one,
# so the two files cannot drift apart without the build saying so.
def _check() -> None:
    from glossary import GLOSSARY  # noqa: E402
    extra = sorted(set(REMEMBER) - set(GLOSSARY))
    missing = sorted(set(GLOSSARY) - set(REMEMBER))
    if extra:
        raise AssertionError("remember.py names terms the glossary lacks: " + ", ".join(extra))
    if missing:
        raise AssertionError("glossary terms with no line to remember: " + ", ".join(missing))
    for name, line in REMEMBER.items():
        if len(line) > 160:
            raise AssertionError(f"{name}: a line to remember should fit a line ({len(line)} characters)")


if __name__ == "__main__":
    _check()
    print(len(REMEMBER), "lines to remember, all matched to a term")
