#!/usr/bin/env python3
"""
The handful of choices the exam keeps asking you to make.

Eighteen hundred questions are not eighteen hundred decisions. They come back
to about thirty: which storage class, where to run a container, how to
decouple, which load balancer, where to keep a secret. Together they reach
most of the bank, and the rest is trivia with no choice in it.

Written as a list of branches rather than a flowchart, deliberately. The same
decision drawn as boxes and arrows fans out seven ways, and at the width of a
phone the conditions on the arrows -- which are the whole point -- shrink to
nothing. One branch per line reads top to bottom, needs no tracing across the
page, and works at any width.

Each one is:

    id      short and stable
    title   what the choice is, as a question
    area    which part of the exam it belongs to
    choices the distinct destinations. A question is asking this decision when
            two or more of them turn up among its options, which is what being
            asked to choose actually looks like.
    stem    the problem this choice exists to solve, as the question states it.
            A well-made question often pairs one real destination with three
            distractors nobody would list, so one destination counts when the
            question says it has this problem.
    unless  a phrase that rules it out
    rows    (what the question says, what that means you pick)
    traps   what the question is really testing, which is usually a limit or a
            minimum that makes the obvious answer wrong
"""

from __future__ import annotations

import re

DECISIONS: list[dict] = [

    {
        "id": "s3-class",
        "stem": r"storage cost|cost of storage|access(ed)? (less|infrequent|rarely)|archiv|retain|older than|after \d+ days|lifecycle|how often",
        "choices": [
            r"S3 Standard(?!-IA)|Standard storage class",
            r"Intelligent-Tiering",
            r"Standard-IA|Standard Infrequent",
            r"One Zone",
            r"Glacier Instant",
            r"Glacier Flexible|Glacier(?!.{0,12}(Instant|Deep))",
            r"Deep Archive",
        ],
        "title": "Which S3 storage class",
        "area": "storage",
        "rows": [
            ("read often, and you know it will be", "S3 Standard"),
            ("nobody can say how often", "Intelligent-Tiering"),
            ("rarely, but wanted at once", "Standard-IA"),
            ("rarely, and you could re-create it", "One Zone-IA"),
            ("archived, wanted in milliseconds", "Glacier Instant Retrieval"),
            ("archived, minutes will do", "Glacier Flexible Retrieval"),
            ("archived, hours will do, cheapest of all", "Glacier Deep Archive"),
        ],
        "traps": [
            "Infrequent access charges for a minimum of 30 days and Glacier for 90, "
            "so something short-lived costs more there than in Standard.",
            "One Zone is the only one that does not survive losing a zone. S3 Express "
            "One Zone is a different thing again: the fastest and dearest, not an "
            "archive.",
            "Where the pattern is unknown, Intelligent-Tiering beats guessing: it "
            "moves each object on its own and charges no retrieval fee.",
        ],
    },

    {
        "id": "container-where",
        "stem": r"container|Docker image|microservice",
        "choices": [
            r"Lambda",
            r"Fargate",
            r"\bECS\b",
            r"\bEKS\b",
            r"\bBatch\b",
            r"\bEC2\b.{0,40}container|container.{0,40}\bEC2\b",
        ],
        "title": "Where to run a container",
        "area": "compute",
        "rows": [
            ("it finishes inside 15 minutes", "Lambda, with a container image"),
            ("longer than that, or always on", "ECS on Fargate"),
            ("the question says Kubernetes", "EKS on Fargate"),
            ("you must choose the hardware, or need a GPU", "ECS or EKS on EC2"),
            ("many queued jobs with an order between them", "AWS Batch"),
            ("it must run on your own hardware", "ECS Anywhere or EKS Anywhere"),
        ],
        "traps": [
            "Work down the list and stop at the first that fits: each step down is "
            "more to manage, so the one above is the least-overhead answer.",
            "An existing Docker image is no reason to rule out Lambda. It runs an "
            "image up to 10 GB; that is what a question means by being willing to "
            "change the image.",
            "Fargate still has a cluster, a task definition and a service. It is less "
            "than owning instances and more than Lambda.",
        ],
    },

    {
        "id": "db-engine",
        "stem": r"(new|choose|select|which) .{0,40}database|migrat\w+ .{0,30}database|relational|non-relational|NoSQL|key-value|document database|graph database|time series",
        "choices": [
            r"Aurora",
            r"DynamoDB",
            r"RDS for (MySQL|PostgreSQL|MariaDB|Oracle|SQL)",
            r"DocumentDB",
            r"Neptune",
            r"Redshift",
            r"Timestream",
            r"Keyspaces",
        ],
        "title": "Which database",
        "area": "database",
        "rows": [
            ("joins, transactions, existing SQL", "RDS"),
            ("the same, but faster and surviving a Region", "Aurora"),
            ("key-value, any scale, single-digit milliseconds", "DynamoDB"),
            ("the load comes and goes, or is unknown", "Aurora Serverless, or "
                                                       "DynamoDB on-demand"),
            ("documents, MongoDB wording", "DocumentDB"),
            ("relationships between things, graph wording", "Neptune"),
            ("reporting across a great deal of history", "Redshift"),
            ("readings over time, from devices", "Timestream"),
        ],
        "traps": [
            "Aurora is still relational. A question wanting to leave SQL behind wants "
            "DynamoDB, not Aurora.",
            "Multi-AZ is not a read scaler for an RDS DB instance: its standby serves "
            "nothing. A Multi-AZ DB cluster and Aurora are different, and do serve "
            "reads.",
            "DynamoDB global tables are the active-active answer across Regions. An "
            "Aurora global database has one writer.",
        ],
    },

    {
        "id": "decouple",
        "stem": r"decoupl|loosely coupled|buffer|spike|asynchron|between the|must not be lost|order of|fan out",
        "choices": [
            r"\bSQS\b",
            r"\bSNS\b",
            r"EventBridge",
            r"Kinesis",
            r"Step Functions",
            r"\bMQ\b|ActiveMQ|RabbitMQ",
        ],
        "title": "How to put something in between",
        "area": "integration",
        "rows": [
            ("one sender, one worker, nothing lost", "SQS"),
            ("order matters, and no duplicates", "SQS FIFO"),
            ("one message, several places at once", "SNS, to several queues"),
            ("route on what is inside the event", "EventBridge"),
            ("a stream several readers can replay", "Kinesis Data Streams"),
            ("straight into S3 or Redshift, no code", "Kinesis Data Firehose"),
            ("steps, retries and waiting for a person", "Step Functions"),
        ],
        "traps": [
            "A queue holds work for one worker to take. A topic hands a copy to every "
            "subscriber. A question wanting both is SNS in front of SQS.",
            "Firehose keeps nothing, so it cannot be replayed or read twice. That is "
            "what separates it from Data Streams.",
            "Order in a Kinesis stream holds within a shard, not across the stream.",
        ],
    },

    {
        "id": "balancer",
        "stem": r"load balanc|distribute (the )?traffic|in front of|static IP|route (the )?requests",
        "choices": [
            r"Application Load Balancer|\bALB\b",
            r"Network Load Balancer|\bNLB\b",
            r"Gateway Load Balancer|\bGWLB\b",
            r"Global Accelerator",
            r"CloudFront",
        ],
        "title": "Which load balancer",
        "area": "networking",
        "rows": [
            ("routing on path, host or header", "Application Load Balancer"),
            ("a fixed address, or an allow-list", "Network Load Balancer"),
            ("TCP or UDP rather than web traffic", "Network Load Balancer"),
            ("millions of requests, lowest latency", "Network Load Balancer"),
            ("traffic through a firewall appliance", "Gateway Load Balancer"),
            ("fixed addresses and more than one Region", "Global Accelerator"),
            ("caching static content near the user", "CloudFront"),
        ],
        "traps": [
            "Only an ALB can authenticate at the edge, redirect to HTTPS, return a "
            "fixed response, or send to Lambda.",
            "Global Accelerator carries any protocol and caches nothing. CloudFront "
            "caches and is for web traffic.",
            "AWS WAF attaches to an ALB, CloudFront or an API, never to an NLB.",
        ],
    },

    {
        "id": "read-scale",
        "stem": r"report(ing)? quer|read (traffic|queries|load|performance)|without (affecting|impacting)|offload|read-heavy|same quer|repeated(ly)? (read|quer)|latency of (the )?(read|quer)",
        "choices": [
            r"read replica",
            r"ElastiCache",
            r"\bDAX\b",
            r"reader endpoint",
            r"Multi-AZ",
        ],
        "title": "How to take load off a database",
        "area": "database",
        "rows": [
            ("the same queries over and over", "ElastiCache"),
            ("the same, and it is DynamoDB", "DAX"),
            ("more reads than one instance can serve", "Read replicas"),
            ("readers in another Region", "A cross-Region read replica"),
            ("sessions shared between servers", "ElastiCache for Redis"),
            ("writes are the problem, not reads", "A bigger instance, or sharding"),
        ],
        "traps": [
            "ElastiCache does not fetch from the database for you. The application "
            "misses, queries, and writes the value in. DAX does go to the table "
            "itself, which is the difference.",
            "A read replica is promoted by hand, so it is a recovery tool rather than "
            "one that fails over on its own.",
            "DAX serves eventually consistent reads only; a strongly consistent read "
            "goes to the table.",
        ],
    },

    {
        "id": "files-in",
        "stem": r"on-premises|on premises|data cent(er|re)|migrat\w+ .{0,30}data|transfer .{0,30}(data|files)|existing (NFS|SMB|tape)",
        "choices": [
            r"Storage Gateway",
            r"DataSync",
            r"Snowball|Snowcone|Snowmobile",
            r"Transfer Family",
            r"Direct Connect",
            r"\bVPN\b",
        ],
        "title": "How to get data in from your own building",
        "area": "storage",
        "rows": [
            ("a lot, once, and the line is too slow", "Snowball Edge"),
            ("a lot, repeatedly, over the network", "DataSync"),
            ("carry on using SFTP", "Transfer Family"),
            ("a file share backed by a bucket", "S3 File Gateway"),
            ("keep working locally, with a copy in AWS", "Volume Gateway, cached"),
            ("retire a tape library", "Tape Gateway"),
            ("a steady private line for everything", "Direct Connect"),
        ],
        "traps": [
            "Work out how long the data would take over the line you have. Past "
            "roughly a week, posting a device wins.",
            "Snowball Edge comes in two kinds. Storage Optimized is for moving data; "
            "Compute Optimized is for running work where there is no connection.",
            "Direct Connect takes weeks to install, so it is never the answer to "
            "something needed this month.",
        ],
    },

    {
        "id": "shared-files",
        "stem": r"shared (file|storage)|same files|concurrently|many (instances|servers)|file system|mount",
        "choices": [
            r"\bEFS\b",
            r"FSx for Windows",
            r"FSx for Lustre",
            r"NetApp|ONTAP",
            r"OpenZFS",
            r"\bEBS\b",
        ],
        "title": "Which file system",
        "area": "storage",
        "rows": [
            ("many Linux servers, across zones", "EFS"),
            ("Windows, SMB, Active Directory", "FSx for Windows File Server"),
            ("speed for modelling or training", "FSx for Lustre"),
            ("an existing NetApp estate", "FSx for NetApp ONTAP"),
            ("one server, one zone, a plain disk", "EBS"),
            ("objects rather than files", "S3"),
        ],
        "traps": [
            "An EBS volume lives in one zone. Multi-Attach exists but does not cross "
            "zones, and an ordinary file system cannot safely be shared that way.",
            "EFS throughput: bursting goes by how much is stored and runs out of "
            "credit; elastic rises with the work and suits a spike nobody can size.",
            "FSx for Lustre links to a bucket and presents the objects as files, which "
            "is what training jobs want.",
        ],
    },

    {
        "id": "ec2-buy",
        "stem": r"cost|cheapest|reduce .{0,20}spend|interrupt|steady state|committed|licens",
        "choices": [
            r"Spot",
            r"Reserved Instance",
            r"Savings Plan",
            r"On-Demand",
            r"Dedicated Host",
            r"Dedicated Instance",
        ],
        "title": "How to pay for EC2",
        "area": "cost",
        "rows": [
            ("steady, and running all the time", "Savings Plan, or Reserved Instances"),
            ("steady, and you may change instance type", "Compute Savings Plan"),
            ("it can be interrupted and tried again", "Spot"),
            ("short, unpredictable, or being measured", "On-Demand"),
            ("a licence counted by socket or core", "Dedicated Host"),
            ("you need it off other tenants' hardware", "Dedicated Instance"),
        ],
        "traps": [
            "Spot is taken back with two minutes' warning, so it is never the answer "
            "for anything that cannot be interrupted.",
            "A Dedicated Host is the one that shows you sockets and cores, which is "
            "what a bring-your-own-licence question needs. A Dedicated Instance does "
            "not.",
            "A Savings Plan is a pound-per-hour commitment, not a reservation, so it "
            "keeps paying off when the instance type changes.",
        ],
    },

    {
        "id": "network-join",
        "stem": r"on-premises|on premises|data cent(er|re)|hybrid|private connect|without (traversing|using) the (public )?internet|between VPCs",
        "choices": [
            r"Direct Connect",
            r"Site-to-Site VPN",
            r"Transit Gateway",
            r"VPC peering",
            r"PrivateLink",
            r"VPC endpoint",
        ],
        "title": "How to join two networks",
        "area": "networking",
        "rows": [
            ("steady, predictable, never the internet", "Direct Connect"),
            ("needed this week, cost matters", "Site-to-Site VPN"),
            ("both, with the VPN as the fallback", "Direct Connect, VPN backup"),
            ("exactly two VPCs", "VPC peering"),
            ("more than a few VPCs, or many sites", "Transit Gateway"),
            ("reach one service, not a whole network", "PrivateLink"),
            ("reach S3 or DynamoDB from inside a VPC", "A gateway VPC endpoint"),
        ],
        "traps": [
            "PrivateLink creates no network path. From your own building it still "
            "needs Direct Connect or a VPN underneath.",
            "A gateway endpoint works only from inside the VPC and only over IPv4. "
            "From on premises you need the interface kind.",
            "VPC peering is not transitive, and Direct Connect reaches a transit "
            "gateway only through a Direct Connect gateway.",
        ],
    },

    {
        "id": "encrypt",
        "stem": r"encrypt|at rest|key|complian|audit",
        "choices": [
            r"SSE-KMS|\bKMS\b",
            r"SSE-S3",
            r"SSE-C\b",
            r"client-side",
            r"CloudHSM",
            r"Bucket Key",
        ],
        "title": "Who holds the key",
        "area": "security",
        "rows": [
            ("encrypted, and nobody asked who by", "SSE-S3"),
            ("you must say who may use the key", "SSE-KMS, a customer managed key"),
            ("every use must be in an audit trail", "SSE-KMS, and CloudTrail"),
            ("you hold the key and AWS never sees it", "SSE-C, or client-side"),
            ("a hardware module you control", "CloudHSM"),
            ("the KMS bill is the problem", "An S3 Bucket Key"),
        ],
        "traps": [
            "The data key encrypts the data, and KMS encrypts the data key. Rotation "
            "changes the outer key, so nothing is written again.",
            "Only a customer managed key lets you set who may use it and see every "
            "use. An AWS managed key does not.",
            "A multi-Region key is for the same key material in two Regions, which is "
            "a different question from who holds it.",
        ],
    },

    {
        "id": "who-may",
        "stem": r"access to|permission|who (can|may)|least privilege|sign in|sign-in|authenticat|federat|credential",
        "choices": [
            r"IAM role",
            r"instance profile",
            r"resource-based|bucket policy",
            r"Identity Center",
            r"\bSCP\b|service control polic",
            r"Cognito",
            r"access key",
            r"\bSAML\b|SAML-based",
            r"[Ww]eb [Ii]dentity [Ff]ederation|OpenID|OIDC",
            r"[Cc]ross-[Aa]ccount",
            r"Directory Service|Managed Microsoft AD",
        ],
        "title": "How to say who may do what",
        "area": "security",
        "rows": [
            ("an application on an instance", "An instance role"),
            ("a function", "An execution role"),
            ("one account reaching another", "A role in the far account"),
            ("staff who already have company logins", "IAM Identity Center"),
            ("a ceiling nobody in the account may pass", "A service control policy"),
            ("letting an outsider at one bucket or queue", "A resource-based policy"),
            ("an app user reaching S3 directly", "A Cognito identity pool"),
        ],
        "traps": [
            "A role is assumed and its credentials expire. Anything that copies an "
            "access key onto a server is the wrong answer.",
            "A service control policy sets a maximum and never grants anything, and "
            "does not apply to the management account.",
            "Across accounts you need both ends: the trust policy on the role and the "
            "permission on the caller.",
        ],
    },

    {
        "id": "scale-how",
        "choices": [
            r"Auto Scaling group",
            r"larger instance|instance (size|type)|vertical|scale up|resiz",
            r"horizontal|scale out|additional (EC2 )?instances|more instances",
            r"scheduled scaling|scheduled action",
            r"(across|in) (two|three|multiple|separate|different) Availability Zones|"
            r"spread across|Multi-AZ",
            r"load balancer|\bALB\b|\bNLB\b",
        ],
        "stem": r"growing|grow(th|s)?|more traffic|increase in (traffic|usage|load)|"
                r"handle (the )?(growing|increasing|additional)? ?(traffic|load|demand)|"
                r"spike|peak|scal|resilien|single (EC2 )?instance|"
                r"single Availability Zone",
        "title": "How to carry more traffic",
        "area": "compute",
        "rows": [
            ("more of the same work at once", "More instances, in an Auto Scaling group"),
            ("one job that cannot be split up", "A larger instance"),
            ("it must survive losing a zone", "Instances in two zones or more"),
            ("the rush has an hour you can name", "Scheduled scaling"),
            ("the rush cannot be predicted", "A scaling policy on a measurement"),
            ("the work must never be turned away", "A minimum count on the group"),
        ],
        "traps": [
            "Scaling up means a stop and a start, so it is not a way to meet a spike "
            "and it leaves you on one machine, which is still one thing to lose.",
            "Adding instances by hand is not scaling. Without a group, nothing adds "
            "them, nothing takes them away, and nothing replaces one that dies.",
            "Instances in a single zone are not resilient however many there are. "
            "Resilience is about where they sit, not how many.",
            "Nine instances to be safe is the expensive wrong answer: a group with a "
            "sensible minimum does the same job and costs what the traffic costs.",
        ],
    },

    {
        "id": "scaling-policy",
        "choices": [
            r"target tracking",
            r"step scaling",
            r"simple scaling",
            r"scheduled scaling|scheduled action",
            r"predictive scaling",
            r"warm pool",
        ],
        "title": "Which scaling policy",
        "area": "compute",
        "rows": [
            ("keep one number where you want it", "Target tracking"),
            ("different sizes of response to different gaps", "Step scaling"),
            ("a rush you can name the hour of", "Scheduled scaling"),
            ("a pattern that repeats week to week", "Predictive scaling"),
            ("instances take too long to start", "A warm pool"),
            ("the metric is memory or disk", "The CloudWatch agent, then "
                                             "target tracking"),
        ],
        "traps": [
            "Target tracking is the one to reach for unless the question gives a "
            "reason not to. Step scaling is for when the size of the response has "
            "to vary with how far out the number is.",
            "Memory and disk space are not there until the CloudWatch agent is "
            "installed. Processor and network are.",
            "A warm pool answers slow starts, not slow scaling decisions: it is "
            "about how long an instance takes to be useful.",
        ],
    },

    {
        "id": "secret-where",
        "stem": r"credential|password|secret|rotat|connection string|API key",
        "choices": [
            r"Secrets Manager",
            r"Parameter Store",
            r"IAM database authentication",
            r"environment variable|hard-?code|in the (code|AMI|user data)|configuration file",
        ],
        "title": "Where to keep a secret",
        "area": "security",
        "rows": [
            ("a database password that must change on its own", "Secrets Manager, "
                                                                "automatic rotation"),
            ("a setting or a plain value, nothing to rotate", "Parameter Store"),
            ("a secret, but no rotation and cost matters", "Parameter Store, "
                                                            "SecureString"),
            ("the same secret needed in several Regions", "Secrets Manager, "
                                                           "replicated"),
            ("no password at all for RDS or Aurora", "IAM database authentication"),
        ],
        "traps": [
            "Secrets Manager rotates by itself, with a Lambda it writes for you, and "
            "is built in to RDS, Aurora, Redshift and DocumentDB. Parameter Store "
            "never rotates anything.",
            "Anything in code, in an AMI, in user data, in a config file or in an "
            "environment variable is the wrong answer every time.",
            "Parameter Store standard tier is free. Secrets Manager charges per "
            "secret per month. Lowest cost with no rotation is Parameter Store.",
            "KMS holds keys, not secrets. It encrypts what the other two store.",
        ],
    },

    {
        "id": "bucket-lock",
        "stem": r"delet|overwrit|tamper|public|unauthori[sz]ed|WORM|regulat|complian|retention|immutable|only (through|via|from) CloudFront|legal hold",
        "choices": [
            r"Object Lock",
            r"MFA Delete",
            r"Block Public Access",
            r"bucket policy",
            r"origin access (control|identity)|\bOAC\b|\bOAI\b",
            r"presigned|pre-signed|signed URL",
            r"access point",
            r"[Vv]ersioning",
        ],
        "title": "How to lock down a bucket",
        "area": "storage",
        "rows": [
            ("nothing may be deleted or changed, by anyone, ever", "Object Lock, "
                                                                 "compliance mode"),
            ("protected, but an administrator can lift it", "Object Lock, "
                                                            "governance mode"),
            ("stop an accidental delete", "Versioning, and MFA Delete"),
            ("make sure nothing is ever public", "Block Public Access, "
                                                 "on the account"),
            ("reachable only through CloudFront", "Origin access control, "
                                                  "and a bucket policy"),
            ("one person, one object, for a short time", "A presigned URL"),
            ("only over HTTPS, or only from one VPC", "A bucket policy "
                                                      "with a condition"),
            ("many teams, each with their own rules", "S3 Access Points"),
        ],
        "traps": [
            "Object Lock needs versioning and is turned on when the bucket is made. "
            "Compliance mode cannot be shortened or removed, not even by the root "
            "user. Governance mode can be, by someone with the permission.",
            "MFA Delete can only be turned on by the root user, from the CLI.",
            "Origin access control is the current answer and origin access identity "
            "the old one. Same idea: the bucket answers only CloudFront.",
            "A presigned URL carries the permissions of whoever made it, and "
            "expires. It is how a browser uploads straight to S3.",
        ],
    },

    {
        "id": "nat-out",
        "stem": r"private subnet|no public IP|without .{0,30}public|outbound|reach .{0,30}(internet|S3|DynamoDB)|patch|software update|download .{0,20}updates|IPv6",
        "choices": [
            r"NAT gateway",
            r"NAT instance",
            r"gateway (VPC )?endpoint|VPC gateway endpoint",
            r"interface (VPC )?endpoint|VPC interface endpoint",
            r"egress-only",
            r"internet gateway",
        ],
        "title": "How a private instance reaches out",
        "area": "networking",
        "rows": [
            ("a private subnet needs the internet", "A NAT gateway in a public "
                                                    "subnet, and a route to it"),
            ("the same, but over IPv6", "An egress-only internet gateway"),
            ("it only needs S3 or DynamoDB", "A gateway endpoint, which is free"),
            ("any other AWS service, privately", "An interface endpoint"),
            ("it must survive losing a zone", "One NAT gateway per zone, and a "
                                              "route table per zone"),
            ("cheapest, and you will manage it yourself", "A NAT instance"),
        ],
        "traps": [
            "A NAT gateway lives in one zone. One per zone, with each private subnet "
            "routing to its own, or losing that zone takes everyone's internet.",
            "Traffic to S3 through a NAT gateway is charged by the gigabyte. A "
            "gateway endpoint carries it for nothing. Cut the NAT bill means add "
            "the endpoint.",
            "The NAT gateway goes in the public subnet. The route to it goes in the "
            "private subnet's route table. Questions swap these.",
            "A NAT instance needs source and destination check turned off, and a "
            "security group. A NAT gateway needs neither.",
        ],
    },

    {
        "id": "who-finds",
        "stem": r"detect|find|discover|identif|monitor|audit|complian|who (made|changed|deleted|created)|unusual|threat|vulnerab|personal|PII|sensitive|drift",
        "choices": [
            r"GuardDuty",
            r"Macie",
            r"Inspector",
            r"AWS Config|Config (custom |managed )?rule",
            r"Security Hub",
            r"Access Analyzer",
            r"CloudTrail",
            r"Detective",
            r"Trusted Advisor",
        ],
        "title": "Which service finds what",
        "area": "security",
        "rows": [
            ("threats: a stolen key, crypto mining, an odd login", "GuardDuty"),
            ("personal or sensitive data sitting in S3", "Macie"),
            ("software flaws on instances, containers, Lambda", "Inspector"),
            ("a setting that drifted from the rule", "AWS Config"),
            ("who called which API, and when", "CloudTrail"),
            ("a bucket or role that outsiders can reach", "IAM Access Analyzer"),
            ("every finding, in one place", "Security Hub"),
            ("why a finding happened, the whole story", "Detective"),
            ("cost, limits and best practice checks", "Trusted Advisor"),
        ],
        "traps": [
            "GuardDuty reads CloudTrail, VPC Flow Logs and DNS logs without you "
            "turning them on. It finds threats, not wrong settings. Wrong settings "
            "are Config.",
            "Config says what changed and whether it is allowed. CloudTrail says who "
            "did it. A question that asks both wants both.",
            "Macie is only S3 and only sensitive data. Inspector is only "
            "vulnerabilities. Neither does the other's job.",
            "Security Hub shows findings from the others. It finds nothing itself.",
        ],
    },

    {
        "id": "edge-defend",
        "stem": r"DDoS|attack|flood|malicious|SQL injection|cross-site|block .{0,30}(IP|address|countr|request)|too many requests|\bbots?\b|rate limit",
        "choices": [
            r"\bWAF\b|web ACL",
            r"Shield Advanced",
            r"Shield Standard",
            r"Firewall Manager",
            r"Network Firewall",
            r"geographic restriction|geo-?restriction|geo-?blocking",
            r"rate-based",
            r"network ACL|\bNACL\b",
        ],
        "title": "Which defence, and where",
        "area": "security",
        "rows": [
            ("SQL injection, cross-site scripting, bad requests", "WAF, managed rules"),
            ("too many requests from one address", "WAF, a rate-based rule"),
            ("a known list of bad addresses", "WAF, an IP set"),
            ("a big DDoS, and a team to call", "Shield Advanced"),
            ("the same rules in every account", "Firewall Manager"),
            ("block a whole country on a distribution", "CloudFront geographic "
                                                        "restriction"),
            ("inspect traffic inside the VPC", "Network Firewall"),
            ("block one address at the subnet", "A network ACL deny rule"),
        ],
        "traps": [
            "WAF attaches to CloudFront, an ALB, API Gateway, AppSync or Cognito. "
            "Never an NLB and never an instance. For an NLB or an Elastic IP the "
            "answer is Shield Advanced.",
            "Shield Standard is already on and costs nothing. Shield Advanced is paid "
            "and brings the response team and cost protection.",
            "A security group cannot deny. Only a network ACL has deny rules, so "
            "blocking an address at the subnet is always the network ACL.",
            "Firewall Manager needs Organizations. It is for many accounts, not one.",
        ],
    },

    {
        "id": "query-s3",
        "stem": r"quer|analy|\bSQL\b|report|dashboard|visuali[sz]|catalog|data lake|ad hoc|one-time|log files",
        "choices": [
            r"Athena",
            r"\bGlue\b",
            r"QuickSight",
            r"Redshift Spectrum",
            r"\bEMR\b",
            r"Lake Formation",
            r"S3 Select",
            r"OpenSearch|Elasticsearch",
            r"Apache Flink|Kinesis Data Analytics",
        ],
        "title": "How to query data in S3",
        "area": "analytics",
        "rows": [
            ("SQL over files in S3, now and then", "Athena"),
            ("the files need cleaning or converting first", "Glue, then Athena"),
            ("a chart or a dashboard", "QuickSight"),
            ("join files in S3 to a warehouse", "Redshift Spectrum"),
            ("Spark or Hadoop, a big batch", "EMR"),
            ("who may see which columns, across accounts", "Lake Formation"),
            ("search through text or logs", "OpenSearch"),
            ("as the data streams in", "Managed Service for Apache Flink"),
        ],
        "traps": [
            "Athena has no cluster and charges per data scanned. For ad hoc SQL "
            "with the least to run, it is the answer.",
            "Converting to Parquet with Glue, and partitioning, cuts what Athena "
            "scans and so what it costs. That is the cost question.",
            "The Glue Data Catalog is the table definition Athena, Redshift Spectrum "
            "and EMR all read from. A Glue crawler fills it in.",
            "QuickSight draws. It does not read files by itself: it sits on Athena, "
            "Redshift or RDS.",
        ],
    },

    {
        "id": "api-front",
        "stem": r"\bAPI\b|REST|endpoint|throttl|quota|JWT|webhook|callers?",
        "choices": [
            r"edge-optimized",
            r"Regional (API|endpoint)",
            r"private (API|endpoint)|private REST",
            r"HTTP API",
            r"REST API",
            r"function URL",
            r"usage plan|API key",
            r"resource policy",
            r"WebSocket",
        ],
        "title": "Which front door for an API",
        "area": "compute",
        "rows": [
            ("callers all over the world", "Edge-optimized"),
            ("callers in the same Region, or your own CloudFront in front",
             "Regional"),
            ("only from inside a VPC", "Private, with an interface endpoint"),
            ("cheapest, JWT, a simple pass-through to Lambda", "HTTP API"),
            ("caching, usage plans, API keys, request validation, WAF", "REST API"),
            ("one function, one URL, nothing in between", "A Lambda function URL"),
            ("two-way and live", "WebSocket API"),
            ("a limit per customer", "Usage plans and API keys, REST only"),
        ],
        "traps": [
            "HTTP API is cheaper and faster but has no caching, no usage plans, no "
            "API keys and no request validation. The moment the question needs any "
            "of those it is REST.",
            "A JWT authorizer is built in to HTTP API. REST needs a Lambda "
            "authorizer or a Cognito authorizer instead.",
            "Edge-optimized already uses CloudFront underneath. To put your own "
            "CloudFront in front, make it Regional.",
            "API Gateway times out at 29 seconds and allows 10,000 requests a second "
            "by default. Past those, the question is about something else.",
        ],
    },

    {
        "id": "survive-region",
        "stem": r"disaster|recover|\bRPO\b|\bRTO\b|Region (fails|outage|goes|is lost|becomes)|los(e|es|ing) a Region|another Region|second Region|business continuity|backup|restore|back up",
        "choices": [
            r"AWS Backup",
            r"cross-Region (replication|snapshot|copy|backup)|copy .{0,30}(snapshot|backup).{0,30}Region",
            r"\bAMI\b",
            r"point-in-time recovery|PITR",
            r"Multi-Region Access Point",
            r"global database|Aurora Global",
            r"global tables?",
            r"Global Datastore",
            r"Route 53 (health check|failover)|failover routing",
            r"pilot light|warm standby|multi-site|backup and restore",
        ],
        "title": "How to survive losing a Region",
        "area": "resilience",
        "rows": [
            ("hours to recover, and cheapest", "Backup and restore: snapshots "
                                               "copied to the other Region"),
            ("minutes, the data already there", "Pilot light: database replicated, "
                                                "servers switched off"),
            ("minutes, a small copy running", "Warm standby: a scaled-down stack "
                                              "already running"),
            ("seconds, and nothing lost", "Multi-site active-active: both "
                                          "Regions serving"),
            ("one place to schedule every backup", "AWS Backup, a plan and a vault"),
            ("a relational database in two Regions", "Aurora global database, "
                                                     "one writer"),
            ("DynamoDB in two Regions, both writing", "Global tables"),
            ("send users to the Region that is up", "Route 53 failover, with "
                                                    "a health check"),
            ("back to any second in the last 35 days", "Point-in-time recovery"),
        ],
        "traps": [
            "RPO is how much data you may lose. RTO is how long you may be down. "
            "Lower numbers cost more: match the strategy to the numbers given.",
            "A snapshot stays in its Region. Automated RDS backups do not leave the "
            "Region on their own. It only helps elsewhere if you copied it there.",
            "An Aurora global database has one writer. Failing over promotes the "
            "secondary in about a minute. Global tables write in both Regions.",
            "A copy of an encrypted snapshot into another Region needs a KMS key in "
            "that Region. A vault lock in compliance mode cannot be undone, not "
            "even by the root user.",
        ],
    },

    {
        "id": "placement",
        "stem": r"placement|low latency between|tightly coupled|\bHPC\b|high.performance computing|node-to-node|inter-node|not .{0,20}same (rack|hardware)|separate hardware|large distributed|network throughput between",
        "choices": [
            r"cluster placement",
            r"spread placement",
            r"partition placement",
            r"Elastic Fabric Adapter|\bEFA\b",
            r"enhanced networking|Elastic Network Adapter|\bENA\b",
            r"Dedicated Host",
        ],
        "title": "Which placement group",
        "area": "compute",
        "rows": [
            ("instances talking to each other, fast", "Cluster, in one zone"),
            ("tightly coupled HPC, MPI between nodes", "Cluster, and an Elastic "
                                                       "Fabric Adapter"),
            ("a few critical instances that must not share a rack", "Spread, "
                                                                   "up to 7 per zone"),
            ("a large distributed system: Hadoop, Cassandra, Kafka", "Partition, "
                                                                     "7 partitions per zone"),
        ],
        "traps": [
            "Cluster stays in one zone. Spread and partition can cross zones. A "
            "question that wants both speed and surviving a zone cannot have both.",
            "Spread allows only 7 running instances per zone per group. Partition "
            "allows 7 partitions per zone, with many instances in each.",
            "An Elastic Fabric Adapter needs a cluster placement group and a "
            "supported instance type. Enhanced networking is already on.",
            "When a cluster group cannot find room, stop every instance in it and "
            "start them together, so they land near each other.",
        ],
    },

    {
        "id": "ebs-type",
        "stem": r"IOPS|throughput|volume|disk|boot|database (storage|disk)|sequential|big data|log processing|scratch|temporary|ephemeral",
        "choices": [
            r"\bgp2\b",
            r"\bgp3\b|General Purpose SSD",
            r"\bio[12]\b|Provisioned IOPS",
            r"\bst1\b|Throughput Optimized",
            r"\bsc1\b|Cold HDD",
            r"instance store",
            r"Data Lifecycle Manager|snapshot lifecycle",
            r"Compute Optimizer",
        ],
        "title": "Which EBS volume",
        "area": "storage",
        "rows": [
            ("boot, general, most things", "gp3"),
            ("over 16,000 IOPS, or a database that needs a promise", "io2 Block "
                                                                    "Express"),
            ("large sequential reads: big data, logs, cheap", "st1"),
            ("rarely touched, cheapest", "sc1"),
            ("scratch space, fastest, lost on stop", "Instance store"),
            ("snapshots on a schedule", "Data Lifecycle Manager"),
            ("the volume is bigger than it needs to be", "Compute Optimizer, or "
                                                        "the volume's CloudWatch "
                                                        "metrics"),
        ],
        "traps": [
            "gp3 sets IOPS and throughput apart from size. gp2 ties IOPS to size. "
            "Moving gp2 to gp3 saves about a fifth with the same performance.",
            "Only io1 and io2 support Multi-Attach, and only within one zone.",
            "st1 and sc1 cannot be a boot volume. An instance store loses "
            "everything on stop, so it is never the answer for anything kept.",
            "A volume can be changed in place without stopping: size, type and "
            "IOPS. Nothing has to be copied.",
        ],
    },

    {
        "id": "s3-fast",
        "stem": r"upload|download|slow|latency|large (file|object)|far (from|away)|around the world|global users|bandwidth|transfer|many (small )?(requests|reads)",
        "choices": [
            r"Transfer Acceleration",
            r"multipart",
            r"CloudFront",
            r"Express One Zone",
            r"Requester Pays",
            r"byte-range|S3 Select",
            r"Cross-Region Replication|\bCRR\b",
            r"presigned|pre-signed",
        ],
        "title": "How to move S3 data faster or cheaper",
        "area": "storage",
        "rows": [
            ("uploads from far away, to one bucket", "Transfer Acceleration"),
            ("large files, over 100 MB", "Multipart upload"),
            ("downloads to users everywhere, cached", "CloudFront"),
            ("users upload straight from the browser", "Presigned URLs"),
            ("millions of small reads, single-digit milliseconds", "S3 Express "
                                                                   "One Zone"),
            ("the reader should pay for the transfer", "Requester Pays"),
            ("a copy near the users in another Region", "Cross-Region Replication"),
        ],
        "traps": [
            "Transfer Acceleration uses the CloudFront edge network to reach the "
            "bucket, for uploads over a long distance, at extra cost. CloudFront "
            "itself caches downloads.",
            "Multipart upload is required over 5 GB and advised over 100 MB. "
            "Incomplete uploads still cost. A lifecycle rule cleans them up.",
            "S3 scales per prefix: 3,500 writes and 5,500 reads a second each. "
            "More prefixes, more throughput.",
            "A presigned URL lets the browser upload with no server in between, "
            "and carries the permissions of whoever made it.",
        ],
    },

    {
        "id": "many-accounts",
        "stem": r"accounts|organization|multi-account|landing zone|govern|guardrail|billing|cost (per|by|for each)|chargeback|department|business unit",
        "choices": [
            r"\bSCP\b|service control polic",
            r"Control Tower",
            r"Organizations",
            r"consolidated billing",
            r"tag polic",
            r"Resource Access Manager|\bRAM\b",
            r"cost allocation tag",
            r"Cost Explorer|Cost and Usage Report",
            r"Budgets",
            r"permissions boundar",
        ],
        "title": "How to govern many accounts",
        "area": "security",
        "rows": [
            ("stop every account doing one thing", "A service control policy on "
                                                   "the OU"),
            ("new accounts, set up the right way", "Control Tower"),
            ("one bill, and volume discounts", "Organizations, consolidated billing"),
            ("cost by team or by project", "Cost allocation tags, then "
                                           "Cost Explorer"),
            ("share a subnet or a prefix list between accounts", "Resource Access "
                                                                 "Manager"),
            ("only allowed tag values", "A tag policy"),
            ("a warning before the money runs out", "Budgets, with an action"),
            ("a developer who may not go past a line", "A permissions boundary"),
        ],
        "traps": [
            "A service control policy never grants. It only limits, it does not "
            "touch the management account, and attached to the root OU it covers "
            "every account.",
            "Cost allocation tags show nothing until they are activated in the "
            "billing console, and only the management account can do that.",
            "Reserved Instance and Savings Plan discounts are shared across the "
            "whole organization under consolidated billing.",
            "Control Tower sits on top of Organizations: guardrails, a landing zone "
            "and Account Factory. An existing organization can be enrolled.",
        ],
    },

    {
        "id": "dynamodb-how",
        "stem": r"DynamoDB",
        "choices": [
            r"on-demand|on demand capacity",
            r"provisioned (capacity|throughput|mode)",
            r"DynamoDB auto ?scaling|auto ?scaling (for|on) the table|table.{0,30}auto ?scaling",
            r"Time to Live|\bTTL\b",
            r"DynamoDB Streams",
            r"point-in-time recovery|PITR",
            r"global tables?",
            r"\bDAX\b",
            r"export .{0,20}to .{0,10}S3",
            r"Standard-IA table",
        ],
        "title": "Which DynamoDB feature",
        "area": "database",
        "rows": [
            ("unpredictable, spiky, or brand new", "On-demand capacity"),
            ("steady and known", "Provisioned, with auto scaling"),
            ("rows should vanish after a time", "TTL"),
            ("react to every change", "Streams, into Lambda"),
            ("back to any point in the last 35 days", "Point-in-time recovery"),
            ("two Regions, both writing", "Global tables"),
            ("the same reads, in microseconds", "DAX"),
            ("analyse it without a scan", "Export to S3, then Athena"),
            ("rarely read, keep the bill down", "Standard-IA table class"),
        ],
        "traps": [
            "On-demand is the least to manage but costs more per request. For a "
            "steady load, provisioned with auto scaling is cheaper.",
            "TTL deletes for free, in the background, within about 48 hours. "
            "Expired rows can still show up in a read until then.",
            "Global tables need Streams turned on. Both Regions write, and the last "
            "writer wins.",
            "A scan reads every item and is the expensive wrong answer for "
            "analysis. Export to S3 uses no table capacity at all.",
        ],
    },

    {
        "id": "rds-how",
        "stem": r"\bRDS\b|Aurora|relational database",
        "choices": [
            r"RDS Proxy",
            r"blue/green|blue-green",
            r"Aurora Serverless",
            r"I/O-Optimized",
            r"Performance Insights",
            r"Babelfish",
            r"storage auto ?scaling",
            r"parameter group",
            r"IAM database authentication",
            r"Multi-AZ",
            r"read replica",
            r"(take|create) a snapshot",
        ],
        "title": "Which RDS feature",
        "area": "database",
        "rows": [
            ("too many connections, Lambda opening them", "RDS Proxy"),
            ("upgrade with a rehearsal and a quick switch", "Blue/green deployment"),
            ("the load comes and goes", "Aurora Serverless v2"),
            ("the bill is mostly I/O", "Aurora I/O-Optimized"),
            ("which query is slow", "Performance Insights"),
            ("SQL Server code at a PostgreSQL price", "Babelfish for Aurora "
                                                      "PostgreSQL"),
            ("the disk keeps filling up", "Storage auto scaling"),
            ("change an engine setting", "A parameter group"),
            ("no password in the app", "IAM database authentication"),
            ("a test database idle most of the week", "Snapshot and delete, "
                                                      "restore when wanted"),
        ],
        "traps": [
            "Multi-AZ is for failover and serves no reads. A read replica is for "
            "reads and does not fail over. Aurora replicas do both.",
            "RDS Proxy pools connections and makes failover faster. It is the answer "
            "whenever Lambda is exhausting connections.",
            "Encryption cannot be added to a running unencrypted instance. Snapshot, "
            "copy the snapshot with encryption, restore from the copy.",
            "A stopped RDS instance starts itself again after 7 days. To stop paying "
            "for a long time, snapshot and delete.",
        ],
    },

    {
        "id": "lambda-how",
        "stem": r"Lambda",
        "choices": [
            r"provisioned concurrency",
            r"SnapStart",
            r"reserved concurrency",
            r"function URL",
            r"Lambda@Edge",
            r"CloudFront Functions",
            r"mount .{0,40}\bEFS\b|\bEFS\b.{0,30}(mount|access point)|EFS .{0,20}Lambda|Lambda .{0,20}EFS",
            r"Lambda layer",
            r"container image",
            r"event source mapping",
            r"dead-letter|on-failure destination|Lambda destination",
        ],
        "title": "Which Lambda feature",
        "area": "compute",
        "rows": [
            ("cold starts hurt", "Provisioned concurrency"),
            ("cold starts hurt, and it is Java", "SnapStart"),
            ("stop one function eating all the concurrency", "Reserved concurrency"),
            ("an HTTPS address with nothing in front", "A function URL"),
            ("change a request at the edge, a little", "CloudFront Functions"),
            ("at the edge, and it needs the network or more time", "Lambda@Edge"),
            ("files bigger than 512 MB, or shared", "Mount EFS"),
            ("read from a queue or a stream", "An event source mapping"),
            ("failed events must go somewhere", "A dead-letter queue, or a "
                                                "destination"),
        ],
        "traps": [
            "The limits: 15 minutes, 10 GB of memory, a 10 GB image, 250 MB "
            "unzipped, 10 GB of /tmp. Past any of them it is Fargate or Batch.",
            "Provisioned concurrency costs whether it is used or not. For a busy "
            "hour you can name, schedule it with Application Auto Scaling.",
            "A Lambda inside a VPC has no public address. To reach the internet it "
            "needs a NAT gateway, and to reach AWS services, endpoints.",
            "Reserved concurrency set to zero turns the function off. Set to a "
            "number, it is both a ceiling and a guarantee.",
        ],
    },
]


_NOT: dict[str, re.Pattern] = {}
_STEM: dict[str, re.Pattern] = {}


def _rx(cache: dict, key: str, phrase: str) -> re.Pattern:
    rx = cache.get(key)
    if rx is None:
        rx = cache[key] = re.compile(phrase, re.I)
    return rx


_CHOICE: dict[str, list[re.Pattern]] = {}


def decisions_for(question: str, options: list[str] | None = None,
                  limit: int = 2) -> list[str]:
    """The choices this question is asking you to make.

    A question is asking a decision when two or more of that decision's
    destinations turn up among its options, which is what being asked to
    choose actually looks like. Matching on a word in the question instead
    pulled in anything that merely mentioned a database, including questions
    about backing one up or logging a distribution in front of one.

    The question's own words still have to agree, so that a list of unrelated
    services does not count as a choice between them.
    """
    opts = options or []
    if not opts:
        return []
    text = (question or "") + " " + " ".join(opts)
    if len(text) < 40:
        return []

    out = []
    for d in DECISIONS:
        pats = _CHOICE.get(d["id"])
        if pats is None:
            pats = _CHOICE[d["id"]] = [re.compile(p, re.I) for p in d["choices"]]
        spanned = sum(1 for rx in pats if any(rx.search(o) for o in opts))
        if not spanned:
            continue
        # Two destinations on offer is a choice on its own. One destination is
        # a choice when the question states the problem that choice answers,
        # because a well-made question often pairs the right service with
        # three distractors nobody would list as destinations.
        if spanned < 2:
            stem = d.get("stem")
            if not stem or not _rx(_STEM, d["id"], stem).search(question or ""):
                continue
        no = d.get("unless")
        if no and _rx(_NOT, d["id"], no).search(text):
            continue
        out.append((spanned, d["id"]))

    # The decision whose destinations the options cover most fully is the one
    # the question is really about.
    out.sort(key=lambda x: -x[0])
    return [did for _, did in out[:limit]]


# The same two mistakes as the diagram library, which have cost hours: a
# pattern written without the r prefix holds a backspace instead of a word
# boundary, and a doubled backslash matches a real backslash. Both compile,
# both match nothing, and neither shows up except as a thing that never
# appears.
_ids = [d["id"] for d in DECISIONS]
if len(set(_ids)) != len(_ids):
    raise AssertionError("two decisions share an id")
for _d in DECISIONS:
    _pat = (_d.get("stem") or "") + (_d.get("unless") or "")
    if any(ord(c) < 32 for c in _pat):
        raise AssertionError(
            f"{_d['id']}: a control character in the pattern, which means a "
            "missing r prefix on the string")
    if "\\\\" in _pat:
        raise AssertionError(
            f"{_d['id']}: a doubled backslash, which matches a real backslash "
            "and so matches nothing")
    re.compile(_pat)
    for _c in _d["choices"]:
        if any(ord(c) < 32 for c in _c) or "\\\\" in _c:
            raise AssertionError(f"{_d['id']}: a broken choice pattern")
        re.compile(_c)
    if len(_d["choices"]) < 2:
        raise AssertionError(f"{_d['id']}: a choice needs at least two destinations")
    if not _d["rows"] or not _d.get("traps"):
        raise AssertionError(f"{_d['id']}: nothing to show")


if __name__ == "__main__":
    import json
    import pathlib
    rows = json.loads(
        (pathlib.Path(__file__).parent / "bank.json").read_text(encoding="utf-8"))
    rows = rows if isinstance(rows, list) else rows.get("questions")
    seen: set[str] = set()
    counts: dict[str, int] = {}
    for r in rows:
        for did in decisions_for(r.get("question", ""), r.get("options"), limit=99):
            counts[did] = counts.get(did, 0) + 1
            seen.add(r["id"])
    print(f"{len(DECISIONS)} decisions against {len(rows)} questions")
    for d in DECISIONS:
        print(f"  {counts.get(d['id'], 0):5d}  {d['title']}")
    print(f"\n{len(seen)} questions reach at least one ({len(seen) * 100 // len(rows)}%)")