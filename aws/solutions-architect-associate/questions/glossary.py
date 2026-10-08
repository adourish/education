#!/usr/bin/env python3
"""
Plain-English glossary of the AWS terms that turn up in exam questions.

build-data.py matches every entry against each question and its options, and
attaches the ones it finds. The app then offers a hint showing just those
entries, so a question full of unfamiliar service names becomes something you
can learn from rather than guess at.

Each entry is:
    "name": (pattern, what it is)

The pattern is matched case-insensitively against the question plus all its
options. Keep patterns tight: a term that matches everything is noise.

The definitions deliberately say what a thing IS and what it is FOR. They never
say which option is correct, because a hint that answers the question for you
teaches nothing.
"""

import re


GLOSSARY: dict[str, tuple[str, str]] = {

    # ---------------- compute ----------------
    "Amazon EC2": (r"\bEC2\b|Elastic Compute Cloud",
        "Virtual servers rented by the second. You pick size, OS and disk, and you patch it yourself."),
    "AWS Lambda": (r"\bLambda\b(?!@)",
        "Runs your code on a trigger with no server to manage. Billed per "
        "request and millisecond, capped at 15 minutes. It can run a container "
        "image as well as a zip, so an existing Docker image is no reason to "
        "rule it out. Nothing to patch and no cluster, which makes it the least "
        "to manage of anything that runs code."),
    "Lambda@Edge": (r"Lambda@Edge",
        "Lambda functions that run at CloudFront edge locations, close to the viewer, so a request can be changed or answered without reaching your origin."),
    "Lambda container image": (r"container image|image to Lambda|Lambda[^.]{0,40}container",
        "Lambda can run a container image, up to 10 GB, instead of a zip of "
        "code. So an application that already ships as a Docker image is not "
        "shut out of Lambda: that is what a question means when it says the "
        "company is willing to change the image, because the image has to use "
        "the Lambda runtime interface. The 15-minute limit still applies. It is "
        "the least to manage of any way of running a container, because there "
        "is no cluster at all."),
    "Choosing where a container runs": (r"container|Docker",
        "Least to manage first. Lambda, where there is no cluster at all, if "
        "the job finishes inside 15 minutes. Then ECS on Fargate: no servers, "
        "but a cluster, a task definition and a service to set up. Then EKS on "
        "Fargate, which is that plus Kubernetes. Then ECS or EKS on EC2, where "
        "the instances are yours to patch and scale. Work down the list and "
        "stop at the first one that fits. What pushes you down it: a job longer "
        "than 15 minutes, something that must stay running, a need for "
        "Kubernetes by name, or a need for particular hardware such as a GPU."),
    "Amazon ECS": (r"\bECS\b|Elastic Container Service",
        "AWS's own container orchestrator: it runs and schedules Docker "
        "containers for you. Simpler than Kubernetes and the one to reach for "
        "unless a question names Kubernetes. Run it on Fargate for no servers, "
        "or on EC2 when you need to choose the hardware."),
    "Amazon EKS": (r"\bEKS\b|Elastic Kubernetes",
        "Managed Kubernetes. Pick this when the question says Kubernetes or "
        "kubectl, or when a team already runs Kubernetes elsewhere. AWS runs "
        "the control plane, but Kubernetes itself is still yours, so it is more "
        "to manage than ECS and is rarely the least-overhead answer."),
    "Amazon EKS Anywhere": (r"EKS Anywhere",
        "Kubernetes managed the same way, but running on hardware you have rather than in an AWS Region, including on Snowball Edge Compute Optimized devices. The answer when a question wants a Kubernetes cluster somewhere with no reliable connection."),
    "AWS Fargate": (r"\bFargate\b",
        "Runs containers without you managing any servers underneath. You give "
        "it a container and it finds somewhere to run it. There is still a "
        "cluster, a task definition and a service to set up, so it is more to "
        "manage than Lambda and far less than owning the instances. The answer "
        "when the work runs longer than 15 minutes or has to stay up."),
    "Amazon ECR": (r"\bECR\b|Elastic Container Registry",
        "A private store for your container images. Images live in one region, so using them elsewhere means copying them."),
    "AWS Elastic Beanstalk": (r"Elastic Beanstalk",
        "You upload code and AWS builds the servers, load balancer and scaling "
        "around it. You still own the resources it creates, and you still pay "
        "for them. It also owns how a new version goes out, which is where the "
        "marks are: pick the deployment policy that matches what the question "
        "is willing to risk."),
    "Beanstalk deployment policies": (r"Elastic Beanstalk",
        "How a new version replaces the old, in rising order of care and cost. "
        "All at once is quickest and drops the service while it happens. "
        "Rolling goes in batches and runs short of capacity meanwhile. Rolling "
        "with an additional batch adds a batch first so full capacity is kept. "
        "Immutable builds a whole new set of instances and throws them away if "
        "anything is wrong. Traffic splitting is immutable plus a trial on real "
        "traffic. Pick the first one that meets what the question will not give "
        "up."),
    "Beanstalk traffic splitting": (r"traffic.split",
        "The canary. A set percentage of live traffic goes to the new version "
        "on new instances for a stated time, and if it stays healthy the rest "
        "follows and the old instances go. The answer whenever a question wants "
        "a new version tried on a slice of real users with the least work, "
        "because it is a setting rather than something to wire up: shifting "
        "traffic by hand with load balancer rules does the same job and is more "
        "to manage."),
    "Immutable deployment": (r"\bimmutable\b",
        "A whole new set of instances is built alongside the old ones, and only "
        "when they are healthy does traffic move. If anything is wrong they are "
        "thrown away and nothing was ever changed, which is why it is the "
        "safest and the easiest to undo. It is the slowest, and briefly pays "
        "for twice the instances."),
    "Blue/green deployment": (r"blue.?green",
        "Two complete environments, one live and one new. You test the new one, "
        "then send traffic to it, and go back by sending it to the old one "
        "again. In Elastic Beanstalk that is a URL swap between two "
        "environments. The answer when going back has to be quick, or when the "
        "change is too big to make in place."),
    "AWS Batch": (r"AWS Batch",
        "Runs large numbers of batch jobs, working out how much compute to "
        "start and when. It queues them and runs them on Fargate or EC2 "
        "underneath, so it adds a scheduler rather than removing the choice. "
        "Worth it for many jobs with dependencies between them, not for one job "
        "that runs in three minutes."),
    "Warm pool": (r"warm pool",
        "Instances kept ready beside an Auto Scaling group, stopped or running but not yet in service, so they can be put to work in seconds. The answer when a question says an instance takes a long time to start up -- a big application to install, a long boot, a cache to fill -- and scaling out therefore arrives too late. A stopped instance in the pool costs only its disk."),
    "EC2 Auto Scaling": (r"Auto Scaling|scaling polic|launch template|launch configuration",
        "Adds and removes EC2 instances automatically to match demand, keeping the count between a minimum and a maximum you set."),
    "Amazon Machine Image (AMI)": (r"\bAMI\b|Amazon Machine Image",
        "A saved template of a disk, used to launch instances that all start identical. An AMI belongs to one region and must be copied to be used in another."),
    "Spot Instances": (r"\bSpot\b",
        "Spare EC2 capacity at up to about 90% off, which AWS can take back with two minutes' warning. Only suitable for work that can be interrupted and retried."),
    "Reserved Instances": (r"Reserved Instance",
        "A one or three year commitment to a certain amount of EC2 usage, for up to about 72% off the on-demand price."),
    "Savings Plans": (r"Savings Plan",
        "A commitment to spend a certain amount per hour for one or three years, in exchange for a lower rate. More flexible than a Reserved Instance about which instance you run."),
    "Dedicated Host": (r"Dedicated Host",
        "A whole physical server reserved for you, where you can see the sockets and cores. Needed when a software licence is tied to physical hardware."),
    "Placement group": (r"placement group",
        "How instances sit on the physical hardware. Cluster packs them for speed, spread separates them for safety, partition splits them across racks."),
    "Cluster placement group": (r"cluster placement",
        "Packs the instances close together on the same fast network, inside one Availability Zone. The lowest latency and the highest throughput between them. It is one zone, so it is the wrong answer whenever the question wants to survive losing a zone, however fast it sounds."),
    "Spread placement group": (r"spread placement",
        "Puts every instance on its own hardware, with its own rack and its own power, and can stretch across Availability Zones. Seven running instances per zone per group at most. The answer when a small number of important instances must never fail together."),
    "Partition placement group": (r"partition placement",
        "Splits the group into partitions, each on its own set of racks, up to seven per Availability Zone. Losing one partition leaves the rest standing. The answer for large distributed systems such as Cassandra, Kafka or HDFS, which already cope with a lost partition."),
    "Instance store": (r"instance store",
        "Disk physically attached to the host. Very fast, and wiped the moment the instance stops. For scratch space, never for anything you need to keep."),
    "AWS Outposts": (r"Outposts",
        "AWS hardware installed in your own building, running the same services and APIs. It is wired back to an AWS Region and needs that link to work, so it is for a datacentre or a factory, not for anywhere that loses its connection."),
    "AWS Local Zones": (r"Local Zone",
        "A small piece of an AWS Region placed in a city, close to users who need single-digit millisecond latency. It is AWS infrastructure in a building somewhere, not something you can take with you."),
    "AWS Wavelength": (r"Wavelength",
        "AWS compute placed inside a telephone company's 5G network, so traffic from a phone reaches it without crossing the public internet. For mobile users on that network, and useless without it."),

    # ---------------- storage ----------------
    "Amazon S3": (r"\bS3\b|Simple Storage Service",
        "Object storage: files in a bucket, fetched over the network. Effectively unlimited and very durable."),
    "S3 storage classes": (r"storage class",
        "One bucket, several prices. Which class an object sits in decides what it costs to keep and what it costs to read back."),
    "S3 Standard": (r"S3 Standard(?!-)|Standard storage class",
        "The default class: data you read often, held across at least three Availability Zones, with no retrieval charge."),
    "S3 Standard-IA": (r"Standard-IA|Standard-Infrequent Access",
        "For data you keep but rarely read. Cheaper to store than Standard, charged to retrieve, still across three Availability Zones. Minimum 30 days."),
    "S3 One Zone-IA": (r"One Zone-IA|One Zone-Infrequent Access",
        "Like Standard-IA and about 20% cheaper, but held in a single Availability Zone. Only for data you could recreate if that zone were lost."),
    "S3 Intelligent-Tiering": (r"Intelligent[- ]Tiering",
        "Watches how each object is actually used and moves that one object between tiers on its own. No retrieval charge, and the tiers it uses for anything recent all give the data back in milliseconds. The answer when the access pattern is unknown, or when it differs from one object to the next, because a rule based on age cannot tell the busy ones from the quiet ones. It costs a small monitoring fee per object, which is why it is not simply the answer to everything."),
    "S3 Glacier": (r"\bGlacier\b",
        "S3 archive storage, in three tiers that differ by how long you wait to get the data back. Which tier is almost always what the question is really asking."),
    "S3 Glacier Instant Retrieval": (r"Glacier Instant",
        "Archive prices with no waiting: the data comes back in milliseconds, like Standard. For things read perhaps once a quarter that still have to appear at once when asked for. Minimum 90 days."),
    "S3 Glacier Flexible Retrieval": (r"Glacier Flexible|Glacier(?! Instant| Deep)",
        "Minutes to hours to get anything back, in exchange for a much lower price. Expedited is one to five minutes, Standard three to five hours, Bulk five to twelve. Minimum 90 days."),
    "S3 Glacier Deep Archive": (r"Deep Archive",
        "The cheapest storage AWS sells, and the slowest: up to twelve hours to retrieve, or forty-eight on the bulk option. For records kept because the law says so. Minimum 180 days."),
    "S3 lifecycle policy": (r"lifecycle (polic|rule|config)",
        "A rule that moves objects to a cheaper class, or deletes them, once they reach a certain age. It goes by age and nothing else, so it moves every object on the same day whether or not anyone is still reading it. That is what makes it the wrong answer when some of the old objects are still popular: those get moved too, and then cost money every time they are read."),
    "S3 versioning": (r"versioning",
        "Keeps every version of an object, so an overwrite or delete can be undone. Required before replication or MFA Delete will work."),
    "S3 Object Lock": (r"Object Lock",
        "Makes objects undeletable for a set period, even by an administrator. Used where records must be retained for compliance."),
    "S3 Cross-Region Replication": (r"Cross-Region Replication|\bCRR\b",
        "Copies new objects automatically into a bucket in another region. Needs versioning on both buckets, and does not touch objects already there."),
    "S3 Transfer Acceleration": (r"Transfer Acceleration",
        "Speeds up long-distance uploads by sending them through a nearby CloudFront edge location onto the AWS network."),
    "S3 presigned URL": (r"presigned|pre-signed",
        "A temporary link that lets someone upload or download one object without needing an AWS account."),
    "Multipart upload": (r"multipart upload",
        "Splits a large upload into parts sent in parallel. Required above 5 GB and sensible above about 100 MB."),
    "Amazon EBS": (r"\bEBS\b|Elastic Block Store",
        "A virtual disk attached to one EC2 instance. Lives in one AZ; its data survives the instance stopping."),
    "EBS volume types": (r"\bgp2\b|\bgp3\b|\bio1\b|\bio2\b|\bst1\b|\bsc1\b|Provisioned IOPS",
        "gp3 is the general-purpose default. io1 and io2 are for guaranteed high IOPS. st1 is cheap sequential throughput, sc1 is the coldest and cheapest."),
    "EBS snapshot": (r"snapshot",
        "A point-in-time backup of a disk, stored in S3 and tied to one region. Copying a snapshot is how you move a volume between zones or regions."),
    "Amazon EFS": (r"\bEFS\b|Elastic File System",
        "A shared file system many Linux servers can mount at once, over NFS. It spans Availability Zones and grows and shrinks on its own."),
    "Amazon FSx": (r"\bFSx\b",
        "Managed file systems, and which one matters: FSx for Windows File Server for Windows and SMB, FSx for Lustre for speed. Picking the family is never the answer; picking the right one is."),
    "FSx for Windows File Server": (r"FSx for Windows",
        "A fully managed Windows file share over SMB, joined to Active Directory. The answer whenever a question says Windows, SMB, or that users need their existing domain logins."),
    "FSx for Lustre": (r"FSx for Lustre",
        "A very fast file system for work that reads enormous amounts of data at once: modelling, genomics, video processing, machine learning training. It can sit in front of an S3 bucket and read from it. The answer when a question says high performance computing, or wants a scratch file system linked to S3."),
    "AWS Storage Gateway": (r"Storage Gateway",
        "A family name rather than a thing you deploy. You pick a type: S3 File Gateway, FSx File Gateway, Volume Gateway or Tape Gateway. The question is always which type, so read the options for the type and not for the family."),
    "S3 File Gateway": (r"\bS3 File Gateway\b|\bFile Gateway\b",
        "Gives machines in your own building an ordinary file share over NFS or SMB. Every file written to it becomes one object in an S3 bucket, so anything else in AWS can read those same files straight from the bucket. The answer when an old application has to carry on writing files and something in AWS needs to read them."),
    "FSx File Gateway": (r"FSx File Gateway",
        "The same idea for Amazon FSx for Windows File Server: a local copy of a Windows file share, so machines in the office get local speed while the files really live in AWS."),
    "Volume Gateway": (r"\bVolume Gateway\b",
        "Gives machines disks over iSCSI rather than a file share. Cached mode keeps the whole disk in AWS with the recently used parts held locally; stored mode keeps the whole disk locally and copies it to AWS. What arrives in S3 is a snapshot of the disk, not your individual files, so nothing else can read them as files. That is what makes it the wrong answer whenever something in AWS has to read the files themselves."),
    "Tape Gateway": (r"\bTape Gateway\b|virtual tape",
        "Pretends to be a tape library, so backup software that only knows how to write tapes carries on working while the tapes are kept in S3 and archived to Glacier. The answer when a company wants to stop buying and storing physical tapes."),
    "AWS Snow Family": (r"Snowball|Snowcone|Snowmobile|Snow Family",
        "Rugged devices AWS posts to you. They do two jobs, not one: moving data the network would take too long to carry, and running compute where there is no usable network at all. Reading one of these questions as being about data transfer when it is really about running something in a disconnected place is the way to get it wrong."),
    "AWS Snowcone": (r"Snowcone",
        "The smallest of them, 8 or 14 TB, light enough to carry and able to run on a battery. It runs EC2 instances too, for a drone, a vehicle or a backpack."),
    "AWS DataSync": (r"DataSync",
        "Copies files between your datacentre and AWS over the network, on a schedule, repeatedly. The online alternative to shipping a Snowball."),
    "AWS Backup": (r"AWS Backup",
        "One place to set backup schedules and retention across many services at once, rather than configuring each separately."),

    "AWS Snowball Edge": (r"Snowball Edge",
        "Comes in two kinds, and which one the question wants decides the answer. Storage Optimized is mostly capacity, for shifting data. Compute Optimized carries up to 104 vCPUs and 416 GB of memory and runs EC2 instances and Kubernetes on the device itself."),
    "Snowball Edge Compute Optimized": (r"Compute Optimi[sz]ed",
        "A rugged computer, not just a disk. Up to 104 vCPUs, 416 GB of memory and 42 TB of storage, running EC2 instances and, with EKS Anywhere, a Kubernetes cluster. More than one device can be run alongside another so the work survives one of them failing, which is how local users get high availability somewhere with nothing to fall back on: a ship, a rig, a construction site. For a Kubernetes cluster with EKS Anywhere, three or more devices is the arrangement AWS documents for that."),

    # ---------------- databases ----------------
    "Amazon RDS": (r"\bRDS\b|Relational Database Service",
        "Managed relational databases: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server and Aurora. AWS handles patching and backups; you get no access to the operating system."),
    "Amazon Aurora": (r"Aurora",
        "AWS's MySQL and PostgreSQL-compatible database. Six copies across three AZs, up to 128 TiB."),
    "Aurora Serverless": (r"Aurora Serverless",
        "Aurora that scales its capacity up and down automatically, so an idle database costs very little."),
    "RDS Multi-AZ": (r"Multi-AZ",
        "A synchronous standby in another AZ that takes over automatically. For availability only; you cannot read from it."),
    "RDS read replica": (r"read replica",
        "An asynchronous readable copy that takes read load off the main database. Can be cross-region; promoted by hand."),
    "Amazon DynamoDB": (r"DynamoDB",
        "A serverless key-value database, single-digit milliseconds at any size. You design around a partition key, not joins."),
    "DynamoDB Accelerator (DAX)": (r"\bDAX\b",
        "An in-memory cache in front of DynamoDB that brings reads down to microseconds. It helps reads only, not writes."),
    "DynamoDB Global Tables": (r"Global Table",
        "The same DynamoDB table kept in several regions at once, writable in all of them."),
    "Amazon ElastiCache": (r"ElastiCache|Memcached|\bRedis\b",
        "Managed in-memory caching. Redis adds persistence, failover and data structures; Memcached is a simpler multi-threaded cache."),
    "Amazon Redshift": (r"Redshift",
        "A data warehouse for analytics over large structured datasets. Built for reporting, not transactions."),
    "Amazon Neptune": (r"Neptune",
        "A graph database, for data that is mostly about relationships: social networks, fraud rings, recommendations."),
    "Amazon DocumentDB": (r"DocumentDB",
        "A managed document database that speaks MongoDB's API."),
    "Amazon QLDB": (r"\bQLDB\b|Quantum Ledger",
        "A ledger database with a complete, cryptographically verifiable history of every change, owned by a single trusted party."),
    "AWS DMS": (r"\bDMS\b|Database Migration Service",
        "Moves a database into AWS while the original keeps running, so the switchover is short. Paired with the Schema Conversion Tool when the engine changes."),
    "RDS Proxy": (r"RDS Proxy",
        "Pools and reuses database connections, so many short-lived clients such as Lambda functions do not exhaust the database. It does not add read capacity."),

    "AWS Schema Conversion Tool": (r"Schema Conversion Tool|\bSCT\b",
        "Rewrites a database's schema and stored code for a different engine. Paired with DMS when the migration changes engine, not just location."),

    # ---------------- networking ----------------
    "Amazon VPC": (r"\bVPC\b|Virtual Private Cloud",
        "Your own private network inside AWS, with its own address range, subnets and routing."),
    "Subnet": (r"subnet",
        "A slice of a VPC's address range, living in exactly one Availability Zone. It is public if its route table has a path to an internet gateway."),
    "Security group": (r"security group",
        "A stateful firewall on an instance: replies to allowed traffic come back automatically, and it can only allow, never deny."),
    "Network ACL": (r"network ACL|\bNACL\b",
        "A stateless firewall on a subnet: traffic must be allowed both ways, and unlike a security group it can deny."),
    "NAT gateway": (r"NAT gateway|NAT instance",
        "Lets servers in a private subnet reach the internet to fetch updates, while stopping anything on the internet from starting a connection to them."),
    "Internet gateway": (r"internet gateway",
        "The VPC's door to the internet. A subnet is only public if its route table points at one."),
    "VPC peering": (r"VPC peering",
        "A private link between two VPCs. It is not transitive, so A to B and B to C does not give A to C, and the address ranges must not overlap."),
    "AWS Transit Gateway": (r"Transit Gateway",
        "A hub that connects many VPCs and on-premises networks to each other, which peering cannot do once there are more than a few."),
    "AWS PrivateLink": (r"PrivateLink",
        "A private door into one building, not the road that gets you there. It gives you a private address inside a VPC for one specific service, with no peering and without crossing the internet. It creates no network path and assumes you already have one. The trap: when a question says the solution must not use the public internet, this option looks right on the word private alone. Ask whether the option gives you a wire out of your own building. Direct Connect and Site-to-Site VPN do. This does not, so from a data centre it still needs one of them underneath."),
    "VPC endpoint": (r"VPC endpoint|gateway endpoint|interface endpoint",
        "A private route to an AWS service, so traffic never leaves AWS. Gateway endpoints serve S3 and DynamoDB and are free, but they are a route inside one VPC only: they cannot be reached from your own network over Direct Connect or a VPN, and they do not do IPv6. An interface endpoint is a network card in your subnet, charged by the hour and by the traffic, and it is the kind that on-premises systems can reach. Everything other than S3 and DynamoDB is an interface endpoint anyway."),
    "AWS Direct Connect": (r"Direct Connect",
        "The road. A dedicated physical circuit between your data centre and AWS, which creates a network path that did not exist before. Latency is consistent because the circuit is yours, and traffic never touches the public internet. That combination, steady low latency and no internet, is what only this can give you. It takes weeks or months to install, so a question in a hurry wants a VPN instead."),
    "AWS Client VPN": (r"Client VPN",
        "An encrypted tunnel for one person at a time, from a laptop into a VPC. It is for staff who need to reach private resources while away from the office, not for joining two networks: there is no site at the other end, and it runs over the public internet. Whenever a question is about a data centre rather than people, this is the wrong shape."),
    "Site-to-Site VPN": (r"Site-to-Site VPN|virtual private gateway|customer gateway",
        "An encrypted tunnel from your network to AWS over the ordinary internet. The right shape for joining two sites, and up the same day, which is why it wins whenever cost or speed of setup is the point. But it rides the public internet, so latency varies with whatever else is happening out there. That rules it out when a question asks for consistent or predictable latency, and it is often run as the backup for a Direct Connect line."),
    "Amazon Route 53": (r"Route ?53",
        "AWS's DNS. Routes by latency, geography or weight, and away from anything failing a health check."),
    "Amazon CloudFront": (r"CloudFront",
        "A content delivery network. It caches your content at edge locations around the world so users are served from somewhere near them."),
    "AWS Global Accelerator": (r"Global Accelerator",
        "Two fixed IP addresses routing over the AWS backbone to the nearest healthy region. No caching, and any protocol, not just web."),
    "Application Load Balancer (ALB)": (r"Application Load Balancer|\bALB\b",
        "A load balancer that understands HTTP, so it can route on the URL path, the hostname or a header. It has no fixed IP address."),
    "Network Load Balancer (NLB)": (r"Network Load Balancer|\bNLB\b",
        "A load balancer that works at the TCP and UDP level. Extremely fast, and it can have a fixed IP address."),
    "VPC Flow Logs": (r"Flow Logs",
        "A record of which traffic was allowed and which was rejected in your VPC. The first place to look when a connection is being blocked and you do not know why."),
    "Elastic IP": (r"[Ee]lastic IP",
        "A fixed public address you own and can move between instances."),
    "CIDR block": (r"\bCIDR\b",
        "The notation for an address range. The number after the slash says how many addresses: /32 is one address, /24 is 256, /16 is 65,536, and /0 means everything."),

    # ---------------- security ----------------
    "AWS IAM": (r"\bIAM\b|Identity and Access Management",
        "Controls who can do what. Users and roles are given policies, and the rule is that an explicit deny always beats an allow."),
    "IAM role": (r"IAM role|instance profile|AssumeRole",
        "A set of permissions something can borrow temporarily, with no password or long-lived key. This is how an EC2 instance or a Lambda function should get its access."),
    "AWS STS": (r"\bSTS\b|Security Token Service",
        "Issues the short-lived credentials behind a role, used for cross-account access and for federating outside identities."),
    "AWS Organizations": (r"Organizations",
        "Groups many AWS accounts under one roof for central billing and central control."),
    "Service Control Policy (SCP)": (r"\bSCP\b|service control polic",
        "A ceiling on what accounts in an organization are allowed to do. It can only take permissions away, never grant them, and it never restricts the management account."),
    "AWS Control Tower": (r"Control Tower",
        "Sets up new AWS accounts with guard rails and logging already in place."),
    "Amazon Cognito": (r"Cognito",
        "Handles sign-up and sign-in for your application's users, and can swap a social or corporate login for temporary AWS credentials."),
    "AWS KMS": (r"\bKMS\b|Key Management Service|customer master key|\bCMK\b",
        "Creates and controls encryption keys, and is wired into nearly every AWS service. It encrypts up to 4 KB directly; anything larger uses a data key it hands out."),
    "AWS CloudHSM": (r"CloudHSM",
        "A dedicated hardware security module that only you use, where AWS cannot see the keys. For rules that demand single-tenant, FIPS 140-2 Level 3 hardware."),
    "AWS IAM Identity Center": (r"IAM Identity Center|Single Sign-On|\bSSO\b",
        "One sign-in across every account in an organisation, and the place to connect an existing company directory. It was called AWS Single Sign-On. The answer when a question wants people to use the logins they already have across many accounts, rather than a user per account."),
    "AWS Secrets Manager": (r"Secrets Manager",
        "Stores passwords and API keys, and can rotate a database password automatically on a schedule."),
    "SSM Parameter Store": (r"Parameter Store",
        "A free place to keep configuration values, with an encrypted option. No built-in rotation."),
    "AWS Certificate Manager (ACM)": (r"\bACM\b|Certificate Manager",
        "Issues and renews TLS certificates at no cost. A certificate for CloudFront must be created in the us-east-1 region."),
    "WAF IP set": (r"IP set|IP rule set|IP match",
        "A list of addresses and ranges that a WAF rule either allows or "
        "refuses, holding up to ten thousand each, and a web ACL can use "
        "several. That is what makes it the answer when a question has "
        "thousands of addresses to let through: a network ACL stops at about "
        "twenty rules and forty at the very most, and a security group at "
        "sixty, so neither can hold a list that long. Changing the list is an "
        "edit to the set, with nothing redeployed."),
    "AWS WAF": (r"\bWAF\b",
        "A firewall for web traffic, attached to a load balancer, a CloudFront "
        "distribution or an API, and checked at the edge before the request "
        "reaches anything of yours. It blocks things like SQL injection and "
        "cross-site scripting, can rate-limit a single address, and can allow "
        "or refuse by IP address using an IP set."),
    "AWS Shield": (r"\bShield\b",
        "Protection against traffic floods. Standard is on for everyone at no charge. Advanced is paid, and is the one the exam means when it talks about a response team, cost protection for the bill a flood runs up, or protection beyond the network layer."),
    "AWS Shield Advanced": (r"Shield Advanced",
        "The paid tier. Adds a response team you can call, refunds the scaling charges an attack causes, and covers application-layer floods alongside AWS WAF. The answer when a question mentions a dedicated team, a refund, or a service-level guarantee during an attack."),
    "Amazon GuardDuty": (r"GuardDuty",
        "Watches your logs for signs of compromise, such as unusual API calls or crypto-mining. It detects; it does not scan software."),
    "Amazon Inspector": (r"Inspector",
        "Scans your EC2 instances, container images and Lambda functions for known software vulnerabilities."),
    "Amazon Macie": (r"Macie",
        "Looks through S3 for sensitive data such as personal details or card numbers."),
    "AWS Security Hub": (r"Security Hub",
        "Collects findings from GuardDuty, Inspector, Macie, Config and others into one list, and scores you against standards."),
    "Amazon Detective": (r"Detective",
        "Helps work out the root cause of a security finding after it has been raised."),
    "AWS Directory Service": (r"Directory Service|Active Directory",
        "Managed Microsoft Active Directory, or a connection to the one you already run. Needed by FSx for Windows and WorkSpaces."),
    "Multi-factor authentication (MFA)": (r"\bMFA\b|multi-factor",
        "A second proof of identity beyond the password, such as a code from a phone or a hardware key."),

    # ---------------- integration ----------------
    "Amazon SQS": (r"\bSQS\b|Simple Queue Service",
        "A queue holding messages until a worker takes them, so a busy front end cannot swamp the back end. A standard queue may deliver a message more than once and in any order; a FIFO queue does neither."),
    "SQS FIFO queue": (r"\bFIFO\b",
        "A queue that keeps messages in order and delivers each one once. Its name must end in .fifo. The trade is speed: 300 messages a second, 3,000 if you send them ten to a call, and more only in high-throughput mode. A standard queue has no such ceiling."),
    "SQS message deduplication": (r"deduplicat|dedupe|duplicate message",
        "How a FIFO queue drops a repeat. Every message carries a deduplication ID, either one you set or, with content-based deduplication switched on, a hash of the message body. A second message with the same ID inside a five-minute window is accepted and quietly thrown away. Past five minutes it counts as new, so a retry that slow is processed twice."),
    "SQS message group ID": (r"message group",
        "The label saying which messages must stay in order relative to each other. A FIFO queue orders within one group, not across the whole queue, so different groups are handled side by side. One group for everything gives strict order but no work in parallel."),
    "SQS visibility timeout": (r"visibility timeout",
        "How long a message stays hidden after a worker takes it. Shorter than the processing time and the message gets handled twice."),
    "Dead-letter queue": (r"dead-letter|dead letter",
        "Where a message goes after failing to be processed a set number of times, so one bad message does not block the queue."),
    "Amazon SNS": (r"\bSNS\b|Simple Notification Service",
        "Publishes one message to many subscribers at once: queues, functions, email addresses, phone numbers or web endpoints."),
    "Amazon EventBridge": (r"EventBridge|CloudWatch Events",
        "Routes events between services based on what is inside the event, and can run things on a schedule. Also receives events from outside SaaS products."),
    "AWS Step Functions": (r"Step Functions",
        "Strings several steps into one workflow, handling the retries, branches and waiting for you, so your code does not have to."),
    "Amazon MQ": (r"Amazon MQ",
        "Managed RabbitMQ or ActiveMQ, for applications that already speak a standard broker protocol and are being moved as-is."),
    "Amazon Kinesis": (r"\bKinesis\b",
        "The family for data arriving continuously. Data Streams keeps the records so several applications can read them in order; Data Firehose just delivers them somewhere and keeps nothing. Which one is the question."),
    "Amazon Kinesis Data Streams": (r"Kinesis Data Stream|Kinesis Stream",
        "Takes in a continuous stream of records and keeps them, so several applications can read the same data, in order, and go back over it."),
    "Kinesis Data Firehose": (r"Firehose",
        "Delivers a stream straight into S3, Redshift, OpenSearch or Splunk with no code. It buffers for about a minute, so it is near-real-time rather than instant."),
    "Amazon API Gateway": (r"API Gateway",
        "A managed front door for an API. It handles authentication, throttling and caching in front of Lambda or any other backend."),
    "API Gateway HTTP API": (r"HTTP API",
        "The newer, plainer kind of API Gateway API: cheaper, quicker, and the "
        "only one that can check a JWT by itself. Point it at your identity "
        "provider and it validates the signature and the claims with no code of "
        "yours in the way. It gives up the extras to do it: no API keys or "
        "usage plans, no request validation, no caching, no AWS WAF, no "
        "resource policies and no private endpoint."),
    "API Gateway REST API": (r"REST API",
        "The full-featured kind of API Gateway API. API keys and usage plans, "
        "request validation, caching, AWS WAF, resource policies and a private "
        "endpoint inside a VPC all belong to this one. For tokens it has a "
        "Cognito user pool authorizer or a Lambda authorizer, but no built-in "
        "JWT check, so a token from somebody else's identity provider means "
        "writing a Lambda authorizer."),
    "JWT": (r"\bJWT\b|JSON Web Token|bearer token",
        "A signed ticket the caller carries, saying who they are and what they "
        "may do. Whatever receives it checks the signature and reads the claims "
        "inside, rather than calling the identity provider on every request. An "
        "HTTP API can do that check on its own; a REST API needs a Lambda "
        "authorizer unless the token came from a Cognito user pool."),
    "Lambda authorizer": (r"Lambda authorizer|custom authorizer",
        "A function API Gateway calls to decide whether a request may go on. "
        "The answer whenever the checking is yours to define, or the token is "
        "of a kind the API cannot check for itself. The verdict is cached, so "
        "it is not run on every single call."),
    "API Gateway WebSocket API": (r"WebSocket API",
        "A connection the client and the server both keep open, so the server "
        "can push without being asked. For chat, live scores and anything else "
        "where the news comes from the server's side."),
    "AWS AppSync": (r"AppSync",
        "A managed GraphQL API, with offline syncing for mobile applications."),

    "Amazon SES": (r"\bSES\b|Simple Email Service",
        "Sends and receives email at volume: transactional messages, newsletters, and the deliverability reporting that goes with them."),

    # ---------------- analytics ----------------
    "Amazon Athena": (r"\bAthena\b",
        "Runs SQL straight against files sitting in S3, with nothing to set up. You pay for the data each query reads."),
    "AWS Glue": (r"\bGlue\b",
        "Serverless data preparation, plus a catalogue that records what your data looks like so Athena and Redshift can query it."),
    "Amazon EMR": (r"\bEMR\b|Elastic MapReduce",
        "Runs Hadoop, Spark, Hive and similar frameworks on EC2 instances you can see and log into."),
    "Amazon OpenSearch Service": (r"OpenSearch|Elasticsearch",
        "Full-text search and log analytics, with dashboards."),
    "Amazon QuickSight": (r"QuickSight",
        "Business intelligence dashboards for non-technical readers."),

    # ---------------- management ----------------
    "Amazon CloudWatch": (r"CloudWatch",
        "Collects metrics, logs and alarms, and tells you how things are performing. Memory and disk space are not collected unless you install the agent."),
    "AWS CloudTrail": (r"CloudTrail",
        "Records who called which AWS API, when, and from where. The audit trail, as opposed to CloudWatch's performance view."),
    "AWS Config": (r"AWS Config",
        "Records how your resources were configured over time and checks them against rules, so you can see what changed and whether it is compliant."),
    "AWS CloudFormation": (r"CloudFormation",
        "Describes your infrastructure in a template file so the same stack can be built again identically."),
    "AWS Systems Manager": (r"Systems Manager|\bSSM\b",
        "A toolbox for running and maintaining instances: shell access without opening ports, patching, running commands across a fleet, and storing parameters."),
    "Session Manager": (r"Session Manager",
        "Gives a shell on an instance with no open inbound port, no SSH key and no bastion host, and records the whole session."),
    "AWS Trusted Advisor": (r"Trusted Advisor",
        "Checks your account against best practice in five areas: cost, performance, fault tolerance, security and service limits."),
    "AWS Compute Optimizer": (r"Compute Optimizer",
        "Looks at real usage and tells you where an instance or volume is bigger than it needs to be."),
    "AWS Cost Explorer": (r"Cost Explorer",
        "Shows and forecasts your spending, broken down by service, tag or account."),
    "AWS Budgets": (r"AWS Budgets",
        "Alerts you when spending or usage passes a threshold you set."),
    "AWS X-Ray": (r"X-Ray",
        "Traces a single request as it passes through several services, so you can see which step is slow or failing."),
    "AWS OpsWorks": (r"OpsWorks",
        "Managed Chef and Puppet servers. The answer only when a team already runs Chef or Puppet and is bringing it with them."),
    "AWS CLI": (r"AWS CLI\b|command line interface",
        "The command line tool for AWS. Worth noting when a question contrasts doing something by script against doing it in the console."),
    "AWS Service Catalog": (r"Service Catalog",
        "A list of approved infrastructure templates teams can deploy for themselves without raising a ticket."),

    # ---------------- concepts ----------------
    "Availability Zone": (r"Availability Zone|\bAZ\b",
        "One or more separate datacentres within a region, with their own power and networking. Spreading across zones is how you survive one of them failing."),
    "Region": (r"\bRegion\b",
        "A geographic area containing several Availability Zones. Spreading across regions is how you survive a whole region failing."),
    "Edge location": (r"edge location",
        "A small CloudFront site close to users, used for caching. There are far more of these than there are regions."),
    "High availability": (r"highly available|high availability",
        "Designed to keep working when a component fails, usually by running in more than one Availability Zone with something in front sharing the load."),
    "Disaster recovery": (r"disaster recovery|\bRTO\b|\bRPO\b|pilot light|warm standby",
        "Planning for a whole region going down. RTO is how long you may be offline; RPO is how much recent data you may lose."),
    "Encryption at rest": (r"encrypt",
        "Scrambling stored data so it is unreadable without the key. Encryption in transit does the same for data moving over the network, usually with TLS."),
    "Least privilege": (r"least privilege",
        "Giving an identity only the permissions it actually needs, and nothing more."),
    "Decoupling": (r"decoupl",
        "Putting a queue or a topic between two parts of a system so each can fail, restart or scale without breaking the other."),
}


def compile_glossary():
    """Return [(name, compiled pattern, definition)], longest name first.

    Longest first so that a specific term is reported before a general one when
    both match, which keeps the hint's first lines the most relevant.
    """
    import re
    items = []
    for name, (pattern, what) in GLOSSARY.items():
        items.append((name, re.compile(pattern, re.I), what))
    items.sort(key=lambda t: -len(t[0]))
    return items



# --------------------------------------------------------------------------
# Patterns that cannot match, caught here rather than noticed later.
#
# A pattern written without the r prefix turns \b into a backspace character.
# It still compiles, still runs, and matches nothing, so the only sign is a
# term that quietly never appears. That has happened twice: once to a term for
# an exam option worth three questions, and once to a pair of service names.
# Both were found by counting matches by hand, which is luck rather than a
# process, so the same three checks the diagram library makes are made here.
# --------------------------------------------------------------------------
def _audit_patterns() -> None:
    control, doubled, broken, empty = [], [], [], []
    for name, (pattern, what) in GLOSSARY.items():
        if any(ord(c) < 32 for c in pattern + what):
            control.append(name)
        if "\\\\" in pattern:
            doubled.append(name)
        if not pattern.strip() or not what.strip():
            empty.append(name)
            continue
        try:
            re.compile(pattern)
        except re.error as e:
            broken.append(f"{name} ({e})")

    trouble = []
    if control:
        trouble.append(
            "a control character, which means a missing r prefix on the "
            "string: " + ", ".join(control))
    if doubled:
        trouble.append(
            "a doubled backslash, which matches a real backslash and so "
            "matches nothing: " + ", ".join(doubled))
    if broken:
        trouble.append("a pattern that will not compile: " + ", ".join(broken))
    if empty:
        trouble.append("nothing to match, or nothing to say: " + ", ".join(empty))
    if trouble:
        raise AssertionError("glossary: " + "; ".join(trouble))


_audit_patterns()

if __name__ == "__main__":
    print(f"{len(GLOSSARY)} terms defined")
    import re
    for name, (pattern, what) in GLOSSARY.items():
        try:
            re.compile(pattern)
        except re.error as e:
            print(f"  BAD PATTERN  {name}: {e}")
        if len(what) < 40:
            print(f"  THIN         {name}: {what!r}")
