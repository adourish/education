#!/usr/bin/env python3
"""
A small library of architecture pictures, shared between questions.

Six hundred questions do not need six hundred pictures. They keep describing
the same two dozen arrangements: something in front of a bucket, a queue
between a web tier and a worker, a load balancer over an Auto Scaling group.
Drawing each arrangement once and showing it wherever it turns up is less work,
stays consistent, and teaches the pattern rather than the instance.

A diagram is matched to a question by the services its *answer* names, not its
question. The picture has to show the architecture that is correct, or it
teaches the wrong thing with the authority of a drawing.

Each one is a handful of boxes and arrows, not a rendering. The app draws them
at display time in whatever colours the chosen theme uses, so they cost a few
hundred bytes each and work in high contrast and on a phone.

    nodes:  [id, label, kind]   kind is one of the KINDS below
    edges:  [from, to, label]
    when:   every service named here must appear in the answer
    words:  a phrase that must appear in the answer. Required, always. Naming
            two services is not a pattern: plenty of answers mention S3 and
            Lambda while being about something else entirely, and a picture
            that does not belong is worse than no picture. The phrase is what
            says the answer is really doing this thing.
    unless_words: a phrase that rules the picture out. Mostly for the near
            miss that shares the vocabulary: a lifecycle hook is not a storage
            lifecycle, Express One Zone is not One Zone-IA, and an answer that
            says "versioning disabled" must never get the versioning picture.
    unless: no service named here may appear
"""

from __future__ import annotations

import re

# What a box is, which is all the drawing needs to know. Shape carries the
# meaning so the picture still reads with no colour at all.
KINDS = {
    "actor": "people or systems outside AWS",
    "edge": "something at the edge of the network",
    "compute": "something that runs code",
    "store": "something that holds data",
    "queue": "something that holds messages in between",
    "net": "a way in or out",
}

# How a service is spotted in an answer. Shared with the matcher below.
SERVICES = {
    "ALB": r"Application Load Balancer|\bALB\b",
    "NLB": r"Network Load Balancer|\bNLB\b",
    "ASG": r"Auto Scaling",
    "EC2": r"\bEC2\b",
    "S3": r"\bS3\b|Amazon S3",
    "CloudFront": r"CloudFront",
    "Route53": r"Route 53",
    "RDS": r"\bRDS\b",
    "Aurora": r"Aurora",
    "DynamoDB": r"DynamoDB",
    "Lambda": r"\bLambda\b",
    "APIGW": r"API Gateway",
    "SQS": r"\bSQS\b|Simple Queue",
    "SNS": r"\bSNS\b|Simple Notification",
    "EventBridge": r"EventBridge",
    "ECS": r"\bECS\b|Fargate",
    "EKS": r"\bEKS\b",
    "EFS": r"\bEFS\b",
    "FSx": r"\bFSx\b",
    "Glacier": r"Glacier",
    "KMS": r"\bKMS\b",
    "VPCe": r"VPC endpoint|PrivateLink|gateway endpoint|interface endpoint",
    "NAT": r"NAT gateway",
    "TGW": r"Transit Gateway",
    "DX": r"Direct Connect",
    "VPN": r"Site-to-Site VPN",
    "SGW": r"Storage Gateway",
    "Kinesis": r"Kinesis",
    "Cognito": r"Cognito",
    "WAF": r"\bWAF\b",
    "GlobalAccelerator": r"Global Accelerator",
    "Athena": r"Athena",
    "Redshift": r"Redshift",
    "ElastiCache": r"ElastiCache",
    "DAX": r"\bDAX\b",
    "StepFunctions": r"Step Functions",
    "DMS": r"\bDMS\b|Database Migration",
    "Outposts": r"Outposts",
    "Snow": r"Snowball|Snowcone",
    "Backup": r"AWS Backup",
    "SCP": r"service control polic|\bSCP\b|Organizations",
    "MultiAZ": r"Multi-AZ",
    "ReadReplica": r"read replica",
    "Replication": r"Cross-Region Replication|\bCRR\b|replicat",
    "Glue": r"AWS Glue|Glue (Data )?Catalog|Glue crawler",
    "LakeFormation": r"Lake Formation",
    "QuickSight": r"QuickSight",
    "Batch": r"AWS Batch",
    "Fargate": r"Fargate",
    "Firehose": r"Firehose",
    "ObjectLock": r"Object Lock",
    "Lustre": r"Lustre",
}

_RX = {k: re.compile(v, re.I) for k, v in SERVICES.items()}


def services_in(text: str) -> set[str]:
    return {name for name, rx in _RX.items() if rx.search(text or "")}


# --------------------------------------------------------------------------
# The library. Ordered most specific first, because a question matches the
# first picture that fits and a three-service arrangement says more than the
# two-service one inside it.
# --------------------------------------------------------------------------
DIAGRAMS = [
    {
        "id": "fsx-lustre",
        "title": "A very fast file system beside a bucket",
        "when": ["FSx"],
        "words": r"Lustre",
        "nodes": [["s3", "S3 bucket", "store"], ["fsx", "FSx for Lustre", "store"],
                  ["c", "Compute fleet", "compute"]],
        "edges": [["s3", "fsx", "data repository association"],
                  ["fsx", "c", "mounted, sub-millisecond"]],
        "note": "For modelling, training and anything where the processors are waiting on "
                "the disk. It links to a bucket and presents the objects as files. Scratch "
                "is cheapest and keeps no second copy; persistent does. This is the FSx "
                "answer whenever speed is the point and Windows is not mentioned.",
    },
    {
        "id": "sgw-tape",
        "title": "Virtual tapes, so the old backup software carries on",
        "when": ["SGW"],
        "words": r"Tape Gateway|virtual tape|\bVTL\b",
        "nodes": [["bk", "Existing backup software", "actor"],
                  ["tg", "Tape Gateway", "net"], ["s3", "S3", "store"],
                  ["gl", "Glacier Deep Archive", "store"]],
        "edges": [["bk", "tg", "writes tapes over iSCSI"], ["tg", "s3", "kept"],
                  ["s3", "gl", "archived tapes"]],
        "note": "The point is that nothing on the backup side changes: it still thinks it is "
                "writing tapes. Nothing on the AWS side reads these as files, which is what "
                "separates it from a file share backed by a bucket.",
    },
    {
        "id": "ddb-export-s3",
        "title": "A table copied out without touching its capacity",
        "when": ["DynamoDB", "S3"],
        "words": r"export|point-in-time|\bPITR\b",
        "nodes": [["d", "DynamoDB table", "store"], ["ex", "Export to S3", "net"],
                  ["s3", "S3 bucket", "store"], ["q", "Athena or Redshift", "compute"]],
        "edges": [["d", "ex", "full, or only what changed"], ["ex", "s3", "written"],
                  ["s3", "q", "queried or loaded"]],
        "note": "This reads nothing through the table, so it uses no read capacity and needs "
                "no code. Point-in-time recovery has to be on. It is the least-effort answer "
                "wherever a question would otherwise tempt you into Streams and a function.",
    },
    {
        "id": "ddb-metadata-s3",
        "title": "The file in a bucket, the facts about it in a table",
        "when": ["DynamoDB", "S3"],
        "words": r"metadata|pointer|the (key|location|path|URL) (of|to|in)",
        "nodes": [["c", "Client", "actor"], ["s3", "S3 object", "store"],
                  ["d", "DynamoDB table", "store"]],
        "edges": [["c", "s3", "the file itself"], ["c", "d", "its key, and what it is"]],
        "note": "Large things belong in a bucket; the small facts you search on belong in a "
                "table that holds the object key. It keeps items under the size limit and "
                "makes lookups quick without reading the files.",
    },
    {
        "id": "s3-vpce-interface",
        "title": "Reaching a bucket privately, including from your own network",
        "when": ["S3", "VPCe"],
        "words": r"interface (VPC )?endpoint|PrivateLink",
        "nodes": [["src", "Subnet, or on premises", "compute"],
                  ["eni", "Endpoint network card", "net"], ["s3", "S3", "store"]],
        "edges": [["src", "eni", "a private address"], ["eni", "s3", "never leaves AWS"]],
        "note": "This is the kind to pick when the request comes from outside the VPC over "
                "Direct Connect or a VPN, or when the addresses are IPv6: the free gateway "
                "kind can do neither. It is charged by the hour and by the traffic.",
    },
    {
        "id": "privatelink-endpoint-service",
        "title": "Publishing your own service for other networks to reach",
        "when": ["VPCe"],
        "words": r"endpoint service",
        "nodes": [["con", "Consumer, or on premises", "actor"],
                  ["eni", "Interface endpoint", "net"],
                  ["nlb", "Network Load Balancer", "edge"],
                  ["app", "Your targets", "compute"]],
        "edges": [["con", "eni", "a private address on their side"],
                  ["eni", "nlb", ""], ["nlb", "app", ""]],
        "note": "The detail being tested is the balancer: an endpoint service has to sit "
                "behind a Network Load Balancer, or a Gateway Load Balancer. No addresses "
                "overlap and nothing is peered, because the consumer only ever sees an "
                "address in their own subnet.",
    },
    {
        "id": "lambda-exec-role",
        "title": "The one role a function runs as",
        "when": ["Lambda"],
        "words": r"execution role",
        "nodes": [["fn", "Lambda function", "compute"], ["role", "Execution role", "net"],
                  ["svc", "What it may call", "store"]],
        "edges": [["fn", "role", "runs as"], ["role", "svc", "allows the call"]],
        "note": "A function has one role, trusted to lambda.amazonaws.com, and it covers "
                "writing its own logs as well as whatever else it reaches. There is no "
                "second role: that split belongs to ECS, not here.",
    },
    {
        "id": "s3-object-lock",
        "title": "A copy that cannot be deleted yet",
        "when": ["S3"],
        "words": r"Object Lock|\bWORM\b|compliance mode|governance mode|legal hold",
        "nodes": [["u", "Anyone", "actor"], ["b", "Bucket, versioning on", "store"],
                  ["v", "Locked version", "store"]],
        "edges": [["u", "b", "asks to delete"], ["b", "v", "refused until the time is up"]],
        "note": "Versioning has to be on first. Compliance mode stops everyone, including "
                "the account root and AWS, for the stated time. Governance mode can be "
                "lifted by someone holding the bypass permission, which is the whole reason "
                "the exam asks which mode. A legal hold has no end date and is lifted by "
                "hand.",
    },
    {
        "id": "route53-routing-policies",
        "title": "One name, answered differently depending who asks",
        "when": ["Route53"],
        "words": r"weighted|latency-based|geolocation|geoproximity|multivalue",
        "nodes": [["z", "Hosted zone", "edge"], ["w", "Weighted: a share each", "compute"],
                  ["l", "Latency: the quickest", "compute"],
                  ["g", "Geolocation: by country", "compute"],
                  ["m", "Multivalue: several answers", "compute"]],
        "edges": [["z", "w", ""], ["z", "l", ""], ["z", "g", ""], ["z", "m", ""]],
        "note": "Weighted is for sending a measured slice somewhere, which is what a staged "
                "release needs. Latency is for speed, geolocation for rules about where "
                "people are. Multivalue returns up to eight healthy records and is the "
                "nearest DNS gets to spreading load.",
    },
    {
        "id": "route53-active-active",
        "title": "Two Regions both taking traffic",
        "when": ["Route53"],
        "words": r"active-active|both Regions (are )?(live|active)|all Regions serve",
        "nodes": [["u", "Users", "actor"], ["r53", "Route 53", "edge"],
                  ["a", "Region A, live", "compute"], ["b", "Region B, live", "compute"]],
        "edges": [["u", "r53", ""], ["r53", "a", "health checked"], ["r53", "b", "health checked"]],
        "note": "Both sides serve all the time, so losing one costs only the traffic already "
                "in flight. It is the dearest arrangement and the only one that answers a "
                "recovery time of almost nothing. Failover routing is the other shape, where "
                "the second side waits.",
    },
    {
        "id": "rds-iam-auth",
        "title": "Signing in to a database with no stored password",
        "when": ["RDS"],
        "words": r"IAM (database )?authentication|auth(entication)? token",
        "nodes": [["app", "Application", "compute"], ["role", "IAM role", "net"],
                  ["db", "RDS", "store"]],
        "edges": [["app", "role", "asks for a token"], ["role", "db", "token, good for 15 minutes"]],
        "note": "No password is kept anywhere and access is granted and taken away in IAM. "
                "It works with MySQL, MariaDB and PostgreSQL. Secrets Manager is the other "
                "answer: it keeps a real password and rotates it for you.",
    },
    {
        "id": "lambda-async-dlq",
        "title": "Where a failed call goes when nobody is waiting",
        "when": ["Lambda"],
        "words": r"on-failure destination|dead-letter",
        "nodes": [["src", "Event", "actor"], ["fn", "Lambda", "compute"],
                  ["dlq", "Queue or topic", "queue"]],
        "edges": [["src", "fn", "called without waiting"],
                  ["fn", "dlq", "after the retries, the event is kept here"]],
        "note": "An asynchronous call is retried twice by Lambda itself. What is kept here is "
                "the event, so nothing is lost and it can be looked at or put through again. "
                "This is the other way round from a queue in front of a function.",
    },
    {
        "id": "eventbridge-long-job",
        "title": "A schedule that starts something too long for a function",
        "when": ["EventBridge"],
        "words": r"Fargate|\bBatch\b|ECS task",
        "nodes": [["sch", "Schedule or event", "net"],
                  ["run", "Fargate task, or a Batch job", "compute"],
                  ["out", "Where the work lands", "store"]],
        "edges": [["sch", "run", "starts it"], ["run", "out", "writes when done"]],
        "note": "A function stops at 15 minutes, which is exactly why these questions exist: "
                "anything longer has to run as a task or a job. Nothing is left running "
                "between times, so it costs the same kind of nothing as a function would.",
    },
    {
        "id": "snowball-bulk",
        "title": "Moving a great deal of data by post",
        "when": ["Snow"],
        "words": r"Storage Optimized|transfer|migrat|petabyte|terabyte",
        "nodes": [["nas", "On-premises storage", "actor"],
                  ["dev", "Snowball Edge, Storage Optimized", "store"],
                  ["s3", "S3", "store"], ["gl", "Glacier Deep Archive", "store"]],
        "edges": [["nas", "dev", "copied on site"], ["dev", "s3", "shipped back"],
                  ["s3", "gl", "lifecycle, if it is only being kept"]],
        "note": "The sum to do is how long the data would take over the line you have. Past "
                "roughly a week, posting a device wins. Nothing runs on it: that is the "
                "Compute Optimized one.",
    },
    {
        "id": "cognito-identity-pool",
        "title": "A sign-in turned into AWS credentials",
        "when": ["Cognito"],
        "words": r"identity pool",
        "nodes": [["u", "Signed-in user", "actor"], ["ip", "Identity pool", "net"],
                  ["role", "IAM role", "net"], ["res", "S3 or DynamoDB", "store"]],
        "edges": [["u", "ip", "presents the sign-in"], ["ip", "role", "assumes"],
                  ["role", "res", "reaches it directly"]],
        "note": "A user pool answers who someone is. An identity pool is the other half: it "
                "turns that into temporary AWS credentials so the app can reach a bucket or "
                "a table itself, with no server in between. Questions that mention each user "
                "reaching only their own folder are asking for this.",
    },
    {
        "id": "s3-query-in-place",
        "title": "Reporting on what is in the bucket, where it sits",
        "when": ["S3", "Athena"],
        "words": r"Glue|Data Catalog|QuickSight",
        "nodes": [["s3", "S3", "store"], ["g", "Glue Data Catalog", "net"],
                  ["a", "Athena", "compute"], ["q", "QuickSight", "actor"]],
        "edges": [["s3", "g", "crawled, or registered"], ["g", "a", "the table definitions"],
                  ["a", "q", "charts"]],
        "note": "Nothing is loaded and no server is kept running: you pay by the data each "
                "query reads. The catalogue is what makes the files look like tables. This "
                "is the least-effort answer whenever a question wants reports over data "
                "already in a bucket.",
    },
    {
        "id": "rds-cross-region-replica",
        "title": "A copy of the database in another Region",
        "when": ["RDS"],
        "words": r"(replica|read replica) in (another|a different|a second) Region|"
                 r"cross-Region read replica",
        "nodes": [["a", "Primary, Region A", "store"], ["b", "Replica, Region B", "store"],
                  ["app", "Readers nearby", "actor"]],
        "edges": [["a", "b", "copied across, a little behind"], ["b", "app", "local reads"]],
        "note": "Two things at once: readers in that Region get a short trip, and if the "
                "first Region is lost the replica can be promoted to a database of its own. "
                "Promotion is by hand, so this is a recovery tool rather than one that fails "
                "over on its own.",
    },
    {
        "id": "lake-formation-columns",
        "title": "Letting people see some columns and not others",
        "words": r"Lake Formation",
        "nodes": [["lf", "Lake Formation", "net"],
                  ["p", "Permissions by column or row", "net"],
                  ["a", "Athena or Redshift", "compute"], ["u", "Analysts", "actor"]],
        "edges": [["lf", "p", "granted centrally"], ["p", "a", "applied as they query"],
                  ["a", "u", "only what they may see"]],
        "note": "One place to say who may see what, down to a single column, instead of "
                "bucket policies per team. Whatever queries through the catalogue obeys it, "
                "so the same rule covers Athena, Redshift Spectrum and QuickSight.",
    },
    {
        "id": "dx-tgw",
        "title": "One line from your building into many VPCs",
        "when": ["DX", "TGW"],
        "words": r"[Tt]ransit [Gg]ateway",
        "nodes": [["dc", "Your building", "actor"], ["dxg", "Direct Connect gateway", "net"],
                  ["tgw", "Transit Gateway", "net"], ["v", "The VPCs", "compute"]],
        "edges": [["dc", "dxg", "Direct Connect"], ["dxg", "tgw", "transit virtual interface"],
                  ["tgw", "v", "all of them, from the one line"]],
        "note": "A Direct Connect line cannot attach to a transit gateway by itself: the "
                "gateway in the middle and a transit virtual interface are the part being "
                "tested. One line then reaches every VPC on the hub instead of needing a "
                "connection each.",
    },
    {
        "id": "s3-express-onezone",
        "title": "The fastest bucket, in one zone",
        "when": ["S3"],
        "words": r"Express One Zone|directory bucket",
        "nodes": [["app", "Application in that zone", "compute"],
                  ["b", "Directory bucket, one zone", "store"]],
        "edges": [["app", "b", "very many small reads"]],
        "note": "This is the dearest storage and the quickest, not a cheap tier: the name "
                "sounds like One Zone-IA and means the opposite. Storage costs more and "
                "requests cost less, so it suits a great many small reads from compute in "
                "the same zone. Only one zone, so losing it loses the data.",
    },
    {
        "id": "cf-s3-waf",
        "title": "A private bucket served at the edge, with a firewall in front",
        "when": ["CloudFront", "S3", "WAF"],
        "words": r"web ACL|\bWAF\b",
        "unless_words": r"multiple origins|second origin|origin group|as origins",
        "nodes": [["u", "Users", "actor"], ["cf", "CloudFront, with a web ACL", "edge"],
                  ["s3", "Private bucket", "store"]],
        "edges": [["u", "cf", "every request"], ["s3", "cf", "read by OAC only"]],
        "note": "The web ACL is attached to the distribution, not a box in front of it: "
                "CloudFront checks each request against it at the edge, before any "
                "cache or origin read. The bucket stays private and only the "
                "distribution may read it.",
    },
    {
        "id": "cf-s3",
        "title": "A private bucket served at the edge",
        "when": ["CloudFront", "S3"],
        "words": r"distribution|cach|Origin Access|\bOAC\b|\bOAI\b|edge location",
        "unless_words": r"\bWAF\b|web ACL|multiple origins|second origin|origin group",
        "nodes": [["u", "Users", "actor"], ["cf", "CloudFront", "edge"],
                  ["s3", "S3 bucket", "store"]],
        "edges": [["u", "cf", "requests"], ["cf", "s3", "origin, read by OAC only"]],
        "note": "CloudFront holds a copy near the user. The bucket is never public: origin "
                "access control is what lets CloudFront, and only CloudFront, read it.",
    },
    {
        "id": "apigw-lambda-sqs",
        "title": "A queue between the front door and the work",
        "when": ["APIGW", "Lambda", "SQS"],
        "words": r"queue|\bSQS\b",
        "nodes": [["u", "Users", "actor"], ["api", "API Gateway", "edge"],
                  ["q", "SQS queue", "queue"], ["fn", "Lambda", "compute"]],
        "edges": [["u", "api", "requests"], ["api", "q", "accepts and returns"],
                  ["q", "fn", "polled"]],
        "note": "The front door answers at once and the work happens behind the queue, so a "
                "rush of requests queues up instead of being lost.",
    },
    {
        "id": "apigw-lambda",
        "title": "A front door with no servers behind it",
        "when": ["APIGW", "Lambda"],
        "words": r"API Gateway[\s\S]{0,120}(Lambda|function)|Lambda[\s\S]{0,120}API Gateway",
        "unless_words": r"\bSQS\b|queue",
        "nodes": [["u", "Users", "actor"], ["api", "API Gateway", "edge"],
                  ["fn", "Lambda", "compute"]],
        "edges": [["u", "api", "requests"], ["api", "fn", "invokes"]],
        "note": "No servers to size and nothing running between requests, so it suits "
                "traffic that comes and goes. Provisioned concurrency is the answer "
                "where the wait for a cold start matters. A function caps out at 15 "
                "minutes, which is what rules it out of longer jobs.",
    },
    {
        "id": "alb-asg-rds",
        "title": "The ordinary three tiers, spread across zones",
        "when": ["ALB", "ASG"],
        "words": r"Auto Scaling group",
        "unless_words": r"Fargate|\bECS\b|\bEKS\b|Service Auto Scaling|Application Auto Scaling",
        "nodes": [["u", "Users", "actor"], ["alb", "Application Load Balancer", "edge"],
                  ["asg", "Auto Scaling group of EC2", "compute"],
                  ["db", "Database", "store"]],
        "edges": [["u", "alb", ""], ["alb", "asg", "spreads the load"], ["asg", "db", "reads and writes"]],
        "note": "The load balancer is what makes losing an instance survivable; the Auto "
                "Scaling group is what makes losing one not matter.",
    },
    {
        "id": "alb-waf",
        "title": "A firewall in front of the load balancer",
        "when": ["ALB", "WAF"],
        "words": r"web ACL|\bWAF\b|rate|block",
        "nodes": [["u", "Users", "actor"], ["w", "AWS WAF", "edge"],
                  ["alb", "Application Load Balancer", "edge"],
                  ["app", "Application", "compute"]],
        "edges": [["u", "w", ""], ["w", "alb", "clean traffic"], ["alb", "app", ""]],
        "note": "WAF reads the request itself, so it can stop SQL injection and cross-site "
                "scripting, and rate-limit one address.",
    },
    {
        "id": "sqs-worker",
        "title": "A queue between a busy front end and the work",
        "when": ["SQS", "Lambda"],
        "words": r"\bSQS\b|queue",
        "unless_words": r"on-failure destination|dead-letter queue (for|with|as) [\s\S]{0,40}Lambda|Lambda[\s\S]{0,40}dead-letter",
        "nodes": [["app", "Front end", "compute"], ["q", "SQS queue", "queue"],
                  ["fn", "Lambda", "compute"], ["dlq", "Dead-letter queue", "queue"]],
        "edges": [["app", "q", "sends"], ["q", "fn", "polled"],
                  ["q", "dlq", "after repeated failure"]],
        "note": "The queue lets the front end answer at once and the workers catch up. "
                "After a few failed tries a message goes to the dead-letter queue. "
                "In a standard queue the rest carry on past it; in a FIFO queue it "
                "holds up its own message group until it is moved aside.",
    },
    {
        "id": "sqs-asg",
        "title": "Workers that grow with the queue",
        "when": ["SQS", "ASG"],
        "words": r"queue (depth|length|size)|number of messages|ApproximateNumberOfMessages|backlog per instance",
        "unless_words": r"Fargate|ECS service",
        "nodes": [["app", "Front end", "compute"], ["q", "SQS queue", "queue"],
                  ["asg", "Auto Scaling group", "compute"]],
        "edges": [["app", "q", "sends"], ["q", "asg", "polled"],
                  ["q", "asg", "queue depth drives scaling"]],
        "note": "Scaling on how deep the queue is, rather than on processor use, is what "
                "matches the number of workers to the work waiting.",
    },
    {
        "id": "sns-fanout",
        "title": "One message, several places",
        "when": ["SNS", "SQS"],
        "words": r"(topic|\bSNS\b)[\s\S]{0,200}(multiple|several|each|one .{0,24}for each|fan)|(multiple|several|each)[\s\S]{0,120}(subscrib|\bSQS\b queue)",
        "nodes": [["p", "Publisher", "compute"], ["t", "SNS topic", "queue"],
                  ["q1", "Queue A", "queue"], ["q2", "Queue B", "queue"]],
        "edges": [["p", "t", "publishes once"], ["t", "q1", "subscribes"], ["t", "q2", "subscribes"]],
        "note": "Each subscriber gets its own copy and its own queue, so a slow one never "
                "holds up the others. Filter policies decide who gets what.",
    },
    {
        "id": "s3-event-lambda",
        "title": "An upload sets work going",
        "when": ["S3", "Lambda"],
        "words": r"event notification|s3:ObjectCreated|object is (uploaded|created|added|put)|(uploaded|created|added) to the (bucket|S3)|S3 (PUT|upload) event",
        "unless_words": r"DynamoDB Stream|Object Lambda|\bKinesis\b|trust polic",
        "nodes": [["u", "Upload", "actor"], ["s3", "S3 bucket", "store"],
                  ["fn", "Lambda", "compute"], ["out", "Result", "store"]],
        "edges": [["u", "s3", "puts an object"], ["s3", "fn", "event notification"],
                  ["fn", "out", "writes"]],
        "note": "The bucket tells something to run when an object arrives. Events can go to "
                "Lambda, SQS, SNS or EventBridge, but not to a FIFO queue.",
    },
    {
        "id": "s3-vpce",
        "title": "Reaching a bucket without crossing the internet",
        "when": ["S3", "VPCe"],
        "words": r"gateway (VPC )?endpoint|VPC endpoint|route table",
        "unless_words": r"interface (VPC )?endpoint|PrivateLink|\bIPv6\b",
        "nodes": [["ec2", "Private subnet", "compute"], ["ep", "Gateway endpoint", "net"],
                  ["s3", "S3 bucket", "store"]],
        "edges": [["ec2", "ep", "route table entry"], ["ep", "s3", "stays on the AWS network"]],
        "note": "A gateway endpoint is a route, not a device, and costs nothing. It "
                "only works from inside the VPC and only over IPv4, so reaching a "
                "bucket from on premises, or over IPv6, needs the interface kind "
                "instead. The free gateway kind exists for S3 and DynamoDB alone.",
    },
    {
        "id": "s3-glacier-lifecycle",
        "title": "Objects moving to colder storage as they age",
        "when": ["S3", "Glacier"],
        "words": r"lifecycle (polic|rule|configuration)|S3 Lifecycle|transition",
        "unless_words": r"resource-based|lifecycle hook",
        "nodes": [["s3", "S3 Standard", "store"], ["ia", "Standard-IA", "store"],
                  ["g", "Glacier", "store"]],
        "edges": [["s3", "ia", "after 30 days"], ["ia", "g", "after 90 days"]],
        "note": "A lifecycle rule moves everything on the same schedule. Where some old "
                "objects stay popular, Intelligent-Tiering decides per object instead.",
    },
    {
        "id": "sgw-s3",
        "title": "A file share on your premises, backed by a bucket",
        "when": ["SGW", "S3"],
        "words": r"File Gateway|file share|\bNFS\b|\bSMB\b",
        "unless_words": r"Tape Gateway|virtual tape|\bVTL\b|Volume Gateway",
        "nodes": [["app", "On-premises application", "actor"],
                  ["gw", "S3 File Gateway", "net"], ["s3", "S3 bucket", "store"]],
        "edges": [["app", "gw", "NFS or SMB"], ["gw", "s3", "one file, one object"]],
        "note": "Each file becomes an object anything in AWS can read. A Volume Gateway would "
                "put a disk snapshot there instead, which nothing else can read as files.",
    },
    {
        "id": "athena-s3",
        "title": "Asking questions of what is already in the bucket",
        "when": ["Athena", "S3"],
        "words": r"Athena to (query|run|analy[sz]e|read)|quer(y|ies|ying) [\s\S]{0,60}Athena|Athena[\s\S]{0,40}quer",
        "unless_words": r"Lake Formation|\bEMR\b|Redshift Spectrum",
        "nodes": [["s3", "S3 bucket", "store"], ["a", "Athena", "compute"],
                  ["u", "Analyst", "actor"]],
        "edges": [["u", "a", "SQL"], ["a", "s3", "reads in place"]],
        "note": "Nothing is loaded anywhere first. Charged by data scanned, so Parquet, "
                "compression and partitions are what make it cheap.",
    },
    {
        "id": "kinesis-lambda",
        "title": "A stream of records, read as it arrives",
        "when": ["Kinesis", "Lambda"],
        "words": r"Kinesis Data Stream|\bshard|stream",
        "unless_words": r"Firehose",
        "nodes": [["src", "Producers", "actor"], ["k", "Kinesis Data Streams", "queue"],
                  ["fn", "Lambda", "compute"], ["s3", "Store", "store"]],
        "edges": [["src", "k", "put records"], ["k", "fn", "read in order, within a shard"],
                  ["fn", "s3", "writes"]],
        "note": "The stream keeps the records, so several applications can read the same ones "
                "and go back over them. A queue would hand each record to one reader and "
                "then forget it.",
    },
    {
        "id": "eventbridge-targets",
        "title": "Events routed on what is inside them",
        "when": ["EventBridge"],
        "words": r"EventBridge[\s\S]{0,160}(Lambda|\bSNS\b|notif)|(Lambda|\bSNS\b)[\s\S]{0,160}EventBridge",
        "unless_words": r"Fargate|\bBatch\b|ECS task|Step Functions|Run Command",
        "nodes": [["src", "Events", "actor"], ["eb", "EventBridge bus", "net"],
                  ["r", "Rule, matching the contents", "net"],
                  ["t", "Lambda, or a notification", "compute"]],
        "edges": [["src", "eb", "events arrive"], ["eb", "r", "checked against the rule"],
                  ["r", "t", "sent on when it matches"]],
        "note": "Rules read the body of the event, not just its type, and it can take events "
                "from outside software and run things on a schedule.",
    },
    {
        "id": "rds-multiaz",
        "title": "A database that survives losing a zone",
        "when": ["RDS", "MultiAZ"],
        "words": r"Multi-AZ|standby|automatic failover|fail(s)? over",
        "unless_words": r"Multi-AZ DB cluster|Aurora|read replica",
        "nodes": [["app", "Application", "compute"], ["p", "Primary, zone A", "store"],
                  ["s", "Standby, zone B", "store"]],
        "edges": [["app", "p", "one endpoint"], ["p", "s", "synchronous copy"]],
        "note": "In a Multi-AZ DB *instance* the standby serves no reads: it is there "
                "to take over, and the endpoint stays the same when it does. A "
                "Multi-AZ DB *cluster* is a different thing, with two standbys that "
                "do serve reads, as Aurora replicas do.",
    },
    {
        "id": "rds-read-replica",
        "title": "Reads taken off the main database",
        "when": ["RDS", "ReadReplica"],
        "words": r"read replica|reader endpoint",
        "unless_words": r"(replica|read replica) in (another|a different|a second) Region|cross-Region read replica",
        "nodes": [["app", "Application", "compute"], ["p", "Primary", "store"],
                  ["r", "Read replica", "store"]],
        "edges": [["app", "p", "writes"], ["app", "r", "reads"], ["p", "r", "asynchronous copy"]],
        "note": "Mainly for read load. A replica only helps with failure if you "
                "promote it, by hand; Multi-AZ is the one that fails over on its "
                "own. Aurora has one endpoint for writing and another that spreads "
                "reads across the replicas.",
    },
    {
        "id": "dynamodb-dax",
        "title": "A key-value store with a cache in front",
        "when": ["DAX"],
        "words": r"\bDAX\b",
        "nodes": [["app", "Application", "compute"], ["c", "DAX cluster", "store"],
                  ["t", "DynamoDB table", "store"]],
        "edges": [["app", "c", "reads"], ["c", "t", "fetches on a miss, and keeps it"]],
        "note": "DAX is the write-through cache built for DynamoDB and turns "
                "millisecond reads into microseconds. Unlike ElastiCache it does go "
                "to the table itself on a miss, so the application does not have to. "
                "The same calls, but it must use the DAX client and point at the "
                "cluster endpoint. Only eventually consistent reads come from the "
                "cache; a strongly consistent read goes to the table.",
    },
    {
        "id": "ecs-queue-db",
        "title": "Containers working through a queue",
        "when": ["ECS", "SQS"],
        "words": r"queue|\bSQS\b",
        "nodes": [["q", "SQS queue", "queue"], ["ecs", "ECS or Fargate tasks", "compute"],
                  ["db", "Database", "store"]],
        "edges": [["q", "ecs", "polled"], ["ecs", "db", "writes"]],
        "note": "Fargate means no instances to manage. Scaling on queue depth matches the "
                "number of tasks to the work waiting.",
    },
    {
        "id": "efs-shared",
        "title": "One file system, many instances",
        "when": ["EFS", "EC2"],
        "words": r"shared|share the|same file system|mount|\bNFS\b",
        "nodes": [["a", "EC2, zone A", "compute"], ["b", "EC2, zone B", "compute"],
                  ["efs", "EFS file system", "store"]],
        "edges": [["a", "efs", "NFS"], ["b", "efs", "NFS"]],
        "note": "Mounted by many instances at once, across zones. An EBS volume lives "
                "in a single zone, and even with Multi-Attach cannot cross zones or "
                "be safely shared by an ordinary file system.",
    },
    {
        "id": "s3-crr",
        "title": "Objects copied to a second bucket",
        "when": ["S3", "Replication"],
        "words": r"replicat",
        "nodes": [["a", "Source bucket", "store"],
                  ["b", "Destination bucket", "store"]],
        "edges": [["a", "b", "replication rule"]],
        "note": "Both buckets need versioning on. Objects already there are not copied "
                "until you run Batch Replication. Cross-Region is for distance and "
                "for surviving a Region; Same-Region is for keeping a second copy "
                "where the data is not allowed to leave.",
    },
    {
        "id": "dx-vpn-hybrid",
        "title": "Joining your own network to AWS",
        "when": ["DX"],
        "words": r"Direct Connect|Site-to-Site VPN|\bVPN\b",
        "unless_words": r"[Tt]ransit [Gg]ateway",
        "nodes": [["dc", "Your datacentre", "actor"], ["dx", "Direct Connect", "net"],
                  ["vpc", "VPC", "compute"]],
        "edges": [["dc", "dx", "private line"], ["dx", "vpc", "virtual interface"]],
        "note": "Steady bandwidth and steady latency, but weeks to put in. A Site-to-Site VPN "
                "is the one that can be working the same day.",
    },
    {
        "id": "tgw-hub",
        "title": "Many networks joined in one place",
        "when": ["TGW"],
        "words": r"[Tt]ransit [Gg]ateway",
        "nodes": [["v1", "VPC A", "compute"], ["v2", "VPC B", "compute"],
                  ["tgw", "Transit Gateway", "net"], ["dc", "On premises", "actor"]],
        "edges": [["v1", "tgw", ""], ["v2", "tgw", ""],
                  ["dc", "tgw", "VPN, or Direct Connect through a "
                                "Direct Connect gateway"]],
        "note": "VPC peering joins exactly two networks and does not pass traffic "
                "onwards, so a dozen VPCs would need dozens of links. One hub "
                "replaces them. A Direct Connect line reaches the hub through a "
                "Direct Connect gateway on a transit virtual interface, never "
                "straight onto it.",
    },
    {
        "id": "nat-egress",
        "title": "Private instances reaching out",
        "when": ["NAT"],
        "words": r"NAT gateway|NAT instance|outbound|egress|reach the internet",
        "nodes": [["ec2", "Private subnet", "compute"], ["nat", "NAT gateway", "net"],
                  ["igw", "Internet gateway", "net"], ["net", "Internet", "actor"]],
        "edges": [["ec2", "nat", "route to 0.0.0.0/0"], ["nat", "igw", ""], ["igw", "net", ""]],
        "note": "Traffic goes out and answers come back; nothing can start a connection "
                "inwards. One per zone, or losing a zone takes the others with it.",
    },
    {
        "id": "cognito-api",
        "title": "Signing in before the request is allowed through",
        "when": ["Cognito"],
        "words": r"user pool",
        "unless_words": r"identity pool",
        "nodes": [["u", "User", "actor"], ["up", "User pool", "net"],
                  ["api", "API Gateway, ALB or CloudFront", "edge"],
                  ["fn", "The application", "compute"]],
        "edges": [["u", "up", "signs in"], ["u", "api", "with the token"],
                  ["api", "fn", "once the token checks out"]],
        "note": "A user pool is sign-up and sign-in for your own users. An identity pool is "
                "the other one: it swaps a login for AWS credentials.",
    },
    {
        "id": "global-accelerator",
        "title": "Two fixed addresses, traffic sent to the nearest healthy Region",
        "when": ["GlobalAccelerator"],
        "words": r"Global Accelerator",
        "nodes": [["u", "Users", "actor"], ["ga", "Global Accelerator", "edge"],
                  ["r1", "Region A", "compute"], ["r2", "Region B", "compute"]],
        "edges": [["u", "ga", "two fixed addresses"], ["ga", "r1", "the nearest healthy endpoint"],
                  ["ga", "r2", "other endpoint groups, where there are any"]],
        "note": "Two addresses that never change, which is what allow-lists and "
                "hard-coded clients need, and it carries TCP and UDP rather than "
                "only web traffic. It helps with a single Region as well, because "
                "traffic joins the AWS network at the edge nearest the user. "
                "CloudFront caches; this does not.",
    },
    {
        "id": "snow-edge",
        "title": "Running where there is no connection",
        "when": ["Snow"],
        "words": r"disconnect|at sea|in transit|intermittent|"
            r"no (reliable )?(internet|connectivity)|Compute Optimized|Kubernetes|"
            r"run[a-z]* local|process[a-z]* local|process and store|"
            r"primary and secondary site",
        "unless_words": r"Storage Optimized|Tape Gateway",
        "nodes": [["site", "Ship, rig or site", "actor"],
                  ["snow", "Snowball Edge, compute optimised", "compute"],
                  ["aws", "AWS Region", "store"]],
        "edges": [["site", "snow", "collected or processed on site"],
                  ["snow", "aws", "shipped back, or synced when a connection returns"]],
        "note": "Compute Optimized is the one that runs work where there is no "
                "connection. Storage Optimized is for moving a lot of data once, "
                "and goes back by courier rather than over a line.",
    },
    {
        "id": "kms-envelope",
        "title": "Data encrypted with a key that is itself encrypted",
        "when": ["KMS"],
        "words": r"envelope|data key|customer managed key|\bCMK\b|rotat",
        "unless_words": r"external key store|client-side|multi-Region key|CloudHSM|Secrets Manager",
        "nodes": [["svc", "S3, EBS, RDS", "store"], ["dk", "Data key", "net"],
                  ["kms", "KMS key", "store"]],
        "edges": [["svc", "dk", "asks KMS for a data key"],
                  ["dk", "kms", "which is itself encrypted by"]],
        "note": "The key that encrypts your data is kept beside it, encrypted by a key "
                "whose material does not leave KMS. Rotation changes the outer key, "
                "so nothing has to be written again.",
    },
    {
        "id": "route53-failover",
        "title": "Sending people somewhere else when a Region is unwell",
        "when": ["Route53"],
        "words": r"failover (routing|polic|record|configuration)|fail(s)? over to|primary and secondary|health check[\s\S]{0,80}(Region|secondary|standby)",
        "unless_words": r"multivalue|weighted|latency-based|geolocation|geoproximity|"
                   r"CloudFront|Shield|import|hosted zones|active-active",
        "nodes": [["u", "Users", "actor"], ["r53", "Route 53", "edge"],
                  ["a", "Primary Region", "compute"], ["b", "Standby Region", "compute"]],
        "edges": [["u", "r53", "looks up the name"], ["r53", "a", "while healthy"],
                  ["r53", "b", "when the health check fails"]],
        "note": "Failover routing needs a health check to know. Latency routing sends each "
                "person to the quickest Region; geolocation sends them by where they are.",
    },
    {
        "id": "asg-across-zones",
        "title": "Instances replaced and spread across zones",
        "when": ["ASG", "EC2"],
        "words": r"Auto Scaling group",
        "unless_words": r"Aurora Auto Scaling|storage Auto Scaling|Application Auto Scaling|ECS Service Auto Scaling|DynamoDB auto scaling|Fargate|lifecycle hook",
        "nodes": [["asg", "Auto Scaling group", "compute"], ["a", "Zone A", "compute"],
                  ["b", "Zone B", "compute"]],
        "edges": [["asg", "a", "keeps the count up"], ["asg", "b", "keeps the count up"]],
        "note": "A launch template says what an instance is; the group says how many and "
                "where. Target tracking is the policy to reach for unless told otherwise.",
    },
    {
        "id": "ec2-rds",
        "title": "An application and its database, in separate subnets",
        "when": ["EC2", "RDS"],
        "words": r"private subnet|security group",
        "unless_words": r"Reserved Instance|Savings Plan|backup|\bAMI\b|"
                   r"IAM (database )?authentication|(another|different|second) [Rr]egion|"
                   r"US (East|West)|\bus-(east|west|central)-\d|across Regions",
        "nodes": [["app", "EC2, private subnet", "compute"], ["db", "RDS, private subnet", "store"]],
        "edges": [["app", "db", "security group to security group"]],
        "note": "The database security group allows the application's security group "
                "rather than an address range, which only works within one VPC, or "
                "a peered one in the same Region. Neither subnet needs a route to "
                "the internet.",
    },
    {
        "id": "ec2-s3-role",
        "title": "An instance reaching a bucket without any keys",
        "when": ["EC2", "S3"],
        "words": r"IAM role|instance profile|instance metadata|access key|long-term credential",
        "unless_words": r"FSx for Lustre|[Ll]ifecycle|Glacier|Savings Plan|Reserved Instance|\bAMI\b|Identity Center|VPC endpoint",
        "nodes": [["ec2", "EC2 instance", "compute"], ["role", "Instance role", "net"],
                  ["s3", "S3 bucket", "store"]],
        "edges": [["ec2", "role", "gets temporary credentials from"],
                  ["role", "s3", "allows the call"]],
        "note": "A role on the instance is the answer whenever a question mentions "
                "access keys sitting on an EC2 instance. Nothing is stored and the "
                "credentials rotate on their own. For a server outside AWS it is "
                "IAM Roles Anywhere instead.",
    },
    {
        "id": "ddb-stream-s3",
        "title": "Every change to a table, sent somewhere else",
        "when": ["DynamoDB"],
        "words": r"DynamoDB Stream",
        "unless_words": r"export|\bPITR\b|point-in-time",
        "nodes": [["d", "DynamoDB table", "store"], ["st", "DynamoDB Streams", "queue"],
                  ["fn", "Lambda", "compute"], ["s3", "S3 bucket", "store"]],
        "edges": [["d", "st", "every item change"], ["st", "fn", "reads in order"], ["fn", "s3", "writes"]],
        "note": "A stream carries every item change for 24 hours, and the before and "
                "after of it when set to do so. Time to live removes old items at "
                "no charge and the deletion shows up in the stream.",
    },
    {
        "id": "rds-snapshot-s3",
        "title": "A database copied somewhere it can be kept",
        "when": ["RDS"],
        "words": r"snapshot|automated backup|point-in-time|final snapshot",
        "unless_words": r"read replica",
        "nodes": [["db", "RDS instance", "store"], ["snap", "Snapshot", "store"],
                  ["copy", "Copy in another Region", "store"]],
        "edges": [["db", "snap", "automated, or taken by hand"],
                  ["snap", "copy", "copy snapshot"]],
        "note": "Automated backups go when the instance does; a snapshot taken by hand "
                "stays until deleted. Copying one to another Region is what "
                "survives losing this one. RDS holds snapshots itself: they do not "
                "land in a bucket of yours. Exporting one to S3 writes Parquet "
                "files for analysis, which cannot be restored as a database.",
    },
    {
        "id": "alb-route53",
        "title": "A name pointing at a load balancer",
        "when": ["ALB", "Route53"],
        "words": r"alias record|\balias\b|zone apex|\bapex\b|"
            r"point (the|a) (DNS|domain|record)|"
            r"[Rr]oute to the (ALB|load balancer)|"
            r"point[a-z]* (to|at) the (ALB|load balancer)",
        "unless_words": r"private hosted zone|internal (ALB|Application Load Balancer)|Shield|geolocation|geoproximity|latency-based|failover",
        "nodes": [["u", "Users", "actor"], ["r53", "Route 53", "edge"],
                  ["alb", "Load balancer", "edge"], ["app", "Targets", "compute"]],
        "edges": [["u", "r53", "looks up the name"], ["r53", "alb", "alias record"], ["alb", "app", ""]],
        "note": "An alias record points at an AWS resource, costs nothing to resolve, and can "
                "sit at the root of a domain where a CNAME cannot.",
    },
    {
        "id": "elasticache-reads",
        "title": "A cache in front of a database",
        "when": ["ElastiCache"],
        "words": r"cach",
        "unless_words": r"session (state|store|data)|user session|sticky session",
        "nodes": [["app", "Application", "compute"], ["c", "ElastiCache", "store"],
                  ["db", "Database", "store"]],
        "edges": [["app", "c", "looks here first"],
                  ["app", "db", "on a miss, asks the database"],
                  ["app", "c", "and puts the answer here"]],
        "note": "Redis keeps its data and can fail over; Memcached is plain and simply "
                "scales out. Nothing reads through on your behalf: the application "
                "misses, fetches, and writes the value in. Reads for the same thing "
                "over and over are what it is for.",
    },
    {
        "id": "redshift-s3",
        "title": "A warehouse loaded from, and reading, a bucket",
        "when": ["Redshift", "S3"],
        "words": r"COPY|Redshift Spectrum|external (table|schema)|\bunload\b",
        "unless_words": r"Athena|QuickSight|\bEMR\b",
        "nodes": [["s3", "S3 bucket", "store"], ["rs", "Redshift", "compute"],
                  ["u", "Reports", "actor"]],
        "edges": [["s3", "rs", "COPY, or Spectrum reads in place"], ["rs", "u", "queries"]],
        "note": "Redshift is for queries across a great deal of structured data. Spectrum "
                "reads straight from the bucket without loading it first.",
    },
    {
        "id": "ecs-efs",
        "title": "Containers sharing one file system",
        "when": ["ECS", "EFS"],
        "words": r"mount|shared|persist|same file system",
        "nodes": [["t1", "Task", "compute"], ["t2", "Task", "compute"],
                  ["efs", "EFS file system", "store"]],
        "edges": [["t1", "efs", "mounted"], ["t2", "efs", "mounted"]],
        "note": "A container's own storage goes when the task does. EFS is what keeps "
                "anything that has to outlive it, and lets tasks share it.",
    },
    {
        "id": "lambda-vpc-rds",
        "title": "A function reaching a private database",
        "when": ["Lambda", "RDS"],
        "words": r"RDS Proxy|proxy endpoint|too many connections|connection pool|exhaust[a-z]* the (database|connection)|overload the database",
        "unless_words": r"EventBridge",
        "nodes": [["fn", "Lambda in the VPC", "compute"], ["px", "RDS Proxy", "net"],
                  ["db", "RDS, private subnet", "store"]],
        "edges": [["fn", "px", "pooled connections"], ["px", "db", ""]],
        "note": "Many functions at once would open many connections and exhaust the database. "
                "The proxy holds a pool between them. A function in a VPC also loses its "
                "route to the internet unless a NAT gateway gives it one.",
    },
    {
        "id": "fsx-windows",
        "title": "A Windows file share, managed",
        "when": ["FSx"],
        "words": r"FSx for Windows|\bSMB\b|Active Directory|Windows file",
        "unless_words": r"Lustre|NetApp|ONTAP|OpenZFS",
        "nodes": [["u", "Windows machines", "actor"], ["ad", "Active Directory", "net"],
                  ["fsx", "FSx for Windows", "store"]],
        "edges": [["u", "fsx", "SMB"], ["fsx", "ad", "joined to the domain"]],
        "note": "FSx for Windows File Server is SMB and domain logins. There are three "
                "others: Lustre for speed in modelling and training, able to read "
                "from a bucket, plus NetApp ONTAP and OpenZFS.",
    },
    {
        "id": "s3-encrypt",
        "title": "Objects encrypted where they sit",
        "when": ["S3", "KMS"],
        "words": r"SSE-KMS|SSE-S3|encrypt",
        "unless_words": r"client-side|encryption client|SSE-C\b",
        "nodes": [["u", "Upload", "actor"], ["s3", "S3 bucket", "store"], ["k", "KMS key", "store"]],
        "edges": [["u", "s3", "puts an object"], ["s3", "k", "encrypts with a key from"]],
        "note": "SSE-S3 uses a key AWS manages. SSE-KMS uses one you control, so you "
                "can say who may use it and see every use in CloudTrail, which is "
                "what audit questions are after. An S3 Bucket Key holds one key per "
                "bucket so SSE-KMS stops calling KMS for every object, which is the "
                "answer whenever the cost of it comes up.",
    },
    {
        "id": "dms-migrate",
        "title": "Moving a database with the old one still running",
        "when": ["DMS"],
        "words": r"\bDMS\b|Database Migration",
        "nodes": [["src", "Source database", "store"], ["dms", "DMS", "compute"],
                  ["dst", "Target in AWS", "store"]],
        "edges": [["src", "dms", "full load, then changes"], ["dms", "dst", "writes"]],
        "note": "Change data capture keeps the two together until the moment you switch, so "
                "the old one stays in use throughout. Schema Conversion Tool is the one "
                "that comes first when the engines differ.",
    },
    {
        "id": "org-scp",
        "title": "A rule across every account",
        "when": ["SCP"],
        "words": r"service control polic|\bSCP\b",
        "unless_words": r"tag polic|backup polic|Control Tower|discount|cost allocation",
        "nodes": [["root", "Organization root", "net"], ["ou", "Organizational unit", "net"],
                  ["acc", "Member accounts", "compute"]],
        "edges": [["root", "ou", "service control policy"], ["ou", "acc", "applies to all below"]],
        "note": "A policy here sets the most anything in those accounts may do, including "
                "their administrators. It never grants anything, and it does not apply to "
                "the management account.",
    },
    {
        "id": "cw-alarm-action",
        "title": "A measurement that sets something off",
        "words": r"alarm|CloudWatch metric|custom metric",
        "nodes": [["src", "What is being watched", "compute"],
                  ["cw", "CloudWatch metric", "store"],
                  ["al", "Alarm", "net"], ["act", "Notify or scale", "compute"]],
        "edges": [["src", "cw", "sends the number"], ["cw", "al", "crosses the line"],
                  ["al", "act", "does something"]],
        "note": "Memory used and disk space left are not there until the agent is installed; "
                "processor use and network are. An alarm can notify, scale a group, or stop "
                "or restart an instance.",
    },
    {
        "id": "cloudtrail-audit",
        "title": "A record of who did what",
        "words": r"CloudTrail",
        "nodes": [["api", "API calls", "actor"], ["ct", "CloudTrail", "net"],
                  ["s3", "S3 bucket", "store"], ["cw", "CloudWatch Logs", "store"]],
        "edges": [["api", "ct", "recorded"], ["ct", "s3", "kept"], ["ct", "cw", "watched live"]],
        "note": "Management events are recorded by default. Data events, which are the "
                "ones about objects and items rather than settings, have to be "
                "switched on and are charged for. CloudTrail is who called what, "
                "CloudWatch is how things are performing, Config is what the "
                "settings were.",
    },
    {
        "id": "config-rules",
        "title": "Settings checked against the rules",
        "words": r"AWS Config|Config rule|conformance pack",
        "nodes": [["res", "Resources", "compute"], ["cfg", "AWS Config", "net"],
                  ["rule", "Rules", "net"], ["fix", "Report or put right", "compute"]],
        "edges": [["res", "cfg", "settings recorded"], ["cfg", "rule", "checked"],
                  ["rule", "fix", "when a rule is broken"]],
        "note": "It keeps the history of how a thing was set up, so it can answer what changed "
                "and when, and can put some things back on its own.",
    },
    {
        "id": "cross-account-role",
        "title": "Reaching into another account without a second login",
        "words": r"cross-account|cross account|(another|second|different|central|source|target|other|production|development|management|analytics|logging) (AWS )?account|AssumeRole|web identity federation",
        "unless_words": r"Managed Microsoft AD|\bMFA\b",
        "nodes": [["u", "User in account A", "actor"], ["role", "Role in account B", "net"],
                  ["res", "Resources in B", "store"]],
        "edges": [["u", "role", "assumes it"], ["role", "res", "temporary credentials"]],
        "note": "The role in B says who may assume it; the policy in A says its people may "
                "ask. No keys are copied anywhere, and the credentials expire on their own.",
    },
    {
        "id": "resource-policy",
        "title": "A rule attached to the thing itself",
        "words": r"bucket policy|resource-based polic|resource polic|key polic",
        "nodes": [["other", "Another account or service", "actor"],
                  ["pol", "Policy on the resource", "net"], ["res", "Bucket, queue or key", "store"]],
        "edges": [["other", "pol", "asks"], ["pol", "res", "allows or refuses"]],
        "note": "A policy on the resource says who may use it and must name who. An identity "
                "policy says what one person may do. Across accounts you need both ends.",
    },
    {
        "id": "interface-endpoint",
        "title": "Reaching a service privately from inside a VPC",
        "words": r"interface endpoint|PrivateLink",
        "unless_words": r"endpoint service",
        "nodes": [["ec2", "Private subnet", "compute"],
                  ["eni", "Interface endpoint", "net"], ["svc", "The service", "store"]],
        "edges": [["ec2", "eni", "a private address in your subnet"], ["eni", "svc", "never leaves AWS"]],
        "note": "An interface endpoint is a network card in your own subnet, and is charged "
                "by the hour and by the traffic. The free gateway kind exists only for S3 "
                "and DynamoDB.",
    },
    {
        "id": "lifecycle-tiers",
        "title": "Objects moved to cheaper storage as they age",
        "words": r"S3 Lifecycle|lifecycle (polic|rule|configuration)|Intelligent-Tiering|Standard-IA|One Zone-IA|transition[a-z]* (the )?(objects|data)",
        "unless_words": r"lifecycle hook|Express One Zone|directory bucket",
        "nodes": [["hot", "Standard", "store"], ["warm", "Infrequent access", "store"],
                  ["cold", "Archive", "store"]],
        "edges": [["hot", "warm", "after 30 days"], ["warm", "cold", "later"]],
        "note": "A rule goes by age alone and moves everything on the same day. Where some "
                "old objects stay popular, Intelligent-Tiering decides for each object "
                "instead and charges no retrieval fee.",
    },
    {
        "id": "backup-vault",
        "title": "Backups made and kept to a plan",
        "words": r"AWS Backup|backup plan|backup vault|Backup Vault Lock|Backup Audit Manager",
        "unless_words": r"Storage Gateway|cached volume",
        "nodes": [["res", "EBS, RDS, EFS, DynamoDB, S3, FSx", "store"],
                  ["plan", "Backup plan", "net"],
                  ["vault", "Vault, with a lock", "store"]],
        "edges": [["plan", "res", "on a schedule"], ["res", "vault", "copies kept"]],
        "note": "One plan across several services. A vault lock in compliance mode "
                "cannot be removed by anyone once its cooling-off period has "
                "passed, not an administrator and not AWS; governance mode can be "
                "lifted by someone holding the right permission. Regulator "
                "questions are asking for compliance mode.",
    },
    {
        "id": "cost-tools",
        "title": "Seeing and holding down what is being spent",
        "words": r"Cost Explorer|\bBudgets\b|Trusted Advisor|cost allocation tag",
        "unless_words": r"Data Exports|QuickSight|Athena|Cost and Usage Report",
        "nodes": [["use", "What is running", "compute"], ["ce", "Cost Explorer", "net"],
                  ["bud", "Budgets", "net"], ["who", "Warn, or block", "actor"]],
        "edges": [["use", "ce", "where the money went"], ["use", "bud", "watched against a limit"],
                  ["bud", "who", "warns, and can stop or deny"]],
        "note": "Cost Explorer looks back, Budgets looks forward. A budget action can "
                "do more than warn: it can attach a deny policy or stop instances "
                "when the limit is passed. Trusted Advisor points at waste. Tags "
                "are what let any of them answer by team or project.",
    },
    {
        "id": "ecs-roles",
        "title": "Two different roles on one container",
        "when": ["ECS"],
        "words": r"task role|execution role",
        "unless_words": r"Lambda",
        "nodes": [["task", "Task", "compute"], ["tr", "Task role", "net"],
                  ["er", "Execution role", "net"]],
        "edges": [["task", "tr", "what your code may call"],
                  ["task", "er", "what pulls the image and writes the logs"]],
        "note": "The execution role is for the agent that starts the container. The task role "
                "is for the code inside it. Mixing them up is the point of the question.",
    },
    {
        "id": "datasync-move",
        "title": "Moving files in, over the network",
        "words": r"DataSync|Transfer Family|\\bSFTP\\b",
        "nodes": [["src", "On premises, or in AWS", "actor"],
                  ["ag", "Agent, or an AWS endpoint", "net"],
                  ["dst", "S3, EFS or FSx", "store"]],
        "edges": [["src", "ag", "reads"], ["ag", "dst", "writes, and checks it arrived"]],
        "note": "DataSync is for moving a lot of files once or on a schedule. Transfer Family "
                "is for carrying on speaking SFTP to something that is now a bucket.",
    },
    {
        "id": "versioning-protection",
        "title": "Keeping what was there before",
        "words": r"versioning|MFA delete",
        "unless_words": r"versioning (is )?(disabled|turned off)|without versioning|not versioning-enabled|Storage Lens|Object Lock|\bWORM\b|compliance mode|governance mode",
        "nodes": [["u", "Writer", "actor"], ["b", "Bucket with versioning", "store"],
                  ["old", "Older versions", "store"]],
        "edges": [["u", "b", "overwrites or deletes"], ["b", "old", "the previous one is kept"]],
        "note": "A delete puts a marker on top; the object is still underneath. MFA "
                "delete guards removing a version for good.",
    },
    {
        "id": "sg-vs-nacl",
        "title": "Two places traffic is allowed or refused",
        "words": r"network ACL|\\bNACL\\b",
        "nodes": [["net", "Traffic", "actor"], ["nacl", "Network ACL, on the subnet", "net"],
                  ["sg", "Security group, on the instance", "net"], ["ec2", "Instance", "compute"]],
        "edges": [["net", "nacl", "allow and deny, in order"],
                  ["nacl", "sg", "allow only"], ["sg", "ec2", ""]],
        "note": "A security group remembers the conversation, so a reply is always allowed "
                "back. A network ACL does not, and is the only one of the two that can "
                "refuse a single address.",
    },
    {
        "id": "placement-groups",
        "title": "Where instances sit in relation to each other",
        "words": r"placement group",
        "nodes": [["c", "Cluster: packed, one zone", "compute"],
                  ["s", "Spread: apart, several zones", "compute"],
                  ["p", "Partition: in groups of racks", "compute"]],
        "edges": [],
        "note": "Cluster is for speed between them and is one zone, so it is wrong wherever "
                "losing a zone matters. Spread allows seven per zone. Partition suits "
                "systems that already cope with losing a part.",
    },
    {
        "id": "scaling-policy",
        "title": "What decides how many are running",
        "words": r"target tracking|step scaling|scheduled scaling|scaling polic|warm pool",
        "nodes": [["m", "A measurement", "store"], ["pol", "Scaling policy", "net"],
                  ["asg", "Auto Scaling group", "compute"]],
        "edges": [["m", "pol", "watched"], ["pol", "asg", "adds or removes"]],
        "note": "Target tracking keeps one number where you want it and is what to "
                "reach for. Scheduled is for a rush you can name the hour of. "
                "Predictive learns a pattern that repeats and starts things before "
                "it arrives. A warm pool is for instances that take too long to "
                "start.",
    },
    {
        "id": "read-scaling",
        "title": "Taking reads off the main database",
        "words": r"read replica|reader endpoint|read traffic",
        "nodes": [["app", "Application", "compute"], ["w", "Writer", "store"],
                  ["r", "Readers", "store"]],
        "edges": [["app", "w", "writes"], ["app", "r", "reads"], ["w", "r", "copied across"]],
        "note": "RDS read replicas are for read load, and only help with failure if "
                "you promote one. Aurora replicas and a Multi-AZ DB cluster's "
                "readers are different: they serve reads and double as failover "
                "targets.",
    },
    {
        "id": "sts-federation",
        "title": "Signing in with a directory you already have",
        "words": r"federat|\bSAML\b|Identity Center|Single Sign-On|\bSSO\b|Active Directory|Directory Service|\bLDAP\b",
        "unless_words": r"directory bucket|Express One Zone|WorkSpaces",
        "nodes": [["u", "Staff", "actor"], ["idp", "Your directory", "net"],
                  ["sts", "Temporary credentials", "net"], ["aws", "AWS accounts", "compute"]],
        "edges": [["u", "idp", "signs in once"], ["idp", "sts", "hands over a signed assertion"],
                  ["sts", "aws", "a role, for a while"]],
        "note": "Nobody gets a user of their own in each account. The answer whenever a "
                "question says people already have company logins and there are many "
                "accounts.",
    },
    {
        "id": "multi-region-dr",
        "title": "A second Region, ready to take over",
        "words": r"pilot light|warm standby|backup and restore|(multi|cross)[- ]Region (disaster recovery|\bDR\b)|global database|promote the (secondary|standby|replica)",
        "unless_words": r"multi-Region key|multi-Region secret|Multi-Region Access Point|\bKMS\b|Secrets Manager",
        "nodes": [["u", "Users", "actor"], ["r53", "Route 53", "edge"],
                  ["a", "Region A, live", "compute"], ["b", "Region B, waiting", "compute"]],
        "edges": [["u", "r53", ""], ["r53", "a", "while healthy"], ["a", "b", "data copied"],
                  ["r53", "b", "on failure"]],
        "note": "Backup and restore is cheapest and slowest. Pilot light keeps the data warm "
                "and the servers off. Warm standby runs a small copy. Active-active runs "
                "both and costs the most.",
    },
]


# Every picture must say, in words, what the answer has to be doing before it
# is shown. A review of all 62 against 531 answers found that the ones matched
# on service names alone were wrong between a fifth and all of the time, and
# the failure was always the same: an answer naming RDS and S3 for unrelated
# reasons got a disaster-recovery backup flow drawn over it. So the gate is
# checked here, at import, rather than trusted to whoever adds the next one.
_missing = [d["id"] for d in DIAGRAMS if not d.get("words")]
if _missing:
    raise AssertionError(
        "every diagram needs a 'words' phrase saying what the answer must be "
        "doing; these have none: " + ", ".join(_missing))

# A pattern written without the r prefix turns \b into a backspace character,
# which still compiles and still matches, just never against anything real. It
# has gone unnoticed here more than once, so it is checked rather than watched
# for: no pattern may hold a control character.
_bad = [d["id"] for d in DIAGRAMS
        if any(ord(c) < 32 for c in (d["words"] + (d.get("unless_words") or "")))]
if _bad:
    raise AssertionError(
        "a control character in a pattern, which means a missing r prefix on "
        "the string: " + ", ".join(_bad))

# Enough of an answer to be worth drawing. The phrase gates do the real work;
# this only skips a stub such as "B. None of these".
MIN_ANSWER = 20

_WORDS: dict[str, re.Pattern] = {}
_NOT_WORDS: dict[str, re.Pattern] = {}


def _rx(cache: dict, key: str, phrase: str) -> re.Pattern:
    rx = cache.get(key)
    if rx is None:
        rx = cache[key] = re.compile(phrase, re.I)
    return rx


def diagrams_for(answer_text: str, limit: int = 2) -> list[str]:
    """The pictures that fit this answer, most specific first."""
    text = answer_text or ""
    if len(text) < MIN_ANSWER:
        return []
    present = services_in(text)
    hits = []
    for d in DIAGRAMS:
        if not set(d.get("when", [])) <= present:
            continue
        if any(s in present for s in d.get("unless", [])):
            continue
        if not _rx(_WORDS, d["id"], d["words"]).search(text):
            continue
        no = d.get("unless_words")
        if no and _rx(_NOT_WORDS, d["id"], no).search(text):
            continue
        hits.append(d["id"])
        if len(hits) >= limit:
            break
    return hits

# --------------------------------------------------------------------------
# Which pictures can stand for what a question says they have already.
#
# A question's own words are not an answer: they describe a situation, often
# naming services for reasons that have nothing to do with the arrangement
# being asked about. So a picture is only allowed to play the "now" part when
# it draws something an organisation could actually have today and want to
# change. The rest are a rule, a practice or a control -- a policy across
# accounts, a role borrowed between them, an alarm, a mode of encryption --
# and showing one as a before leaves a pair that reads as nonsense: "now you
# have a cross-account role, you should have a resource policy".
# --------------------------------------------------------------------------
AS_IS = {
    "alb-asg-rds", "asg-across-zones", "ec2-rds", "cf-s3", "cf-s3-waf",
    "apigw-lambda", "apigw-lambda-sqs", "sqs-worker", "sqs-asg", "ecs-queue-db",
    "ecs-efs", "efs-shared", "fsx-windows", "fsx-lustre", "sgw-s3", "sgw-tape",
    "dx-vpn-hybrid", "tgw-hub", "dx-tgw", "nat-egress", "rds-multiaz",
    "rds-read-replica", "read-scaling", "rds-snapshot-s3",
    "rds-cross-region-replica", "elasticache-reads", "dynamodb-dax",
    "redshift-s3", "athena-s3", "s3-query-in-place", "lambda-vpc-rds",
    "s3-event-lambda", "kinesis-lambda", "ddb-stream-s3", "ddb-export-s3",
    "ddb-metadata-s3", "s3-crr", "s3-vpce", "s3-vpce-interface",
    "interface-endpoint", "snow-edge", "snowball-bulk", "lifecycle-tiers",
    "s3-glacier-lifecycle", "s3-express-onezone", "route53-failover",
    "route53-active-active", "global-accelerator", "alb-waf", "alb-route53",
    "eventbridge-targets", "sns-fanout", "multi-region-dr",
}

_unknown = AS_IS - {d["id"] for d in DIAGRAMS}
if _unknown:
    raise AssertionError("AS_IS names a picture that is not here: "
                         + ", ".join(sorted(_unknown)))


def as_is_for(question_text: str, after: list[str] | None = None) -> str | None:
    """The picture for what the question says they have now, if there is one.

    Left out when it is the same arrangement the answer proposes, because then
    there is no before and after to show -- only one picture, twice.
    """
    for did in diagrams_for(question_text, limit=3):
        if did in AS_IS and did not in (after or []):
            return did
    return None

# --------------------------------------------------------------------------
# A label has to fit the box it is drawn in.
#
# The app wraps a label onto at most two lines and then draws it, so anything
# that does not fit simply runs out past the edge of its box. Four did. This
# mirrors the app's wrapping so the next one is caught here instead of being
# noticed on a phone.
#
# Keep in step with wrapLabel and BOX_W in app.template.html.
# --------------------------------------------------------------------------
BOX_CHARS = 17          # what wrapLabel is given
LINE_LIMIT = 17         # what actually fits a 136-wide box at 13px


def _wrap(text: str, per: int = BOX_CHARS) -> list[str]:
    lines = [""]
    for word in str(text).split(" "):
        if not lines[-1]:
            lines[-1] = word
        elif len(lines[-1] + " " + word) <= per:
            lines[-1] = lines[-1] + " " + word
        else:
            lines.append(word)
    if len(lines) > 2:
        lines = [lines[0], " ".join(lines[1:])]
    return lines


_wide = [(d["id"], n[1], line)
         for d in DIAGRAMS for n in d["nodes"]
         for line in _wrap(n[1]) if len(line) > LINE_LIMIT]
if _wide:
    raise AssertionError(
        "these labels wrap to a line too long for the box, so the words would "
        "run out past its edge. Shorten them:" + "".join(
            f"{chr(10)}    {i}: {lab!r} -> {line!r} ({len(line)} characters)"
            for i, lab, line in _wide))
