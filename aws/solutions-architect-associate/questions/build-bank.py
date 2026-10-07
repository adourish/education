#!/usr/bin/env python3
"""
Build a categorized question bank for the AWS SAA-C03 exam.

Reads every raw source file in sources/, parses it into question records, tags
each record with a topic area, and writes:

    bank.json          every record, machine readable
    bank/<area>.md     one markdown drill file per topic area
    bank/README.md     counts and coverage

Each source format gets its own parser function registered in PARSERS, keyed by
the filename suffix, so adding a new source means adding one function.

Usage:
    python build-bank.py
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
SOURCES = HERE / "sources"
BANK = HERE / "bank"
CORRECTIONS = HERE / "corrections.json"
AUDIT_DROP = HERE / "audit-drop.json"

# Sources whose questions carry a star: a human has checked them, so they are
# worth more than a scraped set. Also sources that must never be published,
# because the file they came from is a watermarked paid product.
REVIEWED_SOURCES = {"certempire"}

# Every source needs its own id prefix. Two sources parsed by the same function
# both numbered from 1, so 327 ids collided and 260 questions in the bank shared
# an id with a different question. A correction aimed at one then landed on the
# other.
ID_PREFIX = {
    "certempire": "ce",
    "saa-c03-optioned": "et",
    "ditectrev-saa-c03": "dt",
    "iamrushabhshahh-saa-c03": "gh",
    "whizlabs-25": "wl",
}


# Who actually published a set. Two of the source files come from one GitHub
# repository - its text dump and its PDF - so a question in both is the same
# question from one publisher, not two independent sets agreeing. Counting
# files rather than publishers would have called 381 questions corroborated
# when they are nothing of the sort.
ORIGIN = {
    "iamrushabhshahh-saa-c03": "iamrushabhshahh",
    "saa-c03-optioned": "iamrushabhshahh",
    "certempire": "certempire",
    "ditectrev-saa-c03": "ditectrev",
    "whizlabs-25": "whizlabs",
}


def origin_of(source: str) -> str:
    return ORIGIN.get(source, source)


def prefix_for(source: str) -> str:
    return ID_PREFIX.get(source, re.sub(r"[^a-z0-9]", "", source.lower())[:3] or "x")
PRIVATE_SOURCES: set[str] = set()   # nothing is held back from the build

# --------------------------------------------------------------------------
# Topic areas. Each is a list of (weight, regex). Highest total score wins.
# Weights let a decisive term ("DynamoDB") beat an incidental one ("bucket").
# --------------------------------------------------------------------------

AREAS: dict[str, list[tuple[int, str]]] = {
    "compute": [
        (3, r"\bEC2\b|\bLambda\b|\bFargate\b|\bECS\b|\bEKS\b|Elastic Beanstalk|\bAMI\b|AWS Batch"),
        (3, r"Auto Scaling|launch template|launch configuration|placement group"),
        (2, r"\bSpot\b|Reserved Instance|Dedicated Host|instance type|instance store"),
        (1, r"\bcontainer|serverless function|compute"),
    ],
    "storage": [
        (3, r"\bS3\b|Glacier|\bEBS\b|\bEFS\b|\bFSx\b|Storage Gateway|Snowball|Snowcone|Snowmobile"),
        (3, r"DataSync|Transfer Family|AWS Backup|lifecycle polic|storage class"),
        (2, r"\bbucket\b|object storage|file system|volume|snapshot|archive"),
        (1, r"durabilit|Intelligent-Tiering|One Zone"),
    ],
    "database": [
        (3, r"\bRDS\b|Aurora|DynamoDB|ElastiCache|Redshift|DocumentDB|Neptune|Keyspaces|QLDB|Timestream|MemoryDB"),
        (3, r"read replica|Multi-AZ|\bDAX\b|Global Table|\bDMS\b|Schema Conversion"),
        (2, r"\bdatabase\b|\bMySQL\b|PostgreSQL|Oracle|SQL Server|MongoDB|Cassandra"),
        (1, r"\bRCU\b|\bWCU\b|partition key|sort key"),
    ],
    "networking": [
        (3, r"\bVPC\b|subnet|security group|network ACL|\bNACL\b|NAT gateway|internet gateway"),
        (3, r"Route 53|Route53|CloudFront|Direct Connect|Transit Gateway|PrivateLink|VPC endpoint|Global Accelerator"),
        (3, r"Site-to-Site VPN|Client VPN|VPC peering|Flow Logs|\bCIDR\b"),
        (2, r"load balancer|\bALB\b|\bNLB\b|\bELB\b|target group|\bDNS\b|latency routing|failover routing"),
        (1, r"\bIPv6\b|elastic IP|\bENI\b|bastion"),
    ],
    "security": [
        (3, r"\bIAM\b|\bKMS\b|CloudHSM|Secrets Manager|\bWAF\b|Shield|GuardDuty|Macie|Inspector|Security Hub|Detective"),
        (3, r"\bSCP\b|Organizations|Control Tower|permission boundar|Identity Center|\bCognito\b|\bSTS\b|AssumeRole"),
        (3, r"\bACM\b|certificate manager|Firewall Manager|Network Firewall|Directory Service"),
        (2, r"encrypt|\brole\b|\bpolicy\b|credential|authenticat|authoriz|least privilege|\bMFA\b"),
        (1, r"compliance|audit|\bPII\b"),
    ],
    "integration": [
        (3, r"\bSQS\b|\bSNS\b|EventBridge|Step Functions|Amazon MQ|Kinesis|\bMSK\b|AppSync|AppFlow"),
        (3, r"API Gateway|dead-letter|visibility timeout|\bFIFO\b|fan-out|fanout"),
        (2, r"\bqueue\b|\btopic\b|decoupl|message|event-driven|\bstream\b"),
    ],
    "analytics": [
        (3, r"\bAthena\b|\bGlue\b|\bEMR\b|QuickSight|OpenSearch|Lake Formation|Data Pipeline|Data Exchange|Kendra"),
        (2, r"data lake|\bETL\b|data warehouse|\bParquet\b|business intelligence|\bHadoop\b|\bSpark\b"),
    ],
    "monitoring": [
        (3, r"CloudWatch|CloudTrail|AWS Config\b|CloudFormation|Systems Manager|\bSSM\b|Session Manager|OpsWorks"),
        (3, r"Service Catalog|\bStackSet|X-Ray|Health Dashboard|Trusted Advisor|Managed Grafana|Prometheus"),
        (2, r"\balarm\b|\bmetric\b|\blog\b|\bmonitor|\baudit trail|drift|runbook|patch"),
    ],
    "cost": [
        (3, r"Savings Plan|Cost Explorer|AWS Budgets|Cost and Usage|Compute Optimizer|Cost Anomaly|License Manager"),
        (3, r"MOST cost-effective|LEAST expensive|lowest cost|reduce cost|minimize cost"),
        (2, r"cost-effective|cost optimiz|pricing|\bbilling\b"),
    ],
    "resilience": [
        (3, r"disaster recovery|\bRTO\b|\bRPO\b|pilot light|warm standby|active-active|multi-region"),
        (3, r"high availability|highly available|fault toler|business continuity"),
        (2, r"\bfailover\b|\bbackup\b|\brestore\b|\bresilien|\bredundan"),
    ],
}

AREA_TITLES = {
    "compute": "Compute — EC2, Lambda, containers, scaling",
    "storage": "Storage — S3, EBS, EFS, FSx, archive, transfer",
    "database": "Databases — RDS, Aurora, DynamoDB, caching, warehousing",
    "networking": "Networking — VPC, load balancing, DNS, edge, hybrid",
    "security": "Security and identity — IAM, encryption, protection, governance",
    "integration": "Application integration — queues, topics, events, streams, APIs",
    "analytics": "Analytics — query, ETL, big data, search, BI",
    "monitoring": "Monitoring and management — observability, IaC, operations",
    "cost": "Cost optimization",
    "resilience": "Resilience and disaster recovery",
    "unclassified": "Unclassified — review and tag by hand",
}

# Phrases that reveal what the question is really optimising for.
QUALIFIERS = [
    ("cost", r"MOST cost-effective|LEAST expensive|lowest cost|most cost effective"),
    ("least-ops", r"LEAST operational overhead|LEAST amount of operational|minimal operational|LEAST management overhead"),
    ("performance", r"LOWEST latency|BEST performance|highest performance|improve performance"),
    ("availability", r"highly available|high availability|MOST resilient|fault tolerant"),
    ("security", r"MOST secure|securely|MOST restrictive|least privilege"),
]


def classify(text: str) -> tuple[str, dict[str, int]]:
    """Return the best-matching area and the full score breakdown.

    A rule scores its full weight for matching at all, plus a small bonus for
    each additional distinct term it matched. Counting raw occurrences instead
    would let a question that says "S3 bucket" six times beat one that is really
    about the IAM policy guarding that bucket.
    """
    scores: dict[str, int] = {}
    for area, rules in AREAS.items():
        total = 0
        for weight, pattern in rules:
            hits = {h.lower() for h in re.findall(pattern, text, re.I)}
            if hits:
                total += weight + min(len(hits) - 1, 3)
        if total:
            scores[area] = total
    if not scores:
        return "unclassified", {}
    best = max(scores.items(), key=lambda kv: kv[1])[0]
    return best, scores


# Which of the four scored exam domains a question belongs to. The rules live
# in domains.py so that retag-domains.py can apply exactly the same ones to
# questions already in the bank.
from domains import domain, EXAM_WEIGHTS  # noqa: E402,F401


def qualifiers(text: str) -> list[str]:
    return [name for name, pat in QUALIFIERS if re.search(pat, text, re.I)]


# --------------------------------------------------------------------------
# Parsers, one per source format
# --------------------------------------------------------------------------

def parse_github_dump(raw: str, source: str) -> list[dict]:
    """
    Format used by the Iamrushabhshahh SAA-C03 repo:

        <n>] <question text>
        ans-<answer>            (or)   <A-E>. <answer>
        <explanation>
        -------------------------------------
    """
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    chunks = [c.strip() for c in re.split(r"(?m)^-{5,}\s*$", raw) if c.strip()]

    records = []
    for chunk in chunks:
        # Numbering is inconsistent: "12]", "12 ]" and "12." all appear.
        m = re.match(r"\s*(\d{1,4})\s*[\].)]\s*(.*)", chunk, re.S)
        if not m:
            continue
        number, body = m.group(1), m.group(2)

        answer = question = None

        # Preferred marker, when the author used one.
        am = re.search(r"(?mi)^\s*ans\s*[-:]\s*(.+?)$", body)
        if am:
            question, answer = body[: am.start()].strip(), am.group(1).strip()
            rest = body[am.end():]
        else:
            # Otherwise: these questions always end with a line asking something
            # ("Which solution will meet these requirements?"). The answer is the
            # first non-empty line after it. Anchoring on the question mark avoids
            # mistaking a question that opens "A company..." for an option "A".
            qm = list(re.finditer(r"(?m)^.*\?\s*$", body))
            if qm:
                cut = qm[-1].end()
                tail = body[cut:].lstrip("\n")
                first = next((l for l in tail.split("\n") if l.strip()), "")
                if len(first.strip()) >= 12:
                    question = body[:cut].strip()
                    answer = re.sub(r"^\s*([A-E])[.)]?\s+", r"\1. ", first.strip())
                    rest = tail[tail.find(first) + len(first):]

            # Last resort for chunks with no closing question mark: the first
            # lettered option line that is not the stem's own opening word.
            if not answer:
                om = re.search(r"(?m)^\s*([A-E])[.)]\s+(.{15,}?)\s*$", body)
                if om:
                    question = body[: om.start()].strip()
                    answer = f"{om.group(1)}. {om.group(2)}".strip()
                    rest = body[om.end():]

        if not question or not answer or len(question) < 40:
            continue

        full = f"{question}\n{answer}"
        area, scores = classify(full)
        records.append({
            "id": f"gh-{number}",
            "source": source,
            "number": int(number),
            "question": re.sub(r"\n{2,}", "\n", question),
            "answer": answer,
            "explanation": re.sub(r"\n{3,}", "\n\n", rest.strip())[:1600],
            "area": area,
            "domain": domain(full),
            "scores": scores,
            "qualifiers": qualifiers(question),
        })
    return records


def parse_whizlabs(raw: str, source: str) -> list[dict]:
    """
    Whizlabs practice PDF, converted to text:

        <n>) <question text>
        A. <option>
        B. <option>
        ...
        Answer: <letter(s)>
        <explanation>
    """
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    # The PDF text layer scatters zero-width joiners through the explanations.
    raw = raw.replace("​", "").replace("­", "")

    starts = list(re.finditer(r"(?m)^\s*(\d{1,3})\)\s+", raw))
    records = []
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(raw)
        body = raw[m.end(): end]
        number = m.group(1)

        am = re.search(r"(?m)^\s*Answers?\s*:\s*([A-E](?:\s*,?\s*[A-E])*)\s*$", body)
        if not am:
            continue

        head = body[: am.start()]
        letters = re.findall(r"[A-E]", am.group(1))
        explanation = body[am.end():].strip()

        # Options are the trailing "X. ..." lines; everything above them is the stem.
        opts = list(re.finditer(r"(?m)^\s*([A-E])[.)]\s+(.+?)\s*$", head))
        if not opts:
            continue
        question = head[: opts[0].start()].strip()
        options = {o.group(1): o.group(2).strip() for o in opts}
        answer = "; ".join(f"{l}. {options.get(l, '')}".strip() for l in letters)

        if len(question) < 30:
            continue

        full = f"{question}\n{answer}"
        area, scores = classify(full)
        records.append({
            "id": f"wl-{number}",
            "source": source,
            "number": int(number),
            "question": re.sub(r"\n+", " ", question),
            "answer": answer,
            "options": [f"{k}. {v}" for k, v in sorted(options.items())],
            "explanation": re.sub(r"\n{2,}", "\n", explanation)[:1200],
            "area": area,
            "domain": domain(full),
            "scores": scores,
            "qualifiers": qualifiers(question),
        })
    return records


def parse_optioned(raw: str, source: str) -> list[dict]:
    """
    The canonical format enrich-options.py writes: a full stem, every option,
    and the verified answer letter.

        ### 12
        <stem>
        A. <option>
        ...
        ANSWER: C
        WHY: <explanation>
        ---
    """
    raw = raw.replace("\r\n", "\n")
    records = []
    for chunk in re.split(r"(?m)^-{3,}\s*$", raw):
        chunk = chunk.strip()
        m = re.match(r"###\s+(\d+)\s*\n(.*)", chunk, re.S)
        if not m:
            continue
        number, body = int(m.group(1)), m.group(2)

        am = re.search(r"(?m)^ANSWER:\s*([A-E])\s*$", body)
        if not am:
            continue
        letter = am.group(1)
        why = ""
        wm = re.search(r"(?m)^WHY:\s*(.*)$", body)
        if wm:
            why = wm.group(1).strip()

        head = body[: am.start()]
        opts = list(re.finditer(r"(?m)^([A-E])\.\s+(.+?)\s*$", head))
        if not opts:
            continue
        question = head[: opts[0].start()].strip()
        options = {o.group(1): o.group(2).strip() for o in opts}
        if letter not in options or len(question) < 40:
            continue

        answer = f"{letter}. {options[letter]}"
        full = f"{question}\n{answer}"
        area, scores = classify(full)
        records.append({
            "id": f"{prefix_for(source)}-{number}",
            "source": source,
            "number": number,
            "question": question,
            "answer": answer,
            "options": [f"{k}. {v}" for k, v in sorted(options.items())],
            "explanation": why[:1600],
            "area": area,
            "domain": domain(full),
            "scores": scores,
            "qualifiers": qualifiers(question),
        })
    return records


def parse_ditectrev(raw: str, source: str) -> list[dict]:
    """
    The Ditectrev community question set, which marks the answer in a checkbox:

        ### <question>

        - [ ] <wrong option>
        - [x] <right option>

    Corrections to this set arrive as pull requests, so the answers carry a bit
    more scrutiny than a one-author dump.
    """
    raw = raw.replace("\r\n", "\n")
    records = []
    chunks = re.split(r"(?m)^###\s+", raw)[1:]

    for n, chunk in enumerate(chunks, 1):
        lines = chunk.split("\n")
        question = lines[0].strip()
        opts = re.findall(r"(?m)^- \[([ xX])\]\s+(.+?)\s*$", chunk)
        if len(opts) < 2 or len(question) < 25:
            continue

        letters = "ABCDEFGH"
        options, correct = [], []
        for i, (mark, text) in enumerate(opts):
            if i >= len(letters):
                break
            options.append(f"{letters[i]}. {text}")
            if mark.lower() == "x":
                correct.append(f"{letters[i]}. {text}")
        if not correct:
            continue

        answer = "; ".join(correct)
        full = f"{question}\n{answer}"
        area, scores = classify(full)
        records.append({
            "id": f"dt-{n}",
            "source": source,
            "number": n,
            "question": question,
            "answer": answer,
            "options": options,
            "explanation": "",
            "area": area,
            "domain": domain(full),
            "scores": scores,
            "qualifiers": qualifiers(question),
        })
    return records


def parse_qa_markdown(raw: str, source: str) -> list[dict]:
    """
    Generic fallback for simple interview-style sources:

        Q: <question>
        A: <answer>

    or markdown headings followed by a paragraph.
    """
    raw = raw.replace("\r\n", "\n")
    records = []
    pairs = re.findall(r"(?ms)^\s*(?:\*\*)?Q(?:uestion)?\s*\d*[.):]?\s*(?:\*\*)?\s*(.+?)\n+\s*(?:\*\*)?A(?:nswer)?\s*[.):]?\s*(?:\*\*)?\s*(.+?)(?=\n\s*(?:\*\*)?Q(?:uestion)?\s*\d*[.):]|\Z)", raw)
    for i, (q, a) in enumerate(pairs, 1):
        q, a = q.strip(), a.strip()
        if len(q) < 15:
            continue
        area, scores = classify(f"{q}\n{a}")
        records.append({
            "id": f"{source[:6]}-{i}",
            "source": source,
            "number": i,
            "question": q,
            "answer": a[:900],
            "explanation": "",
            "area": area,
            "domain": domain(q + " " + a),
            "scores": scores,
            "qualifiers": qualifiers(q),
        })
    return records


PARSERS = {
    "optioned": parse_optioned,
    "ditectrev": parse_ditectrev,
    "github-dump": parse_github_dump,
    "whizlabs": parse_whizlabs,
    "qa": parse_qa_markdown,
}


def id_aliases(qid: str) -> list[str]:
    """The same question under the two ids it can carry.

    gh-N and et-N are the same question: the option-less dump and the optioned
    PDF come from one numbered set, so a correction against either must find
    both. This pairing holds ONLY for those two. It must never be widened to
    any id ending in the same number: Cert Empire numbers its own questions
    from 1 as well, and a looser rule put a DynamoDB correction onto an
    unrelated API Gateway question.
    """
    out = [qid]
    for a, b in (("gh-", "et-"), ("et-", "gh-")):
        if qid.startswith(a):
            out.append(b + qid[len(a):])
    return out


def pick_parser(path: Path):
    """Source files are named <name>.<parser>.txt so the parser is explicit."""
    parts = path.name.split(".")
    if len(parts) >= 3 and parts[-2] in PARSERS:
        return PARSERS[parts[-2]]
    return parse_qa_markdown


# --------------------------------------------------------------------------

def main() -> None:
    SOURCES.mkdir(exist_ok=True)
    BANK.mkdir(exist_ok=True)

    records: list[dict] = []
    for path in sorted(SOURCES.glob("*.txt")) + sorted(SOURCES.glob("*.md")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        parser = pick_parser(path)
        got = parser(raw, path.stem.split(".")[0])
        print(f"{path.name:46} {parser.__name__:22} {len(got):5} records")
        records.extend(got)

    if not records:
        print("No records parsed — is sources/ empty?")
        return

    # Questions audit-source.py found structurally broken: an option letter
    # missing, an answer naming nothing on offer, two identical options. They
    # render fine and cannot be answered, so they go before anything else.
    if AUDIT_DROP.exists():
        broken = set(json.loads(AUDIT_DROP.read_text(encoding="utf-8")))
        before = len(records)
        records = [r for r in records if r["id"] not in broken]
        if before != len(records):
            print(f"audit: dropped {before - len(records)} structurally broken questions")

    # Stamp provenance once, centrally, rather than inside every parser.
    for r in records:
        r["reviewed"] = r["source"] in REVIEWED_SOURCES
        r["private"] = r["source"] in PRIVATE_SOURCES

    # Apply the adjudicators' verdicts. These live outside the bank because the
    # bank is regenerated from sources/ and would otherwise lose them.
    corrections = {}
    if CORRECTIONS.exists():
        corrections = json.loads(CORRECTIONS.read_text(encoding="utf-8"))

    dropped, fixed = 0, 0
    kept = []
    for r in records:
        c = next((corrections[a] for a in id_aliases(r["id"]) if a in corrections), None)
        if not c:
            kept.append(r)
            continue
        if c["verdict"] == "drop":
            dropped += 1
            continue
        if c["verdict"] == "fix":
            r["answer"] = c["answer"]
            r["explanation"] = c["why"]
            r["corrected"] = True
            fixed += 1
        kept.append(r)
    records = kept
    if corrections:
        print(f"corrections applied: {fixed} answers rewritten, {dropped} questions dropped")

    # De-duplicate on the first 150 characters of the question. Records that
    # carry their options go first, so when the same question arrives from both
    # the optioned source and the option-less dump, the usable one wins.
    records.sort(key=lambda r: 0 if r.get("options") else 1)

    # Which sets a question turned up in is worth keeping, not discarding. The
    # same question written independently by two outfits is a question the exam
    # is widely believed to ask, so the copy that survives records the others.
    seen: dict[str, dict] = {}
    unique = []
    for r in records:
        key = re.sub(r"\W+", "", r["question"].lower())[:150]
        kept = seen.get(key)
        if kept is None:
            seen[key] = r
            r["in_sources"] = [r["source"]]
            unique.append(r)
            continue
        if r["source"] not in kept["in_sources"]:
            kept["in_sources"].append(r["source"])
        # A question a person checked keeps its star even when the copy that
        # survived came from a set nobody reviewed.
        if r.get("reviewed"):
            kept["reviewed"] = True
    dropped = len(records) - len(unique)

    # Count publishers, not files: two of the source files come from one
    # repository, so counting files would call 381 questions corroborated when
    # they are one publisher's question appearing twice.
    for r in unique:
        r["in_origins"] = sorted({origin_of(s) for s in r["in_sources"]})
    agreed = sum(1 for r in unique if len(r["in_origins"]) > 1)
    print(f"{agreed} questions are published by more than one outfit")

    corroborated = sum(1 for r in unique if len(r["in_sources"]) > 1)
    print(f"{corroborated} questions appear in more than one set")

    (HERE / "bank.json").write_text(
        json.dumps(unique, indent=1, ensure_ascii=False), encoding="utf-8"
    )

    by_area: dict[str, list[dict]] = {}
    for r in unique:
        by_area.setdefault(r["area"], []).append(r)

    for area, items in sorted(by_area.items()):
        lines = [
            f"# {AREA_TITLES.get(area, area.title())}",
            "",
            f"{len(items)} questions. Answers are hidden behind a toggle — read the "
            "question, commit to an answer out loud, then open it.",
            "",
            "---",
            "",
        ]
        for i, r in enumerate(sorted(items, key=lambda x: x["number"]), 1):
            tags = " ".join(f"`{q}`" for q in r["qualifiers"])
            lines.append(f"### {i}. {r['id']} {tags}".rstrip())
            lines.append("")
            lines.append(r["question"])
            lines.append("")
            lines.append("<details><summary>Answer</summary>")
            lines.append("")
            lines.append(f"**{r['answer']}**")
            if r["explanation"]:
                lines.append("")
                lines.append(r["explanation"])
            lines.append("")
            lines.append("</details>")
            lines.append("")
        (BANK / f"{area}.md").write_text("\n".join(lines), encoding="utf-8")

    counts = Counter(r["area"] for r in unique)
    quals = Counter(q for r in unique for q in r["qualifiers"])

    readme = [
        "# Question bank",
        "",
        f"**{len(unique)} questions** across {len(by_area)} topic areas"
        + (f" ({dropped} duplicates removed)." if dropped else "."),
        "",
        "Built by `build-bank.py` from the raw files in `sources/`. Do not edit the",
        "files in this folder by hand — they are regenerated. To add a source, drop",
        "it in `sources/` named `<name>.<parser>.txt` and re-run the script.",
        "",
        "| Area | Questions | File |",
        "|---|---:|---|",
    ]
    for area, n in counts.most_common():
        readme.append(f"| {AREA_TITLES.get(area, area)} | {n} | [`{area}.md`]({area}.md) |")
    readme += [
        "",
        "## What the questions optimise for",
        "",
        "Exam questions almost always name a priority. These are the counts:",
        "",
        "| Qualifier | Questions |",
        "|---|---:|",
    ]
    for q, n in quals.most_common():
        readme.append(f"| {q} | {n} |")
    readme += [
        "",
        "Read the qualifier first. Several options are usually workable and the",
        "qualifier is what makes exactly one of them correct.",
        "",
    ]
    (BANK / "README.md").write_text("\n".join(readme), encoding="utf-8")

    print(f"\n{len(unique)} unique questions ({dropped} duplicates dropped)")
    for area, n in counts.most_common():
        print(f"  {area:14} {n:5}")


if __name__ == "__main__":
    main()
