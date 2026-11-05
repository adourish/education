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
            ("read a few times a year, wanted at once", "Glacier Instant Retrieval"),
            ("archived, minutes will do", "Glacier Flexible Retrieval"),
            ("archived, hours will do, cheapest of all", "Glacier Deep Archive"),
            ("delete after a set time, or by object size", "A lifecycle expiration rule"),
            ("kept a day, then deleted", "S3 Standard"),
        ],
        "kinds": [
            ("Glacier, by how fast you get it back", [
                ("Instant Retrieval", "milliseconds"),
                ("Flexible Retrieval", "minutes to 12 hours"),
                ("Deep Archive", "up to 48 hours; cheapest"),
            ]),
        ],
        "traps": [
            "Infrequent access charges for a minimum of 30 days and Glacier for 90, "
            "so something short-lived costs more there than in Standard.",
            "One Zone is the only one that does not survive losing a zone. S3 Express "
            "One Zone is a different thing again: the fastest and dearest, not an "
            "archive.",
            "Where the pattern is unknown, Intelligent-Tiering beats guessing: it "
            "moves each object on its own and charges no retrieval fee.",
            "Millions of tiny files: bundle them into large objects first. Every object pays per request and per lifecycle move.",
            "Deleting after a set time is a lifecycle expiration rule. A bucket policy only allows or denies; it never deletes.",
            "Unknown size is not unknown access: data kept one day and read is Standard. Tiering only pays off over months.",
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
            ("under 15 minutes, willing to change the image", "Lambda, from a container image"),
            ("an existing container, minimal changes to the application", "ECS, on Fargate for no servers"),
            ("longer than that, or always on", "ECS on Fargate"),
            ("highly available across zones, least work", "ECS service, at least one task per zone, spread by Availability Zone"),
            ("the question says Kubernetes", "EKS on Fargate"),
            ("needs a GPU, or a chosen instance type", "ECS on EC2, a GPU instance family"),
            ("many parallel jobs, running hours or days", "AWS Batch"),
            ("it must run on your own hardware", "ECS Anywhere or EKS Anywhere"),
            ("over 15 minutes, can be interrupted, cheapest", "ECS on Fargate Spot"),
            ("critical, must not be interrupted", "On-Demand, never Spot or Fargate Spot"),
            ("see EKS and on-premises clusters in one place", "EKS Connector"),
        ],
        "kinds": [
            ("Where ECS tasks run", [
                ("EC2 launch type", "you pick the instances; GPUs"),
                ("Fargate", "no servers; no GPU"),
                ("Fargate Spot", "up to 70% off; can be stopped"),
            ]),
            ("Roles on an ECS task", [
                ("Task role", "what your code uses: S3, DynamoDB"),
                ("Task execution role", "what ECS uses: pull image, logs, secrets"),
            ]),
            ("EKS options", [
                ("Managed node groups", "EC2 nodes AWS patches and replaces"),
                ("Fargate profile", "pods with no nodes to run"),
                ("EKS Anywhere", "Kubernetes on your own servers"),
                ("EKS Connector", "see any cluster in the EKS console"),
            ]),
        ],
        "traps": [
            "Work down the list and stop at the first that fits: each step down is "
            "more to manage, so the one above is the least-overhead answer.",
            "Lambda runs a container image only if it is built for Lambda: the "
            "runtime interface client and a handler taking one event at a time. "
            "An ordinary app in a container needs its start-up rewritten, so "
            "'minimal changes to the application' rules Lambda out and points to "
            "ECS. 'Willing to change the image' is the phrase that lets Lambda in.",
            "A Lambda option with 'minimum capacity 3' is a decoy. Lambda in a VPC "
            "already spreads across its subnets; Application Auto Scaling there "
            "only keeps instances warm (provisioned concurrency).",
            "'Self-managed nodes' means you patch and scale the servers, so it is "
            "never the least-overhead answer. A spread placement group keeps "
            "instances on separate hardware, at most seven per zone; it is not "
            "a container platform, and Reserved Instances save money, not work.",
            "Fargate still has a cluster, a task definition and a service. It is less "
            "than owning instances and more than Lambda.",
            "Neither Lambda nor Fargate offers a GPU, so a GPU means EC2 instances underneath, run by ECS or EKS.",
            "Fargate Spot can be stopped with two minutes' warning, so 'critical' or 'must not be interrupted' rules it out.",
            "An ECS spread task strategy spreads tasks across zones; an EC2 spread placement group is about racks, not containers.",
        ],
    },

    {
        "id": "db-engine",
        "stem": r"(new|choose|select|which) .{0,40}database|migrat\w+ .{0,30}database|relational|non-relational|NoSQL|key-value|document database|graph database|time series|vector|embedding|SQL Server|T-SQL|stored procedure|telemetry",
        "choices": [
            r"Aurora",
            r"DynamoDB",
            r"RDS for (Microsoft )?(MySQL|PostgreSQL|MariaDB|Oracle|SQL)",
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
            ("Oracle or SQL Server, kept as it is", "RDS (Aurora only does MySQL and "
                                                    "PostgreSQL)"),
            ("SQL Server, but cut cost or licences", "Aurora PostgreSQL with "
                                                     "Babelfish"),
            ("MySQL or PostgreSQL, best performance or MOST available", "Aurora"),
            ("the same, but faster and surviving a Region", "Aurora"),
            ("key-value, any scale, single-digit milliseconds", "DynamoDB"),
            ("dev or test databases used a few hours a day", "Aurora Serverless v2, "
                                                             "one each"),
            ("the load comes and goes, or is unknown", "Aurora Serverless, or "
                                                       "DynamoDB on-demand"),
            ("documents, MongoDB wording", "DocumentDB"),
            ("relationships between things, graph wording", "Neptune"),
            ("reporting across a great deal of history", "Redshift"),
            ("readings over time, from devices", "Timestream"),
            ("AI vectors, already on Aurora or RDS PostgreSQL", "pgvector on the "
                                                               "same database"),
            ("SQL Server, least effort, no cost goal", "RDS for SQL Server, Multi-AZ"),
            ("telemetry for ML and visual reports", "Timestream, SageMaker, QuickSight"),
            ("huge sensor writes, read a few times a year", "DynamoDB, Standard-IA table class"),
        ],
        "traps": [
            "An RDS instance or a provisioned Aurora cluster bills every hour, used "
            "or not. Databases busy only a few hours a day are cheapest on Aurora "
            "Serverless v2, and a test database does not need Multi-AZ.",
            "Moving RDS for MySQL or PostgreSQL to Aurora is a routine, low-effort "
            "move: make an Aurora read replica of the running database and promote "
            "it, or restore a snapshot into Aurora. It counts as no code change.",
            "Aurora is still relational. A question wanting to leave SQL behind wants "
            "DynamoDB, not Aurora.",
            "Multi-AZ is not a read scaler for an RDS DB instance: its standby serves "
            "nothing. A Multi-AZ DB cluster and Aurora are different, and do serve "
            "reads.",
            "DynamoDB global tables are the active-active answer across Regions. An "
            "Aurora global database has one writer.",
            "Vector storage at the lowest cost on an existing PostgreSQL database is "
            "pgvector. OpenSearch, DocumentDB and Neptune all store vectors too, but "
            "each is a new cluster to pay for.",
            "With no cost or licence goal, SQL Server stays on RDS for SQL Server. DynamoDB would mean rewriting the app, never least effort.",
            "Redshift is for reports over history. It is never the database behind a live website or an order system.",
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
            r'visibility timeout',
            r'delivery delay|delay queue',
            r'Apache Flink|Kinesis Data Analytics',
            r'\bMSK\b|Managed Streaming for (Apache )?Kafka',
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
            ("the same message is processed twice", "Visibility timeout longer than the work"),
            ("transform or check a stream as it flows", "Managed Service for Apache Flink"),
            ("many readers, kept for months, strict order", "Data Streams, enhanced fan-out"),
            ("on-premises databases feeding live dashboards", "Amazon MSK (managed Kafka)"),
            ("a workflow of steps, each tracked in one place", "SQS to hold, Step Functions to run"),
        ],
        "kinds": [
            ("Kinesis", [
                ("Data Streams", "replay, many readers, keeps data up to a year"),
                ("Data Firehose", "delivers to S3, Redshift, OpenSearch; no replay"),
                ("Video Streams", "video in from cameras; not for serving viewers"),
            ]),
            ("Step Functions workflows", [
                ("Standard", "up to a year, each step once, tracked"),
                ("Express", "up to 5 minutes, huge volume, cheaper"),
            ]),
        ],
        "traps": [
            "A queue holds work for one worker to take. A topic hands a copy to every "
            "subscriber. A question wanting both is SNS in front of SQS.",
            "Firehose keeps nothing, so it cannot be replayed or read twice. That is "
            "what separates it from Data Streams.",
            "Order in a Kinesis stream holds within a shard, not across the stream.",
            "Visibility timeout hides a message while it is worked on. Delivery delay only hides it before first delivery, so it never stops duplicates.",
            "SQS keeps a message 14 days at most, and SNS, SQS and EventBridge take 256 KB at most. Longer or bigger points to Kinesis Data Streams.",
            "If the data lands in S3 before it is checked, it is not real time. Real-time work on a stream is Flink.",
            "EventBridge routes events but tracks no workflow. 'Defined workflow' or 'centrally tracked' is Step Functions.",
            "Step Functions Express workflows stop at 5 minutes and Lambda at 15, so an hour-long job is neither.",
        ],
    },

    {
        "id": "queue-topic-bus",
        "stem": r"fan[- ]?out|subscriber|notif|event-driven|react to|on a schedule|every \d+ minutes|cron|SaaS|partner",
        "choices": [
            r"\bSQS\b",
            r"\bSNS\b",
            r"EventBridge|CloudWatch Events",
        ],
        "title": "SQS, SNS or EventBridge",
        "area": "integration",
        "rows": [
            ("hold it until a worker can take it, the worker is slow or offline", "SQS"),
            ("absorb a spike, scale workers on how long the queue is", "SQS"),
            ("in order, exactly once", "SQS FIFO"),
            ("one message to many subscribers at once, fastest fan-out", "SNS"),
            ("tell people by email, text message or mobile push", "SNS"),
            ("every subscriber gets it, a durable buffer each", "SNS, to one SQS queue each"),
            ("react to an AWS service's event: EC2 state change, GuardDuty finding", "EventBridge"),
            ("route on any field inside the event, many different targets", "EventBridge"),
            ("events from a SaaS partner: Zendesk, Datadog, Shopify", "EventBridge"),
            ("on a cron, every few minutes, or business hours", "EventBridge Scheduler"),
            ("send events to another account or Region", "EventBridge"),
            ("route on content, then hold it for slow workers", "EventBridge, to SQS"),
            ("alert the team when a service reports something", "EventBridge, to SNS"),
            ("which bus: an AWS service's own events", "EventBridge default bus"),
            ("which bus: your own application's events, or one bus for many accounts", "EventBridge custom bus"),
            ("which bus: events from a SaaS product", "EventBridge partner bus"),
            ("keep every message for 30 days, replay later", "EventBridge archive"),
            ("Lambda throttled in a burst, TooManyRequests", "SQS in front of the Lambda"),
            ("process each order the moment it arrives", "An event rule, not polling every minute"),
        ],
        "kinds": [
            ("EventBridge buses", [
                ("Default bus", "AWS services' own events; already there"),
                ("Custom bus", "your app's events, or one bus for many accounts"),
                ("Partner bus", "events from a SaaS product: Zendesk, Datadog, Shopify"),
            ]),
            ("SQS queues", [
                ("Standard", "any order, may arrive twice, almost no limit"),
                ("FIFO", "in order, exactly once, 300 a second (3,000 batched)"),
            ]),
            ("SNS topics", [
                ("Standard", "fan out to anything: email, SMS, Lambda, queues"),
                ("FIFO", "in order, but only to SQS FIFO queues"),
            ]),
        ],
        "traps": [
            "Ask: who should hear about this (EventBridge), everyone at once (SNS), "
            "or hold it until someone can do it (SQS)?",
            "Only SQS holds a backlog. SNS and EventBridge push and retry, but keep "
            "nothing for a worker to pull, so 'must not be lost while the consumer is "
            "down for hours' needs a queue behind them.",
            "SNS filters on message attributes. EventBridge filters on any field of "
            "the event itself. Rich content routing, or AWS and SaaS events, means "
            "EventBridge; plain high-volume fan-out from your own app means SNS.",
            "EventBridge cannot send email: an alert to subscribers goes through SNS, and a report to the one user who asked goes through SES.",
            "A schedule is EventBridge, not a CloudWatch alarm. An alarm watches a "
            "metric; it does not run on a clock.",
            "AWS events land on the default bus with no setup, so a rule for an "
            "EC2 or GuardDuty event goes there, not on a bus you create. Many "
            "accounts reporting to one place: each sends to a custom bus in a "
            "central account, allowed by that bus's resource policy.",
            "SQS never delivers to a person; it holds messages until code pulls them. Email out is SNS, or SES for real mail.",
            "EventBridge rules straight to each consumer hold nothing. 'Durable buffering for each consumer' needs a queue per consumer.",
            "TooManyRequestsException from Lambda is throttling. SQS in front soaks up the burst; reserved concurrency only lowers the cap.",
            "EventBridge cannot write to DynamoDB, so put a Lambda function between them.",
            "To get an event to an API with no public address, make the target a Lambda function in the same VPC.",
        ],
    },

    {
        "id": "balancer",
        "stem": r"load balanc|distribute (the )?traffic|in front of|static IP|route (the |incoming )?requests|microservices?",
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
            ("routing on path, host, header or cookie", "Application Load Balancer"),
            ("blocking web requests by rule", "Application Load Balancer, "
                                               "with AWS WAF"),
            ("a fixed address, so customers can allow-list it", "Network Load "
                                                                "Balancer"),
            ("targets on premises, by IP address", "Either, with IP targets; a "
                                                   "fixed address makes it the NLB"),
            ("TCP or UDP rather than web traffic", "Network Load Balancer"),
            ("millions of requests, lowest latency", "Network Load Balancer"),
            ("traffic through a firewall appliance", "Gateway Load Balancer"),
            ("fixed addresses and more than one Region", "Global Accelerator"),
            ("users worldwide, dynamic or cached content", "CloudFront, the ALB as its origin"),
            ("a site that is only files: HTML, JavaScript, images", "S3, with "
                                                                    "CloudFront in "
                                                                    "front, no "
                                                                    "servers"),
            ("users must log in before they reach the servers", "ALB, with a "
                                                                "Cognito user pool"),
            ("static files and dynamic pages, both faster", "One CloudFront, two origins: S3 and the ALB"),
            ("users only on some continents, cut cost", "CloudFront, a price class leaving out the rest"),
            ("route requests to several microservices", "One ALB, a rule per path"),
            ("EKS, routing to its services", "ALB, from the AWS Load Balancer Controller"),
            ("the app runs entirely in the browser, cut cost", "S3 + CloudFront; the web servers go"),
            ("reuse the ALB's certificate on CloudFront", "No: CloudFront needs one in us-east-1"),
        ],
        "kinds": [
            ("Load balancers", [
                ("ALB", "HTTP: paths, headers, Cognito login, WAF"),
                ("NLB", "TCP or UDP, fixed IP, PrivateLink, millions a second"),
                ("Gateway LB", "third-party firewalls and appliances in the path"),
            ]),
            ("CloudFront origins", [
                ("S3 origin", "only files: HTML, JavaScript, images; no servers to pay for"),
                ("ALB origin", "pages your servers build; the servers stay"),
                ("Both", "one distribution, a behaviour per path"),
            ]),
        ],
        "traps": [
            "Users worldwide is not, alone, a reason for several Regions: one Region behind CloudFront is cheaper.",
            "CloudFront speeds up dynamic content too: the user connects at the edge and AWS's own network carries the rest.",
            "Global users who need the logic and a relational database near them: Fargate in each Region and an Aurora global database.",
            "Global Accelerator caches nothing, so it is not the answer when the content can be cached.",
            "An internet-facing load balancer sits in the public subnets. The "
            "instances and the database sit in private subnets behind it. Nothing "
            "else of yours belongs in a public subnet but the NAT gateway.",
            "Both load balancers can send to IP addresses, including on premises "
            "over Direct Connect. What picks the NLB is the fixed address.",
            "Anything about a header, a path, a cookie or what is inside a "
            "request is web-level work, and that is the ALB. An NLB never looks "
            "inside a request, so it cannot route on a header or block one by "
            "rule, however the option words it.",
            "AWS WAF attaches to an ALB, CloudFront or an API, never to an NLB. "
            "Rules-based blocking of web requests means WAF, and WAF means ALB. "
            "Network Firewall is a different thing: it filters the VPC's traffic "
            "by address, port and domain, not web requests by their content.",
            "Only an ALB can authenticate at the edge, redirect to HTTPS, return a "
            "fixed response, or send to Lambda.",
            "Global Accelerator carries any protocol and caches nothing. CloudFront "
            "caches and is for web traffic.",
            "CloudFront behaviours match on the path. Choosing an origin by the user's country or a header needs Lambda@Edge.",
            "API Gateway in front of microservices charges per request on top, so one ALB with path rules is the cheaper router.",
            "An ALB serves one Region, so spreading traffic across Regions is Route 53, never one ALB with targets in both.",
            "On Elastic Beanstalk, a slice of live traffic to a new version is the traffic-splitting policy, not ALB rules you edit.",
            "'Runs entirely in the browser' means the site is only files. CloudFront in front of the ALB still pays for servers doing nothing. S3 + CloudFront drops them.",
            "CloudFront only takes a certificate from us-east-1. The ALB's certificate in another Region cannot be reused. Make a new one in us-east-1.",
        ],
    },

    {
        "id": "read-scale",
        "stem": r"report(ing)? quer|read (traffic|queries|load|performance)|without (affecting|impacting)|offload|read-heavy|same quer|repeated(ly)? (read|quer)|latency of (the )?(read|quer)|write load|heavy write|writes? (spike|increase)",
        "choices": [
            r"read replica",
            r"Aurora Serverless",
            r"ElastiCache",
            r"\bDAX\b",
            r"reader endpoint",
            r"Multi-AZ",
            r'RDS Proxy',
            r'Aurora Auto Scaling|Aurora Replicas?',
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
            ("heavy writes in sudden spikes, no code changes", "Aurora Serverless, "
                                                               "with max ACUs set for the peak"),
            ("too many connections, not too much load", "RDS Proxy"),
            ("RDS reads repeated, keep schema, least to run", "ElastiCache, not Memcached on EC2"),
            ("data that rarely changes, CPU high on searches", "ElastiCache, lazy loading"),
            ("read surges at known times, MySQL", "Aurora, Auto Scaling of replicas"),
            ("a shared cache that must persist", "ElastiCache for Redis (Memcached keeps nothing)"),
        ],
        "kinds": [
            ("ElastiCache engines", [
                ("Redis (Valkey)", "keeps data, fails over, sorted sets"),
                ("Memcached", "simplest, many threads, keeps nothing"),
            ]),
            ("Cache strategies", [
                ("Lazy loading", "fill on a miss; data that rarely changes"),
                ("Write-through", "every write goes to the cache too"),
            ]),
        ],
        "traps": [
            "ElastiCache does not fetch from the database for you. The application "
            "misses, queries, and writes the value in. DAX does go to the table "
            "itself, which is the difference.",
            "A read replica is promoted by hand, so it is a recovery tool rather than "
            "one that fails over on its own.",
            "DAX serves eventually consistent reads only; a strongly consistent read "
            "goes to the table.",
            "RDS Proxy fixes too many connections, not too much load: it adds no "
            "capacity and caches nothing. DAX is for DynamoDB only; for RDS the cache "
            "is ElastiCache.",
            "Heavy write load: a cache or more EC2 servers will not help, because a "
            "cache only serves reads and more servers send more writes. Moving RDS "
            "for MySQL or PostgreSQL to Aurora Serverless is not extreme: it speaks "
            "the same language, so the application only needs a new connection "
            "address, which is configuration, not code.",
            "DAX works only with DynamoDB; 'DAX on RDS' does not exist. Memcached you install on EC2 is never least overhead.",
            "RDS Multi-AZ adds no reads and RDS cannot auto scale replicas. Read surges on MySQL mean Aurora Auto Scaling.",
            "Instance store is wiped on stop and belongs to one instance, so it is never a shared or lasting cache.",
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
            ("old app writes to NFS or SMB, AWS reads the files", "S3 File Gateway"),
            ("local access to ALL the data, backed up to AWS", "Volume Gateway, stored mode"),
            ("only recent data kept locally, the rest in AWS", "Volume Gateway, cached mode"),
            ("tapes, and the backup software must not change", "Tape Gateway, then Deep Archive"),
            ("a steady private line for everything", "Direct Connect"),
        ],
        "kinds": [
            ("Storage Gateway", [
                ("S3 File Gateway", "NFS or SMB share; files land in S3"),
                ("FSx File Gateway", "local cache for FSx for Windows"),
                ("Volume, stored", "all data local, snapshots to AWS"),
                ("Volume, cached", "recent data local, the rest in AWS"),
                ("Tape Gateway", "virtual tapes; same backup software"),
            ]),
            ("Snowball Edge", [
                ("Storage Optimized", "moving a lot of data"),
                ("Compute Optimized", "running work with no connection"),
            ]),
        ],
        "traps": [
            "Work out how long the data would take over the line you have. Past "
            "roughly a week, posting a device wins.",
            "Snowball Edge comes in two kinds. Storage Optimized is for moving data; "
            "Compute Optimized is for running work where there is no connection.",
            "Direct Connect takes weeks to install, so it is never the answer to "
            "something needed this month.",
            "Volume Gateway sends disk snapshots to AWS, not files. If something in AWS must read the files, it is File Gateway.",
            "Cached mode keeps only recent data on site. 'Local access to all the data' means stored mode.",
            "Partners on SFTP: Transfer Family. File Gateway is an NFS or SMB share, and DMS moves databases, not files.",
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
            ("NetApp, or SMB and NFS on the same data", "FSx for NetApp ONTAP"),
            ("one server, one zone, a plain disk", "EBS"),
            ("objects rather than files", "S3"),
            ("shared Linux files, mostly rarely read", "EFS, lifecycle to Infrequent Access"),
            ("Lustre that must be highly available or kept", "FSx for Lustre, persistent"),
            ("give a customer more block storage on request", "EBS Elastic Volumes, grown in place"),
        ],
        "kinds": [
            ("FSx", [
                ("for Windows", "SMB, Active Directory"),
                ("for Lustre", "HPC and training; linked to a bucket"),
                ("for NetApp ONTAP", "SMB and NFS on the same data"),
                ("for OpenZFS", "Linux NFS moved from ZFS"),
            ]),
            ("Lustre deployment", [
                ("Scratch", "cheapest, no second copy, short jobs"),
                ("Persistent", "kept, repaired, highly available"),
            ]),
            ("EFS storage classes", [
                ("Standard", "files in use"),
                ("Infrequent Access", "files not opened for N days"),
                ("Archive", "touched a few times a year"),
            ]),
            ("EFS throughput", [
                ("Elastic", "rises with the work; spikes nobody can size"),
                ("Bursting", "grows with what is stored; credits run out"),
                ("Provisioned", "a fixed rate you set and pay for"),
            ]),
        ],
        "traps": [
            "An EBS volume lives in one zone. Multi-Attach exists but does not cross "
            "zones, and an ordinary file system cannot safely be shared that way.",
            "EFS throughput: bursting goes by how much is stored and runs out of "
            "credit; elastic rises with the work and suits a spike nobody can size.",
            "FSx for Lustre links to a bucket and presents the objects as files, which "
            "is what training jobs want.",
            "S3 is not a file system. An option that mounts a bucket on the servers is the trap; shared files across servers is EFS.",
            "EFS has its own cheaper class. Lifecycle to Infrequent Access cuts the bill with no change to mount points.",
            "Lustre scratch is cheapest but keeps no second copy. Highly available or long-lived means persistent.",
            "One EFS mount target per zone. Each instance mounts through its own zone's target, for the lowest latency.",
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
            ("one plan for EC2 and Fargate or Lambda", "Compute Savings Plan"),
            ("it can be interrupted and tried again", "Spot"),
            ("short, unpredictable, or being measured", "On-Demand"),
            ("a licence counted by socket or core", "Dedicated Host"),
            ("you need it off other tenants' hardware", "Dedicated Instance"),
            ("known baseline, surges, no interruptions", "RIs for the baseline, On-Demand above"),
            ("runs part of the day, stopped the rest", "On-Demand"),
            ("stateless, copes with losing a server", "Spot, in an Auto Scaling group"),
            ("Spot keeps failing, or fewest interruptions", "Capacity-optimized, more instance types"),
            ("most cost-effective, upfront allowed", "All Upfront"),
            ("EMR, and no data may be lost", "Primary and core On-Demand, task nodes Spot"),
        ],
        "kinds": [
            ("Reserved Instances", [
                ("Standard", "biggest discount; cannot change instance family"),
                ("Convertible", "smaller discount; can change family"),
            ]),
            ("Savings Plans", [
                ("Compute", "EC2, Fargate and Lambda, any family or Region"),
                ("EC2 Instance", "one family in one Region; bigger discount"),
            ]),
            ("How you pay", [
                ("All Upfront", "most saving"),
                ("Partial Upfront", "in between"),
                ("No Upfront", "least saving"),
            ]),
            ("Spot allocation", [
                ("capacity-optimized", "fewest interruptions"),
                ("price-capacity-optimized", "balances price and interruptions"),
                ("lowest-price", "cheapest, interrupted most"),
            ]),
        ],
        "traps": [
            "Spot is taken back with two minutes' warning, so it is never the answer "
            "for anything that cannot be interrupted.",
            "A Dedicated Host is the one that shows you sockets and cores, which is "
            "what a bring-your-own-licence question needs. A Dedicated Instance does "
            "not.",
            "A Savings Plan is a dollars-per-hour commitment, not a reservation, so it keeps paying off when the instance type changes.",
            "A Reserved Instance is paid every hour whether it runs or not, so anything stopped most of the day is cheaper On-Demand.",
            "All Upfront gives the biggest discount and No Upfront the smallest, so 'most cost-effective' means All Upfront.",
            "Capacity-optimized gives the fewest interruptions; price-capacity-optimized also weighs price, so it is not the 'fewest' pick.",
            "EMR core nodes hold the HDFS data, so only task nodes go on Spot when no data may be lost.",
            "Wanting the newest instance generation every year rules out a 3-year term and Standard Reserved Instances.",
        ],
    },

    {
        "id": "network-join",
        "stem": r"on-premises|on premises|data cent(er|re)|hybrid|private connect|without (traversing|using) the (public )?internet|between VPCs",
        "choices": [
            r"Direct Connect",
            r"Site-to-Site VPN",
            r"Transit Gateway",
            r"VPC peering|peering connection|[Pp]eer (each|the|all|every)",
            r"PrivateLink",
            r"VPC endpoint",
            r"Resolver (inbound|outbound) endpoint|Route 53 Resolver",
        ],
        "title": "How to join two networks",
        "area": "networking",
        "rows": [
            ("steady, predictable, never the internet", "Direct Connect"),
            ("needed this week, cost matters", "Site-to-Site VPN"),
            ("both, with the VPN as the fallback", "Direct Connect, VPN backup"),
            ("exactly two VPCs", "VPC peering"),
            ("more than a few VPCs, many accounts, or many sites", "Transit "
                                                                   "Gateway"),
            ("hundreds of VPCs, or a thousand", "Transit Gateway, nothing else "
                                                "scales to it"),
            ("many VPCs that must not see each other", "Transit Gateway, a route "
                                                       "table per attachment"),
            ("reach one service, not a whole network", "PrivateLink"),
            ("a SaaS product that is hosted on AWS", "PrivateLink"),
            ("offer your own service to other VPCs", "An NLB, with a PrivateLink "
                                                    "endpoint service in front"),
            ("traffic must stay in the company's private address space",
             "PrivateLink: an interface endpoint with a private address, reached "
             "over the VPN"),
            ("reach S3 or DynamoDB from inside a VPC", "A gateway VPC endpoint"),
            ("names on premises must resolve from the VPC", "Route 53 Resolver, "
                                                            "an outbound endpoint"),
            ("names in the VPC must resolve from on premises", "Route 53 Resolver, "
                                                               "an inbound endpoint"),
            ("one VPC to on premises, cheapest", "Site-to-Site VPN"),
            ("one office, two VPCs that must not see each other", "A VPN to each VPC, no peering"),
        ],
        "kinds": [
            ("VPN", [
                ("Site-to-Site", "a whole office or data centre"),
                ("Client VPN", "one person's laptop"),
            ]),
            ("Direct Connect", [
                ("Dedicated", "your own port: 1, 10 or 100 Gbps"),
                ("Hosted", "a slice from a partner; smaller speeds"),
                ("Direct Connect gateway", "one line to many VPCs or Regions"),
            ]),
        ],
        "traps": [
            "Hundreds of VPCs is always the transit gateway. Peering is one link "
            "between two VPCs, is not transitive, and a VPC can have at most 125 "
            "of them. Shared across accounts with Resource Access Manager.",
            "Keeping spokes apart on a transit gateway is done with a route table "
            "per attachment, each allowed only to the shared VPC. The default "
            "route table lets every spoke reach every other.",
            "PrivateLink's provider side is always a Network Load Balancer with an "
            "endpoint service in front of it. There is no gateway endpoint for "
            "anything but S3 and DynamoDB.",
            "PrivateLink creates no network path. From your own building it still "
            "needs Direct Connect or a VPN underneath. A gateway endpoint works "
            "only from inside the VPC; from on premises you need the interface "
            "kind.",
            "A company you do not control, such as a SaaS provider, is reached by "
            "PrivateLink. A VPN or a transit gateway needs both sides to take "
            "part, which is not on offer.",
            "Name resolution across a VPN is the Route 53 Resolver, not a DNS "
            "server you run on EC2, not a public hosted zone, and never a "
            "network ACL. Outbound sends the VPC's questions out; inbound takes "
            "on-premises questions in.",
            "Direct Connect reaches a transit gateway only through a Direct "
            "Connect gateway.",
            "With only one VPC, a transit gateway is cost with no gain. It earns its place at many VPCs or many sites.",
            "VPCs kept apart means no path between them: no peering, no shared route table. Separate VPNs, or a route table each.",
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
            ("you must control key rotation", "A customer managed key"),
            ("admins manage the keys, an app only decrypts", "Customer managed key; app role gets kms:Decrypt"),
            ("dedicated hardware, but RDS or S3 uses the key", "KMS custom key store, backed by CloudHSM"),
            ("every new EBS volume encrypted, none without", "EBS encryption by default, set per Region"),
            ("an existing unencrypted database or volume", "Snapshot, encrypted copy, restore"),
            ("uploads must use one key, users cannot change it", "SSE-KMS, bucket policy denying other keys"),
        ],
        "kinds": [
            ("KMS keys", [
                ("AWS owned", "you never see it"),
                ("AWS managed", "you see it; rotates yearly; no control"),
                ("Customer managed", "your rotation, your key policy, audit"),
                ("Custom key store", "key material in your CloudHSM"),
            ]),
            ("S3 encryption", [
                ("SSE-S3", "nobody asked who holds the key"),
                ("SSE-KMS", "control and audit the key; add Bucket Key"),
                ("DSSE-KMS", "two layers, for rules that demand it"),
                ("SSE-C", "you send the key every time; AWS keeps none"),
                ("Client-side", "encrypted before it leaves you"),
            ]),
        ],
        "traps": [
            "The data key encrypts the data, and KMS encrypts the data key. Rotation "
            "changes the outer key, so nothing is written again.",
            "Only a customer managed key lets you set who may use it and see every "
            "use. An AWS managed key does not.",
            "A multi-Region key is for the same key material in two Regions, which is "
            "a different question from who holds it.",
            "Only a customer managed key lets you control rotation. AWS managed keys rotate yearly on their own; AWS owned keys you never see.",
            "Least privilege splits the jobs: admins create, rotate and delete; the app role only decrypts. 'Full access' is never it.",
            "Encryption cannot be switched on for an existing database or volume. Snapshot it, copy the snapshot encrypted, restore.",
            "An ACM public certificate cannot be installed on an instance. For the hop behind the ALB, self-signed is enough.",
            "CloudHSM on its own does not plug into RDS or S3. They use it through a KMS custom key store.",
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
            ("code in an ECS task calls S3 or DynamoDB", "The task role"),
            ("ECS pulls the image or reads a secret at start", "The task execution role"),
            ("keep everyone to certain Regions", "A policy with aws:RequestedRegion"),
            ("each team's EMR jobs get only their own access", "EMR runtime roles"),
        ],
        "kinds": [
            ("Policy types", [
                ("Identity policy", "on a user, group or role"),
                ("Resource policy", "on the thing: bucket, queue, key"),
                ("SCP", "a ceiling for an account; never grants"),
                ("Permissions boundary", "a ceiling for one user or role"),
                ("Session policy", "narrows one assumed session"),
            ]),
        ],
        "traps": [
            "A role is assumed and its credentials expire. Anything that copies an "
            "access key onto a server is the wrong answer.",
            "A service control policy sets a maximum and never grants anything, and "
            "does not apply to the management account.",
            "Across accounts you need both ends: the trust policy on the role and the "
            "permission on the caller.",
            "Users of your own web application sign in through Cognito, never "
            "through IAM or Identity Center, which are for people using AWS "
            "itself. A Cognito user pool federates with AD FS, Google or any SAML "
            "or OpenID provider, and an ALB can demand that sign-in before it "
            "forwards anything. Directory Service and AD Connector join servers "
            "and desktops to a domain; they do not log users into a web page.",
            "Task role is what your code uses. Task execution role is what ECS uses to start the task. The app reading S3 is the task role.",
            "Access denied and the policy has a condition: the condition was not met. Check source IP, Region or MFA first.",
            "KMS and S3 permissions go on the role the code runs as: the Lambda execution role, the ECS task role. Never on the function.",
            "An instance profile is shared by every job on the cluster, so it cannot keep one team's access apart from another's.",
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
            ("growing, and it must be resilient", "Auto Scaling group across zones, ALB"),
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
            "A group with min, max and desired all set to the baseline can never grow, so it cannot meet a surge.",
        ],
    },

    {
        "id": "scaling-policy",
        "stem": r"start-?up time|initiali[sz]ation latency|slow to (start|boot)|long (time )?to (start|boot|launch)|large AMI",
        "choices": [
            r"target tracking",
            r"step scaling",
            r"simple scaling",
            r"scheduled scaling|scheduled action",
            r"predictive scaling",
            r"warm pool",
            r'fast snapshot restore|\bFSR\b',
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
            ("a large AMI is slow on first boot", "EBS fast snapshot restore"),
            ("slow to start, and the peak must be met", "Warm pool, and max set for the peak"),
        ],
        "kinds": [
            ("Scaling policies", [
                ("Target tracking", "keep one number steady; the default"),
                ("Step", "bigger alarm, bigger step"),
                ("Simple", "one step, then waits"),
                ("Scheduled", "a time you can name"),
                ("Predictive", "a pattern that repeats daily or weekly"),
            ]),
        ],
        "traps": [
            "Target tracking is the one to reach for unless the question gives a "
            "reason not to. Step scaling is for when the size of the response has "
            "to vary with how far out the number is.",
            "Memory and disk space are not there until the CloudWatch agent is "
            "installed. Processor and network are.",
            "A warm pool answers slow starts, not slow scaling decisions: it is "
            "about how long an instance takes to be useful.",
            "A warm pool never goes past the group's maximum, so set max for the peak or the spare instances have nowhere to go.",
            "Slow because the disk loads from a big snapshot is fast snapshot restore; slow because the app sets itself up is a warm pool.",
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
            ("EC2 to RDS, no long-term credentials", "IAM role, IAM database auth token"),
        ],
        "kinds": [
            ("Where secrets live", [
                ("Secrets Manager", "rotates itself; RDS built in"),
                ("Parameter Store, Standard", "free; settings; no rotation"),
                ("Parameter Store, Advanced", "bigger values, policies, a fee"),
                ("SecureString", "a Parameter Store value encrypted with KMS"),
            ]),
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
            "IAM database authentication replaces the password, so adding Secrets Manager mixes two ideas. The pair is an IAM role plus a token.",
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
            ("public may read, nobody may change until a date", "CloudFront with OAC, plus Object Lock"),
            ("only certain outside IP addresses may read", "A bucket policy with aws:SourceIp"),
            ("only one AWS service may write, for named accounts", "Bucket policy: that service + aws:SourceAccount"),
        ],
        "kinds": [
            ("Object Lock", [
                ("Compliance mode", "nobody can lift it, not even root"),
                ("Governance mode", "someone with permission can lift it"),
                ("Legal hold", "no end date; on until removed"),
            ]),
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
            "'Only from this VPC' is a Deny when aws:SourceVpc does not match. An Allow with a not-equal condition is backwards.",
            "OAC lets only CloudFront in. It cannot filter callers by IP address; that is a bucket policy condition.",
            "Compliance mode for regulators, governance mode when an admin may need to lift it. 'Regulatory' means compliance.",
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
            r'Instance Connect Endpoint|EIC Endpoint',
        ],
        "title": "How a private instance reaches out",
        "area": "networking",
        "rows": [
            ("a private subnet needs the internet", "A NAT gateway in a public "
                                                    "subnet, and a route to it"),
            ("the same, but over IPv6", "An egress-only internet gateway"),
            ("only S3 or DynamoDB, IPv4, from inside the VPC", "A gateway endpoint, which is free"),
            ("any other AWS service, privately", "An interface endpoint"),
            ("it must survive losing a zone", "One NAT gateway per zone, and a "
                                              "route table per zone"),
            ("it need not survive losing a zone, and cost matters", "One NAT "
                                                                    "gateway, every "
                                                                    "private subnet "
                                                                    "routed to it"),
            ("cheapest, and you will manage it yourself", "A NAT instance"),
            ("S3 or DynamoDB over IPv6, or from on premises", "Interface endpoints, not gateway"),
            ("the instances may reach only certain buckets", "Gateway endpoint, and the role names the buckets"),
            ("shell into private instances, no agent, no public IP", "EC2 Instance Connect Endpoint"),
            ("private Lambda to DynamoDB, no internet, most secure", "A gateway endpoint for DynamoDB"),
            ("only this one table or bucket may go through it", "An endpoint policy on the gateway endpoint"),
            ("the bucket or table must refuse every other way in", "Its policy requires aws:sourceVpce"),
            ("where the NAT gateway goes", "A public subnet; the private route points at it"),
            ("where the egress-only gateway goes", "On the VPC, in no subnet, like an internet gateway"),
        ],
        "kinds": [
            ("VPC endpoints", [
                ("Gateway", "S3 and DynamoDB only; free; IPv4; same VPC"),
                ("Interface", "most services; by the hour; works from on premises"),
                ("Gateway Load Balancer", "send traffic through appliances"),
            ]),
            ("A path, or a filter", [
                ("Gateway endpoint", "the path: private, to S3 or DynamoDB, no internet"),
                ("Endpoint policy", "what may use the path: which table, which bucket"),
                ("Security group", "a filter on an instance; makes no path"),
                ("Network ACL", "a filter on a subnet; makes no path"),
            ]),
            ("Ways out", [
                ("NAT gateway", "IPv4; sits in a public subnet; by the hour; one per zone"),
                ("NAT instance", "an EC2 you run; never the answer now"),
                ("Egress-only gateway", "IPv6; on the VPC, in no subnet; free; out, never in"),
            ]),
        ],
        "traps": [
            "A NAT gateway costs by the hour whether it carries anything or not. "
            "For a test or development environment that does not need to survive "
            "a zone, one gateway shared by every private subnet is the saving. "
            "Production keeps one per zone.",
            "An internet gateway is one per VPC and lives in no zone. An option "
            "that puts one in each zone, or in a subnet, is nonsense, and so is a "
            "NAT device in a private subnet: it needs the public subnet's route "
            "to the internet gateway to get out. An egress-only internet gateway "
            "is IPv6 only.",
            "A NAT gateway lives in one zone. One per zone, with each private subnet "
            "routing to its own, or losing that zone takes everyone's internet.",
            "A shared route table is the trap. A route has one target, so one "
            "table shared by every private subnet sends them all to one NAT "
            "gateway in one zone. One route table per private subnet, each "
            "pointing at its own zone's NAT gateway.",
            "Traffic to S3 through a NAT gateway is charged by the gigabyte. A "
            "gateway endpoint carries it for nothing. Cut the NAT bill means add "
            "the endpoint.",
            "The NAT gateway goes in the public subnet. The route to it goes in the "
            "private subnet's route table. Questions swap these.",
            "A NAT instance needs source and destination check turned off, and a "
            "security group. A NAT gateway needs neither.",
            "Gateway endpoints carry IPv4 only and work only inside their own VPC. IPv6, or traffic from on premises, needs interface endpoints.",
            "Session Manager needs the SSM Agent and a way out to Systems Manager, so 'no agents' means EC2 Instance Connect Endpoint.",
            "A security group or network ACL only filters traffic. It makes no path. With no internet, the Lambda still cannot reach DynamoDB. The gateway endpoint is the path.",
            "A security group or network ACL sees addresses, not tables. It cannot say 'this table only'. An endpoint policy can.",
            "DynamoDB and S3 never go inside a VPC. An option that puts the table in your VPC is wrong.",
            "An egress-only internet gateway goes in no subnet. It attaches to the VPC, like an internet gateway. The private subnet's route sends ::/0 to it.",
            "Every IPv6 address is public, so there is nothing to translate. IPv6 needs no NAT, only a gateway that refuses connections started from outside.",
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
            ("log DNS queries and their response codes", "Route 53 query logging"),
            ("one account sees every account's findings", "A delegated administrator account"),
            ("check settings against your rules, then fix or tell", "Config rule, then SSM remediation or Lambda"),
            ("mask personal data before it lands in S3", "Firehose, with a Lambda transform"),
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
            "Config finds and can fix after the fact. It never stops a thing being made: that is an SCP, an IAM policy or an account setting.",
            "Macie finds personal data and reports it. It never masks or deletes; that is Lambda, run by EventBridge or Firehose.",
            "Macie, GuardDuty, Security Hub or Access Analyzer across an organization: first name a delegated administrator.",
            "CloudTrail records API calls, not DNS lookups. What Route 53 answered is query logging.",
            "Inspector finds flaws but never patches; patched AMIs for an Auto Scaling group come from EC2 Image Builder.",
            "A Security Hub custom action is a button a person presses, so an automatic response is an EventBridge rule and Lambda.",
        ],
    },

    {
        "id": "trail-watch",
        "stem": r"CloudTrail|CloudWatch|Flow Logs|\blogs?\b|metric|alarm|monitor|audit|traffic",
        "choices": [
            r"CloudTrail",
            r"CloudWatch",
            r"Flow Logs",
            r"X-Ray",
            r"access logs?",
        ],
        "title": "CloudTrail, CloudWatch or Flow Logs",
        "area": "security",
        "rows": [
            ("who deleted the bucket, who changed the rule", "CloudTrail"),
            ("CPU, errors, an alarm when it is too high", "CloudWatch"),
            ("application logs from servers or Lambda", "CloudWatch Logs"),
            ("network traffic to and from the interfaces", "VPC Flow Logs"),
            ("traffic logs to OpenSearch, near real time", "Flow Logs to CloudWatch Logs, then Firehose"),
            ("each web request to the site", "ALB or CloudFront access logs"),
            ("which step of a request is slow", "X-Ray"),
            ("memory or disk space on an instance", "The CloudWatch agent"),
            ("keep the API record for years, tamper-proof", "A CloudTrail trail to S3, log file validation"),
        ],
        "kinds": [
            ("Which record", [
                ("CloudTrail", "who did what to your AWS account: API calls"),
                ("CloudWatch", "how things are running: metrics, logs, alarms"),
                ("VPC Flow Logs", "network traffic: addresses, ports, allowed or rejected"),
                ("Access logs", "each web request, from the ALB or CloudFront"),
                ("X-Ray", "one request's path through several services"),
                ("AWS Config", "how a resource is set up, and what changed"),
            ]),
            ("Getting logs out", [
                ("Subscription filter", "sends CloudWatch Logs on to Firehose or Lambda"),
                ("Data Firehose", "delivers to OpenSearch, S3 or Redshift; no code"),
                ("Kinesis Data Streams", "you write the reader; for replay or many readers"),
            ]),
        ],
        "traps": [
            "Remember it: a trail is footprints, who did it. A watch is a check on health, how it runs.",
            "Traffic is never CloudTrail. CloudTrail records API calls, like someone deleting a bucket. Packets and connections are VPC Flow Logs.",
            "VPC Flow Logs go to CloudWatch Logs, S3 or Firehose. Never to a CloudTrail trail.",
            "Into OpenSearch with no code: Data Firehose. Kinesis Data Streams needs a reader you write, so it is more work.",
            "Memory and disk space are not in CloudWatch until you install the CloudWatch agent.",
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
            r'Bot Control',
            r'IP reputation',
        ],
        "title": "Which defence, and where",
        "area": "security",
        "rows": [
            ("SQL injection, cross-site scripting, bad requests", "WAF, managed rules"),
            ("too many requests from one address", "WAF, a rate-based rule"),
            ("a known list of bad addresses", "WAF, an IP set"),
            ("a big DDoS, and a team to call", "Shield Advanced"),
            ("several resources that share one load, blue/green", "Shield Advanced "
                                                                   "protection group, "
                                                                   "Sum"),
            ("several resources that each carry the same", "Shield Advanced "
                                                            "protection group, "
                                                            "Mean"),
            ("resources that differ a lot in size", "Shield Advanced protection "
                                                    "group, Max"),
            ("the same WAF or security group rules in every account", "Firewall Manager"),
            ("block a whole country on a distribution", "CloudFront geographic "
                                                        "restriction"),
            ("inspect traffic inside the VPC", "Network Firewall"),
            ("block one address at the subnet", "A network ACL deny rule"),
            ("unused or duplicate security group rules", "Firewall Manager, an audit policy"),
            ("stop subnet A sending to subnet B", "Outbound deny in subnet A's network ACL"),
            ("automated requests from all over the world", "WAF Bot Control managed rules"),
            ("SQL injection on API Gateway, least effort", "WAF on the API itself, no CloudFront"),
            ("new CVEs, known exploits, bad inputs", "WAF, AWS managed rule groups"),
        ],
        "kinds": [
            ("Shield", [
                ("Standard", "on and free; common floods"),
                ("Advanced", "big DDoS, a team to call, bill refunded"),
            ]),
            ("WAF rules", [
                ("Managed rule groups", "known exploits, kept updated by AWS"),
                ("Rate-based", "too many requests from one address"),
                ("IP set", "allow or block a list of addresses"),
                ("Bot Control", "bots, spotted by behaviour"),
            ]),
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
            "In a protection group, Mean sounds the most reasonable and is the "
            "trap for a blue/green shift: the average barely moves while the new "
            "balancer's rise reads as an attack. Sum sees the pair as one load.",
            "Firewall Manager runs WAF, Shield, security groups and Network Firewall across accounts. Config only watches them.",
            "WAF reads only the first part of a request body (8 KB on an ALB). Larger bodies follow the rule's oversize setting.",
            "Bots from everywhere keep changing address, so an IP list misses them. Bot Control spots them by behaviour.",
            "WAF attaches straight to an API Gateway REST API. Adding CloudFront just to hold WAF is an extra layer.",
            "Shield stops floods of traffic, not exploits; protection against new vulnerabilities is WAF managed rules, kept updated by AWS.",
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
            ("hot data fast, cold data cheap, same SQL", "Redshift for hot, Spectrum for cold"),
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
            "Logs out of CloudWatch Logs and into OpenSearch, S3 or Redshift go by "
            "a subscription filter into Data Firehose, with no code. Data Streams "
            "would need something written to read it. CloudTrail records API "
            "calls; it never carries VPC Flow Logs.",
        ],
    },

    {
        "id": "analytics-where",
        "stem": r"analy[sz]|report|dashboard|visuali[sz]|warehouse|big data|Spark|Hadoop|business intelligence|petabyte|metrics",
        "choices": [
            r"Athena",
            r"Redshift(?! Spectrum)",
            r"Redshift Spectrum",
            r"\bEMR\b",
            r"\bGlue\b",
            r"OpenSearch",
            r"QuickSight",
            r"Apache Flink|Kinesis Data Analytics",
        ],
        "title": "Which analytics service",
        "area": "analytics",
        "rows": [
            ("SQL now and then on S3 files, nothing to run", "Athena"),
            ("reports over years of history, many users", "Redshift"),
            ("warehouse tables plus S3 files, one query", "Redshift Spectrum"),
            ("Spark, Hadoop or Hive, a big batch job", "EMR"),
            ("clean or convert data on a schedule, serverless", "Glue"),
            ("search text, or look through logs", "OpenSearch"),
            ("charts and dashboards for people", "QuickSight"),
            ("live results as the data streams in", "Managed Service for Apache Flink"),
            ("a website's own searches and pages", "The database plus ElastiCache"),
        ],
        "kinds": [
            ("Redshift", [
                ("Provisioned", "a cluster you size; steady use"),
                ("Serverless", "pay when queried; uneven use"),
                ("Spectrum", "queries files in S3 from Redshift"),
            ]),
            ("EMR node types", [
                ("Primary", "runs the cluster"),
                ("Core", "work plus HDFS data; On-Demand"),
                ("Task", "work only; safe on Spot"),
            ]),
        ],
        "traps": [
            "Redshift is a warehouse for reports. It is never the database behind a live website or an order system.",
            "EMR is a cluster you size and look after. 'Least operational overhead' with SQL is Athena or Glue, not EMR.",
            "Athena queries and QuickSight draws. An option that visualises with Athena has the two the wrong way round.",
            "Redshift COPY only loads data in. It calculates nothing, so 'use COPY to work out metrics' is not an answer.",
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
            r'AWS (service )?integration|integration type',
        ],
        "title": "Which front door for an API",
        "area": "compute",
        "rows": [
            ("callers all over the world", "Edge-optimized"),
            ("callers in the same Region, or your own CloudFront in front",
             "Regional"),
            ("only from inside a VPC", "Private, with an interface endpoint"),
            ("JWT, cheapest, straight to an ALB or Lambda", "HTTP API"),
            ("caching, usage plans, API keys, request validation, WAF", "REST API"),
            ("one function, one HTTPS URL, a webhook", "A Lambda function URL"),
            ("two-way and live", "WebSocket API"),
            ("a limit per customer", "Usage plans and API keys, REST only"),
            ("write to DynamoDB or SQS, no code", "AWS service integration, no Lambda"),
            ("only certain IP addresses or accounts", "A resource policy on the API (REST)"),
            ("API keys, and the backend scales alone", "REST API to SQS, workers read it"),
            ("the caller waits minutes for the answer", "Lambda function URL, not API Gateway"),
            ("smaller replies, faster transfer", "Content encoding (compression)"),
        ],
        "kinds": [
            ("API Gateway APIs", [
                ("REST API", "API keys, usage plans, caching, WAF, resource policy"),
                ("HTTP API", "cheaper, JWT built in, private ALB directly"),
                ("WebSocket API", "two-way, live: chat, games"),
            ]),
            ("Endpoint types", [
                ("Edge-optimized", "callers all over the world, through CloudFront"),
                ("Regional", "callers in one Region, or your own CloudFront"),
                ("Private", "only from inside a VPC"),
            ]),
        ],
        "traps": [
            "HTTP API is cheaper and faster but has no caching, no usage plans, no "
            "API keys and no request validation. The moment the question needs any "
            "of those it is REST.",
            "A JWT authorizer is built in to HTTP API. REST needs a Lambda "
            "authorizer or a Cognito authorizer instead.",
            "Edge-optimized already uses CloudFront underneath. To put your own "
            "CloudFront in front, make it Regional.",
            "API Gateway gives up after 29 seconds, so a caller that waits minutes for the answer needs a Lambda function URL.",
            "API Gateway can call DynamoDB, SQS, SNS or Step Functions itself. A Lambda in between is code you did not need.",
            "API Gateway has no security group, subnet or network ACL. Limit callers by IP with a resource policy.",
            "A REST API reaches a private load balancer only through an NLB; an HTTP API can reach a private ALB directly.",
            "API Gateway offers REST, HTTP and WebSocket APIs only; an option offering a gRPC API is a decoy.",
            "SNS and SQS have no web address a third party can call, so a webhook into Lambda is a function URL.",
            "Reserved concurrency limits a function and never makes an API faster.",
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
            r"cross-Region read replicas?",
            r"Aurora Replicas?",
            r"Multi-AZ",
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
            ("Aurora in another Region, no global database offered",
                "Cross-Region read replica, promoted by hand"),
            ("Aurora reads and failover inside one Region", "Aurora Replicas "
                                                            "(never another Region)"),
            ("DynamoDB in two Regions, both writing", "Global tables"),
            ("send users to the Region that is up", "Route 53 failover, with "
                                                    "a health check"),
            ("back to any second in the last 35 days", "Point-in-time recovery"),
            ("S3 in two Regions, one endpoint, nearest bucket", "Multi-Region Access Point, plus CRR"),
            ("an EFS copy in another Region, managed", "AWS Backup, a copy rule to that Region"),
            ("Aurora, other Region, RPO 1 min, RTO 5 min", "Aurora global database"),
        ],
        "kinds": [
            ("Disaster recovery, cheapest first", [
                ("Backup and restore", "hours to recover; cheapest"),
                ("Pilot light", "data copied; servers off until needed"),
                ("Warm standby", "a small copy running; scale it up"),
                ("Multi-site active-active", "both live; seconds; dearest"),
            ]),
        ],
        "traps": [
            "RPO is how much data you may lose. RTO is how long you may be down. "
            "Lower numbers cost more: match the strategy to the numbers given.",
            "A snapshot stays in its Region. Automated RDS backups do not leave the "
            "Region on their own. It only helps elsewhere if you copied it there.",
            "An Aurora global database has one writer. Failing over promotes the "
            "secondary in about a minute. Global tables write in both Regions.",
            "Aurora Replicas and Multi-AZ are both read copies or standbys in the "
            "same Region. When the question says another Region, they are wrong.",
            "A copy of an encrypted snapshot into another Region needs a KMS key in "
            "that Region. A vault lock in compliance mode cannot be undone, not "
            "even by the root user.",
            "A cross-Region read replica never fails over on its own. An option saying it does is false.",
        ],
    },

    {
        "id": "placement",
        "stem": r"placement|low(est)?( possible)? latency between|tightly coupled|\bHPC\b|high.performance computing|node-to-node|inter-node|not .{0,20}same (rack|hardware)|separate hardware|large distributed|network throughput between",
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
            ("lowest latency between nodes, no cluster offered", "Elastic Fabric Adapter"),
            ("no two nodes on the same hardware, 99.99%", "Spread, across three zones"),
        ],
        "kinds": [
            ("Placement groups", [
                ("Cluster", "one rack area; lowest latency; HPC"),
                ("Spread", "each on its own hardware; 7 per zone"),
                ("Partition", "groups on separate racks; Hadoop, Cassandra"),
            ]),
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
            "A spread placement group adds distance for safety, so it never lowers latency between nodes.",
            "99.99% availability needs two or more zones, so a group in one zone cannot promise it.",
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
        "kinds": [
            ("EBS volumes", [
                ("gp3", "default; IOPS set apart from size"),
                ("io2 Block Express", "highest IOPS; Multi-Attach"),
                ("st1", "big sequential reads; cheap; cannot boot"),
                ("sc1", "cold, cheapest; cannot boot"),
            ]),
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
            ("one zone, fastest S3, keep the S3 API", "S3 Express One Zone, a directory bucket"),
            ("a site that runs entirely in the browser", "S3 origin + CloudFront, no web servers"),
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
        "id": "s3-copy",
        "stem": r"replicat|copy .{0,40}(bucket|Region)|single (S3 )?bucket|centrali[sz]ed .{0,30}bucket|must not leave|nearest (S3 )?bucket",
        "choices": [
            r"Cross-Region Replication|\bCRR\b",
            r"Same-Region Replication|\bSRR\b",
            r"Multi-Region Access Point",
            r"Batch Replication|S3 Batch Operations",
            r"lifecycle (polic|rule|config)",
            r"PutObject|Lambda[^.]{0,80}\bcop(y|ies)\b",
        ],
        "title": "How to copy S3 objects to another bucket",
        "area": "storage",
        "rows": [
            ("a copy in another Region, least data lost", "Cross-Region Replication"),
            ("many buckets into one, same Region", "Same-Region Replication"),
            ("logs from many accounts, must stay in the Region", "Same-Region Replication, cross-account"),
            ("one endpoint, nearest bucket, fails over itself", "Multi-Region Access Point, plus CRR"),
            ("objects that were there before replication", "S3 Batch Replication"),
            ("copied within 15 minutes, with a promise", "Replication Time Control"),
        ],
        "kinds": [
            ("S3 replication", [
                ("Cross-Region (CRR)", "a copy in another Region"),
                ("Same-Region (SRR)", "many buckets into one; stays in Region"),
                ("Batch Replication", "objects that were already there"),
                ("Replication Time Control", "15 minutes, promised"),
            ]),
        ],
        "traps": [
            "Replication copies only new objects. Objects already in the bucket need S3 Batch Replication.",
            "Replication needs versioning turned on in both buckets.",
            "A lifecycle rule moves or deletes objects in its own bucket. It never copies them anywhere.",
            "A script or a Lambda that copies objects is the high-effort wrong answer when replication is offered.",
        ],
    },

    {
        "id": "many-accounts",
        "stem": r"accounts|organization|multi-account|landing zone|govern|guardrail|billing|cost (per|by|for each)|chargeback|department|business unit|AWS Budgets|forget to stop",
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
            ("block it before CloudFormation creates it", "A Control Tower proactive control"),
            ("no EBS snapshot may ever be public", "Block public access for snapshots, org-wide"),
            ("stop forgotten instances before the bill grows", "Budgets, forecasted, a stop-EC2 action"),
        ],
        "kinds": [
            ("Control Tower controls", [
                ("Preventive", "blocks it: an SCP"),
                ("Detective", "reports it after: Config"),
                ("Proactive", "checks CloudFormation before it builds"),
            ]),
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
            "Control Tower controls come in three: preventive (an SCP), detective (Config), proactive (checked before CloudFormation builds).",
            "A budget action stops EC2 by itself, so SNS to a Lambda that stops the instances is extra work for the same result.",
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
            r"export .{0,20}to .{0,10}S3|export connector",
            r"Standard-IA\)? table|Standard-Infrequent Access",
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
            ("analyse daily, spare the table's capacity", "Export to S3, then Glue or Athena"),
            ("huge data, rarely read, storage is the bill", "Standard-IA table class"),
            ("busy and unpredictable, cheapest", "On-demand, Standard table class"),
            ("high performance, cheapest, known range", "Auto scaling, target about 70%"),
            ("continuously available across Regions", "Global tables; settle this first"),
            ("session data, expires itself, restorable", "TTL plus point-in-time recovery"),
            ("DAX found not encrypted at rest", "Make a new DAX cluster with it on"),
            ("changes into an S3 data lake, near real time", "Through Data Firehose, which batches"),
        ],
        "kinds": [
            ("Capacity", [
                ("On-demand", "new or unpredictable; pay per request"),
                ("Provisioned", "steady; add auto scaling at about 70%"),
            ]),
            ("Table classes", [
                ("Standard", "busy tables"),
                ("Standard-IA", "storage is the bill; reads are rare"),
            ]),
            ("Indexes", [
                ("Global secondary (GSI)", "any key, added any time"),
                ("Local secondary (LSI)", "same partition key, only at creation"),
            ]),
            ("Reads", [
                ("Eventually consistent", "default, half the cost"),
                ("Strongly consistent", "latest write, same Region only"),
            ]),
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
            "Standard-IA cuts storage cost but makes every read and write dearer. A busy table stays on Standard.",
            "The Athena DynamoDB connector reads the live table and spends its capacity. An export to S3 spends none.",
            "An alarm that calls Lambda to raise capacity is auto scaling built by hand. Pick the built-in auto scaling.",
            "DAX encryption at rest is set when the cluster is made. It cannot be turned on later: make a new cluster.",
            "Export to S3 needs point-in-time recovery turned on for that table. An export that fails on some tables is that.",
            "DynamoDB has no read replicas, and reserved capacity only cuts the bill, so throttling on spikes means on-demand.",
            "Writing each change straight to S3 makes many tiny files, so send changes through Data Firehose, which batches them.",
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
            r"(take|create) a snapshot|manual (copy|snapshot)|copy of the snapshot",
        ],
        "title": "Which RDS feature",
        "area": "database",
        "rows": [
            ("too many connections, Lambda opening them", "RDS Proxy"),
            ("failover must be quicker without reconnecting", "RDS Proxy"),
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
            ("single point of failure, least effort", "Modify the instance to Multi-AZ"),
            ("highly available, back within minutes", "Multi-AZ, fails over in 1 to 2 min"),
            ("keep an automated snapshot past 35 days", "Copy it: the copy is manual, kept"),
        ],
        "kinds": [
            ("Copies of RDS", [
                ("Multi-AZ instance", "one standby; no reads; failover"),
                ("Multi-AZ cluster", "two standbys that serve reads"),
                ("Read replica", "reads; promoted by hand"),
            ]),
            ("Aurora endpoints", [
                ("Cluster", "the writer"),
                ("Reader", "spreads reads across replicas"),
                ("Custom", "a chosen set of replicas, such as for reports"),
            ]),
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
            "Multi-AZ is switched on by changing the running instance. A new instance from a snapshot is more work and loses recent data.",
            "Automated backups are deleted after 35 days at most. A copy becomes a manual snapshot and stays until you delete it.",
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
            r"[Aa]ttach the (Lambda )?function to the VPC|VPC-enabled|connect the function to the VPC|Lambda function to the VPC",
        ],
        "title": "Which Lambda feature",
        "area": "compute",
        "rows": [
            ("it must reach something private in a VPC", "Attach the function to "
                                                         "the VPC's private subnets, "
                                                         "with a security group"),
            ("cold starts hurt", "Provisioned concurrency"),
            ("cold starts hurt, Java, cost first", "SnapStart, on a published version"),
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
            "Reaching a database or anything else private in a VPC is a setting on "
            "the function: its subnets and a security group. Not a VPN, not an "
            "endpoint, not PrivateLink. Those are for reaching things outside the "
            "VPC.",
            "Reserved concurrency set to zero turns the function off. Set to a "
            "number, it is both a ceiling and a guarantee.",
            "Provisioned is speed, reserved is a limit. 'Respond consistently "
            "with low latency' at peak is provisioned concurrency; reserved does "
            "nothing about cold starts and throttles anything over its cap, so it "
            "can make peak latency worse. With API Gateway in front, Lambda with "
            "provisioned concurrency is also less to run than ECS or EKS behind "
            "a load balancer.",
            "SnapStart works only on a published version, never on $LATEST, and never together with provisioned concurrency.",
            "SnapStart copies the start-up memory into every copy, so make unique IDs in the handler, not in the start-up code.",
        ],
    },

    {
        "id": "lambda-concurrency",
        "stem": r"cold start|consistent(?:ly)? .{0,30}latency|concurren|throttl",
        "choices": [
            r"provisioned concurrency",
            r"reserved concurrency",
        ],
        "title": "Provisioned or reserved concurrency",
        "area": "compute",
        # The comparison table, one feature per line: what the feature is, and
        # which of the two has it.
        "rows": [
            ("guarantees the function can run that many at once", "Both (provisioned also starts them in advance)"),
            ("caps the most it can run at once", "Reserved only"),
            ("removes cold starts, steady low latency", "Provisioned only"),
            ("costs extra, even when idle", "Provisioned only (reserved is free)"),
            ("protects a database or other system behind it", "Reserved (provisioned only indirectly)"),
            ("best for: throughput control, fairness between functions", "Reserved"),
            ("best for: low-latency workloads, a known busy peak", "Provisioned"),
            ("switch the function off", "Reserved, set to zero"),
            ("a burst at a named hour, TooManyRequests", "SQS buffer, plus provisioned"),
        ],
        "kinds": [
            ("Concurrency", [
                ("Reserved", "a ceiling and a guarantee; 0 turns it off"),
                ("Provisioned", "kept warm; no cold starts; costs more"),
                ("Unreserved", "the shared pool everything else uses"),
            ]),
            ("How Lambda is called", [
                ("Synchronous", "the caller waits: API Gateway, function URL"),
                ("Asynchronous", "fire and forget; retries; DLQ or destination"),
                ("Event source mapping", "Lambda polls: SQS, Kinesis, DynamoDB Streams"),
            ]),
        ],
        "traps": [
            "Provisioned is speed, reserved is a limit. 'Respond consistently with "
            "low latency' is provisioned; reserved does nothing about cold starts.",
            "Reserved is a cap as well as a guarantee, so at peak it throttles "
            "requests over the cap and can make latency worse.",
            "Provisioned concurrency is billed while it sits warm. For a busy "
            "period you can name, schedule it with Application Auto Scaling.",
        ],
    },

    {
        "id": "route53-policy",
        "stem": r"Route ?53|DNS|routing polic|fail ?over|lowest latency|high-performing|users? in|nearest Region|closest Region",
        "choices": [
            r"latency(-based)? (routing )?polic|latency routing|latency-based",
            r"geolocation",
            r"geoproximity",
            r"failover (routing )?polic|failover record|fail over to",
            r"weighted",
            r"multivalue|multi-value",
            r"simple (routing )?polic|simple record",
            r"IP-based routing",
            r"health check",
            r'private hosted zone',
            r'public hosted zone',
        ],
        "title": "Which Route 53 routing policy",
        "area": "networking",
        "rows": [
            ("fastest answer for each user, several Regions", "Latency"),
            ("users in a country must get one particular answer", "Geolocation"),
            ("like geolocation, but you can lean traffic one way", "Geoproximity, "
                                                                 "with a bias"),
            ("a standby to fall over to on its own", "Failover, with a health "
                                                     "check"),
            ("a share of traffic each: a canary, a staged release", "Weighted"),
            ("several healthy addresses, no load balancer", "Multivalue answer"),
            ("one name, one target, nothing clever", "Simple"),
            ("answer by the range the user's address falls in", "IP-based"),
            ("a name that resolves only inside the VPC", "Private hosted zone, internal ALB"),
        ],
        "kinds": [
            ("Routing policies", [
                ("Simple", "one answer, no health checks"),
                ("Weighted", "a share to each: 90/10"),
                ("Latency", "the fastest Region for each user"),
                ("Failover", "a standby when the health check fails"),
                ("Geolocation", "by the user's country or continent"),
                ("Geoproximity", "by distance, with a bias to shift traffic"),
                ("Multivalue", "several healthy answers, no load balancer"),
                ("IP-based", "by the user's IP range"),
            ]),
            ("Hosted zones", [
                ("Public", "answers anyone on the internet"),
                ("Private", "answers only inside joined VPCs"),
            ]),
        ],
        "traps": [
            "Latency is about speed and picks whichever Region answers quickest "
            "for that user. Geolocation is about where the user is, and sends a "
            "country to one place even when another is quicker. 'Most high-"
            "performing' means latency.",
            "Only failover with a health check moves traffic on its own when a "
            "Region goes down. IP-based routing is for answering by address "
            "range; it is not a failover policy, however an option words it.",
            "An alias A record points at a load balancer, a distribution or a "
            "bucket, costs nothing to query, and works at the top of the domain. "
            "A CNAME cannot sit at the top of the domain at all.",
            "Weighted is a percentage you set; it does not look at health or "
            "speed. Multivalue is up to eight healthy answers, the nearest DNS "
            "gets to a load balancer, and it is not one.",
            "A private hosted zone answers only inside the VPCs joined to it. An internal load balancer is the other half: no public address.",
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
        out.append((spanned / len(pats), spanned, d["id"]))

    # The decision whose destinations the options cover most fully is the one
    # the question is really about. Measured as a share of that decision's own
    # destinations, so a narrow choice the options settle completely, such as
    # provisioned against reserved concurrency, beats a broad one they only
    # touch; the raw count breaks ties.
    out.sort(key=lambda x: (-x[0], -x[1]))
    return [did for _, _, did in out[:limit]]


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