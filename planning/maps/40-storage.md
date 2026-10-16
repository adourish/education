# The storage map

> Cue on the left, pick on the right. Which kind, then S3, EFS, EBS, getting
> data in, keeping it.

## zone: Which kind | vpc

### row

**S3**
match: \bS3\b
Objects by URL, unlimited. *Static site: S3 + CloudFront.*

**EBS**
match: \bEBS\b
*One instance, one zone.* Multi-Attach: io1/io2 only, same zone.

**EFS**
match: \bEFS\b
*Linux, many servers, across zones*, NFS.

**FSx for Windows**
match: FSx for Windows
*SMB, Active Directory.* Multi-AZ to survive a zone; SSD for 2 GB/s.

**FSx for Lustre**
match: FSx for Lustre
*HPC, training, sub-millisecond.* Linked to a bucket.

**FSx for ONTAP**
match: ONTAP
*SMB and NFS together*, Windows and Linux on one share. Auto tiering.

**Instance store**
match: instance store
*Scratch, fastest, gone on stop.*

## end

## arrow

Then what to do with it

## zone: S3 | sub

### row

**Retrieval time picks the class**
match: Intelligent-Tiering|Standard-IA|One Zone-IA|Glacier|Deep Archive|storage class
Milliseconds, once a year: *Glacier Instant*. Up to 12 hours: *Flexible*.
Up to 48 hours, cheapest: *Deep Archive*. Pattern unknown or varies, no
retrieval cost, minimal management: *Intelligent-Tiering*.

**Minimums**
match: minimum (storage )?(duration|charge)|minimum of \d+ days
IA *30 days*, Glacier *90*, Deep Archive *180*, 128 KB. Short-lived or tiny:
stay in Standard.

**Lifecycle rules**
match: [Ll]ifecycle (rule|polic|configuration)
*Move after N days, delete after N days.* Filter by prefix, tag or *size*.
Clears incomplete multipart uploads.

**Cannot be deleted**
match: Object Lock|legal hold|WORM
*Object Lock compliance*: not even root. Governance: an admin can. Needs
versioning. Public-read-but-locked: Object Lock + CloudFront + bucket policy.

**Against accidents**
match: MFA Delete|[Vv]ersioning|Block Public Access
*Versioning + MFA Delete.* *Block Public Access* on the account.

**Who may reach it**
match: bucket polic|aws:Source|access point|Requester Pays|gateway (VPC )?endpoint
Another account: *bucket policy*. One VPC: *aws:SourceVpc*. Named addresses:
*IP condition*. Many apps: *access point each*. Reader pays: *Requester
Pays*. From instances, privately: *gateway endpoint*.

**Three kinds of signed access**
match: origin access|\bOAC\b|\bOAI\b|presigned|pre-signed|signed URL|signed cookie
Bucket answers only CloudFront: *origin access control*. Paying viewers:
*CloudFront signed URL*. One person, one object, one upload: *S3 presigned
URL*.

**Encryption**
match: SSE-S3|SSE-KMS|Bucket Key|server-side encryption
Nobody asked who holds the key: *SSE-S3*. Control rotation, audit use:
*SSE-KMS, customer managed key*. KMS bill or request limit: *Bucket Key*.

**Personal data (Macie)**
match: Macie|Object Lambda|sensitive data discovery
Watch buckets all the time: *Macie automated sensitive data discovery*. A
one-off look: *a classification job*. Act on a finding: *EventBridge rule,
Lambda removes it*. Serve it to one app with the PII masked, no copy:
*Object Lambda*. Macie only finds; it never changes an object.

**Faster**
match: Transfer Acceleration|multipart|Express One Zone
Uploads from far away: *Transfer Acceleration + multipart*. Sub-millisecond
reads: *Express One Zone*. Downloads everywhere: CloudFront.

**Copies and events**
match: [Rr]eplication|Multi-Region Access Point|event notification|S3 Event
Disaster recovery, least loss: *Cross-Region Replication*. Logs into one
bucket: *Same-Region Replication*. One address, nearest bucket: *Multi-Region
Access Point*. On every upload: *event notification* to Lambda, SQS, SNS.

**Across many buckets**
match: Storage Lens|S3 Inventory|Batch Operations
Which buckets are idle or unversioned: *Storage Lens*. Act on millions of
objects: *Inventory + Batch Operations*.

## end

## zone: EFS | sub

### row

**Mounting**
match: mount target|EFS.{0,60}(Lambda|ECS|Fargate)|VPC sharing
*A mount target per zone.* Lambda mounts it for big dependencies. Another
account: *VPC sharing*.

**Throughput and cost**
match: throughput mode|elastic throughput|bursting|EFS (Standard-)?Infrequent|Transition into IA|EFS.{0,40}lifecycle
Spike nobody can size: *elastic*. Files unused for N days: *lifecycle to
Infrequent Access*. Another Region: *AWS Backup*.

## end

## zone: EBS | sub

### row

**Which volume**
match: \bgp3\b|General Purpose SSD|\bio[12]\b|Provisioned IOPS|\bst1\b|\bsc1\b|Throughput Optimized|Cold HDD
Default: *gp3* (IOPS set apart from size). Over 16,000 IOPS: *io2*; 200,000:
*io2 Block Express*. Big sequential reads, cheap: *st1*. Cold: *sc1*. HDDs
cannot boot.

**Snapshots**
match: EBS snapshot|snapshot lifecycle|Data Lifecycle Manager|fast snapshot restore
Schedule and prune: *Data Lifecycle Manager*. Clone production into test:
*fast snapshot restore*.

**Controls**
match: encrypt(ed|ion) by default|account attribute|Elastic Volumes|Compute Optimizer|block public access for (EBS )?snapshots|Config rule.{0,60}(EBS|volume)
Encrypt every new volume: *account setting*. Prove they are: *Config rule*.
No public snapshots: *block at the organization*. Grow live: *Elastic
Volumes*. Right-size: *Compute Optimizer*.

## end

## zone: Getting data in | home

### row

**Snowball Edge**
match: Snowball|Snowcone|Snowmobile
Too much for the line: *a device*. 10 Mbps is about 100 GB a day. Work with
no connection: *Compute Optimized*.

**DataSync**
match: DataSync
Over the network, *repeatedly, only what changed*, encrypted. Hundreds of
GB on 100 Mbps is this.

**Storage Gateway**
match: Storage Gateway|File Gateway|Volume Gateway|Tape Gateway|stored volume|cached volume
NFS or SMB share into a bucket: *File*. All data local, backed up: *Volume,
stored*. Hot data local, rest in S3: *Volume, cached*. Tapes into Deep
Archive, same backup software: *Tape*.

**Transfer Family**
match: Transfer Family|Transfer for SFTP
Partners keep *SFTP*, files land in S3.

## end

## row: hub

**AWS Backup**
match: AWS Backup
*One plan for every service*, retention in years, copy to another Region.
Vault lock cannot be undone.

**Querying files**
match: Athena|Parquet
SQL over S3, no server: *Athena*. Cut the scan: *Parquet*.

## key

cyan: which kind · amber: getting data in · magenta: keeping it. Underlined
text is the pick.

## Notes

Reviewed against all 150 reviewed storage questions on 2026-10-15. Written
as cue: pick, so each line can be learnt as a pair.
