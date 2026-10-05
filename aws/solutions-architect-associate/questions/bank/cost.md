# Cost optimization

22 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. gh-221 `cost`

A company runs an application on a group of Amazon Linux EC2 instances. For compliance reasons, the company must retain all application log files for 7 years. The log files will be analyzed by a reporting tool that must be able to access all the files concurrently.
Which storage solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Amazon S3**

S3 is a highly durable and scalable object storage service. It is designed for high availability and can store large amounts of data. S3 is cost-effective for long-term storage, and its pricing is based on the amount of data stored.

</details>

### 2. gh-238 `cost`

A company wants to experiment with individual AWS accounts for its engineer team. The company wants to be notified as soon as the Amazon EC2 instance usage for a given month exceeds a specific threshold for each account.
What should a solutions architect do to meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use AWS Budgets to create a cost budget for each account. Set the period to monthly. Set the scope to EC2 instances. Set an alert threshold for the budget. Configure an Amazon Simple Notification Service (Amazon SNS) topic to receive a notification when a threshold is exceeded.**

AWS Budgets is a cost management service that allows you to set custom cost and usage budgets that alert you when you exceed your thresholds. In this case, you can create a monthly budget specifically for EC2 instances, and when the usage exceeds the defined threshold, it triggers an alert.

</details>

### 3. gh-262 `cost`

A company plans to use Amazon ElastiCache for its multi-tier web application. A solutions architect creates a Cache VPC for the ElastiCache cluster and an App VPC for the application’s Amazon EC2 instances. Both VPCs are in the us-east-1 Region.
The solutions architect must implement a solution to provide the application’s EC2 instances with access to the ElastiCache cluster.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create a peering connection between the VPCs. Add a route table entry for the peering connection in both VPCs. Configure an inbound rule for the ElastiCache cluster’s security group to allow inbound connection from the application’s security groups.**

Creating a peering connection allows communication between the Cache VPC and the App VPC.

Adding a route table entry in both VPCs for the peering connection ensures that traffic can flow between them.
Inbound Rule in ElastiCache Security Group:

Configuring an inbound rule in the ElastiCache cluster's security group to allow connections from the application's security group enables the EC2 instances in the App VPC to access the ElastiCache cluster.

</details>

### 4. gh-284

As part of budget planning, management wants a report of AWS billed items listed by user. The data will be used to create department budgets. A solutions architect needs to determine the most efficient way to obtain this report information.
Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Create a report in Cost Explorer and download the report.**

AWS Cost Explorer is a tool that allows you to visualize, understand, and manage your AWS costs and usage over time. It provides various pre-built reports and the ability to customize and filter reports based on different dimensions.

Option B, creating a report in Cost Explorer and downloading the report, is a suitable solution for obtaining detailed billed items listed by user. The report can be customized to include data relevant to user costs, and the downloadable report can be used for budget planning.

</details>

### 5. gh-347 `cost`

A company has an application that is running on Amazon EC2 instances. A solutions architect has standardized the company on a particular instance family and various instance sizes based on the current needs of the company.
The company wants to maximize cost savings for the application over the next 3 years. The company needs to be able to change the instance family and sizes in the next 6 months based on application popularity and usage.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Compute Savings Plan**

Compute Savings Plans provide significant cost savings over On-Demand pricing in exchange for a commitment to a consistent amount of compute usage (measured in $/hr) for a 1 or 3 year period. They offer flexibility by allowing you to switch between instance families, sizes, and AZs (Availability Zones) while still benefiting from the savings plan pricing. This aligns well with the company's requirement to change instance family and sizes based on application needs.

</details>

### 6. gh-348 `cost`

A company collects data from a large number of participants who use wearable devices. The company stores the data in an Amazon DynamoDB table and uses applications to analyze the data. The data workload is constant and predictable. The company wants to stay at or below its forecasted budget for DynamoDB.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use provisioned mode. Specify the read capacity units (RCUs) and write capacity units (WCUs).**

In provisioned mode, you provision a specific amount of read and write capacity, which allows you to manage costs more effectively based on your expected workload. This approach is suitable when your workload is predictable, as you can provision the capacity to meet your known requirements. DynamoDB Standard-Infrequent Access (Option A) is designed for cost savings on long-term storage and retrieval of infrequently accessed data, and it might not be the best fit for a constant and predictable workload.

</details>

### 7. gh-383 `cost`

A company is planning to migrate a commercial off-the-shelf application from its on-premises data center to AWS. The software has a software licensing model using sockets and cores with predictable capacity and uptime requirements. The company wants to use its existing licenses, which were purchased earlier this year.
Which Amazon EC2 pricing option is the MOST cost-effective?

<details><summary>Answer</summary>

**A. Dedicated Reserved Hosts**

A Dedicated Host is a physical server with EC2 instance capacity fully dedicated to your use. When you launch instances on a Dedicated Host, those instances run on the dedicated hardware of that host.
Dedicated Hosts provide control over the placement of instances for compliance, licensing, or regulatory requirements.
You can purchase Dedicated Hosts on a reservation model (Reserved Hosts) or pay for them on-demand. The host remains dedicated to you for the specified term in the case of Reserved Hosts.
Dedicated Hosts can be useful for workloads with specific licensing models tied to physical sockets or cores.

</details>

### 8. gh-398 `cost`

A company needs to transfer 600 TB of data from its on-premises network-attached storage (NAS) system to the AWS Cloud. The data transfer must be complete within 2 weeks. The data is sensitive and must be encrypted in transit. The company’s internet connection can support an upload speed of 100 Mbps.
Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use the AWS Snow Family console to order several AWS Snowball Edge Storage Optimized devices. Use the devices to transfer the data to Amazon S3.**

Transferring 600 TB of data over a 100 Mbps connection would take a very long time. AWS Snowball Edge devices allow for offline data transfer, and you can transfer the data to the devices at your location before shipping them to AWS. This way, you are not constrained by the upload speed during the 2-week period.

</details>

### 9. gh-455

A company uses AWS Organizations. The company wants to operate some of its AWS accounts with different budgets. The company wants to receive alerts and automatically prevent provisioning of additional resources on AWS accounts when the allocated budget threshold is met during a specific period.
Which combination of solutions will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**B. Use AWS Budgets to create a budget. Set the budget amount under the Billing dashboards of the required AWS accounts.**

D. Create an IAM role for AWS Budgets to run budget actions with the required permissions.

F. Add an alert to notify the company when each account meets its budget threshold. Add a budget action that selects the IAM identity created with the appropriate service control policy (SCP) to prevent provisioning of additional resources.

</details>

### 10. gh-456 `cost`

A company runs applications on Amazon EC2 instances in one AWS Region. The company wants to back up the EC2 instances to a second Region. The company also wants to provision EC2 resources in the second Region and manage the EC2 instances centrally from one AWS account.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a backup plan by using AWS Backup. Configure cross-Region backup to the second Region for the EC2 instances.**

AWS Backup is a centralized backup service that allows you to create backup plans for various AWS resources, including EC2 instances. With AWS Backup, you can configure cross-Region backups, meaning you can replicate backups from one AWS Region to another. This provides a cost-effective and centralized solution for backup.

</details>

### 11. gh-467

A company uses AWS Organizations. A member account has purchased a Compute Savings Plan. Because of changes in the workloads inside the member account, the account no longer receives the full benefit of the Compute Savings Plan commitment. The company uses less than 50% of its purchased compute power.

<details><summary>Answer</summary>

**B. Turn on discount sharing from the Billing Preferences section of the account console in the company's Organizations management account.**

</details>

### 12. gh-525 `least-ops`

A company wants to add its existing AWS usage cost to its operation cost dashboard. A solutions architect needs to recommend a solution that will give the company access to its usage cost programmatically. The company must be able to access cost data for the current year and forecast costs for the next 12 months.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Access usage cost-related data by using the AWS Cost Explorer API with pagination.**

AWS Cost Explorer is a tool provided by Amazon Web Services (AWS) that allows users to visualize, understand, and manage their AWS costs and usage.

</details>

### 13. gh-541 `cost`

A company wants to build a web application on AWS. Client access requests to the website are not predictable and can be idle for a long time. Only customers who have paid a subscription fee can have the ability to sign in and use the web application.
Which combination of steps will meet these requirements MOST cost-effectively? (Choose three.)

<details><summary>Answer</summary>

**A. Create an AWS Lambda function to retrieve user information from Amazon DynamoDB. Create an Amazon API Gateway endpoint to accept RESTful APIs. Send the API calls to the Lambda function.**

C. Create an Amazon Cognito user pool to authenticate users.

E. Use AWS Amplify to serve the frontend web content with HTML, CSS, and JS. Use an integrated Amazon CloudFront configuration.

AWS Lambda is a serverless computing service, and its pay-per-use pricing model can be cost-effective for sporadic and unpredictable workloads. DynamoDB is a NoSQL database that can scale with demand.

Amazon Cognito provides a scalable and secure user directory for your web application. It allows you to manage user identities and authentication in a cost-effective manner. User pools can be used to handle user registration, authentication, and account recovery.

AWS Amplify simplifies the development of scalable and secure cloud-powered web and mobile apps. CloudFront is a content delivery network (CDN) that can efficiently distribute your web content globally, improving performance.

</details>

### 14. gh-551 `cost`

A company has a financial application that produces reports. The reports average 50 KB in size and are stored in Amazon S3. The reports are frequently accessed during the first week after production and must be stored for several years. The reports must be retrievable within 6 hours.
Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Use S3 Standard. Use an S3 Lifecycle rule to transition the reports to S3 Glacier after 7 days.**

After the initial period, using an S3 Lifecycle rule to transition the reports to the S3 Glacier storage class is a cost-effective approach. Glacier is designed for long-term archival storage with lower storage costs compared to S3 Standard.

</details>

### 15. gh-573 `cost`

A company wants to use an event-driven programming model with AWS Lambda. The company wants to reduce startup latency for Lambda functions that run on Java 11. The company does not have strict latency requirements for the applications. The company wants to reduce cold starts and outlier latencies when a function scales up.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Configure Lambda SnapStart.**

Lambda Cold Start:
When a Lambda function is invoked, it may take a bit of time for the system to set up everything needed to run the function. This initial setup time is called a "cold start." Cold starts can add some delay, especially if the function hasn't been used recently.
Lambda SnapStart:
SnapStart is a feature in AWS Lambda designed to make these cold starts faster, specifically for functions written in Java. Instead of starting from scratch every time a function is called, SnapStart pre-warms the environment. It's like getting things ready in advance so that when your function is called, it can start quickly without much delay.

</details>

### 16. gh-591 `cost`

A company runs a container application by using Amazon Elastic Kubernetes Service (Amazon EKS). The application includes microservices that manage customers and place orders. The company needs to route incoming requests to the appropriate microservices.
Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use the AWS Load Balancer Controller to provision an Application Load Balancer.**

This is a Kubernetes-native controller that allows you to define and manage Application Load Balancers and Network Load Balancers to route traffic to services in your Amazon EKS cluster.
ALBs are designed for routing HTTP/HTTPS traffic and provide more advanced routing features compared to Network Load Balancers.

</details>

### 17. gh-598 `cost`

A research company uses on-premises devices to generate data for analysis. The company wants to use the AWS Cloud to analyze the data. The devices generate .csv files and support writing the data to an SMB file share. Company analysts must be able to use SQL commands to query the data. The analysts will run queries periodically throughout the day.
Which combination of steps will meet these requirements MOST cost-effectively? (Choose three.)

<details><summary>Answer</summary>

**A. Deploy an AWS Storage Gateway on premises in Amazon S3 File Gateway mode.**

C. Set up an AWS Glue crawler to create a table based on the data that is in Amazon S3.

F. Setup Amazon Athena to query the data that is in Amazon S3. Provide access to analysts.

This step allows you to seamlessly integrate on-premises devices with AWS S3, providing a scalable and cost-effective storage solution. The AWS Storage Gateway in S3 File Gateway mode enables you to write data from on-premises devices to S3.

AWS Glue can discover, catalog, and transform data from S3. By setting up a Glue crawler, you create a table schema based on the .csv files in S3. This step prepares the data for analysis.

Amazon Athena allows you to run SQL queries directly on the data stored in S3 without the need for a dedicated database. You can create databases and tables in Athena based on the cataloged data using Glue.

</details>

### 18. gh-606 `cost`

A solutions architect is designing an application that will allow business users to upload objects to Amazon S3. The solution needs to maximize object durability. Objects also must be readily available at any time and for any length of time. Users will access objects frequently within the first 30 days after the objects are uploaded, but users are much less likely to access objects that are older than 30 days.
Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Store all the objects in S3 Standard with an S3 Lifecycle rule to transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.**

Storing objects in S3 Standard ensures low-latency access and high durability. After 30 days, transitioning objects to S3 Standard-IA allows you to take advantage of a lower storage cost for objects that are less frequently accessed.

</details>

### 19. gh-641

A company wants to monitor its AWS costs for financial review. The cloud operations team is designing an architecture in the AWS Organizations management account to query AWS Cost and Usage Reports for all member accounts. The team must run this query once a month and provide a detailed analysis of the bill.
Which solution is the MOST scalable and cost-effective way to meet these requirements?

<details><summary>Answer</summary>

**B. Enable Cost and Usage Reports in the management account. Deliver the reports to Amazon S3 Use Amazon Athena for analysis.**

Amazon Athena is a serverless query service that allows you to analyze data directly in Amazon S3 using SQL queries.

</details>

### 20. gh-643 `cost`

A company runs several websites on AWS for its different brands. Each website generates tens of gigabytes of web traffic logs each day. A solutions architect needs to design a scalable solution to give the company's developers the ability to analyze traffic patterns across all the company's websites. This analysis by the developers will occur on demand once a week over the course of several months. The solution must support queries with standard SQL.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Store the logs in Amazon S3. Use Amazon Athena tor analysis.**

Amazon Athena is a serverless query service that allows you to analyze data directly in Amazon S3 using standard SQL queries. It is cost-effective because you pay only for the queries you run, and there is no need to provision or manage infrastructure.

</details>

### 21. gh-652 `cost`

A company has a large data workload that runs for 6 hours each day. The company cannot lose any data while the process is running. A solutions
architect is designing an Amazon EMR cluster con guration to support this critical data workload.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Answer: B) Configure a transient cluster with primary/core nodes on On-Demand Instances and task nodes on Spot Instances.**

Transient clusters are cost-effective for short workloads. Spot Instances reduce costs for non-critical task nodes.
Long-running clusters (Options A/D) are unnecessary for a 6-hour workload.

</details>

### 22. gh-656 `cost` `availability`

A company runs a website that stores images of historical events. Website users need the ability to search and view images based on the year
that the event in the image occurred. On average, users request each image only once or twice a year. The company wants a highly available
solution to store and deliver the images to users.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Answer: D) Store images in S3 Standard-IA and deliver via static website.**

Standard-IA is cost-effective for rarely accessed images. Static websites simplify delivery.
EBS/EFS (Options A/B) are expensive and lack S3’s durability.

</details>
