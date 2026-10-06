# Databases — question review

Reviewed 95 questions. Found 8 problems.

## Confirmed wrong

### gh-268
**Stated answer:** B. Use RDS Proxy between the application and the database.
**Should be:** The caching option — put Amazon ElastiCache between the application and the RDS for MySQL database (a read replica would also address the symptom; RDS Proxy does not).
**Why:** The stated problem is *read performance* ("long delays and interruptions that are caused by database read performance"). RDS Proxy pools and reuses database connections and shortens failover; it does not serve any read from cache and adds no read capacity, so it cannot relieve a read-throughput or read-latency bottleneck. The file's own explanation only claims connection-management benefits, which does not answer the question asked.

### gh-338
**Stated answer:** D. Set up an Aurora global database for the DB cluster. Specify a minimum of one DB instance in the secondary Region.
**Should be:** Set up the Aurora global database and then remove the DB instance from the secondary Region (a "headless" secondary cluster).
**Why:** Aurora global databases support a headless secondary — a secondary cluster with zero DB instances. Storage-level replication to the secondary Region continues, so the DR requirement ("must replicate data to a secondary AWS Region") is still met, but you pay only storage and replicated write I/O instead of instance-hours. Since the qualifier is MOST cost-effectively and no RTO is stated, keeping a provisioned instance running in the secondary Region is the more expensive of the two Aurora global database choices.

### gh-536
**Stated answer:** C. Change the setup from a Single-AZ to a Multi-AZ instance deployment. Provide two additional read replicas for the data scientists.
**Should be:** Change the setup to a Multi-AZ **DB cluster** deployment (two readable standby instances) and give the data scientists the cluster reader endpoint.
**Why:** The qualifier is MOST cost-effectively. The stated answer provisions four instances (primary + non-readable standby + two read replicas). An RDS for PostgreSQL Multi-AZ DB cluster provisions three instances (writer + two standbys) and, unlike the Multi-AZ *instance* deployment, those standbys **are** readable through the reader endpoint. That delivers the same two things the question asks for — high availability and near real-time read-only access for complex queries — with one fewer billed instance and no separate replicas to manage.

## Explanation problems

### gh-31
**Issue:** The explanation says "you can use AWS Config to create tags for your resources… rules that automatically tag resources when they are created or when their configurations change." AWS Config does not tag anything. It evaluates resource configuration against rules (here, the managed `required-tags` rule) and reports non-compliance; applying a tag would require a separate remediation action (for example an SSM Automation document) or a different service. The stated answer is right for *detecting* untagged resources, but the reason given for it is wrong.

### gh-420
**Issue:** The explanation describes an RDS Multi-AZ DB cluster as "automatically replicating data to a standby instance in a different Availability Zone" — the single, non-readable standby of a Multi-AZ *instance* deployment. A Multi-AZ DB cluster has two standby instances in two other AZs and both are readable via the reader endpoint. That readability is the entire reason the stated answer ("point the read workload to the reader endpoint") works, so the explanation misdescribes the feature it is justifying.

### gh-472
**Issue:** The explanation ends with an unrelated paragraph pasted in from a different question: "A company hosts a website on Amazon EC2 instances behind an Application Load Balancer (ALB). The website serves static content. Website traffic is increasing, and the company is concerned about a potential increase in cost." Nothing in it relates to DynamoDB or DAX. The DAX reasoning itself is correct.

### gh-515
**Issue:** The explanation justifies only two of the three required options (B and C) and never addresses E. Option E as worded — "scaling globally to support petabytes of data and tens of millions of requests per minute" — describes DynamoDB, not Redshift; Redshift is a petabyte-scale data warehouse for analytic queries, not a service characterised by tens of millions of requests per minute. A reader cannot tell from this explanation why the third option was chosen.

### gh-670
**Issue:** The explanation states "On-demand (Option A) is expensive for infrequent use." That is backwards. DynamoDB on-demand mode bills per request with no charge for idle capacity, which makes it the cheap option for a table exercised for 4 hours a week; provisioned capacity bills per RCU/WCU-hour for all 168 hours of the week whether the tests are running or not. On the numbers, on-demand is several times cheaper for this usage pattern unless the provisioned capacity is also scaled down between tests — so the reasoning given here is wrong, and it puts the stated answer in doubt as well.

Checked 95 questions: 3 stated answers are wrong, 0 are out of date, and 5 have defective explanations — overall a reasonably sound set whose errors cluster in the cost-qualified Multi-AZ and caching questions and in carelessly copied explanations.
