# The database map

> Cue on the left, pick on the right. Which engine, then the feature the
> question is really about.

## zone: Which engine | vpc

### row

**RDS**
match: \bRDS\b
*SQL, joins, an existing app*, SQL Server, Oracle. Multi-AZ for failover.

**Aurora**
match: Aurora(?! Serverless)
*SQL, faster, Region-safe.* Reporting surges: *Aurora Auto Scaling adds
replicas*. SQL Server code at PostgreSQL price: *Babelfish*. Vectors for
AI: *pgvector*.

**Aurora Serverless v2**
match: Aurora Serverless|capacity units|\bACUs?\b
*Load comes and goes*, dev and test environments each their own: Serverless
v2. Set the *max ACUs* high enough for the peak.

**DynamoDB**
match: DynamoDB(?! Streams)
*Key-value, any scale, milliseconds*, session data, ratings, sensor reads. No
joins.

**ElastiCache**
match: ElastiCache
*Same reads over and over*, read-only history, a catalog, sessions: Redis.
App reads cache, misses, reads database, *writes it in (lazy loading)*.

**The odd ones**
match: DocumentDB|Neptune|Redshift|Timestream|\bQLDB\b|Keyspaces
MongoDB: *DocumentDB*. Graph: *Neptune*. Warehouse: *Redshift*. Telemetry
over time: *Timestream*. Tamper-proof ledger: *QLDB*. Cassandra: *Keyspaces*.

## end

## arrow

Then the feature

## zone: RDS and Aurora | sub

### row

**Multi-AZ**
match: Multi-AZ
*Failover*, no reads. A standby that serves nothing.

**Read replica**
match: read replica|custom endpoint
*Reads*, in Region or across. Promoted by hand, so not a failover. Reporting
on chosen Aurora replicas: *a custom endpoint*.

**Another Region**
match: global database|cross-Region (read )?replica|snapshot.{0,60}Region
RPO minutes: *Aurora global database*, one writer. RPO 24 hours, cheapest:
*copy snapshots to the other Region daily*. Aurora elsewhere, simplest:
*cross-Region read replica*.

**RDS Proxy**
match: RDS Proxy
*Too many connections*, Lambda opening them: RDS Proxy.

**Encrypt an existing one**
match: snapshot.{0,80}encrypt|encrypt.{0,80}snapshot
*Snapshot, copy with encryption, restore.* Cannot be switched on in place.
DAX the same: *recreate it encrypted*.

**Keeping snapshots**
match: manual (copy|snapshot)|automated backup|retention period
Keep one past 35 days: *a manual copy*. Keep paying less for idle: *snapshot
and delete*; stop lasts 7 days.

**Keep the bill down**
match: storage auto ?scaling|I/O-Optimized|Performance Insights|parameter group
Disk filling: *storage auto scaling*. Bill is I/O: *I/O-Optimized*. Which
query is slow: *Performance Insights*. Engine setting: *parameter group*.

**Who may connect**
match: IAM database authentication|IAM authentication|Secrets Manager|key rotation
No password in the app: *IAM database authentication*, a token from a role.
A password that must rotate: *Secrets Manager*. Key rotation: *KMS automatic
rotation*.

## end

## zone: DynamoDB | sub

### row

**Capacity**
match: on-demand (capacity|mode)|provisioned capacity|DynamoDB auto ?scaling|automatic scaling for the DynamoDB|capacity mode|Standard-Infrequent Access table
Unpredictable or new: *on-demand*. Steady: *provisioned + auto scaling at
70%*. Rarely read, many Regions: *Standard-IA table class*.

**DAX**
match: \bDAX\b
Same reads, *microseconds*, in front of the table.

**Global tables**
match: global tables?
*Two Regions, both writing.* Needs Streams on.

**Streams**
match: DynamoDB Streams
*React to every change*, into Lambda; to a data lake: *Streams, Lambda,
Firehose, S3*.

**TTL and PITR**
match: Time to Live|\bTTL\b|point-in-time
Rows vanish after a time: *TTL*. Back to any second in 35 days: *PITR*.
Session data for 48 hours, restorable: both.

**Analyse it**
match: export.{0,40}S3|Glue.{0,40}DynamoDB|DynamoDB.{0,40}Glue
*Export to S3*, then Athena or Redshift COPY. Metrics on a schedule: *Glue
DynamoDB export connector*. Never a scan.

**Writing to it**
match: PutItem|integration type.{0,40}DynamoDB|API Gateway.{0,80}DynamoDB
Ratings from a web form, no code: *API Gateway REST, AWS integration,
PutItem*.

## end

## zone: Taking load off | home

### row

**ElastiCache**
match: ElastiCache
Same reads, custom queries on history: *Redis cache*. Sessions shared
between servers: *Redis*.

**DAX**
match: \bDAX\b
The same for DynamoDB, *goes to the table itself*.

**Read replica**
match: read replica
*More reads* than one instance can serve.

**Writes are the problem**
match: shard|larger (DB |database )?instance
*A bigger instance, or sharding.* A replica does nothing for writes.

## end

## row: hub

**Moving in**
match: \bDMS\b|Database Migration|Schema Conversion|\bSCT\b|App2Container
Keep the old one running: *DMS*. Engine changes: *SCT*. Snapshot straight into
Aurora. Java monolith with SQL Server: *App2Container to EKS, RDS for SQL
Server Multi-AZ*.

**Backups**
match: AWS Backup
EC2 and RDS on one schedule, *with restore testing*: AWS Backup.

## key

cyan: which engine · amber: taking load off · magenta: moving in. Underlined
text is the pick.

## Notes

Reviewed against all 97 reviewed database questions on 2026-10-15. Written as
cue: pick, so each line can be learnt as a pair.
