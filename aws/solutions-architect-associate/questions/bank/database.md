# Databases — RDS, Aurora, DynamoDB, caching, warehousing

208 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-8

When should I choose Provisioned IOPS over Standard RDS storage?

<details><summary>Answer</summary>

**B. If you use production online transaction processing (OLTP) workloads.**

</details>

### 2. wl-9

Organization XYZ is planning to build an online chat application for their enterprise level collaboration for their employees across the world. They are looking for a single digit latency fully managed database to store and retrieve conversations. What would AWS Database service you recommend?

<details><summary>Answer</summary>

**A. AWS DynamoDB**

Read more here: https://aws.amazon.com/dynamodb/#whentousedynamodb
Read more here:
https://aws.amazon.com/about-aws/whats-new/2015/07/amazon-dynamodb-available-
now-cross-region-replication-triggers-and-streams/

</details>

### 3. dt-10

Because of the extensibility limitations of striped storage attached to Windows Server, Amazon RDS does not currently support increasing storage on a [...] DB Instance.

<details><summary>Answer</summary>

**A. SQL Server.**

</details>

### 4. q-11

A company has an application that runs on Amazon EC2 instances and uses an Amazon Aurora database. The EC2 instances connect to the database by using user names and passwords that are stored locally in a file. The company wants to minimize the operational overhead of credential management. What should a solutions architect do to accomplish this goal?

<details><summary>Answer</summary>

**A. Use AWS Secrets Manager. Turn on automatic rotation.**

AWS Secrets Manager is a secrets management service that helps you protect access to your applications, services, and IT resources. This service enables you to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

</details>

### 5. q-13 `least-ops`

A company performs monthly maintenance on its AWS infrastructure. During these maintenance activities, the company needs to rotate the credentials for its Amazon RDS for MySQL databases across multiple AWS Regions. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Store the credentials as secrets in AWS Secrets Manager. Use multi-Region secret replication for the required Regions. Configure Secrets Manager to rotate the secrets on a schedule.**

AWS Secrets Manager allows you to store, manage, and rotate secrets, such as database credentials, across multiple AWS Regions. By enabling multi-Region secret replication, you can replicate the secrets across the required Regions to allow for seamless rotation of the credentials during maintenance activities. Additionally, Secrets Manager provides automatic rotation of secrets on a schedule, which would minimize the operational overhead of rotating the credentials on a monthly basis.

</details>

### 6. wl-14

Your organization is building a collaboration platform for which they chose AWS EC2 for web and application servers and MySQL RDS instance as the database. Due to the nature of the traffic to the application, they would like to increase the number of connections to RDS instances. How can this be achieved?

<details><summary>Answer</summary>

**B. Create a new parameter group, attach it to the DB instance and change the setting.**

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithPar
amGroups

</details>

### 7. dt-17

Amazon RDS supports SOAP only through [...].

<details><summary>Answer</summary>

**D. HTTPS.**

</details>

### 8. dt-23

In the context of MySQL, version numbers are organized as MySQL version = X.Y.Z. What does X denote here?

<details><summary>Answer</summary>

**D. Major version.**

</details>

### 9. wl-24

You have launched an RDS instance with MySQL database with default configuration for your file sharing application to store all the transactional information. Due to security compliance, your organization wants to encrypt all the databases and storage on the cloud. They approached you to perform this activity on your MySQL RDS database. How can you achieve this?

<details><summary>Answer</summary>

**A. Copy snapshot from the latest snapshot of your RDS instance, select encryption**

https://aws.amazon.com/blogs/aws/amazon-rds-update-share-encrypted-snapshots-enc
rypt-existing-instances/

</details>

### 10. dt-27

When running my DB Instance as a Multi-AZ deployment, can I use the standby for read or write operations?

<details><summary>Answer</summary>

**D. No.**

</details>

### 11. dt-31

What does Amazon DynamoDB provide?

<details><summary>Answer</summary>

**D. A fast, highly scalable managed NoSQL database service.**

</details>

### 12. dt-34

Multi-AZ deployment [...] supported for Microsoft SQL Server DB Instances.

<details><summary>Answer</summary>

**A. is not currently.**

</details>

### 13. dt-38

A company is running a batch analysis every hour on their main transactional DB, running on an RDS MySQL instance to populate their central Data Warehouse running on Redshift. During the execution of the batch their transactional applications are very slow. When the batch completes they need to update the top management dashboard with the new data. The dashboard is produced by another system running on-premises that is currently started when a manually-sent email notifies that an update is required. The on-premises system cannot be modified because it is managed by another team. How would you optimize this scenario to solve performance issues and automate the process as much as possible?

<details><summary>Answer</summary>

**A. Replace RDS with Redshift for the batch analysis and SNS to notify the on-premises system to update the dashboard.**

</details>

### 14. q-39

A company maintains a searchable repository of items on its website. The data is stored in an Amazon RDS for MySQL database table that contains more than 10 million rows. The database has 2 TB of General Purpose SSD storage. There are millions of updates against this data every day through the company's website. The company has noticed that some insert operations are taking 10 seconds or longer. The company has determined that the database storage performance is the problem. Which solution addresses this performance issue?

<details><summary>Answer</summary>

**A. Change the storage type to Provisioned IOPS SSD.**

Using Amazon Provisioned IOPS (PIOPS) SSD storage is the best way to solve the performance issue of insert operations taking 10 seconds or longer on an Amazon RDS for MySQL database table with more than 10 million rows and 2 TB of General Purpose SSD storage.  A high-performance storage solution with reliable throughput and minimal latency is PIOPS SSD storage. Workloads like insert operations, which demand high I/O performance, are ideally suited for it.

</details>

### 15. dt-40

You have been asked to build a database warehouse using Amazon Redshift. You know a little about it, including that it is a SQL data warehouse solution, and uses industry standard ODBC and JDBC connections and PostgreSQL drivers. However, you are not sure about what sort of storage it uses for database tables. What sort of storage does Amazon Redshift use for database tables?

<details><summary>Answer</summary>

**C. Columnar data storage.**

</details>

### 16. dt-48 `availability`

You are deploying an application to collect votes for a very popular television show. Millions of users will submit votes using mobile devices. The votes must be collected into a durable, scalable, and highly available data store for real-time public tabulation. Which service should you use?

<details><summary>Answer</summary>

**A. Amazon DynamoDB.**

</details>

### 17. dt-58

You need to import several hundred megabytes of data from a local Oracle database to an Amazon RDS DB instance. What does AWS recommend you use to accomplish this?

<details><summary>Answer</summary>

**C. Oracle Data Pump.**

</details>

### 18. dt-69

Your company is getting ready to do a major public announcement of a social media site on AWS. The website is running on EC2 instances deployed across multiple Availability Zones with a Multi-AZ RDS MySQL Extra Large DB Instance. The site performs a high number of small reads and writes per second and relies on an eventual consistency model. After comprehensive tests you discover that there is read contention on RDS MySQL. Which are the best approaches to meet these requirements? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Deploy ElasticCache in-memory cache running in each Availability Zone.; D. Add an RDS MySQL read replica in each Availability Zone.**

</details>

### 19. dt-71

The SQL Server [...] feature is an efficient means of copying data from a source database to your DB Instance. It writes the data that you specify to a data file, such as an ASCII file.

<details><summary>Answer</summary>

**A. bulk copy.**

</details>

### 20. dt-83

In the Amazon RDS which uses the SQL Server engine, what is the maximum size for a Microsoft SQL Server DB Instance with SQL Server Express edition?

<details><summary>Answer</summary>

**A. 10GB per DB.**

</details>

### 21. dt-92

Is Federated Storage Engine currently supported by Amazon RDS for MySQL?

<details><summary>Answer</summary>

**C. No.**

</details>

### 22. dt-95

Will my standby RDS instance be in the same Region as my primary?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 23. dt-99

What does Amazon RDS stand for?

<details><summary>Answer</summary>

**B. Relational Database Service.**

</details>

### 24. dt-104

You need to set up a high level of security for an Amazon Relational Database Service (RDS) you have just built in order to protect the confidential information stored in it. What are all the possible security groups that RDS uses?

<details><summary>Answer</summary>

**A. DB security groups, VPC security groups, and EC2 security groups.**

</details>

### 25. dt-127

If you are using Amazon RDS Provisioned IOPS storage with MySQL and Oracle database engines, you can scale the throughput of your database Instance by specifying the IOPS rate from [...].

<details><summary>Answer</summary>

**D. 1,000 to 10,000.**

</details>

### 26. dt-132

You are designing a social media site and are considering how to mitigate distributed denial-of service (DDoS) attacks. Which of the below are viable mitigation techniques? (Choose 3 answers)

<details><summary>Answer</summary>

**C. Use an Amazon CloudFront distribution for both static and dynamic content.; D. Use an Elastic Load Balancer with auto scaling groups at the web. App and Amazon Relational Database Service (RDS) tiers.; E. Add alert Amazon CloudWatch to look for high Network in and CPU utilization.**

</details>

### 27. dt-139

You need a persistent and durable storage to trace call activity of an IVR (Interactive Voice Response) system. Call duration is mostly in the 2-3 minutes timeframe. Each traced call can be either active or terminated. An external application needs to know each minute the list of currently active calls, which are usually a few calls/second. Put once per month there is a periodic peak up to 1000 calls/second for a few hours. The system is open 24/7 and any downtime should be avoided. Historical data is periodically archived to files. Cost saving is a priority for this project. What database implementation would better fit this scenario, keeping costs as low as possible?

<details><summary>Answer</summary>

**A. Use RDS Multi-AZ with two tables, one for 'Active calls' and one for 'Terminated calls'. in this way the 'Active calls' table is always small and effective to access.**

</details>

### 28. dt-140

If you have chosen Multi-AZ deployment, in the event of a planned or unplanned outage of your primary DB Instance, Amazon RDS automatically switches to the standby replica. The automatic failover mechanism simply changes the record of the main DB Instance to point to the standby DB Instance.

<details><summary>Answer</summary>

**B. CNAME.**

</details>

### 29. dt-160

A company wants to implement their website in a virtual private cloud (VPC). The web tier will use an Auto Scaling group across multiple Availability Zones (AZs). The database will use Multi-AZ RDS MySQL and should not be publicly accessible. What is the minimum number of subnets that need to be configured in the VPC?

<details><summary>Answer</summary>

**D. 4.**

</details>

### 30. dt-177

Does Amazon RDS allow direct host access via Telnet, Secure Shell (SSH), or Windows Remote Desktop Connection?

<details><summary>Answer</summary>

**B. No.**

</details>

### 31. dt-178 `availability`

A user wants to achieve High Availability with PostgreSQL DB. Which of the below mentioned functionalities helps achieve HA?

<details><summary>Answer</summary>

**A. Multi-AZ.**

</details>

### 32. dt-182

What is the name of licensing model in which I can use your existing Oracle Database licenses to run Oracle deployments on Amazon RDS?

<details><summary>Answer</summary>

**A. Bring Your Own License.**

</details>

### 33. dt-185

Can I initiate a 'forced failover' for my Oracle Multi-AZ DB Instance deployment?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 34. dt-186 `availability`

Amazon RDS provides high availability and failover support for DB instances using [...].

<details><summary>Answer</summary>

**D. Multi-AZ deployments.**

</details>

### 35. q-187 `availability`

A company is developing an ecommerce application that will consist of a load-balanced front end, a container-based application, and a relational database. A solutions architect needs to create a highly available solution that operates with as little manual intervention as possible. Which solutions meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Create an Amazon RDS DB instance in Multi-AZ mode.**

D. Create an Amazon Elastic Container Service (Amazon ECS) cluster with a Fargate launch type to handle the dynamic application load.

</details>

### 36. dt-190

A 3-tier e-commerce web application is current deployed on-premises and will be migrated to AWS for greater scalability and elasticity The web server currently shares read-only data using a network distributed file system The app server tier uses a clustering mechanism for discovery and shared session state that depends on I P multicast The database tier uses shared-storage clustering to provide database fail over capability, and uses several read slaves for scaling Data on all servers and the distributed file system directory is backed up weekly to off-site tapes. Which AWS storage and database architecture meets the requirements of the application?

<details><summary>Answer</summary>

**C. Web servers: store read-only data in S3, and copy from S3 to root volume at boot time. App servers: share state using a combination of DynamoDB and IP unicast. Database: use RDS with multi-AZ deployment and one or more Read Replicas. Backup: web and app servers backed up weekly via AMIs, database backed up via DB snapshots.**

</details>

### 37. dt-195

A company needs to monitor the read and write IOPs metrics for their AWS MySQL RDS instance and send real-time alerts to their operations team. Which AWS services can accomplish this? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Amazon CloudWatch.; E. Amazon Simple Notification Service.**

</details>

### 38. dt-197

What is Oracle SQL Developer?

<details><summary>Answer</summary>

**B. A graphical Java tool distributed without cost by Oracle.**

</details>

### 39. dt-215

In DynamoDB, could you use IAM to grant access to Amazon DynamoDB resources and API actions?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 40. dt-216

The common use cases for DynamoDB Fine-Grained Access Control (FGAC) are cases in which the end user wants [...].

<details><summary>Answer</summary>

**D. to read or modify the table directly, without a middle-tier service.**

</details>

### 41. dt-222

True or False: The new DB Instance that is created when you promote a Read Replica retains the backup window period.

<details><summary>Answer</summary>

**A. True.**

</details>

### 42. q-228

A company has an API that receives real-time data from a fleet of monitoring devices. The API stores this data in an Amazon RDS DB instance for later analysis. The amount of data that the monitoring devices send to the API fluctuates. During periods of heavy traffic, the API often returns timeout errors. After an inspection of the logs, the company determines that the database is not capable of processing the volume of write traffic that comes from the API. A solutions architect must minimize the number of connections to the database and must ensure that data is not lost during periods of heavy traffic. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Modify the API to write incoming data to an Amazon Simple Queue Service (Amazon SQS) queue. Use an AWS Lambda function that Amazon SQS invokes to write data from the queue to the database.**

Amazon SQS: SQS is a fully managed message queuing service that decouples the components of a cloud application. It acts as a buffer between the API and the database, allowing for better handling of varying write traffic.  AWS Lambda: Using Lambda to process the data from the SQS queue helps in efficiently managing the connection to the database. Lambda functions can be scaled automatically based on the incoming workload.

</details>

### 43. dt-229

While launching an RDS DB instance, on which page I can select the Availability Zone?

<details><summary>Answer</summary>

**D. ADDITIONAL CONFIGURATION.**

</details>

### 44. q-229

A company manages its own Amazon EC2 instances that run MySQL databases. The company is manually managing replication and scaling as demand increases or decreases. The company needs a new solution that simplifies the process of adding or removing compute capacity to or from its database tier as needed. The solution also must offer improved performance, scaling, and durability with minimal effort from operations. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Migrate the databases to Amazon Aurora Serverless for Aurora MySQL.**

Amazon Aurora Serverless: Aurora Serverless is an on-demand, auto-scaling configuration for Amazon Aurora. It automatically adjusts the database capacity based on actual consumption, enabling seamless scaling without manual intervention. It is a fully managed service, reducing operational overhead.

</details>

### 45. dt-233

Can I use Provisioned IOPS with VPC?

<details><summary>Answer</summary>

**D. Yes for all RDS instances.**

</details>

### 46. q-236 `availability`

A company has a three-tier application for image sharing. The application uses an Amazon EC2 instance for the front-end layer, another EC2 instance for the application layer, and a third EC2 instance for a MySQL database. A solutions architect must design a scalable and highly available solution that requires the least amount of change to the application. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use load-balanced Multi-AZ AWS Elastic Beanstalk environments for the front-end layer and the application layer. Move the database to an Amazon RDS Multi-AZ DB instance. Use Amazon S3 to store and serve users’ images.**

AWS Elastic Beanstalk provides an easy way to deploy and manage applications. By using Multi-AZ environments, the front-end and application layers can automatically scale and provide high availability across multiple Availability Zones (AZs). Amazon RDS Multi-AZ DB Instance: Moving the database to an Amazon RDS Multi-AZ DB instance ensures high availability and automatic failover in the event of a failure in one Availability Zone. Amazon S3 for Storing and Serving Images: Using Amazon S3 for storing and serving users' images is a scalable and cost-effective solution. S3 is designed for high durability and availability, making it suitable for serving static content like images.

</details>

### 47. q-241 `least-ops`

An online learning company is migrating to the AWS Cloud. The company maintains its student records in a PostgreSQL database. The company needs a solution in which its data is available and online across multiple AWS Regions at all times. Which solution will meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Migrate the PostgreSQL database to an Amazon RDS for PostgreSQL DB instance. Create a read replica in another Region.**

Amazon RDS for PostgreSQL allows you to create read replicas in different AWS Regions. This provides cross-Region availability and redundancy. Additionally, it allows you to offload read traffic from the primary database.

</details>

### 48. gh-241 `least-ops`

n online learning company is migrating to the AWS Cloud. The company maintains its student records in a PostgreSQL database. The company needs a solution in which its data is available and online across multiple AWS Regions at all times.
Which solution will meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Migrate the PostgreSQL database to an Amazon RDS for PostgreSQL DB instance. Create a read replica in another Region.**

Amazon RDS for PostgreSQL allows you to create read replicas in different AWS Regions. This provides cross-Region availability and redundancy. Additionally, it allows you to offload read traffic from the primary database.

</details>

### 49. dt-244

Your customer wishes to deploy an enterprise application to AWS which will consist of several web servers, several application servers and a small (50GB) Oracle database information is stored, both in the database and the file systems of the various servers. The backup system must support database recovery whole server and whole disk restores, and individual file restores with a recovery time of no more than two hours. They have chosen to use RDS Oracle as the database. Which backup architecture will meet these requirements?

<details><summary>Answer</summary>

**A. Backup RDS using automated daily DB backups Backup the EC2 instances using AMIs and supplement with file-level backup to S3 using traditional enterprise backup software to provide file level restore.**

</details>

### 50. q-244 `availability`

A company is using a content management system that runs on a single Amazon EC2 instance. The EC2 instance contains both the web server and the database software. The company must make its website platform highly available and must enable the website to scale to meet user demand. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Move the database to Amazon Aurora with a read replica in another Availability Zone. Create an Amazon Machine Image (AMI) from the EC2 instance. Configure an Application Load Balancer in two Availability Zones. Attach an Auto Scaling group that uses the AMI across two Availability Zones.**

This option provides both high availability and scalability. Using Amazon Aurora with a read replica in another Availability Zone ensures data redundancy and failover capabilities. Configuring an Application Load Balancer across two Availability Zones and using Auto Scaling allows for scalability.

</details>

### 51. dt-246

Is the SQL Server Audit feature supported in the Amazon RDS SQL Server engine?

<details><summary>Answer</summary>

**B. No.**

</details>

### 52. dt-252

What are the two types of licensing options available for using Amazon RDS for Oracle?

<details><summary>Answer</summary>

**B. BYOL and License Included.**

</details>

### 53. dt-258

[...] embodies the 'share-nothing' architecture and essentially involves breaking a large database into several smaller databases. Common ways to split a database include: 1. Splitting tables that are not joined in the same query onto different hosts or 2. Duplicating a table across multiple hosts and then using a hashing algorithm to determine which host receives a given update.

<details><summary>Answer</summary>

**A. $harding.**

</details>

### 54. dt-260

Your company plans to host a large donation website on Amazon Web Services (AWS). You anticipate a large and undetermined amount of traffic that will create many database writes. To be certain that you do not drop any writes to a database hosted on AWS. Which service should you use?

<details><summary>Answer</summary>

**B. Amazon Simple Queue Service (SOS) for capturing the writes and draining the queue to write to the database.**

</details>

### 55. dt-262 `availability`

You are migrating a legacy client-server application to AWS. The application responds to a specific DNS domain (e.g. <www.example.com>) and has a 2-tier architecture, with multiple application servers and a database server. Remote clients use TCP to connect to the application servers. The application servers need to know the IP address of the clients in order to function properly and are currently taking that information from the TCP socket. A Multi-AZ RDS MySQL instance will be used for the database. During the migration you can change the application code, but you have to file a change request. How would you implement the architecture on AWS in order to maximize scalability and high availability?

<details><summary>Answer</summary>

**D. File a change request to implement Proxy Protocol support in the application. Use an ELB with a TCP Listener and Proxy Protocol enabled to distribute load on two application servers in different AZs.**

</details>

### 56. dt-265

You have just set up a large site for a client which involved a huge database which you set up with Amazon RDS to run as a Multi-AZ deployment. You now start to worry about what will happen if the database instance fails. Which statement best describes how this database will function if there is a database failure?

<details><summary>Answer</summary>

**A. Updates to your DB Instance are synchronously replicated across Availability Zones to the standby in order to keep both in sync and protect your latest database updates against DB Instance failure.**

</details>

### 57. q-268

A gaming company has a web application that displays scores. The application runs on Amazon EC2 instances behind an Application Load Balancer. The application stores data in an Amazon RDS for MySQL database. Users are starting to experience long delays and interruptions that are caused by database read performance. The company wants to improve the user experience while minimizing changes to the application’s architecture. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**Put Amazon ElastiCache between the application and the Amazon RDS for MySQL database so repeated score reads are served from the cache instead of the database.**

The bottleneck is read volume against the MySQL database, so the fix has to take reads off it. ElastiCache serves the hot, frequently requested score data from memory, which cuts both the delays and the load on RDS without re-platforming the application. RDS Proxy only manages and reuses database connections - useful when an application opens too many connections or needs faster failover, but it adds no read capacity. Migrating to Lambda or to DynamoDB would be a far larger change than the question allows.

</details>

### 58. q-269

An ecommerce company has noticed performance degradation of its Amazon RDS based web application. The performance degradation is attributed to an increase in the number of read-only SQL queries triggered by business analysts. A solutions architect needs to solve the problem with minimal changes to the existing web application. What should the solutions architect recommend?

<details><summary>Answer</summary>

**C. Create a read replica of the primary database and have the business analysts run their queries.**

Creating a read replica is a common approach to offload read-only queries from the primary database, improving overall performance. A read replica is an asynchronous copy of the primary database that allows for read-only operations.  Read replicas can be transparently used by the web application without requiring changes to the application logic. Business analysts can direct their read-only queries to the read replica, reducing the load on the primary database.

</details>

### 59. q-273

A rapidly growing ecommerce company is running its workloads in a single AWS Region. A solutions architect must create a disaster recovery (DR) strategy that includes a different AWS Region. The company wants its database to be up to date in the DR Region with the least possible latency. The remaining infrastructure in the DR Region needs to run at reduced capacity and must be able to scale up if necessary. Which solution will meet these requirements with the LOWEST recovery time objective (RTO)?

<details><summary>Answer</summary>

**B. Use an Amazon Aurora global database with a warm standby deployment.**

Amazon Aurora supports a global database feature that allows you to create read replicas in multiple AWS Regions. In a warm standby deployment, you can have a read replica in the DR Region that stays warm, meaning it is ready to take over in case of a failover.

</details>

### 60. gh-273

273Topic 1
A rapidly growing ecommerce company is running its workloads in a single AWS Region. A solutions architect must create a disaster recovery (DR) strategy that includes a different AWS Region. The company wants its database to be up to date in the DR Region with the least possible latency. The remaining infrastructure in the DR Region needs to run at reduced capacity and must be able to scale up if necessary.
Which solution will meet these requirements with the LOWEST recovery time objective (RTO)?

<details><summary>Answer</summary>

**B. Use an Amazon Aurora global database with a warm standby deployment.**

Amazon Aurora supports a global database feature that allows you to create read replicas in multiple AWS Regions.
In a warm standby deployment, you can have a read replica in the DR Region that stays warm, meaning it is ready to take over in case of a failover.

</details>

### 61. q-279

A company has an application that is backed by an Amazon DynamoDB table. The company’s compliance requirements specify that database backups must be taken every month, must be available for 6 months, and must be retained for 7 years. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an AWS Backup plan to back up the DynamoDB table on the first day of each month. Specify a lifecycle policy that transitions the backup to cold storage after 6 months. Set the retention period for each backup to 7 years.**

AWS Backup will automatically take full backups of the DynamoDB table on the schedule defined in the backup plan (the first of each month). The lifecycle policy can transition backups to cold storage after 6 months, meeting that requirement. Setting a 7-year retention period in the backup plan will ensure each backup is retained for 7 years as required. AWS Backup manages the backup jobs and lifecycle policies, requiring no custom scripting or management.

</details>

### 62. dt-281

Read Replicas require a transactional storage engine and are only supported for the [...] storage engine.

<details><summary>Answer</summary>

**C. InnoDB.**

</details>

### 63. q-281

A company runs a fleet of web servers using an Amazon RDS for PostgreSQL DB instance. After a routine compliance check, the company sets a standard that requires a recovery point objective (RPO) of less than 1 second for all its production databases. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Enable a Multi-AZ deployment for the DB instance.**

A Multi-AZ (Availability Zone) deployment for Amazon RDS provides high availability and failover support for DB instances. In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone.

</details>

### 64. dt-284

Can I initiate a 'forced failover' for my MySQL Multi-AZ DB Instance deployment?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 65. dt-289

A gaming company comes to you and asks you to build them infrastructure for their site. They are not sure how big they will be as with all start ups they have limited money and big ideas. What they do tell you is that if the game becomes successful, like one of their previous games, it may rapidly grow to millions of users and generate tens (or even hundreds) of thousands of writes and reads per second. After considering all of this, you decide that they need a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. Which of the following databases do you think would best fit their needs?

<details><summary>Answer</summary>

**A. Amazon DynamoDB.**

</details>

### 66. dt-294

In the HQ region you run an hourly batch process reading data from every region to compute cross regional reports that are sent by email to all offices this batch process must be completed as fast as possible to quickly optimize logistics how do you build the database architecture in order to meet the requirements'?

<details><summary>Answer</summary>

**A. For each regional deployment, use RDS MySQL with a master in the region and a read replica in the HQ region.**

</details>

### 67. dt-308

When automatic failover occurs, Amazon RDS will emit a DB Instance event to inform you that automatic failover occurred. You can use the [...] to return information about events related to your DB Instance.

<details><summary>Answer</summary>

**C. DescribeEvents.**

</details>

### 68. q-314

A company has an on-premises MySQL database used by the global sales team with infrequent access patterns. The sales team requires the database to have minimal downtime. A database administrator wants to migrate this database to AWS without selecting a particular instance type in anticipation of more users in the future. Which service should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Amazon Aurora Serverless for MySQL**

Amazon Aurora Serverless: Aurora Serverless is a fully managed, on-demand, and auto-scaling relational database engine provided by AWS. It is suitable for infrequent access patterns and allows the database to automatically start up, shut down, and scale capacity based on actual usage.

</details>

### 69. dt-315

You have just been given a scope for a new client who has an enormous amount of data (petabytes) that he constantly needs analysed. Currently he is paying a huge amount of money for a data warehousing company to do this for him and is wondering if AWS can provide a cheaper solution. Do you think AWS has a solution for this?

<details><summary>Answer</summary>

**C. Yes. Amazon Redshift.**

</details>

### 70. dt-323

In the Amazon RDS Oracle DB engine, the Database Diagnostic Pack and the Database Tuning Pack are only available with [...].

<details><summary>Answer</summary>

**C. Oracle Enterprise Edition.**

</details>

### 71. dt-324

Will my standby RDS instance be in the same Availability Zone as my primary?

<details><summary>Answer</summary>

**D. No.**

</details>

### 72. dt-325

An administrator is using Amazon CloudFormation to deploy a three tier web application that consists of a web tier and application tier that will utilize Amazon DynamoDB for storage. When creating the CloudFormation template, which of the following would allow the application instance access to the DynamoDB tables without exposing API credentials?

<details><summary>Answer</summary>

**C. Create an Identity and Access Management Role that has the required permissions to read and write from the required DynamoDB table and reference the Role in the instance profile property of the application instance.**

</details>

### 73. dt-335

How would you improve page load times for your users? (Choose 3 answers)

<details><summary>Answer</summary>

**B. Add an Amazon ElastiCache caching layer to your application for storing sessions and frequent DB queries.; C. Configure Amazon CloudFront dynamic content support to enable caching of re-usable content from your site.; D. Switch Amazon RDS database to the high memory extra large Instance type.**

</details>

### 74. dt-336

Typically, you want your application to check whether a request generated an error before you spend any time processing results. The easiest way to find out if an error occurred is to look for an [...] node in the response from the Amazon RDS API.

<details><summary>Answer</summary>

**B. error.**

</details>

### 75. q-337

A company has deployed a web application on AWS. The company hosts the backend database on Amazon RDS for MySQL with a primary DB instance and five read replicas to support scaling needs. The read replicas must lag no more than 1 second behind the primary DB instance. The database routinely runs scheduled stored procedures. As traffic on the website increases, the replicas experience additional lag during periods of peak load. A solutions architect must reduce the replication lag as much as possible. The solutions architect must minimize changes to the application code and must minimize ongoing operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Migrate the database to Amazon Aurora MySQL. Replace the read replicas with Aurora Replicas, and configure Aurora Auto Scaling. Replace the stored procedures with Aurora MySQL native functions.**

Amazon Aurora MySQL: Aurora Replicas in Amazon Aurora MySQL are designed to have minimal replication lag compared to traditional MySQL read replicas. Aurora is built for high performance and low replication lag, making it a suitable choice for reducing lag in read replicas.  Aurora Auto Scaling: Aurora Auto Scaling allows you to automatically adjust the number of Aurora Replicas based on actual application usage. This ensures that you have the right amount of read capacity during periods of peak load, minimizing replication lag.

</details>

### 76. q-338 `cost`

A solutions architect must create a disaster recovery (DR) plan for a high-volume software as a service (SaaS) platform. All data for the platform is stored in an Amazon Aurora MySQL DB cluster. The DR plan must replicate data to a secondary AWS Region. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Set up an Aurora global database for the DB cluster and, once setup is complete, remove the DB instance from the secondary Region, leaving a headless secondary cluster.**

Aurora global database replication happens in the shared storage layer, not through a database instance, so data keeps arriving in the secondary Region even when that cluster has no instance running. For a plan that only has to hold a replica of the data, this is the cheapest shape: you pay for replicated storage and cross-Region replication traffic but no idle compute. When you need to recover, you add an instance to the secondary cluster and promote it. Keeping a DB instance running in the secondary Region also works, but it costs more, so it loses on the MOST cost-effectively test.

</details>

### 77. q-340

A media company hosts its website on AWS. The website application’s architecture includes a fleet of Amazon EC2 instances behind an Application Load Balancer (ALB) and a database that is hosted on Amazon Aurora. The company’s cybersecurity team reports that the application is vulnerable to SQL injection. How should the company resolve this issue?

<details><summary>Answer</summary>

**A. Use AWS WAF in front of the ALB. Associate the appropriate web ACLs with AWS WAF.**

AWS WAF (Web Application Firewall): AWS WAF is designed to protect web applications from common web exploits, including SQL injection. It allows you to create web access control lists (web ACLs) to define rules that filter and monitor HTTP traffic to your application.  Associating Web ACLs with AWS WAF: By using AWS WAF in front of the ALB, you can define rules to block or allow web requests based on conditions that you specify. This includes protection against SQL injection attempts. AWS WAF provides a range of conditions and rulesets that you can use to mitigate common security threats.

</details>

### 78. dt-341

You are building infrastructure for a data warehousing solution and an extra request has come through that there will be a lot of business reporting queries running all the time and you are not sure if your current DB instance will be able to handle it. What would be the best solution for this?

<details><summary>Answer</summary>

**B. Read Replicas.**

</details>

### 79. q-343 `least-ops`

A solutions architect is designing a company’s disaster recovery (DR) architecture. The company has a MySQL database that runs on an Amazon EC2 instance in a private subnet with scheduled backup. The DR design needs to include multiple AWS Regions. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Migrate the MySQL database to an Amazon Aurora global database. Host the primary DB cluster in the primary Region. Host the secondary DB cluster in the DR Region.**

</details>

### 80. dt-345

After you recommend Amazon Redshift to a client as an alternative solution to paying data warehouses to analyze his data, your client asks you to explain why you are recommending Redshift. Which of the following would be a reasonable response to his request?

<details><summary>Answer</summary>

**D. All answers listed are a reasonable response to his question.**

</details>

### 81. dt-347

Does Amazon DynamoDB support both increment and decrement atomic operations?

<details><summary>Answer</summary>

**C. Yes, both increment and decrement operations.**

</details>

### 82. q-349 `security`

A company stores confidential data in an Amazon Aurora PostgreSQL database in the ap-southeast-3 Region. The database is encrypted with an AWS Key Management Service (AWS KMS) customer managed key. The company was recently acquired and must securely share a backup of the database with the acquiring company’s AWS account in ap-southeast-3. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create a database snapshot. Add the acquiring company’s AWS account to the KMS key policy. Share the snapshot with the acquiring company’s AWS account.**

sharing encrypted snapshots involves granting permission not only on the snapshot itself but also on the underlying AWS Key Management Service (KMS) key used for encryption. By adding the acquiring company's AWS account to the KMS key policy, you ensure that they have the necessary permissions to decrypt and access the snapshot. Sharing the snapshot with the acquiring company's AWS account completes the process, allowing them to restore the database from the shared snapshot.

</details>

### 83. q-350 `availability`

A company uses a 100 GB Amazon RDS for Microsoft SQL Server Single-AZ DB instance in the us-east-1 Region to store customer transactions. The company needs high availability and automatic recovery for the DB instance. The company must also run reports on the RDS database several times a year. The report process causes transactions to take longer than usual to post to the customers’ accounts. The company needs a solution that will improve the performance of the report process. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Modify the DB instance from a Single-AZ DB instance to a Multi-AZ deployment.**

Enabling Multi-AZ deployment provides high availability by replicating the database to a standby instance in another Availability Zone. This helps in automatic failover and recovery in case of a primary instance failure. C. Create a read replica of the DB instance in a different Availability Zone. Point all requests for reports to the read replica:  By creating a read replica in a different Availability Zone, you offload the reporting workload from the primary instance, reducing the impact on transaction processing. Read replicas can be used to scale read-heavy workloads and improve overall performance.

</details>

### 84. q-353 `cost` `availability`

A company hosts a three-tier web application on Amazon EC2 instances in a single Availability Zone. The web application uses a self-managed MySQL database that is hosted on an EC2 instance to store data in an Amazon Elastic Block Store (Amazon EBS) volume. The MySQL database currently uses a 1 TB Provisioned IOPS SSD (io2) EBS volume. The company expects traffic of 1,000 IOPS for both reads and writes at peak traffic. The company wants to minimize any disruptions, stabilize performance, and reduce costs while retaining the capacity for double the IOPS. The company wants to move the database tier to a fully managed solution that is highly available and fault tolerant. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use a Multi-AZ deployment of an Amazon RDS for MySQL DB instance with a General Purpose SSD (gp2) EBS volume.**

</details>

### 85. q-354

A company hosts a serverless application on AWS. The application uses Amazon API Gateway, AWS Lambda, and an Amazon RDS for PostgreSQL database. The company notices an increase in application errors that result from database connection timeouts during times of peak traffic or unpredictable traffic. The company needs a solution that reduces the application failures with the least amount of change to the code. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Enable RDS Proxy on the RDS DB instance.**

RDS Proxy is a fully managed, highly available database proxy that can handle database connections for serverless and highly scalable applications. It helps manage database connections efficiently, reducing issues related to connection timeouts and errors.

</details>

### 86. dt-359

After setting up several database instances in Amazon Relational Database Service (Amazon RDS) you decide that you need to track the performance and health of your databases. How can you do this?

<details><summary>Answer</summary>

**C. All of the items listed will track the performance and health of a database.**

</details>

### 87. q-361 `least-ops`

A company hosts a multiplayer gaming application on AWS. The company wants the application to read data with sub-millisecond latency and run one-time queries on historical data. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Use Amazon DynamoDB with DynamoDB Accelerator (DAX) for data that is frequently accessed. Export the data to an Amazon S3 bucket by using DynamoDB table export. Run one-time queries on the data in Amazon S3 by using Amazon Athena.**

Amazon DynamoDB with DynamoDB Accelerator (DAX):  DynamoDB is a highly scalable and low-latency NoSQL database, suitable for frequently accessed data. DynamoDB Accelerator (DAX) is a caching layer that provides sub-millisecond read latencies for DynamoDB. Export Data to Amazon S3:  Use DynamoDB table export to periodically export historical data to an Amazon S3 bucket. This allows you to store historical data in a cost-effective manner while still benefiting from DynamoDB for frequently accessed data. Amazon Athena for One-time Queries:  Amazon Athena allows you to run SQL queries directly on data stored in Amazon S3. By using Athena, you can perform one-time queries on the historical data without the need to manage a separate database.

</details>

### 88. q-365

A company runs a web application that is backed by Amazon RDS. A new database administrator caused data loss by accidentally editing information in a database table. To help recover from this type of incident, the company wants the ability to restore the database to its state from 5 minutes before any change within the last 30 days. Which feature should the solutions architect include in the design to meet this requirement?

<details><summary>Answer</summary>

**C. Automated backups**

Amazon RDS (Relational Database Service) can automatically create backups of your database every day. These backups are like snapshots of your entire database, capturing all the data. They happen automatically, so you don't have to remember to do it. You can decide how long you want to keep these backup snapshots. For example, you might choose to keep them for up to 35 days. This is like saying, "I want to keep the pictures of my database for the last 35 days."

</details>

### 89. q-372 `cost` `availability`

A company wants to migrate an Oracle database to AWS. The database consists of a single table that contains millions of geographic information systems (GIS) images that are high resolution and are identified by a geographic code. When a natural disaster occurs, tens of thousands of images get updated every few minutes. Each geographic code has a single image or row that is associated with it. The company wants a solution that is highly available and scalable during such events. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Store the images in Amazon S3 buckets. Use Amazon DynamoDB with the geographic code as the key and the image S3 URL as the value.**

Explanation: Each geographic code maps to a single image/row — a simple key-value access pattern — and updates arrive in spiky bursts during disasters. DynamoDB is built for exactly that: high, unpredictable write throughput with simple key lookups, scaling more cost-effectively than a relational Oracle-on-RDS table for this access pattern.

</details>

### 90. q-376 `least-ops`

A company has launched an Amazon RDS for MySQL DB instance. Most of the connections to the database come from serverless applications. Application traffic to the database changes significantly at random intervals. At times of high demand, users report that their applications experience database connection rejection errors. Which solution will resolve this issue with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create a proxy in RDS Proxy. Configure the users’ applications to use the DB instance through RDS Proxy.**

RDS Proxy is a fully managed, highly available database proxy for Amazon RDS that makes applications more scalable, more resilient to database failures, and more secure. It automatically routes database traffic to the appropriate DB instance, handling connection pooling and failover.

</details>

### 91. q-378

A company is developing a real-time multiplayer game that uses UDP for communications between the client and servers in an Auto Scaling group. Spikes in demand are anticipated during the day, so the game server platform must adapt accordingly. Developers want to store gamer scores and other non-relational data in a database solution that will scale without intervention. Which solution should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Use a Network Load Balancer for traffic distribution and Amazon DynamoDB on-demand for data storage.**

Think of an NLB like a traffic cop for your game. It helps distribute and manage the incoming traffic from players to your game servers. It ensures that the load is balanced across your servers, which is crucial for handling the expected spikes in demand. DynamoDB is a type of database that can store data for your game, such as gamer scores. "On-demand" means that DynamoDB automatically scales to handle the amount of data and traffic your game is experiencing.

</details>

### 92. q-379

A company hosts a frontend application that uses an Amazon API Gateway API backend that is integrated with AWS Lambda. When the API receives requests, the Lambda function loads many libraries. Then the Lambda function connects to an Amazon RDS database, processes the data, and returns the data to the frontend application. The company wants to ensure that response latency is as low as possible for all its users with the fewest number of changes to the company's operations. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure provisioned concurrency for the Lambda function that handles the requests.**

Provisioned Concurrency: Provisioned concurrency allows you to pre-warm a specific number of instances of your Lambda function. This ensures that there are already instances available to handle incoming requests, reducing the cold start latency. Since the Lambda function loads many libraries, reducing cold start latency is crucial for optimizing response time.

</details>

### 93. dt-380

A read only news reporting site with a combined web and application tier and a database tier that receives large and unpredictable traffic demands must be able to respond to these traffic fluctuations automatically. What AWS services should be used meet these requirements?

<details><summary>Answer</summary>

**A. Stateless instances for the web and application tier synchronized using Elasticache Memcached in an autoscaimg group monitored with CloudWatch. And RDSwith read replicas.**

</details>

### 94. q-381

A company hosts a three-tier web application that includes a PostgreSQL database. The database stores the metadata from documents. The company searches the metadata for key terms to retrieve documents that the company reviews in a report each month. The documents are stored in Amazon S3. The documents are usually written only once, but they are updated frequently. The reporting process takes a few hours with the use of relational queries. The reporting process must not prevent any document modifications or the addition of new documents. A solutions architect needs to implement a solution to speed up the reporting process. Which solution will meet these requirements with the LEAST amount of change to the application code?

<details><summary>Answer</summary>

**B. Set up a new Amazon Aurora PostgreSQL DB cluster that includes an Aurora Replica. Issue queries to the Aurora Replica to generate the reports.**

Amazon Aurora PostgreSQL DB cluster that includes an Aurora Replica. Issue queries to the Aurora Replica to generate the reports) is the best option for speeding up the reporting process for a three-tier web application that includes a PostgreSQL database storing metadata from documents, while not impacting document modifications or additions, with the least amount of change to the application code.

</details>

### 95. dt-382

What does Amazon ElastiCache provide?

<details><summary>Answer</summary>

**C. A managed In-memory cache service.**

</details>

### 96. dt-386

Your company is in the process of developing a next generation pet collar that collects biometric information to assist families with promoting healthy lifestyles for their pets. Each collar will push 30kb of biometric data in JSON format every 2 seconds to a collection platform that will process and analyze the data providing health trending information back to the pet owners and veterinarians via a web portal. Management has tasked you to architect the collection platform ensuring the following requirements are met. Provide the ability for real-time analytics of the inbound biometric data. Ensure processing of the biometric data is highly durable, elastic and parallel. The results of the analytic processing should be persisted for data mining. Which architecture outlined below will meet the initial requirements for the collection platform?

<details><summary>Answer</summary>

**B. Utilize Amazon Kinesis to collect the inbound sensor data, analyze the data with Kinesis clients and save the results to a Redshift cluster using EMR.**

</details>

### 97. q-386

An ecommerce company is running a multi-tier application on AWS. The front-end and backend tiers both run on Amazon EC2, and the database runs on Amazon RDS for MySQL. The backend tier communicates with the RDS instance. There are frequent calls to return identical datasets from the database that are causing performance slowdowns. Which action should be taken to improve the performance of the backend?

<details><summary>Answer</summary>

**B. Implement Amazon ElastiCache to cache the large datasets.**

Amazon ElastiCache: Amazon ElastiCache is a fully managed in-memory caching service. By implementing ElastiCache, you can cache frequently accessed data in-memory, reducing the need to make repeated calls to the database. This helps improve the performance of your application by serving data directly from the cache instead of querying the database every time.  Caching Large Datasets: In scenarios where identical datasets are frequently requested, caching the results in ElastiCache can significantly reduce the load on the database and improve response times for subsequent requests. It is particularly effective for read-heavy workloads where the data does not change frequently.

</details>

### 98. q-389

A company has a large dataset for its online advertising business stored in an Amazon RDS for MySQL DB instance in a single Availability Zone. The company wants business reporting queries to run without impacting the write operations to the production DB instance. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Deploy RDS read replicas to process the business reporting queries.**

Amazon RDS provides the ability to create read replicas of a source DB instance. Read replicas can be used to offload read traffic from the primary (write) DB instance, allowing you to scale read operations horizontally. This is particularly useful for scenarios where you want to run reporting queries without affecting the write performance of the production DB instance.

</details>

### 99. dt-390

You have recently joined a startup company building sensors to measure street noise and air quality in urban areas. The company has been running a pilot deployment of around 100 sensors for 3 months. Each sensor uploads 1KB of sensor data every minute to a backend hosted on AWS. During the pilot, you measured a peak of 10 IOPS on the database, and you stored an average of 3GB of sensor data per month in the database. The current deployment consists of a load-balanced auto scaled Ingestion layer using EC2 instances and a PostgreSQL RDS database with 500GB standard storage. The pilot is considered a success and your CEO has managed to get the attention of some potential investors. The business plan requires a deployment of at least 100K sensors which needs to be supported by the backend. You also need to store sensor data for at least two years to be able to compare year over year improvements. To secure funding, you have to make sure that the platform meets these requirements and leaves room for further scaling. Which setup will meet the requirements?

<details><summary>Answer</summary>

**C. Replace the RDS instance with a 6 node Redshift cluster with 96TB of storage.**

</details>

### 100. q-392

A company wants to deploy a new public web application on AWS. The application includes a web server tier that uses Amazon EC2 instances. The application also includes a database tier that uses an Amazon RDS for MySQL DB instance. The application must be secure and accessible for global customers that have dynamic IP addresses. How should a solutions architect configure the security groups to meet these requirements?

<details><summary>Answer</summary>

**A. Configure the security group for the web servers to allow inbound traffic on port 443 from 0.0.0.0/0. Configure the security group for the DB instance to allow inbound traffic on port 3306 from the security group of the web servers.**

</details>

### 101. q-394

A company is running a multi-tier ecommerce web application in the AWS Cloud. The application runs on Amazon EC2 instances with an Amazon RDS for MySQL Multi-AZ DB instance. Amazon RDS is configured with the latest generation DB instance with 2,000 GB of storage in a General Purpose SSD (gp3) Amazon Elastic Block Store (Amazon EBS) volume. The database performance affects the application during periods of high demand. A database administrator analyzes the logs in Amazon CloudWatch Logs and discovers that the application performance always degrades when the number of read and write IOPS is higher than 20,000. What should a solutions architect do to improve the application performance?

<details><summary>Answer</summary>

**C. Replace the volume with a Provisioned IOPS SSD (io2) volume.**

io2 volumes are designed for high-performance, low-latency applications such as databases. Provisioned IOPS allows you to specify the amount of IOPS the volume needs, ensuring consistent performance. For applications with high demand and where consistent performance is crucial, io2 volumes provide better control over IOPS compared to gp3 volumes.

</details>

### 102. dt-401

You are running a successful multitier web application on AWS and your marketing department has asked you to add a reporting tier to the application. The reporting tier will aggregate and publish status reports every 30 minutes from user-generated information that is being stored in your web application s database. You are currently running a Multi-AZ RDS MySQL instance for the database tier. You also have implemented Elasticache as a database caching layer between the application tier and database tier. Please select the answer that will allow you to successful ly implement the reporting tier with as little impact as possible to your database.

<details><summary>Answer</summary>

**C. Launch a RDS Read Replica connected to your Multi-AZ master database and generate reports by querying the Read Replica.**

</details>

### 103. q-401 `availability`

A company wants to use the AWS Cloud to make an existing application highly available and resilient. The current version of the application resides in the company's data center. The application recently experienced data loss after a database server crashed because of an unexpected power outage. The company needs a solution that avoids any single points of failure. The solution must give the application the ability to scale to meet user demand. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application servers by using Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Use an Amazon RDS DB instance in a Multi-AZ configuration.**

Auto Scaling Across Multiple Availability Zones: Deploying application servers using EC2 instances in an Auto Scaling group across multiple Availability Zones (AZs) helps avoid a single point of failure. If one AZ experiences an issue, the application can continue to operate in another AZ.

</details>

### 104. dt-403

MySQL installations default to port [...].

<details><summary>Answer</summary>

**A. 3306.**

</details>

### 105. q-406

A solutions architect is designing a two-tiered architecture that includes a public subnet and a database subnet. The web servers in the public subnet must be open to the internet on port 443. The Amazon RDS for MySQL DB instance in the database subnet must be accessible only to the web servers on port 3306. Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Create a security group for the web servers in the public subnet. Add a rule to allow traffic from 0.0.0.0/0 on port 443.**

D. Create a security group for the DB instance. Add a rule to allow traffic from the web servers’ security group on port 3306.  This allows inbound traffic from the internet on port 443 to the web servers.  This ensures that the RDS instance is accessible only from the web servers in the public subnet.

</details>

### 106. dt-410

True or False: When using IAM to control access to your RDS resources, the key names that can be used are case sensitive. For example, aws: CurrentTime is NOT equivalent to AWS: currenttime.

<details><summary>Answer</summary>

**B. False.**

</details>

### 107. q-411

A company has a web application with sporadic usage patterns. There is heavy usage at the beginning of each month, moderate usage at the start of each week, and unpredictable usage during the week. The application consists of a web server and a MySQL database server running inside the data center. The company would like to move the application to the AWS Cloud, and needs to select a cost-effective database platform that will not require database modifications. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. MySQL-compatible Amazon Aurora Serverless**

Aurora Serverless is a serverless option for MySQL-compatible databases. It automatically adjusts the database capacity based on actual usage, making it suitable for sporadic usage patterns. It is MySQL-compatible, so it won't require significant database modifications.

</details>

### 108. q-416

A rapidly growing global ecommerce company is hosting its web application on AWS. The web application includes static content and dynamic content. The website stores online transaction processing (OLTP) data in an Amazon RDS database The website’s users are experiencing slow page loads. Which combination of actions should a solutions architect take to resolve this issue? (Choose two.)

<details><summary>Answer</summary>

**B. Set up an Amazon CloudFront distribution.**

D. Create a read replica for the RDS DB instance.  Amazon CloudFront is a content delivery network (CDN) that can improve the performance of a website by caching static content closer to the users. This reduces latency and improves page load times. Configure CloudFront to distribute static content such as images, stylesheets, and JavaScript files. This will offload the serving of static assets from the web servers, improving overall website performance.  Creating a read replica for the Amazon RDS database allows you to offload read traffic from the primary database, improving the overall database performance.

</details>

### 109. q-420 `availability`

A company wants to use an Amazon RDS for PostgreSQL DB cluster to simplify time-consuming database administrative tasks for production database workloads. The company wants to ensure that its database is highly available and will provide automatic failover support in most scenarios in less than 40 seconds. The company wants to offload reads off of the primary instance and keep costs as low as possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use an Amazon RDS Multi-AZ DB cluster deployment. Point the read workload to the reader endpoint.**

An RDS Multi-AZ DB cluster runs one writer instance and two standby instances spread across three Availability Zones. The standbys are readable, so pointing the read workload at the cluster reader endpoint takes those queries off the writer with nothing extra to provision. Replication to the standbys is faster than in a plain Multi-AZ instance deployment, and failover typically completes in under 35 seconds, which satisfies the under-40-second requirement. A Multi-AZ instance deployment would meet the availability goal but its single standby cannot serve reads, so you would have to add and pay for separate read replicas.

</details>

### 110. dt-421

An International company has deployed a multi-tier web application that relies on DynamoDB in a single region. For regulatory reasons they need disaster recovery capability in a separate region with a Recovery Time Objective of 2 hours and a Recovery Point Objective of 24 hours. They should synchronize their data on a regular basis and be able to provision the web application rapidly using CloudFormation. The objective is to minimize changes to the existing web application, control the throughput of DynamoDB used for the synchronization of data and synchronize only the modified elements. Which design would you choose to meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS data Pipeline to schedule a DynamoDB cross region copy once a day. Create a 'Last updated' attribute in your DynamoDB table that would represent the timestamp of the last update and use it as a filter.**

</details>

### 111. dt-424

You currently operate a web application in the AWS US-East region. The application runs on an autoscaled layer of EC2 instances and an RDS Multi-AZ database. Your IT security compliance officer has tasked you to develop a reliable and durable logging solution to track changes made to your EC2, IAM, and RDS resources. The solution must ensure the integrity and confidentiality of your log data. Which of these solutions would you recommend?

<details><summary>Answer</summary>

**A. Create a new CloudTrail trail with one new S3 bucket to store the logs and with the global services option selected. Use IAM roles, S3 bucket policies, and Multi Factor Authentication (MFA) Delete on the S3 bucket that stores your logs.**

</details>

### 112. dt-431

Does Amazon RDS for SQL Server currently support importing data into the msdb database?

<details><summary>Answer</summary>

**B. No.**

</details>

### 113. q-431

A company has developed a new video game as a web application. The application is in a three-tier architecture in a VPC with Amazon RDS for MySQL in the database layer. Several players will compete concurrently online. The game’s developers want to display a top-10 scoreboard in near- real time and offer the ability to stop and restore the game while preserving the current scores. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Set up an Amazon ElastiCache for Redis cluster to compute and cache the scores for the web application to display.**

Redis is an in-memory data store that is well-suited for caching and real-time data processing. By setting up an ElastiCache for Redis cluster, you can compute and cache the scores in-memory, allowing for fast retrieval and updates.

</details>

### 114. q-435 `cost`

A company needs to migrate a MySQL database from its on-premises data center to AWS within 2 weeks. The database is 20 TB in size. The company wants to complete the migration with minimal downtime. Which solution will migrate the database MOST cost-effectively?

<details><summary>Answer</summary>

**A. Order an AWS Snowball Edge Storage Optimized device. Use AWS Database Migration Service (AWS DMS) with AWS Schema Conversion Tool (AWS SCT) to migrate the database with replication of ongoing changes. Send the Snowball Edge device to AWS to finish the migration and continue the ongoing replication.**

This is a cost-effective solution for shipping large amounts of data to AWS. Snowball Edge devices are designed for efficient data transfer, and they can handle the 20 TB database.  AWS DMS is a managed service for migrating databases to AWS, and AWS SCT can assist in converting the database schema. Using these tools in combination allows for a smooth migration process.

</details>

### 115. q-436 `cost`

A company moved its on-premises PostgreSQL database to an Amazon RDS for PostgreSQL DB instance. The company successfully launched a new product. The workload on the database has increased. The company wants to accommodate the larger workload without adding infrastructure. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Buy reserved DB instances for the total workload. Make the Amazon RDS for PostgreSQL DB instance larger.**

When you commit to using a database instance for a longer time (with reserved instances), AWS gives you a discount compared to paying on a month-to-month basis.  Imagine you have a computer, and you want to make it more powerful because you have more things to do on it. Making the instance larger means upgrading the power of your virtual computer.

</details>

### 116. dt-438

Is the encryption of connections between my application and my DB Instance using SSL for the MySQL server engines available?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 117. q-440

A company used an Amazon RDS for MySQL DB instance during application testing. Before terminating the DB instance at the end of the test cycle, a solutions architect created two backups. The solutions architect created the first backup by using the mysqldump utility to create a database dump. The solutions architect created the second backup by enabling the final DB snapshot option on RDS termination. The company is now planning for a new test cycle and wants to create a new DB instance from the most recent backup. The company has chosen a MySQL-compatible edition ofAmazon Aurora to host the DB instance. Which solutions will create the new DB instance? (Choose two.)

<details><summary>Answer</summary>

**A. Import the RDS snapshot directly into Aurora.**

C. Upload the database dump to Amazon S3. Then import the database dump into Aurora.  A. Amazon Aurora allows you to directly import an Amazon RDS snapshot into Aurora. This is a straightforward process for migrating data from RDS to Aurora.  C. Uploading the database dump to Amazon S3 and then importing the database dump into Aurora is a common method. You can use the MySQL-compatible version of Aurora to restore the data from a database dump stored in Amazon S3.

</details>

### 118. dt-448

Do the system resources on the Micro instance meet the recommended configuration for Oracle?

<details><summary>Answer</summary>

**B. Yes, but only for certain situations.**

</details>

### 119. q-449 `cost`

A company runs its application on an Oracle database. The company plans to quickly migrate to AWS because of limited resources for the database, backup administration, and data center maintenance. The application uses third-party database features that require privileged access. Which solution will help the company migrate the database to AWS MOST cost-effectively?

<details><summary>Answer</summary>

**B. Migrate the database to Amazon RDS Custom for Oracle. Customize the database settings to support third-party features.**

</details>

### 120. q-464

A company hosts an online shopping application that stores all orders in an Amazon RDS for PostgreSQL Single-AZ DB instance. Management wants to eliminate single points of failure and has asked a solutions architect to recommend an approach to minimize database downtime without requiring any changes to the application code. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Convert the existing database instance to a Multi-AZ deployment by modifying the database instance and specifying the Multi-AZ option.**

By converting the existing RDS instance to a Multi-AZ deployment, you enable high availability with automatic failover. Amazon RDS will automatically replicate the database to a standby instance in a different Availability Zone (AZ). In the event of a failure, Amazon RDS will automatically promote the standby to the primary, minimizing downtime.

</details>

### 121. dt-467

Is creating a Read Replica of another Read Replica supported?

<details><summary>Answer</summary>

**D. No.**

</details>

### 122. q-472

A company has a mobile chat application with a data store based in Amazon DynamoDB. Users would like new messages to be read with as little latency as possible. A solutions architect needs to design an optimal solution that requires minimal application changes. Which method should the solutions architect select?

<details><summary>Answer</summary>

**A. Configure Amazon DynamoDB Accelerator (DAX) for the new messages table. Update the code to use the DAX endpoint.**

DAX is an in-memory cache that sits in front of a DynamoDB table and answers cached reads in microseconds instead of the single-digit milliseconds DynamoDB itself returns. Because DAX speaks the DynamoDB API, the only change is to point the client at the DAX cluster endpoint, which keeps the application work small. A general-purpose cache such as ElastiCache would also cut latency, but you would have to write and maintain the cache-loading and invalidation logic yourself.

</details>

### 123. dt-473

A favored client needs you to quickly deploy a database that is a relational database service with minimal administration as he wants to spend the least amount of time administering it. Which database would be the best option?

<details><summary>Answer</summary>

**C. Amazon RDS.**

</details>

### 124. q-479

A company is making a prototype of the infrastructure for its new website by manually provisioning the necessary infrastructure. This infrastructure includes an Auto Scaling group, an Application Load Balancer and an Amazon RDS database. After the configuration has been thoroughly validated, the company wants the capability to immediately deploy the infrastructure for development and production use in two Availability Zones in an automated fashion. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**B. Define the infrastructure as a template by using the prototype infrastructure as a guide. Deploy the infrastructure with AWS CloudFormation.**

AWS CloudFormation is a service specifically designed for defining and deploying AWS infrastructure as code using templates. In this case, you can create a CloudFormation template based on the validated prototype infrastructure, and then use CloudFormation to deploy and manage the infrastructure in an automated and repeatable way.

</details>

### 125. dt-480 `performance` `availability`

Your application is using an ELB in front of an Auto Scaling group of web/application servers deployed across two AZs and a Multi-AZ RDS Instance for data persistence. The database CPU is often above 80% usage and 90% of I/O operations on the database are reads. To improve performance you recently added a single-node Memcached ElastiCache Cluster to cache frequent DB query results. In the next weeks the overall workload is expected to grow by 30%. Do you need to change anything in the architecture to maintain the high availability of the application with the anticipated additional load? Why?

<details><summary>Answer</summary>

**A. Yes, you should deploy two Memcached ElastiCache Clusters in different AZs because the RDS instance will not be able to handle the load if the cache node fails.**

</details>

### 126. q-481

A company hosts a three-tier web application in the AWS Cloud. A Multi-AZAmazon RDS for MySQL server forms the database layer Amazon ElastiCache forms the cache layer. The company wants a caching strategy that adds or updates data in the cache when a customer adds an item to the database. The data in the cache must always match the data in the database. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Implement the write-through caching strategy**

In a write-through caching strategy, data is always written or updated in the cache when it is modified in the database. This ensures that the cache is consistently updated with the latest data from the database. When a customer adds an item to the database, the write-through caching strategy ensures that the item is also added or updated in the cache.

</details>

### 127. dt-487

An online gaming site asked you if you can deploy a database that is a fast, highly scalable NoSQL database service in AWS for a new site that he wants to build. Which database should you recommend?

<details><summary>Answer</summary>

**A. Amazon DynamoDB.**

</details>

### 128. dt-499

How many relational database engines does RDS currently support?

<details><summary>Answer</summary>

**D. Eight: Amazon Aurora PostgreSQL-Compatible Edition, Amazon Aurora MySQL-Compatible Edition, RDS for PostgreSQL, RDS for MySQL, RDS for MariaDB, RDS for SQL Server, RDS for Oracle, and RDS for Db2.**

</details>

### 129. q-502

A company runs a website that uses a content management system (CMS) on Amazon EC2. The CMS runs on a single EC2 instance and uses an Amazon Aurora MySQL Multi-AZ DB instance for the data tier. Website images are stored on an Amazon Elastic Block Store (Amazon EBS) volume that is mounted inside the EC2 instance. Which combination of actions should a solutions architect take to improve the performance and resilience of the website? (Choose two.)

<details><summary>Answer</summary>

**C. Move the website images onto an Amazon Elastic File System (Amazon EFS) file system that is mounted on every EC2 instance.**

E. Create an Amazon Machine Image (AMI) from the existing EC2 instance. Use the AMI to provision new instances behind an Application Load Balancer as part of an Auto Scaling group. Configure the Auto Scaling group to maintain a minimum of two instances. Configure an Amazon CloudFront distribution for the website.  Option C provides moving the website images onto an Amazon EFS file system that is mounted on every EC2 instance. Amazon EFS provides a scalable and fully managed file storage solution that can be accessed concurrently from multiple EC2 instances. This ensures that the website images can be accessed efficiently and consistently by all instances, improving performance.  In Option E The Auto Scaling group maintains a minimum of two instances, ensuring resilience by automatically replacing any unhealthy instances. Additionally, configuring an Amazon CloudFront distribution for the website further improves performance by caching content at edge locations closer to the end-users, reducing latency and improving content delivery. Hence combining these actions, the website's performance is improved through efficient image storage and content delivery

</details>

### 130. q-507

A company has a web application for travel ticketing. The application is based on a database that runs in a single data center in North America. The company wants to expand the application to serve a global user base. The company needs to deploy the application to multiple AWS Regions. Average latency must be less than 1 second on updates to the reservation database. The company wants to have separate deployments of its web platform across multiple Regions. However, the company must maintain a single primary reservation database that is globally consistent. Which solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Convert the application to use Amazon DynamoDB. Use a global table for the center reservation table. Use the correct Regional endpoint in each Regional deployment.**

Using DynamoDB's global tables feature, you can achieve a globally consistent reservation database with low latency on updates, making it suitable for serving a global user base. The automatic replication provided by DynamoDB eliminates the need for manual synchronization between Regions.

</details>

### 131. dt-510

What is an isolated database environment running in the cloud (Amazon RDS) called?

<details><summary>Answer</summary>

**A. DB Instance.**

</details>

### 132. q-511 `cost`

A company is developing software that uses a PostgreSQL database schema. The company needs to configure multiple development environments and databases for the company's developers. On average, each development environment is used for half of the 8-hour workday. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure each development environment with its own Amazon RDS for PostgreSQL Single-AZ DB instances**

Explanation: Since each environment is only used for half of the workday, a standard RDS for PostgreSQL instance that gets stopped when not in use is cheaper than running Aurora continuously — Aurora costs more than standard RDS and this workload doesn't need Aurora's extra performance/availability features.

</details>

### 133. dt-515

My Read Replica appears 'stuck' after a Multi-AZ failover and is unable to obtain or apply updates from the source DB Instance. What do I do?

<details><summary>Answer</summary>

**A. You will need to delete the Read Replica and create a new one to rep lace it.**

</details>

### 134. q-520 `cost`

A company is designing a new web application that will run on Amazon EC2 Instances. The application will use Amazon DynamoDB for backend data storage. The application traffic will be unpredictable. The company expects that the application read and write throughput to the database will be moderate to high. The company needs to scale in response to application traffic. Which DynamoDB table configuration will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure DynamoDB in on-demand mode by using the DynamoDB Standard table class.**

On-demand capacity mode allows DynamoDB to automatically scale read and write capacity based on actual application traffic. It eliminates the need for manual provisioning of read and write capacity, making it well-suited for unpredictable workloads. DynamoDB Standard Table Class:  The DynamoDB Standard table class provides general-purpose storage with consistent, single-digit millisecond latency. It's suitable for a wide range of applications, including those with unpredictable traffic

</details>

### 135. dt-521

Amazon RDS automated backups and DB Snapshots are currently supported for only the [...] storage engine.

<details><summary>Answer</summary>

**A. InnoDB.**

</details>

### 136. q-526 `least-ops`

A solutions architect is reviewing the resilience of an application. The solutions architect notices that a database administrator recently failed over the application's Amazon Aurora PostgreSQL database writer instance as part of a scaling exercise. The failover resulted in 3 minutes of downtime for the application. Which solution will reduce the downtime for scaling exercises with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Set up an Amazon RDS proxy for the database. Update the application to use the proxy endpoint.**

Amazon RDS Proxy is a fully managed, highly available database proxy for Amazon RDS (Relational Database Service). It provides connection pooling, read/write splitting, and automatic failover, helping to improve the availability and scalability of database workloads.

</details>

### 137. q-529

A company is migrating its workloads to AWS. The company has transactional and sensitive data in its databases. The company wants to use AWS Cloud solutions to increase security and reduce operational overhead for the databases. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the databases to Amazon RDS Configure encryption at rest.**

Amazon RDS (Relational Database Service) is a fully managed database service that simplifies database management tasks, such as hardware provisioning, patching, and backups.  Encryption at Rest Amazon RDS supports encryption at rest, which means data stored in the database is automatically encrypted. This provides an additional layer of security for sensitive data. Managed Service: Amazon RDS is a managed service, meaning AWS takes care of operational aspects such as hardware maintenance, software patching, and backups. This reduces operational overhead for the company.

</details>

### 138. q-536 `cost` `availability`

A company wants to provide data scientists with near real-time read-only access to the company's production Amazon RDS for PostgreSQL database. The database is currently configured as a Single-AZ database. The data scientists use complex queries that will not affect the production database. The company needs a solution that is highly available. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Change the setup from Single-AZ to a Multi-AZ DB cluster deployment and give the data scientists the cluster's reader endpoint.**

An RDS for PostgreSQL Multi-AZ DB cluster runs a writer plus two standby instances in two other Availability Zones, and both standbys serve reads through the reader endpoint. That covers high availability and read-only access for the data scientists with three instances and no extra components. Replication to the standbys is fast enough that the data they query is near real-time, and their heavy queries never touch the writer. Making the database a Multi-AZ instance deployment and then adding two read replicas reaches the same result with a fourth instance to pay for, so it is the more expensive answer.

</details>

### 139. q-537 `availability`

A company runs a three-tier web application in the AWS Cloud that operates across three Availability Zones. The application architecture has an Application Load Balancer, an Amazon EC2 web server that hosts user session states, and a MySQL database that runs on an EC2 instance. The company expects sudden increases in application traffic. The company wants to be able to scale to meet future application capacity demands and to ensure high availability across all three Availability Zones. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Migrate the MySQL database to Amazon RDS for MySQL with a Multi-AZ DB cluster deployment. Use Amazon ElastiCache for Redis with high availability to store session data and to cache reads. Migrate the web server to an Auto Scaling group that is in three Availability Zones.**

Migrating the MySQL database to Amazon RDS for MySQL with a Multi-AZ DB cluster deployment provides high availability by replicating the database across multiple Availability Zones. Using Amazon ElastiCache for Redis with high availability ensures that session data and reads are cached effectively, improving performance

</details>

### 140. q-540

A company has an on-premises server that uses an Oracle database to process and store customer information. The company wants to use an AWS database service to achieve higher availability and to improve application performance. The company also wants to offload reporting from its primary database system. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**D. Use Amazon RDS deployed in a Multi-AZ instance deployment to create an Amazon Aurora database. Direct the reporting functions to the reader instances.**

Deploying Amazon RDS in a Multi-AZ instance deployment ensures high availability by replicating the primary database instance in a different Availability Zone (AZ). This provides automatic failover in case of a hardware failure or maintenance event.

</details>

### 141. dt-545

A scope has been handed to you to set up a super fast gaming server and you decide that you will use Amazon DynamoDB as your database. For efficient access to data in a table, Amazon DynamoDB creates and maintains indexes for the primary key attributes. A secondary index is a data structure that contains a subset of attributes from a table, along with an alternate key to support Query operations. How many types of secondary indexes does DynamoDB support?

<details><summary>Answer</summary>

**A. 2.**

</details>

### 142. q-554

A company's SAP application has a backend SQL Server database in an on-premises environment. The company wants to migrate its on-premises application and database server to AWS. The company needs an instance type that meets the high demands of its SAP database. On-premises performance data shows that both the SAP application and the database have high memory utilization. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use the memory optimized instance family for both the application and the database.**

Memory optimized instances are designed to provide a high memory-to-CPU ratio, which aligns well with workloads that have significant memory requirements, such as SAP applications with backend databases.

</details>

### 143. q-561 `least-ops`

A company's website handles millions of requests each day, and the number of requests continues to increase. A solutions architect needs to improve the response time of the web application. The solutions architect determines that the application needs to decrease latency when retrieving product details from the Amazon DynamoDB table. Which solution will meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**A. Set up a DynamoDB Accelerator (DAX) cluster. Route all read requests through DAX.**

DynamoDB Accelerator (DAX) is a fully managed, highly available, and in-memory cache for DynamoDB. It is designed to improve the response time of read-intensive DynamoDB workloads by caching frequently accessed data. Using DAX helps reduce the read latency as it retrieves data from an in-memory cache instead of the DynamoDB table.

</details>

### 144. dt-564

When you run a DB Instance as a Multi-AZ deployment, the [...] serves database writes and reads

<details><summary>Answer</summary>

**D. primary.**

</details>

### 145. q-564

A company is building an ecommerce application and needs to store sensitive customer information. The company needs to give customers the ability to complete purchase transactions on the website. The company also needs to ensure that sensitive customer data is protected, even from database administrators. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Store sensitive data in Amazon RDS for MySQL. Use AWS Key Management Service (AWS KMS) client-side encryption to encrypt the data.**

Amazon RDS (Relational Database Service) for MySQL is a managed relational database service that makes it easy to set up, operate, and scale a MySQL database in the cloud. AWS Key Management Service (KMS) provides a way to create and control encryption keys. In the context of client-side encryption, the application (in this case, the ecommerce application) handles the encryption and decryption of data before it is stored in or retrieved from the database.

</details>

### 146. q-565

A company has an on-premises MySQL database that handles transactional data. The company is migrating the database to the AWS Cloud. The migrated database must maintain compatibility with the company's applications that use the database. The migrated database also must scale automatically during periods of increased demand. Which migration solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Database Migration Service (AWS DMS) to migrate the database to Amazon Aurora. Turn on Aurora Auto Scaling.**

AWS DMS is a fully managed service that helps you migrate databases to AWS easily and securely. It supports homogeneous and heterogeneous database migrations. Amazon Aurora is a fully managed relational database service that is compatible with MySQL and PostgreSQL. It provides high performance and availability with compatibility for MySQL, making it a seamless choice for migrating MySQL databases.

</details>

### 147. q-567 `least-ops`

A solutions architect is designing a workload that will store hourly energy consumption by business tenants in a building. The sensors will feed a database through HTTP requests that will add up usage for each tenant. The solutions architect must use managed services when possible. The workload will receive more features in the future as the solutions architect adds independent components. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon API Gateway with AWS Lambda functions to receive the data from the sensors, process the data, and store the data in an Amazon DynamoDB table.**

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. It acts as an entry point for HTTP requests and can handle the communication with the sensors. In this scenario, you can use Lambda functions to process the data received from the sensors.  Amazon DynamoDB is a fully managed NoSQL database that can handle the storage of the hourly energy consumption data.

</details>

### 148. dt-568

When you resize the Amazon RDS DB instance, Amazon RDS will perform the upgrade during the next maintenance window. If you want the upgrade to be performed now, rather than waiting for the maintenance window, specify the [...] option.

<details><summary>Answer</summary>

**D. Apply Immediately.**

</details>

### 149. q-572

A company runs an application on AWS. The application receives inconsistent amounts of usage. The application uses AWS Direct Connect to connect to an on-premises MySQL-compatible database. The on-premises database consistently uses a minimum of 2 GiB of memory. The company wants to migrate the on-premises database to a managed AWS service. The company wants to use auto scaling capabilities to manage unexpected workload increases. Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**C. Provision an Amazon Aurora Serverless v2 database with a minimum capacity of 1 Aurora capacity unit (ACU).**

Aurora Serverless is designed for applications with variable or unpredictable workloads. With Aurora Serverless v2, you can set the minimum capacity to 1 Aurora capacity unit (ACU), and it will automatically scale based on the actual workload.

</details>

### 150. q-574 `cost`

A financial services company launched a new application that uses an Amazon RDS for MySQL database. The company uses the application to track stock market trends. The company needs to operate the application for only 2 hours at the end of each week. The company needs to optimize the cost of running the database. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Migrate the existing RDS for MySQL database to an Aurora Serverless v2 MySQL database cluster.**

Aurora Serverless allows the database to automatically start up, shut down, and scale capacity based on actual usage. With Aurora Serverless v2, you can set a minimum and maximum capacity for the cluster. This is suitable for intermittent workloads, such as the application that is only operated for 2 hours at the end of each week.

</details>

### 151. q-575 `availability`

A company deploys its applications on Amazon Elastic Kubernetes Service (Amazon EKS) behind an Application Load Balancer in an AWS Region. The application needs to store data in a PostgreSQL database engine. The company wants the data in the database to be highly available. The company also needs increased capacity for read workloads. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**C. Create an Amazon RDS database with Multi-AZ DB cluster deployment.**

Amazon RDS with Multi-AZ (Availability Zone) DB cluster deployment provides high availability by automatically replicating the primary database to a standby instance in a different Availability Zone. This helps ensure database availability in the event of a failure in the primary Availability Zone.

</details>

### 152. q-578 `least-ops`

A company deployed a serverless application that uses Amazon DynamoDB as a database layer. The application has experienced a large increase in users. The company wants to improve database response time from milliseconds to microseconds and to cache requests to the database. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use DynamoDB Accelerator (DAX).**

DAX is a fully managed, highly available, in-memory cache for DynamoDB that delivers fast response times for DynamoDB queries. It can be seamlessly integrated with existing DynamoDB applications, requiring minimal code changes. DAX allows you to cache frequently accessed data, reducing the need to read from the DynamoDB table and improving response times.

</details>

### 153. q-579

A company runs an application that uses Amazon RDS for PostgreSQL. The application receives traffic only on weekdays during business hours. The company wants to optimize costs and reduce operational overhead based on this usage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use the Instance Scheduler on AWS to configure start and stop schedules.**

Instance Scheduler: The AWS Instance Scheduler is a solution that allows you to schedule the start and stop times of your Amazon EC2 and RDS instances. By configuring start and stop schedules, you can ensure that resources are only running during the required business hours, thereby optimizing costs.

</details>

### 154. q-588 `cost`

An ecommerce company wants a disaster recovery solution for its Amazon RDS DB instances that run Microsoft SQL Server Enterprise Edition. The company's current recovery point objective (RPO) and recovery time objective (RTO) are 24 hours. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Copy automatic snapshots to another Region every 24 hours.**

RDS automatically takes snapshots of your database instances. These snapshots capture the entire DB instance, including the data and the DB instance's metadata.

</details>

### 155. q-590

A company migrated a MySQL database from the company's on-premises data center to an Amazon RDS for MySQL DB instance. The company sized the RDS DB instance to meet the company's average daily workload. Once a month, the database performs slowly when the company runs queries for a report. The company wants to have the ability to run reports and maintain the performance of the daily workloads. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a read replica of the database. Direct the queries to the read replica.**

Read Replica: Creating a read replica of the database allows you to offload read queries to a replica instance. This helps in distributing the workload and prevents the additional load from impacting the performance of the primary database.  Direct Queries to the Read Replica: By directing the queries for the monthly reports to the read replica, you ensure that the heavy reporting workload doesn't affect the performance of the primary database handling daily workloads. Read replicas are designed to handle read-intensive workloads, providing a scalable solution.

</details>

### 156. dt-592

Can I control if and when MySQL based RDS Instance is upgraded to new supported versions?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 157. dt-593

If I have multiple Read Replicas for my master DB Instance and I promote one of them, what happens to the rest of the Read Replicas?

<details><summary>Answer</summary>

**A. The remaining Read Replicas will still replicate from the older master DB Instance.**

</details>

### 158. q-593 `availability`

A solutions architect is designing a highly available Amazon ElastiCache for Redis based solution. The solutions architect needs to ensure that failures do not result in performance degradation or loss of data locally and within an AWS Region. The solution needs to provide high availability at the node level and at the Region level. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Multi-AZ Redis replication groups with shards that contain multiple nodes.**

Multi-AZ (Availability Zone) replication groups provide high availability at the node level. In a Multi-AZ setup, your data is replicated asynchronously to a standby replica in a different Availability Zone. Using shards with multiple nodes within each Availability Zone further enhances availability and provides scalability.

</details>

### 159. q-596 `cost`

An ecommerce application uses a PostgreSQL database that runs on an Amazon EC2 instance. During a monthly sales event, database usage increases and causes database connection issues for the application. The traffic is unpredictable for subsequent monthly sales events, which impacts the sales forecast. The company needs to maintain performance when there is an unpredictable increase in traffic. Which solution resolves this issue in the MOST cost-effective way?

<details><summary>Answer</summary>

**A. Migrate the PostgreSQL database to Amazon Aurora Serverless v2.**

Aurora Serverless is a serverless relational database engine provided by Amazon. It automatically adjusts its capacity based on actual usage, allowing it to scale up or down as needed. Aurora Serverless v2 builds upon the original Aurora Serverless model with additional features for even more efficient scaling.

</details>

### 160. q-601 `least-ops`

A company runs its critical database on an Amazon RDS for PostgreSQL DB instance. The company wants to migrate to Amazon Aurora PostgreSQL with minimal downtime and data loss. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Aurora read replica of the RDS for PostgreSQL DB instance. Promote the Aurora read replicate to a new Aurora PostgreSQL DB cluster.**

Aurora Read Replica: Creating an Aurora read replica from the RDS for PostgreSQL DB instance is a low-impact operation that allows you to replicate the data to Aurora with minimal downtime. Promote to Aurora PostgreSQL DB Cluster: Once the read replica is in sync with the primary RDS instance, you can promote the Aurora read replica to become the new primary cluster.

</details>

### 161. dt-603

SQL Server [...] store log ins and passwords in the master database.

<details><summary>Answer</summary>

**C. does.**

</details>

### 162. dt-618

A client needs you to import some existing infrastructure from a dedicated hosting provider to AWS to try and save on the cost of running his current website. He also needs an automated process that manages backups, software patching, automatic failure detection, and recovery. You are aware that his existing set up currently uses an Oracle database. Which of the following AWS databases would be best for accomplishing this task?

<details><summary>Answer</summary>

**A. Amazon RDS.**

</details>

### 163. dt-620

Amazon RDS creates an SSL certificate and installs the certificate on the DB Instance when Amazon RDS provisions the instance. These certificates are signed by a certificate authority. The [...] is stored at <https://rds.amazonaws.com/doc/rds-ssl-ca-cert.pem>.

<details><summary>Answer</summary>

**A. private key.**

</details>

### 164. q-622

A company is creating a new web application for its subscribers. The application will consist of a static single page and a persistent database layer. The application will have millions of users for 4 hours in the morning, but the application will have only a few thousand users during the rest of the day. The company's data architects have requested the ability to rapidly evolve their schema. Which solutions will meet these requirements and provide the MOST scalability? (Choose two.)

<details><summary>Answer</summary>

**C. Deploy Amazon DynamoDB as the database solution. Ensure that DynamoDB auto scaling is enabled.**

DynamoDB auto scaling allows the database to automatically adjust its read and write capacity based on the application's traffic, making it well-suited for varying workloads.  D. Deploy the static content into an Amazon S3 bucket. Provision an Amazon CloudFront distribution with the S3 bucket as the origin.  Amazon S3 is a highly scalable and durable object storage service, and using CloudFront, a content delivery network (CDN), helps distribute static content globally, reducing latency and providing scalability.

</details>

### 165. dt-627 `availability`

A company is deploying a new two-tier web application in AWS. The company has limited staff and requires high availability, and the application requires complex queries and table joins. Which configuration provides the solution for the company's requirements?

<details><summary>Answer</summary>

**B. Amazon RDS for MySQL with Multi-AZ.**

</details>

### 166. q-629 `least-ops`

A company runs a production database on Amazon RDS for MySQL. The company wants to upgrade the database version for security compliance reasons. Because the database contains critical data, the company wants a quick solution to upgrade and test functionality without losing any data. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use Amazon RDS Blue/Green Deployments to deploy and test production changes.**

</details>

### 167. q-631 `least-ops`

A social media company wants to store its database of user profiles, relationships, and interactions in the AWS Cloud. The company needs an application to monitor any changes in the database. The application needs to analyze the relationships between the data entities and to provide recommendations to users. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon Neptune to store the information. Use Neptune Streams to process changes in the database.**

Amazon Neptune is a fully managed graph database service that is designed for storing and querying highly connected data. It supports the property graph and RDF graph models, making it suitable for scenarios where relationships between data entities need to be analyzed. Neptune Streams:  Neptune Streams is a feature of Amazon Neptune that allows you to capture changes (inserts, updates, deletes) made to the graph database in a streaming fashion. This streaming capability enables you to react to changes in near real-time and trigger additional processing based on those changes.

</details>

### 168. q-633

A company manages an application that stores data on an Amazon RDS for PostgreSQL Multi-AZ DB instance. Increases in traffic are causing performance problems. The company determines that database queries are the primary reason for the slow performance. What should a solutions architect do to improve the application's performance?

<details><summary>Answer</summary>

**C. Create a read replica from the source DB instance. Serve read traffic from the read replica.**

Creating read replicas allows you to offload read traffic from the primary (master) DB instance to one or more read replicas. Read replicas can serve read-only queries, distributing the load and improving overall query performance.

</details>

### 169. q-637

A solutions architect is designing a new service behind Amazon API Gateway. The request patterns for the service will be unpredictable and can change suddenly from 0 requests to over 500 per second. The total size of the data that needs to be persisted in a backend database is currently less than 1 GB with unpredictable future growth. Data can be queried using simple key-value requests. Which combination ofAWS services would meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Amazon DynamoDB**

AWS Lambda is a serverless compute service that automatically scales with the number of incoming requests. It's suitable for unpredictable workloads, as it allows you to run code without provisioning or managing servers. Lambda functions can be triggered by API Gateway for handling HTTP requests. Amazon DynamoDB (Option C):  DynamoDB is a fully managed NoSQL database service that can handle unpredictable and scalable workloads. It provides low-latency, high-throughput performance for simple key-value queries. DynamoDB automatically scales to accommodate varying request rates, and you pay for the throughput you provision.

</details>

### 170. dt-642

You are running PostgreSQL on Amazon RDS and it seems to be all running smoothly deployed in one Availability Zone. A database administrator asks you if DB instances running PostgreSQL support Multi-AZ deployments. What would be a correct response to this question?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 171. dt-643

What is the data model of DynamoDB?

<details><summary>Answer</summary>

**C. 'Table', a collection of Items; 'Items', with Keys and one or more Attribute; and 'Attribute', with Name and Value.**

</details>

### 172. dt-646 `cost`

A large company wants to provide its globally located developers separate, limited size, managed PostgreSQL databases for development purposes. The databases will be low volume. The developers need the databases only when they are actively working. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon Aurora Serverless cluster. Develop an AWS Service Catalog product to launch databases in the cluster with the default capacity settings. Grant the developers access to the product.**

</details>

### 173. dt-648

A company's web application consists of multiple Amazon EC2 instances that run behind an Application Load Balancer in a VPC. An Amazon RDS for MySQL DB instance contains the data. The company needs the ability to automatically detect and respond to suspicious or unexpected behavior in its AWS environment. The company already has added AWS WAF to its architecture. What should a solutions architect do next to protect against threats?

<details><summary>Answer</summary>

**A. Use Amazon GuardDuty to perform threat detection. Configure Amazon EventBridge (Amazon CloudWatch Events) to filter for GuardDuty findings and to invoke an AWS Lambda function to adjust the AWS WAF rules.**

</details>

### 174. q-649 `cost`

An ecommerce company runs a PostgreSQL database on premises. The database stores data by using high IOPS Amazon Elastic Block Store (Amazon EBS) block storage. The daily peak I/O transactions per second do not exceed 15,000 IOPS. The company wants to migrate the database to Amazon RDS for PostgreSQL and provision disk IOPS performance independent of disk storage capacity. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Configure the General Purpose SSD (gp3) EBS volume storage type and provision 15,000 IOPS.**

Amazon EBS gp3 volumes are designed for general-purpose workloads and offer a balance of price and performance. They allow you to provision IOPS independently of storage capacity, similar to io1 volumes.

</details>

### 175. q-650 `least-ops`

A company wants to migrate its on-premises Microsoft SQL Server Enterprise edition database to AWS. The company's online application uses the database to process transactions. The data analysis team uses the same production database to run reports for analytical processing. The company wants to reduce operational overhead by moving to managed services wherever possible. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Migrate to Amazon RDS for Microsoft SOL Server. Use read replicas for reporting purposes**

Amazon RDS supports read replicas, allowing you to offload reporting and analytical workloads to replicas without impacting the performance of the primary database. This is a cost-effective and efficient way to handle reporting without affecting transactional processing on the primary database.

</details>

### 176. gh-653

A company maintains an Amazon RDS database that maps users to cost centers. The company has accounts in an organization in AWS
Organizations. The company needs a solution that will tag all resources that are created in a speci c AWS account in the organization. The
solution must tag each resource with the cost center ID of the user who created the resource.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Create a Lambda function triggered by EventBridge (via CloudTrail) to tag resources based on the RDS cost center DB.**

EventBridge + Lambda automates real-time tagging without manual intervention.
SCPs (Option A) cannot dynamically tag resources, and scheduled rules (Option C) are not event-driven.

</details>

### 177. dt-654

A company runs several Amazon RDS for Oracle On-Demand DB instances that have high utilization. The RDS DB instances run in member accounts that are in an organization in AWS Organizations. The company's finance team has access to the organization's management account and member accounts. The finance team wants to find ways to optimize costs by using AWS Trusted Advisor. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use the Trusted Advisor recommendations in the management account.; C. Review the Trusted Advisor checks for Amazon RDS Reserved Instance Optimization.**

</details>

### 178. gh-654 `availability`

A company recently migrated its web application to the AWS Cloud. The company uses an Amazon EC2 instance to run multiple processes to host
the application. The processes include an Apache web server that serves static content. The Apache web server makes requests to a PHP
application that uses a local Redis server for user sessions.
The company wants to redesign the architecture to be highly available and to use AWS managed solutions.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: D) Use CloudFront + S3 for static content, ALB + ECS Fargate for PHP, and Multi-AZ ElastiCache for Redis.**

Fully managed services (ECS, ElastiCache) ensure high availability. CloudFront improves static content delivery.
Elastic Beanstalk (Option A) lacks decoupling, and Lambda (Option B) is unsuitable for PHP sessions.

</details>

### 179. dt-656

A company wants to relocate its on-premises MySQL database to AWS. The database accepts regular imports from a client-facing application, which causes a high volume of write operations. The company is concerned that the amount of traffic might be causing performance issues within the application. How should a solutions architect design the architecture on AWS?

<details><summary>Answer</summary>

**A. Provision an Amazon RDS for MySQL DB instance with Provisioned IOPS SSD storage. Monitor write operation metrics by using Amazon CloudWatch. Adjust the provisioned IOPS if necessary.**

</details>

### 180. dt-658 `least-ops`

A company uses Amazon RDS with default backup settings for its database tier. The company needs to make a daily backup of the database to meet regulatory requirements. The company must retain the backups for 30 days. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Modify the RDS database to have a retention period of 30 days for automated backups.**

</details>

### 181. dt-659

A company is running a multi-tier web application on AWS. The application runs its database tier on Amazon Aurora MySQL. The application and database tiers are in the us-east-1 Region. A database administrator who regularly monitors the Aurora DB cluster finds that an intermittent increase in read traffic is creating high CPU utilization on the read replica and causing increased read latency of the application. What should a solutions architect do to improve read scalability?

<details><summary>Answer</summary>

**D. Configure Aurora Auto Scaling for the read replica.**

</details>

### 182. dt-660 `cost`

A company that runs its application on AWS uses an Amazon Aurora DB cluster as its database. During peak usage hours when multiple users access and read the data, the monitoring system shows degradation of database performance for write queries. The company wants to increase the scalability of the application to meet peak usage demands. Which solution will meet these requirements MOST cost effectively?

<details><summary>Answer</summary>

**C. Create an Aurora read replica in the existing Aurora DB cluster. Update the application to use the replica endpoint for read only queries and to use the cluster endpoint for write queries.**

</details>

### 183. q-661 `least-ops`

A company runs applications on AWS that connect to the company's Amazon RDS database. The applications scale on weekends and at peak times of the year. The company wants to scale the database more effectively for its applications that connect to the database. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon RDS Proxy with a target group for the database. Change the applications to use the RDS Proxy endpoint.**

RDS Proxy manages scaling connections with minimal code changes. DynamoDB (Option A) is incompatible with RDS.

</details>

### 184. q-669 `least-ops`

A company runs its databases on Amazon RDS for PostgreSQL. The company wants a secure solution to manage the master user password by rotating the password every 30 days. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Integrate AWS Secrets Manager with Amazon RDS for PostgreSQL to automate password rotation.**

Secrets Manager automates rotation every 30 days with zero operational effort. Manual rotation (Option B) or Parameter Store (Option D) lacks automation.

</details>

### 185. q-670

A company performs tests on an application that uses an Amazon DynamoDB table. The tests run for 4 hours once a week. The company knows how many read and write operations the application performs to the table each second during the tests. The company does not currently use DynamoDB for any other use case. A solutions architect needs to optimize the costs for the table. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Choose on-demand capacity mode for the table.**

The table is used for 4 hours a week and sits idle the rest of the time. On-demand mode charges per read and write request and nothing for idle time, so the bill tracks the actual 4 hours of testing. Provisioned mode charges for the capacity units every hour of the month, so roughly 97 percent of what you paid would be for an idle table; on-demand only loses to provisioned once a table is busy something like 15 to 20 percent of the time, far above this workload. Reserved capacity deepens the problem by committing to those hourly charges for a year or more. Knowing the per-second request rate is a distractor - predictable traffic favours provisioned capacity only when the table is busy most of the time.

</details>

### 186. dt-679

A company hosts a data lake on AWS. The data lake consists of data in Amazon S3 and Amazon RDS for PostgreSQL. The company needs a reporting solution that provides data visualization and includes all the data sources within the data lake. Only the company's management team should have full access to all the visualizations. The rest of the company should have only limited access. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an analysis in Amazon QuickSight. Connect all the data sources and create new datasets. Publish dashboards to visualize the data. Share the dashboards with the appropriate IAM roles.**

</details>

### 187. dt-680 `availability`

A company runs an ecommerce application on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales based on CPU utilization metrics. The ecommerce application stores the transaction data in a MySQL 8.0 database that is hosted on a large EC2 instance. The database's performance degrades quickly as application load increases. The application handles more read requests than write transactions. The company wants a solution that will automatically scale the database to meet the demand of unpredictable read workloads while maintaining high availability. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon Aurora with a Multi-AZ deployment. Configure Aurora Auto Scaling with Aurora Replicas.**

</details>

### 188. dt-694 `cost`

A development team runs monthly resource-intensive tests on its general purpose Amazon RDS for MySQL DB instance with Performance Insights enabled. The testing lasts for 48 hours once a month and is the only process that uses the database. The team wants to reduce the cost of running the tests without reducing the compute and memory attributes of the DB instance. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a snapshot when tests are completed. Terminate the DB instance and restore the snapshot when required.**

</details>

### 189. dt-695

A company that hosts its web application on AWS wants to ensure all Amazon EC2 instances, Amazon RDS DB instances, and Amazon Redshift clusters are configured with tags. The company wants to minimize the effort of configuring and operating this check. What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**A. Use AWS Config rules to define and detect resources that are not properly tagged.**

</details>

### 190. dt-696

A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in AmazonDynamoDB. Other applications can consume the transactions data off the Kinesis data stream.**

</details>

### 191. dt-702 `least-ops`

A company uses Amazon RDS for PostgreSQL databases for its data tier. The company must implement password rotation for the databases. Which solution meets this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Store the password in AWS Secrets Manager. Enable automatic rotation on the secret.**

</details>

### 192. dt-703 `cost`

A company runs its application on Oracle Database Enterprise Edition. The company needs to migrate the application and the database to AWS. The company can use the Bring Your Own License (BYOL) model while migrating to AWS. The application uses third-party database features that require privileged access. A solutions architect must design a solution for the database migration. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Migrate the database to Amazon RDS Custom for Oracle by using native tools. Customize the new database settings to support the third-party features.**

</details>

### 193. dt-708

A company uses a Microsoft SQL Server database. The company's applications are connected to the database. The company wants to migrate to an Amazon Aurora PostgreSQL database with minimal changes to the application code. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Enable Babelfish on Aurora PostgreSQL to run the SQL queries from the applications.; C. Migrate the database schema and data by using the AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS).**

</details>

### 194. dt-715 `cost` `availability`

A company has migrated a two-tier application from its on-premises data center to the AWS Cloud. The data tier is a Multi-AZ deployment of Amazon RDS for Oracle with 12 TB of General Purpose SSD Amazon Elastic Block Store (Amazon EBS) storage. The application is designed to process and store documents in the database as binary large objects (blobs) with an average document size of 6 MB. The database size has grown over time, reducing the performance and increasing the cost of storage. The company must improve the database performance and needs a solution that is highly available and resilient. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon S3 bucket. Update the application to store documents in the S3 bucket. Store the object metadata in the existing database.**

</details>

### 195. dt-717

A company is creating a three-tier web application consisting of a web server, an application server, and a database server. The application will track GPS coordinates of packages as they are being delivered. The application will update the database every 0.5 seconds. The tracking will need to be read as fast as possible for users to check the status of their packages. Only a few packages might be tracked on some days, whereas millions of packages might be tracked on other days. Tracking will need to be searchable by tracking ID, customer ID, and order ID. Orders older than 1 month no longer need to be tracked. What should a solutions architect recommend to accomplish this with minimal total cost of ownership?

<details><summary>Answer</summary>

**B. Use Amazon DynamoDB with global secondary indexes. Activate Auto Scaling for the DynamoDB table and the global secondary indexes. Turn on TTL for the DynamoDB table.**

</details>

### 196. dt-725

A company's legacy application is currently relying on a single-instance Amazon RDS MySQL database without encryption. Due to new compliance requirements, all existing and new data in this database must be encrypted. How should this be accomplished?

<details><summary>Answer</summary>

**C. Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from the encrypted snapshot.**

</details>

### 197. dt-726

An ecommerce company is preparing to deploy a web application on AWS to ensure continuous service for customers. The architecture includes a web application that the company hosts on Amazon EC2 instances, a relational database in Amazon RDS, and static assets that the company stores in Amazon S3. The company wants to design a robust and resilient architecture for the application. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Deploy a Multi-AZ RDS DB instance. Use Amazon CloudFront to distribute static assets.**

</details>

### 198. dt-728

A company runs its production workload on an Amazon Aurora MySQL DB cluster that includes six Aurora Replicas. The company wants near-real-time reporting queries from one of its departments to be automatically distributed across three of the Aurora Replicas. Those three replicas have a different compute and memory specification from the rest of the DB cluster. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Create and use a custom endpoint for the workload.**

</details>

### 199. dt-734

A company is running a multi-tier web application on premises. The web application is containerized and runs on a number of Linux hosts connected to a PostgreSQL database that contains user records. The operational overhead of maintaining the infrastructure and capacity planning is limiting the company's growth. A solutions architect must improve the application's infrastructure. Which combination of actions should the solutions architect take to accomplish this? (Choose two.)

<details><summary>Answer</summary>

**A. Migrate the PostgreSQL database to Amazon Aurora.; E. Migrate the web application to be hosted on AWS Fargate with Amazon Elastic Container Service (Amazon ECS).**

</details>

### 200. dt-735

An application allows users at a company's headquarters to access product data. The product data is stored in an Amazon RDS MySQL DB instance. The operations team has isolated an application performance slowdown and wants to separate read traffic from write traffic. A solutions architect needs to optimize the application's performance quickly. What should the solutions architect recommend?

<details><summary>Answer</summary>

**D. Create read replicas for the database. Configure the read replicas with the same compute and storage resources as the source database.**

</details>

### 201. dt-736

A company is using Amazon DynamoDB with provisioned throughput for the database tier of its ecommerce website. During flash sales, customers experience periods of time when the database cannot handle the high number of transactions taking place. This causes the company to lose transactions. During normal periods, the database performs appropriately. Which solution solves the performance problem the company faces?

<details><summary>Answer</summary>

**A. Switch DynamoDB to on-demand mode during flash sales.**

</details>

### 202. dt-745 `availability`

A company is building a payment application that must be highly available even during regional service disruptions. A solutions architect must design a data storage solution that can be easily replicated and used in other AWS Regions. The application also requires low-latency atomicity, consistency, isolation, and durability (ACID) transactions that need to be immediately available to generate reports. The development team also needs to use SQL. Which data storage solution meets these requirements?

<details><summary>Answer</summary>

**A. Amazon Aurora Global Database**

</details>

### 203. dt-749

A company has a custom application with embedded credentials that retrieves information from an Amazon RDS MySQL DB instance. Management says the application must be made more secure with the least amount of programming effort. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Secrets Manager.**

</details>

### 204. dt-750

A company's order fulfillment service uses a MySQL database. The database needs to support a large number of concurrent queries and transactions. Developers are spending time patching and tuning the database. This is causing delays in releasing new product features. The company wants to use cloud-based services to help address this new challenge. The solution must allow the developers to migrate the database with little or no code changes and must optimize performance. Which service should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**A. Amazon Aurora**

</details>

### 205. dt-752

A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance. What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?

<details><summary>Answer</summary>

**A. Encrypt a copy of the latest DB snapshot. Replace the existing DB instance by restoring the encrypted snapshot.**

</details>

### 206. dt-753 `availability`

A company is setting up an application to use an Amazon RDS MySQL DB instance. The database must be architected for high availability across Availability Zones and AWS Regions with minimal downtime. How should a solutions architect meet this requirement?

<details><summary>Answer</summary>

**B. Set up an RDS MySQL Multi-AZ DB instance. Configure a read replica in a different Region.**

</details>

### 207. dt-762

An application uses an Amazon RDS MySQL DB instance. The RDS database is becoming low on disk space. A solutions architect wants to increase the disk space without downtime. Which solution meets these requirements with the LEAST amount of effort?

<details><summary>Answer</summary>

**A. Enable storage auto scaling in RDS.**

</details>

### 208. dt-764

A company has a website deployed on AWS. The database backend is hosted on Amazon RDS for MySQL with a primary instance and five read replicas to support scaling needs. The read replicas should lag no more than 1 second behind the primary instance to support the user experience. As traffic on the website continues to increase, the replicas are falling further behind during periods of peak load, resulting in complaints from users when searches yield inconsistent results. A solutions architect needs to reduce the replication lag as much as possible, with minimal changes to the application code or operational requirements. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Migrate the database to Amazon Aurora MySQL. Replace the MySQL read replicas with Aurora Replicas and enable Aurora Auto Scaling.**

</details>
