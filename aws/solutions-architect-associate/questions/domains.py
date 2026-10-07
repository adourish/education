#!/usr/bin/env python3
"""
Work out which of the four scored exam domains a question belongs to.

The exam is weighted by domain, not by service: secure 30%, resilient 26%,
high-performing 24%, cost-optimised 20%. Knowing a question's domain is what
lets practice be drawn in the same proportions the exam uses.

Two kinds of signal, counted differently:

  The steer.  Almost every question in this exam ends by saying what it is
  really asking: "MOST cost-effective", "MOST secure", "with the LEAST
  downtime". That phrase is the question telling you which domain it is scored
  against, so it counts for far more than anything else in the text.

  The subject matter.  Services and words that belong to one domain more than
  the others. Any single one of these is weak evidence on its own, because a
  question about encryption may really be about cost, so they are counted and
  the heaviest wins.

Used by build-bank.py when a question is first read, and by retag-domains.py to
re-apply the rules to questions already in the bank.
"""

from __future__ import annotations

import re

# What the exam guide weights each domain at. Practice drawn to this mix looks
# like the real paper rather than like whatever the question sets happen to
# hold.
EXAM_WEIGHTS = {
    "secure": 30,
    "resilient": 26,
    "high-performing": 24,
    "cost-optimized": 20,
}

DOMAIN_NAMES = {
    "secure": "Design secure architectures",
    "resilient": "Design resilient architectures",
    "high-performing": "Design high-performing architectures",
    "cost-optimized": "Design cost-optimized architectures",
    "unassigned": "Not yet placed in a domain",
}

# The question saying outright what it is asking for. Worth more than the rest
# of the text put together.
STEERS = [
    ("cost-optimized",
     r"most cost[- ]effective|least expensive|lowest[- ]cost|lowest possible cost|"
     r"least cost|most economical|cheapest|reduce (?:the )?(?:overall )?costs?|"
     r"minimi[sz]e (?:the )?(?:overall )?costs?|lower (?:the )?costs?|"
     r"save (?:the most )?money|cost savings|at the lowest|without increasing cost"),
    ("secure",
     r"most secure|most securely|securely|security requirements|"
     r"without exposing|not be publicly|keep .{0,20}private|"
     r"principle of least privilege|follows? security best practice"),
    ("resilient",
     r"highly available|high availability|highest availability|most resilient|"
     r"least (?:amount of )?downtime|minimi[sz]e downtime|no downtime|"
     r"without (?:any )?data loss|least data loss|meet (?:the|these) rto|"
     r"meet (?:the|these) rpo|continue to (?:operate|function)|survive"),
    ("high-performing",
     r"best performance|highest performance|improve .{0,20}performance|"
     r"lowest latency|reduce latency|most performant|fastest|"
     r"highest throughput|improve .{0,20}response time"),
]

# Subject matter that leans one way. Each distinct hit counts once.
SUBJECTS = [
    ("secure",
     r"\bIAM\b|\bKMS\b|encrypt|\bWAF\b|Shield|GuardDuty|Macie|Inspector|\bSCP\b|"
     r"Organizations|Secrets Manager|credential|least privilege|\bMFA\b|"
     r"authenticat|authoriz|private subnet|bucket policy|security group|"
     r"\bNACL\b|network ACL|certificate|\bTLS\b|\bSSL\b|Cognito|Directory Service|"
     r"\bSAML\b|federat|key rotation|audit|CloudTrail|compliance|PII\b|"
     r"sensitive data|access key|role|permission"),
    ("resilient",
     r"Multi-AZ|multiple Availability Zones|disaster recovery|\bRTO\b|\bRPO\b|"
     r"fault toler|failover|\bbackup\b|multi[- ]region|resilien|redundan|"
     r"outage|business continuity|durab|replicat|snapshot|restore|standby|"
     r"availability zone fail|pilot light|warm standby|health check|"
     r"automatically recover|self[- ]healing|99\.9"),
    ("high-performing",
     r"latency|performance|throughput|\bIOPS\b|\bcach|scal(?:e|ing|able)|"
     r"bottleneck|\bDAX\b|ElastiCache|read replica|CloudFront|Global Accelerator|"
     r"Provisioned IOPS|io1|io2|gp3|compute optimi|concurren|queue depth|"
     r"accelerat|edge location|burst"),
    ("cost-optimized",
     r"Savings Plan|\bSpot\b|Reserved Instance|\bRI\b|budget|cost|pricing|"
     r"charge|\bbill(?:ing|ed)?\b|expense|spend|free tier|On-Demand|"
     r"lifecycle polic|Intelligent-Tiering|Glacier|infrequent access|"
     r"right[- ]siz|idle|over[- ]provision|Cost Explorer|Trusted Advisor"),
]

_STEERS = [(name, re.compile(pat, re.I)) for name, pat in STEERS]
_SUBJECTS = [(name, re.compile(pat, re.I)) for name, pat in SUBJECTS]

# How much a steer outweighs a single piece of subject matter. Six means a
# question has to be heavily about one domain before it overrules what the
# question says it is asking for.
STEER_WEIGHT = 6


def domain(text: str) -> str:
    """The domain this question is scored against, or "unassigned"."""
    scores = {name: 0 for name in EXAM_WEIGHTS}

    for name, rx in _STEERS:
        if rx.search(text):
            scores[name] += STEER_WEIGHT

    for name, rx in _SUBJECTS:
        scores[name] += len({hit.lower() for hit in rx.findall(text)})

    best = max(scores, key=lambda k: scores[k])
    if scores[best] == 0:
        return "unassigned"

    # A tie helps nobody: if two domains come out level the question genuinely
    # sits between them, and guessing would quietly skew the practice mix.
    if list(scores.values()).count(scores[best]) > 1:
        return "unassigned"

    return best
