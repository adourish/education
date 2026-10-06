#!/usr/bin/env python3
"""
Work out which concepts actually get asked, by counting them in the question bank.

The point is to replace opinion ("this is high-yield") with a count. Every yield
mark on the poster and in the notes should trace back to a number this script
produced, so it can be re-checked whenever new questions are added.

Writes yield-report.md and yield.json.

Usage:
    python yield-report.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent

# A concept is a thing the exam can ask about, and the pattern is every way the
# question text might refer to it. Keep patterns tight: counting "S3" would tell
# us nothing, because S3 appears as set dressing in questions about other things.
CONCEPTS: dict[str, str] = {
    # --- storage
    "S3 storage classes / lifecycle": r"S3 Standard-IA|One Zone-IA|Intelligent-Tiering|Glacier|storage class|lifecycle (polic|rule|config)",
    "S3 encryption (SSE-S3/KMS/C)": r"SSE-S3|SSE-KMS|SSE-C|server-side encryption",
    "S3 versioning / Object Lock / MFA Delete": r"versioning|Object Lock|MFA Delete",
    "S3 replication (CRR/SRR)": r"Cross-Region Replication|\bCRR\b|Same-Region Replication|\bSRR\b|replicat\w+ .{0,20}bucket",
    "S3 presigned URL": r"presigned|pre-signed",
    "S3 Transfer Acceleration": r"Transfer Acceleration",
    "EBS volume types / IOPS": r"\bgp2\b|\bgp3\b|\bio1\b|\bio2\b|\bst1\b|\bsc1\b|Provisioned IOPS",
    "EBS snapshots": r"EBS snapshot|snapshot .{0,25}volume|create-snapshot",
    "EFS": r"\bEFS\b|Elastic File System",
    "FSx (Windows / Lustre)": r"\bFSx\b",
    "Storage Gateway": r"Storage Gateway|File Gateway|Volume Gateway|Tape Gateway",
    "Snow family": r"Snowball|Snowcone|Snowmobile",
    "DataSync": r"DataSync",
    # --- compute
    "EC2 purchasing (Spot/RI/Savings Plans)": r"\bSpot\b|Reserved Instance|Savings Plan|On-Demand|Dedicated Host",
    "Auto Scaling": r"Auto Scaling|scaling polic|launch template|launch configuration",
    "Placement groups": r"placement group",
    "Lambda": r"\bLambda\b",
    "Containers (ECS/EKS/Fargate)": r"\bECS\b|\bEKS\b|Fargate|Elastic Container",
    "Elastic Beanstalk": r"Elastic Beanstalk",
    # --- load balancing / dns / edge
    "ALB vs NLB": r"Application Load Balancer|Network Load Balancer|\bALB\b|\bNLB\b",
    "CloudFront": r"CloudFront",
    "Route 53 routing policies": r"Route ?53|latency.based routing|failover routing|weighted routing|geolocation routing",
    "Global Accelerator": r"Global Accelerator",
    # --- networking
    "VPC security groups vs NACLs": r"security group|network ACL|\bNACL\b",
    "NAT gateway": r"NAT gateway|NAT instance",
    "VPC endpoints / PrivateLink": r"VPC endpoint|PrivateLink|gateway endpoint|interface endpoint",
    "VPC peering / Transit Gateway": r"VPC peering|Transit Gateway",
    "Direct Connect / Site-to-Site VPN": r"Direct Connect|Site-to-Site VPN|virtual private gateway|customer gateway",
    "VPC Flow Logs": r"Flow Logs",
    # --- databases
    "RDS Multi-AZ": r"Multi-AZ",
    "RDS read replicas": r"read replica",
    "Aurora": r"Aurora",
    "DynamoDB": r"DynamoDB",
    "DynamoDB DAX": r"\bDAX\b",
    "DynamoDB Global Tables": r"Global Table",
    "ElastiCache (Redis/Memcached)": r"ElastiCache|Memcached|\bRedis\b",
    "Redshift": r"Redshift",
    "DMS / SCT migration": r"\bDMS\b|Database Migration Service|Schema Conversion",
    # --- integration
    "SQS": r"\bSQS\b|Simple Queue Service|\bFIFO\b|dead-letter|visibility timeout",
    "SQS visibility timeout / DLQ": r"visibility timeout|dead-letter|dead letter",
    "SNS": r"\bSNS\b|Simple Notification Service",
    "EventBridge": r"EventBridge|CloudWatch Events",
    "Step Functions": r"Step Functions",
    "Kinesis": r"Kinesis",
    "API Gateway": r"API Gateway",
    # --- security
    "IAM roles vs users / instance profile": r"IAM role|instance profile|IAM user",
    "IAM policies / least privilege": r"IAM polic|bucket policy|resource-based polic|least privilege",
    "Cross-account access / STS": r"AssumeRole|\bSTS\b|cross-account",
    "KMS / encryption keys": r"\bKMS\b|customer master key|\bCMK\b|envelope encryption",
    "CloudHSM": r"CloudHSM",
    "Secrets Manager / Parameter Store": r"Secrets Manager|Parameter Store",
    "Cognito": r"Cognito",
    "AWS WAF": r"\bWAF\b",
    "Shield / DDoS": r"\bShield\b|\bDDoS\b",
    "GuardDuty / Inspector / Macie": r"GuardDuty|Inspector|Macie",
    "Organizations / SCPs": r"Organizations|\bSCP\b|service control polic",
    "Directory Service / AD": r"Directory Service|Active Directory|\bAD\b connector",
    # --- ops
    "CloudWatch metrics / alarms": r"CloudWatch",
    "CloudTrail": r"CloudTrail",
    "AWS Config": r"AWS Config",
    "CloudFormation": r"CloudFormation",
    "Systems Manager / Session Manager": r"Systems Manager|Session Manager|\bSSM\b",
    "Trusted Advisor": r"Trusted Advisor",
    "Cost Explorer / Budgets": r"Cost Explorer|AWS Budgets|Cost and Usage",
    # --- analytics
    "Athena": r"\bAthena\b",
    "Glue": r"\bGlue\b",
    "EMR": r"\bEMR\b",
    "OpenSearch / Elasticsearch": r"OpenSearch|Elasticsearch",
    "QuickSight": r"QuickSight",
}

TIERS = [(3, "very likely"), (2, "likely"), (1, "possible")]


def main() -> None:
    bank = json.loads((HERE / "bank.json").read_text(encoding="utf-8"))
    total = len(bank)

    # Match on question + answer. The explanation is excluded on purpose: it is
    # the author's commentary and name-drops services the question never asked about.
    texts = [f"{r['question']}\n{r['answer']}" for r in bank]

    counts: dict[str, int] = {}
    for concept, pattern in CONCEPTS.items():
        rx = re.compile(pattern, re.I)
        counts[concept] = sum(1 for t in texts if rx.search(t))

    ranked = sorted(counts.items(), key=lambda kv: -kv[1])
    hits = [c for _, c in ranked if c > 0]

    # Tier by position in the ranking, not by raw count, so the tiers stay
    # meaningful as the bank grows.
    n = len(hits)
    cut3 = hits[min(int(n * 0.20), n - 1)] if n else 0
    cut2 = hits[min(int(n * 0.50), n - 1)] if n else 0

    def tier(c: int) -> int:
        if c >= cut3:
            return 3
        if c >= cut2:
            return 2
        return 1 if c else 0

    out = [{"concept": k, "count": v, "pct": round(100 * v / total, 1), "tier": tier(v)}
           for k, v in ranked]
    (HERE / "yield.json").write_text(json.dumps(out, indent=1), encoding="utf-8")

    lines = [
        "# What actually gets asked",
        "",
        f"Counted across **{total} questions** in the bank. A concept is counted once per",
        "question, matching on the question stem and the correct answer only — the",
        "explanations are excluded because they name services the question never asked about.",
        "",
        "These counts are what the yield marks on the poster and in the notes are based on.",
        "Re-run `yield-report.py` after adding sources and the tiers move with the data.",
        "",
        "| Tier | Meaning | Mark |",
        "|---|---|---|",
        "| 3 | Top 20% by frequency — **expect this on the day** | `▰▰▰` |",
        "| 2 | Next 30% — likely | `▰▰▱` |",
        "| 1 | Appears, but thinly | `▰▱▱` |",
        "| 0 | Not in the bank — still in the exam guide, so do not skip it | — |",
        "",
        "---",
        "",
        "| Concept | Questions | Share | Tier |",
        "|---|---:|---:|:--:|",
    ]
    marks = {3: "`▰▰▰`", 2: "`▰▰▱`", 1: "`▰▱▱`", 0: "—"}
    for row in out:
        lines.append(
            f"| {row['concept']} | {row['count']} | {row['pct']}% | {marks[row['tier']]} |"
        )

    zero = [r["concept"] for r in out if r["count"] == 0]
    if zero:
        lines += [
            "",
            "## Nothing in the bank for these",
            "",
            "They are on the exam guide's in-scope list, so this says the question bank is",
            "thin there, not that the exam is. Treat it as a gap to fill, not a topic to drop.",
            "",
        ] + [f"- {c}" for c in zero]

    (HERE / "yield-report.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"{total} questions analysed, {len(CONCEPTS)} concepts")
    print(f"tier cutoffs: tier3 >= {cut3} questions, tier2 >= {cut2}\n")
    print("Top 30:")
    ascii_marks = {3: "***", 2: "** ", 1: "*  ", 0: "   "}
    for row in out[:30]:
        print(f"  {ascii_marks[row['tier']]} {row['count']:4}  {row['pct']:5.1f}%  {row['concept']}")


if __name__ == "__main__":
    main()
