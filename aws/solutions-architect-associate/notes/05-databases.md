# 05 — Databases

## Pick the database first

| Shape of the need | Service |
|---|---|
| Relational, standard engine, managed | **RDS** |
| Relational, needs MySQL or PostgreSQL compatibility with cloud-scale performance | **Aurora** |
| Relational, want to pay nothing when idle | **Aurora Serverless v2** |
| Key-value or document, single-digit millisecond, massive scale | **DynamoDB** |
| DynamoDB but needs **microseconds** | **DynamoDB + DAX** |
| Caching in front of a database | **ElastiCache (Redis or Memcached)** |
| Petabyte analytics and reporting over structured data | **Redshift** |
| SQL over data already sitting in S3, no servers | **Athena** |
| Graph — social, fraud rings, recommendations | **Neptune** |
| Time series — IoT sensors, metrics | **Timestream** |
| Ledger with a cryptographically verifiable history | **QLDB** |
| MongoDB-compatible document store | **DocumentDB** |
| Wide-column Cassandra-compatible | **Keyspaces** |
| In-memory **durable** data store, Redis-compatible | **MemoryDB for Redis** |

## RDS — Relational Database Service

| Cue | Answer |
|---|---|
| Engines | **Aurora, MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server** |
| What AWS manages | **provisioning, patching, backups, recovery, failure detection, repair** |
| What you do **not** get | **operating system access** — no SSH to the host |
| If a question requires OS access or an unsupported engine | run the database **on EC2**, not RDS |
| Automated backup retention, default and range | **7 days**, range **0 to 35 days** |
| What automated backups let you do | **point-in-time recovery**, usually to within **5 minutes** |
| Manual snapshots | kept **until you delete them**, and they survive deleting the instance |
| Restoring a snapshot produces | a **new instance with a new endpoint** — it never restores in place |
| Can you encrypt an existing unencrypted RDS instance | **no, not in place** — snapshot it, copy the snapshot with encryption on, restore from that |
| Encryption at rest uses | **KMS** |
| Encryption in transit uses | **SSL/TLS** |
| Maintenance window | a weekly window when AWS applies patches; **Multi-AZ patches the standby first, then fails over** |

### Multi-AZ versus read replicas — the most-tested table on the exam

| | Multi-AZ | Read replica |
|---|---|---|
| Purpose | **High availability** | **Read scaling** |
| Replication | **Synchronous** | **Asynchronous** |
| Can you read from it | **No** | **Yes** |
| Failover | **Automatic**, 60 to 120 seconds | **Manual promotion** |
| Location | Another **AZ** in the same region | Same AZ, another AZ, or **another region** |
| How many | 1 standby (or 2 readable standbys in the newer Multi-AZ DB cluster) | **5** per instance, 15 for Aurora |
| Endpoint | **Same endpoint**, DNS flips | **Its own endpoint** |
| What it protects against | AZ failure, instance failure, patching downtime | nothing — it is not a HA feature |

> **Say it out loud:** "Multi-AZ is durability and availability. Read replicas are scalability." Both can be true at once — you can have Multi-AZ **and** read replicas.

### Multi-AZ failover triggers

AZ outage, primary instance failure, instance type change, OS patching, manual reboot with failover, storage failure. **Not** triggered by heavy read load.

## Aurora

| Cue | Answer |
|---|---|
| Compatibility | **MySQL and PostgreSQL** |
| Performance claim | up to **5x MySQL**, **3x PostgreSQL** |
| Storage | **grows automatically in 10 GB steps up to 128 TiB** |
| Copies of your data | **6 copies across 3 AZs** |
| Fault tolerance | survives losing **2 copies for writes**, **3 copies for reads**, self-healing |
| Read replicas | up to **15 Aurora Replicas**, with sub-10-millisecond replica lag |
| Failover time | typically **under 30 seconds** |
| Endpoints | **cluster (writer)**, **reader**, and **custom** endpoints |
| To scale replicas automatically | **Aurora Auto Scaling** on the replica count |
| For cross-region, near-zero-lag disaster recovery | **Aurora Global Database** — up to 5 secondary regions, typically **under 1 second** lag, failover in about **1 minute** |
| For unpredictable or intermittent load | **Aurora Serverless v2** — scales in fine increments, can scale to a low floor |
| To run analytics without touching the main cluster | **Aurora parallel query** or a reader endpoint |
| Zero-ETL to Redshift | **Aurora zero-ETL integration with Redshift** |
| Backtrack | rewind an Aurora MySQL cluster **in place** to a recent point, without restoring a snapshot |
| Cloning | **fast database cloning** — a copy-on-write clone, far quicker and cheaper than a snapshot restore |

## DynamoDB

| Cue | Answer |
|---|---|
| Type | **serverless key-value and document** NoSQL |
| Latency | **single-digit milliseconds** at any scale |
| Max item size | **400 KB** |
| Primary key options | **partition key alone**, or **partition key + sort key (composite)** |
| Capacity modes | **on-demand** (unpredictable traffic, pay per request) and **provisioned** (predictable traffic, cheaper, supports auto scaling) |
| Read consistency | **eventually consistent by default**; ask for **strongly consistent** and it costs twice the RCUs |
| 1 RCU | one strongly consistent read per second of up to **4 KB** |
| 1 WCU | one write per second of up to **1 KB** |
| Microsecond reads | **DAX** — a fully managed, highly available, in-memory cache that sits in front of the table |
| Is DAX good for write-heavy work | **no** — it is a read-through cache |
| Global secondary index | **different partition and sort key**, can be added any time, has **its own capacity**, **eventually consistent only** |
| Local secondary index | **same partition key, different sort key**, must be created **with the table**, shares the table's capacity, **can be strongly consistent** |
| To replicate a table across regions, active-active | **Global Tables** |
| To react to every change to an item | **DynamoDB Streams** plus Lambda, 24-hour retention |
| To delete old items automatically and for free | **TTL** on an attribute holding an epoch timestamp |
| To stop two writers clobbering each other | **conditional writes** / optimistic locking with a version attribute |
| To make several writes all-or-nothing | **transactions** |
| To back it up | **point-in-time recovery (35 days)** and **on-demand backups** |
| Scan versus Query | **Query** uses the key and is efficient. **Scan** reads the whole table and is the thing to avoid. |
| Symptom: `ProvisionedThroughputExceededException` | a **hot partition** or under-provisioned capacity — fix the key design or switch to on-demand |
| How to design a good partition key | **high cardinality, evenly accessed** — user ID, not a status flag |

## ElastiCache

| | Redis | Memcached |
|---|---|---|
| Data structures | Lists, sets, sorted sets, hashes, bitmaps | **Simple key-value only** |
| Persistence | **Yes**, snapshots and AOF | **No** |
| Replication and failover | **Yes**, Multi-AZ with automatic failover | **No** |
| Read replicas | **Yes** | No |
| Multi-threaded | No (mostly single-threaded) | **Yes** |
| Scaling shape | **Sharding (cluster mode) and replicas** | **Horizontal, add nodes** |
| Pub/sub, geospatial, Lua | **Yes** | No |
| Pick it when the question says | "high availability", "persistence", "leaderboard", "session store that must survive", "sorted set" | "simplest possible cache", "multi-threaded", "no persistence needed", "scale out horizontally" |

| Caching concept | Meaning |
|---|---|
| **Lazy loading / cache-aside** | Only cache on a miss. Cheap on memory, but the first request is always slow and data can go stale. |
| **Write-through** | Write to cache and database together. Cache is always fresh, but you cache data nobody reads. |
| **TTL** | Expire entries, the usual answer to "how do we stop stale data?" |

> **The classic scenario:** "A read-heavy relational workload is slowing down and the same queries repeat." The two valid answers are **a read replica** (scale reads at the database) and **ElastiCache** (remove the reads entirely). If the question says "reduce database load" and "microsecond or sub-millisecond", pick the cache.

## Redshift

| Cue | Answer |
|---|---|
| Type | **Petabyte-scale columnar data warehouse**, for OLAP not OLTP |
| Architecture | one **leader node** that parses and distributes SQL, plus **compute nodes** with slices |
| What the leader node does | receives queries, builds the plan, **distributes SQL to the compute nodes** when the query touches user tables |
| Availability shape | historically **single-AZ**; now supports **Multi-AZ** for RA3 clusters |
| Backups | automatic snapshots to S3, and **cross-region snapshot copy** for disaster recovery |
| To query data left in S3 without loading it | **Redshift Spectrum** |
| To control concurrency and give short queries priority | **Workload Management (WLM)** — it defines **query queues** |
| To run without managing clusters | **Redshift Serverless** |
| Distribution styles | **KEY** (co-locate join keys), **EVEN**, **ALL** (copy a small dimension table to every node), **AUTO** |
| Sort keys | **compound** (default, best for predictable filter order) and **interleaved** (equal weight across columns) |
| To load data efficiently | the **COPY** command from S3, in parallel |
| Encryption | KMS or CloudHSM, and **enhanced VPC routing** keeps traffic inside your VPC |
| Redshift versus Athena | **Redshift** for repeated, complex, high-concurrency reporting on loaded data. **Athena** for ad-hoc SQL on S3 with nothing to run. |
| Redshift versus EMR | **Redshift** for SQL analytics. **EMR** for Hadoop, Spark, and custom processing frameworks. |

## The purpose-built databases

| Service | One-line trigger |
|---|---|
| **Neptune** | "graph", "relationships", "social network", "fraud ring", "knowledge graph", "Gremlin", "SPARQL" |
| **Timestream** | "time series", "IoT sensor readings", "metrics over time" |
| **QLDB** | "immutable", "cryptographically verifiable", "complete history of changes", "central trusted ledger" |
| **Managed Blockchain** | "multiple parties", "no central trusted authority", "Hyperledger", "Ethereum" |
| **DocumentDB** | "MongoDB compatible", "JSON documents", managed |
| **Keyspaces** | "Cassandra compatible", "CQL" |
| **MemoryDB for Redis** | "in-memory speed **and** durability as the primary database" |

> **QLDB versus Managed Blockchain:** QLDB has **one owner** you trust. Managed Blockchain has **several parties** who do not fully trust each other.

## Database migration

| Cue | Answer |
|---|---|
| Move a database to AWS with minimal downtime | **AWS DMS** — the source stays live during migration |
| Change engines, for example Oracle to Aurora PostgreSQL | **DMS plus the Schema Conversion Tool (SCT)** |
| Keep source and target in sync for a while | **DMS ongoing replication (change data capture)** |
| Move whole servers, not just databases | **AWS Application Migration Service (MGN)** |
