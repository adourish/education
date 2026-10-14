# The database map

> Where every database question lives, top to bottom: which engine, then the
> feature the question is really about.

## zone: Which engine | vpc

### row

**RDS**
*SQL, joins, transactions*, an existing app. Multi-AZ for failover, read
replicas for reads.

**Aurora**
The same, *faster and Region-safe*. Serverless v2 when load comes and goes.

**DynamoDB**
*Key-value, any scale*, single-digit milliseconds. No joins.

**ElastiCache**
*Memory*: the same reads over and over, sessions. Redis or Memcached.

**DocumentDB, Neptune**
*MongoDB wording*: DocumentDB. *Relationships, graph*: Neptune.

**Redshift, Timestream**
*Reporting over history*: Redshift. *Readings over time*: Timestream.

## end

## arrow

Then the feature

## zone: RDS and Aurora | sub

### row

**Multi-AZ**
*Failover*, no reads. A standby that serves nothing.

**Read replica**
*Reads*, in Region or across. Promoted by hand, so not a failover.

**RDS Proxy**
*Too many connections*, Lambda opening them. Pools them.

**Encrypt an existing one**
*Snapshot, copy with encryption, restore*. It cannot be switched on in place.

**Aurora global**
*One writer*, other Regions read. Failover about a minute.

**Keep the bill down**
Stop lasts 7 days: *snapshot and delete*. Storage auto scaling for a filling
disk. I/O-Optimized when the bill is I/O.

## end

## zone: DynamoDB | sub

### row

**On-demand or provisioned**
*Spiky or new: on-demand*. Steady: provisioned with auto scaling.

**DAX**
The same reads, *microseconds*. In front of the table.

**Global tables**
*Two Regions, both writing*. Needs Streams on.

**Streams**
*React to every change*, into Lambda.

**TTL and PITR**
*TTL*: rows vanish after a time, free. *PITR*: back to any second in 35 days.

**Analyse it**
*Export to S3*, then Athena. Never a scan.

## end

## zone: Taking load off | home

### row

**ElastiCache**
The app checks the cache, misses, reads the database, *writes the value in*.

**DAX**
The same for DynamoDB, but it *goes to the table itself*.

**Read replica**
*More reads* than one instance can serve.

**Writes are the problem**
A bigger instance, or *sharding*. A replica does nothing for writes.

## end

## row: hub

**Moving in**
*DMS* keeps the old one running, switchover short. *SCT* when the engine
changes. An RDS snapshot imports straight into Aurora.

**Who may connect**
*IAM database authentication*: no password in the app. *Secrets Manager*
rotates one that must exist.

## key

cyan: which engine · amber: taking load off · magenta: moving in and
connecting. Underlined text is the pick.

## Notes

Aurora is still relational: a question wanting to leave SQL behind wants
DynamoDB. Multi-AZ and read replicas are the pair the exam keeps swapping.
