# Cost optimization

44 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. et-221 `cost`

A company runs an application on a group of Amazon Linux EC2 instances. For compliance reasons, the company must retain all application log files for 7 years. The log files will be analyzed by a reporting tool that must be able to access all the files concurrently. Which storage solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Amazon S3**

S3 is a highly durable and scalable object storage service. It is designed for high availability and can store large amounts of data. S3 is cost-effective for long-term storage, and its pricing is based on the amount of data stored.

</details>

### 2. et-238 `cost`

A company wants to experiment with individual AWS accounts for its engineer team. The company wants to be notified as soon as the Amazon EC2 instance usage for a given month exceeds a specific threshold for each account. What should a solutions architect do to meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use AWS Budgets to create a cost budget for each account. Set the period to monthly. Set the scope to EC2 instances. Set an alert threshold for the budget. Configure an Amazon Simple Notification Service (Amazon SNS) topic to receive a notification when a threshold is exceeded.**

AWS Budgets is a cost management service that allows you to set custom cost and usage budgets that alert you when you exceed your thresholds. In this case, you can create a monthly budget specifically for EC2 instances, and when the usage exceeds the defined threshold, it triggers an alert.

</details>

### 3. et-262 `cost`

A company plans to use Amazon ElastiCache for its multi-tier web application. A solutions architect creates a Cache VPC for the ElastiCache cluster and an App VPC for the application’s Amazon EC2 instances. Both VPCs are in the us-east-1 Region. The solutions architect must implement a solution to provide the application’s EC2 instances with access to the ElastiCache cluster. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create a peering connection between the VPCs. Add a route table entry for the peering connection in both VPCs. Configure an inbound rule for the ElastiCache cluster’s security group to allow inbound connection from the application’s security group.**

Creating a peering connection allows communication between the Cache VPC and the App VPC.  Adding a route table entry in both VPCs for the peering connection ensures that traffic can flow between them. Inbound Rule in ElastiCache Security Group:  Configuring an inbound rule in the ElastiCache cluster's security group to allow connections from the application's security group enables the EC2 instances in the App VPC to access the ElastiCache cluster.

</details>

### 4. dt-267

When using consolidated billing there are two account types. What are they?

<details><summary>Answer</summary>

**A. Paying account and Linked account.**

</details>

### 5. et-347 `cost`

A company has an application that is running on Amazon EC2 instances. A solutions architect has standardized the company on a particular instance family and various instance sizes based on the current needs of the company. The company wants to maximize cost savings for the application over the next 3 years. The company needs to be able to change the instance family and sizes in the next 6 months based on application popularity and usage. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Compute Savings Plan**

Compute Savings Plans provide significant cost savings over On-Demand pricing in exchange for a commitment to a consistent amount of compute usage (measured in $/hr) for a 1 or 3 year period. They offer flexibility by allowing you to switch between instance families, sizes, and AZs (Availability Zones) while still benefiting from the savings plan pricing. This aligns well with the company's requirement to change instance family and sizes based on application needs.

</details>

### 6. et-348 `cost`

A company collects data from a large number of participants who use wearable devices. The company stores the data in an Amazon DynamoDB table and uses applications to analyze the data. The data workload is constant and predictable. The company wants to stay at or below its forecasted budget for DynamoDB. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use provisioned mode. Specify the read capacity units (RCUs) and write capacity units (WCUs).**

In provisioned mode, you provision a specific amount of read and write capacity, which allows you to manage costs more effectively based on your expected workload. This approach is suitable when your workload is predictable, as you can provision the capacity to meet your known requirements. DynamoDB Standard-Infrequent Access (Option A) is designed for cost savings on long-term storage and retrieval of infrequently accessed data, and it might not be the best fit for a constant and predictable workload.

</details>

### 7. et-383 `cost`

A company is planning to migrate a commercial off-the-shelf application from its on-premises data center to AWS. The software has a software licensing model using sockets and cores with predictable capacity and uptime requirements. The company wants to use its existing licenses, which were purchased earlier this year. Which Amazon EC2 pricing option is the MOST cost-effective?

<details><summary>Answer</summary>

**A. Dedicated Reserved Hosts**

A Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use. When you launch instances on a Dedicated Host, those instances run on the dedicated hardware of that host. Dedicated Hosts provide control over the placement of instances for compliance, licensing, or regulatory requirements. You can purchase Dedicated Hosts on a reservation model (Reserved Hosts) or pay for them on-demand. The host remains dedicated to you for the specified term in the case of Reserved Hosts. Dedicated Hosts can be useful for workloads with specific licensing models tied to physical sockets or cores.

</details>

### 8. dt-387 `cost`

Which of the following approaches provides the lowest cost for Amazon Elastic Block Store snapshots while giving you the ability to fully restore data?

<details><summary>Answer</summary>

**A. Maintain two snapshots: the original snapshot and the latest incremental snapshot.**

</details>

### 9. et-398 `cost`

A company needs to transfer 600 TB of data from its on-premises network-attached storage (NAS) system to the AWS Cloud. The data transfer must be complete within 2 weeks. The data is sensitive and must be encrypted in transit. The company’s internet connection can support an upload speed of 100 Mbps. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use the AWS Snow Family console to order several AWS Snowball Edge Storage Optimized devices. Use the devices to transfer the data to Amazon S3.**

Transferring 600 TB of data over a 100 Mbps connection would take a very long time. AWS Snowball Edge devices allow for offline data transfer, and you can transfer the data to the devices at your location before shipping them to AWS. This way, you are not constrained by the upload speed during the 2-week period.

</details>

### 10. dt-439

Your manager has come to you saying that he is very confused about the bills he is receiving from AWS as he is getting different bills for every user and needs you to look into making it more understandable. Which of the following would be the best solution to meet his request?

<details><summary>Answer</summary>

**B. Consolidated Billing.**

</details>

### 11. dt-441

If I scale the storage capacity provisioned to my DB Instance by mid of a billing month, how will I be charged?

<details><summary>Answer</summary>

**B. On a proration basis.**

</details>

### 12. et-455

A company uses AWS Organizations. The company wants to operate some of its AWS accounts with different budgets. The company wants to receive alerts and automatically prevent provisioning of additional resources on AWS accounts when the allocated budget threshold is met during a specific period. Which combination of solutions will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**B. Use AWS Budgets to create a budget. Set the budget amount under the Billing dashboards of the required AWS accounts.**

D. Create an IAM role for AWS Budgets to run budget actions with the required permissions.  F. Add an alert to notify the company when each account meets its budget threshold. Add a budget action that selects the IAM identity created with the appropriate service control policy (SCP) to prevent provisioning of additional resources.

</details>

### 13. et-456 `cost`

A company runs applications on Amazon EC2 instances in one AWS Region. The company wants to back up the EC2 instances to a second Region. The company also wants to provision EC2 resources in the second Region and manage the EC2 instances centrally from one AWS account. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a backup plan by using AWS Backup. Configure cross-Region backup to the second Region for the EC2 instances.**

AWS Backup is a centralized backup service that allows you to create backup plans for various AWS resources, including EC2 instances. With AWS Backup, you can configure cross-Region backups, meaning you can replicate backups from one AWS Region to another. This provides a cost-effective and centralized solution for backup.

</details>

### 14. et-467

A company uses AWS Organizations. A member account has purchased a Compute Savings Plan. Because of changes in the workloads inside the member account, the account no longer receives the full benefit of the Compute Savings Plan commitment. The company uses less than 50% of its purchased compute power.

<details><summary>Answer</summary>

**B. Turn on discount sharing from the Billing Preferences section of the account console in the company's Organizations management account.**

</details>

### 15. et-525 `least-ops`

A company wants to add its existing AWS usage cost to its operation cost dashboard. A solutions architect needs to recommend a solution that will give the company access to its usage cost programmatically. The company must be able to access cost data for the current year and forecast costs for the next 12 months. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Access usage cost-related data by using the AWS Cost Explorer API with pagination.**

AWS Cost Explorer is a tool provided by Amazon Web Services (AWS) that allows users to visualize, understand, and manage their AWS costs and usage.

</details>

### 16. ce-537 `cost`

A manufacturing company develops an application to give a small team of executives the ability to track sales performance globally. The application provides a real-time simulator in a popular programming language. The company uses AWS Lambda functions to support the simulator. The simulator is an algorithm that predicts sales performance based on specific variables. Although the solution works well initially, the company notices that the time required to complete simulations is increasing exponentially. A solutions architect needs to improve the response time of the simulator. Which solution will meet this requirement in the MOST cost-effective way?

<details><summary>Answer</summary>

**D. Use Lambda provisioned concurrency for the simulator functions.**

The problem describes increasing simulation completion times for an AWS Lambda-based application, which is a classic symptom of "cold start" latency. When a Lambda function is invoked after a period of inactivity, AWS must initialize a new execution environment, which adds latency. Provisioned Concurrency is a feature designed specifically to solve this problem by keeping a specified number of function instances initialized and ready to respond immediately. This directly reduces latency for performance-sensitive applications in the most cost-effective manner by optimizing the existing serverless architecture, rather than re-architecting to a more expensive, constantly running model. Why Incorrect Options are Wrong: A. Use AWS Fargate to run the simulator. Serve requests through an Application Load Balancer (ALB). This is a viable but more expensive solution. Fargate tasks run continuousl

</details>

### 17. et-541 `cost`

A company wants to build a web application on AWS. Client access requests to the website are not predictable and can be idle for a long time. Only customers who have paid a subscription fee can have the ability to sign in and use the web application. Which combination of steps will meet these requirements MOST cost-effectively? (Choose three.)

<details><summary>Answer</summary>

**A. Create an AWS Lambda function to retrieve user information from Amazon DynamoDB. Create an Amazon API Gateway endpoint to accept RESTful APIs. Send the API calls to the Lambda function.**

C. Create an Amazon Cognito user pool to authenticate users.  E. Use AWS Amplify to serve the frontend web content with HTML, CSS, and JS. Use an integrated Amazon CloudFront configuration.  AWS Lambda is a serverless computing service, and its pay-per-use pricing model can be cost-effective for sporadic and unpredictable workloads. DynamoDB is a NoSQL database that can scale with demand.  Amazon Cognito provides a scalable and secure user directory for your web application. It allows you to manage user identities and authentication in a cost-effective manner. User pools can be used to handle user registration, authentication, and account recovery.  AWS Amplify simplifies the development of scalable and secure cloud-powered web and mobile apps. CloudFront is a content delivery network (CDN) that can efficiently distribute your web content globally, improving performance.

</details>

### 18. et-551 `cost`

A company has a financial application that produces reports. The reports average 50 KB in size and are stored in Amazon S3. The reports are frequently accessed during the first week after production and must be stored for several years. The reports must be retrievable within 6 hours. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Use S3 Standard. Use an S3 Lifecycle rule to transition the reports to S3 Glacier after 7 days.**

After the initial period, using an S3 Lifecycle rule to transition the reports to the S3 Glacier storage class is a cost-effective approach. Glacier is designed for long-term archival storage with lower storage costs compared to S3 Standard.

</details>

### 19. et-573 `cost`

A company wants to use an event-driven programming model with AWS Lambda. The company wants to reduce startup latency for Lambda functions that run on Java 11. The company does not have strict latency requirements for the applications. The company wants to reduce cold starts and outlier latencies when a function scales up. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Configure Lambda SnapStart.**

Lambda Cold Start: When a Lambda function is invoked, it may take a bit of time for the system to set up everything needed to run the function. This initial setup time is called a "cold start." Cold starts can add some delay, especially if the function hasn't been used recently. Lambda SnapStart: SnapStart is a feature in AWS Lambda designed to make these cold starts faster, specifically for functions written in Java. Instead of starting from scratch every time a function is called, SnapStart pre-warms the environment. It's like getting things ready in advance so that when your function is called, it can start quickly without much delay.

</details>

### 20. et-598 `cost`

A research company uses on-premises devices to generate data for analysis. The company wants to use the AWS Cloud to analyze the data. The devices generate .csv files and support writing the data to an SMB file share. Company analysts must be able to use SQL commands to query the data. The analysts will run queries periodically throughout the day. Which combination of steps will meet these requirements MOST cost-effectively? (Choose three.)

<details><summary>Answer</summary>

**A. Deploy an AWS Storage Gateway on premises in Amazon S3 File Gateway mode.**

C. Set up an AWS Glue crawler to create a table based on the data that is in Amazon S3.  F. Setup Amazon Athena to query the data that is in Amazon S3. Provide access to analysts.  This step allows you to seamlessly integrate on-premises devices with AWS S3, providing a scalable and cost-effective storage solution. The AWS Storage Gateway in S3 File Gateway mode enables you to write data from on-premises devices to S3.  AWS Glue can discover, catalog, and transform data from S3. By setting up a Glue crawler, you create a table schema based on the .csv files in S3. This step prepares the data for analysis.  Amazon Athena allows you to run SQL queries directly on the data stored in S3 without the need for a dedicated database. You can create databases and tables in Athena based on the cataloged data using Glue.

</details>

### 21. ce-615 `cost`

A company is developing a latency-sensitive application. Part of the application includes several AWS Lambda functions that need to initialize as quickly as possible. The Lambda functions are written in Java and contain initialization code outside the handlers to load libraries, initialize classes, and generate unique IDs. Which solution will meet the startup performance requirement MOST cost-effectively?

<details><summary>Answer</summary>

**D. Update the Lambda functions to add a pre-snapshot hook. Move the code that generates unique IDs into the handlers. Publish a version of each Lambda function. Activate Lambda SnapStart for the published versions of the Lambda functions.**

The question seeks the most cost-effective solution to reduce startup latency for Java-based AWS Lambda functions. Lambda SnapStart is a feature designed specifically for this purpose. It improves startup performance by creating a snapshot of the initialized execution environment and caching it for reuse. This service is available at no additional cost, making it the most cost-effective option. However, a critical consideration with SnapStart is ensuring the uniqueness of state across invocations. Since the snapshot captures the state of the initialized environment, any unique IDs generated during the initialization phase (outside the handler) would be identical for all functions restored from that snapshot. The correct approach is to move the code that requires uniqueness, such as generating unique IDs, into the function handler. This ensures a new ID is generated for each invocation. S

</details>

### 22. et-641

A company wants to monitor its AWS costs for financial review. The cloud operations team is designing an architecture in the AWS Organizations management account to query AWS Cost and Usage Reports for all member accounts. The team must run this query once a month and provide a detailed analysis of the bill. Which solution is the MOST scalable and cost-effective way to meet these requirements?

<details><summary>Answer</summary>

**B. Enable Cost and Usage Reports in the management account. Deliver the reports to Amazon S3 Use Amazon Athena for analysis.**

Amazon Athena is a serverless query service that allows you to analyze data directly in Amazon S3 using SQL queries.

</details>

### 23. et-656 `cost` `availability`

A company runs a website that stores images of historical events. Website users need the ability to search and view images based on the year that the event in the image occurred. On average, users request each image only once or twice a year. The company wants a highly available solution to store and deliver the images to users. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Store images in Amazon S3 Standard. Use S3 Standard to directly deliver images by using a static website.**

Standard-IA is cost-effective for rarely accessed images. Static websites simplify delivery. EBS/EFS (Options A/B) are expensive and lack S3’s durability.

</details>

### 24. dt-671 `cost`

A company runs an application on Amazon EC2 instances in a private subnet. The application needs to store and retrieve data in Amazon S3 buckets. According to regulatory requirements, the data must not travel across the public internet. What should a solutions architect do to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Deploy an S3 gateway endpoint to access the S3 buckets.**

</details>

### 25. et-671

A company runs its applications on Amazon EC2 instances. The company performs periodic financial assessments of its AWS costs. The company recently identified unusual spending. The company needs a solution to prevent unusual spending. The solution must monitor costs and notify responsible stakeholders in the event of unusual spending. Which solution will meet these requirements?

<details><summary>Answer</summary>

**Create an AWS Cost Anomaly Detection monitor.**

Cost Anomaly Detection applies machine learning to your AWS cost and usage data and raises an alert when spend departs from the learned pattern, naming the service, linked account, cost category or tag the unexpected charges came from. Alerts go to email or to an Amazon SNS topic, either one at a time or as a daily or weekly summary, so the responsible stakeholders hear about it without anyone running a manual review. CloudWatch can also detect anomalies in a metric, but the only billing data it holds is the coarse EstimatedCharges metric in us-east-1, so it cannot break spend down by service or account; AWS Budgets is useful alongside this but fires on thresholds you set yourself rather than on unusual patterns.

</details>

### 26. dt-705 `cost`

A solutions architect is designing an application that will allow business users to upload objects to Amazon S3. The solution needs to maximize object durability. Objects also must be readily available at any time and for any length of time. Users will access objects frequently within the first 30 days after the objects are uploaded, but users are much less likely to access objects that are older than 30 days. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.**

</details>

### 27. dt-719 `cost`

A company has a well-architected application that streams audio data by using UDP in the AWS Cloud. The company hosts the application in the eu-central-1 Region. The company plans to offer services to North American users. A solutions architect must improve application network performance for the North American users. Which of the following is the MOST cost-effective solution?

<details><summary>Answer</summary>

**A. Create an AWS Global Accelerator standard accelerator with an endpoint group in eu-central-1.**

</details>

### 28. ce-777 `cost`

A company needs a secure connection between its on-premises environment and AWS. This connection does not need high bandwidth and will handle a small amount of traffic. The connection should be set up quickly. What is the MOST cost-effective method to establish this type of connection?

<details><summary>Answer</summary>

**D. Implement an AWS Site-to-Site VPN connection.**

An AWS Site-to-Site VPN establishes a secure, IPsec-encrypted tunnel between an on-premises network and an AWS Virtual Private Cloud (VPC) over the public internet. This solution is ideal for the described scenario because it can be configured rapidly, often within minutes or hours. It is also highly cost-effective for use cases with low to modest bandwidth requirements and small amounts of traffic, as pricing is based on connection hours and data transfer, avoiding the higher fixed costs of a dedicated connection. Why Incorrect Options are Wrong: A. A client VPN is designed to connect individual users or devices to a network, not for connecting an entire on-premises environment to an AWS VPC. B. AWS Direct Connect provides a dedicated, private network connection. It is more expensive, takes weeks or months to provision, and is designed for high-bandwidth, consistent performance needs. C

</details>

### 29. ce-787 `cost`

A company is migrating its databases to Amazon RDS for PostgreSQL. The company is migrating its applications to Amazon EC2 instances. The company wants to optimize costs for long-running workloads. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**D. Purchase Reserved Instances for a 3 year term with the All Upfront option for the Amazon RDS for PostgreSQL workloads. Purchase a 3 year EC2 Instance Savings Plan with the All Upfront option for the EC2 instances.**

For long-running and predictable workloads, commitment-based pricing models provide the most significant discounts compared to On-Demand pricing. The highest level of savings is achieved by committing to the longest term (3 years) and paying the most upfront (All Upfront). Amazon RDS Reserved Instances and EC2 Savings Plans both offer these options. By selecting a 3-year, All Upfront plan for both the RDS database and the EC2 instances, the company maximizes its discounts, resulting in the most cost-effective solution for its stable, long-term usage pattern. Why Incorrect Options are Wrong: A. Using On-Demand Instances for a long-running RDS workload is the most expensive pricing model and is not cost-effective. B. A 1-year term with the No Upfront option provides the lowest discount among all commitment-based pricing options for both RDS and EC2. C. While a 1-year Partial Upfront plan o

</details>

### 30. ce-789 `cost`

A company runs several websites on AWS for its different brands Each website generates tens of gigabytes of web traffic logs each day. A solutions architect needs to design a scalable solution to give the company's developers the ability to analyze traffic patterns across all the company's websites. This analysis by the developers will occur on demand once a week over the course of several months. The solution must support queries with standard SQL. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Store the logs in Amazon S3. Use Amazon Athena for analysis.**

The most cost-effective solution is to use Amazon S3 for storage and Amazon Athena for analysis. Amazon S3 provides highly durable, scalable, and low-cost object storage, which is ideal for large volumes of log data. Amazon Athena is a serverless query service that allows you to run standard SQL queries directly on data in S3. Because the analysis is infrequent (once a week), Athena's pay-per-query pricing model is extremely cost-effective. You only pay for the data scanned by your queries, with no charges for idle time or infrastructure management. This serverless architecture perfectly matches the on-demand and cost-sensitive nature of the requirements. Why Incorrect Options are Wrong: B. Storing logs in Amazon RDS is not cost-effective as it requires provisioning database instances that run continuously, incurring costs even when not in use. It's also not optimal for semi-structured l

</details>

### 31. ce-793 `cost`

A company has a large data workload that runs for 6 hours each day. The company cannot lose any data while the process is running. A solutions architect is designing an Amazon EMR cluster configuration to support this critical data workload. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure a transient cluster that runs the primary node and core nodes on On-Demand Instances and the task nodes on Spot Instances.**

The workload runs for a predictable 6-hour duration daily, making a transient cluster the most cost-effective choice because it is created for the job and terminated upon completion, avoiding idle costs. The requirement to not lose any data is critical. In Amazon EMR, core nodes run the Hadoop Distributed File System (HDFS) and store data. Using On-Demand Instances for the primary and core nodes ensures the cluster's control plane and its data are protected from interruptions. Task nodes only perform computations and do not store data in HDFS. Therefore, using Spot Instances for task nodes is the ideal way to reduce costs significantly without risking data loss, as the termination of a task node only requires the task to be rescheduled. Why Incorrect Options are Wrong: A. A long-running cluster is not cost-effective for a workload that only runs for 6 hours per day, as it would incur cos

</details>

### 32. ce-806 `cost`

A solutions architect needs to optimize a large data analytics job that runs on an Amazon EMR cluster. The job takes 13 hours to finish. The cluster has multiple core nodes and worker nodes deployed on large, compute-optimized instances. After reviewing EMR logs, the solutions architect discovers that several nodes are idle for more than 5 hours while the job is running. The solutions architect needs to optimize cluster performance. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use the EMR managed scaling feature to automatically resize the cluster based on workload.**

The key issue identified is that several EMR nodes are idle for a significant portion of the 13-hour job run. This indicates that the cluster is over-provisioned for long periods, leading to unnecessary costs. EMR managed scaling is the feature designed specifically to address this problem. It automatically resizes the cluster by adding or removing task nodes based on the workload's demand. This ensures that the cluster has the necessary resources during peak processing and scales down during periods of low utilization (idle time), thereby optimizing performance and achieving the most cost-effective operation. Why Incorrect Options are Wrong: A. Increasing core nodes would worsen the problem by adding more static resources that could also become idle, thus increasing costs without addressing the fluctuating workload. C. Migrating a 13-hour EMR job to AWS Lambda is impractical due to Lamb

</details>

### 33. ce-863 `cost`

A company wants a flexible compute solution that includes Amazon EC2 instances and AWS Fargate. The company does not want to commit to multi-year contracts. Which purchasing option will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Purchase a 1-year Compute Savings Plan with the All Upfront option.**

The requirement is for a flexible compute solution covering both Amazon EC2 and AWS Fargate, which must be the most cost-effective option without a multi-year commitment. A Compute Savings Plan is the most suitable choice as it provides flexibility across instance families, regions, and compute services, including EC2 and Fargate. Among the payment options for a 1-year term, the All Upfront option provides the highest discount, making it the most cost-effective choice as requested by the question. Why Incorrect Options are Wrong: A. An EC2 Instance Savings Plan does not apply to AWS Fargate usage, so it fails to meet the requirements of the scenario. B. The No Upfront option provides the lowest discount for a Savings Plan, making it less cost-effective than the Partial or All Upfront options. C. The Partial Upfront option offers a lower discount than the All Upfront option, and therefore

</details>

### 34. ce-868

A company wants to run its experimental workloads in the AWS Cloud. The company has a budget for cloud spending. The company's CFO is concerned about cloud spending accountabil-ity for each department. The CFO wants to receive notification when the spending threshold reaches 60% of the budget. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use cost allocation tags on AWS resources to label owners. Create usage budgets in AWS Budgets. Add an alert threshold to receive notification when spending exceeds 60% of the budget.**

This solution correctly addresses all aspects of the scenario. AWS Cost Allocation Tags are the standard mechanism for categorizing resources by department, project, or any other label, which is essential for cost accountability. AWS Budgets is the specific service designed to set custom spending limits and track costs against them. Within AWS Budgets, you can configure alerts to send notifications via Amazon SNS or email when actual or forecasted costs exceed a defined threshold, such as 60% of the budgeted amount. This combination provides a complete, automated solution for departmental cost management and proactive alerting as requested by the CFO. Why Incorrect Options are Wrong: B: AWS Cost Explorer is used for analyzing cost data, not determining resource owners. AWS Cost Anomaly Detection identifies unexpected spending, not for alerting on predefined budget thresholds. C: While us

</details>

### 35. ce-874 `cost`

A data science team needs storage for nightly log processing. The size and number of logs is unknown, and the logs persist for only 24 hours. What is the MOST cost-effective solution?

<details><summary>Answer</summary>

**B. Amazon S3 Standard**

The most cost-effective solution is Amazon S3 Standard. The logs are processed nightly and deleted after 24 hours, which means they are frequently accessed during their short lifecycle. S3 Standard is designed for frequently accessed data and, crucially, has no minimum storage duration charge. Other storage classes designed for infrequent access or archival impose minimum duration charges (e.g., 30 or 180 days), making them significantly more expensive for data that is deleted daily. S3 Intelligent-Tiering would also be more expensive as it incurs a monitoring fee without providing any benefit, since objects are deleted long before the 30-day period required for automatic tiering. Why Incorrect Options are Wrong: A. Amazon S3 Glacier Deep Archive: This is for long-term archival and has a minimum storage duration charge of 180 days, making it unsuitable and costly for data deleted after o

</details>

### 36. ce-878 `cost`

A data science team requires storage for nightly log processing. The size and number of logs is unknown and the logs will persist for 24 hours only. What is the MOST cost-effective solution?

<details><summary>Answer</summary>

**B. Amazon S3 Standard**

The logs are generated nightly and persist for only 24 hours, indicating a frequent access pattern but a very short storage duration. Amazon S3 Standard is designed for frequently accessed data and has no minimum storage duration charge or retrieval fees. For data stored for only one day, the slightly higher storage rate of S3 Standard is negligible and more cost-effective than paying for 30 days of minimum storage or high monitoring fees associated with other tiers. Why Incorrect Options are Wrong: A. Amazon S3 Glacier Deep Archive is for long-term archival with retrieval times of hours, making it unsuitable for data needed for processing within 24 hours. C. Amazon S3 Intelligent-Tiering incurs a monitoring fee and has a 30-day minimum storage duration for tiering, making it more expensive for short-lived objects. D. Amazon S3 One Zone-IA has a minimum storage duration charge of 30 days

</details>

### 37. ce-880

As part of budget planning, management wants a report of AWS billed items listed by user. The data will be used to create department budgets. A solutions architect needs to determine the most efficient way to obtain this report information. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Create a report in Cost Explorer and download the report.**

AWS Cost Explorer is the most efficient tool for this requirement. It provides a user-friendly interface to visualize, understand, and manage AWS costs and usage over time. A solutions architect can easily use Cost Explorer to filter and group costs by specific tags, such as a "user" or "department" tag, which would have been applied to resources. The resulting view can be saved as a report and downloaded as a CSV file for budget planning. This method is significantly more efficient than writing custom queries or manually parsing detailed billing files, as it is a purpose-built tool for this exact task. Why Incorrect Options are Wrong: A. Using Amazon Athena requires setting up Cost and Usage Report (CUR) delivery to S3 and writing SQL queries, which is less efficient than using the pre-built Cost Explorer interface. C. The main billing dashboard provides a high-level summary of charges

</details>

### 38. ce-883 `cost`

A company runs a container application by using Amazon Elastic Kubernetes Service (Amazon EKS). The application includes microservices that manage customers and place orders. The company needs to route incoming requests to the appropriate microservices. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use the AWS Load Balancer Controller to provision an Application Load Balancer.**

The most cost-effective and appropriate solution is to use an Application Load Balancer (ALB) provisioned by the AWS Load Balancer Controller. An ALB operates at Layer 7 (the application layer) and can inspect incoming requests to perform advanced routing, such as path-based or host-based routing. This allows a single ALB to route traffic to multiple microservices (e.g., /customers to the customer service, /orders to the order service) running in the EKS cluster. This consolidation onto a single load balancer is highly cost-effective compared to provisioning a separate load balancer for each service. Why Incorrect Options are Wrong: A. A Network Load Balancer (NLB) operates at Layer 4 and cannot perform path-based routing, which is required to direct traffic to different microservices based on the URL. C. Using an AWS Lambda function as a proxy adds unnecessary complexity, potential late

</details>

### 39. ce-891 `cost`

A company needs a solution to process customer orders from a global ecommerce platform. The solution must automatically start processing new orders immediately and must maintain a history of all order processing attempts. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**B. Create an Amazon EventBridge event pattern that monitors the ecommerce platform's order events. Configure an EventBridge rule to invoke an AWS Lambda function when the platform receives a new order. Configure the function to store the results in Amazon DynamoDB.**

This solution describes a serverless, event-driven architecture, which is highly cost-effective and efficient. Amazon EventBridge can be configured with an event pattern to listen for new order events from the platform. Upon detecting an event, it immediately invokes an AWS Lambda function to process the order. This meets the "immediately" requirement without paying for idle resources. Using Amazon DynamoDB for storing results provides a scalable, low-cost, and durable history of processing attempts. Why Incorrect Options are Wrong: A. This uses polling (checking every minute) instead of being event-driven, so processing is not immediate. It is also less efficient than a direct trigger. C. Using a dedicated EC2 instance for polling is not cost-effective as it incurs costs 24/7. Polling is also an inefficient pattern that does not meet the "immediately" requirement. D. This option does no

</details>

### 40. ce-894 `cost`

A company deploys a stateful application on Amazon EC2 On-Demand Instances in multiple Availability Zones behind an Application Load Balancer (ALB). The application workload is predictable, and the company has not received any CPU usage alerts. The company expects to run the application for at least 1 year. The company expects CPU usage to increase by 50% during an upcoming 2-week holiday period. The company wants to optimize costs for the application for both the holiday period and normal operations. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**B. Purchase a 12-month EC2 Instance Savings Plan to handle the existing workload. Use On-Demand Instances to handle the additional capacity requirement for the upcoming holiday period.**

This solution provides the best cost optimization. A 12-month EC2 Instance Savings Plan offers significant discounts (up to 72%) over On-Demand prices for the predictable, consistent baseline workload. This commitment aligns with the company's plan to run the application for at least one year. For the temporary, 2-week holiday spike, using On-Demand Instances provides the necessary capacity without any long-term commitment. This combination ensures the baseline is covered at a low cost, while the short-term increase is handled flexibly, avoiding payment for unused capacity during the rest of the year. Why Incorrect Options are Wrong: A. Using only On-Demand Instances is not cost-effective for a predictable, long-term workload, as it forgoes available discounts from Savings Plans or Reserved Instances. C. While Spot Instances are cheaper, they can be interrupted. For a critical holiday pe

</details>

### 41. ce-898 `cost`

A healthcare company needs a storage solution for electronic health records EHRs. The company must store the EHRs for at least 10 years to comply with regulations. The company rarely accesses the records. The records must be secure, immutable, and retrievable within a few hours when needed. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**B. Store the records in Amazon S3 Glacier Flexible Retrieval. Configure S3 Object Lock and set a retention period of 10 years.**

This solution is the most cost-effective and meets all compliance requirements. Amazon S3 Glacier Flexible Retrieval is specifically designed for long-term, low-cost data archiving where data is rarely accessed. It supports retrieval times ranging from minutes to hours, satisfying the "retrievable within a few hours" requirement. S3 Object Lock provides Write-Once-Read-Many (WORM) protection, which makes the records immutable by preventing them from being deleted or overwritten for the duration of the 10-year retention period. This combination directly addresses the need for secure, immutable, long-term, and cost-optimized storage. Why Incorrect Options are Wrong: A. S3 Standard is for frequently accessed data and is not cost-effective for archival. S3 Versioning does not provide true immutability like Object Lock. C. S3 One Zone-IA is not resilient to the loss of an Availability Zone, m

</details>

### 42. ce-931 `cost`

A company needs to run a critical Python data processing job each night. The job runs for approximately 1 hour and must not be interrupted. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Deploy an Amazon EC2 On-Demand Instance that runs Amazon Linux. Migrate the Python script to the EC2 instance. Use a cron job to schedule the script. Create an AWS Lambda function to start and stop the instance once each night.**

The job runs for 1 hour and must not be interrupted. AWS Lambda has a maximum execution time of 15 minutes, and AWS Step Functions Express workflows have a maximum duration of 5 minutes, making them unsuitable. Fargate Spot can be interrupted, which violates a critical requirement. An EC2 On-Demand Instance guarantees uninterrupted execution for the required duration. Automating the start and stop of the instance with a Lambda function ensures that the company only pays for the time the instance is running the job, making it the most cost-effective and reliable solution among the choices. Why Incorrect Options are Wrong: A. Fargate Spot instances can be interrupted with a two-minute warning, which is not suitable for a critical job that must not be interrupted. B. AWS Step Functions Express workflows have a maximum duration of 5 minutes, which is insufficient for a 1-hour job. C. AWS Lam

</details>

### 43. ce-932 `cost`

A company runs compute workloads across multiple private subnets across multiple VPCs. Sometimes the company opens shell access to Amazon EC2 instances in the private subnets to troubleshoot issues. The current design uses NAT gateways. The company wants to reduce costs. However, the company does not support the following: • Using public IP addresses • Installing agents on instances • Permitting inbound internet access Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create an EC2 Instance Connect Endpoint in each VPC. Grant IAM permissions for administrators to connect to instances by using SSH. Decommission all NAT gateways.**

EC2 Instance Connect (EIC) Endpoint allows secure SSH connections to instances in private subnets without requiring public IPs, bastion hosts, or internet gateways. It is agentless for SSH connections and uses IAM policies for granular access control. This solution directly meets all the specified constraints: no public IPs, no agents, and no inbound internet access. By providing a direct connection path, it allows for the decommissioning of NAT gateways if their purpose was to enable connectivity for management, thus meeting the requirement to reduce costs most effectively. Why Incorrect Options are Wrong: B. AWS Systems Manager Session Manager is not suitable because it requires the SSM Agent to be installed on the instances, which violates a stated requirement. C. Bastion hosts require inbound internet access (violating a requirement), and managing them adds operational overhead and c

</details>

### 44. ce-944 `cost`

A company runs its infrastructure on AWS and has a registered base of 700,000 users for its document management application. The company intends to create a product that converts large PDF files to JPG image files. The PDF files average 5 MB in size. The company needs to store the original files and the converted files. A solutions architect must design a scalable solution to accommodate demand that will grow rapidly over time. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Save the PDF files to Amazon S3. Configure an S3 PUT event to invoke an AWS Lambda function to convert the files to JPG format and store them back in Amazon S3.**

This solution represents a classic serverless, event-driven architecture that is both highly scalable and cost-effective. Amazon S3 is the optimal service for storing large, unstructured objects like PDF and image files due to its low cost, high durability, and virtually unlimited scalability. Configuring an S3 PUT event to trigger an AWS Lambda function creates an automated processing pipeline. Lambda scales automatically to handle any number of concurrent file uploads and conversions, and its pay-per-execution pricing model ensures that the company only pays for the compute time used, making it the most cost-effective option for this workload. Why Incorrect Options are Wrong: B: Amazon DynamoDB is unsuitable for storing large files. It has a 400 KB limit per item, making it impractical and expensive to store 5 MB files, which would require complex chunking logic. C: Using Amazon EBS fo

</details>
