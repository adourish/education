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
    words:  a phrase that must appear in the answer, for the arrangements that
            are an idea rather than a set of services. Many answers name no
            service at all and are still about something worth drawing: an
            alarm that does something, a role borrowed across accounts.
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
        "id": "cf-s3-waf",
        "title": "A private bucket served at the edge, with a firewall in front",
        "when": ["CloudFront", "S3", "WAF"],
        "nodes": [["u", "Users", "actor"], ["w", "AWS WAF", "edge"],
                  ["cf", "CloudFront", "edge"], ["s3", "S3 bucket", "store"]],
        "edges": [["u", "w", ""], ["w", "cf", "clean traffic"],
                  ["cf", "s3", "origin, read by OAC only"]],
        "note": "The bucket stays private. Only CloudFront may read it, and the firewall sees "
                "every request before CloudFront does.",
    },
    {
        "id": "cf-s3",
        "title": "A private bucket served at the edge",
        "when": ["CloudFront", "S3"],
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
        "nodes": [["u", "Users", "actor"], ["api", "API Gateway", "edge"],
                  ["fn", "Lambda", "compute"]],
        "edges": [["u", "api", "requests"], ["api", "fn", "invokes"]],
        "note": "Nothing to keep running between requests, and nothing to patch.",
    },
    {
        "id": "alb-asg-rds",
        "title": "The ordinary three tiers, spread across zones",
        "when": ["ALB", "ASG"],
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
        "nodes": [["app", "Front end", "compute"], ["q", "SQS queue", "queue"],
                  ["fn", "Lambda", "compute"], ["dlq", "Dead-letter queue", "queue"]],
        "edges": [["app", "q", "sends"], ["q", "fn", "polled"],
                  ["q", "dlq", "after repeated failure"]],
        "note": "Nothing is lost when the workers fall behind, and one poisonous message ends "
                "up in the dead-letter queue instead of blocking the rest.",
    },
    {
        "id": "sqs-asg",
        "title": "Workers that grow with the queue",
        "when": ["SQS", "ASG"],
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
        "nodes": [["ec2", "Private subnet", "compute"], ["ep", "Gateway endpoint", "net"],
                  ["s3", "S3 bucket", "store"]],
        "edges": [["ec2", "ep", "route table entry"], ["ep", "s3", "stays on the AWS network"]],
        "note": "A gateway endpoint is free and serves S3 and DynamoDB. It also removes the "
                "NAT gateway charges that bucket traffic would otherwise run up.",
    },
    {
        "id": "s3-glacier-lifecycle",
        "title": "Objects moving to colder storage as they age",
        "when": ["S3", "Glacier"],
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
        "nodes": [["src", "Producers", "actor"], ["k", "Kinesis Data Streams", "queue"],
                  ["fn", "Lambda", "compute"], ["s3", "Store", "store"]],
        "edges": [["src", "k", "put records"], ["k", "fn", "reads in order"], ["fn", "s3", "writes"]],
        "note": "The stream keeps the records, so several applications can read the same ones "
                "and go back over them. A queue would hand each record to one reader and "
                "then forget it.",
    },
    {
        "id": "eventbridge-targets",
        "title": "Events routed on what is inside them",
        "when": ["EventBridge"],
        "nodes": [["src", "Event source", "actor"], ["eb", "EventBridge", "queue"],
                  ["fn", "Lambda", "compute"], ["sns", "SNS topic", "queue"]],
        "edges": [["src", "eb", "events"], ["eb", "fn", "rule matches"], ["eb", "sns", "rule matches"]],
        "note": "Rules read the body of the event, not just its type, and it can take events "
                "from outside software and run things on a schedule.",
    },
    {
        "id": "rds-multiaz",
        "title": "A database that survives losing a zone",
        "when": ["RDS", "MultiAZ"],
        "nodes": [["app", "Application", "compute"], ["p", "Primary, zone A", "store"],
                  ["s", "Standby, zone B", "store"]],
        "edges": [["app", "p", "one endpoint"], ["p", "s", "synchronous copy"]],
        "note": "The standby takes nothing from you and serves no reads. It exists to take "
                "over, and the endpoint stays the same when it does.",
    },
    {
        "id": "rds-read-replica",
        "title": "Reads taken off the main database",
        "when": ["RDS", "ReadReplica"],
        "nodes": [["app", "Application", "compute"], ["p", "Primary", "store"],
                  ["r", "Read replica", "store"]],
        "edges": [["app", "p", "writes"], ["app", "r", "reads"], ["p", "r", "asynchronous copy"]],
        "note": "For load, not for failure. The copy lags, so a read may be a moment behind.",
    },
    {
        "id": "dynamodb-dax",
        "title": "A key-value store with a cache in front",
        "when": ["DAX"],
        "nodes": [["app", "Application", "compute"], ["c", "Cache", "store"],
                  ["d", "DynamoDB", "store"]],
        "edges": [["app", "c", "reads"], ["c", "d", "on a miss"]],
        "note": "DAX is the one built for DynamoDB and turns milliseconds into microseconds "
                "without the application changing how it reads.",
    },
    {
        "id": "ecs-queue-db",
        "title": "Containers working through a queue",
        "when": ["ECS", "SQS"],
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
        "nodes": [["a", "EC2, zone A", "compute"], ["b", "EC2, zone B", "compute"],
                  ["efs", "EFS file system", "store"]],
        "edges": [["a", "efs", "NFS"], ["b", "efs", "NFS"]],
        "note": "Mounted by many instances at once, across zones. EBS can only be attached to "
                "one instance in one zone.",
    },
    {
        "id": "s3-crr",
        "title": "Objects copied to another Region",
        "when": ["S3", "Replication"],
        "nodes": [["a", "Bucket, Region A", "store"], ["b", "Bucket, Region B", "store"]],
        "edges": [["a", "b", "replication rule"]],
        "note": "Versioning has to be on in both buckets. It copies what arrives after the "
                "rule is made, not what is already there, unless a batch job is run.",
    },
    {
        "id": "dx-vpn-hybrid",
        "title": "Joining your own network to AWS",
        "when": ["DX"],
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
        "nodes": [["v1", "VPC A", "compute"], ["v2", "VPC B", "compute"],
                  ["tgw", "Transit Gateway", "net"], ["dc", "On premises", "actor"]],
        "edges": [["v1", "tgw", ""], ["v2", "tgw", ""], ["dc", "tgw", "VPN or Direct Connect"]],
        "note": "Peering joins two networks and does not pass traffic onwards. A transit "
                "gateway is what joins many without a connection between every pair.",
    },
    {
        "id": "nat-egress",
        "title": "Private instances reaching out",
        "when": ["NAT"],
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
        "nodes": [["u", "App users", "actor"], ["c", "Cognito user pool", "edge"],
                  ["api", "API Gateway", "edge"], ["fn", "Back end", "compute"]],
        "edges": [["u", "c", "signs in"], ["u", "api", "with the token"],
                  ["api", "fn", "once the token checks out"]],
        "note": "A user pool is sign-up and sign-in for your own users. An identity pool is "
                "the other one: it swaps a login for AWS credentials.",
    },
    {
        "id": "global-accelerator",
        "title": "Two fixed addresses, traffic sent to the nearest healthy Region",
        "when": ["GlobalAccelerator"],
        "nodes": [["u", "Users", "actor"], ["ga", "Global Accelerator", "edge"],
                  ["r1", "Region A", "compute"], ["r2", "Region B", "compute"]],
        "edges": [["u", "ga", "two anycast IPs"], ["ga", "r1", ""], ["ga", "r2", "if A is unwell"]],
        "note": "For TCP and UDP, and for a firewall that needs a fixed address to allow. "
                "CloudFront is the one that caches, and only for HTTP.",
    },
    {
        "id": "snow-edge",
        "title": "Running where there is no connection",
        "when": ["Snow"],
        "nodes": [["site", "Ship, rig or site", "actor"],
                  ["snow", "Snowball Edge, compute optimised", "compute"],
                  ["aws", "AWS Region", "store"]],
        "edges": [["site", "snow", "runs locally"], ["snow", "aws", "when a connection returns"]],
        "note": "The compute kind runs EC2 instances and Kubernetes on the device itself. More "
                "than one device side by side is how local users get high availability.",
    },
    {
        "id": "kms-envelope",
        "title": "Data encrypted with a key that is itself encrypted",
        "when": ["KMS"],
        "nodes": [["svc", "S3, EBS, RDS", "store"], ["dk", "Data key", "net"],
                  ["kms", "KMS key", "store"]],
        "edges": [["svc", "dk", "encrypts the data"], ["dk", "kms", "and is itself encrypted by"]],
        "note": "The key that encrypts your data is kept beside it, encrypted by a key that "
                "never leaves KMS. Rotation changes the outer key, so nothing has to be "
                "written again.",
    },
    {
        "id": "route53-failover",
        "title": "Sending people somewhere else when a Region is unwell",
        "when": ["Route53"],
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
        "when": ["ASG"],
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
        "nodes": [["app", "EC2, private subnet", "compute"], ["db", "RDS, private subnet", "store"]],
        "edges": [["app", "db", "security group to security group"]],
        "note": "The database security group allows the application's security group, not an "
                "address range. Neither subnet needs a route to the internet.",
    },
    {
        "id": "ec2-s3-role",
        "title": "An instance reaching a bucket without any keys",
        "when": ["EC2", "S3"],
        "nodes": [["ec2", "EC2 instance", "compute"], ["role", "Instance role", "net"],
                  ["s3", "S3 bucket", "store"]],
        "edges": [["ec2", "role", "temporary credentials"], ["role", "s3", "allows the call"]],
        "note": "A role attached to the instance is the answer whenever a question mentions "
                "access keys on a server. Nothing is stored, and the credentials rotate "
                "on their own.",
    },
    {
        "id": "ddb-stream-s3",
        "title": "Every change to a table, sent somewhere else",
        "when": ["DynamoDB", "S3"],
        "nodes": [["d", "DynamoDB table", "store"], ["st", "DynamoDB Streams", "queue"],
                  ["fn", "Lambda", "compute"], ["s3", "S3 bucket", "store"]],
        "edges": [["d", "st", "every item change"], ["st", "fn", "reads in order"], ["fn", "s3", "writes"]],
        "note": "Streams carry the before and after of every change for 24 hours. Time to "
                "live removes old items at no charge and shows the deletion in the stream.",
    },
    {
        "id": "rds-snapshot-s3",
        "title": "A database copied somewhere it can be kept",
        "when": ["RDS", "S3"],
        "nodes": [["db", "RDS instance", "store"], ["snap", "Snapshot", "store"],
                  ["s3", "S3, another Region", "store"]],
        "edges": [["db", "snap", "automated or on demand"], ["snap", "s3", "copied across"]],
        "note": "Automated snapshots go when the instance does; a snapshot taken by hand "
                "stays until deleted. Copying one to another Region is what survives losing "
                "this one.",
    },
    {
        "id": "alb-route53",
        "title": "A name pointing at a load balancer",
        "when": ["ALB", "Route53"],
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
        "nodes": [["app", "Application", "compute"], ["c", "ElastiCache", "store"],
                  ["db", "Database", "store"]],
        "edges": [["app", "c", "reads"], ["c", "db", "on a miss"], ["app", "db", "writes"]],
        "note": "Redis keeps its data and can fail over; Memcached is plain and simply "
                "scales out. Reads for the same thing over and over are what it is for.",
    },
    {
        "id": "redshift-s3",
        "title": "A warehouse loaded from, and reading, a bucket",
        "when": ["Redshift", "S3"],
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
        "nodes": [["u", "Windows machines", "actor"], ["ad", "Active Directory", "net"],
                  ["fsx", "FSx for Windows", "store"]],
        "edges": [["u", "fsx", "SMB"], ["fsx", "ad", "joined to the domain"]],
        "note": "FSx for Windows is SMB and domain logins. FSx for Lustre is the other one: "
                "speed for modelling and training, able to read from a bucket.",
    },
    {
        "id": "s3-encrypt",
        "title": "Objects encrypted where they sit",
        "when": ["S3", "KMS"],
        "nodes": [["u", "Upload", "actor"], ["s3", "S3 bucket", "store"], ["k", "KMS key", "store"]],
        "edges": [["u", "s3", "puts an object"], ["s3", "k", "encrypts with a key from"]],
        "note": "SSE-S3 uses a key AWS manages. SSE-KMS uses one you control, so you can say "
                "who may use it and see every use in CloudTrail, which is what audit "
                "questions are asking for.",
    },
    {
        "id": "dms-migrate",
        "title": "Moving a database with the old one still running",
        "when": ["DMS"],
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
        "words": "alarm|CloudWatch metric|custom metric",
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
        "words": "CloudTrail",
        "nodes": [["api", "Every API call", "actor"], ["ct", "CloudTrail", "net"],
                  ["s3", "S3 bucket", "store"], ["cw", "CloudWatch Logs", "store"]],
        "edges": [["api", "ct", "recorded"], ["ct", "s3", "kept"], ["ct", "cw", "watched live"]],
        "note": "CloudTrail is who called what and when. CloudWatch is how things are "
                "performing. Config is what the settings were and whether they are allowed.",
    },
    {
        "id": "config-rules",
        "title": "Settings checked against the rules",
        "words": "AWS Config|Config rule|conformance pack",
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
        "words": "cross-account|another account|assume|AssumeRole|trust polic",
        "nodes": [["u", "User in account A", "actor"], ["role", "Role in account B", "net"],
                  ["res", "Resources in B", "store"]],
        "edges": [["u", "role", "assumes it"], ["role", "res", "temporary credentials"]],
        "note": "The role in B says who may assume it; the policy in A says its people may "
                "ask. No keys are copied anywhere, and the credentials expire on their own.",
    },
    {
        "id": "resource-policy",
        "title": "A rule attached to the thing itself",
        "words": "bucket policy|resource-based polic|resource polic|key polic",
        "nodes": [["other", "Another account or service", "actor"],
                  ["pol", "Policy on the resource", "net"], ["res", "Bucket, queue or key", "store"]],
        "edges": [["other", "pol", "asks"], ["pol", "res", "allows or refuses"]],
        "note": "A policy on the resource says who may use it and must name who. An identity "
                "policy says what one person may do. Across accounts you need both ends.",
    },
    {
        "id": "interface-endpoint",
        "title": "Reaching a service privately from inside a VPC",
        "words": "interface endpoint|PrivateLink",
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
        "words": "lifecycle|Intelligent-Tiering|Standard-IA|One Zone",
        "nodes": [["hot", "S3 Standard", "store"], ["warm", "Infrequent access", "store"],
                  ["cold", "Archive", "store"]],
        "edges": [["hot", "warm", "after 30 days"], ["warm", "cold", "later"]],
        "note": "A rule goes by age alone and moves everything on the same day. Where some "
                "old objects stay popular, Intelligent-Tiering decides for each object "
                "instead and charges no retrieval fee.",
    },
    {
        "id": "backup-vault",
        "title": "Backups made and kept to a plan",
        "words": "AWS Backup|backup plan|backup vault|point-in-time",
        "nodes": [["res", "EBS, RDS, EFS, DynamoDB", "store"], ["plan", "Backup plan", "net"],
                  ["vault", "Vault, with a lock", "store"]],
        "edges": [["plan", "res", "on a schedule"], ["res", "vault", "copies kept"]],
        "note": "One plan across several services, and a vault lock nobody can delete from, "
                "including an administrator. That is what regulator questions are after.",
    },
    {
        "id": "cost-tools",
        "title": "Seeing and holding down what is being spent",
        "words": "Cost Explorer|Budgets|Cost and Usage|Trusted Advisor|cost allocation tag",
        "nodes": [["use", "What is running", "compute"], ["ce", "Cost Explorer", "net"],
                  ["bud", "Budgets", "net"], ["who", "An alert", "actor"]],
        "edges": [["use", "ce", "where the money went"], ["ce", "bud", "a limit set"],
                  ["bud", "who", "warns before it is passed"]],
        "note": "Cost Explorer looks back, Budgets looks forward and warns, Trusted Advisor "
                "points at waste. Tags are what let any of them answer by team or project.",
    },
    {
        "id": "ecs-roles",
        "title": "Two different roles on one container",
        "words": "task role|execution role|task definition",
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
        "words": "DataSync|Transfer Family|\\bSFTP\\b",
        "nodes": [["src", "On-premises storage", "actor"], ["ag", "Agent or endpoint", "net"],
                  ["dst", "S3, EFS or FSx", "store"]],
        "edges": [["src", "ag", "reads"], ["ag", "dst", "writes, and checks it arrived"]],
        "note": "DataSync is for moving a lot of files once or on a schedule. Transfer Family "
                "is for carrying on speaking SFTP to something that is now a bucket.",
    },
    {
        "id": "versioning-protection",
        "title": "Keeping what was there before",
        "words": "versioning|MFA delete|Object Lock",
        "nodes": [["u", "Writer", "actor"], ["b", "Bucket with versioning", "store"],
                  ["old", "Older versions", "store"]],
        "edges": [["u", "b", "overwrites or deletes"], ["b", "old", "the previous one is kept"]],
        "note": "A delete puts a marker on top; the object is still underneath. MFA delete "
                "guards removing a version for good, and Object Lock stops anyone at all, "
                "for a stated time.",
    },
    {
        "id": "sg-vs-nacl",
        "title": "Two places traffic is allowed or refused",
        "words": "network ACL|\\bNACL\\b",
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
        "words": "placement group",
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
        "words": "target tracking|step scaling|scheduled scaling|scaling polic|warm pool",
        "nodes": [["m", "A measurement", "store"], ["pol", "Scaling policy", "net"],
                  ["asg", "Auto Scaling group", "compute"]],
        "edges": [["m", "pol", "watched"], ["pol", "asg", "adds or removes"]],
        "note": "Target tracking keeps one number where you want it and is what to reach for. "
                "Scheduled is for a rush you can predict. A warm pool is for instances that "
                "take too long to start.",
    },
    {
        "id": "read-scaling",
        "title": "Taking reads off the main database",
        "words": "read replica|reader endpoint|read traffic",
        "nodes": [["app", "Application", "compute"], ["w", "Writer", "store"],
                  ["r", "Readers", "store"]],
        "edges": [["app", "w", "writes"], ["app", "r", "reads"], ["w", "r", "copied across"]],
        "note": "For load, not for failure. Aurora has one endpoint for writing and another "
                "that spreads reads across the replicas.",
    },
    {
        "id": "sts-federation",
        "title": "Signing in with a directory you already have",
        "words": "federat|\\bSAML\\b|Identity Center|Single Sign-On|directory",
        "nodes": [["u", "Staff", "actor"], ["idp", "Your directory", "net"],
                  ["sts", "Temporary credentials", "net"], ["aws", "AWS accounts", "compute"]],
        "edges": [["u", "idp", "signs in once"], ["idp", "sts", "vouches for them"],
                  ["sts", "aws", "a role, for a while"]],
        "note": "Nobody gets a user of their own in each account. The answer whenever a "
                "question says people already have company logins and there are many "
                "accounts.",
    },
    {
        "id": "multi-region-dr",
        "title": "A second Region, ready to take over",
        "words": "multi-Region|another Region|second Region|pilot light|warm standby|\\bRTO\\b|\\bRPO\\b",
        "nodes": [["u", "Users", "actor"], ["r53", "Route 53", "edge"],
                  ["a", "Region A, live", "compute"], ["b", "Region B, waiting", "compute"]],
        "edges": [["u", "r53", ""], ["r53", "a", "while healthy"], ["a", "b", "data copied"],
                  ["r53", "b", "on failure"]],
        "note": "Backup and restore is cheapest and slowest. Pilot light keeps the data warm "
                "and the servers off. Warm standby runs a small copy. Active-active runs "
                "both and costs the most.",
    },
]


_WORDS = {}


def diagrams_for(answer_text: str, limit: int = 2) -> list[str]:
    """The pictures that fit this answer, most specific first."""
    present = services_in(answer_text)
    hits = []
    for d in DIAGRAMS:
        if not set(d.get("when", [])) <= present:
            continue
        if any(s in present for s in d.get("unless", [])):
            continue
        phrase = d.get("words")
        if phrase:
            if len(answer_text or "") < 70:
                continue
            rx = _WORDS.get(d["id"])
            if rx is None:
                rx = _WORDS[d["id"]] = re.compile(phrase, re.I)
            if not rx.search(answer_text or ""):
                continue
        hits.append(d["id"])
        if len(hits) >= limit:
            break
    return hits
