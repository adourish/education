# Storage — S3, EBS, EFS, FSx, archive, transfer

129 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. gh-1

A company collects data for temperature, humidity, and atmospheric pressure in cities across multiple continents. The average volume of data that the company collects from each site daily is 500 GB. Each site has a high-speed Internet connection.
The company wants to aggregate the data from all these global sites as quickly as possible in a single Amazon S3 bucket. The solution must minimize operational complexity.
Which solution meets these requirements

<details><summary>Answer</summary>

**Turn on S3 Transfer Acceleration on the destination S3 bucket. Use multipart uploads to directly upload site data to the destination S3 bucket.**

General line: Collect huge amount of the files across multiple continents
Conditions: High speed Internet connectivity
Task: aggregate the data from all in a single S3 bucket
Requirements: as quick as possible, minimize operational complexity

Correct answer A: S3 Transfer Acceleration because:
- ideally works with objects for long-distance transfer (uses Edge Locations)
- can speed up content transfers to and from S3 as much as 50-500%
- use cases: mobile & web application uploads and downloads, distributed office transfers, data exchange with trusted partners. Generally for sharing of large data sets between companies, customers can set up special access to their S3 buckets with accelerated uploads to speed data exchanges and the pace of innovation.

</details>

### 2. gh-2 `least-ops`

A company needs the ability to analyze the log files of its proprietary application. The logs are stored in JSON format in an Amazon S3 bucket. Queries will be simple and will run on-demand. A solutions architect needs to perform the analysis with minimal changes to the existing architecture.
What should the solutions architect do to meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**Use Amazon Athena directly with Amazon S3 to run the queries as needed.**

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds.

</details>

### 3. wl-2

Your team is developing a high-performance computing (HPC) application. The application resolves complex, compute-intensive problems and needs a high-performance and low-latency Lustre file system. You need to configure this file system in AWS at a low cost. Which method is the most suitable?

<details><summary>Answer</summary>

**A. Create a Lustre file system through Amazon FSx.**

The Lustre file system is an open-source, parallel file system that can be used for HPC
applications. Refer to http://lustre.org/ for its introduction. In Amazon FSx, users can
quickly launch a Lustre file system at a low cost.
Option
A 
is
CORRECT:
Amazon FSx supports Lustre file systems and
users pay for only the resources they use.
Option
B 
is
incorrect:
Although users may be able to configure a
Lustre file system through EBS, it needs lots of extra configurations, Option A is
more straightforward.
Option
C 
is
incorrect:
Because the EC2 placement group does not
support a Lustre file system.
Option
D 
is
incorrect:
Because products in AWS Marketplace are not
cost-effective. For Amazon FSx, there are no minimum fees or set-up charges. Check
its pricing in Amazon FSx for Lustre Pricing.
Read Now: Amazon Braket

</details>

### 4. gh-3 `least-ops`

A company uses AWS Organizations to manage multiple AWS accounts for different departments. The management account has an Amazon S3 bucket that contains project reports. The company wants to limit access to this S3 bucket to only users of accounts within the organization in AWS Organizations.
Which solution meets these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**. Add the aws PrincipalOrgID global condition key with a reference to the organization ID to the S3 bucket policy.**

aws:PrincipalOrgID – Simplifies specifying the Principal element in a resource-based policy. This global key provides an alternative to listing all the account IDs for all AWS accounts in an organization. Instead of listing all of the accounts that are members of an organization, you can specify the organization ID in the Condition element.
proposes adding the aws PrincipalOrgID global condition key with a reference to the organization ID to the S3 bucket policy. This would limit access to the S3 bucket to only users of accounts within the organization in AWS Organizations, as the aws PrincipalOrgID condition key can check if the request is coming from within the organization.

</details>

### 5. wl-3

You host a static website in an S3 bucket and there are global clients from multiple regions. You want to use an AWS service to store cache for frequently accessed content so that the latency is reduced and the data transfer rate is increased. Which of the following options would you choose?

<details><summary>Answer</summary>

**D. Configure CloudFront to deliver the content in the S3 bucket.**

CloudFront is able to store the frequently accessed content as a cache and the
performance is optimized. Other options may help on the performance however they
do not store cache for the S3 objects.
Option
A 
is
incorrect:
This option may increase the throughput
however it does not store cache.
Option
B 
is
incorrect:
Because this option does not use cache.
Option
C 
is
incorrect:
This option creates multiple S3 buckets in
different regions. It does not improve the performance using cache.
Option
D 
is
CORRECT:
Because CloudFront caches copies of the S3
files in its edge locations and users are routed to the edge location that has the lowest
latency.

</details>

### 6. gh-5

A company is hosting a web application on AWS using a single Amazon EC2 instance that stores user-uploaded documents in an Amazon EBS volume. For better scalability and availability, the company duplicated the architecture and created a second EC2 instance and EBS volume in another Availability Zone, placing both behind an Application Load Balancer. After completing this change, users reported that, each time they refreshed the website, they could see one subset of their documents or the other, but never all of the documents at the same time.
What should a solutions architect propose to ensure users see all of their documents at once?

<details><summary>Answer</summary>

**C. Copy the data from both EBS volumes to Amazon EFS. Modify the application to save new documents to Amazon EFS**

Option C, which involves copying the data to Amazon EFS and modifying the application to use Amazon EFS for document storage, is the most appropriate solution to ensure users can see all their documents at once in the duplicated architecture. Amazon EFS provides scalability, availability, and shared access, allowing both EC2 instances to access and synchronize the documents seamlessly. Unlike EBS volumes or snapshots, which cannot be shared in real time across multiple instances and Availability Zones, Amazon EFS allows both EC2 instances to access the same file system simultaneously, ensuring all users see the same set of documents regardless of which instance serves their request.

</details>

### 7. gh-6

A company uses NFS to store large video files in on-premises network attached storage. Each video file ranges in size from 1 MB to 500 GB. The total storage is 70 TB and is no longer growing. The company decides to migrate the video files to Amazon S3. The company must migrate the video files as soon as possible while using the least possible network bandwidth.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an AWS Snowball Edge job. Receive a Snowball Edge device on premises. Use the Snowball Edge client to transfer data to the device. Return the device so that AWS can import the data into Amazon S3**

On a Snowball Edge device you can copy files with a speed of up to 100Gbps. 70TB will take around 5600 seconds, so very quickly, less than 2 hours. The downside is that it'll take between 4-6 working days to receive the device and then another 2-3 working days to send it back and for AWS to move the data onto S3 once it reaches them. Total time: 6-9 working days. Bandwidth used: 0.

</details>

### 8. wl-8

You are planning to build a fleet of EBS-optimized EC2 instances for your new application. Due to security compliance, your organization wants you to encrypt root volume which is used to boot the instances. How can this be achieved?

<details><summary>Answer</summary>

**D. Launch an unencrypted EC2 instance and create a snapshot of the root volume.**

When launching an EC2 instance, the EBS volume for root cannot be encrypted.
You can launch the instance with unencrypted root volume and create a snapshot of
the root volume. Once the snapshot is created, you can copy the snapshot where you
can make the new snapshot encrypted.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html#AMI
Encryption

</details>

### 9. gh-9

A company is running an SMB file server in its data center. The file server stores large files that are accessed frequently for the first few days after the files are created. After 7 days the files are rarely accessed.
The total data size is increasing and is close to the company's total storage capacity. A solutions architect must increase the company's available storage space without losing low-latency access to the most recently accessed files. The solutions architect must also provide file lifecycle management to avoid future storage issues.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an Amazon S3 File Gateway to extend the company's storage space. Create an S3 Lifecycle policy to transition the data to S3 Glacier Deep Archive after 7 days.**

Option B: Amazon S3 File Gateway provides a hybrid cloud storage solution, integrating on-premises environments with cloud storage. Files written to the file share are automatically saved as S3 objects. With S3 Lifecycle policies, you can transition objects between storage classes. Transitioning to Glacier Deep Archive is suitable for rarely accessed files. This solution addresses both the storage capacity and lifecycle management requirements.

</details>

### 10. wl-12

Organization ABC has a customer base in the US and Australia that would be downloading 10s of GBs files from your application. For them to have a better download experience, they decided to use the AWS S3 bucket with cross-region replication with the US as the source and Australia as the destination. They are using existing unused S3 buckets and had set up cross-region replication successfully. However, when files uploaded to the US bucket, they are not being replicated to Australia bucket. What could be the reason?

<details><summary>Answer</summary>

**C. Source bucket has a policy with DENY and the role used for replication is not**

When you have a bucket policy which has explicit DENY, you must exclude all IAM
resources which need to access the bucket.
Read more here:
https://aws.amazon.com/blogs/security/how-to-create-a-policy-that-whitelists-access-t
o-sensitive-amazon-s3-buckets/
For option A, Cross region replication cannot be enabled without enabling versioning.
The question states that cross-region replication has been successfully enabled. So this
option is not correct.

</details>

### 11. wl-15

You will be launching and terminating EC2 instances on a need basis for your workloads. You need to run some shell scripts and perform certain checks connecting to the AWS S3 bucket when the instance is getting launched. Which of the following options will allow performing any tasks during launch? (choose multiple)

<details><summary>Answer</summary>

**A. Use Instance user data for shell scripts.; C. Use AutoScaling Group lifecycle hooks and trigger AWS Lambda function**

Option A is correct.
Option C is correct.
https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html#prepari
ng-for-notification

</details>

### 12. gh-17

A company is implementing a new business application. The application runs on two Amazon EC2 instances and uses an Amazon S3 bucket for document storage. A solutions architect needs to ensure that the EC2 instances can access the S3 bucket.
What should the solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Create an IAM role that grants access to the S3 bucket. Attach the role to the EC2 instances**

An IAM role is an AWS resource that allows you to delegate access to AWS resources and services. You can create an IAM role that grants access to the S3 bucket and then attach the role to the EC2 instances. This will allow the EC2 instances to access the S3 bucket and the documents stored within it.

</details>

### 13. gh-18

An application development team is designing a microservice that will convert large images to smaller, compressed images. When a user uploads an image through the web interface, the microservice should store the image in an Amazon S3 bucket, process and compress the image with an AWS Lambda function, and store the image in its compressed form in a different S3 bucket.
A solutions architect needs to design a solution that uses durable, stateless components to process the images automatically.
Which combination of actions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Create an Amazon Simple Queue Service (Amazon SQS) queue. Configure the S3 bucket to send a notification to the SQS queue when an image is uploaded to the S3 bucket.**

B. Configure the Lambda function to use the Amazon Simple Queue Service (Amazon SQS) queue as the invocation source. When the SQS message is successfully processed, delete the message in the queue

Option A: By creating an Amazon SQS queue and configuring the S3 bucket to send a notification to the SQS queue when an image is uploaded, the system establishes a durable and scalable way to handle incoming image processing tasks.

Option B: Configuring the Lambda function to use the SQS queue as the invocation source allows it to retrieve messages from the queue and process them in a stateless manner. After successfully processing the image, the Lambda function can delete the message from the queue to avoid duplicate processing.

</details>

### 14. gh-20

A company wants to improve its ability to clone large amounts of production data into a test environment in the same AWS Region. The data is stored in Amazon EC2 instances on Amazon Elastic Block Store (Amazon EBS) volumes. Modifications to the cloned data must not affect the production environment. The software that accesses this data requires consistently high I/O performance.
A solutions architect needs to minimize the time that is required to clone the production data into the test environment.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Take EBS snapshots of the production EBS volumes. Turn on the EBS fast snapshot restore feature on the EBS snapshots. Restore the snapshots into new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment**

Amazon EBS fast snapshot restore (FSR) enables you to create a volume from a snapshot that is fully initialized at creation. This eliminates the latency of I/O operations on a block when it is accessed for the first time. Volumes that are created using fast snapshot restore instantly deliver all of their provisioned performance

</details>

### 15. gh-21 `least-ops`

An ecommerce company wants to launch a one-deal-a-day website on AWS. Each day will feature exactly one product on sale for a period of 24 hours. The company wants to be able to handle millions of requests each hour with millisecond latency during peak hours.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use an Amazon S3 bucket to host the website's static content. Deploy an Amazon CloudFront distribution. Set the S3 bucket as the origin. Use Amazon API Gateway and AWS Lambda functions for the backend APIs. Store the data in Amazon DynamoDB.**

Use an Amazon S3 bucket to host the website's static content, deploy an Amazon CloudFront distribution, set the S3 bucket as the origin, and use Amazon API Gateway and AWS Lambda functions for the backend APIs. Store the data in Amazon DynamoDB.

Using Amazon S3 to host static content and Amazon CloudFront to distribute the content can provide high performance and scale for websites with millions of requests each hour. Amazon API Gateway and AWS Lambda can be used to build scalable and highly available backend APIs to support the website, and Amazon DynamoDB can be used to store the data. This solution requires minimal operational overhead as it leverages fully managed services that automatically scale to meet demand.

</details>

### 16. gh-22

A solutions architect is using Amazon S3 to design the storage architecture of a new digital media application. The media files must be resilient to the loss of an Availability Zone. Some files are accessed frequently while other files are rarely accessed in an unpredictable pattern. The solutions architect must minimize the costs of storing and retrieving the media files.
Which storage option meets these requirements?

<details><summary>Answer</summary>

**B. S3 Intelligent-Tiering**

Amazon S3 Intelligent Tiering is a storage class that automatically moves data to the most cost-effective storage tier based on access patterns. It can store objects in two access tiers: the frequent access tier and the infrequent access tier. The frequent access tier is optimized for frequently accessed objects and is charged at the same rate as S3 Standard. The infrequent access tier is optimized for objects that are not accessed frequently and are charged at a lower rate than S3 Standard.

S3 Intelligent Tiering is a good choice for storing media files that are accessed frequently and infrequently in an unpredictable pattern because it automatically moves data to the most cost-effective storage tier based on access patterns, minimizing storage and retrieval costs. It is also resilient to the loss of an Availability Zone because it stores objects in multiple Availability Zones within a region.

</details>

### 17. gh-23 `cost`

A company is storing backup files by using Amazon S3 Standard storage. The files are accessed frequently for 1 month. However, the files are not accessed after 1 month. The company must keep the files indefinitely.
Which storage solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create an S3 Lifecycle configuration to transition objects from S3 Standard to S3 Glacier Deep Archive after 1 month.**

Amazon S3 Glacier Deep Archive is a secure, durable, and extremely low-cost Amazon S3 storage class for long-term retention of data that is rarely accessed and for which retrieval times of several hours are acceptable. It is the lowest-cost storage option in Amazon S3, making it a cost-effective choice for storing backup files that are not accessed after 1 month.

You can use an S3 Lifecycle configuration to automatically transition objects from S3 Standard to S3 Glacier Deep Archive after 1 month. This will minimize the storage costs for the backup files that are not accessed frequently.

</details>

### 18. gh-26

A company needs to review its AWS Cloud deployment to ensure that its Amazon S3 buckets do not have unauthorized configuration changes.
What should a solutions architect do to accomplish this goal?

<details><summary>Answer</summary>

**A. Turn on AWS Config with the appropriate rules.**

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. You can use AWS Config to monitor and record changes to the configuration of your Amazon S3 buckets. By turning on AWS Config and enabling the appropriate rules, you can ensure that your S3 buckets do not have unauthorized configuration changes.

</details>

### 19. gh-32 `cost`

A development team needs to host a website that will be accessed by other teams. The website contents consist of HTML, CSS, client-side JavaScript, and images.
Which method is the MOST cost-effective for hosting the website?

<details><summary>Answer</summary>

**B. Create an Amazon S3 bucket and host the website there.**

Explanation:
The website is a static website because it consists only of HTML, CSS, client-side JavaScript, and images. The most cost-effective method is to create an Amazon S3 bucket and host the website there.

Amazon S3 is a highly scalable and cost-effective object storage service. It is suitable for hosting static websites because no web servers, containers, or backend compute resources are required.

To host the website on Amazon S3, the development team would create an S3 bucket, upload the website files to the bucket, and configure the bucket for static website hosting.

Option A is incorrect because AWS Fargate is used to run containers and is unnecessary for a static website. Option C is incorrect because an EC2 web server would add compute cost and operational overhead. Option D is incorrect because using an Application Load Balancer with Lambda and Express.js is overly complex for static content.

</details>

### 20. gh-36 `least-ops`

A company is building an application in the AWS Cloud. The application will store data in Amazon S3 buckets in two AWS Regions. The company must use an AWS Key Management Service (AWS KMS) customer managed key to encrypt all data that is stored in the S3 buckets. The data in both S3 buckets must be encrypted and decrypted with the same KMS key. The data and the key must be stored in each of the two Regions.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a customer managed multi-Region KMS key. Create an S3 bucket in each Region. Configure replication between the S3 buckets. Configure the application to use the KMS key with client-side encryption.**

Explanation:
The requirement says that the data in both S3 buckets must be encrypted and decrypted with the same KMS key, and that the key must exist in both AWS Regions. This points to an AWS KMS multi-Region customer managed key. A multi-Region KMS key has related keys in different Regions with the same key material, which allows data encrypted in one Region to be decrypted in another Region.

Option A is incorrect because SSE-S3 uses Amazon S3 managed keys, not AWS KMS customer managed keys. Option C is incorrect because it creates customer managed KMS keys but then uses SSE-S3. Option D is close, but it creates separate KMS keys in each Region instead of using a multi-Region KMS key with the same key material.

</details>

### 21. gh-40 `availability`

A company has thousands of edge devices that collectively generate 1 TB of status alerts each day. Each alert is approximately 2 KB in size. A solutions architect needs to implement a solution to ingest and store the alerts for future analysis.
The company wants a highly available solution. However, the company needs to minimize costs and does not want to manage additional infrastructure. Additionally, the company wants to keep 14 days of data available for immediate analysis and archive any data older than 14 days.
What is the MOST operationally efficient solution that meets these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon Kinesis Data Firehose delivery stream to ingest the alerts. Configure the Kinesis Data Firehose stream to deliver the alerts to an Amazon S3 bucket. Set up an S3 Lifecycle configuration to transition data to Amazon S3 Glacier after 14 days.**

Amazon Kinesis Data Firehose is a fully managed service that can capture, transform, and deliver streaming data into storage systems or analytics tools, making it an ideal solution for ingesting and storing status alerts. In this solution, the Kinesis Data Firehose delivery stream ingests the alerts and delivers them to an S3 bucket, which is a cost-effective storage solution. An S3 Lifecycle configuration is set up to transition the data to Amazon S3 Glacier after 14 days to minimize storage costs.

</details>

### 22. gh-43

A company has an on-premises application that generates a large amount of time-sensitive data that is backed up to Amazon S3. The application has grown and there are user complaints about internet bandwidth limitations. A solutions architect needs to design a long-term solution that allows for both timely backups to Amazon S3 and with minimal impact on internet connectivity for internal users.
Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Establish a new AWS Direct Connect connection and direct backup traffic through this new connection.**

AWS Direct Connect is a network service that allows you to establish a dedicated network connection from your on-premises data center to AWS. This connection bypasses the public Internet and can provide more reliable, lower-latency communication between your on-premises application and Amazon S3. By directing backup traffic through the AWS Direct Connect connection, you can minimize the impact on your internet bandwidth and ensure timely backups to S3.

</details>

### 23. gh-44

A company has an Amazon S3 bucket that contains critical data. The company must protect the data from accidental deletion.
Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Enable versioning on the S3 bucket**

B. Enable MFA Delete on the S3 bucket

The two most effective steps a solutions architect can take to protect an Amazon S3 bucket from accidental deletion are:

A. Enable versioning on the S3 bucket.
B. Enable MFA Delete on the S3 bucket.

Versioning keeps multiple versions of objects in the S3 bucket, even when they are overwritten or deleted. This allows you to recover objects that have been accidentally deleted.

MFA Delete requires you to enter a one-time password from a multi-factor authentication (MFA) device before you can delete an object in the S3 bucket. This helps to prevent accidental deletions.

</details>

### 24. gh-46

A company has an application that provides marketing services to stores. The services are based on previous purchases by store customers. The stores upload transaction data to the company through SFTP, and the data is processed and analyzed to generate new marketing offers. Some of the files can exceed 200 GB in size.
Recently, the company discovered that some of the stores have uploaded files that contain personally identifiable information (PII) that should not have been included. The company wants administrators to be alerted if PII is shared again. The company also wants to automate remediation.
What should a solutions architect do to meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**B. Use an Amazon S3 bucket as a secure transfer point. Use Amazon Macie to scan the objects in the bucket. If objects contain PII, use Amazon Simple Notification Service (Amazon SNS) to trigger a notification to the administrators to remove the objects that contain PII.**

Some quotas can be increased, while others cannot. To request an increase to a quota, use the Service Quotas console. To learn how to request an increase, see Requesting a quota increase in the Service Quotas User Guide. If a quota isn't available on the Service Quotas console, use the service limit increase form on the AWS Support Center Console to request an increase to the quota.

</details>

### 25. gh-49 `cost`

A company stores call transcript files on a monthly basis. Users access the files randomly within 1 year of the call, but users access the files infrequently after 1 year. The company wants to optimize its solution by giving users the ability to query and retrieve files that are less than 1-year-old as quickly as possible. A delay in retrieving older files is acceptable.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Store individual files in Amazon S3 Intelligent-Tiering. Use S3 Lifecycle policies to move the files to S3 Glacier Flexible Retrieval after 1 year. Query and retrieve the files that are in Amazon S3 by using Amazon Athena. Query and retrieve the files that are in S3 Glacier by using S3 Glacier Select.**

S3 Intelligent-Tiering is the ideal storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. You can use S3 Intelligent-Tiering as the default storage class for virtually any workload, especially data lakes, data analytics, new applications, and user-generated content.

</details>

### 26. gh-188 `availability`

A company uses Amazon S3 as its data lake. The company has a new partner that must use SFTP to upload data files. A solutions architect needs to implement a highly available SFTP solution that minimizes operational overhead.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Transfer Family to configure an SFTP-enabled server with a publicly accessible endpoint. Choose the S3 data lake as the destination.**

AWS Transfer Family is a fully managed service that allows you to set up a secure file transfer protocol (SFTP) server for transferring files into and out of Amazon S3. With AWS Transfer Family, you can avoid the operational overhead of managing traditional SFTP servers. This solution provides a highly available SFTP service with minimal effort, and the data can be directly transferred to the S3 data lake.

</details>

### 27. gh-189 `least-ops`

A company needs to store contract documents. A contract lasts for 5 years. During the 5-year period, the company must ensure that the documents cannot be overwritten or deleted. The company needs to encrypt the documents at rest and rotate the encryption keys automatically every year.
Which combination of steps should a solutions architect take to meet these requirements with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**B. Store the documents in Amazon S3. Use S3 Object Lock in compliance mode.**

S3 Object Lock in compliance mode enforces a "Write Once, Read Many" (WORM) model, preventing the objects (contract documents, in this case) from being deleted or overwritten for a specified retention period.

D. Use server-side encryption with AWS Key Management Service (AWS KMS) customer managed keys. Configure key rotation.

By using AWS KMS customer managed keys, you can configure key rotation to automatically rotate encryption keys, meeting the requirement of rotating encryption keys every year.

</details>

### 28. gh-202 `least-ops`

A company is planning to move its data to an Amazon S3 bucket. The data must be encrypted when it is stored in the S3 bucket. Additionally, the encryption key must be automatically rotated every year.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an AWS Key Management Service (AWS KMS) customer managed key. Enable automatic key rotation. Set the S3 bucket’s default encryption behavior to use the customer managed KMS key. Move the data to the S3 bucket.**

In this option, you use AWS KMS to create a customer managed key, enable automatic key rotation, and set it as the default encryption key for the S3 bucket. This ensures that the data is encrypted with a key managed by AWS KMS, and the key rotation is handled automatically. This approach minimizes manual intervention and provides a secure and automated solution for data encryption with key rotation.

</details>

### 29. gh-205 `cost`

A company hosts a marketing website in an on-premises data center. The website consists of static documents and runs on a single server. An administrator updates the website content infrequently and uses an SFTP client to upload new documents.
The company decides to host its website on AWS and to use Amazon CloudFront. The company’s solutions architect creates a CloudFront distribution. The solutions architect must design the most cost-effective and resilient architecture for website hosting to serve as the CloudFront origin.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a private Amazon S3 bucket. Use an S3 bucket policy to allow access from a CloudFront origin access identity (OAI). Upload website content by using the AWS CLI.**

This option leverages Amazon S3 as the origin for CloudFront. By creating a private S3 bucket and using a bucket policy to allow access from a CloudFront origin access identity (OAI), you ensure that the content is served securely from S3 and that only CloudFront can access the bucket.

</details>

### 30. gh-212 `cost`

A company needs to export its database once a day to Amazon S3 for other teams to access. The exported object size varies between 2 GB and 5 GB. The S3 access pattern for the data is variable and changes rapidly. The data must be immediately available and must remain accessible for up to 3 months. The company needs the most cost-effective solution that will not increase retrieval time.
Which S3 storage class should the company use to meet these requirements?

<details><summary>Answer</summary>

**A. S3 Intelligent-Tiering**

S3 Intelligent-Tiering is designed to optimize costs by automatically moving objects between two access tiers: frequent and infrequent access. It is suitable for data with unknown or changing access patterns.
With S3 Intelligent-Tiering, Amazon S3 automatically and transparently moves objects between access tiers based on changing access patterns. It is cost-effective for a wide range of storage access patterns.
The objects can be immediately accessed, and the storage cost is lower than using S3 Standard, making it a suitable choice for varying access patterns.

</details>

### 31. gh-215 `cost`

A company has 700 TB of backup data stored in network attached storage (NAS) in its data center. This backup data need to be accessible for infrequent regulatory requests and must be retained 7 years. The company has decided to migrate this backup data from its data center to AWS. The migration must be complete within 1 month. The company has 500 Mbps of dedicated bandwidth on its public internet connection available for data transfer.
What should a solutions architect do to migrate and store the data at the LOWEST cost?

<details><summary>Answer</summary>

**A. Order AWS Snowball devices to transfer the data. Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.**

AWS Snowball: AWS Snowball is a physical data transfer service that allows you to securely transfer large amounts of data into and out of AWS. In this scenario, with 700 TB of data, using Snowball devices can expedite the transfer process. It's a one-time cost-efficient solution for large data transfers.
Amazon S3 Glacier Deep Archive: After transferring the data to Amazon S3 using Snowball, you can use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive. This storage class is designed for infrequently accessed data with a retention requirement of 7 years, aligning with the regulatory compliance needs.

</details>

### 32. gh-216

A company has a serverless website with millions of objects in an Amazon S3 bucket. The company uses the S3 bucket as the origin for an Amazon CloudFront distribution. The company did not set encryption on the S3 bucket before the objects were loaded. A solutions architect needs to enable encryption for all existing objects and for all objects that are added to the S3 bucket in the future.
Which solution will meet these requirements with the LEAST amount of effort?

<details><summary>Answer</summary>

**B. Turn on the default encryption settings for the S3 bucket. Use the S3 Inventory feature to create a .csv file that lists the unencrypted objects. Run an S3 Batch Operations job that uses the copy command to encrypt those objects.**

This option utilizes the S3 Inventory feature to generate a list of unencrypted objects in the S3 bucket. It then leverages S3 Batch Operations to perform a copy operation, allowing the encryption of the objects during the copy process. This approach is efficient and does not require downloading and re-uploading all existing objects.

</details>

### 33. gh-226

A company collects data from thousands of remote devices by using a RESTful web services application that runs on an Amazon EC2 instance. The EC2 instance receives the raw data, transforms the raw data, and stores all the data in an Amazon S3 bucket. The number of remote devices will increase into the millions soon. The company needs a highly scalable solution that minimizes operational overhead.
Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use AWS Glue to process the raw data in Amazon S3.**

E. Use Amazon API Gateway to send the raw data to an Amazon Kinesis data stream. Configure Amazon Kinesis Data Firehose to use the data stream as a source to deliver the data to Amazon S3.

A. It automatically discovers the schema of the data and generates ETL code to transform it.

E. API Gateway can be used to receive the raw data from the remote devices via RESTful web services. It provides a scalable and managed infrastructure to handle the incoming requests. The data can then be sent to an Amazon Kinesis data stream, which is a highly scalable and durable real-time data streaming service. From there, Amazon Kinesis Data Firehose can be configured to use the data stream as a source and deliver the transformed data to Amazon S3. This combination of services allows for the seamless ingestion and processing of data while minimizing operational overhead.

</details>

### 34. gh-227 `cost`

A company needs to retain its AWS CloudTrail logs for 3 years. The company is enforcing CloudTrail across a set of AWS accounts by using AWS Organizations from the parent account. The CloudTrail target S3 bucket is configured with S3 Versioning enabled. An S3 Lifecycle policy is in place to delete current objects after 3 years.
After the fourth year of use of the S3 bucket, the S3 bucket metrics show that the number of objects has continued to rise. However, the number of new CloudTrail logs that are delivered to the S3 bucket has remained consistent.
Which solution will delete objects that are older than 3 years in the MOST cost-effective manner?

<details><summary>Answer</summary>

**B. Configure the S3 Lifecycle policy to delete previous versions as well as current versions.**

S3 Lifecycle Policy: Enabling S3 versioning allows you to use a lifecycle policy to manage both current and previous versions of objects in the bucket. By configuring the S3 Lifecycle policy to delete objects older than 3 years, it will automatically delete both the current and previous versions that meet the specified criteria.

</details>

### 35. gh-243

A medical research lab produces data that is related to a new study. The lab wants to make the data available with minimum latency to clinics across the country for their on-premises, file-based applications. The data files are stored in an Amazon S3 bucket that has read-only permissions for each clinic.
What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Deploy an AWS Storage Gateway file gateway as a virtual machine (VM) on premises at each clinic**

This option provides a way to present an S3 bucket as a file system to on-premises applications. Each clinic can deploy an AWS Storage Gateway file gateway as a VM on-premises, allowing them to access the data in the S3 bucket as if it were local files. It minimizes latency because the data is cached locally, and read-only permissions can be controlled at the S3 bucket level.

</details>

### 36. gh-249

249Topic 1
A company is implementing a shared storage solution for a media application that is hosted in the AWS Cloud. The company needs the ability to use SMB clients to access data. The solution must be fully managed.
Which AWS solution meets these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Windows File Server file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Windows File Server is a fully managed file storage service that supports the SMB protocol. It provides a native Windows file system experience and is designed to be accessed by SMB clients. This option meets the requirements for a fully managed shared storage solution accessible via SMB.

</details>

### 37. gh-250

A company’s security team requests that network traffic be captured in VPC Flow Logs. The logs will be frequently accessed for 90 days and then accessed intermittently.
What should a solutions architect do to meet these requirements when configuring the logs?

<details><summary>Answer</summary>

**D. Use Amazon S3 as the target. Enable an S3 Lifecycle policy to transition the logs to S3 Standard-Infrequent Access (S3 Standard-IA) after 90 days.**

Amazon S3 is a scalable and cost-effective object storage service. Enabling an S3 Lifecycle policy to transition logs to S3 Standard-Infrequent Access (S3 Standard-IA) after 90 days is a suitable solution. This approach allows you to store the logs in a cost-effective manner, automatically moving them to a lower-cost storage class after the initial 90 days.

</details>

### 38. gh-252

A solutions architect needs to design a system to store client case files. The files are core company assets and are important. The number of files will grow over time.
The files must be simultaneously accessible from multiple application servers that run on Amazon EC2 instances. The solution must have built-in redundancy.
Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Amazon Elastic File System (Amazon EFS)**

</details>

### 39. gh-256

A solutions architect is implementing a document review application using an Amazon S3 bucket for storage. The solution must prevent accidental deletion of the documents and ensure that all versions of the documents are available. Users must be able to download, modify, and upload documents.
Which combination of actions should be taken to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Enable versioning on the bucket.**

D. Enable MFA Delete on the bucket.
B. allows multiple versions of objects in the S3 bucket to be stored. This ensures that all versions of the documents are available, even if they are accidentally overwritten or deleted.

D. adds an extra layer of protection against accidental deletion of objects in the bucket. With MFA Delete enabled, a user would need to provide an additional authentication factor to successfully delete objects from the bucket. This helps prevent accidental or unauthorized deletions and provides an extra level of security for critical documents.

</details>

### 40. gh-259

A company is implementing new data retention policies for all databases that run on Amazon RDS DB instances. The company must retain daily backups for a minimum period of 2 years. The backups must be consistent and restorable.
Which solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Create a backup vault in AWS Backup to retain RDS backups. Create a new backup plan with a daily schedule and an expiration period of 2 years after creation. Assign the RDS DB instances to the backup plan.**

</details>

### 41. gh-260

A company’s compliance team needs to move its file shares to AWS. The shares run on a Windows Server SMB file share. A self-managed on-premises Active Directory controls access to the files and folders.
The company wants to use Amazon FSx for Windows File Server as part of the solution. The company must ensure that the on-premises Active Directory groups restrict access to the FSx for Windows File Server SMB compliance shares, folders, and files after the move to AWS. The company has created an FSx for Windows File Server file system.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Join the file system to the Active Directory to restrict access.**

Join the File System to Active Directory:

By joining the FSx for Windows File Server file system to the on-premises Active Directory, you extend the trust relationship to AWS.
This ensures that access control is based on the on-premises Active Directory groups, allowing you to continue using the existing groups to restrict access to shares, folders, and files.
After joining the file system to Active Directory, you can manage access controls using the existing Active Directory groups.
Users and groups from the on-premises Active Directory can be granted appropriate permissions on the FSx file system.

</details>

### 42. gh-270

A company is using a centralized AWS account to store log data in various Amazon S3 buckets. A solutions architect needs to ensure that the data is encrypted at rest before the data is uploaded to the S3 buckets. The data also must be encrypted in transit.
Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Use client-side encryption to encrypt the data that is being uploaded to the S3 buckets.**

</details>

### 43. gh-277 `cost`

A company provides an online service for posting video content and transcoding it for use by any mobile platform. The application architecture uses Amazon Elastic File System (Amazon EFS) Standard to collect and store the videos so that multiple Amazon EC2 Linux instances can access the video content for processing. As the popularity of the service has grown over time, the storage costs have become too expensive.
Which storage solution is MOST cost-effective?

<details><summary>Answer</summary>

**D. Use Amazon S3 for storing the video content. Move the files temporarily over to an Amazon Elastic Block Store (Amazon EBS) volume attached to the server for processing.**

Amazon S3 is a highly durable, scalable, and cost-effective object storage service.
It is well-suited for storing large amounts of video content at a lower cost compared to Amazon EFS.

</details>

### 44. gh-278

A company wants to create an application to store employee data in a hierarchical structured relationship. The company needs a minimum-latency response to high-traffic queries for the employee data and must protect any sensitive data. The company also needs to receive monthly email messages if any financial information is present in the employee data.
Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Use Amazon DynamoDB to store the employee data in hierarchies. Export the data to Amazon S3 every month.**

E. Configure Amazon Macie for the AWS account. Integrate Macie with Amazon EventBridge to send monthly notifications through an Amazon Simple Notification Service (Amazon SNS) subscription.

Amazon DynamoDB is a highly scalable, low-latency NoSQL database that can efficiently store hierarchical data.
Exporting the data to Amazon S3 every month allows further analysis and integration with other AWS services.

Amazon Macie is a security service that automatically discovers, classifies, and protects sensitive data.
Integrating Macie with EventBridge allows you to set up monthly events and send notifications through Amazon SNS if financial information is detected.

</details>

### 45. gh-280

A company is using Amazon CloudFront with its website. The company has enabled logging on the CloudFront distribution, and logs are saved in one of the company’s Amazon S3 buckets. The company needs to perform advanced analyses on the logs and build visualizations.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Use standard SQL queries in Amazon Athena to analyze the CloudFront logs in the S3 bucket. Visualize the results with Amazon QuickSight.**

Amazon Athena allows you to run standard SQL queries directly on the CloudFront logs stored in the S3 bucket. This enables you to perform advanced analyses on the log data.

Once you have queried and processed the CloudFront log data using Athena, you can use Amazon QuickSight for data visualization and building visualizations.

Amazon QuickSight is a business intelligence (BI) tool that allows you to create interactive dashboards and visualizations from various data sources, including the results of Athena queries.

</details>

### 46. gh-286

A company has a static website that is hosted on Amazon CloudFront in front of Amazon S3. The static website uses a database backend. The company notices that the website does not reflect updates that have been made in the website’s Git repository. The company checks the continuous integration and continuous delivery (CI/CD) pipeline between the Git repository and Amazon S3. The company verifies that the webhooks are configured properly and that the CI/CD pipeline is sending messages that indicate successful deployments.
A solutions architect needs to implement a solution that displays the updates on the website.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Invalidate the CloudFront cache.**

When the website does not reflect updates that have been made in the Git repository, and the CI/CD pipeline is sending messages indicating successful deployments, it's likely that the issue is related to caching. Amazon CloudFront caches content to improve performance and reduce latency, and if the cache is not updated, it may serve stale content.

By invalidating the CloudFront cache, you ensure that the next request to CloudFront fetches the latest content from the origin (in this case, Amazon S3). This process forces CloudFront to re-fetch the content and update its cache.

</details>

### 47. gh-288

A company is migrating a Linux-based web server group to AWS. The web servers must access files in a shared file store for some content. The company must not make any changes to the application.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Elastic File System (Amazon EFS) file system. Mount the EFS file system on all web servers.**

To meet the requirement of providing a shared file store for Linux-based web servers without making changes to the application, you can use Amazon Elastic File System (Amazon EFS). Amazon EFS is a scalable and fully managed file storage service that can be easily mounted on multiple EC2 instances.

</details>

### 48. gh-293 `security`

A company has an on-premises volume backup solution that has reached its end of life. The company wants to use AWS as part of a new backup solution and wants to maintain local access to all the data while it is backed up on AWS. The company wants to ensure that the data backed up on AWS is automatically and securely transferred.
Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use AWS Storage Gateway and configure a stored volume gateway. Run the Storage Gateway software appliance on premises and map the gateway storage volumes to on-premises storage. Mount the gateway storage volumes to provide local access to the data.**

</details>

### 49. gh-295 `least-ops`

An ecommerce company stores terabytes of customer data in the AWS Cloud. The data contains personally identifiable information (PII). The company wants to use the data in three applications. Only one of the applications needs to process the PII. The PII must be removed before the other two applications process the data.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Store the data in an Amazon S3 bucket. Process and transform the data by using S3 Object Lambda before returning the data to the requesting application.**

S3 Object Lambda allows you to add custom code to process and transform data as it is requested by applications, without having to modify the original data stored in S3.
By using S3 Object Lambda, you can process and remove the personally identifiable information (PII) on-the-fly before returning the data to the applications.
This approach minimizes operational overhead because you don't need to create separate storage (buckets or tables) for each application, and you can apply the PII removal logic dynamically as the data is requested.

</details>

### 50. gh-299

A research laboratory needs to process approximately 8 TB of data. The laboratory requires sub-millisecond latencies and a minimum throughput of 6 GBps for the storage subsystem. Hundreds of Amazon EC2 instances that run Amazon Linux will distribute and process the data.
Which solution will meet the performance requirements?

<details><summary>Answer</summary>

**B. Create an Amazon S3 bucket to store the raw data. Create an Amazon FSx for Lustre file system that uses persistent SSD storage. Select the option to import data from and export data to Amazon S3. Mount the file system on the EC2 instances.**

Amazon FSx for Lustre is a high-performance file system designed for use with compute-intensive workloads. It provides sub-millisecond latencies and is well-suited for scenarios where high throughput is required.
Using persistent SSD storage for the Amazon FSx for Lustre file system ensures that it meets the minimum throughput requirement of 6 GBps.
Storing the raw data in an Amazon S3 bucket allows for scalable and durable storage, and the integration with FSx for Lustre allows seamless importing and exporting of data to and from S3.
This solution is designed to provide the required performance characteristics for processing large amounts of data with hundreds of EC2 instances.

</details>

### 51. gh-302

A company wants to create a mobile app that allows users to stream slow-motion video clips on their mobile devices. Currently, the app captures video clips and uploads the video clips in raw format into an Amazon S3 bucket. The app retrieves these video clips directly from the S3 bucket. However, the videos are large in their raw format.
Users are experiencing issues with buffering and playback on mobile devices. The company wants to implement solutions to maximize the performance and scalability of the app while minimizing operational overhead.
Which combination of solutions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Deploy Amazon CloudFront for content delivery and caching.**

C. Use Amazon Elastic Transcoder to convert the video files to more appropriate formats.

Amazon CloudFront is a content delivery network (CDN) that can distribute your video content globally, reducing latency and improving the speed of delivery.
CloudFront can cache the video content at edge locations, which helps in minimizing the load on the S3 bucket and improves playback performance for users.

Amazon Elastic Transcoder can convert the raw video files into more appropriate formats suitable for streaming, reducing the size of the videos.
By using Elastic Transcoder, you can create different versions of the video files optimized for different devices, bitrates, and resolutions, which can significantly improve the playback experience on mobile devices

</details>

### 52. gh-304 `least-ops`

A company recently created a disaster recovery site in a different AWS Region. The company needs to transfer large amounts of data back and forth between NFS file systems in the two Regions on a periodic basis.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS DataSync.**

If we want to transfer large amount of data we can used AWS Datasync.

</details>

### 53. gh-305

A company is designing a shared storage solution for a gaming application that is hosted in the AWS Cloud. The company needs the ability to use SMB clients to access data. The solution must be fully managed.
Which AWS solution meets these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon FSx for Windows File Server file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Windows File Server is a fully managed file storage service that is compatible with the Server Message Block (SMB) protocol, making it suitable for use with SMB clients, including Windows-based systems.
With Amazon FSx for Windows File Server, you can create a file system that can be mounted on application servers, providing shared storage for the gaming application.
Amazon FSx for Windows File Server handles the management aspects such as server provisioning, maintenance, and backups, making it a fully managed solution.

</details>

### 54. gh-307

A company that primarily runs its application servers on premises has decided to migrate to AWS. The company wants to minimize its need to scale its Internet Small Computer Systems Interface (iSCSI) storage on premises. The company wants only its recently accessed data to remain stored locally.
Which AWS solution should the company use to meet these requirements?

<details><summary>Answer</summary>

**D. AWS Storage Gateway Volume Gateway cached volumes.**

AWS Storage Gateway provides a hybrid cloud storage service that enables on-premises applications to use cloud storage seamlessly.
Volume Gateway offers two modes: cached volumes and stored volumes.
In the cached volumes mode, the entire dataset is stored in Amazon S3, and the most frequently accessed data is cached on-premises. This allows the company to keep recently accessed data locally, minimizing the need for on-premises scaling.

</details>

### 55. gh-309 `least-ops`

A solutions architect needs to optimize storage costs. The solutions architect must identify any Amazon S3 buckets that are no longer being accessed or are rarely accessed.
Which solution will accomplish this goal with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Analyze bucket access patterns by using the S3 Storage Lens dashboard for advanced activity metrics.**

S3 Storage Lens is a feature of Amazon S3 that provides a detailed set of reports and metrics to help you understand, analyze, and optimize your storage usage.
The S3 Storage Lens dashboard provides advanced activity metrics, including insights into access patterns, data transfer, and other storage-related activities.
By using the S3 Storage Lens dashboard, you can easily identify buckets that are no longer being accessed or are rarely accessed without the need for additional setup or operational overhead.

</details>

### 56. gh-310 `performance`

A company sells datasets to customers who do research in artificial intelligence and machine learning (AI/ML). The datasets are large, formatted files that are stored in an Amazon S3 bucket in the us-east-1 Region. The company hosts a web application that the customers use to purchase access to a given dataset. The web application is deployed on multiple Amazon EC2 instances behind an Application Load Balancer. After a purchase is made, customers receive an S3 signed URL that allows access to the files.
The customers are distributed across North America and Europe. The company wants to reduce the cost that is associated with data transfers and wants to maintain or improve performance.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an Amazon CloudFront distribution with the existing S3 bucket as the origin. Direct customer requests to the CloudFront URL. Switch to CloudFront signed URLs for access control.**

Amazon CloudFront: CloudFront is a content delivery network (CDN) service that distributes content globally with low latency and high data transfer speeds. It helps reduce data transfer costs and improves performance by caching content at edge locations.
S3 Bucket as the Origin: By configuring the existing S3 bucket as the origin for CloudFront, you allow CloudFront to cache and serve the datasets from edge locations around the world.
CloudFront Signed URLs: CloudFront provides the ability to generate signed URLs, allowing you to control access to your content. You can use CloudFront signed URLs for access control, providing a secure way for customers to access datasets.

</details>

### 57. gh-312

A company has an application that runs on several Amazon EC2 instances. Each EC2 instance has multiple Amazon Elastic Block Store (Amazon EBS) data volumes attached to it. The application’s EC2 instance configuration and data need to be backed up nightly. The application also needs to be recoverable in a different AWS Region.
Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create a backup plan by using AWS Backup to perform nightly backups. Copy the backups to another Region. Add the application’s EC2 instances as resources.**

AWS Backup: AWS Backup is a fully managed backup service that centralizes and automates the backup of data across AWS services. It provides a simple and efficient way to back up your EC2 instances and their associated EBS volumes.
Backup Plan: With AWS Backup, you can create backup plans to define when and how your backups are performed. Backup plans allow you to schedule nightly backups and define retention policies.
Explanation: Adding only the EBS volumes as resources backs up the data but not the instance configuration, so recovery would mean manually rebuilding the EC2 instance and reattaching volumes. Adding the EC2 instances themselves as resources backs up the instance and its attached volumes together, in one operationally simpler recovery step.

</details>

### 58. gh-321

What should a solutions architect do to ensure that all objects uploaded to an Amazon S3 bucket are encrypted?

<details><summary>Answer</summary>

**D. Update the bucket policy to deny if the PutObject does not have an x-amz-server-side-encryption header set.**

x-amz-server-side-encryption header: This header specifies the server-side encryption algorithm to be used for the object. If an object is uploaded without the x-amz-server-side-encryption header or with an incorrect value, it can be denied.

</details>

### 59. gh-324

A company wants to implement a disaster recovery plan for its primary on-premises file storage volume. The file storage volume is mounted from an Internet Small Computer Systems Interface (iSCSI) device on a local storage server. The file storage volume holds hundreds of terabytes (TB) of data.
The company wants to ensure that end users retain immediate access to all file types from the on-premises systems without experiencing latency.
Which solution will meet these requirements with the LEAST amount of change to the company's existing infrastructure?

<details><summary>Answer</summary>

**D. Provision an AWS Storage Gateway Volume Gateway stored volume sized to hold all the existing data. Mount the Volume Gateway stored volume to the existing file server by using iSCSI, and copy all files to the storage volume. Configure scheduled snapshots of the storage volume. To recover from a disaster, restore a snapshot to an Amazon Elastic Block Store (Amazon EBS) volume and attach the EBS volume to an Amazon EC2 instance.**

Explanation: A cached volume only keeps the most frequently accessed data locally — anything not in cache has to be fetched from S3 first, adding latency, so it fails the "immediate access to all file types" requirement. A stored volume keeps the entire dataset on-premises (with async backup to S3), giving true zero-latency access to every file.

</details>

### 60. gh-331

A company must migrate 20 TB of data from a data center to the AWS Cloud within 30 days. The company’s network bandwidth is limited to 15 Mbps and cannot exceed 70% utilization.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Snowball.**

AWS Snowball is a physical data transport solution that helps customers transfer large amounts of data into and out of AWS. It addresses challenges associated with large-scale data transfers, particularly when network constraints, transfer times, or security concerns make online data transfer less practical.

</details>

### 61. gh-332 `security`

A company needs to provide its employees with secure access to confidential and sensitive files. The company wants to ensure that the files can be accessed only by authorized users. The files must be downloaded securely to the employees’ devices.
The files are stored in an on-premises Windows file server. However, due to an increase in remote usage, the file server is running out of capacity.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the files to an Amazon FSx for Windows File Server file system. Integrate the Amazon FSx file system with the on-premises Active Directory. Configure AWS Client VPN.**

Amazon FSx for Windows File Server: It is a fully managed file storage service built on Windows Server. It is designed to be integrated with on-premises Active Directory, allowing for a seamless extension of your existing directory and authentication infrastructure to the AWS Cloud.

Integrate with On-Premises Active Directory: With Amazon FSx, you can integrate the file system with your on-premises Active Directory, ensuring that the same user accounts and permissions are used both on-premises and in the cloud.

</details>

### 62. gh-334 `least-ops`

A company wants to give a customer the ability to use on-premises Microsoft Active Directory to download files that are stored in Amazon S3. The customer’s application uses an SFTP client to download the files.
Which solution will meet these requirements with the LEAST operational overhead and no changes to the customer’s application?

<details><summary>Answer</summary>

**A. Set up AWS Transfer Family with SFTP for Amazon S3. Configure integrated Active Directory authentication.**

AWS Transfer Family with SFTP for Amazon S3: AWS Transfer Family is a fully managed service that allows you to set up an SFTP (Secure File Transfer Protocol) service for Amazon S3. It enables you to transfer files directly to and from Amazon S3 using the SFTP protocol.

Integrated Active Directory Authentication: AWS Transfer Family allows you to configure authentication with Microsoft Active Directory. By integrating with Active Directory, you can provide users with seamless access to S3 resources using their existing credentials without modifying their applications.

</details>

### 63. gh-346

A company has an aging network-attached storage (NAS) array in its data center. The NAS array presents SMB shares and NFS shares to client workstations. The company does not want to purchase a new NAS array. The company also does not want to incur the cost of renewing the NAS array’s support contract. Some of the data is accessed frequently, but much of the data is inactive.
A solutions architect needs to implement a solution that migrates the data to Amazon S3, uses S3 Lifecycle policies, and maintains the same look and feel for the client workstations. The solutions architect has identified AWS Storage Gateway as part of the solution.
Which type of storage gateway should the solutions architect provision to meet these requirements?

<details><summary>Answer</summary>

**D. Amazon S3 File Gateway**

Amazon S3 File Gateway provides on-premises applications with access to virtually unlimited cloud storage using NFS and SMB file interfaces. It seamlessly moves frequently accessed data to a low-latency cache while storing colder data in Amazon S3, using S3 Lifecycle policies to transition data between storage classes over tim

</details>

### 64. gh-371 `least-ops`

A company needs to create an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to host a digital media streaming application. The EKS cluster will use a managed node group that is backed by Amazon Elastic Block Store (Amazon EBS) volumes for storage. The company must encrypt all data at rest by using a customer managed key that is stored in AWS Key Management Service (AWS KMS).
Which combination of actions will meet this requirement with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**C. Enable EBS encryption by default in the AWS Region where the EKS cluster will be created. Select the customer managed key as the default key.**

D. Create the EKS cluster. Create an IAM role that has a policy that grants permission to the customer managed key. Associate the role with the EKS cluster.

EBS encryption is set regionally. AWS account is global but it does not mean EBS encryption is enable by default at account level. default EBS encryption is a regional setting within your AWS account. Enabling it in a specific region ensures that all new EBS volumes created in that region are encrypted by default, using either the default AWS managed key or a customer managed key that you specify.

</details>

### 65. gh-373 `cost`

A company has an application that collects data from IoT sensors on automobiles. The data is streamed and stored in Amazon S3 through Amazon Kinesis Data Firehose. The data produces trillions of S3 objects each year. Each morning, the company uses the data from the previous 30 days to retrain a suite of machine learning (ML) models.
Four times each year, the company uses the data from the previous 12 months to perform analysis and train other ML models. The data must be available with minimal delay for up to 1 year. After 1 year, the data must be retained for archival purposes.
Which storage solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Use the S3 Standard storage class. Create an S3 Lifecycle policy to transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days, and then to S3 Glacier Deep Archive after 1 year.**

S3 Standard Storage Class:

Use S3 Standard for the first 30 days because it's the default storage class for frequently accessed data.
This is suitable for the initial period when you need quick and frequent access to your data.
S3 Standard-Infrequent Access (S3 Standard-IA) Storage Class:
After the initial 30 days, transition the data to S3 Standard-IA.
S3 Standard-IA is designed for data that is accessed less frequently but still requires quick retrieval when needed.
It's more cost-effective for data that is accessed less often compared to S3 Standard.
S3 Glacier Deep Archive:
After 1 year, transition the data from S3 Standard-IA to S3 Glacier Deep Archive using an S3 Lifecycle policy.
S3 Glacier Deep Archive is the most cost-effective option for long-term archival storage.
This is suitable for storing data that you need to retain for compliance or archival purposes but don't need to access frequently.

</details>

### 66. gh-384 `cost` `availability`

A company runs an application on Amazon EC2 Linux instances across multiple Availability Zones. The application needs a storage layer that is highly available and Portable Operating System Interface (POSIX)-compliant. The storage layer must provide maximum data durability and must be shareable across the EC2 instances. The data in the storage layer will be accessed frequently for the first 30 days and will be accessed infrequently after that time.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use the Amazon Elastic File System (Amazon EFS) Standard storage class. Create a lifecycle management policy to move infrequently accessed data to EFS Standard-Infrequent Access (EFS Standard-IA).**

Amazon EFS provides scalable and highly available file storage in the cloud. The Standard storage class is designed for frequently accessed data, making it suitable for the initial 30 days of frequent access.

You can create a lifecycle management policy for EFS that automatically transitions infrequently accessed files to the EFS Standard-Infrequent Access (EFS Standard-IA) storage class. This helps optimize costs by moving less frequently accessed data to a lower-cost storage tier.

</details>

### 67. gh-393

A payment processing company records all voice communication with its customers and stores the audio files in an Amazon S3 bucket. The company needs to capture the text from the audio files. The company must remove from the text any personally identifiable information (PII) that belongs to customers.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Configure an Amazon Transcribe transcription job with PII redaction turned on. When an audio file is uploaded to the S3 bucket, invoke an AWS Lambda function to start the transcription job. Store the output in a separate S3 bucket.**

Amazon Transcribe is a fully managed service provided by Amazon Web Services (AWS) that enables automatic speech recognition (ASR). It allows developers to convert spoken language into written text, making it useful for various applications such as transcription services, voice analytics, and content indexing.

</details>

### 68. gh-404

A company has deployed a serverless application that invokes an AWS Lambda function when new documents are uploaded to an Amazon S3 bucket. The application uses the Lambda function to process the documents. After a recent marketing campaign, the company noticed that the application did not process many of the documents.
What should a solutions architect do to improve the architecture of this application?

<details><summary>Answer</summary>

**D. Create an Amazon Simple Queue Service (Amazon SQS) queue. Send the requests to the queue. Configure the queue as an event source for Lambda.**

Introducing Amazon SQS as a queue allows for better decoupling between the S3 events and the document processing. This ensures that the Lambda function is not overwhelmed with spikes in incoming events, leading to missed document processing.

</details>

### 69. gh-407

A company is implementing a shared storage solution for a gaming application that is hosted in the AWS Cloud. The company needs the ability to use Lustre clients to access data. The solution must be fully managed.
Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Lustre file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Lustre: Amazon FSx for Lustre is a fully managed service that provides high-performance shared storage. It is specifically designed to be used with Lustre, making it a suitable solution for Lustre clients.

Fully Managed: Amazon FSx for Lustre is a fully managed service, meaning that AWS takes care of maintenance, updates, and other operational tasks, reducing the management overhead for the company.

</details>

### 70. gh-410

A company is deploying a new application on Amazon EC2 instances. The application writes data to Amazon Elastic Block Store (Amazon EBS) volumes. The company needs to ensure that all data that is written to the EBS volumes is encrypted at rest.
Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Create the EBS volumes as encrypted volumes. Attach the EBS volumes to the EC2 instances.**

By creating the EBS volumes as encrypted volumes, you ensure that all data written to those volumes is automatically encrypted. This provides a straightforward and effective solution for meeting the encryption-at-rest requirement.

</details>

### 71. gh-415

A company is storing petabytes of data in Amazon S3 Standard. The data is stored in multiple S3 buckets and is accessed with varying frequency. The company does not know access patterns for all the data. The company needs to implement a solution for each S3 bucket to optimize the cost of S3 usage.
Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**A. Create an S3 Lifecycle configuration with a rule to transition the objects in the S3 bucket to S3 Intelligent-Tiering.**

S3 Intelligent-Tiering: This storage class is designed to automatically and dynamically move objects between two access tiers – frequent and infrequent access – based on changing access patterns. It is a good fit for data with unknown or changing access patterns. It provides cost savings compared to S3 Standard while maintaining low-latency access to frequently accessed objects.

</details>

### 72. gh-421 `availability`

A company runs a highly available SFTP service. The SFTP service uses two Amazon EC2 Linux instances that run with elastic IP addresses to accept traffic from trusted IP sources on the internet. The SFTP service is backed by shared storage that is attached to the instances. User accounts are created and managed as Linux users in the SFTP servers.
The company wants a serverless option that provides high IOPS performance and highly configurable security. The company also wants to maintain control over user permissions.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an encrypted Amazon Elastic File System (Amazon EFS) volume. Create an AWS Transfer Family SFTP service with elastic IP addresses and a VPC endpoint that has internet-facing access. Attach a security group to the endpoint that allows only trusted IP addresses. Attach the EFS volume to the SFTP service endpoint. Grant users access to the SFTP service.**

</details>

### 73. gh-425 `cost`

A company uses high block storage capacity to runs its workloads on premises. The company's daily peak input and output transactions per second are not more than 15,000 IOPS. The company wants to migrate the workloads to Amazon EC2 and to provision disk performance independent of storage capacity.
Which Amazon Elastic Block Store (Amazon EBS) volume type will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. GP3 volume type**

General Purpose SSD (gp3) volumes are designed to provide a balance of price and performance. They allow you to provision IOPS independently of storage capacity, making them suitable for workloads with varying performance requirements. GP3 volumes offer a lower price per IOPS compared to io1 volumes and are a good fit for general-purpose workloads.

</details>

### 74. gh-426 `security`

A company needs to store data from its healthcare application. The application’s data frequently changes. A new regulation requires audit access at all levels of the stored data.
The company hosts the application on an on-premises infrastructure that is running out of storage capacity. A solutions architect must securely migrate the existing data to AWS while satisfying the new regulation.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Storage Gateway to move the existing data to Amazon S3. Use AWS CloudTrail to log data events for the S3 bucket.**

Explanation: CloudTrail management events don't capture object-level (data) access, so they can't satisfy "audit access at all levels of the stored data." CloudTrail data events, which log individual object-level API activity on the S3 bucket, are needed instead.

</details>

### 75. gh-430 `cost`

A manufacturing company has machine sensors that upload .csv files to an Amazon S3 bucket. These .csv files must be converted into images and must be made available as soon as possible for the automatic generation of graphical reports.
The images become irrelevant after 1 month, but the .csv files must be kept to train machine learning (ML) models twice a year. The ML trainings and audits are planned weeks in advance.
Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**B. Design an AWS Lambda function that converts the .csv files into images and stores the images in the S3 bucket. Invoke the Lambda function when a .csv file is uploaded. Most Voted**

C. Create S3 Lifecycle rules for .csv files and image files in the S3 bucket. Transition the .csv files from S3 Standard to S3 Glacier 1 day after they are uploaded. Expire the image files after 30 days.

</details>

### 76. gh-443

A company wants to host a scalable web application on AWS. The application will be accessed by users from different geographic regions of the world. Application users will be able to download and upload unique data up to gigabytes in size. The development team wants a cost-effective solution to minimize upload and download latency and maximize performance.
What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**A. Use Amazon S3 with Transfer Acceleration to host the application.**

</details>

### 77. gh-445

A company is storing 700 terabytes of data on a large network-attached storage (NAS) system in its corporate data center. The company has a hybrid environment with a 10 Gbps AWS Direct Connect connection.
After an audit from a regulator, the company has 90 days to move the data to the cloud. The company needs to move the data efficiently and without disruption. The company still needs to be able to access and update the data during the transfer window.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an AWS DataSync agent in the corporate data center. Create a data transfer task Start the transfer to an Amazon S3 bucket.**

using AWS DataSync, which is designed for efficiently transferring large amounts of data between on-premises storage and Amazon S3. It allows you to create data transfer tasks and initiate the transfer to an Amazon S3 bucket.

</details>

### 78. gh-446 `least-ops`

A company stores data in PDF format in an Amazon S3 bucket. The company must follow a legal requirement to retain all new and existing data in Amazon S3 for 7 years.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Turn on S3 Object Lock with compliance retention mode for the S3 bucket. Set the retention period to expire after 7 years. Use S3 Batch Operations to bring the existing data into compliance.**

</details>

### 79. gh-453

A company wants to implement a backup strategy for Amazon EC2 data and multiple Amazon S3 buckets. Because of regulatory requirements, the company must retain backup files for a specific time period. The company must not alter the files for the duration of the retention period.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Backup to create a backup vault that has a vault lock in compliance mode. Create the required backup plan.**

AWS Backup provides a centralized solution for managing backups across various AWS services, including Amazon EC2. By creating a backup vault with a vault lock in compliance mode, the company ensures that the backup files are retained and cannot be altered for the duration of the retention period. Compliance mode is designed to meet regulatory requirements for data retention.

</details>

### 80. gh-463 `cost`

An IoT company is releasing a mattress that has sensors to collect data about a user’s sleep. The sensors will send data to an Amazon S3 bucket. The sensors collect approximately 2 MB of data every night for each mattress. The company must process and summarize the data for each mattress. The results need to be available as soon as possible. Data processing will require 1 GB of memory and will finish within 30 seconds.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use AWS Lambda with a Python script**

AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It automatically scales with the number of requests, making it well-suited for event-driven workloads like processing data from IoT devices.

Python is a lightweight and efficient language for data processing tasks.

Lambda allows you to execute code in response to events, such as data arriving in the S3 bucket.

</details>

### 81. gh-465

A company is developing an application to support customer demands. The company wants to deploy the application on multiple Amazon EC2 Nitro-based instances within the same Availability Zone. The company also wants to give the application the ability to write to multiple block storage volumes in multiple EC2 Nitro-based instances simultaneously to achieve higher application availability.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Provisioned IOPS SSD (io2) EBS volumes with Amazon Elastic Block Store (Amazon EBS) Multi-Attach**

Provisioned IOPS SSD (io2) volumes do indeed support Multi-Attach, allowing you to attach a single volume to multiple Nitro-based instances in the same Availability Zone. This can be suitable for scenarios where multiple instances need simultaneous access to a shared volume with high performance.

</details>

### 82. gh-469

A company stores raw collected data in an Amazon S3 bucket. The data is used for several types of analytics on behalf of the company's customers. The type of analytics requested determines the access pattern on the S3 objects.
The company cannot predict or control the access pattern. The company wants to reduce its S3 costs.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use S3 Lifecycle rules to transition objects from S3 Standard to S3 Intelligent-Tiering**

S3 Intelligent-Tiering is designed to optimize costs by automatically moving objects between two access tiers: frequent and infrequent access. It is well-suited for scenarios where access patterns are unpredictable.
Using S3 Lifecycle rules to transition objects to S3 Intelligent-Tiering allows you to take advantage of automatic cost savings based on actual access patterns without the need for manual adjustments.

</details>

### 83. gh-475

A company is designing a containerized application that will use Amazon Elastic Container Service (Amazon ECS). The application needs to access a shared file system that is highly durable and can recover data to another AWS Region with a recovery point objective (RPO) of 8 hours. The file system needs to provide a mount target m each Availability Zone within a Region.
A solutions architect wants to use AWS Backup to manage the replication to another Region.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Amazon Elastic File System (Amazon EFS) with the Standard storage class**

</details>

### 84. gh-478 `security`

A law firm needs to share information with the public. The information includes hundreds of files that must be publicly readable. Modifications or deletions of the files by anyone before a designated future date are prohibited.
Which solution will meet these requirements in the MOST secure way?

<details><summary>Answer</summary>

**B. Create a new Amazon S3 bucket with S3 Versioning enabled. Use S3 Object Lock with a retention period in accordance with the designated date. Configure the S3 bucket for static website hosting. Set an S3 bucket policy to allow read-only access to the objects.**

S3 Versioning helps maintain multiple versions of an object over time. With S3 Object Lock, you can enforce retention periods during which the objects cannot be modified or deleted. This aligns with the requirement to prohibit modifications or deletions before a designated future date.

</details>

### 85. gh-482 `least-ops`

A company wants to migrate 100 GB of historical data from an on-premises location to an Amazon S3 bucket. The company has a 100 megabits per second (Mbps) internet connection on premises. The company needs to encrypt the data in transit to the S3 bucket. The company will store new data directly in Amazon S3.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS DataSync to migrate the data from the on-premises location to an S3 bucket**

AWS DataSync is a service designed for efficiently transferring large amounts of data between on-premises storage systems and Amazon S3.
It supports encryption of data in transit, ensuring the security of the data during the migration process.
AWS DataSync is specifically built for data transfer scenarios and minimizes operational overhead, providing an efficient and straightforward solution.

</details>

### 86. gh-485 `cost`

A company is looking for a solution that can store video archives in AWS from old news footage. The company needs to minimize costs and will rarely need to restore these files. When the files are needed, they must be available in a maximum of five minutes.
What is the MOST cost-effective solution?

<details><summary>Answer</summary>

**A. Store the video archives in Amazon S3 Glacier and use Expedited retrievals.**

</details>

### 87. gh-490

A gaming company uses Amazon DynamoDB to store user information such as geographic location, player data, and leaderboards. The company needs to configure continuous backups to an Amazon S3 bucket with a minimal amount of coding. The backups must not affect availability of the application and must not affect the read capacity units (RCUs) that are defined for the table.
Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Export the data directly from DynamoDB to Amazon S3 with continuous backups. Turn on point-in-time recovery for the table.**

</details>

### 88. gh-495

A company is conducting an internal audit. The company wants to ensure that the data in an Amazon S3 bucket that is associated with the company’s AWS Lake Formation data lake does not contain sensitive customer or employee data. The company wants to discover personally identifiable information (PII) or financial information, including passport numbers and credit card numbers.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure Amazon Macie to run a data discovery job that uses managed identifiers for the required data types.**

Amazon Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data like PII or financial information.
By configuring Amazon Macie to run a data discovery job, you can use managed identifiers to search for specific types of sensitive data within the S3 bucket.

</details>

### 89. gh-496

A company uses on-premises servers to host its applications. The company is running out of storage capacity. The applications use both block storage and NFS storage. The company needs a high-performing solution that supports local caching without re-architecting its existing applications.
Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Deploy an AWS Storage Gateway file gateway to replace NFS storage.**

D. Deploy an AWS Storage Gateway volume gateway to replace the block storage.

</details>

### 90. gh-497 `cost`

A company has a service that reads and writes large amounts of data from an Amazon S3 bucket in the same AWS Region. The service is deployed on Amazon EC2 instances within the private subnet of a VPC. The service communicates with Amazon S3 over a NAT gateway in the public subnet. However, the company wants a solution that will reduce the data output costs.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Provision a VPC gateway endpoint. Configure the route table for the private subnet to use the gateway endpoint as the route for all S3 traffic.**

</details>

### 91. gh-498 `least-ops`

A company uses Amazon S3 to store high-resolution pictures in an S3 bucket. To minimize application changes, the company stores the pictures as the latest version of an S3 object. The company needs to retain only the two most recent versions of the pictures.
The company wants to reduce costs. The company has identified the S3 bucket as a large expense.
Which solution will reduce the S3 costs with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use S3 Lifecycle to delete expired object versions and retain the two most recent versions.**

This approach allows you to automate the deletion of object versions based on lifecycle policies, reducing manual intervention and operational overhead.

</details>

### 92. gh-500

A company has multiple Windows file servers on premises. The company wants to migrate and consolidate its files into an Amazon FSx for Windows File Server file system. File permissions must be preserved to ensure that access rights do not change.
Which solutions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Deploy AWS DataSync agents on premises. Schedule DataSync tasks to transfer the data to the FSx for Windows File Server file system.**

D. Order an AWS Snowcone device. Connect the device to the on-premises network. Launch AWS DataSync agents on the device. Schedule DataSync tasks to transfer the data to the FSx for Windows File Server file system.

</details>

### 93. gh-501

A company wants to ingest customer payment data into the company's data lake in Amazon S3. The company receives payment data every minute on average. The company wants to analyze the payment data in real time. Then the company wants to ingest the data into the data lake.
Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**C. Use Amazon Kinesis Data Firehose to ingest data. Use Amazon Kinesis Data Analytics to analyze the data in real time.**

Amazon Kinesis Data Firehose:

It is a fully managed service that can reliably load streaming data into data lakes, data stores, and analytics tools.
It can automatically scale to handle varying data throughput.
It simplifies the data delivery process, making it easy to ingest data into Amazon S3.

Amazon Kinesis Data Analytics:

It enables you to analyze streaming data in real-time with SQL queries.
It integrates seamlessly with other AWS services, including Kinesis Data Firehose.
It provides the capability to perform real-time analytics on the streaming data before storing it in Amazon S3.

</details>

### 94. gh-506

A social media company is building a feature for its website. The feature will give users the ability to upload photos. The company expects significant increases in demand during large events and must ensure that the website can handle the upload traffic from users.
Which solution meets these requirements with the MOST scalability?

<details><summary>Answer</summary>

**C. Generate Amazon S3 presigned URLs in the application. Upload files directly from the user's browser into an S3 bucket.**

Amazon S3 Presigned URLs: This approach allows the client (user's browser) to directly upload files to Amazon S3 using a presigned URL generated by the server. This offloads the file transfer process from the application servers and enables a direct upload to S3 from the client side.

</details>

### 95. gh-512 `least-ops`

A company uses AWS Organizations with resources tagged by account. The company also uses AWS Backup to back up its AWS infrastructure resources. The company needs to back up all AWS resources.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Config to identify all untagged resources. Tag the identified resources programmatically. Use tags in the backup plan.**

AWS Config can be used to identify untagged resources, and it can provide a comprehensive view of the resource inventory across your AWS Organization. 
AWS Backup supports the use of tags in backup plans. By utilizing tags, you can create a backup plan that automatically includes resources based on their tags.

</details>

### 96. gh-513 `availability`

A social media company wants to allow its users to upload images in an application that is hosted in the AWS Cloud. The company needs a solution that automatically resizes the images so that the images can be displayed on multiple device types. The application experiences unpredictable traffic patterns throughout the day. The company is seeking a highly available solution that maximizes scalability.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Create a static website hosted in Amazon S3 that invokes AWS Lambda functions to resize the images and store the images in an Amazon S3 bucket.**

Hosting a static website in Amazon S3 is a cost-effective and highly available solution. Amazon S3 provides scalable and durable object storage.
A static website in S3 can serve as the front end for user interactions.
In this option, Lambda functions can be triggered by events (e.g., new image uploads to an S3 bucket) to perform image resizing. Lambda can efficiently handle sporadic and unpredictable workloads.

</details>

### 97. gh-517

A company wants to send all AWS Systems Manager Session Manager logs to an Amazon S3 bucket for archival purposes.
Which solution will meet this requirement with the MOST operational efficiency?

<details><summary>Answer</summary>

**A. Enable S3 logging in the Systems Manager console. Choose an S3 bucket to send the session data to.**

While AWS Systems Manager supports logging command output to an S3 bucket, this is primarily for storing the output of commands executed through Systems Manager, not specifically for Session Manager logs.
It may not capture all the detailed session logs, including interactive session input/output and other session-specific details.

</details>

### 98. gh-534 `cost` `availability`

A company wants to build a logging solution for its multiple AWS accounts. The company currently stores the logs from all accounts in a centralized account. The company has created an Amazon S3 bucket in the centralized account to store the VPC flow logs and AWS CloudTrail logs. All logs must be highly available for 30 days for frequent analysis, retained for an additional 60 days for backup purposes, and deleted 90 days after creation.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Transition objects to the S3 Standard-Infrequent Access (S3 Standard-IA) storage class 30 days after creation. Move all objects to the S3 Glacier Flexible Retrieval storage class after 90 days. Write an expiration action that directs Amazon S3 to delete objects after 90 days.**

</details>

### 99. gh-542

A media company uses an Amazon CloudFront distribution to deliver content over the internet. The company wants only premium customers to have access to the media streams and file content. The company stores all content in an Amazon S3 bucket. The company also delivers content on demand to customers for a specific purpose, such as movie rentals or music downloads.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Generate and provide CloudFront signed URLs to premium customers.**

This solution involves generating signed URLs for the content, which allows access only to those who have the appropriate permissions. Signed URLs can be time-limited, and you can define custom policies specifying who can access the content and for how long.

</details>

### 100. gh-546

A recent analysis of a company's IT expenses highlights the need to reduce backup costs. The company's chief information officer wants to simplify the on-premises backup infrastructure and reduce costs by eliminating the use of physical backup tapes. The company must preserve the existing investment in the on-premises backup applications and workflows.
What should a solutions architect recommend?

<details><summary>Answer</summary>

**D. Set up AWS Storage Gateway to connect with the backup applications using the iSCSI-virtual tape library (VTL) interface.**

AWS Storage Gateway provides a hybrid cloud storage service that enables on-premises applications to seamlessly use cloud storage.
The iSCSI-virtual tape library (VTL) interface of AWS Storage Gateway is designed to integrate with existing backup applications that use tape-based workflows. It emulates a tape library, allowing you to store virtual tapes in Amazon S3 or Glacier, providing a cost-effective and scalable alternative to physical tapes.

</details>

### 101. gh-547 `least-ops`

A company has data collection sensors at different locations. The data collection sensors stream a high volume of data to the company. The company wants to design a platform on AWS to ingest and process high-volume streaming data. The solution must be scalable and support data collection in near real time. The company must store the data in Amazon S3 for future reporting.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Firehose to deliver streaming data to Amazon S3.**

Amazon Kinesis Data Firehose: It is a fully managed service for ingesting, transforming, and delivering streaming data to various destinations, including Amazon S3. Kinesis Data Firehose can scale automatically based on the volume of incoming data, and it simplifies the process of delivering data to S3 without the need for manual intervention.

</details>

### 102. gh-557

A solutions architect manages an analytics application. The application stores large amounts of semistructured data in an Amazon S3 bucket. The solutions architect wants to use parallel data processing to process the data more quickly. The solutions architect also wants to use information that is stored in an Amazon Redshift database to enrich the data.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon EMR to process the S3 data. Use Amazon EMR with the Amazon Redshift data to enrich the S3 data.**

B. Amazon EMR is a cloud-based big data platform that uses Apache Hadoop and other open-source frameworks to process and analyze large datasets. EMR supports parallel data processing, making it a good fit for the requirement. Additionally, using EMR with the Amazon Redshift data allows for efficient enrichment of the S3 data.

</details>

### 103. gh-566

A company runs multiple Amazon EC2 Linux instances in a VPC across two Availability Zones. The instances host applications that use a hierarchical directory structure. The applications need to read and write rapidly and concurrently to shared storage.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create an Amazon Elastic File System (Amazon EFS) file system. Mount the EFS file system from each EC2 instance.**

Amazon EFS is a fully managed, scalable file storage service designed to provide shared access to files across multiple Amazon EC2 instances. It is particularly well-suited for use cases that require concurrent access from multiple instances.

</details>

### 104. gh-568

A solutions architect is designing the storage architecture for a new web application used for storing and viewing engineering drawings. All application components will be deployed on the AWS infrastructure.
The application design must support caching to minimize the amount of time that users wait for the engineering drawings to load. The application must be able to store petabytes of data.
Which combination of storage and caching should the solutions architect use?

<details><summary>Answer</summary>

**A. Amazon S3 with Amazon CloudFront**

It is suitable for storing petabytes of data and is designed to provide low-latency access.
Amazon CloudFront is a content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds. By integrating CloudFront with S3, you can distribute the engineering drawings to edge locations worldwide, reducing the latency for users and improving load times.

</details>

### 105. gh-580 `cost`

A company uses locally attached storage to run a latency-sensitive application on premises. The company is using a lift and shift method to move the application to the AWS Cloud. The company does not want to change the application architecture.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Host the application on an Amazon EC2 instance. Use an Amazon Elastic Block Store (Amazon EBS) GP3 volume to run the application.**

Amazon EC2 Instance with GP3 Volume (Option D): Amazon EBS GP3 volumes are designed to provide cost savings compared to GP2 volumes while still offering good performance for a broad range of workloads. GP3 volumes allow you to provision the IOPS (input/output operations per second) and throughput that your application needs, giving you flexibility and cost-effectiveness.

</details>

### 106. gh-583 `cost`

A company has 5 PB of archived data on physical tapes. The company needs to preserve the data on the tapes for another 10 years for compliance purposes. The company wants to migrate to AWS in the next 6 months. The data center that stores the tapes has a 1 Gbps uplink internet connectivity.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Order multiple AWS Snowball devices that have Tape Gateway. Copy the physical tapes to virtual tapes in Snowball. Ship the Snowball devices to AWS. Create a lifecycle policy to move the tapes to Amazon S3 Glacier Deep Archive.**

AWS Snowball devices can be more cost-effective than transferring large amounts of data over a 1 Gbps internet connection, especially when dealing with petabytes of data. 
AWS, a lifecycle policy can be configured to move the data to Amazon S3 Glacier Deep Archive, which is a cost-effective storage class designed for long-term archival.

</details>

### 107. gh-592

A company uses AWS and sells access to copyrighted images. The company’s global customer base needs to be able to access these images quickly. The company must deny access to users from specific countries. The company wants to minimize costs as much as possible.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon S3 to store the images. Use Amazon CloudFront to distribute the images with geographic restrictions. Provide a signed URL for each customer to access the data in CloudFront.**

By using CloudFront, you can cache and serve the images from edge locations around the world, improving access speed for global customers.
Geographic Restrictions in CloudFront: CloudFront allows you to set up geographic restrictions to deny access to users from specific countries.

</details>

### 108. gh-602

A company's infrastructure consists of hundreds of Amazon EC2 instances that use Amazon Elastic Block Store (Amazon EBS) storage. A solutions architect must ensure that every EC2 instance can be recovered after a disaster.
What should the solutions architect do to meet this requirement with the LEAST amount of effort?

<details><summary>Answer</summary>

**C. Use AWS Backup to set up a backup plan for the entire group of EC2 instances. Use the AWS Backup API or the AWS CLI to speed up the restore process for multiple EC2 instances.**

AWS Backup: AWS Backup is a fully managed backup service that centralizes and automates the backup of data across AWS services. 
Backup Plan: You can set up a backup plan in AWS Backup to create and manage backups of the entire group of EC2 instances. 
AWS Backup provides a streamlined process for restoring data. You can use the AWS Backup console, API, or AWS CLI to initiate the restore process for multiple EC2 instances.

</details>

### 109. gh-603

A company recently migrated to the AWS Cloud. The company wants a serverless solution for large-scale parallel on-demand processing of a semistructured dataset. The data consists of logs, media files, sales transactions, and IoT sensor data that is stored in Amazon S3. The company wants the solution to process thousands of items in the dataset in parallel.
Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**B. Use the AWS Step Functions Map state in Distributed mode to process the data in parallel.**

The Map state in AWS Step Functions is designed for parallel processing. In Distributed mode, it efficiently processes items in parallel, providing a scalable solution. This allows you to process thousands of items concurrently, achieving high throughput.

</details>

### 110. gh-604

A company will migrate 10 PB of data to Amazon S3 in 6 weeks. The current data center has a 500 Mbps uplink to the internet. Other on-premises applications share the uplink. The company can use 80% of the internet bandwidth for this one-time migration task.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Order multiple AWS Snowball devices. Copy the data to the devices. Send the devices to AWS to copy the data to Amazon S3.**

With only a 500 Mbps uplink bandwidth shared among other on-premises applications, transferring 10 PB of data over the internet would be impractical and time-consuming. AWS Snowball provides a physical device that can be shipped to the company to facilitate faster initial data transfer.

</details>

### 111. gh-605

A company has several on-premises Internet Small Computer Systems Interface (ISCSI) network storage servers. The company wants to reduce the number of these servers by moving to the AWS Cloud. A solutions architect must provide low-latency access to frequently used data and reduce the dependency on on-premises servers with a minimal number of infrastructure changes.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Deploy an AWS Storage Gateway volume gateway that is configured with cached volumes.**

A volume gateway with cached volumes is a good fit when you want to keep frequently accessed data on-premises for low-latency access while still having a copy in the AWS Cloud. Cached volumes store the entire dataset in Amazon S3 while retaining the most frequently accessed data locally.

</details>

### 112. gh-609 `least-ops`

A company is building a data analysis platform on AWS by using AWS Lake Formation. The platform will ingest data from different sources such as Amazon S3 and Amazon RDS. The company needs a secure solution to prevent access to portions of the data that contain sensitive information.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create data filters to implement row-level security and cell-level security.**

AWS Lake Formation allows you to create data filters that can be used for row-level security and cell-level security.

</details>

### 113. gh-616

A company has deployed its newest product on AWS. The product runs in an Auto Scaling group behind a Network Load Balancer. The company stores the product’s objects in an Amazon S3 bucket.
The company recently experienced malicious attacks against its systems. The company needs a solution that continuously monitors for malicious activity in the AWS account, workloads, and access patterns to the S3 bucket. The solution must also report suspicious activity and display the information on a dashboard.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure Amazon GuardDuty to monitor and report findings to AWS Security Hub.**

Amazon GuardDuty:

GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior in your AWS account. It analyzes events, such as API calls and network traffic, to detect potentially malicious activity.
AWS Security Hub:
AWS Security Hub is a comprehensive security service that aggregates and prioritizes security findings from various AWS services, including GuardDuty. It provides a centralized dashboard for security alerts and findings.

</details>

### 114. gh-617 `cost`

A company wants to migrate an on-premises data center to AWS. The data center hosts a storage server that stores data in an NFS-based file system. The storage server holds 200 GB of data. The company needs to migrate the data without interruption to existing services. Multiple resources in AWS must be able to access the data by using the NFS protocol.
Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon Elastic File System (Amazon EFS) file system.**

E. Install an AWS DataSync agent in the on-premises data center. Use a DataSync task between the on-premises location and AWS.

Amazon EFS is a scalable, fully managed file system that supports the NFSv4 protocol. It is designed to be highly available and can be mounted on multiple EC2 instances concurrently.
Creating an Amazon EFS file system allows you to easily migrate the data and have multiple AWS resources access it concurrently.
AWS DataSync is a service for efficiently transferring large amounts of data between on-premises storage and AWS. By installing a DataSync agent in the on-premises data center, you can use DataSync to perform the migration task.
DataSync ensures efficient and secure transfer of data, making it suitable for migrating large amounts of data to AWS.

</details>

### 115. gh-618

A company wants to use Amazon FSx for Windows File Server for its Amazon EC2 instances that have an SMB file share mounted as a volume in the us-east-1 Region. The company has a recovery point objective (RPO) of 5 minutes for planned system maintenance or unplanned service disruptions. The company needs to replicate the file system to the us-west-2 Region. The replicated data must not be deleted by any user for 5 years.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create an FSx for Windows File Server file system in us-east-1 that has a Multi-AZ deployment type. Use AWS Backup to create a daily backup plan that includes a backup rule that copies the backup to us-west-2. Configure AWS Backup Vault Lock in compliance mode for a target vault in us-west-2. Configure a minimum duration of 5 years.**

FSx for Windows File Server:
Create an FSx for Windows File Server file system in the us-east-1 Region with a Multi-AZ deployment type. The Multi-AZ deployment type ensures high availability.
AWS Backup:
Use AWS Backup to create a daily backup plan for the FSx file system. Include a backup rule that copies the backup to the us-west-2 Region. This ensures that a backup is replicated to the us-west-2 Region regularly.

</details>

### 116. gh-620

A company is planning to deploy a business-critical application in the AWS Cloud. The application requires durable storage with consistent, low-latency performance.
Which type of storage should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Provisioned IOPS SSD Amazon Elastic Block Store (Amazon EBS) volume**

Provisioned IOPS (Input/Output Operations Per Second) SSD volumes are designed to deliver predictable, consistent, and low-latency performance for critical applications.
These volumes allow you to specify the amount of IOPS you need, providing a consistent level of performance regardless of the volume size.

</details>

### 117. gh-621

An online photo-sharing company stores its photos in an Amazon S3 bucket that exists in the us-west-1 Region. The company needs to store a copy of all new photos in the us-east-1 Region.
Which solution will meet this requirement with the LEAST operational effort?

<details><summary>Answer</summary>

**A. Create a second S3 bucket in us-east-1. Use S3 Cross-Region Replication to copy photos from the existing S3 bucket to the second S3 bucket.**

S3 Cross-Region Replication (CRR) is designed specifically for replicating objects across different AWS regions. It is a fully managed feature that automatically replicates objects from the source bucket to the destination bucket in a different region. This requires minimal operational effort as it is a built-in S3 feature for cross-region replication, and you don't have to manually trigger actions or configure additional services.

</details>

### 118. gh-626

A company stores its data on premises. The amount of data is growing beyond the company's available capacity.
The company wants to migrate its data from the on-premises location to an Amazon S3 bucket. The company needs a solution that will automatically validate the integrity of the data after the transfer.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an AWS DataSync agent on premises. Configure the DataSync agent to perform the online data transfer to an S3 bucket.**

AWS DataSync is a service designed for fast and secure online data transfer between on-premises storage and Amazon S3, Amazon EFS, or Amazon FSx for Windows File Server.
DataSync automatically performs integrity validation by ensuring that the data transferred to S3 matches the source data. It uses checksums to validate the integrity of the files.

</details>

### 119. gh-632

A company is creating a new application that will store a large amount of data. The data will be analyzed hourly and will be modified by several Amazon EC2 Linux instances that are deployed across multiple Availability Zones. The needed amount of storage space will continue to grow for the next 6 months.
Which storage solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Store the data in an Amazon Elastic File System (Amazon EFS) file system. Mount the file system on the application instances.**

Amazon EFS is a scalable and fully managed file storage service that can be mounted on multiple Amazon EC2 instances simultaneously. It provides a shared file system that can be accessed concurrently from different instances.Amazon EFS can automatically scale its file system capacity to accommodate growing data sets. It can handle a large amount of data and is designed to grow and shrink as needed.

</details>

### 120. gh-634

A company collects 10 GB of telemetry data daily from various machines. The company stores the data in an Amazon S3 bucket in a source data account.
The company has hired several consulting agencies to use this data for analysis. Each agency needs read access to the data for its analysts. The company must share the data from the source data account by choosing a solution that maximizes security and operational efficiency.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure cross-account access for the S3 bucket to the accounts that the agencies own.**

By configuring cross-account access, you can grant permissions to specific AWS accounts (owned by the consulting agencies) to access the S3 bucket. This allows you to share the data securely with the agencies without making the data public or creating additional IAM users in the source data account.

</details>

### 121. gh-646

solutions architect needs to host a high performance computing (HPC) workload in the AWS Cloud. The workload will run on hundreds of Amazon EC2 instances and will require parallel access to a shared file system to enable distributed processing of large datasets. Datasets will be accessed across multiple instances simultaneously. The workload requires access latency within 1 ms. After processing has completed, engineers will need access to the dataset for manual postprocessing.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon FSx for Lustre as a shared file system. Link the file system to an Amazon S3 bucket for postprocessing.**

FSx for Lustre is designed for high-performance computing workloads that require fast and scalable shared storage. It provides low-latency access to data and is well-suited for parallel processing across multiple instances.

</details>

### 122. gh-648 `availability`

A weather forecasting company needs to process hundreds of gigabytes of data with sub-millisecond latency. The company has a high performance computing (HPC) environment in its data center and wants to expand its forecasting capabilities.
A solutions architect must identify a highly available cloud storage solution that can handle large amounts of sustained throughput. Files that are stored in the solution should be accessible to thousands of compute instances that will simultaneously access and process the entire dataset.
What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon FSx for Lustre persistent file systems.**

Persistent file systems in FSx for Lustre are designed for longer-term storage needs. They provide a durable and highly available solution for your data. This is important for the weather forecasting company's requirement to handle large amounts of sustained throughput.

</details>

### 123. gh-651

A company stores a large volume of image files in an Amazon S3 bucket. The images need to be readily available for the first 180 days. The images are infrequently accessed for the next 180 days. After 360 days, the images need to be archived but must be available instantly upon request. After 5 years, only auditors can access the images. The auditors must be able to retrieve the images within 12 hours. The images cannot be lost during this process.

<details><summary>Answer</summary>

**C. Transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 180 days, S3 Glacier Instant Retrieval after 360 days, and S3 Glacier Deep Archive after 5 years.**

Explanation:
S3 Standard-IA (instead of One Zone-IA) ensures high durability across multiple AZs for infrequent access.
Glacier Instant Retrieval meets the "instant availability" requirement after 360 days, while Glacier Deep Archive is cost-effective for audits after 5 years.
(Option A/B use less durable One Zone-IA, and Option D uses slower Glacier Flexible Retrieval, which violates the "instant" requirement.)

Answer: C) Configure the General Purpose SSD (gp3) EBS volume storage type and provision 15,000 IOPS.
gp3 allows independent provisioning of IOPS (unlike gp2) and is more cost-effective than io1 for 15,000 IOPS.
Magnetic volumes (Option D) are outdated and cannot meet the performance requirement.

</details>

### 124. gh-659 `security`

A company is relocating its data center and wants to securely transfer 50 TB of data to AWS within 2 weeks. The existing data center has a Site-to-
Site VPN connection to AWS that is 90% utilized.
Which AWS service should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**Answer: C) Use AWS Snowball Edge Storage Optimized.**

Snowball Edge is ideal for large offline transfers (50 TB in 2 weeks) without VPN bottlenecks.
DataSync (Option A) is for online transfers; Direct Connect (Option B) is too slow.

</details>

### 125. gh-667 `security`

A company is moving its data and applications to AWS during a multiyear migration project. The company wants to securely access data on
Amazon S3 from the company's AWS Region and from the company's on-premises location. The data must not traverse the internet. The company
has established an AWS Direct Connect connection between its Region and its on-premises location.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: A) Create S3 gateway endpoints.**

Gateway endpoints allow secure S3 access via Direct Connect/VPC without internet.
Interface endpoints (Option C) are for private-link services, not S3.

</details>

### 126. gh-673

A company runs an SMB le server in its data center. The le server stores large les that the company frequently accesses for up to 7 days after
the le creation date. After 7 days, the company needs to be able to access the les with a maximum retrieval time of 24 hours.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use S3 File Gateway + Lifecycle policy to Glacier Deep Archive.**

File Gateway extends on-prem storage; Glacier Deep Archive is cost-effective for archives.
DataSync (Option A) doesn’t automate tiering.

</details>

### 127. gh-675

A company uses Amazon EC2 instances and Amazon Elastic Block Store (Amazon EBS) volumes to run an application. The company creates one
snapshot of each EBS volume every day to meet compliance requirements. The company wants to implement an architecture that prevents the
accidental deletion of EBS volume snapshots. The solution must not change the administrative rights of the storage administrator user.
Which solution will meet these requirements with the LEAST administrative effort?

<details><summary>Answer</summary>

**Answer: D) Lock the EBS snapshots.**

Prevents accidental deletion without IAM changes.
Recycle Bin (Option C) requires tagging; IAM (Option B) changes permissions.

</details>

### 128. gh-680 `least-ops`

A solutions architect needs to copy les from an Amazon S3 bucket to an Amazon Elastic File System (Amazon EFS) le system and another S3
bucket. The les must be copied continuously. New les are added to the original S3 bucket consistently. The copied les should be overwritten
only if the source le changes.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Answer: A) Use DataSync with "changed data only" mode.**

Continuously syncs only modified files to S3/EFS.
Lambda (Option B) requires custom code; full syncs (Option C) are inefficient.

</details>

### 129. gh-681 `least-ops`

A company uses Amazon EC2 instances and stores data on Amazon Elastic Block Store (Amazon EBS) volumes. The company must ensure that
all data is encrypted at rest by using AWS Key Management Service (AWS KMS). The company must be able to control rotation of the encryption
keys.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Answer: A) Use customer-managed KMS keys for EBS encryption.**

Allows control over key rotation. AWS-managed keys (Option B) limit rotation flexibility.

</details>
