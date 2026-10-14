# The storage map

> Where every storage question lives, top to bottom: which kind, then what S3
> and EBS can do, then getting data in and keeping it safe.

## zone: Which kind | vpc

### row

**S3**
match: \bS3\b
*Objects*, unlimited, reached by URL. Not a disk.

**EBS**
match: \bEBS\b
*One instance, one zone*, a plain disk. Multi-Attach only io1/io2, same zone.

**EFS**
*Many Linux servers, across zones*. Grows on its own.

**FSx for Windows**
*SMB, Active Directory*, Windows apps.

**FSx for Lustre**
*Speed for modelling or training*. Links to a bucket.

**Instance store**
*Scratch, fastest, gone on stop*.

## end

## arrow

Then what the question wants done with it

## zone: S3 | sub

### row

**Storage classes**
match: Intelligent-Tiering|Standard-IA|One Zone-IA|Glacier|Deep Archive|storage class
Standard · *Intelligent-Tiering when unknown* · Standard-IA · One Zone-IA ·
Glacier Instant · Flexible · *Deep Archive, cheapest*.

**Minimums**
match: minimum (storage )?(duration|charge)|minimum of \d+ days
IA charges *30 days*, Glacier *90*, Deep Archive *180*. Short-lived data costs
more there than in Standard.

**Lifecycle rules**
match: [Ll]ifecycle (rule|polic|configuration)
*Move after N days, delete after N days*, clean up incomplete multipart
uploads.

**Nobody may delete it**
match: Object Lock|legal hold|WORM
*Object Lock, compliance mode*: not even root. Governance: an admin can lift
it.

**Accidents**
match: MFA Delete|[Vv]ersioning|Block Public Access
*Versioning and MFA Delete*. Block Public Access on the account.

**Only through CloudFront**
match: origin access|\bOAC\b|\bOAI\b|presigned|pre-signed
*Origin access control* and a bucket policy. Presigned URL: one person, one
object, a while.

**Faster**
match: Transfer Acceleration|multipart|Express One Zone
*Transfer Acceleration* for uploads from far away. *Multipart* over 100 MB.
Express One Zone for millions of tiny reads.

**Copies and events**
match: [Rr]eplication|event notification|S3 Event
*Replication* to another Region or bucket, needs versioning. Event
notifications into Lambda, SQS, SNS.

## end

## zone: EBS | sub

### row

**gp3**
match: \bgp3\b|General Purpose SSD
The default. IOPS and throughput *set apart from size*; gp2 ties them.

**io2**
match: \bio[12]\b|Provisioned IOPS
*Over 16,000 IOPS*, a database that needs a promise, Multi-Attach.

**st1 and sc1**
match: \bst1\b|\bsc1\b|Throughput Optimized|Cold HDD
Hard disks: *big sequential reads* cheap, and cold. Neither can boot.

**Snapshots**
match: EBS snapshot|snapshot lifecycle|Data Lifecycle Manager|encryption by default
To S3, incremental. *Data Lifecycle Manager* on a schedule. Encrypt by
default in the Region.

## end

## zone: Getting data in | home

### row

**Snowball Edge**
match: Snowball|Snowcone|Snowmobile
*A lot, once*, and the line is too slow. Past about a week of transfer.

**DataSync**
*A lot, repeatedly*, over the network. Only what changed.

**Storage Gateway**
match: Storage Gateway|File Gateway|Volume Gateway|Tape Gateway
*File*: a share backed by a bucket. *Volume*: local disk, copy in AWS. *Tape*:
retire a tape library.

**Transfer Family**
Keep using *SFTP*, straight into S3.

## end

## row: hub

**AWS Backup**
*One plan, every service*, a vault. Vault lock in compliance mode cannot be
undone. Copy to another Region.

**Querying files**
match: Athena|Parquet
*Athena* for SQL over S3; convert to Parquet with Glue to cut the scan.

## key

cyan: which kind · amber: getting data in · magenta: keeping it. Underlined text is the pick.

## Notes

One Zone is the only class that does not survive losing a zone. S3 Express
One Zone is a different thing: the fastest and dearest, not an archive.
