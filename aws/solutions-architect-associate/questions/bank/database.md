# Databases — RDS, Aurora, DynamoDB, caching, warehousing

293 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. ce-6 `cost` `least-ops`

A company maintains its accounting records in a custom application that runs on Amazon EC2 instances. The company needs to migrate the data to an AWS managed service for development and maintenance of the application dat a. The solution must require minimal operational support and provide immutable, cryptographically verifiable logs of data changes. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Copy the records from the application into an Amazon Quantum Ledger Database (Amazon QLDB) ledger.**

The core requirements are for a managed service that provides an immutable and cryptographically verifiable log of data changes, which is essential for accounting systems. Amazon Quantum Ledger Database (QLDB) is a purpose-built, fully managed ledger database designed for this exact use case. It maintains a complete and unchangeable history of all application data changes. Its journal is append-only and uses cryptographic hashing to link transactions, ensuring data integrity can be verified. As a serverless service, it also fulfills the requirement for minimal operational support. Why Incorrect Options are Wrong: A. Amazon Redshift is a data warehouse optimized for large-scale analytics and business intelligence, not for maintaining a transactional, verifiable ledger. B. Amazon Neptune is a managed graph database service designed for querying datasets with complex relationships, which is

</details>

### 2. dt-8

When should I choose Provisioned IOPS over Standard RDS storage?

<details><summary>Answer</summary>

**B. If you use production online transaction processing (OLTP) workloads.**

</details>

### 3. wl-9

Organization XYZ is planning to build an online chat application for their enterprise level collaboration for their employees across the world. They are looking for a single digit latency fully managed database to store and retrieve conversations. What would AWS Database service you recommend?

<details><summary>Answer</summary>

**A. AWS DynamoDB**

Read more here: https://aws.amazon.com/dynamodb/#whentousedynamodb
Read more here:
https://aws.amazon.com/about-aws/whats-new/2015/07/amazon-dynamodb-available-
now-cross-region-replication-triggers-and-streams/

</details>

### 4. dt-10

Because of the extensibility limitations of striped storage attached to Windows Server, Amazon RDS does not currently support increasing storage on a [...] DB Instance.

<details><summary>Answer</summary>

**A. SQL Server.**

</details>

### 5. et-11

A company has an application that runs on Amazon EC2 instances and uses an Amazon Aurora database. The EC2 instances connect to the database by using user names and passwords that are stored locally in a file. The company wants to minimize the operational overhead of credential management. What should a solutions architect do to accomplish this goal?

<details><summary>Answer</summary>

**A. Use AWS Secrets Manager. Turn on automatic rotation.**

AWS Secrets Manager is a secrets management service that helps you protect access to your applications, services, and IT resources. This service enables you to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

</details>

### 6. et-13 `least-ops`

A company performs monthly maintenance on its AWS infrastructure. During these maintenance activities, the company needs to rotate the credentials for its Amazon RDS for MySQL databases across multiple AWS Regions. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Store the credentials as secrets in AWS Secrets Manager. Use multi-Region secret replication for the required Regions. Configure Secrets Manager to rotate the secrets on a schedule.**

AWS Secrets Manager allows you to store, manage, and rotate secrets, such as database credentials, across multiple AWS Regions. By enabling multi-Region secret replication, you can replicate the secrets across the required Regions to allow for seamless rotation of the credentials during maintenance activities. Additionally, Secrets Manager provides automatic rotation of secrets on a schedule, which would minimize the operational overhead of rotating the credentials on a monthly basis.

</details>

### 7. wl-14

Your organization is building a collaboration platform for which they chose AWS EC2 for web and application servers and MySQL RDS instance as the database. Due to the nature of the traffic to the application, they would like to increase the number of connections to RDS instances. How can this be achieved?

<details><summary>Answer</summary>

**B. Create a new parameter group, attach it to the DB instance and change the setting.**

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithPar
amGroups

</details>

### 8. dt-17

Amazon RDS supports SOAP only through [...].

<details><summary>Answer</summary>

**D. HTTPS.**

</details>

### 9. ce-19 `least-ops`

An ecommerce company has an application that collects order-related information from customers. The company uses one Amazon DynamoDB table to store customer home addresses, phone numbers, and email addresses. Customers can check out without creating an account. The application copies the customer information to a second DynamoDB table if a customer does create an account. The company requires a solution to delete personally identifiable information (PII) for customers who did not create an account within 28 days. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use a createdAt timestamp to set TTL for data in the first DynamoDB table to 28 days.**

Amazon DynamoDB Time To Live (TTL) is a fully managed feature that allows you to define a per-item timestamp to determine when an item is no longer needed. DynamoDB automatically deletes expired items in the background without consuming any write capacity. By setting a createdAt timestamp and a corresponding TTL attribute to 28 days in the future upon item creation, the system can automatically purge the data for guest checkouts. This approach is the most efficient and has the least operational overhead as it requires no custom code, servers, or scheduled tasks to manage. Why Incorrect Options are Wrong: A. This solution requires writing, deploying, and maintaining a Lambda function and its dependencies, which introduces more operational overhead than using a built-in, fully managed DynamoDB feature like TTL. B. This unnecessarily complicates the architecture by introducing Amazon S3 and

</details>

### 10. dt-23

In the context of MySQL, version numbers are organized as MySQL version = X.Y.Z. What does X denote here?

<details><summary>Answer</summary>

**D. Major version.**

</details>

### 11. wl-24

You have launched an RDS instance with MySQL database with default configuration for your file sharing application to store all the transactional information. Due to security compliance, your organization wants to encrypt all the databases and storage on the cloud. They approached you to perform this activity on your MySQL RDS database. How can you achieve this?

<details><summary>Answer</summary>

**A. Copy snapshot from the latest snapshot of your RDS instance, select encryption**

https://aws.amazon.com/blogs/aws/amazon-rds-update-share-encrypted-snapshots-enc
rypt-existing-instances/

</details>

### 12. dt-27

When running my DB Instance as a Multi-AZ deployment, can I use the standby for read or write operations?

<details><summary>Answer</summary>

**D. No.**

</details>

### 13. dt-31

What does Amazon DynamoDB provide?

<details><summary>Answer</summary>

**D. A fast, highly scalable managed NoSQL database service.**

</details>

### 14. ce-34 `security`

A company is building an application on AWS that connects to an Amazon RDS database. The company wants to manage the application configuration and to securely store and retrieve credentials for the database and other services. Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**A. Use AWS AppConfig to store and manage the application configuration. Use AWS Secrets Manager to store and retrieve the credentials.**

This solution correctly pairs two purpose-built AWS services to meet the specified requirements with minimal overhead. AWS AppConfig is designed to create, manage, and quickly deploy application configurations, separating them from the application code. This allows for controlled updates without redeploying the application. AWS Secrets Manager is a dedicated service for securely storing, managing, and retrieving secrets like database credentials. Its key feature is the ability to automatically rotate credentials for supported services, including Amazon RDS, which significantly reduces administrative overhead and enhances security. Why Incorrect Options are Wrong: B: Using AWS Lambda to manage configuration is not its intended purpose and would require custom development, increasing administrative overhead. AWS Secrets Manager is superior to Parameter Store for RDS due to automatic creden

</details>

### 15. dt-34

Multi-AZ deployment [...] supported for Microsoft SQL Server DB Instances.

<details><summary>Answer</summary>

**A. is not currently.**

</details>

### 16. dt-38

A company is running a batch analysis every hour on their main transactional DB, running on an RDS MySQL instance to populate their central Data Warehouse running on Redshift. During the execution of the batch their transactional applications are very slow. When the batch completes they need to update the top management dashboard with the new data. The dashboard is produced by another system running on-premises that is currently started when a manually-sent email notifies that an update is required. The on-premises system cannot be modified because it is managed by another team. How would you optimize this scenario to solve performance issues and automate the process as much as possible?

<details><summary>Answer</summary>

**A. Replace RDS with Redshift for the batch analysis and SNS to notify the on-premises system to update the dashboard.**

</details>

### 17. ce-39 `least-ops` `security`

A company runs a Node.js function on a server in its on-premises data center. The data center stores data in a PostgreSQL database. The company stores the credentials in a connection string in an environment variable on the server. The company wants to migrate its application to AWS and to replace the Node.js application server with AWS Lambd a. The company also wants to migrate to Amazon RDS for PostgreSQL and to ensure that the database credentials are securely managed. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Store the database credentials as a secret in AWS Secrets Manager. Configure Secrets Manager to automatically rotate the credentials every 30 days Update the Lambda function to retrieve the credentials from the secret.**

AWS Secrets Manager is the purpose-built service for managing the lifecycle of secrets, including database credentials. It provides native, automated rotation capabilities for supported services like Amazon RDS for PostgreSQL. By configuring Secrets Manager, the company can schedule automatic credential rotation (e.g., every 30 days) without writing or maintaining custom code. The Lambda function can then be granted IAM permissions to retrieve the current credentials at runtime. This approach securely manages credentials while fulfilling the requirement for the least operational overhead. Why Incorrect Options are Wrong: A. AWS Systems Manager Parameter Store does not have a built-in, automated rotation feature for RDS database credentials. Implementing rotation would require a custom solution, increasing operational overhead. C. Storing credentials in Lambda environment variables and wr

</details>

### 18. et-39

A company maintains a searchable repository of items on its website. The data is stored in an Amazon RDS for MySQL database table that contains more than 10 million rows. The database has 2 TB of General Purpose SSD storage. There are millions of updates against this data every day through the company's website. The company has noticed that some insert operations are taking 10 seconds or longer. The company has determined that the database storage performance is the problem. Which solution addresses this performance issue?

<details><summary>Answer</summary>

**A. Change the storage type to Provisioned IOPS SSD.**

Using Amazon Provisioned IOPS (PIOPS) SSD storage is the best way to solve the performance issue of insert operations taking 10 seconds or longer on an Amazon RDS for MySQL database table with more than 10 million rows and 2 TB of General Purpose SSD storage.  A high-performance storage solution with reliable throughput and minimal latency is PIOPS SSD storage. Workloads like insert operations, which demand high I/O performance, are ideally suited for it.

</details>

### 19. dt-40

You have been asked to build a database warehouse using Amazon Redshift. You know a little about it, including that it is a SQL data warehouse solution, and uses industry standard ODBC and JDBC connections and PostgreSQL drivers. However, you are not sure about what sort of storage it uses for database tables. What sort of storage does Amazon Redshift use for database tables?

<details><summary>Answer</summary>

**C. Columnar data storage.**

</details>

### 20. dt-48 `availability`

You are deploying an application to collect votes for a very popular television show. Millions of users will submit votes using mobile devices. The votes must be collected into a durable, scalable, and highly available data store for real-time public tabulation. Which service should you use?

<details><summary>Answer</summary>

**A. Amazon DynamoDB.**

</details>

### 21. dt-58

You need to import several hundred megabytes of data from a local Oracle database to an Amazon RDS DB instance. What does AWS recommend you use to accomplish this?

<details><summary>Answer</summary>

**C. Oracle Data Pump.**

</details>

### 22. dt-69

Your company is getting ready to do a major public announcement of a social media site on AWS. The website is running on EC2 instances deployed across multiple Availability Zones with a Multi-AZ RDS MySQL Extra Large DB Instance. The site performs a high number of small reads and writes per second and relies on an eventual consistency model. After comprehensive tests you discover that there is read contention on RDS MySQL. Which are the best approaches to meet these requirements? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Deploy ElasticCache in-memory cache running in each Availability Zone.; D. Add an RDS MySQL read replica in each Availability Zone.**

</details>

### 23. dt-71

The SQL Server [...] feature is an efficient means of copying data from a source database to your DB Instance. It writes the data that you specify to a data file, such as an ASCII file.

<details><summary>Answer</summary>

**A. bulk copy.**

</details>

### 24. dt-83

In the Amazon RDS which uses the SQL Server engine, what is the maximum size for a Microsoft SQL Server DB Instance with SQL Server Express edition?

<details><summary>Answer</summary>

**A. 10GB per DB.**

</details>

### 25. dt-92

Is Federated Storage Engine currently supported by Amazon RDS for MySQL?

<details><summary>Answer</summary>

**C. No.**

</details>

### 26. dt-95

Will my standby RDS instance be in the same Region as my primary?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 27. ce-97 `least-ops`

A company hosts an application that processes highly sensitive customer transactions on AWS. The application uses Amazon RDS as its database. The company manages its own encryption keys to secure the data in Amazon RDS. The company needs to update the customer-managed encryption keys at least once each year. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Set up automatic key rotation in AWS Key Management Service (AWS KMS) for the encryption keys.**

The requirement is to rotate customer-managed encryption keys for Amazon RDS annually with the least operational overhead. AWS Key Management Service (KMS) provides a built-in feature for automatic key rotation for customer-managed keys. When enabled, AWS KMS automatically generates new cryptographic material for the KMS key once per year. This is a fully managed process that requires no custom code or manual intervention after initial setup, directly fulfilling the requirements with the lowest possible operational burden. Why Incorrect Options are Wrong: B. This solution adds a manual step. An alert requires a person to perform the rotation, which is higher operational overhead than an automated process. C. Building, deploying, and maintaining a custom AWS Lambda function to perform rotation is significantly more operational overhead than using a native, managed KMS feature. D. This is

</details>

### 28. ce-99

A finance company has a web application that generates credit reports for customers. The company hosts the frontend of the web application on a fleet of Amazon EC2 instances that is associated with an Application Load Balancer (ALB). The application generates reports by running queries on an Amazon RDS for SQL Server database. The company recently discovered that malicious traffic from around the world is abusing the application by submitting unnecessary requests. The malicious traffic is consuming significant compute resources. The company needs to address the malicious traffic. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Use AWS WAF to create a web ACL. Associate the web ACL with the ALB. Use the AWS WAF Bot Control managed rule feature.**

The scenario describes malicious, automated traffic from various sources abusing the application, which is a classic bot attack. The most effective solution is to use AWS WAF, a web application firewall that protects against common web exploits and bots. The AWS WAF Bot Control managed rule group is specifically designed to identify, label, and block or rate-limit various types of bot traffic. By creating a web ACL, adding the Bot Control rule group, and associating it with the Application Load Balancer (ALB), the company can effectively mitigate the malicious requests and reduce the unnecessary load on its compute resources. Why Incorrect Options are Wrong: A. Manually blocking individual IP addresses is not a scalable or effective strategy against a distributed attack where attackers use a vast and constantly changing pool of IP addresses. C. AWS Shield Standard (enabled by default) an

</details>

### 29. dt-99

What does Amazon RDS stand for?

<details><summary>Answer</summary>

**B. Relational Database Service.**

</details>

### 30. dt-104

You need to set up a high level of security for an Amazon Relational Database Service (RDS) you have just built in order to protect the confidential information stored in it. What are all the possible security groups that RDS uses?

<details><summary>Answer</summary>

**A. DB security groups, VPC security groups, and EC2 security groups.**

</details>

### 31. ce-122

A company discovers that an Amazon DynamoDB Accelerator (DAX) cluster for the company's web application workload is not encrypting data at rest. The company needs to resolve thesecurity issue. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Delete the existing DAX cluster. Recreate the DAX cluster, and configure the new cluster to encrypt the data at rest.**

Amazon DynamoDB Accelerator (DAX) encryption at rest is a configuration that must be enabled when a cluster is created. According to the official AWS documentation, this setting is immutable and cannot be changed after the cluster has been provisioned. Therefore, to resolve the security issue of an unencrypted DAX cluster, the existing cluster must be deleted and a new cluster must be created with the encryption at rest feature enabled during the creation process. This ensures all data cached by DAX, including object and transaction logs, is encrypted on the disk. Why Incorrect Options are Wrong: A. DAX clusters do not have a stop/start lifecycle state, and the encryption setting cannot be modified after creation. C. The encryption at rest configuration for an existing DAX cluster is immutable and cannot be updated in-place. D. AWS Security Hub is a security posture management service th

</details>

### 32. dt-127

If you are using Amazon RDS Provisioned IOPS storage with MySQL and Oracle database engines, you can scale the throughput of your database Instance by specifying the IOPS rate from [...].

<details><summary>Answer</summary>

**D. 1,000 to 10,000.**

</details>

### 33. dt-132

You are designing a social media site and are considering how to mitigate distributed denial-of service (DDoS) attacks. Which of the below are viable mitigation techniques? (Choose 3 answers)

<details><summary>Answer</summary>

**C. Use an Amazon CloudFront distribution for both static and dynamic content.; D. Use an Elastic Load Balancer with auto scaling groups at the web. App and Amazon Relational Database Service (RDS) tiers.; E. Add alert Amazon CloudWatch to look for high Network in and CPU utilization.**

</details>

### 34. dt-139

You need a persistent and durable storage to trace call activity of an IVR (Interactive Voice Response) system. Call duration is mostly in the 2-3 minutes timeframe. Each traced call can be either active or terminated. An external application needs to know each minute the list of currently active calls, which are usually a few calls/second. Put once per month there is a periodic peak up to 1000 calls/second for a few hours. The system is open 24/7 and any downtime should be avoided. Historical data is periodically archived to files. Cost saving is a priority for this project. What database implementation would better fit this scenario, keeping costs as low as possible?

<details><summary>Answer</summary>

**A. Use RDS Multi-AZ with two tables, one for 'Active calls' and one for 'Terminated calls'. in this way the 'Active calls' table is always small and effective to access.**

</details>

### 35. ce-140 `least-ops`

A company uses Amazon RDS for PostgreSQL databases for its data tier. The company must implement password rotation for the databases. Which solution meets this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Store the password in AWS Secrets Manager. Enable automatic rotation on the secret.**

AWS Secrets Manager is the purpose-built service for managing the lifecycle of secrets, including database credentials. It provides native, automated rotation capabilities for supported services like Amazon RDS for PostgreSQL. By enabling automatic rotation, Secrets Manager uses a pre-configured AWS Lambda function to handle the entire process of changing the password in the database and updating the stored secret. This approach requires minimal configuration and no custom code, directly fulfilling the requirement for the "LEAST operational overhead." Why Incorrect Options are Wrong: B. Store the password in AWS Systems Manager Parameter Store. Enable automatic rotation on the parameter. AWS Systems Manager Parameter Store does not have a native, built-in feature for automatic secret rotation. This would require a custom solution, increasing operational overhead. C. Store the password in

</details>

### 36. dt-140

If you have chosen Multi-AZ deployment, in the event of a planned or unplanned outage of your primary DB Instance, Amazon RDS automatically switches to the standby replica. The automatic failover mechanism simply changes the record of the main DB Instance to point to the standby DB Instance.

<details><summary>Answer</summary>

**B. CNAME.**

</details>

### 37. ce-143

A company has a web application that uses several web servers that run on Amazon EC2 instances. The instances use a shared Amazon RDS for MySQL database. The company requires a secure method to store database credentials. The credentials must be automatically rotated every 30 days without affecting application availability. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Store database credentials in AWS Secrets Manager. Create an AWS Lambda function to automatically rotate the credentials. Use Amazon EventBridge to run the Lambda function on a schedule. Grant the necessary IAM permissions to allow the web servers to access Secrets Manager.**

AWS Secrets Manager is the purpose-built service for managing the lifecycle of secrets, including database credentials. It provides native, automated rotation capabilities for supported services like Amazon RDS for MySQL. By configuring automatic rotation, Secrets Manager uses an AWS Lambda function to update the credentials in both the database and the secret itself on a defined schedule (e.g., every 30 days). This process is designed to maintain application availability by using a staging label (AWSPENDING) during the update, ensuring the application can retrieve the new credentials without interruption. Using an IAM role attached to the EC2 instances is the secure and standard way to grant applications permission to retrieve secrets. Why Incorrect Options are Wrong: B. AWS Systems Manager OpsCenter is a service for viewing, investigating, and resolving operational issues (OpsItems); i

</details>

### 38. ce-145

A retail company runs its application on AWS. The application uses Amazon EC2 for web servers, Amazon RDS for database services, and Amazon CloudFront for global content distribution. The company needs a solution to mitigate DDoS attacks. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Enable AWS Shield Advanced. Configure CloudFront to work with Shield Advanced.**

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service designed to safeguard applications running on AWS. While AWS Shield Standard provides automatic protection against common network and transport layer attacks for all AWS customers, AWS Shield Advanced offers a higher level of protection. It provides enhanced detection, mitigation against larger and more sophisticated DDoS attacks, near real-time visibility into attacks, and 24/7 access to the AWS DDoS Response Team (DRT). For a company requiring a robust DDoS mitigation solution for its public-facing resources like Amazon CloudFront, enabling and configuring AWS Shield Advanced is the most direct and comprehensive approach. Why Incorrect Options are Wrong: A. AWS WAF is a web application firewall that protects against Layer 7 exploits like SQL injection. While it can mitigate some application-layer DDoS attac

</details>

### 39. ce-160 `least-ops`

A company needs to migrate its customer transactions database from on-premises to AWS. The database resides on an Oracle DB instance that runs on a Linux server. According to a new security requirement, the company must rotate the database password each year. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Migrate the database to Amazon RDS for Oracle. Store the password in AWS Secrets Manager. Turn on automatic rotation. Configure a yearly rotation schedule.**

The most efficient solution with the least operational overhead is to migrate the on-premises Oracle database to Amazon RDS for Oracle. Amazon RDS is a managed service that automates time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups. For the password rotation requirement, AWS Secrets Manager provides built-in, automated rotation capabilities for Amazon RDS databases. By storing the database credentials in Secrets Manager and enabling automatic rotation, the company can configure a yearly schedule without writing or maintaining custom code, thus minimizing operational effort. Why Incorrect Options are Wrong: A. Converting from Oracle (relational) to DynamoDB (NoSQL) is a complex re-architecture, not a simple migration, creating significant operational overhead. C. Migrating to an EC2 instance requires self-management of the OS and dat

</details>

### 40. dt-160

A company wants to implement their website in a virtual private cloud (VPC). The web tier will use an Auto Scaling group across multiple Availability Zones (AZs). The database will use Multi-AZ RDS MySQL and should not be publicly accessible. What is the minimum number of subnets that need to be configured in the VPC?

<details><summary>Answer</summary>

**D. 4.**

</details>

### 41. dt-177

Does Amazon RDS allow direct host access via Telnet, Secure Shell (SSH), or Windows Remote Desktop Connection?

<details><summary>Answer</summary>

**B. No.**

</details>

### 42. dt-178 `availability`

A user wants to achieve High Availability with PostgreSQL DB. Which of the below mentioned functionalities helps achieve HA?

<details><summary>Answer</summary>

**A. Multi-AZ.**

</details>

### 43. dt-182

What is the name of licensing model in which I can use your existing Oracle Database licenses to run Oracle deployments on Amazon RDS?

<details><summary>Answer</summary>

**A. Bring Your Own License.**

</details>

### 44. dt-185

Can I initiate a 'forced failover' for my Oracle Multi-AZ DB Instance deployment?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 45. dt-186 `availability`

Amazon RDS provides high availability and failover support for DB instances using [...].

<details><summary>Answer</summary>

**D. Multi-AZ deployments.**

</details>

### 46. et-187 `availability`

A company is developing an ecommerce application that will consist of a load-balanced front end, a container-based application, and a relational database. A solutions architect needs to create a highly available solution that operates with as little manual intervention as possible. Which solutions meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Create an Amazon RDS DB instance in Multi-AZ mode.**

D. Create an Amazon Elastic Container Service (Amazon ECS) cluster with a Fargate launch type to handle the dynamic application load.

</details>

### 47. dt-190

A 3-tier e-commerce web application is current deployed on-premises and will be migrated to AWS for greater scalability and elasticity The web server currently shares read-only data using a network distributed file system The app server tier uses a clustering mechanism for discovery and shared session state that depends on I P multicast The database tier uses shared-storage clustering to provide database fail over capability, and uses several read slaves for scaling Data on all servers and the distributed file system directory is backed up weekly to off-site tapes. Which AWS storage and database architecture meets the requirements of the application?

<details><summary>Answer</summary>

**C. Web servers: store read-only data in S3, and copy from S3 to root volume at boot time. App servers: share state using a combination of DynamoDB and IP unicast. Database: use RDS with multi-AZ deployment and one or more Read Replicas. Backup: web and app servers backed up weekly via AMIs, database backed up via DB snapshots.**

</details>

### 48. dt-195

A company needs to monitor the read and write IOPs metrics for their AWS MySQL RDS instance and send real-time alerts to their operations team. Which AWS services can accomplish this? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Amazon CloudWatch.; E. Amazon Simple Notification Service.**

</details>

### 49. dt-197

What is Oracle SQL Developer?

<details><summary>Answer</summary>

**B. A graphical Java tool distributed without cost by Oracle.**

</details>

### 50. ce-207

An ecommerce company runs applications in AWS accounts that are part of an organization in AWS Organizations. The applications run on Amazon Aurora PostgreSQL databases across all the accounts. The company needs to prevent malicious activity and must identify abnormal failed and incomplete login attempts to the databases.

<details><summary>Answer</summary>

**B. Enable the Amazon RDS Protection feature in Amazon GuardDuty for the member accounts of the organization.**

Amazon GuardDuty is a managed threat detection service that continuously monitors for malicious activity and unauthorized behavior. The GuardDuty RDS Protection feature is specifically designed to protect Amazon Aurora databases by analyzing and profiling database login activity. It uses tailored machine learning models to detect suspicious login attempts, such as brute-force attacks, logins from known malicious actors, or access from unusual locations. By enabling this feature for the organization, GuardDuty can be centrally managed and will monitor all member accounts, providing a scalable solution to identify the abnormal failed and incomplete login attempts as required. Why Incorrect Options are Wrong: A. Service Control Policies (SCPs) are used to enforce permission guardrails and restrict actions at the account or OU level; they do not have the capability to detect or analyze login

</details>

### 51. ce-214 `least-ops`

A company needs to migrate its customer transactions database from on premises to AWS. The database is an Oracle DB instance on Linux. A new requirement mandates rotating the database password yearly. Which solution provides this capability with the least operational overhead?

<details><summary>Answer</summary>

**B. Migrate the database to Amazon RDS for Oracle. Store the password in AWS Secrets Manager. Turn on automatic rotation with a yearly rotation schedule.**

The most efficient solution with the least operational overhead is to migrate the on-premises Oracle database to Amazon RDS for Oracle. Amazon RDS is a managed service that handles routine database tasks such as patching, backups, and scaling, significantly reducing administrative burden compared to running a database on EC2. For password rotation, AWS Secrets Manager provides native, automated rotation capabilities for Amazon RDS databases. By configuring a yearly rotation schedule in Secrets Manager, the password can be rotated automatically without writing or maintaining custom code (like a Lambda function), which directly fulfills the requirement with the absolute minimum operational overhead. Why Incorrect Options are Wrong: A. Converting from a relational database (Oracle) to a NoSQL database (DynamoDB) is a complex re-architecture, not a simple migration, which introduces massive

</details>

### 52. dt-215

In DynamoDB, could you use IAM to grant access to Amazon DynamoDB resources and API actions?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 53. ce-216

A solutions architect is building a static website hosted on Amazon S3. The website uses an Amazon Aurora PostgreSQL database accessed through an AWS Lambda function. The production website uses a Lambda alias that points to a specific version of the Lambda function. Database credentials must rotate every 2 weeks. Previously deployed Lambda versions must always use the most recent credentials. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Store credentials in AWS Secrets Manager. Turn on rotation. Write code in the Lambda function to retrieve credentials from Secrets Manager.**

AWS Secrets Manager is the purpose-built service for managing the lifecycle of secrets, including database credentials. It provides native, automated rotation for Amazon Aurora databases. By writing code in the Lambda function to retrieve the secret at runtime, any version of the function will always fetch the most current, valid credentials. This architecture decouples the secret from the function's code and version-specific configuration, ensuring that even previously deployed versions can connect to the database after a credential rotation, thus meeting all stated requirements securely and efficiently. Why Incorrect Options are Wrong: B. Including credentials in the code is a severe security anti-pattern. It also fails the requirement, as old function versions would contain old, invalid credentials. C. Lambda environment variables are locked to a specific function version upon publish

</details>

### 54. dt-216

The common use cases for DynamoDB Fine-Grained Access Control (FGAC) are cases in which the end user wants [...].

<details><summary>Answer</summary>

**D. to read or modify the table directly, without a middle-tier service.**

</details>

### 55. dt-222

True or False: The new DB Instance that is created when you promote a Read Replica retains the backup window period.

<details><summary>Answer</summary>

**A. True.**

</details>

### 56. ce-224 `security`

A company is designing a secure solution to grant access to its Amazon RDS for PostgreSQL database. Applications that run on Amazon EC2 instances must be able to securely authenticate to the database without storing long-term credentials. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use IAM roles to assign permissions to the EC2 instances. Configure the applications to obtain a token from the RDS database to authenticate by using IAM authentication.**

This solution correctly implements a secure, passwordless authentication mechanism. By attaching an IAM role to the EC2 instances, applications running on them can acquire temporary security credentials automatically, eliminating the need to store long-term keys. With IAM database authentication enabled on the RDS for PostgreSQL instance, the application uses these temporary credentials via the AWS SDK to generate a short-lived authentication token. This token is then used as the password for the database connection, fulfilling the requirement to authenticate securely without storing static, long-term credentials. Why Incorrect Options are Wrong: A. Secrets Manager is used to store and rotate traditional username/password credentials, which is a different mechanism from the token-based IAM database authentication that eliminates passwords entirely. B. This approach uses a static password

</details>

### 57. ce-227

A company's solutions architect is building a static website to be deployed in Amazon S3 for a production environment. The website integrates with an Amazon Aurora PostgreSQL database by using an AWS Lambda function. The website that is deployed to production will use a Lambda alias that points to a specific version of the Lambda function. The company must rotate the database credentials every 2 weeks. Lambda functions that the company deployed previously must be able to use the most recent credentials. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Store the database credentials in AWS Secrets Manager. Turn on rotation. Write code in the Lambda function to retrieve the credentials from Secrets Manager.**

The optimal solution is to use AWS Secrets Manager. This service is purpose-built for securely storing, managing, and automatically rotating secrets like database credentials. By configuring automatic rotation for the Aurora database credentials, Secrets Manager handles the entire lifecycle. The Lambda function's code is written to retrieve the secret from Secrets Manager at runtime. This design ensures that even old, immutable Lambda function versions (referenced by an alias) will always fetch the most current credentials upon invocation, fulfilling the requirement that previously deployed functions continue to work after a credential rotation. Why Incorrect Options are Wrong: B. Hardcoding credentials in the function code is a severe security risk and requires a new deployment for every rotation, which would break older, immutable function versions. C. Lambda environment variables are

</details>

### 58. et-228

A company has an API that receives real-time data from a fleet of monitoring devices. The API stores this data in an Amazon RDS DB instance for later analysis. The amount of data that the monitoring devices send to the API fluctuates. During periods of heavy traffic, the API often returns timeout errors. After an inspection of the logs, the company determines that the database is not capable of processing the volume of write traffic that comes from the API. A solutions architect must minimize the number of connections to the database and must ensure that data is not lost during periods of heavy traffic. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Modify the API to write incoming data to an Amazon Simple Queue Service (Amazon SQS) queue. Use an AWS Lambda function that Amazon SQS invokes to write data from the queue to the database.**

Amazon SQS: SQS is a fully managed message queuing service that decouples the components of a cloud application. It acts as a buffer between the API and the database, allowing for better handling of varying write traffic.  AWS Lambda: Using Lambda to process the data from the SQS queue helps in efficiently managing the connection to the database. Lambda functions can be scaled automatically based on the incoming workload.

</details>

### 59. dt-229

While launching an RDS DB instance, on which page I can select the Availability Zone?

<details><summary>Answer</summary>

**D. ADDITIONAL CONFIGURATION.**

</details>

### 60. et-229

A company manages its own Amazon EC2 instances that run MySQL databases. The company is manually managing replication and scaling as demand increases or decreases. The company needs a new solution that simplifies the process of adding or removing compute capacity to or from its database tier as needed. The solution also must offer improved performance, scaling, and durability with minimal effort from operations. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Migrate the databases to Amazon Aurora Serverless for Aurora MySQL.**

Amazon Aurora Serverless: Aurora Serverless is an on-demand, auto-scaling configuration for Amazon Aurora. It automatically adjusts the database capacity based on actual consumption, enabling seamless scaling without manual intervention. It is a fully managed service, reducing operational overhead.

</details>

### 61. dt-233

Can I use Provisioned IOPS with VPC?

<details><summary>Answer</summary>

**D. Yes for all RDS instances.**

</details>

### 62. et-236 `availability`

A company has a three-tier application for image sharing. The application uses an Amazon EC2 instance for the front-end layer, another EC2 instance for the application layer, and a third EC2 instance for a MySQL database. A solutions architect must design a scalable and highly available solution that requires the least amount of change to the application. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use load-balanced Multi-AZ AWS Elastic Beanstalk environments for the front-end layer and the application layer. Move the database to an Amazon RDS Multi-AZ DB instance. Use Amazon S3 to store and serve users’ images.**

AWS Elastic Beanstalk provides an easy way to deploy and manage applications. By using Multi-AZ environments, the front-end and application layers can automatically scale and provide high availability across multiple Availability Zones (AZs). Amazon RDS Multi-AZ DB Instance: Moving the database to an Amazon RDS Multi-AZ DB instance ensures high availability and automatic failover in the event of a failure in one Availability Zone. Amazon S3 for Storing and Serving Images: Using Amazon S3 for storing and serving users' images is a scalable and cost-effective solution. S3 is designed for high durability and availability, making it suitable for serving static content like images.

</details>

### 63. et-241 `least-ops`

An online learning company is migrating to the AWS Cloud. The company maintains its student records in a PostgreSQL database. The company needs a solution in which its data is available and online across multiple AWS Regions at all times. Which solution will meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Migrate the PostgreSQL database to an Amazon RDS for PostgreSQL DB instance. Create a read replica in another Region.**

Amazon RDS for PostgreSQL allows you to create read replicas in different AWS Regions. This provides cross-Region availability and redundancy. Additionally, it allows you to offload read traffic from the primary database.

</details>

### 64. gh-241 `least-ops`

n online learning company is migrating to the AWS Cloud. The company maintains its student records in a PostgreSQL database. The company needs a solution in which its data is available and online across multiple AWS Regions at all times.
Which solution will meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Migrate the PostgreSQL database to an Amazon RDS for PostgreSQL DB instance. Create a read replica in another Region.**

Amazon RDS for PostgreSQL allows you to create read replicas in different AWS Regions. This provides cross-Region availability and redundancy. Additionally, it allows you to offload read traffic from the primary database.

</details>

### 65. ce-244

A company is migrating its workloads to AWS. The company has sensitive and critical data in on- premises relational databases that run on SQL Server instances. The company wants to use the AWS Cloud to increase security and reduce operational overhead for the databases. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the databases to a Multi-AZ Amazon RDS for SQL Server DB instance. Use an AWS Key Management Service (AWS KMS) AWS managed key for encryption.**

The requirements are to increase security and reduce operational overhead for on-premises SQL Server databases. Amazon RDS is a managed service that significantly reduces operational overhead by automating tasks like patching, backups, and hardware provisioning. Using a Multi-AZ deployment provides high availability and durability. Encrypting the RDS instance with an AWS Key Management Service (AWS KMS) key enhances security by protecting data at rest. This combination directly meets all the company's stated requirements for a managed, secure, and highly available database solution. Why Incorrect Options are Wrong: A. Using EC2 instances for databases does not reduce operational overhead; it shifts it to the cloud, as the customer still manages the OS and database software. C. Amazon S3 is an object storage service, not a relational database. Migrating would require a complete applicatio

</details>

### 66. dt-244

Your customer wishes to deploy an enterprise application to AWS which will consist of several web servers, several application servers and a small (50GB) Oracle database information is stored, both in the database and the file systems of the various servers. The backup system must support database recovery whole server and whole disk restores, and individual file restores with a recovery time of no more than two hours. They have chosen to use RDS Oracle as the database. Which backup architecture will meet these requirements?

<details><summary>Answer</summary>

**A. Backup RDS using automated daily DB backups Backup the EC2 instances using AMIs and supplement with file-level backup to S3 using traditional enterprise backup software to provide file level restore.**

</details>

### 67. et-244 `availability`

A company is using a content management system that runs on a single Amazon EC2 instance. The EC2 instance contains both the web server and the database software. The company must make its website platform highly available and must enable the website to scale to meet user demand. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Move the database to Amazon Aurora with a read replica in another Availability Zone. Create an Amazon Machine Image (AMI) from the EC2 instance. Configure an Application Load Balancer in two Availability Zones. Attach an Auto Scaling group that uses the AMI across two Availability Zones.**

This option provides both high availability and scalability. Using Amazon Aurora with a read replica in another Availability Zone ensures data redundancy and failover capabilities. Configuring an Application Load Balancer across two Availability Zones and using Auto Scaling allows for scalability.

</details>

### 68. dt-246

Is the SQL Server Audit feature supported in the Amazon RDS SQL Server engine?

<details><summary>Answer</summary>

**B. No.**

</details>

### 69. dt-252

What are the two types of licensing options available for using Amazon RDS for Oracle?

<details><summary>Answer</summary>

**B. BYOL and License Included.**

</details>

### 70. dt-258

[...] embodies the 'share-nothing' architecture and essentially involves breaking a large database into several smaller databases. Common ways to split a database include: 1. Splitting tables that are not joined in the same query onto different hosts or 2. Duplicating a table across multiple hosts and then using a hashing algorithm to determine which host receives a given update.

<details><summary>Answer</summary>

**A. $harding.**

</details>

### 71. dt-260

Your company plans to host a large donation website on Amazon Web Services (AWS). You anticipate a large and undetermined amount of traffic that will create many database writes. To be certain that you do not drop any writes to a database hosted on AWS. Which service should you use?

<details><summary>Answer</summary>

**B. Amazon Simple Queue Service (SOS) for capturing the writes and draining the queue to write to the database.**

</details>

### 72. dt-262 `availability`

You are migrating a legacy client-server application to AWS. The application responds to a specific DNS domain (e.g. <www.example.com>) and has a 2-tier architecture, with multiple application servers and a database server. Remote clients use TCP to connect to the application servers. The application servers need to know the IP address of the clients in order to function properly and are currently taking that information from the TCP socket. A Multi-AZ RDS MySQL instance will be used for the database. During the migration you can change the application code, but you have to file a change request. How would you implement the architecture on AWS in order to maximize scalability and high availability?

<details><summary>Answer</summary>

**D. File a change request to implement Proxy Protocol support in the application. Use an ELB with a TCP Listener and Proxy Protocol enabled to distribute load on two application servers in different AZs.**

</details>

### 73. dt-265

You have just set up a large site for a client which involved a huge database which you set up with Amazon RDS to run as a Multi-AZ deployment. You now start to worry about what will happen if the database instance fails. Which statement best describes how this database will function if there is a database failure?

<details><summary>Answer</summary>

**A. Updates to your DB Instance are synchronously replicated across Availability Zones to the standby in order to keep both in sync and protect your latest database updates against DB Instance failure.**

</details>

### 74. ce-267

A company has a relational database workload that runs on Amazon Aurora MySQL. According to new compliance standards, the company must rotate all database credentials every 30 days. The company needs a solution that maximizes security and minimizes development effort. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Store the database credentials in AWS Secrets Manager. Configure automatic credential rotation for every 30 days.**

AWS Secrets Manager is the ideal service for this requirement. It is specifically designed to manage, retrieve, and rotate database credentials, API keys, and other secrets securely. It offers built-in, automated rotation capabilities for supported services like Amazon Aurora. By configuring automatic rotation for every 30 days, the company meets its compliance standards with maximum security and minimal development effort, as no custom code (like a Lambda function) is needed for the rotation logic. The entire lifecycle of the secret is managed by the AWS service. Why Incorrect Options are Wrong: B. AWS Systems Manager Parameter Store can store secrets but lacks the built-in, automated rotation feature of Secrets Manager, requiring a custom Lambda function and more development effort. C. Storing credentials in a configuration file and manually modifying them is an insecure practice and d

</details>

### 75. gh-268

A gaming company has a web application that displays scores. The application runs on Amazon EC2 instances behind an Application Load Balancer. The application stores data in an Amazon RDS for MySQL database. Users are starting to experience long delays and interruptions that are caused by database read performance. The company wants to improve the user experience while minimizing changes to the application’s architecture.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**Put Amazon ElastiCache between the application and the Amazon RDS for MySQL database so repeated score reads are served from the cache instead of the database.**

The bottleneck is read volume against the MySQL database, so the fix has to take reads off it. ElastiCache serves the hot, frequently requested score data from memory, which cuts both the delays and the load on RDS without re-platforming the application. RDS Proxy only manages and reuses database connections - useful when an application opens too many connections or needs faster failover, but it adds no read capacity. Migrating to Lambda or to DynamoDB would be a far larger change than the question allows.

</details>

### 76. et-269

An ecommerce company has noticed performance degradation of its Amazon RDS based web application. The performance degradation is attributed to an increase in the number of read-only SQL queries triggered by business analysts. A solutions architect needs to solve the problem with minimal changes to the existing web application. What should the solutions architect recommend?

<details><summary>Answer</summary>

**C. Create a read replica of the primary database and have the business analysts run their queries.**

Creating a read replica is a common approach to offload read-only queries from the primary database, improving overall performance. A read replica is an asynchronous copy of the primary database that allows for read-only operations.  Read replicas can be transparently used by the web application without requiring changes to the application logic. Business analysts can direct their read-only queries to the read replica, reducing the load on the primary database.

</details>

### 77. et-273

A rapidly growing ecommerce company is running its workloads in a single AWS Region. A solutions architect must create a disaster recovery (DR) strategy that includes a different AWS Region. The company wants its database to be up to date in the DR Region with the least possible latency. The remaining infrastructure in the DR Region needs to run at reduced capacity and must be able to scale up if necessary. Which solution will meet these requirements with the LOWEST recovery time objective (RTO)?

<details><summary>Answer</summary>

**B. Use an Amazon Aurora global database with a warm standby deployment.**

Amazon Aurora supports a global database feature that allows you to create read replicas in multiple AWS Regions. In a warm standby deployment, you can have a read replica in the DR Region that stays warm, meaning it is ready to take over in case of a failover.

</details>

### 78. gh-273

273Topic 1
A rapidly growing ecommerce company is running its workloads in a single AWS Region. A solutions architect must create a disaster recovery (DR) strategy that includes a different AWS Region. The company wants its database to be up to date in the DR Region with the least possible latency. The remaining infrastructure in the DR Region needs to run at reduced capacity and must be able to scale up if necessary.
Which solution will meet these requirements with the LOWEST recovery time objective (RTO)?

<details><summary>Answer</summary>

**B. Use an Amazon Aurora global database with a warm standby deployment.**

Amazon Aurora supports a global database feature that allows you to create read replicas in multiple AWS Regions.
In a warm standby deployment, you can have a read replica in the DR Region that stays warm, meaning it is ready to take over in case of a failover.

</details>

### 79. et-279

A company has an application that is backed by an Amazon DynamoDB table. The company’s compliance requirements specify that database backups must be taken every month, must be available for 6 months, and must be retained for 7 years. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an AWS Backup plan to back up the DynamoDB table on the first day of each month. Specify a lifecycle policy that transitions the backup to cold storage after 6 months. Set the retention period for each backup to 7 years.**

AWS Backup will automatically take full backups of the DynamoDB table on the schedule defined in the backup plan (the first of each month). The lifecycle policy can transition backups to cold storage after 6 months, meeting that requirement. Setting a 7-year retention period in the backup plan will ensure each backup is retained for 7 years as required. AWS Backup manages the backup jobs and lifecycle policies, requiring no custom scripting or management.

</details>

### 80. dt-281

Read Replicas require a transactional storage engine and are only supported for the [...] storage engine.

<details><summary>Answer</summary>

**C. InnoDB.**

</details>

### 81. et-281

A company runs a fleet of web servers using an Amazon RDS for PostgreSQL DB instance. After a routine compliance check, the company sets a standard that requires a recovery point objective (RPO) of less than 1 second for all its production databases. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Enable a Multi-AZ deployment for the DB instance.**

A Multi-AZ (Availability Zone) deployment for Amazon RDS provides high availability and failover support for DB instances. In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone.

</details>

### 82. dt-284

Can I initiate a 'forced failover' for my MySQL Multi-AZ DB Instance deployment?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 83. dt-289

A gaming company comes to you and asks you to build them infrastructure for their site. They are not sure how big they will be as with all start ups they have limited money and big ideas. What they do tell you is that if the game becomes successful, like one of their previous games, it may rapidly grow to millions of users and generate tens (or even hundreds) of thousands of writes and reads per second. After considering all of this, you decide that they need a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. Which of the following databases do you think would best fit their needs?

<details><summary>Answer</summary>

**A. Amazon DynamoDB.**

</details>

### 84. ce-292

A company wants to deploy a new public web application on AWS. The application includes a web server tier that uses Amazon EC2 instances. The application also includes a database tier that uses an Amazon RDS for MySQL DB instance. The application must be secure and accessible for global customers that have dynamic IP addresses. How should a solutions architect configure the security groups to meet these requirements?

<details><summary>Answer</summary>

**A. Configure the security group for the web servers to allow inbound traffic on port 443 from 0.0.0.0/0. Configure the security group for the DB instance to allow inbound traffic on port 3306 from the security group of the web servers.**

For a public web application serving global customers with dynamic IPs, the web server's security group must allow inbound HTTPS traffic (port 443) from any IP address, represented by the CIDR block 0.0.0.0/0. This ensures accessibility for all users. To secure the database tier, it should not be exposed to the public internet. The best practice is to configure the database instance's security group to only allow inbound traffic on the database port (3306 for MySQL) from the security group of the web servers. This creates a tightly controlled connection path, allowing only the application instances to communicate with the database. Why Incorrect Options are Wrong: B. Allowing traffic only from specific customer IP addresses is not feasible because the customers are global and have dynamic (changing) IP addresses. C. This option has the same infeasible IP restriction as B and incorrectly

</details>

### 85. ce-294

A company stores sensitive financial information for an application in Amazon RDS for MySQL. The company requires a stateful solution to ensure that only a specific on-premises IP address can access the RDS database instances. The company wants to rotate database credentials automatically. The company does not want to hardcode the credentials into the application. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use security groups to allow access only from the specified IP addresses. Store the database credentials in AWS Secrets Manager. Configure automatic rotation for the credentials.**

This solution correctly addresses all three requirements. Security groups are stateful firewalls that can be configured with inbound rules to allow traffic only from the specified on-premises IP address, meeting the stateful access control requirement. AWS Secrets Manager is the purpose-built service for securely storing, managing, and rotating secrets like database credentials. It integrates directly with Amazon RDS to handle automatic credential rotation without hardcoding them in the application, fulfilling the other two requirements with a managed, secure solution. Why Incorrect Options are Wrong: B. IAM policies are not the primary mechanism for controlling network traffic to an RDS instance; security groups are. Managing credentials in code is insecure. C. Network ACLs are stateless, which does not meet the requirement for a stateful solution. Storing credentials in S3 is less secu

</details>

### 86. dt-294

In the HQ region you run an hourly batch process reading data from every region to compute cross regional reports that are sent by email to all offices this batch process must be completed as fast as possible to quickly optimize logistics how do you build the database architecture in order to meet the requirements'?

<details><summary>Answer</summary>

**A. For each regional deployment, use RDS MySQL with a master in the region and a read replica in the HQ region.**

</details>

### 87. dt-308

When automatic failover occurs, Amazon RDS will emit a DB Instance event to inform you that automatic failover occurred. You can use the [...] to return information about events related to your DB Instance.

<details><summary>Answer</summary>

**C. DescribeEvents.**

</details>

### 88. et-314

A company has an on-premises MySQL database used by the global sales team with infrequent access patterns. The sales team requires the database to have minimal downtime. A database administrator wants to migrate this database to AWS without selecting a particular instance type in anticipation of more users in the future. Which service should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Amazon Aurora Serverless for MySQL**

Amazon Aurora Serverless: Aurora Serverless is a fully managed, on-demand, and auto-scaling relational database engine provided by AWS. It is suitable for infrequent access patterns and allows the database to automatically start up, shut down, and scale capacity based on actual usage.

</details>

### 89. dt-315

You have just been given a scope for a new client who has an enormous amount of data (petabytes) that he constantly needs analysed. Currently he is paying a huge amount of money for a data warehousing company to do this for him and is wondering if AWS can provide a cheaper solution. Do you think AWS has a solution for this?

<details><summary>Answer</summary>

**C. Yes. Amazon Redshift.**

</details>

### 90. ce-316

A global ecommerce company runs its critical workloads on AWS. The workloads use an Amazon RDS for PostgreSQL DB instance that is configured for a Multi-AZ deployment. Customers have reported application timeouts when the company undergoes database failovers. The company needs a resilient solution to reduce failover time Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon RDS Proxy. Assign the proxy to the DB instance.**

Amazon RDS Proxy is a fully managed, highly available database proxy that makes applications more resilient to database failures. It maintains a pool of established connections to the RDS database instance. During a database failover, the application's connections to the proxy remain active. The proxy automatically detects the failover and routes traffic to the newly promoted primary instance, often in seconds, without dropping application connections. This significantly reduces the failover time experienced by the application, preventing timeouts that can occur with traditional DNS-based failover mechanisms where applications must re-establish connections. Why Incorrect Options are Wrong: B. A read replica is used for scaling read traffic and does not reduce the failover time of the primary instance in a Multi-AZ configuration. C. Performance Insights is a monitoring and performance tun

</details>

### 91. ce-320 `cost`

An ecommerce company wants a disaster recovery solution for its Amazon RDS DB instances that run Microsoft SQL Server Enterprise Edition. The company's current recovery point objective (RPO) and recovery time objective (RTO) are 24 hours. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Copy automatic snapshots to another Region every 24 hours.**

The requirements are a Recovery Point Objective (RPO) and Recovery Time Objective (RTO) of 24 hours, with a focus on cost-effectiveness. Copying automated daily snapshots to another region is a "backup and restore" disaster recovery strategy. This approach perfectly aligns with a 24-hour RPO, as the latest data available for recovery would be from the last daily snapshot. The RTO of 24 hours is also met, as restoring an RDS instance from a snapshot is a standard procedure that can be completed well within this timeframe. This method is the most cost-effective because it only incurs costs for snapshot storage and data transfer, avoiding the expense of running a continuous, standby database instance in the disaster recovery region. Why Incorrect Options are Wrong: A. A cross-Region read replica provides a much lower RPO (seconds/minutes) and RTO (minutes) than required. This "warm standby"

</details>

### 92. ce-321 `least-ops`

A company is migrating its on-premises Oracle database to an Amazon RDS for Oracle database. The company needs to retain data for 90 days to meet regulatory requirements. The company must also be able to restore the database to a specific point in time for up to 14 days. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create a backup plan that has a retention period of 90 days by using AWS Backup for Amazon RDS.**

AWS Backup is a centralized, policy-based service designed to manage backups across multiple AWS services, including Amazon RDS. It can be configured to meet both requirements with minimal effort. A single backup plan can enable continuous backups for point-in-time recovery (PITR) for up to 35 days, satisfying the 14-day PITR requirement. The same plan can also manage periodic snapshots with a lifecycle policy to retain them for 90 days, meeting the regulatory requirement. This approach automates the entire backup lifecycle, including creation, retention, and deletion, representing the solution with the least operational overhead. Why Incorrect Options are Wrong: A. The maximum retention period for native Amazon RDS automated backups is 35 days, which does not meet the 90-day regulatory requirement. B. Manual snapshots do not support point-in-time recovery (PITR). This option also requir

</details>

### 93. dt-323

In the Amazon RDS Oracle DB engine, the Database Diagnostic Pack and the Database Tuning Pack are only available with [...].

<details><summary>Answer</summary>

**C. Oracle Enterprise Edition.**

</details>

### 94. dt-324

Will my standby RDS instance be in the same Availability Zone as my primary?

<details><summary>Answer</summary>

**D. No.**

</details>

### 95. dt-325

An administrator is using Amazon CloudFormation to deploy a three tier web application that consists of a web tier and application tier that will utilize Amazon DynamoDB for storage. When creating the CloudFormation template, which of the following would allow the application instance access to the DynamoDB tables without exposing API credentials?

<details><summary>Answer</summary>

**C. Create an Identity and Access Management Role that has the required permissions to read and write from the required DynamoDB table and reference the Role in the instance profile property of the application instance.**

</details>

### 96. ce-326 `least-ops`

A company has developed a non-production application that is composed of multiple microservices for each of the company's business units. A single development team maintains all the microservices. The current architecture uses a static web frontend and a Java-based backend that contains the application logic. The architecture also uses a MySQL database that the company hosts on an Amazon EC2 instance. The company needs to ensure that the application is secure and available globally. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon CloudFront and Amazon S3 to host the static web frontend. Refactor the microservices to use AWS Lambda functions that the microservices access by using Amazon API Gateway. Migrate the MySQL database to Amazon RDS for MySQL.**

This solution provides the most optimal architecture to meet all requirements with the least operational overhead. 1. Frontend: Using Amazon S3 to host the static web content and Amazon CloudFront as a Content Delivery Network (CDN) is the standard, best-practice approach. CloudFront caches the content at edge locations globally, ensuring low-latency access for users worldwide and enhancing security with features like AWS Shield Standard. 2. Backend: Refactoring the microservices to use AWS Lambda functions fronted by Amazon API Gateway creates a serverless, highly scalable, and secure backend. This pattern eliminates server management (EC2 instances), significantly reducing operational overhead. API Gateway provides a managed entry point for the APIs. 3. Database: Migrating the self-managed MySQL database on EC2 to Amazon RDS for MySQL offloads database administration tasks such as patc

</details>

### 97. ce-328 `least-ops`

A company runs a production database on Amazon RDS for MySQL. The company wants to upgrade the database version for security compliance reasons. Because the database contains critical data, the company wants a quick solution to upgrade and test functionality without losing any data. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use Amazon RDS Blue/Green Deployments to deploy and test production changes.**

Amazon RDS Blue/Green Deployments are specifically designed for this use case. This feature creates a synchronized, separate staging environment (green) that mirrors the production database (blue). You can upgrade the green environment and conduct thorough testing without impacting the production workload. The service uses logical replication to keep the green environment up-to-date. Once testing is complete, you can promote the green environment to become the new production environment with a switchover that typically completes in under a minute, ensuring minimal downtime and no data loss. This is the most direct solution with the least operational overhead. Why Incorrect Options are Wrong: A. A manual snapshot and in-place upgrade is risky. Testing occurs on the live production database after the upgrade, and rolling back requires a time-consuming restore, leading to data loss since th

</details>

### 98. ce-329 `cost`

An online gaming company is transitioning user data storage to Amazon DynamoDB to support the company's growing user base. The current architecture includes DynamoDB tables that contain user profiles, achievements, and in-game transactions. The company needs to design a robust, continuously available, and resilient DynamoDB architecture to maintain a seamless gaming experience for users. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Use DynamoDB global tables for automatic multi-Region replication. Deploy tables in multiple AWS Regions. Use provisioned capacity mode. Enable auto scaling.**

This solution provides the highest availability and resilience by using DynamoDB global tables, which offer a fully managed, active-active, multi-Region replication architecture. This design ensures continuous availability even during a regional outage. For a gaming application, which often has predictable traffic patterns (e.g., peak usage in evenings and on weekends), using provisioned capacity with auto scaling is the most cost-effective approach. It allows the company to pay for a baseline capacity and automatically scale to handle fluctuations, which is typically less expensive than the on-demand mode for such workloads. Why Incorrect Options are Wrong: A. This option is contradictory. DynamoDB global tables inherently require deployment in multiple AWS Regions, not a single one. On-demand capacity is also less cost-effective for predictable workloads. B. A single-Region architectur

</details>

### 99. dt-335

How would you improve page load times for your users? (Choose 3 answers)

<details><summary>Answer</summary>

**B. Add an Amazon ElastiCache caching layer to your application for storing sessions and frequent DB queries.; C. Configure Amazon CloudFront dynamic content support to enable caching of re-usable content from your site.; D. Switch Amazon RDS database to the high memory extra large Instance type.**

</details>

### 100. dt-336

Typically, you want your application to check whether a request generated an error before you spend any time processing results. The easiest way to find out if an error occurred is to look for an [...] node in the response from the Amazon RDS API.

<details><summary>Answer</summary>

**B. error.**

</details>

### 101. et-337

A company has deployed a web application on AWS. The company hosts the backend database on Amazon RDS for MySQL with a primary DB instance and five read replicas to support scaling needs. The read replicas must lag no more than 1 second behind the primary DB instance. The database routinely runs scheduled stored procedures. As traffic on the website increases, the replicas experience additional lag during periods of peak load. A solutions architect must reduce the replication lag as much as possible. The solutions architect must minimize changes to the application code and must minimize ongoing operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Migrate the database to Amazon Aurora MySQL. Replace the read replicas with Aurora Replicas, and configure Aurora Auto Scaling. Replace the stored procedures with Aurora MySQL native functions.**

Amazon Aurora MySQL: Aurora Replicas in Amazon Aurora MySQL are designed to have minimal replication lag compared to traditional MySQL read replicas. Aurora is built for high performance and low replication lag, making it a suitable choice for reducing lag in read replicas.  Aurora Auto Scaling: Aurora Auto Scaling allows you to automatically adjust the number of Aurora Replicas based on actual application usage. This ensures that you have the right amount of read capacity during periods of peak load, minimizing replication lag.

</details>

### 102. ce-338 `availability`

A company is developing a highly available natural language processing (NLP) application. The application handles large volumes of concurrent requests. The application performs NLP tasks such as entity recognition, sentiment analysis, and key phrase extraction on text data. The company needs to store data that the application processes in a highly available and scalable database. Options:

<details><summary>Answer</summary>

**A. Create an Amazon API Gateway REST API endpoint to handle incoming requests. Configure the REST API to invoke an AWS Lambda function for each request. Configure the Lambda function to call Amazon Comprehend to perform NLP tasks on the text data. Store the processed data in Amazon DynamoDB.**

This option proposes a fully serverless architecture that is inherently highly available and scalable. Amazon API Gateway is designed to handle API requests at scale. AWS Lambda provides serverless compute that scales automatically with the number of concurrent requests. Amazon Comprehend is the specific AWS service designed for the NLP tasks mentioned: entity recognition, sentiment analysis, and key phrase extraction. Finally, Amazon DynamoDB is a fully managed, serverless NoSQL database that provides single-digit millisecond performance at any scale, making it the ideal choice for a highly available and scalable data store for this workload. Why Incorrect Options are Wrong: B. Amazon Translate performs language translation, not the required NLP tasks. Amazon ElastiCache is an in-memory cache, not a durable database for primary data storage. C. This EC2-based architecture requires more

</details>

### 103. et-338 `cost`

A solutions architect must create a disaster recovery (DR) plan for a high-volume software as a service (SaaS) platform. All data for the platform is stored in an Amazon Aurora MySQL DB cluster. The DR plan must replicate data to a secondary AWS Region. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Set up an Aurora global database for the DB cluster and, once setup is complete, remove the DB instance from the secondary Region, leaving a headless secondary cluster.**

Aurora global database replication happens in the shared storage layer, not through a database instance, so data keeps arriving in the secondary Region even when that cluster has no instance running. For a plan that only has to hold a replica of the data, this is the cheapest shape: you pay for replicated storage and cross-Region replication traffic but no idle compute. When you need to recover, you add an instance to the secondary cluster and promote it. Keeping a DB instance running in the secondary Region also works, but it costs more, so it loses on the MOST cost-effectively test.

</details>

### 104. et-340

A media company hosts its website on AWS. The website application’s architecture includes a fleet of Amazon EC2 instances behind an Application Load Balancer (ALB) and a database that is hosted on Amazon Aurora. The company’s cybersecurity team reports that the application is vulnerable to SQL injection. How should the company resolve this issue?

<details><summary>Answer</summary>

**A. Use AWS WAF in front of the ALB. Associate the appropriate web ACLs with AWS WAF.**

AWS WAF (Web Application Firewall): AWS WAF is designed to protect web applications from common web exploits, including SQL injection. It allows you to create web access control lists (web ACLs) to define rules that filter and monitor HTTP traffic to your application.  Associating Web ACLs with AWS WAF: By using AWS WAF in front of the ALB, you can define rules to block or allow web requests based on conditions that you specify. This includes protection against SQL injection attempts. AWS WAF provides a range of conditions and rulesets that you can use to mitigate common security threats.

</details>

### 105. dt-341

You are building infrastructure for a data warehousing solution and an extra request has come through that there will be a lot of business reporting queries running all the time and you are not sure if your current DB instance will be able to handle it. What would be the best solution for this?

<details><summary>Answer</summary>

**B. Read Replicas.**

</details>

### 106. ce-343 `availability`

A company is building a serverless application to process clickstream data from its website. The clickstream data is sent to an Amazon Kinesis Data Streams data stream from the application web servers. The company wants to enrich the clickstream data by joining the clickstream data with customer profile data from an Amazon Aurora Multi-AZ database. The company wants to use Amazon Redshift to analyze the enriched dat a. The solution must be highly available. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use an AWS Lambda function to process and enrich the clickstream data. Use the same Lambda function to write the clickstream data to Amazon S3. Use Amazon Redshift Spectrum to query the enriched data in Amazon S3.**

This solution provides a highly available and serverless architecture that meets all requirements. An AWS Lambda function is triggered by records in the Kinesis Data Stream. This function can connect to the Amazon Aurora database to fetch customer data, enrich the incoming clickstream records, and then write the resulting enriched data to an Amazon S3 bucket. Amazon Redshift Spectrum can then be used to directly query this structured data in S3 without needing to load it into Redshift storage, fulfilling the analysis requirement. This entire pipeline (Kinesis, Lambda, S3, Redshift Spectrum) is composed of managed, highly available services, aligning with the problem's constraints. Why Incorrect Options are Wrong: B: EC2 Spot Instances are not suitable for highly available workloads as they can be terminated with short notice, violating a core requirement. The solution is also not serverl

</details>

### 107. et-343 `least-ops`

A solutions architect is designing a company’s disaster recovery (DR) architecture. The company has a MySQL database that runs on an Amazon EC2 instance in a private subnet with scheduled backup. The DR design needs to include multiple AWS Regions. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Migrate the MySQL database to an Amazon Aurora global database. Host the primary DB cluster in the primary Region. Host the secondary DB cluster in the DR Region.**

</details>

### 108. dt-345

After you recommend Amazon Redshift to a client as an alternative solution to paying data warehouses to analyze his data, your client asks you to explain why you are recommending Redshift. Which of the following would be a reasonable response to his request?

<details><summary>Answer</summary>

**D. All answers listed are a reasonable response to his question.**

</details>

### 109. dt-347

Does Amazon DynamoDB support both increment and decrement atomic operations?

<details><summary>Answer</summary>

**C. Yes, both increment and decrement operations.**

</details>

### 110. et-349 `security`

A company stores confidential data in an Amazon Aurora PostgreSQL database in the ap-southeast-3 Region. The database is encrypted with an AWS Key Management Service (AWS KMS) customer managed key. The company was recently acquired and must securely share a backup of the database with the acquiring company’s AWS account in ap-southeast-3. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create a database snapshot. Add the acquiring company’s AWS account to the KMS key policy. Share the snapshot with the acquiring company’s AWS account.**

sharing encrypted snapshots involves granting permission not only on the snapshot itself but also on the underlying AWS Key Management Service (KMS) key used for encryption. By adding the acquiring company's AWS account to the KMS key policy, you ensure that they have the necessary permissions to decrypt and access the snapshot. Sharing the snapshot with the acquiring company's AWS account completes the process, allowing them to restore the database from the shared snapshot.

</details>

### 111. et-350 `availability`

A company uses a 100 GB Amazon RDS for Microsoft SQL Server Single-AZ DB instance in the us-east-1 Region to store customer transactions. The company needs high availability and automatic recovery for the DB instance. The company must also run reports on the RDS database several times a year. The report process causes transactions to take longer than usual to post to the customers’ accounts. The company needs a solution that will improve the performance of the report process. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Modify the DB instance from a Single-AZ DB instance to a Multi-AZ deployment.**

Enabling Multi-AZ deployment provides high availability by replicating the database to a standby instance in another Availability Zone. This helps in automatic failover and recovery in case of a primary instance failure. C. Create a read replica of the DB instance in a different Availability Zone. Point all requests for reports to the read replica:  By creating a read replica in a different Availability Zone, you offload the reporting workload from the primary instance, reducing the impact on transaction processing. Read replicas can be used to scale read-heavy workloads and improve overall performance.

</details>

### 112. et-353 `cost` `availability`

A company hosts a three-tier web application on Amazon EC2 instances in a single Availability Zone. The web application uses a self-managed MySQL database that is hosted on an EC2 instance to store data in an Amazon Elastic Block Store (Amazon EBS) volume. The MySQL database currently uses a 1 TB Provisioned IOPS SSD (io2) EBS volume. The company expects traffic of 1,000 IOPS for both reads and writes at peak traffic. The company wants to minimize any disruptions, stabilize performance, and reduce costs while retaining the capacity for double the IOPS. The company wants to move the database tier to a fully managed solution that is highly available and fault tolerant. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use a Multi-AZ deployment of an Amazon RDS for MySQL DB instance with a General Purpose SSD (gp2) EBS volume.**

</details>

### 113. et-354

A company hosts a serverless application on AWS. The application uses Amazon API Gateway, AWS Lambda, and an Amazon RDS for PostgreSQL database. The company notices an increase in application errors that result from database connection timeouts during times of peak traffic or unpredictable traffic. The company needs a solution that reduces the application failures with the least amount of change to the code. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Enable RDS Proxy on the RDS DB instance.**

RDS Proxy is a fully managed, highly available database proxy that can handle database connections for serverless and highly scalable applications. It helps manage database connections efficiently, reducing issues related to connection timeouts and errors.

</details>

### 114. dt-359

After setting up several database instances in Amazon Relational Database Service (Amazon RDS) you decide that you need to track the performance and health of your databases. How can you do this?

<details><summary>Answer</summary>

**C. All of the items listed will track the performance and health of a database.**

</details>

### 115. et-361 `least-ops`

A company hosts a multiplayer gaming application on AWS. The company wants the application to read data with sub-millisecond latency and run one-time queries on historical data. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Use Amazon DynamoDB with DynamoDB Accelerator (DAX) for data that is frequently accessed. Export the data to an Amazon S3 bucket by using DynamoDB table export. Run one-time queries on the data in Amazon S3 by using Amazon Athena.**

Amazon DynamoDB with DynamoDB Accelerator (DAX):  DynamoDB is a highly scalable and low-latency NoSQL database, suitable for frequently accessed data. DynamoDB Accelerator (DAX) is a caching layer that provides sub-millisecond read latencies for DynamoDB. Export Data to Amazon S3:  Use DynamoDB table export to periodically export historical data to an Amazon S3 bucket. This allows you to store historical data in a cost-effective manner while still benefiting from DynamoDB for frequently accessed data. Amazon Athena for One-time Queries:  Amazon Athena allows you to run SQL queries directly on data stored in Amazon S3. By using Athena, you can perform one-time queries on the historical data without the need to manage a separate database.

</details>

### 116. et-365

A company runs a web application that is backed by Amazon RDS. A new database administrator caused data loss by accidentally editing information in a database table. To help recover from this type of incident, the company wants the ability to restore the database to its state from 5 minutes before any change within the last 30 days. Which feature should the solutions architect include in the design to meet this requirement?

<details><summary>Answer</summary>

**C. Automated backups**

Amazon RDS (Relational Database Service) can automatically create backups of your database every day. These backups are like snapshots of your entire database, capturing all the data. They happen automatically, so you don't have to remember to do it. You can decide how long you want to keep these backup snapshots. For example, you might choose to keep them for up to 35 days. This is like saying, "I want to keep the pictures of my database for the last 35 days."

</details>

### 117. ce-366

A company runs a mobile game app that stores session data (up to 256 KB) for up to 48 hours. The data updates frequently and must be deleted automatically after expiration. Restorability is also required. Options:

<details><summary>Answer</summary>

**A. Use an Amazon DynamoDB table to store the session data. Enable point-in-time recovery (PITR) and TTL.**

The scenario requires a storage solution for frequently updated session data that needs automatic expiration and restorability. Amazon DynamoDB is a fully managed NoSQL database designed for high-performance applications, making it ideal for session stores. The Time to Live (TTL) feature in DynamoDB allows you to define a per-item timestamp for automatic deletion after it expires, perfectly matching the 48-hour requirement without consuming write capacity. Furthermore, enabling point-in-time recovery (PITR) provides continuous backups, fulfilling the restorability requirement by allowing the table to be restored to any second during the preceding 35 days. Why Incorrect Options are Wrong: B. Use Amazon MemoryDB and enable PITR and TTL. MemoryDB is an in-memory database providing microsecond latency. While it supports the required features, it is generally more expensive and designed for w

</details>

### 118. ce-371 `least-ops`

A company needs a solution to back up and protect critical AWS resources. The company needs to regularly take backups of several Amazon EC2 instances and Amazon RDS for PostgreSQL databases. To ensure high resiliency, the company must have the ability to validate and restore backups. Which solution meets the requirement with LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Backup to create a backup schedule for the resources. Use AWS Backup to create a restoration testing plan for the required resources.**

AWS Backup is a fully managed service designed to centralize and automate data protection across AWS services, including Amazon EC2 and Amazon RDS. It allows users to create backup plans for scheduled, policy-based backups. A key feature that directly addresses the question's requirements is AWS Backup's restore testing capability. This feature automates the process of performing a restore from a backup to a temporary environment and then automatically cleans up the resources after the test is complete. This provides a mechanism to validate backups with minimal manual intervention, thereby meeting the requirement for the least operational overhead. Why Incorrect Options are Wrong: B. Take snapshots of the EC2 instances and RDS DB instances. Create AWS Batch jobs to validate and restore the snapshots. This approach requires significant custom development and management of AWS Batch jobs,

</details>

### 119. ce-373

A company stores a large volume of critical data in Amazon RDS for PostgreSQL tables. The company is developing several new features for an upcoming product launch. Some of the new features require many table alterations. The company needs a solution to test the altered tables for several days. After testing, the solution must make the new features available to customers in production. Which solution will meet these requirements with the HIGHEST availability?

<details><summary>Answer</summary>

**D. Use an Amazon RDS blue/green deployment to deploy a new test instance of the database. Make database table updates in the test instance. When the testing is finished, promote the test instance to become the new production instance.**

Amazon RDS Blue/Green Deployments are specifically designed for this use case. This feature creates a fully managed, synchronized staging environment (the "green" environment) that is a clone of the production database (the "blue" environment). You can safely perform schema alterations and conduct testing on the green environment without impacting production. When testing is complete, you can promote the green environment to become the new production environment. The switchover is typically completed in under a minute with no data loss, ensuring the highest possible availability for the critical application. Why Incorrect Options are Wrong: A. Restoring a backup to the production database is a time-consuming operation that would cause significant downtime, directly violating the high availability requirement. B. Performing schema changes and testing directly on a production database is e

</details>

### 120. ce-374

A company hosts an ecommerce application that stores all data in a single Amazon RDS for MySQL DB instance that is fully managed by AWS. The company needs to mitigate the risk of a single point of failure. Which solution will meet these requirements with the LEAST implementation effort?

<details><summary>Answer</summary>

**A. Modify the RDS DB instance to use a Multi-AZ deployment. Apply the changes during the next maintenance window.**

The most direct and efficient way to mitigate a single point of failure for an Amazon RDS DB instance is to enable a Multi-AZ deployment. This is a simple configuration change that can be applied to the existing instance. AWS then automatically provisions and maintains a synchronous standby replica in a different Availability Zone (AZ). In the event of a failure of the primary instance or its AZ, Amazon RDS performs an automatic failover to the standby replica, minimizing downtime. This approach directly addresses the high availability requirement with the least possible implementation and operational effort. Why Incorrect Options are Wrong: B: Migrating from RDS MySQL to DynamoDB is a complex heterogeneous migration. It requires significant effort in schema redesign, data transformation, and application code changes, violating the "least implementation effort" constraint. C: Creating a

</details>

### 121. ce-376 `availability`

A company is migrating its online shopping platform to AWS and wants to adopt a serverless architecture. The platform has a user profile and preference service that does not have a defined schem a. The platform allows user-defined fields. Profile information is updated several times daily. The company must store profile information in a durable and highly available solution. The solution must capture modifications to profile data for future processing. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an Amazon DynamoDB table to store profile data. Use Amazon DynamoDB Streams to capture modifications.**

The solution requires a serverless, durable, and highly available database that supports a flexible, undefined schema for user profiles. Amazon DynamoDB is a fully managed, serverless NoSQL database that meets these criteria, as it does not enforce a rigid schema. The requirement to capture modifications for future processing is directly addressed by Amazon DynamoDB Streams. DynamoDB Streams provides a time-ordered sequence of item-level changes (create, update, delete) in a DynamoDB table, which can be easily consumed by other AWS services like AWS Lambda for downstream processing. This combination provides a complete serverless solution that fulfills all the stated requirements. Why Incorrect Options are Wrong: A. Amazon RDS for PostgreSQL is a relational database that requires a defined schema, which contradicts the scenario's requirements. CloudWatch Logs is not a Change Data Capture

</details>

### 122. et-376 `least-ops`

A company has launched an Amazon RDS for MySQL DB instance. Most of the connections to the database come from serverless applications. Application traffic to the database changes significantly at random intervals. At times of high demand, users report that their applications experience database connection rejection errors. Which solution will resolve this issue with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create a proxy in RDS Proxy. Configure the users’ applications to use the DB instance through RDS Proxy.**

RDS Proxy is a fully managed, highly available database proxy for Amazon RDS that makes applications more scalable, more resilient to database failures, and more secure. It automatically routes database traffic to the appropriate DB instance, handling connection pooling and failover.

</details>

### 123. ce-377

A company runs a mobile game app on AWS. The app stores data for every user session. The data updates frequently during a gaming session. The app stores up to 256 KB for each session. Sessions can last up to 48 hours. The company wants to automate the deletion of expired session dat a. The company must be able to restore all session data automatically if necessary. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use an Amazon DynamoDB table to store the session data. Enable point-in-time recovery (PITR) and TTL for the table. Select the corresponding attribute for TTL in the session data.**

The scenario requires a data store optimized for frequent updates to small data items (session data), with automated deletion of expired data and the ability to perform point-in-time restores. Amazon DynamoDB is a fully managed NoSQL database service that provides fast, predictable performance with seamless scalability, making it ideal for frequently updated session data in a mobile app. DynamoDB's Time to Live (TTL) feature allows you to set an expiration timestamp on items, after which DynamoDB automatically deletes them at no cost, fulfilling the automated deletion requirement. Furthermore, enabling Point-in-Time Recovery (PITR) for the DynamoDB table provides continuous backups, allowing you to restore the table to any single second in the preceding 35 days, which meets the automated restore requirement. Why Incorrect Options are Wrong: B: Amazon MemoryDB for Redis does not have a fe

</details>

### 124. et-378

A company is developing a real-time multiplayer game that uses UDP for communications between the client and servers in an Auto Scaling group. Spikes in demand are anticipated during the day, so the game server platform must adapt accordingly. Developers want to store gamer scores and other non-relational data in a database solution that will scale without intervention. Which solution should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Use a Network Load Balancer for traffic distribution and Amazon DynamoDB on-demand for data storage.**

Think of an NLB like a traffic cop for your game. It helps distribute and manage the incoming traffic from players to your game servers. It ensures that the load is balanced across your servers, which is crucial for handling the expected spikes in demand. DynamoDB is a type of database that can store data for your game, such as gamer scores. "On-demand" means that DynamoDB automatically scales to handle the amount of data and traffic your game is experiencing.

</details>

### 125. et-379

A company hosts a frontend application that uses an Amazon API Gateway API backend that is integrated with AWS Lambda. When the API receives requests, the Lambda function loads many libraries. Then the Lambda function connects to an Amazon RDS database, processes the data, and returns the data to the frontend application. The company wants to ensure that response latency is as low as possible for all its users with the fewest number of changes to the company's operations. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure provisioned concurrency for the Lambda function that handles the requests.**

Provisioned Concurrency: Provisioned concurrency allows you to pre-warm a specific number of instances of your Lambda function. This ensures that there are already instances available to handle incoming requests, reducing the cold start latency. Since the Lambda function loads many libraries, reducing cold start latency is crucial for optimizing response time.

</details>

### 126. dt-380

A read only news reporting site with a combined web and application tier and a database tier that receives large and unpredictable traffic demands must be able to respond to these traffic fluctuations automatically. What AWS services should be used meet these requirements?

<details><summary>Answer</summary>

**A. Stateless instances for the web and application tier synchronized using Elasticache Memcached in an autoscaimg group monitored with CloudWatch. And RDSwith read replicas.**

</details>

### 127. et-381

A company hosts a three-tier web application that includes a PostgreSQL database. The database stores the metadata from documents. The company searches the metadata for key terms to retrieve documents that the company reviews in a report each month. The documents are stored in Amazon S3. The documents are usually written only once, but they are updated frequently. The reporting process takes a few hours with the use of relational queries. The reporting process must not prevent any document modifications or the addition of new documents. A solutions architect needs to implement a solution to speed up the reporting process. Which solution will meet these requirements with the LEAST amount of change to the application code?

<details><summary>Answer</summary>

**B. Set up a new Amazon Aurora PostgreSQL DB cluster that includes an Aurora Replica. Issue queries to the Aurora Replica to generate the reports.**

Amazon Aurora PostgreSQL DB cluster that includes an Aurora Replica. Issue queries to the Aurora Replica to generate the reports) is the best option for speeding up the reporting process for a three-tier web application that includes a PostgreSQL database storing metadata from documents, while not impacting document modifications or additions, with the least amount of change to the application code.

</details>

### 128. dt-382

What does Amazon ElastiCache provide?

<details><summary>Answer</summary>

**C. A managed In-memory cache service.**

</details>

### 129. ce-386 `cost`

A company has a web application that uses Amazon API Gateway to route HTTPS requests to AWS Lambda functions. The application uses an Amazon Aurora MySQL database for its data storage. The application has experienced unpredictable surges in traffic that overwhelm the database with too many connection requests. The company wants to implement a scalable solution that is more resilient to database failures. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create an Amazon RDS proxy for the database. Replace the database endpoint with the proxy endpoint in the Lambda functions.**

The scenario describes a classic issue with serverless applications like AWS Lambda connecting to relational databases. Lambda's high concurrency can create a large number of simultaneous database connections during traffic surges, exhausting the database's connection limit. Amazon RDS Proxy is a fully managed, highly available database proxy that is specifically designed to solve this problem. It establishes and manages a pool of database connections. Lambda functions connect to the proxy, which then efficiently reuses connections from the pool to serve requests. This improves application scalability by handling connection surges gracefully and enhances resilience by managing database failovers transparently. It is the most cost-effective solution as it avoids the need to over-provision the database instance for peak connection loads. Why Incorrect Options are Wrong: B. Migrating to Dyn

</details>

### 130. dt-386

Your company is in the process of developing a next generation pet collar that collects biometric information to assist families with promoting healthy lifestyles for their pets. Each collar will push 30kb of biometric data in JSON format every 2 seconds to a collection platform that will process and analyze the data providing health trending information back to the pet owners and veterinarians via a web portal. Management has tasked you to architect the collection platform ensuring the following requirements are met. Provide the ability for real-time analytics of the inbound biometric data. Ensure processing of the biometric data is highly durable, elastic and parallel. The results of the analytic processing should be persisted for data mining. Which architecture outlined below will meet the initial requirements for the collection platform?

<details><summary>Answer</summary>

**B. Utilize Amazon Kinesis to collect the inbound sensor data, analyze the data with Kinesis clients and save the results to a Redshift cluster using EMR.**

</details>

### 131. et-386

An ecommerce company is running a multi-tier application on AWS. The front-end and backend tiers both run on Amazon EC2, and the database runs on Amazon RDS for MySQL. The backend tier communicates with the RDS instance. There are frequent calls to return identical datasets from the database that are causing performance slowdowns. Which action should be taken to improve the performance of the backend?

<details><summary>Answer</summary>

**B. Implement Amazon ElastiCache to cache the large datasets.**

Amazon ElastiCache: Amazon ElastiCache is a fully managed in-memory caching service. By implementing ElastiCache, you can cache frequently accessed data in-memory, reducing the need to make repeated calls to the database. This helps improve the performance of your application by serving data directly from the cache instead of querying the database every time.  Caching Large Datasets: In scenarios where identical datasets are frequently requested, caching the results in ElastiCache can significantly reduce the load on the database and improve response times for subsequent requests. It is particularly effective for read-heavy workloads where the data does not change frequently.

</details>

### 132. ce-387

A company has an application that uses a MySQL database that runs on an Amazon EC2 instance. The instance currently runs in a single Availability Zone. The company requires a fault-tolerant database solution that provides a recovery time objective (RTO) and a recovery point objective (RPO) of 2 minutes or less. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the MySQL database to Amazon RDS for MySQL. Configure the new RDS for MySQL database to use a Multi-AZ deployment.**

The core requirements are fault tolerance with a Recovery Time Objective (RTO) and Recovery Point Objective (RPO) of 2 minutes or less. An Amazon RDS for MySQL Multi-AZ deployment is the ideal solution. It automatically provisions and maintains a synchronous standby replica in a different Availability Zone. In case of a primary database failure, RDS automatically fails over to the standby replica. This automated failover typically completes within 60-120 seconds, meeting the RTO. Because replication is synchronous, the data on the standby is up-to-date, resulting in a near-zero RPO, which easily satisfies the requirement. Why Incorrect Options are Wrong: A. RDS Read Replicas use asynchronous replication, which can lead to data loss (RPO) greater than 2 minutes. Promoting a replica is a manual or scripted process that often takes longer than 2 minutes (RTO). C. This is a self-managed solu

</details>

### 133. et-389

A company has a large dataset for its online advertising business stored in an Amazon RDS for MySQL DB instance in a single Availability Zone. The company wants business reporting queries to run without impacting the write operations to the production DB instance. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Deploy RDS read replicas to process the business reporting queries.**

Amazon RDS provides the ability to create read replicas of a source DB instance. Read replicas can be used to offload read traffic from the primary (write) DB instance, allowing you to scale read operations horizontally. This is particularly useful for scenarios where you want to run reporting queries without affecting the write performance of the production DB instance.

</details>

### 134. dt-390

You have recently joined a startup company building sensors to measure street noise and air quality in urban areas. The company has been running a pilot deployment of around 100 sensors for 3 months. Each sensor uploads 1KB of sensor data every minute to a backend hosted on AWS. During the pilot, you measured a peak of 10 IOPS on the database, and you stored an average of 3GB of sensor data per month in the database. The current deployment consists of a load-balanced auto scaled Ingestion layer using EC2 instances and a PostgreSQL RDS database with 500GB standard storage. The pilot is considered a success and your CEO has managed to get the attention of some potential investors. The business plan requires a deployment of at least 100K sensors which needs to be supported by the backend. You also need to store sensor data for at least two years to be able to compare year over year improvements. To secure funding, you have to make sure that the platform meets these requirements and leaves room for further scaling. Which setup will meet the requirements?

<details><summary>Answer</summary>

**C. Replace the RDS instance with a 6 node Redshift cluster with 96TB of storage.**

</details>

### 135. ce-391

A global ecommerce company is planning to enhance its AWS data storage architecture to improve system availability and resilience. The company handles millions of daily transactions in relational form. It stores unstructured data in the form of images over 4 MB in size. The solution must provide continuous operation in multiple geographic locations, minimize downtime/data loss, and support both transactional and unstructured data. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an Amazon Aurora global database for transaction data. Use Amazon S3 with Cross-Region Replication for unstructured data.**

This solution correctly addresses both data types and all requirements. An Amazon Aurora global database is specifically designed for globally distributed applications requiring a relational database. It provides low-latency global reads and disaster recovery across multiple AWS Regions. For large, unstructured data like images, Amazon S3 is the most appropriate and cost-effective service. S3 Cross-Region Replication (CRR) automatically copies objects to a bucket in another region, ensuring high durability, availability, and resilience across geographic locations, which directly meets the company's requirements for continuous operation and data protection. Why Incorrect Options are Wrong: A. Amazon RDS Multi-AZ provides high availability within a single region, not for global operations. Amazon DynamoDB has a 400 KB item size limit, making it unsuitable for storing images over 4 MB. C. A

</details>

### 136. et-394

A company is running a multi-tier ecommerce web application in the AWS Cloud. The application runs on Amazon EC2 instances with an Amazon RDS for MySQL Multi-AZ DB instance. Amazon RDS is configured with the latest generation DB instance with 2,000 GB of storage in a General Purpose SSD (gp3) Amazon Elastic Block Store (Amazon EBS) volume. The database performance affects the application during periods of high demand. A database administrator analyzes the logs in Amazon CloudWatch Logs and discovers that the application performance always degrades when the number of read and write IOPS is higher than 20,000. What should a solutions architect do to improve the application performance?

<details><summary>Answer</summary>

**C. Replace the volume with a Provisioned IOPS SSD (io2) volume.**

io2 volumes are designed for high-performance, low-latency applications such as databases. Provisioned IOPS allows you to specify the amount of IOPS the volume needs, ensuring consistent performance. For applications with high demand and where consistent performance is crucial, io2 volumes provide better control over IOPS compared to gp3 volumes.

</details>

### 137. dt-401

You are running a successful multitier web application on AWS and your marketing department has asked you to add a reporting tier to the application. The reporting tier will aggregate and publish status reports every 30 minutes from user-generated information that is being stored in your web application s database. You are currently running a Multi-AZ RDS MySQL instance for the database tier. You also have implemented Elasticache as a database caching layer between the application tier and database tier. Please select the answer that will allow you to successful ly implement the reporting tier with as little impact as possible to your database.

<details><summary>Answer</summary>

**C. Launch a RDS Read Replica connected to your Multi-AZ master database and generate reports by querying the Read Replica.**

</details>

### 138. et-401 `availability`

A company wants to use the AWS Cloud to make an existing application highly available and resilient. The current version of the application resides in the company's data center. The application recently experienced data loss after a database server crashed because of an unexpected power outage. The company needs a solution that avoids any single points of failure. The solution must give the application the ability to scale to meet user demand. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application servers by using Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Use an Amazon RDS DB instance in a Multi-AZ configuration.**

Auto Scaling Across Multiple Availability Zones: Deploying application servers using EC2 instances in an Auto Scaling group across multiple Availability Zones (AZs) helps avoid a single point of failure. If one AZ experiences an issue, the application can continue to operate in another AZ.

</details>

### 139. ce-402

A gaming company is building an application that uses a database to store user data. The company wants the database to have an active-active configuration that allows data writes to a secondary AWS Region. The database must achieve a sub-second recovery point objective (RPO). Options:

<details><summary>Answer</summary>

**D. Deploy an Amazon DynamoDB table in the primary Region. Configure global tables for the secondary Region.**

Amazon DynamoDB global tables provide a fully managed, multi-region, and multi-active database solution. This configuration directly meets the requirement for an active-active setup, allowing write operations in both the primary and secondary AWS Regions. DynamoDB automatically propagates writes between regions, with replication typically completing in under one second. This satisfies the sub-second recovery point objective (RPO) and is ideal for globally distributed applications like gaming that require low-latency data access and high availability. Why Incorrect Options are Wrong: A. An Amazon ElastiCache for Redis global datastore uses a primary cluster for writes and read-only secondary clusters, which is an active-passive configuration, not active-active for writes. B. Using DynamoDB Streams with AWS Lambda is a custom, complex solution. A fully managed service like DynamoDB global

</details>

### 140. dt-403

MySQL installations default to port [...].

<details><summary>Answer</summary>

**A. 3306.**

</details>

### 141. ce-406

A company is designing a website that displays stock market prices to users. The company wants to use Amazon ElastiCache (Redis OSS) for the data caching layer. The company needs to ensure that the website's data caching layer can automatically fail over to another node if necessary.

<details><summary>Answer</summary>

**B. Enable Multi-AZ in ElastiCache (Redis OSS). Fail over to a second node when necessary.**

Amazon ElastiCache for Redis provides high availability through the Multi-AZ with automatic failover feature. When you enable Multi-AZ on a Redis replication group, ElastiCache continuously monitors the health of the primary node. If the primary node fails, ElastiCache will automatically detect the failure and promote one of the existing read replicas to become the new primary node. It also updates the DNS record for the primary endpoint to point to the new primary, ensuring the application can reconnect with minimal disruption. This directly fulfills the requirement for an automatic failover mechanism for the caching layer. Why Incorrect Options are Wrong: A. Promoting a read replica is the action that occurs during failover, but enabling Multi-AZ is the specific feature that makes this process automatic, which is the key requirement. C. Exporting a backup to Amazon S3 and restoring it

</details>

### 142. et-406

A solutions architect is designing a two-tiered architecture that includes a public subnet and a database subnet. The web servers in the public subnet must be open to the internet on port 443. The Amazon RDS for MySQL DB instance in the database subnet must be accessible only to the web servers on port 3306. Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Create a security group for the web servers in the public subnet. Add a rule to allow traffic from 0.0.0.0/0 on port 443.**

D. Create a security group for the DB instance. Add a rule to allow traffic from the web servers’ security group on port 3306.  This allows inbound traffic from the internet on port 443 to the web servers.  This ensures that the RDS instance is accessible only from the web servers in the public subnet.

</details>

### 143. dt-410

True or False: When using IAM to control access to your RDS resources, the key names that can be used are case sensitive. For example, aws: CurrentTime is NOT equivalent to AWS: currenttime.

<details><summary>Answer</summary>

**B. False.**

</details>

### 144. ce-411

An ecommerce company is preparing to deploy a web application on AWS to ensure continuous service for customers. The architecture includes a web application that the company hosts on Amazon EC2 instances, a relational database in Amazon RDS, and static assets that the company stores in Amazon S3. The company wants to design a robust and resilient architecture for the application.

<details><summary>Answer</summary>

**B. Deploy Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones. Deploy a Multi-AZ RDS DB instance. Use Amazon CloudFront to distribute static assets.**

This architecture correctly implements high availability and resilience, which are crucial for an ecommerce application requiring continuous service. Deploying Amazon EC2 instances in an Auto Scaling group across multiple Availability Zones (AZs) ensures the application can withstand the failure of a single AZ. A Multi-AZ Amazon RDS deployment provides a synchronously replicated standby database in a different AZ for automatic failover, enhancing database resilience. Using Amazon CloudFront, a content delivery network (CDN), to serve static assets from Amazon S3 improves performance, reduces latency for global customers, and adds a layer of availability by caching content at edge locations. Why Incorrect Options are Wrong: A. Deploying both EC2 and RDS in a single Availability Zone creates a single point of failure, which contradicts the requirement for a robust and resilient architectur

</details>

### 145. et-411

A company has a web application with sporadic usage patterns. There is heavy usage at the beginning of each month, moderate usage at the start of each week, and unpredictable usage during the week. The application consists of a web server and a MySQL database server running inside the data center. The company would like to move the application to the AWS Cloud, and needs to select a cost-effective database platform that will not require database modifications. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. MySQL-compatible Amazon Aurora Serverless**

Aurora Serverless is a serverless option for MySQL-compatible databases. It automatically adjusts the database capacity based on actual usage, making it suitable for sporadic usage patterns. It is MySQL-compatible, so it won't require significant database modifications.

</details>

### 146. et-416

A rapidly growing global ecommerce company is hosting its web application on AWS. The web application includes static content and dynamic content. The website stores online transaction processing (OLTP) data in an Amazon RDS database The website’s users are experiencing slow page loads. Which combination of actions should a solutions architect take to resolve this issue? (Choose two.)

<details><summary>Answer</summary>

**B. Set up an Amazon CloudFront distribution.**

D. Create a read replica for the RDS DB instance.  Amazon CloudFront is a content delivery network (CDN) that can improve the performance of a website by caching static content closer to the users. This reduces latency and improves page load times. Configure CloudFront to distribute static content such as images, stylesheets, and JavaScript files. This will offload the serving of static assets from the web servers, improving overall website performance.  Creating a read replica for the Amazon RDS database allows you to offload read traffic from the primary database, improving the overall database performance.

</details>

### 147. et-420 `availability`

A company wants to use an Amazon RDS for PostgreSQL DB cluster to simplify time-consuming database administrative tasks for production database workloads. The company wants to ensure that its database is highly available and will provide automatic failover support in most scenarios in less than 40 seconds. The company wants to offload reads off of the primary instance and keep costs as low as possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use an Amazon RDS Multi-AZ DB cluster deployment. Point the read workload to the reader endpoint.**

An RDS Multi-AZ DB cluster runs one writer instance and two standby instances spread across three Availability Zones. The standbys are readable, so pointing the read workload at the cluster reader endpoint takes those queries off the writer with nothing extra to provision. Replication to the standbys is faster than in a plain Multi-AZ instance deployment, and failover typically completes in under 35 seconds, which satisfies the under-40-second requirement. A Multi-AZ instance deployment would meet the availability goal but its single standby cannot serve reads, so you would have to add and pay for separate read replicas.

</details>

### 148. dt-421

An International company has deployed a multi-tier web application that relies on DynamoDB in a single region. For regulatory reasons they need disaster recovery capability in a separate region with a Recovery Time Objective of 2 hours and a Recovery Point Objective of 24 hours. They should synchronize their data on a regular basis and be able to provision the web application rapidly using CloudFormation. The objective is to minimize changes to the existing web application, control the throughput of DynamoDB used for the synchronization of data and synchronize only the modified elements. Which design would you choose to meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS data Pipeline to schedule a DynamoDB cross region copy once a day. Create a 'Last updated' attribute in your DynamoDB table that would represent the timestamp of the last update and use it as a filter.**

</details>

### 149. ce-423

A solutions architect is designing a customer-facing application for a company. The application's database will have a clearly defined access pattern throughout the year and will have a variable number of reads and writes that depend on the time of year. The company must retain audit records for the database for 7 days. The recovery point objective (RPO) must be less than 5 hours. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use Amazon Aurora MySQL with auto scaling. Activate the database auditing parameter.**

Amazon Aurora is a relational database service designed for high-performance, transactional (OLTP) workloads, making it suitable for a customer-facing application. Aurora features auto-scaling capabilities for read replicas and Aurora Serverless v2 can scale compute capacity for both reads and writes, which directly addresses the requirement for variable workloads. Aurora supports Advanced Auditing to meet the audit record retention policy. Crucially, Aurora's architecture provides continuous, incremental backups to Amazon S3. This allows for point-in-time recovery (PITR) to any second within the backup retention period, resulting in a Recovery Point Objective (RPO) of seconds. This easily satisfies the requirement for an RPO of less than 5 hours without needing to schedule manual or periodic snapshots. Why Incorrect Options are Wrong: A: Amazon DynamoDB's on-demand backups are not suita

</details>

### 150. dt-424

You currently operate a web application in the AWS US-East region. The application runs on an autoscaled layer of EC2 instances and an RDS Multi-AZ database. Your IT security compliance officer has tasked you to develop a reliable and durable logging solution to track changes made to your EC2, IAM, and RDS resources. The solution must ensure the integrity and confidentiality of your log data. Which of these solutions would you recommend?

<details><summary>Answer</summary>

**A. Create a new CloudTrail trail with one new S3 bucket to store the logs and with the global services option selected. Use IAM roles, S3 bucket policies, and Multi Factor Authentication (MFA) Delete on the S3 bucket that stores your logs.**

</details>

### 151. ce-428

A company uses an Amazon Aurora PostgreSQL DB cluster to store its critical data in the us-east-1 Region. The company wants to develop a disaster recovery plan to recover the database in the us- west-1 Region. The company has a recovery time objective (RTO) of 5 minutes and has a recovery point objective (RPO) of 1 minute. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create an Aurora global database. Set us-west-1 as the secondary Region. Update connections to use the writer and reader endpoints as appropriate.**

Aurora Global Database replicates storage asynchronously at the volume level between Regions with typical lag 1 s (RPO 1 min). When the primary Region is impaired, a secondary Region cluster can be promoted to read/write in normally 1 min, so total recovery time is well within the 5-minute RTO. Creating the global database with us-east-1 as primary and us-west-1 as secondary therefore meets both the 1-minute RPO and 5-minute RTO requirements without additional tooling. Why Incorrect Options are Wrong: A. Cross-Region read replicas have no automatic fail-over; promotion is manual, often taking 5 min, so RTO is not met. C. Logical replication over a separately managed cluster is manual, incurs higher and variable lag, and cannot guarantee 1-min RPO or 5-min RTO. D. Snapshot copy/restore is asynchronous and restore alone exceeds several minutes; RPO far exceeds 1 min and RTO far exceeds 5 m

</details>

### 152. ce-431

A company hosts a two-tier website that runs on Amazon EC2 instances. The website has a database that runs on Amazon RDS for MySQL. All users are required to log in to the website to see their own customized pages. The website typically experiences low traffic. Occasionally, the website experiences sudden increases in traffic and becomes unresponsive. During these increases in traffic, the database experiences a heavy write load. A solutions architect must improve the website's availability without changing the application code. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Migrate the database to an Amazon Aurora Serverless cluster. Set the maximum Aurora capacity units (ACUs) to a value high enough to respond to the traffic increases. Configure the EC2 instances to connect to the Aurora database.**

The core issue is the database becoming unresponsive due to sudden, heavy write loads. Amazon Aurora Serverless is designed to automatically and instantly scale database capacity up or down based on application demand. Migrating from RDS for MySQL to the MySQL-compatible Aurora Serverless v2 addresses the write bottleneck without requiring application code changes. This directly resolves the availability problem during traffic spikes by providing on-demand database scaling, which is the root cause of the unresponsiveness. Why Incorrect Options are Wrong: A. ElastiCache is a caching service primarily for read-heavy workloads and would not solve a heavy write load issue. It also requires application code changes. B. Scaling the EC2 instances addresses the web tier, not the database tier, which is the identified bottleneck. The database would still be overwhelmed. C. Amazon CloudFront is a

</details>

### 153. dt-431

Does Amazon RDS for SQL Server currently support importing data into the msdb database?

<details><summary>Answer</summary>

**B. No.**

</details>

### 154. et-431

A company has developed a new video game as a web application. The application is in a three-tier architecture in a VPC with Amazon RDS for MySQL in the database layer. Several players will compete concurrently online. The game’s developers want to display a top-10 scoreboard in near- real time and offer the ability to stop and restore the game while preserving the current scores. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Set up an Amazon ElastiCache for Redis cluster to compute and cache the scores for the web application to display.**

Redis is an in-memory data store that is well-suited for caching and real-time data processing. By setting up an ElastiCache for Redis cluster, you can compute and cache the scores in-memory, allowing for fast retrieval and updates.

</details>

### 155. ce-432

An ecommerce company is redesigning a web application to run on the AWS Cloud. The application needs to store static website content and must use a Microsoft SQL Server database to store customer data. The company needs to deploy the application in a resilient way across multiple Availability Zones. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an Amazon S3 bucket to store static content. Create an Amazon RDS for SQL Server Multi-AZ deployment for the database.**

This solution correctly addresses all requirements. Amazon S3 is the ideal service for storing and serving static website content due to its high durability, availability, and scalability. For the database requirement, Amazon RDS for SQL Server provides a managed database service. A Multi-AZ deployment specifically meets the resilience requirement by creating and maintaining a synchronous standby replica in a different Availability Zone (AZ). AWS manages the failover automatically, providing high availability for the database layer without manual intervention. Why Incorrect Options are Wrong: A. Amazon RDS Custom for SQL Server is for applications needing OS or database customization, which is not specified here and adds complexity. A standard RDS Multi-AZ deployment is sufficient and simpler. C. Amazon EBS Multi-Attach volumes allow attachment to multiple EC2 instances within the same A

</details>

### 156. et-435 `cost`

A company needs to migrate a MySQL database from its on-premises data center to AWS within 2 weeks. The database is 20 TB in size. The company wants to complete the migration with minimal downtime. Which solution will migrate the database MOST cost-effectively?

<details><summary>Answer</summary>

**A. Order an AWS Snowball Edge Storage Optimized device. Use AWS Database Migration Service (AWS DMS) with AWS Schema Conversion Tool (AWS SCT) to migrate the database with replication of ongoing changes. Send the Snowball Edge device to AWS to finish the migration and continue the ongoing replication.**

This is a cost-effective solution for shipping large amounts of data to AWS. Snowball Edge devices are designed for efficient data transfer, and they can handle the 20 TB database.  AWS DMS is a managed service for migrating databases to AWS, and AWS SCT can assist in converting the database schema. Using these tools in combination allows for a smooth migration process.

</details>

### 157. et-436 `cost`

A company moved its on-premises PostgreSQL database to an Amazon RDS for PostgreSQL DB instance. The company successfully launched a new product. The workload on the database has increased. The company wants to accommodate the larger workload without adding infrastructure. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Buy reserved DB instances for the total workload. Make the Amazon RDS for PostgreSQL DB instance larger.**

When you commit to using a database instance for a longer time (with reserved instances), AWS gives you a discount compared to paying on a month-to-month basis.  Imagine you have a computer, and you want to make it more powerful because you have more things to do on it. Making the instance larger means upgrading the power of your virtual computer.

</details>

### 158. dt-438

Is the encryption of connections between my application and my DB Instance using SSL for the MySQL server engines available?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 159. ce-439 `availability`

A company is running a business-critical web application on Amazon EC2 instances behind an Application Load Balancer. The EC2 instances are in an Auto Scaling group. The application uses an Amazon Aurora PostgreSQL database that is deployed in a single Availability Zone. The company wants the application to be highly available with minimum downtime and minimum loss of data. Which solution will meet these requirements with the LEAST operational effort?

<details><summary>Answer</summary>

**B. Configure the Auto Scaling group to use multiple Availability Zones. Configure the database as Multi-AZ. Configure an Amazon RDS Proxy instance for the database.**

This solution addresses the high availability requirements with the least operational effort by leveraging managed AWS services. Configuring the Auto Scaling group to span multiple Availability Zones (AZs) protects the web tier from an AZ failure. Converting the single-AZ Aurora database to a Multi-AZ deployment provides a managed, automatic failover capability with minimal data loss (low RPO) and downtime (low RTO). Adding an Amazon RDS Proxy instance further enhances availability by managing database connections gracefully during a failover, making the process more transparent to the application and reducing downtime. Why Incorrect Options are Wrong: A. A multi-Region architecture provides disaster recovery but involves significantly more complexity and operational effort than a multi-AZ solution, which is sufficient here. C. Recovering from hourly snapshots results in high data loss (

</details>

### 160. et-440

A company used an Amazon RDS for MySQL DB instance during application testing. Before terminating the DB instance at the end of the test cycle, a solutions architect created two backups. The solutions architect created the first backup by using the mysqldump utility to create a database dump. The solutions architect created the second backup by enabling the final DB snapshot option on RDS termination. The company is now planning for a new test cycle and wants to create a new DB instance from the most recent backup. The company has chosen a MySQL-compatible edition ofAmazon Aurora to host the DB instance. Which solutions will create the new DB instance? (Choose two.)

<details><summary>Answer</summary>

**A. Import the RDS snapshot directly into Aurora.**

C. Upload the database dump to Amazon S3. Then import the database dump into Aurora.  A. Amazon Aurora allows you to directly import an Amazon RDS snapshot into Aurora. This is a straightforward process for migrating data from RDS to Aurora.  C. Uploading the database dump to Amazon S3 and then importing the database dump into Aurora is a common method. You can use the MySQL-compatible version of Aurora to restore the data from a database dump stored in Amazon S3.

</details>

### 161. dt-448

Do the system resources on the Micro instance meet the recommended configuration for Oracle?

<details><summary>Answer</summary>

**B. Yes, but only for certain situations.**

</details>

### 162. et-449 `cost`

A company runs its application on an Oracle database. The company plans to quickly migrate to AWS because of limited resources for the database, backup administration, and data center maintenance. The application uses third-party database features that require privileged access. Which solution will help the company migrate the database to AWS MOST cost-effectively?

<details><summary>Answer</summary>

**B. Migrate the database to Amazon RDS Custom for Oracle. Customize the database settings to support third-party features.**

</details>

### 163. ce-450

A company's data platform uses an Amazon Aurora MySQL database. The database has multiple read replicas and multiple DB instances across different Availability Zones. Users have recently reported errors from the database that indicate that there are too many connections. The company wants to reduce the failover time by 20% when a read replica is promoted to primary writer. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Use Amazon RDS Proxy in front of the Aurora database.**

Amazon RDS Proxy is a fully managed, highly available database proxy that makes applications more scalable, resilient, and secure. It addresses the "too many connections" error by pooling and sharing database connections, improving database efficiency. RDS Proxy also improves availability by reducing failover times. It maintains a connection pool and can route requests to a newly promoted read replica in seconds, often without dropping application connections. This directly meets the requirements of connection management and faster failover. Why Incorrect Options are Wrong: A. Aurora is already a high-availability solution. Switching to a standard RDS Multi-AZ cluster would be a downgrade in performance and failover capabilities, not an improvement. C. Switching to DynamoDB is a major architectural change from a relational to a NoSQL database, which is not a direct solution for connectio

</details>

### 164. et-464

A company hosts an online shopping application that stores all orders in an Amazon RDS for PostgreSQL Single-AZ DB instance. Management wants to eliminate single points of failure and has asked a solutions architect to recommend an approach to minimize database downtime without requiring any changes to the application code. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Convert the existing database instance to a Multi-AZ deployment by modifying the database instance and specifying the Multi-AZ option.**

By converting the existing RDS instance to a Multi-AZ deployment, you enable high availability with automatic failover. Amazon RDS will automatically replicate the database to a standby instance in a different Availability Zone (AZ). In the event of a failure, Amazon RDS will automatically promote the standby to the primary, minimizing downtime.

</details>

### 165. ce-467

A company runs a database on Amazon Aurora in the us-east-1 Region. The company has a disaster recovery requirement that the database be available in another Region. Which solution meets this requirement with minimal disruption to the database operations?

<details><summary>Answer</summary>

**B. Deploy Aurora cross-Region read replicas.**

The requirement is to establish a disaster recovery (DR) solution for an Amazon Aurora database in a different AWS Region with minimal disruption. Aurora cross-Region read replicas are specifically designed for this purpose. A read replica is created in a secondary Region, and data is asynchronously replicated from the primary database. During normal operations, this has a minimal performance impact on the primary cluster. In a DR event, the cross-Region replica can be promoted to a standalone, writable cluster in minutes, providing a low Recovery Time Objective (RTO) and Recovery Point Objective (RPO) solution. Why Incorrect Options are Wrong: A. A Multi-AZ deployment provides high availability by placing replicas in different Availability Zones within the same Region, not for cross-Region DR. C. Aurora does not use Amazon EBS volumes for its cluster storage; it uses a shared, custom st

</details>

### 166. dt-467

Is creating a Read Replica of another Read Replica supported?

<details><summary>Answer</summary>

**D. No.**

</details>

### 167. ce-468 `availability`

A company is running a critical workload on an Amazon RDS DB instance. The company needs the DB instance to be highly available. The company requires a recovery time of less than 5 minutes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Modify the DB instance to use a Multi-AZ deployment.**

Modifying the Amazon RDS DB instance to use a Multi-AZ deployment is the standard AWS solution for achieving high availability. In a Multi-AZ deployment, RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. If the primary DB instance fails, RDS performs an automatic failover to the standby replica. This process is fully managed and typically completes within 60-120 seconds, which easily meets the recovery time objective (RTO) of less than 5 minutes. This provides high availability without requiring manual intervention. Why Incorrect Options are Wrong: A. A read replica is for read scaling or disaster recovery. Promoting it to a primary instance is a manual process that takes longer than 5 minutes. B. A CloudFormation template is for infrastructure as code and provisioning; it does not provide an automated, rapid failover mechanism for

</details>

### 168. et-472

A company has a mobile chat application with a data store based in Amazon DynamoDB. Users would like new messages to be read with as little latency as possible. A solutions architect needs to design an optimal solution that requires minimal application changes. Which method should the solutions architect select?

<details><summary>Answer</summary>

**A. Configure Amazon DynamoDB Accelerator (DAX) for the new messages table. Update the code to use the DAX endpoint.**

DAX is an in-memory cache that sits in front of a DynamoDB table and answers cached reads in microseconds instead of the single-digit milliseconds DynamoDB itself returns. Because DAX speaks the DynamoDB API, the only change is to point the client at the DAX cluster endpoint, which keeps the application work small. A general-purpose cache such as ElastiCache would also cut latency, but you would have to write and maintain the cache-loading and invalidation logic yourself.

</details>

### 169. dt-473

A favored client needs you to quickly deploy a database that is a relational database service with minimal administration as he wants to spend the least amount of time administering it. Which database would be the best option?

<details><summary>Answer</summary>

**C. Amazon RDS.**

</details>

### 170. ce-478

A company hosts a PostgreSQL database on an Amazon EC2 instance. Database usage has increased recently. Users are experiencing higher latency during queries on the database. The company needs to update the database to reduce latency for users. The new solution must achieve a recovery time objective (RTO) and a recovery point objective (RPO) of less than 5 minutes. The company also wants to deploy the database to multiple AWS Regions to meet new availability requirements. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS DMS to migrate the database to an Amazon Aurora PostgreSQL database. Configure the Aurora database as a global database. Set the Aurora parameter group RPO setting to 60 seconds. In the event of a database failure, promote a secondary database in a second Region automatically.**

Amazon Aurora Global Database is designed for globally distributed applications, providing low-latency global reads and disaster recovery from region-wide outages. It replicates data with typical latency of under a second, offering a recovery point objective (RPO) well within the 5-minute requirement. In case of a regional failure, a secondary region can be promoted to full read/write capabilities in less than a minute, meeting the recovery time objective (RTO). Migrating the existing PostgreSQL database using AWS Database Migration Service (DMS) to an Aurora PostgreSQL global database directly addresses all requirements for latency, RTO/RPO, and multi-Region availability. Why Incorrect Options are Wrong: A. AWS Backup is for backup and restore, not a high-availability or disaster recovery solution. Restoring an EC2 instance from a backup would not meet the RTO of less than 5 minutes. C.

</details>

### 171. et-479

A company is making a prototype of the infrastructure for its new website by manually provisioning the necessary infrastructure. This infrastructure includes an Auto Scaling group, an Application Load Balancer and an Amazon RDS database. After the configuration has been thoroughly validated, the company wants the capability to immediately deploy the infrastructure for development and production use in two Availability Zones in an automated fashion. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**B. Define the infrastructure as a template by using the prototype infrastructure as a guide. Deploy the infrastructure with AWS CloudFormation.**

AWS CloudFormation is a service specifically designed for defining and deploying AWS infrastructure as code using templates. In this case, you can create a CloudFormation template based on the validated prototype infrastructure, and then use CloudFormation to deploy and manage the infrastructure in an automated and repeatable way.

</details>

### 172. dt-480 `performance` `availability`

Your application is using an ELB in front of an Auto Scaling group of web/application servers deployed across two AZs and a Multi-AZ RDS Instance for data persistence. The database CPU is often above 80% usage and 90% of I/O operations on the database are reads. To improve performance you recently added a single-node Memcached ElastiCache Cluster to cache frequent DB query results. In the next weeks the overall workload is expected to grow by 30%. Do you need to change anything in the architecture to maintain the high availability of the application with the anticipated additional load? Why?

<details><summary>Answer</summary>

**A. Yes, you should deploy two Memcached ElastiCache Clusters in different AZs because the RDS instance will not be able to handle the load if the cache node fails.**

</details>

### 173. et-481

A company hosts a three-tier web application in the AWS Cloud. A Multi-AZAmazon RDS for MySQL server forms the database layer Amazon ElastiCache forms the cache layer. The company wants a caching strategy that adds or updates data in the cache when a customer adds an item to the database. The data in the cache must always match the data in the database. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Implement the write-through caching strategy**

In a write-through caching strategy, data is always written or updated in the cache when it is modified in the database. This ensures that the cache is consistently updated with the latest data from the database. When a customer adds an item to the database, the write-through caching strategy ensures that the item is also added or updated in the cache.

</details>

### 174. ce-484 `least-ops`

A social media company wants to store its database of user profiles, relationships, and interactions in the AWS Cloud. The company needs an application to monitor any changes in the database. The application needs to analyze the relationships between the data entities and to provide recommendations to users. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon Neptune to store the information. Use Neptune Streams to process changes in the database.**

The scenario describes a social media application with highly connected data (profiles, relationships, interactions) and the need for relationship analysis and recommendations. This is a classic use case for a graph database. Amazon Neptune is a fully managed graph database service ideal for this purpose. The requirement to monitor database changes with minimal operational overhead is best met by Neptune Streams. This is a native feature of Amazon Neptune that provides a complete, ordered log of all changes to the graph data. Using this built-in feature is more efficient and requires less management than setting up a separate data streaming pipeline with Amazon Kinesis. Why Incorrect Options are Wrong: A. Use Amazon Neptune to store the information. Use Amazon Kinesis Data Streams to process changes in the database. While possible, this adds operational overhead by requiring a custom mec

</details>

### 175. ce-486 `cost`

A company is planning to deploy its application on an Amazon Aurora PostgreSQL Serverless v2 cluster. The application will receive large amounts of traffic. The company wants to optimize the storage performance of the cluster as the load on the application increases Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Configure the cluster to use the Aurora l/O-Optimized storage configuration.**

Amazon Aurora offers two storage configurations: Aurora Standard and Aurora I/O-Optimized. For applications with high traffic and I/O-intensive workloads, the Aurora I/O-Optimized configuration is the most suitable and cost-effective choice. This configuration provides improved price performance and predictable pricing by bundling storage and I/O operation costs into a single fee. For workloads where I/O charges exceed 25% of the total Aurora bill, the I/O-Optimized configuration offers significant cost savings compared to the pay-per-I/O model of Aurora Standard. This makes it ideal for optimizing both performance and cost for the described high-load scenario. Why Incorrect Options are Wrong: A. The Aurora Standard configuration charges for storage and I/O operations separately. For a high-traffic application, the variable I/O costs can become very high, making it less cost-effective th

</details>

### 176. dt-487

An online gaming site asked you if you can deploy a database that is a fast, highly scalable NoSQL database service in AWS for a new site that he wants to build. Which database should you recommend?

<details><summary>Answer</summary>

**A. Amazon DynamoDB.**

</details>

### 177. ce-494

A company uses an Amazon DynamoDB table to store data that the company receives from devices. The DynamoDB table supports a customer-facing website to display recent activity oncustomer devices The company configured the table with provisioned throughput for writes and reads The company wants to calculate performance metrics for customer device data on a daily basis. The solution must have minimal effect on the table's provisioned read and write capacity Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an AWS Glue job with the AWS Glue DynamoDB export connector to calculate performance metrics on a recurring schedule.**

The primary requirement is to perform daily analytics with minimal impact on the DynamoDB table's provisioned throughput, which is actively serving a customer-facing website. The Amazon DynamoDB Export to Amazon S3 feature is specifically designed for this use case. This feature allows you to export a point-in-time snapshot of your table to an S3 bucket without consuming any read capacity units (RCUs) from the table itself. Once the data is in S3, an AWS Glue job can efficiently process it to calculate the required performance metrics. This approach completely isolates the analytics workload from the production table, ensuring zero performance impact. Why Incorrect Options are Wrong: A. The Amazon Athena DynamoDB connector directly scans the live DynamoDB table. This operation consumes provisioned read capacity, which would directly impact the performance of the customer-facing website.

</details>

### 178. dt-499

How many relational database engines does RDS currently support?

<details><summary>Answer</summary>

**D. Eight: Amazon Aurora PostgreSQL-Compatible Edition, Amazon Aurora MySQL-Compatible Edition, RDS for PostgreSQL, RDS for MySQL, RDS for MariaDB, RDS for SQL Server, RDS for Oracle, and RDS for Db2.**

</details>

### 179. ce-500

A company runs its production workload on an Amazon Aurora MySQL DB cluster that includes six Aurora Replicas. The company wants near-real-time reporting queries from one of its departments to be automatically distributed across three of the Aurora Replicas. Those three replicas have a different compute and memory specification from the rest of the DB cluster. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Create and use a custom endpoint for the workload.**

Amazon Aurora provides custom endpoints to direct specific workloads to a defined subset of DB instances within a cluster. In this scenario, the company needs to isolate a reporting workload to three specific Aurora Replicas that have different hardware specifications. By creating a custom endpoint and adding only these three replicas to it, the company can ensure that all connections made to this endpoint are automatically load-balanced exclusively across those designated instances. This meets the requirement for automatic distribution across a specific group of replicas without affecting the rest of the cluster. Why Incorrect Options are Wrong: B. Create a three-node cluster clone and use the reader endpoint. A cluster clone is a separate, point-in-time copy. It would not provide the near-real-time data from the production cluster required for reporting. C. Use any of the instance endp

</details>

### 180. et-502

A company runs a website that uses a content management system (CMS) on Amazon EC2. The CMS runs on a single EC2 instance and uses an Amazon Aurora MySQL Multi-AZ DB instance for the data tier. Website images are stored on an Amazon Elastic Block Store (Amazon EBS) volume that is mounted inside the EC2 instance. Which combination of actions should a solutions architect take to improve the performance and resilience of the website? (Choose two.)

<details><summary>Answer</summary>

**C. Move the website images onto an Amazon Elastic File System (Amazon EFS) file system that is mounted on every EC2 instance.**

E. Create an Amazon Machine Image (AMI) from the existing EC2 instance. Use the AMI to provision new instances behind an Application Load Balancer as part of an Auto Scaling group. Configure the Auto Scaling group to maintain a minimum of two instances. Configure an Amazon CloudFront distribution for the website.  Option C provides moving the website images onto an Amazon EFS file system that is mounted on every EC2 instance. Amazon EFS provides a scalable and fully managed file storage solution that can be accessed concurrently from multiple EC2 instances. This ensures that the website images can be accessed efficiently and consistently by all instances, improving performance.  In Option E The Auto Scaling group maintains a minimum of two instances, ensuring resilience by automatically replacing any unhealthy instances. Additionally, configuring an Amazon CloudFront distribution for the website further improves performance by caching content at edge locations closer to the end-users, reducing latency and improving content delivery. Hence combining these actions, the website's performance is improved through efficient image storage and content delivery

</details>

### 181. ce-507

A company hosts its multi-tier, public web application in the AWS Cloud. The web application runs on Amazon EC2 instances, and its database runs on Amazon RDS. The company is anticipating a large increase in sales during an upcoming holiday weekend. A solutions architect needs to build asolution to analyze the performance of the web application with a granularity of no more than 2 minutes. What should the solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**B. Enable detailed monitoring on all EC2 instances. Use Amazon CloudWatch metrics to perform further analysis.**

The core requirement is to analyze EC2 instance performance with a data granularity of two minutes or less. Amazon CloudWatch is the native AWS service for monitoring resources like EC2. By default, EC2 instances use basic monitoring, which collects metric data at 5-minute intervals. To meet the requirement, detailed monitoring must be enabled. Detailed monitoring provides metric data at a 1-minute frequency, which is well within the "no more than 2 minutes" constraint. These metrics can then be directly analyzed within the Amazon CloudWatch console or via its API, providing the most direct and efficient solution. Why Incorrect Options are Wrong: A. This describes a log analytics pipeline. While logs can contain performance data, it is an indirect and more complex method than using native CloudWatch performance metrics. C. This option is unnecessarily complex. Using AWS Lambda to fetch l

</details>

### 182. et-507

A company has a web application for travel ticketing. The application is based on a database that runs in a single data center in North America. The company wants to expand the application to serve a global user base. The company needs to deploy the application to multiple AWS Regions. Average latency must be less than 1 second on updates to the reservation database. The company wants to have separate deployments of its web platform across multiple Regions. However, the company must maintain a single primary reservation database that is globally consistent. Which solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Convert the application to use Amazon DynamoDB. Use a global table for the center reservation table. Use the correct Regional endpoint in each Regional deployment.**

Using DynamoDB's global tables feature, you can achieve a globally consistent reservation database with low latency on updates, making it suitable for serving a global user base. The automatic replication provided by DynamoDB eliminates the need for manual synchronization between Regions.

</details>

### 183. dt-510

What is an isolated database environment running in the cloud (Amazon RDS) called?

<details><summary>Answer</summary>

**A. DB Instance.**

</details>

### 184. et-511 `cost`

A company is developing software that uses a PostgreSQL database schema. The company needs to configure multiple development environments and databases for the company's developers. On average, each development environment is used for half of the 8-hour workday. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure each development environment with its own Amazon RDS for PostgreSQL Single-AZ DB instances**

Explanation: Since each environment is only used for half of the workday, a standard RDS for PostgreSQL instance that gets stopped when not in use is cheaper than running Aurora continuously — Aurora costs more than standard RDS and this workload doesn't need Aurora's extra performance/availability features.

</details>

### 185. ce-512

A company needs to migrate a MySQL database from an on-premises data center to AWS within 2 weeks. The database is 180 TB in size. The company cannot partition the database. The company wants to minimize downtime during the migration. The company's internet connection speed is 100 Mbps. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Order an AWS Snowball Edge Storage Optimized device. Use AWS Database Migration Service (AWS DMS) and the AWS Schema Conversion Tool (AWS SCT) to migrate the database to Amazon RDS for MySQL and replicate ongoing changes. Send the Snowball Edge device back to AWS to finish the migration. Continue to replicate ongoing changes.**

The primary constraint is transferring 180 TB of data over a 100 Mbps connection within two weeks. A simple calculation shows that transferring 180 TB at 100 Mbps would take approximately 175 days, making any online transfer method for the initial load infeasible. The correct approach is a hybrid migration. An AWS Snowball Edge device is used for the large, offline initial data transfer, which bypasses the slow network and fits within the timeline. Concurrently, AWS Database Migration Service (DMS) is configured to capture and replicate ongoing changes from the on-premises database. Once the Snowball data is loaded into AWS, DMS applies the captured changes to the new RDS database, synchronizing it with the source and enabling a cutover with minimal downtime. Why Incorrect Options are Wrong: B. This solution relies entirely on the 100 Mbps Site-to-Site VPN connection for the initial 180

</details>

### 186. ce-514 `least-ops`

A company is developing a rating system for its ecommerce web application. The company needs a solution to save ratings that users submit in an Amazon DynamoDB table. The company wants to ensure that developers do not need to interact directly with the DynamoDB table. The solution must be scalable and reusable. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an Amazon API Gateway REST API Define a resource and create a new POST method Choose AWS as the integration type, and select DynamoDB as the service. Set the action to PutItem.**

Amazon API Gateway can be configured with an "AWS Service" integration type. This allows an API endpoint to directly invoke actions on other AWS services, such as PutItem for Amazon DynamoDB, without any intermediary compute layer like AWS Lambda. This solution is fully managed, highly scalable, and reusable. It perfectly abstracts the DynamoDB table from developers, who only need to interact with the API endpoint. Crucially, it has the least operational overhead because it requires no custom code to be written, deployed, or maintained. Why Incorrect Options are Wrong: A. An Application Load Balancer is designed for load balancing web traffic to targets like EC2 or containers, not as a primary tool for creating serverless APIs. This adds unnecessary complexity and cost compared to API Gateway. B. This is a valid serverless pattern, but it involves writing and maintaining Lambda function

</details>

### 187. dt-515

My Read Replica appears 'stuck' after a Multi-AZ failover and is unable to obtain or apply updates from the source DB Instance. What do I do?

<details><summary>Answer</summary>

**A. You will need to delete the Read Replica and create a new one to rep lace it.**

</details>

### 188. ce-521

A company hosts a database that runs on an Amazon RDS instance deployed to multiple Availability Zones. A periodic script negatively affects a critical application by querying the database. How can application performance be improved with minimal costs?

<details><summary>Answer</summary>

**B. Create a read replica of the database. Configure the script to query only the read replica.**

The core issue is resource contention on the primary database instance caused by a periodic script. An Amazon RDS Multi-AZ deployment provides high availability by maintaining a synchronous standby replica in a different Availability Zone, but this standby instance cannot serve read traffic. The most effective and standard architectural solution is to create a read replica. A read replica is a separate, asynchronously replicated database instance designed specifically to offload read-heavy workloads. By configuring the script to query the read replica, the load on the primary instance is eliminated, which directly improves the performance of the critical application that relies on it. Why Incorrect Options are Wrong: A. The standby instance in an RDS Multi-AZ deployment is passive and does not serve read traffic. Therefore, the script cannot query it. C. This is a manual, operational wor

</details>

### 189. dt-521

Amazon RDS automated backups and DB Snapshots are currently supported for only the [...] storage engine.

<details><summary>Answer</summary>

**A. InnoDB.**

</details>

### 190. ce-523

A company needs to ingest and analyze telemetry data from vehicles at scale for machine learning and reporting. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Timestream for LiveAnalytics to store data points. Grant Amazon SageMaker permission to access the data. Use Amazon QuickSight to visualize the data.**

This solution correctly identifies the most suitable AWS services for each part of the requirement. Amazon Timestream is a purpose-built, serverless time-series database, making it the ideal choice for ingesting and storing high-volume telemetry data from vehicles. Amazon SageMaker is the appropriate service for building, training, and deploying machine learning models. Amazon QuickSight is a business intelligence (BI) service that provides visualization and reporting capabilities and has a native connector for Amazon Timestream, allowing for direct analysis of the stored time-series data. This combination provides a scalable, integrated, and efficient architecture for the specified use case. Why Incorrect Options are Wrong: B: Amazon DynamoDB can store time-series data, but it is not purpose-built for it like Timestream, often requiring more complex data modeling and management at scale

</details>

### 191. et-526 `least-ops`

A solutions architect is reviewing the resilience of an application. The solutions architect notices that a database administrator recently failed over the application's Amazon Aurora PostgreSQL database writer instance as part of a scaling exercise. The failover resulted in 3 minutes of downtime for the application. Which solution will reduce the downtime for scaling exercises with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Set up an Amazon RDS proxy for the database. Update the application to use the proxy endpoint.**

Amazon RDS Proxy is a fully managed, highly available database proxy for Amazon RDS (Relational Database Service). It provides connection pooling, read/write splitting, and automatic failover, helping to improve the availability and scalability of database workloads.

</details>

### 192. et-529

A company is migrating its workloads to AWS. The company has transactional and sensitive data in its databases. The company wants to use AWS Cloud solutions to increase security and reduce operational overhead for the databases. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the databases to Amazon RDS Configure encryption at rest.**

Amazon RDS (Relational Database Service) is a fully managed database service that simplifies database management tasks, such as hardware provisioning, patching, and backups.  Encryption at Rest Amazon RDS supports encryption at rest, which means data stored in the database is automatically encrypted. This provides an additional layer of security for sensitive data. Managed Service: Amazon RDS is a managed service, meaning AWS takes care of operational aspects such as hardware maintenance, software patching, and backups. This reduces operational overhead for the company.

</details>

### 193. ce-531

A company is planning to migrate an on-premises online transaction processing (OLTP) database that uses MySQL to an AWS managed database management system. Several reporting and analytics applications use the on-premises database heavily on weekends and at the end of each month. The cloud-based solution must be able to handle read-heavy surges during weekends and at the end of each month. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Migrate the database to an Amazon Aurora MySQL cluster. Configure Aurora Auto Scaling to use replicas to handle surges.**

Amazon Aurora with MySQL compatibility is a fully managed relational database service designed for high-performance OLTP workloads. Its architecture separates compute and storage, allowing for highly efficient scaling. For handling read-heavy surges, Aurora supports up to 15 low-latency read replicas that share the same underlying storage volume as the primary instance. The key feature here is Aurora Auto Scaling, which automatically adds or removes Aurora Replicas in response to changes in workload, such as the predictable weekend and month-end reporting surges described. This provides an elastic, cost-effective solution to maintain performance without manual intervention. Why Incorrect Options are Wrong: B: Running MySQL on EC2 is not a fully managed database service. Using ephemeral (instance) storage for a database is extremely risky as data is lost if the instance is stopped or term

</details>

### 194. ce-535

A company has a large fleet of vehicles that are equipped with internet connectivity to send telemetry to the company. The company receives over 1 million data points every 5 minutes from the vehicles. The company uses the data in machine learning (ML) applications to predict vehicle maintenance needs and to preorder parts. The company produces visual reports based on the captured dat a. The company wants to migrate the telemetry ingestion, processing, and visualization workloads to AWS. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Timestream for LiveAnalytics to store the data points. Grant Amazon SageMaker permission to access the data for processing. Use Amazon QuickSight to visualize the data.**

This solution correctly identifies the most suitable AWS services for each part of the workload. Amazon Timestream is a purpose-built, serverless time-series database designed for high-volume telemetry data, making it ideal for ingesting and storing the vehicle data points. Amazon SageMaker is the primary AWS service for building, training, and deploying machine learning models, which directly addresses the predictive maintenance requirement. Amazon QuickSight is a business intelligence (BI) service that natively integrates with Timestream, allowing the company to easily create the required visual reports and dashboards. This combination provides a scalable, efficient, and well-architected solution for the described use case. Why Incorrect Options are Wrong: B: Amazon DynamoDB is a key-value database, not optimized for time-series analytical queries like Timestream is. While it can handl

</details>

### 195. et-536 `cost` `availability`

A company wants to provide data scientists with near real-time read-only access to the company's production Amazon RDS for PostgreSQL database. The database is currently configured as a Single-AZ database. The data scientists use complex queries that will not affect the production database. The company needs a solution that is highly available. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Change the setup from Single-AZ to a Multi-AZ DB cluster deployment and give the data scientists the cluster's reader endpoint.**

An RDS for PostgreSQL Multi-AZ DB cluster runs a writer plus two standby instances in two other Availability Zones, and both standbys serve reads through the reader endpoint. That covers high availability and read-only access for the data scientists with three instances and no extra components. Replication to the standbys is fast enough that the data they query is near real-time, and their heavy queries never touch the writer. Making the database a Multi-AZ instance deployment and then adding two read replicas reaches the same result with a fourth instance to pay for, so it is the more expensive answer.

</details>

### 196. et-537 `availability`

A company runs a three-tier web application in the AWS Cloud that operates across three Availability Zones. The application architecture has an Application Load Balancer, an Amazon EC2 web server that hosts user session states, and a MySQL database that runs on an EC2 instance. The company expects sudden increases in application traffic. The company wants to be able to scale to meet future application capacity demands and to ensure high availability across all three Availability Zones. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Migrate the MySQL database to Amazon RDS for MySQL with a Multi-AZ DB cluster deployment. Use Amazon ElastiCache for Redis with high availability to store session data and to cache reads. Migrate the web server to an Auto Scaling group that is in three Availability Zones.**

Migrating the MySQL database to Amazon RDS for MySQL with a Multi-AZ DB cluster deployment provides high availability by replicating the database across multiple Availability Zones. Using Amazon ElastiCache for Redis with high availability ensures that session data and reads are cached effectively, improving performance

</details>

### 197. et-540

A company has an on-premises server that uses an Oracle database to process and store customer information. The company wants to use an AWS database service to achieve higher availability and to improve application performance. The company also wants to offload reporting from its primary database system. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**D. Use Amazon RDS deployed in a Multi-AZ instance deployment to create an Amazon Aurora database. Direct the reporting functions to the reader instances.**

Deploying Amazon RDS in a Multi-AZ instance deployment ensures high availability by replicating the primary database instance in a different Availability Zone (AZ). This provides automatic failover in case of a hardware failure or maintenance event.

</details>

### 198. dt-545

A scope has been handed to you to set up a super fast gaming server and you decide that you will use Amazon DynamoDB as your database. For efficient access to data in a table, Amazon DynamoDB creates and maintains indexes for the primary key attributes. A secondary index is a data structure that contains a subset of attributes from a table, along with an alternate key to support Query operations. How many types of secondary indexes does DynamoDB support?

<details><summary>Answer</summary>

**A. 2.**

</details>

### 199. et-554

A company's SAP application has a backend SQL Server database in an on-premises environment. The company wants to migrate its on-premises application and database server to AWS. The company needs an instance type that meets the high demands of its SAP database. On-premises performance data shows that both the SAP application and the database have high memory utilization. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use the memory optimized instance family for both the application and the database.**

Memory optimized instances are designed to provide a high memory-to-CPU ratio, which aligns well with workloads that have significant memory requirements, such as SAP applications with backend databases.

</details>

### 200. et-561 `least-ops`

A company's website handles millions of requests each day, and the number of requests continues to increase. A solutions architect needs to improve the response time of the web application. The solutions architect determines that the application needs to decrease latency when retrieving product details from the Amazon DynamoDB table. Which solution will meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**A. Set up a DynamoDB Accelerator (DAX) cluster. Route all read requests through DAX.**

DynamoDB Accelerator (DAX) is a fully managed, highly available, and in-memory cache for DynamoDB. It is designed to improve the response time of read-intensive DynamoDB workloads by caching frequently accessed data. Using DAX helps reduce the read latency as it retrieves data from an in-memory cache instead of the DynamoDB table.

</details>

### 201. dt-564

When you run a DB Instance as a Multi-AZ deployment, the [...] serves database writes and reads

<details><summary>Answer</summary>

**D. primary.**

</details>

### 202. et-564

A company is building an ecommerce application and needs to store sensitive customer information. The company needs to give customers the ability to complete purchase transactions on the website. The company also needs to ensure that sensitive customer data is protected, even from database administrators. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Store sensitive data in Amazon RDS for MySQL. Use AWS Key Management Service (AWS KMS) client-side encryption to encrypt the data.**

Amazon RDS (Relational Database Service) for MySQL is a managed relational database service that makes it easy to set up, operate, and scale a MySQL database in the cloud. AWS Key Management Service (KMS) provides a way to create and control encryption keys. In the context of client-side encryption, the application (in this case, the ecommerce application) handles the encryption and decryption of data before it is stored in or retrieved from the database.

</details>

### 203. et-565

A company has an on-premises MySQL database that handles transactional data. The company is migrating the database to the AWS Cloud. The migrated database must maintain compatibility with the company's applications that use the database. The migrated database also must scale automatically during periods of increased demand. Which migration solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Database Migration Service (AWS DMS) to migrate the database to Amazon Aurora. Turn on Aurora Auto Scaling.**

AWS DMS is a fully managed service that helps you migrate databases to AWS easily and securely. It supports homogeneous and heterogeneous database migrations. Amazon Aurora is a fully managed relational database service that is compatible with MySQL and PostgreSQL. It provides high performance and availability with compatibility for MySQL, making it a seamless choice for migrating MySQL databases.

</details>

### 204. et-567 `least-ops`

A solutions architect is designing a workload that will store hourly energy consumption by business tenants in a building. The sensors will feed a database through HTTP requests that will add up usage for each tenant. The solutions architect must use managed services when possible. The workload will receive more features in the future as the solutions architect adds independent components. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon API Gateway with AWS Lambda functions to receive the data from the sensors, process the data, and store the data in an Amazon DynamoDB table.**

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. It acts as an entry point for HTTP requests and can handle the communication with the sensors. In this scenario, you can use Lambda functions to process the data received from the sensors.  Amazon DynamoDB is a fully managed NoSQL database that can handle the storage of the hourly energy consumption data.

</details>

### 205. dt-568

When you resize the Amazon RDS DB instance, Amazon RDS will perform the upgrade during the next maintenance window. If you want the upgrade to be performed now, rather than waiting for the maintenance window, specify the [...] option.

<details><summary>Answer</summary>

**D. Apply Immediately.**

</details>

### 206. ce-572 `least-ops`

A company is designing an application to connect AWS Lambda functions to an Amazon RDS for MySQL DB instance. The DB instance manages many connections. The company needs to modify the application to improve connectivity and recovery. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon RDS Proxy for connection pooling. Modify the application to use the RDS Proxy for connections to the DB instance.**

The scenario describes a classic issue where highly concurrent AWS Lambda functions can exhaust the connection limit of an Amazon RDS database. Amazon RDS Proxy is a fully managed database proxy specifically designed to address this problem. It establishes and manages a pool of database connections, allowing Lambda functions to reuse these connections efficiently. This improves scalability and application resilience against database failovers by handling them transparently. As a fully managed service, RDS Proxy introduces the least operational overhead compared to manual solutions. Why Incorrect Options are Wrong: B. An Amazon RDS instance is a database service itself and cannot function as a connection pooler for another database instance. This approach is technically infeasible. C. Read replicas are used to scale read-heavy workloads by offloading queries from the primary DB instance.

</details>

### 207. et-572

A company runs an application on AWS. The application receives inconsistent amounts of usage. The application uses AWS Direct Connect to connect to an on-premises MySQL-compatible database. The on-premises database consistently uses a minimum of 2 GiB of memory. The company wants to migrate the on-premises database to a managed AWS service. The company wants to use auto scaling capabilities to manage unexpected workload increases. Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**C. Provision an Amazon Aurora Serverless v2 database with a minimum capacity of 1 Aurora capacity unit (ACU).**

Aurora Serverless is designed for applications with variable or unpredictable workloads. With Aurora Serverless v2, you can set the minimum capacity to 1 Aurora capacity unit (ACU), and it will automatically scale based on the actual workload.

</details>

### 208. et-574 `cost`

A financial services company launched a new application that uses an Amazon RDS for MySQL database. The company uses the application to track stock market trends. The company needs to operate the application for only 2 hours at the end of each week. The company needs to optimize the cost of running the database. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Migrate the existing RDS for MySQL database to an Aurora Serverless v2 MySQL database cluster.**

Aurora Serverless allows the database to automatically start up, shut down, and scale capacity based on actual usage. With Aurora Serverless v2, you can set a minimum and maximum capacity for the cluster. This is suitable for intermittent workloads, such as the application that is only operated for 2 hours at the end of each week.

</details>

### 209. ce-575

A company is migrating a production environment application to the AWS Cloud. The company uses Amazon RDS for Oracle for the database layer. The company needs to configure thedatabase to meet the needs of high I/O intensive workloads that require low latency and consistent throughput. The database workloads are read intensive and write intensive. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure the RDS for Oracle database to use the Provisioned IOPS SSD storage type.**

The workload is described as high I/O intensive, requiring low latency and consistent throughput for both read and write operations. The Amazon RDS Provisioned IOPS SSD storage type (io1 and io2 Block Express) is specifically engineered for such demanding database workloads. It allows you to specify a consistent IOPS rate, ensuring predictable and sustained high performance with low latency, which directly meets the application's requirements. This storage type is the optimal choice for I/O-bound relational database workloads that cannot tolerate performance variability. Why Incorrect Options are Wrong: A. A Multi-AZ deployment is a high-availability and disaster recovery feature. It provides a synchronous standby replica for failover, not for enhancing the I/O performance of the primary database. C. General Purpose SSD storage provides a balance of price and performance but uses a burst

</details>

### 210. et-575 `availability`

A company deploys its applications on Amazon Elastic Kubernetes Service (Amazon EKS) behind an Application Load Balancer in an AWS Region. The application needs to store data in a PostgreSQL database engine. The company wants the data in the database to be highly available. The company also needs increased capacity for read workloads. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**C. Create an Amazon RDS database with Multi-AZ DB cluster deployment.**

Amazon RDS with Multi-AZ (Availability Zone) DB cluster deployment provides high availability by automatically replicating the primary database to a standby instance in a different Availability Zone. This helps ensure database availability in the event of a failure in the primary Availability Zone.

</details>

### 211. et-578 `least-ops`

A company deployed a serverless application that uses Amazon DynamoDB as a database layer. The application has experienced a large increase in users. The company wants to improve database response time from milliseconds to microseconds and to cache requests to the database. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use DynamoDB Accelerator (DAX).**

DAX is a fully managed, highly available, in-memory cache for DynamoDB that delivers fast response times for DynamoDB queries. It can be seamlessly integrated with existing DynamoDB applications, requiring minimal code changes. DAX allows you to cache frequently accessed data, reducing the need to read from the DynamoDB table and improving response times.

</details>

### 212. et-579

A company runs an application that uses Amazon RDS for PostgreSQL. The application receives traffic only on weekdays during business hours. The company wants to optimize costs and reduce operational overhead based on this usage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use the Instance Scheduler on AWS to configure start and stop schedules.**

Instance Scheduler: The AWS Instance Scheduler is a solution that allows you to schedule the start and stop times of your Amazon EC2 and RDS instances. By configuring start and stop schedules, you can ensure that resources are only running during the required business hours, thereby optimizing costs.

</details>

### 213. ce-582

A company wants to relocate its on-premises MySQL database to AWS. The database accepts regular imports from a client-facing application, which causes a high volume of write operations. The company is concerned that the amount of traffic might be causing performance issues within the application.

<details><summary>Answer</summary>

**A. Provision an Amazon RDS for MySQL DB instance with Provisioned IOPS SSD storage. Monitor write operation metrics by using Amazon CloudWatch. Adjust the provisioned IOPS if necessary.**

The scenario describes migrating a write-intensive MySQL database. Amazon RDS for MySQL is the appropriate managed service for this relocation. The key concern is performance degradation due to a "high volume of write operations." Amazon RDS Provisioned IOPS SSD (io1/io2 Block Express) storage is specifically engineered for I/O-intensive workloads, such as OLTP databases, that require consistent, low-latency performance. This storage type allows you to specify a consistent IOPS rate. By monitoring write operation metrics (like WriteIOPS and WriteLatency) in Amazon CloudWatch, the company can validate performance and dynamically adjust the provisioned IOPS level to meet application demands without over-provisioning. Why Incorrect Options are Wrong: B. Amazon ElastiCache is a caching service that primarily accelerates read-heavy workloads by reducing queries to the database; it does not so

</details>

### 214. ce-584

A company has an ordering application that stores customer information in Amazon RDS for MySQL. During regular business hours, employees run one-time queries for reporting purposes. Timeouts are occurring during order processing because the reporting queries are taking a long time to run. The company needs to eliminate the timeouts without preventing employees from performing queries.

<details><summary>Answer</summary>

**A. Create a read replica. Move reporting queries to the read replica.**

The root cause of the timeouts is resource contention on the single RDS for MySQL database instance. The long-running, read-intensive reporting queries are consuming resources (CPU, I/O, memory) needed by the time-sensitive, transactional ordering application. The standard and most effective solution for this scenario in RDS is to create a read replica. A read replica is an asynchronous copy of the primary database. By directing the reporting queries to the read replica, the analytical workload is isolated from the transactional workload. This frees the primary DB instance to handle order processing exclusively, resolving the contention and eliminating timeouts without restricting when employees can run reports. Why Incorrect Options are Wrong: B. The ordering application performs writes (creating orders), which cannot be directed to a read-only replica. This architecture would cause app

</details>

### 215. et-590

A company migrated a MySQL database from the company's on-premises data center to an Amazon RDS for MySQL DB instance. The company sized the RDS DB instance to meet the company's average daily workload. Once a month, the database performs slowly when the company runs queries for a report. The company wants to have the ability to run reports and maintain the performance of the daily workloads. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a read replica of the database. Direct the queries to the read replica.**

Read Replica: Creating a read replica of the database allows you to offload read queries to a replica instance. This helps in distributing the workload and prevents the additional load from impacting the performance of the primary database.  Direct Queries to the Read Replica: By directing the queries for the monthly reports to the read replica, you ensure that the heavy reporting workload doesn't affect the performance of the primary database handling daily workloads. Read replicas are designed to handle read-intensive workloads, providing a scalable solution.

</details>

### 216. dt-592

Can I control if and when MySQL based RDS Instance is upgraded to new supported versions?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 217. dt-593

If I have multiple Read Replicas for my master DB Instance and I promote one of them, what happens to the rest of the Read Replicas?

<details><summary>Answer</summary>

**A. The remaining Read Replicas will still replicate from the older master DB Instance.**

</details>

### 218. et-593 `availability`

A solutions architect is designing a highly available Amazon ElastiCache for Redis based solution. The solutions architect needs to ensure that failures do not result in performance degradation or loss of data locally and within an AWS Region. The solution needs to provide high availability at the node level and at the Region level. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Multi-AZ Redis replication groups with shards that contain multiple nodes.**

Multi-AZ (Availability Zone) replication groups provide high availability at the node level. In a Multi-AZ setup, your data is replicated asynchronously to a standby replica in a different Availability Zone. Using shards with multiple nodes within each Availability Zone further enhances availability and provides scalability.

</details>

### 219. et-596 `cost`

An ecommerce application uses a PostgreSQL database that runs on an Amazon EC2 instance. During a monthly sales event, database usage increases and causes database connection issues for the application. The traffic is unpredictable for subsequent monthly sales events, which impacts the sales forecast. The company needs to maintain performance when there is an unpredictable increase in traffic. Which solution resolves this issue in the MOST cost-effective way?

<details><summary>Answer</summary>

**A. Migrate the PostgreSQL database to Amazon Aurora Serverless v2.**

Aurora Serverless is a serverless relational database engine provided by Amazon. It automatically adjusts its capacity based on actual usage, allowing it to scale up or down as needed. Aurora Serverless v2 builds upon the original Aurora Serverless model with additional features for even more efficient scaling.

</details>

### 220. et-601 `least-ops`

A company runs its critical database on an Amazon RDS for PostgreSQL DB instance. The company wants to migrate to Amazon Aurora PostgreSQL with minimal downtime and data loss. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Aurora read replica of the RDS for PostgreSQL DB instance. Promote the Aurora read replicate to a new Aurora PostgreSQL DB cluster.**

Aurora Read Replica: Creating an Aurora read replica from the RDS for PostgreSQL DB instance is a low-impact operation that allows you to replicate the data to Aurora with minimal downtime. Promote to Aurora PostgreSQL DB Cluster: Once the read replica is in sync with the primary RDS instance, you can promote the Aurora read replica to become the new primary cluster.

</details>

### 221. dt-603

SQL Server [...] store log ins and passwords in the master database.

<details><summary>Answer</summary>

**C. does.**

</details>

### 222. ce-605

A company has 5 TB of datasets. The datasets consist of 1 million user profiles and 10 million connections. The user profiles have connections as many-to-many relationships. The company needs a performance-efficient way to find mutual connections up to five levels. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon Neptune to store the datasets with edges and vertices. Query the data to find connections.**

The problem describes a highly connected dataset (user profiles and connections) and requires performance-efficient traversal of these relationships up to five levels deep. This is a classic graph database use case. Amazon Neptune is a purpose-built, fully managed graph database service designed to store and query billions of relationships with millisecond latency. It is optimized for complex graph traversal queries, such as finding mutual connections in a social network, which would be slow and computationally expensive using the recursive JOIN operations required by SQL-based systems like Amazon RDS or Amazon Athena. Why Incorrect Options are Wrong: A. Using Amazon Athena with SQL JOINs for a five-level deep relationship query on a large dataset would be extremely inefficient and slow, failing the performance requirement. C. Amazon QuickSight is a business intelligence and visualizatio

</details>

### 223. dt-618

A client needs you to import some existing infrastructure from a dedicated hosting provider to AWS to try and save on the cost of running his current website. He also needs an automated process that manages backups, software patching, automatic failure detection, and recovery. You are aware that his existing set up currently uses an Oracle database. Which of the following AWS databases would be best for accomplishing this task?

<details><summary>Answer</summary>

**A. Amazon RDS.**

</details>

### 224. dt-620

Amazon RDS creates an SSL certificate and installs the certificate on the DB Instance when Amazon RDS provisions the instance. These certificates are signed by a certificate authority. The [...] is stored at <https://rds.amazonaws.com/doc/rds-ssl-ca-cert.pem>.

<details><summary>Answer</summary>

**A. private key.**

</details>

### 225. et-622

A company is creating a new web application for its subscribers. The application will consist of a static single page and a persistent database layer. The application will have millions of users for 4 hours in the morning, but the application will have only a few thousand users during the rest of the day. The company's data architects have requested the ability to rapidly evolve their schema. Which solutions will meet these requirements and provide the MOST scalability? (Choose two.)

<details><summary>Answer</summary>

**C. Deploy Amazon DynamoDB as the database solution. Ensure that DynamoDB auto scaling is enabled.**

DynamoDB auto scaling allows the database to automatically adjust its read and write capacity based on the application's traffic, making it well-suited for varying workloads.  D. Deploy the static content into an Amazon S3 bucket. Provision an Amazon CloudFront distribution with the S3 bucket as the origin.  Amazon S3 is a highly scalable and durable object storage service, and using CloudFront, a content delivery network (CDN), helps distribute static content globally, reducing latency and providing scalability.

</details>

### 226. ce-624

A company needs to accommodate traffic for a web application that the company hosts on AWS, especially during peak usage hours. The application uses Amazon EC2 instances as web servers, an Amazon RDS DB instance for database operations, and an Amazon S3 bucket to store transaction documents. The application struggles to scale effectively and experiences performance issues. The company wants to improve the scalability of the application and prevent future performance issues. The company also wants to improve global access speeds to the transaction documents for the company's global users. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Place the EC2 instances in Auto Scaling groups to scale appropriately during peak usage hours. Use Amazon RDS read replicas to improve database read performance. Deploy an Amazon CloudFront distribution that uses Amazon S3 as the origin.**

This solution directly addresses the three distinct problems outlined in the scenario using the most appropriate AWS services. 1. EC2 Scaling: Amazon EC2 Auto Scaling groups automatically adjust the number of EC2 instances to meet traffic demands, ensuring performance during peak hours and cost-effectiveness during lulls. This directly solves the web server scaling issue. 2. Database Performance: Amazon RDS read replicas offload read-heavy traffic from the primary database instance. This allows the application to scale its read capacity beyond a single DB instance, directly addressing the database performance bottleneck. 3. Global Content Delivery: Amazon CloudFront is a content delivery network (CDN) that caches content in edge locations globally. Using it with an S3 origin significantly reduces latency for global users accessing the transaction documents. Why Incorrect Options are Wron

</details>

### 227. ce-627

An ecommerce company runs a multi-tier application on AWS. The frontend and backend tiers both run on Amazon EC2 instances. The database tier runs on an Amazon RDS for MySQL DB instance. The backend tier communicates with the RDS DB instance. The application makes frequent calls to return identical datasets from the database. The frequent calls on the database cause performance slowdowns. A solutions architect must improve the performance of the application backend. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Configure an Amazon ElastiCache (Redis OSS) cache. Configure the backend EC2 instances to read from the cache.**

The core issue is performance degradation due to frequent, repetitive read queries on the Amazon RDS for MySQL database. The most effective architectural pattern to solve this is to introduce a caching layer. Amazon ElastiCache is a fully managed in-memory caching service designed to improve the performance of web applications by retrieving information from fast, managed, in-memory caches, instead of relying entirely on slower disk-based databases. By caching the identical datasets, ElastiCache reduces the load on the RDS instance and significantly decreases latency for read operations, directly addressing the performance bottleneck. Why Incorrect Options are Wrong: A. Amazon SNS is a pub/sub messaging service used for decoupling microservices, distributed systems, and serverless applications. It is not a caching solution. C. Amazon DynamoDB Accelerator (DAX) is an in-memory cache specif

</details>

### 228. dt-627 `availability`

A company is deploying a new two-tier web application in AWS. The company has limited staff and requires high availability, and the application requires complex queries and table joins. Which configuration provides the solution for the company's requirements?

<details><summary>Answer</summary>

**B. Amazon RDS for MySQL with Multi-AZ.**

</details>

### 229. et-633

A company manages an application that stores data on an Amazon RDS for PostgreSQL Multi-AZ DB instance. Increases in traffic are causing performance problems. The company determines that database queries are the primary reason for the slow performance. What should a solutions architect do to improve the application's performance?

<details><summary>Answer</summary>

**C. Create a read replica from the source DB instance. Serve read traffic from the read replica.**

Creating read replicas allows you to offload read traffic from the primary (master) DB instance to one or more read replicas. Read replicas can serve read-only queries, distributing the load and improving overall query performance.

</details>

### 230. et-637

A solutions architect is designing a new service behind Amazon API Gateway. The request patterns for the service will be unpredictable and can change suddenly from 0 requests to over 500 per second. The total size of the data that needs to be persisted in a backend database is currently less than 1 GB with unpredictable future growth. Data can be queried using simple key-value requests. Which combination ofAWS services would meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Amazon DynamoDB**

AWS Lambda is a serverless compute service that automatically scales with the number of incoming requests. It's suitable for unpredictable workloads, as it allows you to run code without provisioning or managing servers. Lambda functions can be triggered by API Gateway for handling HTTP requests. Amazon DynamoDB (Option C):  DynamoDB is a fully managed NoSQL database service that can handle unpredictable and scalable workloads. It provides low-latency, high-throughput performance for simple key-value queries. DynamoDB automatically scales to accommodate varying request rates, and you pay for the throughput you provision.

</details>

### 231. ce-641

A company stores a large dataset for an online advertising business in an Amazon RDS for MySQL DB instance. The company wants to run business reporting queries on the data without affecting write operations to the DB instance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy RDS read replicas to process the business reporting queries.**

Amazon RDS Read Replicas are designed specifically for offloading read-heavy workloads, such as business reporting queries, from the primary (source) DB instance. By creating a read replica, you get a read-only copy of your database that is updated asynchronously from the source. Directing the reporting queries to the read replica isolates this workload, ensuring that the performance of write operations on the primary DB instance is not affected. This solution directly addresses the requirement to separate read and write traffic to maintain performance. Why Incorrect Options are Wrong: B: You cannot place a standard RDS DB instance behind an Elastic Load Balancer to scale it horizontally. This architecture is not supported and does not solve the read/write workload separation issue. C: Scaling up (vertical scaling) provides more resources to a single instance but does not isolate workloa

</details>

### 232. ce-642

A gaming company has a web application that displays game scores. The application runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The application stores data in an Amazon RDS for MySQL database. Users are experiencing long delays and interruptions caused by degraded database read performance. The company wants to improve the user experience. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Use an Amazon ElastiCache (Redis OSS) cache in front of the database.**

The core issue is degraded database read performance, leading to long delays for users. An in-memory cache is the most effective solution for this common problem. Amazon ElastiCache provides a managed in-memory data store that can be placed in front of the RDS database. By caching frequently requested data, such as game scores, the application can retrieve this data from the high-speed, low-latency cache instead of querying the disk-based database for every request. This significantly reduces the read load on the RDS instance, improves response times, and enhances the user experience. Why Incorrect Options are Wrong: B. Use Amazon RDS Proxy between the application and the database. RDS Proxy primarily manages database connections through pooling, which is beneficial for applications with many connections, but it does not cache data or directly offload read queries to improve read perform

</details>

### 233. dt-642

You are running PostgreSQL on Amazon RDS and it seems to be all running smoothly deployed in one Availability Zone. A database administrator asks you if DB instances running PostgreSQL support Multi-AZ deployments. What would be a correct response to this question?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 234. ce-643

A city's weather forecast team is using Amazon DynamoDB in the data tier for an application. The application has several components. The analysis component of the application requires repeated reads against a large dataset. The application has started to temporarily consume all the read capacity in the DynamoDB table and is negatively affecting other applications that need to access the same data. Which solution will resolve this issue with the LEAST development effort?

<details><summary>Answer</summary>

**A. Use DynamoDB Accelerator (DAX).**

Amazon DynamoDB Accelerator (DAX) is a fully managed, in-memory cache specifically designed for DynamoDB. It addresses the scenario by offloading the high-volume, repeated read requests from the analysis component to the cache. This significantly reduces the read load on the underlying DynamoDB table, freeing up provisioned read capacity for other applications. Implementing DAX requires minimal code changes, as the DAX client is a drop-in replacement for the standard DynamoDB client, fulfilling the requirement for the "LEAST development effort." The application's existing API calls for reading data will be automatically directed to the DAX cluster without needing to rewrite application logic. Why Incorrect Options are Wrong: B. Use Amazon CloudFront in front of DynamoDB. CloudFront is a Content Delivery Network (CDN) for web content, not a database query cache. Integrating it would requi

</details>

### 235. ce-645

A solutions architect has created an AWS Lambda function that makes queries to an Amazon Aurora MySQL DB instance. When the solutions architect performs a test, the DB instance shows an error for too many connections. Which solution will meet these requirements with the LEAST operational effort?

<details><summary>Answer</summary>

**D. Create a proxy in Amazon RDS Proxy. Query the proxy instead of the DB instance.**

AWS Lambda functions can scale rapidly, leading to a high number of concurrent executions. Each execution can open a new database connection, quickly exhausting the maximum number of connections allowed by an Amazon Aurora DB instance. Amazon RDS Proxy is a fully managed database proxy designed specifically for this scenario. It establishes and manages a pool of database connections, allowing Lambda functions to reuse these connections. This approach improves application scalability and resilience by efficiently handling connection surges without overwhelming the database, directly solving the "too many connections" error with minimal changes to the application code. Why Incorrect Options are Wrong: A. A read replica is used to scale read-intensive workloads, not to manage connection pooling. The replica would likely face the same connection exhaustion issue as the primary instance. B. M

</details>

### 236. dt-646 `cost`

A large company wants to provide its globally located developers separate, limited size, managed PostgreSQL databases for development purposes. The databases will be low volume. The developers need the databases only when they are actively working. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon Aurora Serverless cluster. Develop an AWS Service Catalog product to launch databases in the cluster with the default capacity settings. Grant the developers access to the product.**

</details>

### 237. dt-648

A company's web application consists of multiple Amazon EC2 instances that run behind an Application Load Balancer in a VPC. An Amazon RDS for MySQL DB instance contains the data. The company needs the ability to automatically detect and respond to suspicious or unexpected behavior in its AWS environment. The company already has added AWS WAF to its architecture. What should a solutions architect do next to protect against threats?

<details><summary>Answer</summary>

**A. Use Amazon GuardDuty to perform threat detection. Configure Amazon EventBridge (Amazon CloudWatch Events) to filter for GuardDuty findings and to invoke an AWS Lambda function to adjust the AWS WAF rules.**

</details>

### 238. et-649 `cost`

An ecommerce company runs a PostgreSQL database on premises. The database stores data by using high IOPS Amazon Elastic Block Store (Amazon EBS) block storage. The daily peak I/O transactions per second do not exceed 15,000 IOPS. The company wants to migrate the database to Amazon RDS for PostgreSQL and provision disk IOPS performance independent of disk storage capacity. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Configure the General Purpose SSD (gp3) EBS volume storage type and provision 15,000 IOPS.**

Amazon EBS gp3 volumes are designed for general-purpose workloads and offer a balance of price and performance. They allow you to provision IOPS independently of storage capacity, similar to io1 volumes.

</details>

### 239. ce-650 `least-ops`

A companyQUESTIO N NO: 24 A company has launched an Amazon RDS for MySQL DB instance. Most of the connections to the database come from serverless applications. Application traffic to the database changes significantly at random intervals. At times of high demand, users report that their applications experience database connection rejection errors. Which solution will resolve this issue with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create a proxy in RDS Proxy. Configure the users' applications to use the DB instance through RDS Proxy.**

The scenario describes a classic issue where serverless applications, which can scale out rapidly, exhaust the maximum number of available connections on a relational database. Amazon RDS Proxy is a fully managed service designed specifically for this use case. It establishes and manages a pool of database connections. Applications connect to the proxy, which then efficiently reuses connections from the pool to serve requests. This prevents the database from being overwhelmed by a sudden surge in connection requests from numerous serverless function invocations, directly resolving the connection rejection errors with minimal operational overhead. Why Incorrect Options are Wrong: B. Amazon ElastiCache is an in-memory caching service. While it can reduce read load on the database, it does not manage or pool database connections, failing to solve the core issue. C. Migrating to a larger ins

</details>

### 240. et-650 `least-ops`

A company wants to migrate its on-premises Microsoft SQL Server Enterprise edition database to AWS. The company's online application uses the database to process transactions. The data analysis team uses the same production database to run reports for analytical processing. The company wants to reduce operational overhead by moving to managed services wherever possible. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Migrate to Amazon RDS for Microsoft SOL Server. Use read replicas for reporting purposes**

Amazon RDS supports read replicas, allowing you to offload reporting and analytical workloads to replicas without impacting the performance of the primary database. This is a cost-effective and efficient way to handle reporting without affecting transactional processing on the primary database.

</details>

### 241. ce-653 `availability`

A company wants to migrate an Oracle database to AWS. The database consists of a single table that contains millions of geographic information systems (GIS) images that are high resolution and are identified by a geographic code. When a natural disaster occurs, tens of thousands of images get updated every few minutes. Each geographic code has a single image or row that is associated with it. The company wants a solution that is highly available and scalable during such events.

<details><summary>Answer</summary>

**B. Store the images in Amazon S3 buckets. Use Amazon DynamoDB with the geographic code as the key and the image S3 URL as the value.**

This solution follows a well-established AWS best practice for managing large binary objects and their associated metadata. Storing high-resolution images in Amazon S3 provides virtually unlimited scalability, high durability, and cost-effective storage. Amazon DynamoDB is a fully managed NoSQL database designed for high-performance, low-latency data retrieval at any scale. Using the geographic code as the partition key in DynamoDB allows for extremely fast lookups and can easily scale to handle the high-velocity updates ("tens of thousands... every few minutes") during disaster events, especially when using on-demand capacity mode. This architecture decouples the large object storage from the metadata index, creating a highly scalable and available system. Why Incorrect Options are Wrong: A. Storing millions of large image files directly within an Oracle database (as BLOBs) is an anti-p

</details>

### 242. gh-653

A company maintains an Amazon RDS database that maps users to cost centers. The company has accounts in an organization in AWS
Organizations. The company needs a solution that will tag all resources that are created in a speci c AWS account in the organization. The
solution must tag each resource with the cost center ID of the user who created the resource.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Create a Lambda function triggered by EventBridge (via CloudTrail) to tag resources based on the RDS cost center DB.**

EventBridge + Lambda automates real-time tagging without manual intervention.
SCPs (Option A) cannot dynamically tag resources, and scheduled rules (Option C) are not event-driven.

</details>

### 243. dt-654

A company runs several Amazon RDS for Oracle On-Demand DB instances that have high utilization. The RDS DB instances run in member accounts that are in an organization in AWS Organizations. The company's finance team has access to the organization's management account and member accounts. The finance team wants to find ways to optimize costs by using AWS Trusted Advisor. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use the Trusted Advisor recommendations in the management account.; C. Review the Trusted Advisor checks for Amazon RDS Reserved Instance Optimization.**

</details>

### 244. gh-654 `availability`

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

### 245. dt-658 `least-ops`

A company uses Amazon RDS with default backup settings for its database tier. The company needs to make a daily backup of the database to meet regulatory requirements. The company must retain the backups for 30 days. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Modify the RDS database to have a retention period of 30 days for automated backups.**

</details>

### 246. dt-659

A company is running a multi-tier web application on AWS. The application runs its database tier on Amazon Aurora MySQL. The application and database tiers are in the us-east-1 Region. A database administrator who regularly monitors the Aurora DB cluster finds that an intermittent increase in read traffic is creating high CPU utilization on the read replica and causing increased read latency of the application. What should a solutions architect do to improve read scalability?

<details><summary>Answer</summary>

**D. Configure Aurora Auto Scaling for the read replica.**

</details>

### 247. dt-660 `cost`

A company that runs its application on AWS uses an Amazon Aurora DB cluster as its database. During peak usage hours when multiple users access and read the data, the monitoring system shows degradation of database performance for write queries. The company wants to increase the scalability of the application to meet peak usage demands. Which solution will meet these requirements MOST cost effectively?

<details><summary>Answer</summary>

**C. Create an Aurora read replica in the existing Aurora DB cluster. Update the application to use the replica endpoint for read only queries and to use the cluster endpoint for write queries.**

</details>

### 248. et-661 `least-ops`

A company runs applications on AWS that connect to the company's Amazon RDS database. The applications scale on weekends and at peak times of the year. The company wants to scale the database more effectively for its applications that connect to the database. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon RDS Proxy with a target group for the database. Change the applications to use the RDS Proxy endpoint.**

RDS Proxy manages scaling connections with minimal code changes. DynamoDB (Option A) is incompatible with RDS.

</details>

### 249. ce-666

A solutions architect must design a database solution for a high-traffic ecommerce web application. The database stores customer profiles and shopping cart information. The database must support a peak load of several million requests each second and deliver responses in milliseconds. The operational overhead for managing and scaling the database must be minimized. Which database solution should the solutions architect recommend?

<details><summary>Answer</summary>

**B. Amazon DynamoDB**

The scenario requires a database for a high-traffic e-commerce application that can handle millions of requests per second with millisecond latency and minimal operational overhead. Amazon DynamoDB is a fully managed, serverless, NoSQL key-value and document database designed for this exact use case. It delivers consistent, single-digit millisecond performance at any scale, automatically scaling throughput capacity to meet traffic demands without administrative intervention. Its data model is well-suited for storing customer profiles and shopping cart data, making it the optimal choice to meet all stated requirements. Why Incorrect Options are Wrong: A. Amazon Aurora: While a high-performance relational database, scaling to millions of requests per second for this type of transactional workload is challenging and not its primary design point compared to DynamoDB. C. Amazon RDS: A standar

</details>

### 250. et-669 `least-ops`

A company runs its databases on Amazon RDS for PostgreSQL. The company wants a secure solution to manage the master user password by rotating the password every 30 days. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Integrate AWS Secrets Manager with Amazon RDS for PostgreSQL to automate password rotation.**

Secrets Manager automates rotation every 30 days with zero operational effort. Manual rotation (Option B) or Parameter Store (Option D) lacks automation.

</details>

### 251. gh-670

A company performs tests on an application that uses an Amazon DynamoDB table. The tests run for 4 hours once a week. The company knows
how many read and write operations the application performs to the table each second during the tests. The company does not currently use
DynamoDB for any other use case. A solutions architect needs to optimize the costs for the table.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Choose on-demand capacity mode for the table.**

The table is used for 4 hours a week and sits idle the rest of the time. On-demand mode charges per read and write request and nothing for idle time, so the bill tracks the actual 4 hours of testing. Provisioned mode charges for the capacity units every hour of the month, so roughly 97 percent of what you paid would be for an idle table; on-demand only loses to provisioned once a table is busy something like 15 to 20 percent of the time, far above this workload. Reserved capacity deepens the problem by committing to those hourly charges for a year or more. Knowing the per-second request rate is a distractor - predictable traffic favours provisioned capacity only when the table is busy most of the time.

</details>

### 252. ce-673

An application has performance issues due to increased demand. The demand is on read-only historical records in Amazon RDS using custom queries. The company wants improved performance without changing database structure and with minimal management overhead. Which approach meets the requirement?

<details><summary>Answer</summary>

**B. Deploy Amazon ElastiCache (Redis OSS) and cache application data.**

The most effective solution is to implement a caching layer to offload read requests from the Amazon RDS database. Amazon ElastiCache is a fully managed service that simplifies the deployment and management of an in-memory cache. By caching the results of frequent, read-only custom queries, the application can retrieve data from the high-speed ElastiCache layer instead of the RDS database, significantly improving performance. This approach meets the requirements as it does not alter the database structure and, being a managed service, introduces minimal management overhead compared to self-hosting a cache on EC2. Why Incorrect Options are Wrong: A. Migrating all data to DynamoDB is a fundamental change to the database structure and architecture, which explicitly violates a core requirement of the problem. C. Deploying and managing Memcached on EC2 instances creates significant operationa

</details>

### 253. ce-675 `performance`

An application is experiencing performance issues based on increased demand. This increased demand is on read-only historical records pulled from an Amazon RDS-hosted database with custom views and queries. A solutions architect must improve performance without changing the database structure. Which approach will improve performance and MINIMIZE management overhead?

<details><summary>Answer</summary>

**B. Deploy Amazon ElastiCache (Redis OSS) and cache the data for the application.**

The scenario describes a read-heavy workload on an Amazon RDS database causing performance degradation. The most effective strategy to alleviate this is to implement a caching layer to serve the frequently accessed, read-only historical data. Amazon ElastiCache is a fully managed in-memory caching service that is ideal for this purpose. By caching the results of the custom queries and views, the application can retrieve data from the low-latency ElastiCache service instead of repeatedly querying the RDS database. This approach directly addresses the performance issue, requires no changes to the database structure, and aligns with the requirement to minimize management overhead by using a managed AWS service. Why Incorrect Options are Wrong: A. Migrating to DynamoDB is a major architectural change involving data migration and application refactoring, which is high overhead and violates th

</details>

### 254. dt-679

A company hosts a data lake on AWS. The data lake consists of data in Amazon S3 and Amazon RDS for PostgreSQL. The company needs a reporting solution that provides data visualization and includes all the data sources within the data lake. Only the company's management team should have full access to all the visualizations. The rest of the company should have only limited access. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an analysis in Amazon QuickSight. Connect all the data sources and create new datasets. Publish dashboards to visualize the data. Share the dashboards with the appropriate IAM roles.**

</details>

### 255. dt-680 `availability`

A company runs an ecommerce application on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales based on CPU utilization metrics. The ecommerce application stores the transaction data in a MySQL 8.0 database that is hosted on a large EC2 instance. The database's performance degrades quickly as application load increases. The application handles more read requests than write transactions. The company wants a solution that will automatically scale the database to meet the demand of unpredictable read workloads while maintaining high availability. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon Aurora with a Multi-AZ deployment. Configure Aurora Auto Scaling with Aurora Replicas.**

</details>

### 256. ce-691

A company's ecommerce website has unpredictable traffic and uses AWS Lambda functions to directly access a private Amazon RDS for PostgreSQL DB instance. The company wants to maintain predictable database performance and ensure that the Lambda invocations do not overload the database with too many connections. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Point the client driver at an RDS Proxy endpoint. Deploy the Lambda functions inside a VPC.**

The scenario describes a classic use case for Amazon RDS Proxy. AWS Lambda's highly concurrent nature can exhaust a database's connection limit. RDS Proxy sits between the application (Lambda) and the database, pooling and sharing established database connections. This allows a large number of Lambda function invocations to reuse a smaller, managed pool of connections, preventing overload and maintaining predictable performance. Since the RDS instance is private, the Lambda functions must be deployed inside the same VPC to establish network connectivity to the RDS Proxy endpoint. Why Incorrect Options are Wrong: A. RDS custom endpoints are used to direct traffic to specific DB instances (like read replicas) and do not provide connection pooling to solve the connection exhaustion problem. C. This option is incorrect because custom endpoints do not solve the connection pooling issue, and a

</details>

### 257. dt-694 `cost`

A development team runs monthly resource-intensive tests on its general purpose Amazon RDS for MySQL DB instance with Performance Insights enabled. The testing lasts for 48 hours once a month and is the only process that uses the database. The team wants to reduce the cost of running the tests without reducing the compute and memory attributes of the DB instance. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a snapshot when tests are completed. Terminate the DB instance and restore the snapshot when required.**

</details>

### 258. dt-695

A company that hosts its web application on AWS wants to ensure all Amazon EC2 instances, Amazon RDS DB instances, and Amazon Redshift clusters are configured with tags. The company wants to minimize the effort of configuring and operating this check. What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**A. Use AWS Config rules to define and detect resources that are not properly tagged.**

</details>

### 259. dt-696

A company runs an online marketplace web application on AWS. The application serves hundreds of thousands of users during peak hours. The company needs a scalable, near-real-time solution to share the details of millions of financial transactions with several other internal applications. Transactions also need to be processed to remove sensitive data before being stored in a document database for low-latency retrieval. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Stream the transactions data into Amazon Kinesis Data Streams. Use AWS Lambda integration to remove sensitive data from every transaction and then store the transactions data in AmazonDynamoDB. Other applications can consume the transactions data off the Kinesis data stream.**

</details>

### 260. ce-702

An ecommerce company runs a multi-tier application on AWS. The frontend and backend tiers run on Amazon EC2 instances. The database tier runs on an Amazon RDS for MySQL DB instance. The application makes frequent calls to return identical datasets from the database. These frequent calls cause performance slowdowns. A solutions architect must improve the performance of the application backend. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Configure an Amazon ElastiCache (Redis OSS) cache. Configure the backend EC2 instances to read from the cache.**

The problem describes frequent database calls for identical datasets, causing performance issues. This is a classic use case for caching. Amazon ElastiCache is an in-memory caching service that can store the results of these frequent queries. By configuring the backend EC2 instances to first check the ElastiCache for Redis cache, the application can retrieve data with microsecond latency, significantly reducing the load on the RDS for MySQL database and improving overall application performance. This directly addresses the root cause of the slowdown. Why Incorrect Options are Wrong: A. Amazon SNS is a pub/sub messaging service. It does not cache data or reduce database read load for an application. C. Amazon DynamoDB Accelerator (DAX) is a caching service specifically for Amazon DynamoDB, not for Amazon RDS for MySQL. D. Amazon Data Firehose is a data streaming service used for loading d

</details>

### 261. ce-708 `cost`

A company hosts a public web application on AWS with a three-tier architecture: a frontend Auto Scaling group, an application Auto Scaling group, and an Amazon RDS database. During unexpected traffic spikes, the company notices long delays in startup time when the frontend and application tiers scale out. The company needs to improve scaling performance without negatively affecting user experience. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure the maximum number of instances for both Auto Scaling groups to the number required for peak demand. Create a warm pool.**

The core issue is the long startup time for new instances during scale-out events. An Amazon EC2 Auto Scaling warm pool is designed specifically to solve this problem. It maintains a pool of pre-initialized EC2 instances in a stopped state. When the application needs to scale out, instances are started from the warm pool, which is significantly faster than launching and configuring new instances from scratch. This improves scaling performance without affecting users. It is cost-effective because stopped instances incur lower charges than running instances. Setting the maximum size to handle peak demand ensures the application can scale sufficiently. Why Incorrect Options are Wrong: A. Setting the desired number of instances to meet peak demand at all times is not cost-effective, as you pay for idle capacity during non-peak hours. C. Setting the maximum number of instances to normal deman

</details>

### 262. dt-708

A company uses a Microsoft SQL Server database. The company's applications are connected to the database. The company wants to migrate to an Amazon Aurora PostgreSQL database with minimal changes to the application code. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Enable Babelfish on Aurora PostgreSQL to run the SQL queries from the applications.; C. Migrate the database schema and data by using the AWS Schema Conversion Tool (AWS SCT) and AWS Database Migration Service (AWS DMS).**

</details>

### 263. dt-715 `cost` `availability`

A company has migrated a two-tier application from its on-premises data center to the AWS Cloud. The data tier is a Multi-AZ deployment of Amazon RDS for Oracle with 12 TB of General Purpose SSD Amazon Elastic Block Store (Amazon EBS) storage. The application is designed to process and store documents in the database as binary large objects (blobs) with an average document size of 6 MB. The database size has grown over time, reducing the performance and increasing the cost of storage. The company must improve the database performance and needs a solution that is highly available and resilient. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon S3 bucket. Update the application to store documents in the S3 bucket. Store the object metadata in the existing database.**

</details>

### 264. dt-717

A company is creating a three-tier web application consisting of a web server, an application server, and a database server. The application will track GPS coordinates of packages as they are being delivered. The application will update the database every 0.5 seconds. The tracking will need to be read as fast as possible for users to check the status of their packages. Only a few packages might be tracked on some days, whereas millions of packages might be tracked on other days. Tracking will need to be searchable by tracking ID, customer ID, and order ID. Orders older than 1 month no longer need to be tracked. What should a solutions architect recommend to accomplish this with minimal total cost of ownership?

<details><summary>Answer</summary>

**B. Use Amazon DynamoDB with global secondary indexes. Activate Auto Scaling for the DynamoDB table and the global secondary indexes. Turn on TTL for the DynamoDB table.**

</details>

### 265. dt-725

A company's legacy application is currently relying on a single-instance Amazon RDS MySQL database without encryption. Due to new compliance requirements, all existing and new data in this database must be encrypted. How should this be accomplished?

<details><summary>Answer</summary>

**C. Take a snapshot of the RDS instance. Create an encrypted copy of the snapshot. Restore the RDS instance from the encrypted snapshot.**

</details>

### 266. dt-734

A company is running a multi-tier web application on premises. The web application is containerized and runs on a number of Linux hosts connected to a PostgreSQL database that contains user records. The operational overhead of maintaining the infrastructure and capacity planning is limiting the company's growth. A solutions architect must improve the application's infrastructure. Which combination of actions should the solutions architect take to accomplish this? (Choose two.)

<details><summary>Answer</summary>

**A. Migrate the PostgreSQL database to Amazon Aurora.; E. Migrate the web application to be hosted on AWS Fargate with Amazon Elastic Container Service (Amazon ECS).**

</details>

### 267. dt-735

An application allows users at a company's headquarters to access product data. The product data is stored in an Amazon RDS MySQL DB instance. The operations team has isolated an application performance slowdown and wants to separate read traffic from write traffic. A solutions architect needs to optimize the application's performance quickly. What should the solutions architect recommend?

<details><summary>Answer</summary>

**D. Create read replicas for the database. Configure the read replicas with the same compute and storage resources as the source database.**

</details>

### 268. dt-736

A company is using Amazon DynamoDB with provisioned throughput for the database tier of its ecommerce website. During flash sales, customers experience periods of time when the database cannot handle the high number of transactions taking place. This causes the company to lose transactions. During normal periods, the database performs appropriately. Which solution solves the performance problem the company faces?

<details><summary>Answer</summary>

**A. Switch DynamoDB to on-demand mode during flash sales.**

</details>

### 269. dt-745 `availability`

A company is building a payment application that must be highly available even during regional service disruptions. A solutions architect must design a data storage solution that can be easily replicated and used in other AWS Regions. The application also requires low-latency atomicity, consistency, isolation, and durability (ACID) transactions that need to be immediately available to generate reports. The development team also needs to use SQL. Which data storage solution meets these requirements?

<details><summary>Answer</summary>

**A. Amazon Aurora Global Database**

</details>

### 270. dt-749

A company has a custom application with embedded credentials that retrieves information from an Amazon RDS MySQL DB instance. Management says the application must be made more secure with the least amount of programming effort. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Create credentials on the RDS for MySQL database for the application user and store the credentials in AWS Secrets Manager. Configure the application to load the database credentials from Secrets Manager. Set up a credentials rotation schedule for the application user in the RDS for MySQL database using Secrets Manager.**

</details>

### 271. dt-750

A company's order fulfillment service uses a MySQL database. The database needs to support a large number of concurrent queries and transactions. Developers are spending time patching and tuning the database. This is causing delays in releasing new product features. The company wants to use cloud-based services to help address this new challenge. The solution must allow the developers to migrate the database with little or no code changes and must optimize performance. Which service should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**A. Amazon Aurora**

</details>

### 272. dt-752

A company is running an online transaction processing (OLTP) workload on AWS. This workload uses an unencrypted Amazon RDS DB instance in a Multi-AZ deployment. Daily database snapshots are taken from this instance. What should a solutions architect do to ensure the database and snapshots are always encrypted moving forward?

<details><summary>Answer</summary>

**A. Encrypt a copy of the latest DB snapshot. Replace the existing DB instance by restoring the encrypted snapshot.**

</details>

### 273. dt-753 `availability`

A company is setting up an application to use an Amazon RDS MySQL DB instance. The database must be architected for high availability across Availability Zones and AWS Regions with minimal downtime. How should a solutions architect meet this requirement?

<details><summary>Answer</summary>

**B. Set up an RDS MySQL Multi-AZ DB instance. Configure a read replica in a different Region.**

</details>

### 274. dt-762

An application uses an Amazon RDS MySQL DB instance. The RDS database is becoming low on disk space. A solutions architect wants to increase the disk space without downtime. Which solution meets these requirements with the LEAST amount of effort?

<details><summary>Answer</summary>

**A. Enable storage auto scaling in RDS.**

</details>

### 275. ce-763

A company is creating a prototype of an ecommerce website on AWS. The website consists of an Application Load Balancer, an Auto Scaling group of Amazon EC2 instances for web servers, and an Amazon RDS for MySQL DB instance that runs with a Single-AZ configuration. The website is slow to respond during searches of the product catalog. The product catalog is a group of tables in the MySQL database that the company does not update frequently. A solutions architect has determined that CPU utilization on the DB instance is high when product catalog searches occur. What should the solutions architect recommend to improve the performance of the website during searches of the product catalog?

<details><summary>Answer</summary>

**B. Implement an Amazon ElastiCache for Redis OSS cluster to cache the product catalog. Use lazy loading to populate the cache.**

The core issue is high CPU utilization on the RDS database caused by frequent read queries for the product catalog, which is static data. Implementing an in-memory cache like Amazon ElastiCache is the standard architectural pattern to solve this problem. By caching the product catalog data, subsequent requests are served from the fast, in-memory cache instead of the database. This significantly reduces the read load on the RDS instance, lowers its CPU utilization, and improves the website's search performance. The lazy loading strategy is an efficient method to populate the cache only with data that is actually requested. Why Incorrect Options are Wrong: A. Amazon Redshift is a data warehouse optimized for analytical queries (OLAP), not for low-latency transactional lookups required by a website. C. The bottleneck is the database, not the web servers. Adding more EC2 instances would only

</details>

### 276. dt-764

A company has a website deployed on AWS. The database backend is hosted on Amazon RDS for MySQL with a primary instance and five read replicas to support scaling needs. The read replicas should lag no more than 1 second behind the primary instance to support the user experience. As traffic on the website continues to increase, the replicas are falling further behind during periods of peak load, resulting in complaints from users when searches yield inconsistent results. A solutions architect needs to reduce the replication lag as much as possible, with minimal changes to the application code or operational requirements. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Migrate the database to Amazon Aurora MySQL. Replace the MySQL read replicas with Aurora Replicas and enable Aurora Auto Scaling.**

</details>

### 277. ce-780 `cost`

A company runs its application on Oracle Database Enterprise Edition The company needs to migrate the application and the database to AWS. The company can use the Bring Your Own License (BYOL) model while migrating to AWS The application uses third-party database features that require privileged access. A solutions architect must design a solution for the database migration. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Migrate the database to Amazon RDS Custom for Oracle by using native tools Customize the new database settings to support the third-party features.**

The core requirements are to migrate an Oracle database using a Bring Your Own License (BYOL) model and to support third-party features that need privileged access. Amazon RDS Custom for Oracle is specifically designed for this use case. It provides the managed benefits of RDS while allowing access to the underlying operating system and database environment. This elevated access is necessary to install third-party agents or make customizations that are not possible in standard Amazon RDS. RDS Custom for Oracle exclusively uses the BYOL model, directly meeting another key requirement. This approach avoids the high cost and effort of refactoring the application or changing the database engine, making it the most cost-effective solution. Why Incorrect Options are Wrong: A. Standard Amazon RDS for Oracle does not grant privileged access (OS-level or SYSDBA) required for deep customizations o

</details>

### 278. ce-792 `cost`

A company is developing a new application that uses a relational database to store user data and application configurations. The company expects the application to have steady user growth. The company expects the database usage to be variable and read-heavy, with occasional writes. The company wants to cost-optimize the database solution. The company wants to use an AWS managed database solution that will provide the necessary performance. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Deploy the database on Amazon Aurora Serveriess to automatically scale the database capacity based on actual usage to accommodate the workload.**

Amazon Aurora Serverless is the most cost-effective solution for this scenario. It is a managed relational database service designed specifically for variable and unpredictable workloads. It automatically scales compute and memory capacity up or down based on actual usage, and can even scale down to zero during periods of inactivity, significantly optimizing costs. This pay-per-use model perfectly aligns with the requirements of a new application with variable, read-heavy usage and steady growth, while ensuring the necessary performance is available on demand. Why Incorrect Options are Wrong: A. Provisioned IOPS SSD storage is the most expensive storage option, designed for sustained high-throughput workloads, not variable ones. This choice is contrary to the cost-optimization requirement. C. Amazon DynamoDB is a NoSQL database. The question explicitly requires a relational database solu

</details>

### 279. ce-795 `cost`

A company uses Amazon RDS (or PostgreSQL to run its applications in the us-east-1 Region. The company also uses machine learning (ML) models to forecast annual revenue based on neat real- time reports. The reports are generated by using the same RDS for PostgreSQL database. The database performance slows during business hours. The company needs to improve database performance. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Create a read replica in us-east-1. Configure the reports to be generated from the read replica.**

The core issue is performance degradation on the primary RDS database due to heavy read operations from reporting and ML workloads. The most effective and standard AWS solution for scaling read-intensive workloads on an RDS database is to create a read replica. A read replica is an asynchronously replicated, read-only copy of the primary database. By directing the reporting queries to this replica, the read load is isolated from the primary instance, which can then dedicate its resources to the main application's transactions, thus improving its performance. Creating the replica in the same region (us-east-1) is the most cost-effective option as it minimizes data transfer costs and network latency compared to a cross-Region solution. Why Incorrect Options are Wrong: A. A cross-Region read replica solves the read-scaling problem but incurs higher data transfer costs and network latency th

</details>

### 280. ce-820 `cost`

A company launches a new web application that uses an Amazon Aurora PostgreSQL database. The company wants to add new features to the application that rely on AI. The company requires vector storage capability to use AI tools. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**D. Install the pgvector extension on the Aurora PostgreSQL database. Configure the application to write vector embeddings to a vector table.**

The company already operates an Amazon Aurora PostgreSQL database. The most cost-effective solution is to leverage this existing infrastructure. The pgvector extension can be installed directly on the Aurora PostgreSQL database, enabling it to store, index, and query vector embeddings. This approach avoids the significant cost and operational overhead associated with provisioning, managing, and integrating a separate, dedicated service like Amazon OpenSearch Service, Amazon DocumentDB, or Amazon Neptune. By enhancing the current database, the company minimizes new expenses and architectural complexity while meeting the AI feature requirements. Why Incorrect Options are Wrong: A. Using OpenSearch Service requires provisioning a new, separate cluster, which is less cost-effective than extending the existing database. B. Using Amazon DocumentDB requires provisioning a new database cluster,

</details>

### 281. ce-831 `cost`

A company is building an ecommerce application that uses a relational database to store customer data and order history. The company also needs a solution to store 100 GB of product images. The company expects the traffic flow for the application to be predictable. Which solution will meet these requirements MOST cost-effectively? Options:

<details><summary>Answer</summary>

**A. Use Amazon RDS for MySQL for the database. Store the product images in an Amazon S3 bucket.**

This solution correctly aligns the appropriate AWS service with each specific requirement in the most cost-effective manner. Amazon RDS for MySQL is a managed relational database service, perfectly suited for storing structured ecommerce data like customer profiles and order history. Amazon S3 is the ideal service for storing unstructured data, such as product images. S3 provides highly durable, scalable, and low-cost object storage, which is significantly more cost-effective and performant for static assets than storing them in a relational database. This combination represents a standard, well-architected pattern for web applications. Why Incorrect Options are Wrong: B: Amazon DynamoDB is a NoSQL database. The requirement explicitly calls for a relational database to handle customer and order data, which typically involves complex relationships. C: Storing large binary objects like ima

</details>

### 282. ce-840 `cost`

A company is planning to deploy a managed MySQL database solution for its non-production applications. The company plans to run the system for several years on AWS. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create an Amazon RDS for MySQL instance. Purchase a Reserved Instance.**

The question requires the MOST cost-effective managed MySQL solution for a workload lasting several years. Amazon RDS is a managed database service. For a predictable, long-term workload, purchasing a Reserved Instance (RI) provides a significant discount (up to 72%) compared to On-Demand pricing. This combination directly fulfills the requirements for a managed service with the lowest long-term cost. The steady, multi-year nature of the workload makes it an ideal candidate for the commitment-based savings offered by Reserved Instances. Why Incorrect Options are Wrong: B. On-Demand pricing is flexible but is the most expensive option for a predictable, multi-year workload. It does not meet the "MOST cost-effectively" requirement. C. Amazon Aurora is a premium, high-performance service, generally more expensive than standard RDS for MySQL. Using it on-demand is not the most cost-effective

</details>

### 283. ce-851 `cost`

A company is developing software that uses a PostgreSQL database schem a. The company needs to configure development environments and test environments for its developers. Each developer at the company uses their own development environment, which includes a PostgreSQL database. On average, each development environment is used for an 8-hour workday. The test environments will be used for load testing that can take up to 2 hours each day. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Configure development environments and test environments with their own Amazon Aurora Serverless v2 PostgreSQL database.**

The workloads described-development environments used for 8 hours and test environments used for 2 hours-are intermittent and unpredictable. Amazon Aurora Serverless v2 is specifically designed for such use cases. It automatically scales database capacity up and down based on application demand and can scale down to a minimal footprint when idle. This model ensures that the company pays only for the capacity consumed during active use, making it the most cost-effective solution for environments that are inactive for significant portions of the day (16-22 hours). Why Incorrect Options are Wrong: B. Provisioned Amazon RDS instances are billed continuously, regardless of usage. This is not cost-effective for workloads that are idle for most of the day. Multi-AZ is unnecessary for this test environment. C. A standard provisioned Amazon Aurora cluster, like RDS, incurs costs 24/7 for the unde

</details>

### 284. ce-852

A company runs an application on Microsoft SQL Server databases in an on-premises data center. The company wants to migrate to AWS and optimize costs for its infrastructure on AWS. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate to Amazon Aurora PostgreSQL by using Babelfish for Aurora PostgreSQL.**

The primary requirement is to migrate a Microsoft SQL Server database to AWS while optimizing costs. Babelfish for Aurora PostgreSQL is a capability of Amazon Aurora PostgreSQL-Compatible Edition that allows it to understand the SQL Server wire protocol (TDS) and T-SQL dialect. This enables migration from SQL Server to the cost-effective, open-source-compatible Aurora PostgreSQL engine with minimal to no application code changes. By moving away from the commercial SQL Server engine, the company eliminates expensive licensing fees, which is the most significant factor in cost optimization for this scenario. Aurora's managed nature also reduces operational overhead compared to self-managed solutions. Why Incorrect Options are Wrong: A. Migrating to SQL Server on EC2 still requires paying for Microsoft SQL Server licenses and adds the operational burden of managing the instance, making it l

</details>

### 285. ce-867

A company uses an Amazon RDS MySQL database to store data for several applications. The company wants to understand use patterns for the database so the company can identify oppor-tunities to optimize costs. A solutions architect needs to analyze the RDS DB instance to identify right-sizing opportuni-ties. Which solution will meet these requirements with the LEAST effort?

<details><summary>Answer</summary>

**B. Enable Performance Insights for the RDS DB instance. Right-size the RDS DB instance based on the maximum CPU utilization.**

Amazon RDS Performance Insights is a database performance tuning and monitoring feature specifically designed to help users assess the load on their database. It provides a visual dashboard that helps identify the most resource-intensive SQL queries and other factors contributing to the database load, such as CPU utilization. By enabling Performance Insights, a solutions architect can easily visualize the database's performance profile, including peak and average CPU usage, over time. This data is crucial for making informed right-sizing decisions to optimize costs by selecting an instance type that matches the actual workload, thereby meeting the requirements with the least possible effort. Why Incorrect Options are Wrong: A. AWS CloudTrail logs API calls to the AWS environment, not internal database transactions. It is the wrong tool for analyzing database workload for right-sizing pur

</details>

### 286. ce-881

A company runs an ecommerce application on premises on Microsoft SQL Server. The company is planning to migrate the application to the AWS Cloud. The application code contains complex T-SQL queries and stored procedures. The company wants to minimize database server maintenance and operating costs after the migration is completed. The company also wants to minimize the need to rewrite code as part of the migration effort. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Migrate the database to Amazon Aurora PostgreSQL. Turn on Babelfish.**

Babelfish for Amazon Aurora PostgreSQL is a translation layer that enables Aurora PostgreSQL to understand T-SQL, the dialect used by Microsoft SQL Server. This allows the company to migrate its application, including complex queries and stored procedures, with minimal to no code changes. Amazon Aurora is a fully managed database service, which significantly reduces maintenance and operational tasks compared to self-managed or even standard RDS instances. This combination directly addresses the requirements for minimal code rewrite, maintenance, and cost. Why Incorrect Options are Wrong: B. Amazon S3 and Redshift Spectrum are used for data lakes and analytics, not for running a transactional ecommerce application built on SQL Server. C. Amazon RDS for SQL Server maintains compatibility but typically has higher licensing costs and operational overhead compared to the serverless, cloud-nat

</details>

### 287. ce-912 `cost`

A company runs a web application on Amazon EC2 instances behind an Application Load Balancer ALB. The application uses Amazon DynamoDB as its database. The company wants to ensure high performance for reads and writes. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**A. Configure automatic scaling for the DynamoDB table. Set a target utilization of 70%. Set the minimum and maximum capacity units based on the expected workload.**

DynamoDB auto scaling is the most cost-effective solution for managing variable workloads while maintaining high performance. It automatically adjusts the provisioned read and write capacity units in response to actual traffic, preventing performance degradation from throttling. By setting a target utilization (e.g., 70%), it proactively scales capacity before requests are throttled. This approach avoids both under-provisioning (which hurts performance) and over-provisioning (which increases costs), making it the most balanced and cost-effective option for the described scenario. Why Incorrect Options are Wrong: B. A Global Secondary Index (GSI) is used to speed up queries on non-key attributes, not for general read/write performance, and it adds cost. C. This custom solution is reactive, scaling only after ThrottledRequests occur, which means performance has already been impacted. D. Dy

</details>

### 288. ce-917 `cost`

A company uses an Amazon RDS for MySQL database with provisioned IOPS in a Multi-AZ deployment. The company recently migrated the database to Amazon DynamoDB tables successfully. However, the company needs to retain the RDS for MySQL database for several months for occasional post-migration testing and debugging. The company took a snapshot of the RDS database immediately after the migration. The RDS database must be available to query within 10 minutes when needed. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**A. Use the stop-db-cluster AWS CLI command and the stop-db-instance CLI command to stop the RDS database. Restart the database as needed by using CLI commands.**

The most cost-effective solution for an RDS database that is needed only occasionally is to stop it. When an RDS DB instance is stopped, AWS does not charge for DB instance hours, only for provisioned storage, manual snapshots, and automated backup storage. The instance can be started again within minutes when needed, which satisfies the 10-minute availability requirement. This approach directly addresses the need to minimize costs for a rarely used resource by eliminating the primary cost driver (compute hours) while retaining the data and configuration for quick reactivation. Why Incorrect Options are Wrong: B. You cannot attach EBS volumes to an RDS database in this manner; RDS manages its own storage. This option is technically infeasible. C. Restoring from a snapshot into a new Single-AZ instance still incurs 24/7 compute costs, making it more expensive than stopping the instance. D

</details>

### 289. ce-933 `cost`

A financial services company needs to store and manage trading documentation. The documentation includes real-time trade confirmation data, financial statements, and settlement documents that frequently exceed 1 MB in size. The company's current provisioned database solution stores and manages this documentation. This current solution experiences high-volume trading activity during market hours but very low activity during off-hours. The company currently uses a provisioned database solution that is sized to handle the load for peak trading hours. This solution results in significant unused capacity during off-hours. The company needs a solution that will maintain performance during peak hours. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Deploy Amazon DocumentDB serverless with automatic capacity scaling.**

The scenario describes a spiky workload with high activity during market hours and low activity otherwise. Amazon DocumentDB serverless is specifically designed for such variable and unpredictable workloads. It automatically and instantly scales compute and memory capacity based on application needs, ensuring performance during peak hours. During off-hours, it scales down, and the company pays only for the resources consumed. DocumentDB also supports document sizes up to 16 MB, which satisfies the requirement for storing documents larger than 1 MB, making it the most cost-effective and performant solution. Why Incorrect Options are Wrong: A. RDS Reserved Instances are cost-effective for constant, predictable usage, not for spiky workloads. Relational databases are also suboptimal for storing large documents. C. Amazon DynamoDB has a maximum item size limit of 400 KB, which is insufficien

</details>

### 290. ce-939 `cost`

A company is designing a new web application that will run on Amazon EC2 instances. The application will use Amazon DynamoDB for backend data storage. The application traffic will be unpredictable. The company expects that the application read and write throughput to the database will be moderate to high. The company needs to scale in response to application traffic. Which DynamoDB table configuration will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure DynamoDB in on-demand mode by using the DynamoDB Standard table class.**

The scenario describes an application with unpredictable traffic patterns and a need for cost-effective scaling. DynamoDB on-demand capacity mode is designed for this exact use case. It automatically adjusts read and write capacity to serve traffic as it comes, and you pay only for the resources consumed. This eliminates the need for capacity planning and avoids costs associated with overprovisioning, making it the most cost-effective solution for unpredictable workloads. The DynamoDB Standard table class is the default and appropriate for frequently accessed data, as described. Why Incorrect Options are Wrong: A. Provisioned capacity with auto scaling is less cost-effective for unpredictable, spiky traffic, as it can be slower to react and may lead to throttling or overprovisioning. C. The DynamoDB Standard-IA table class is optimized for data that is infrequently accessed, which is not

</details>

### 291. ce-947

A company wants to run a production database in the AWS Cloud. The database will collect billions of sensor readings from multiple locations across multiple AWS Regions. Data is written to the database at a sustained rate of 50,000 writes per second. The company will run reports once every 3 months against the database. The company will run simple queries to retrieve data based on unique location IDs to run the reports. The query results will vary in size. The company needs a solution that will optimize data storage costs. The solution must be highly durable and must not compromise database performance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon DynamoDB Standard-Infrequent Access tables in multiple Regions. Configure DynamoDB to manage capacity.**

The scenario describes a high-throughput, write-heavy workload (50,000 writes/second) with infrequent reads (once every 3 months). The primary requirements are to optimize storage costs while maintaining high performance and durability. Amazon DynamoDB is the ideal service for this key-value workload at scale. The DynamoDB Standard-Infrequent Access (Standard-IA) table class is specifically designed for this use case, offering lower storage costs for data that is accessed infrequently. This directly addresses the core requirement to optimize storage costs. By configuring DynamoDB to manage capacity (using on-demand mode), the database can automatically scale to handle the high, sustained write traffic without performance degradation or manual intervention. Why Incorrect Options are Wrong: A. Amazon Aurora is a relational database, which is not optimal for this high-volume, key-value work

</details>

### 292. ce-948 `least-ops`

A company runs a monolithic application in its on-premises data center. The company used Java/Tomcat to build the application. The application uses Microsoft SQL Server as a database. The company wants to migrate the application to AWS. Which solution will meet this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS App2Container to containerize the application. Deploy the application on Amazon Elastic Kubernetes Service (Amazon EKS). Deploy the database to Amazon RDS for SQL Server. Configure a Multi-AZ deployment.**

The goal is to migrate a monolithic Java/Tomcat application with a Microsoft SQL Server database to AWS with the least operational overhead. Option A proposes a re-platforming strategy using managed services. AWS App2Container helps modernize the existing Java application into a container. Deploying this container on Amazon Elastic Kubernetes Service (Amazon EKS) leverages a managed container orchestration service, reducing the burden of managing a Kubernetes cluster. Using Amazon RDS for SQL Server with a Multi-AZ deployment provides a fully managed, highly available relational database service. This combination directly migrates the existing technology stack while offloading the maximum amount of infrastructure management to AWS, thus meeting the "least operational overhead" requirement. Why Incorrect Options are Wrong: B: This option involves self-managing both the Kubernetes cluster

</details>

### 293. ce-962

A solutions architect needs to save a particular automated database snapshot from an Amazon RDS for Microsoft SQL Server DB instance for longer than the maximum number of days. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**A. Create a manual copy of the snapshot.**

Automated Amazon RDS snapshots are deleted at the end of their configured retention period (maximum of 35 days). To retain a specific snapshot for a longer period, the most operationally efficient method is to create a copy of it. The copied snapshot becomes a manual snapshot, which is not subject to the automated retention policy and persists until it is explicitly deleted by the user. This is a straightforward action performed via the AWS Management Console or a single API call. Why Incorrect Options are Wrong: B. Exporting to Amazon S3 is more complex and is intended for data analysis, not for a standard database restore, making it less operationally efficient for this purpose. C. The maximum retention period for an automated RDS snapshot is 35 days; therefore, changing it to 45 days is not a possible action. D. Creating a native SQL Server backup requires more configuration and manag

</details>
