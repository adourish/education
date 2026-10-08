#!/usr/bin/env python3
"""
The handful of choices the exam keeps asking you to make.

Six hundred questions are not six hundred decisions. They come back to about a
dozen: which storage class, where to run a container, how to decouple, which
load balancer. Twelve of them touch well over half the bank.

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