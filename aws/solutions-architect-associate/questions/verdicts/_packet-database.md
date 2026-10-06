# Flagged questions to adjudicate: database

8 questions. For each: establish the truth, then decide keep / fix / drop.


---

## gh-268  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: B. Use RDS Proxy between the application and the database. Should be: The caching option — put Amazon ElastiCache between the application and the RDS for MySQL database (a read replica would also address the symptom; RDS Proxy does not). Why: The stated problem is *read performance* ("long delays and interruptions that are caused by database read performance"). RDS Proxy pools and r

**Question:**

A gaming company has a web application that displays scores. The application runs on Amazon EC2 instances behind an Application Load Balancer. The application stores data in an Amazon RDS for MySQL database. Users are starting to experience long delays and interruptions that are caused by database read performance. The company wants to improve the user experience while minimizing changes to the application’s architecture.
What should a solutions architect do to meet these requirements?

**Stated answer:** B. Use RDS Proxy between the application and the database.

**Stated explanation:** RDS Proxy is a fully managed database proxy for Amazon RDS databases, including MySQL.
It helps improve scalability and availability for database connections, reducing the impact of database connection management on the application.


---

## gh-31  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation says "you can use AWS Config to create tags for your resources… rules that automatically tag resources when they are created or when their configurations change." AWS Config does not tag anything. It evaluates resource configuration against rules (here, the managed `required-tags` rule) and reports non-compliance; applying a tag would require a separate remediation action (f

**Question:**

A company that hosts its web application on AWS wants to ensure all Amazon EC2 instances. Amazon RDS DB instances. and Amazon Redshift clusters are configured with tags. The company wants to minimize the effort of configuring and operating this check.
What should a solutions architect do to accomplish this?

**Stated answer:** A. Use AWS Config rules to define and detect resources that are not properly tagged.

**Stated explanation:** Yes, you can use AWS Config to create tags for your resources. AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. You can use AWS Config to create rules that automatically tag resources when they are created or when their configurations change.


---

## gh-338  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: D. Set up an Aurora global database for the DB cluster. Specify a minimum of one DB instance in the secondary Region. Should be: Set up the Aurora global database and then remove the DB instance from the secondary Region (a "headless" secondary cluster). Why: Aurora global databases support a headless secondary — a secondary cluster with zero DB instances. Storage-level replication

**Question:**

A solutions architect must create a disaster recovery (DR) plan for a high-volume software as a service (SaaS) platform. All data for the platform is stored in an Amazon Aurora MySQL DB cluster.
The DR plan must replicate data to a secondary AWS Region.
Which solution will meet these requirements MOST cost-effectively?

**Stated answer:** D. Set up an Aurora global database for the DB cluster. Specify a minimum of one DB instance in the secondary Region.

**Stated explanation:** (none)


---

## gh-420  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation describes an RDS Multi-AZ DB cluster as "automatically replicating data to a standby instance in a different Availability Zone" — the single, non-readable standby of a Multi-AZ *instance* deployment. A Multi-AZ DB cluster has two standby instances in two other AZs and both are readable via the reader endpoint. That readability is the entire reason the stated answer ("point t

**Question:**

A company wants to use an Amazon RDS for PostgreSQL DB cluster to simplify time-consuming database administrative tasks for production database workloads. The company wants to ensure that its database is highly available and will provide automatic failover support in most scenarios in less than 40 seconds. The company wants to offload reads off of the primary instance and keep costs as low as possible.
Which solution will meet these requirements?

**Stated answer:** D. Use an Amazon RDS Multi-AZ DB cluster deployment Point the read workload to the reader endpoint.

**Stated explanation:** Amazon RDS Multi-AZ DB Cluster Deployment: This provides high availability by automatically replicating data to a standby instance in a different Availability Zone. In case of a failure, Amazon RDS automatically fails over to the standby instance.


---

## gh-472  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation ends with an unrelated paragraph pasted in from a different question: "A company hosts a website on Amazon EC2 instances behind an Application Load Balancer (ALB). The website serves static content. Website traffic is increasing, and the company is concerned about a potential increase in cost." Nothing in it relates to DynamoDB or DAX. The DAX reasoning itself is correct.

**Question:**

A company has a mobile chat application with a data store based in Amazon DynamoDB. Users would like new messages to be read with as little latency as possible. A solutions architect needs to design an optimal solution that requires minimal application changes.
Which method should the solutions architect select?

**Stated answer:** A. Configure Amazon DynamoDB Accelerator (DAX) for the new messages table. Update the code to use the DAX endpoint.

**Stated explanation:** Amazon DynamoDB Accelerator (DAX) is an in-memory caching service for DynamoDB that helps improve the read performance of DynamoDB tables.A company hosts a website on Amazon EC2 instances behind an Application Load Balancer (ALB). The website serves static content. Website traffic is increasing, and the company is concerned about a potential increase in cost.


---

## gh-515  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation justifies only two of the three required options (B and C) and never addresses E. Option E as worded — "scaling globally to support petabytes of data and tens of millions of requests per minute" — describes DynamoDB, not Redshift; Redshift is a petabyte-scale data warehouse for analytic queries, not a service characterised by tens of millions of requests per minute. A reader

**Question:**

A company is migrating an on-premises application to AWS. The company wants to use Amazon Redshift as a solution.
Which use cases are suitable for Amazon Redshift in this scenario? (Choose three.)

**Stated answer:** B. Supporting client-side and server-side encryption

**Stated explanation:** C. Building analytics workloads during specified hours and when the application is not active

E. Scaling globally to support petabytes of data and tens of millions of requests per minute
Amazon Redshift supports encryption for data at rest and in transit, providing security features for sensitive data. This makes it suitable for scenarios where encryption is a requirement.
Amazon Redshift is a fully managed data warehouse service optimized for analytical queries. Running analytics workloads during specified hours aligns with Redshift's strengths, allowing for efficient query processing and analysis.


---

## gh-536  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: C. Change the setup from a Single-AZ to a Multi-AZ instance deployment. Provide two additional read replicas for the data scientists. Should be: Change the setup to a Multi-AZ DB cluster** deployment (two readable standby instances) and give the data scientists the cluster reader endpoint. **Why: The qualifier is MOST cost-effectively. The stated answer provisions four instances (pr

**Question:**

A company wants to provide data scientists with near real-time read-only access to the company's production Amazon RDS for PostgreSQL database. The database is currently configured as a Single-AZ database. The data scientists use complex queries that will not affect the production database. The company needs a solution that is highly available.
Which solution will meet these requirements MOST cost-effectively?

**Stated answer:** C. Change the setup from a Single-AZ to a Multi-AZ instance deployment. Provide two additional read replicas for the data scientists.

**Stated explanation:** C. Changing to a Multi-AZ instance deployment and providing two additional read replicas for the data scientists is a good solution. Multi-AZ provides high availability, and read replicas can be used to offload read-only queries from the production database, allowing data scientists to run their complex queries without impacting the production environment.


---

## gh-670  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation states "On-demand (Option A) is expensive for infrequent use." That is backwards. DynamoDB on-demand mode bills per request with no charge for idle capacity, which makes it the cheap option for a table exercised for 4 hours a week; provisioned capacity bills per RCU/WCU-hour for all 168 hours of the week whether the tests are running or not. On the numbers, on-demand is seve

**Question:**

A company performs tests on an application that uses an Amazon DynamoDB table. The tests run for 4 hours once a week. The company knows
how many read and write operations the application performs to the table each second during the tests. The company does not currently use
DynamoDB for any other use case. A solutions architect needs to optimize the costs for the table.
Which solution will meet these requirements?

**Stated answer:** Answer: B) Choose provisioned mode with calculated RCU/WCU.

**Stated explanation:** Provisioned mode is cost-effective for predictable weekly workloads.
On-demand (Option A) is expensive for infrequent use.
