# Storage — S3, EBS, EFS, FSx, archive, transfer

412 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-1

Which set of Amazon S3 features helps to prevent and recover from accidental data loss?

<details><summary>Answer</summary>

**B. Object versioning and Multi-factor authentication.**

</details>

### 2. et-2 `least-ops`

A company needs the ability to analyze the log files of its proprietary application. The logs are stored in JSON format in an Amazon S3 bucket. Queries will be simple and will run on-demand. A solutions architect needs to perform the analysis with minimal changes to the existing architecture. What should the solutions architect do to meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Use Amazon Athena directly with Amazon S3 to run the queries as needed.**

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

### 4. et-3 `least-ops`

A company uses AWS Organizations to manage multiple AWS accounts for different departments. The management account has an Amazon S3 bucket that contains project reports. The company wants to limit access to this S3 bucket to only users of accounts within the organization in AWS Organizations. Which solution meets these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**A. Add the aws PrincipalOrgID global condition key with a reference to the organization ID to the S3 bucket policy.**

aws:PrincipalOrgID – Simplifies specifying the Principal element in a resource-based policy. This global key provides an alternative to listing all the account IDs for all AWS accounts in an organization. Instead of listing all of the accounts that are members of an organization, you can specify the organization ID in the Condition element. proposes adding the aws PrincipalOrgID global condition key with a reference to the organization ID to the S3 bucket policy. This would limit access to the S3 bucket to only users of accounts within the organization in AWS Organizations, as the aws PrincipalOrgID condition key can check if the request is coming from within the organization.

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

### 6. dt-4 `availability`

Your website is serving on-demand training videos to your workforce. Videos are uploaded monthly in high resolution MP4 format. Your workforce is distributed globally often on the move and using company-provided tablets that require the HTTP Live Streaming (HLS) protocol to watch a video. Your company has no video transcoding expertise and it required you may need to pay for a consultant. How do you implement the most cost-efficient architecture without compromising high availability and quality of video delivery?

<details><summary>Answer</summary>

**C. Elastic Transcoder to transcode original high-resolution MP4 videos to HLS. S3 to host videos with Lifecycle Management to archive original files to Glacier after a few days. CloudFront to serve HLS transcoded videos from S3.**

</details>

### 7. et-5

A company is hosting a web application on AWS using a single Amazon EC2 instance that stores user-uploaded documents in an Amazon EBS volume. For better scalability and availability, the company duplicated the architecture and created a second EC2 instance and EBS volume in another Availability Zone, placing both behind an Application Load Balancer. After completing this change, users reported that, each time they refreshed the website, they could see one subset of their documents or the other, but never all of the documents at the same time. What should a solutions architect propose to ensure users see all of their documents at once?

<details><summary>Answer</summary>

**C. Copy the data from both EBS volumes to Amazon EFS. Modify the application to save new documents to Amazon EFS**

Option C, which involves copying the data to Amazon EFS and modifying the application to use Amazon EFS for document storage, is the most appropriate solution to ensure users can see all their documents at once in the duplicated architecture. Amazon EFS provides scalability, availability, and shared access, allowing both EC2 instances to access and synchronize the documents seamlessly. Unlike EBS volumes or snapshots, which cannot be shared in real time across multiple instances and Availability Zones, Amazon EFS allows both EC2 instances to access the same file system simultaneously, ensuring all users see the same set of documents regardless of which instance serves their request.

</details>

### 8. dt-6

Which of the following are valid statements about Amazon S3? (Choose 2 answers)

<details><summary>Answer</summary>

**C. A successful response to a PUT request only occurs when a complete object is saved.; E. S3 provides eventual consistency for overwrite PUTS and DELETE.**

</details>

### 9. et-6

A company uses NFS to store large video files in on-premises network attached storage. Each video file ranges in size from 1 MB to 500 GB. The total storage is 70 TB and is no longer growing. The company decides to migrate the video files to Amazon S3. The company must migrate the video files as soon as possible while using the least possible network bandwidth. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an AWS Snowball Edge job. Receive a Snowball Edge device on premises. Use the Snowball Edge client to transfer data to the device. Return the device so that AWS can import the data into Amazon S3.**

On a Snowball Edge device you can copy files with a speed of up to 100Gbps. 70TB will take around 5600 seconds, so very quickly, less than 2 hours. The downside is that it'll take between 4-6 working days to receive the device and then another 2-3 working days to send it back and for AWS to move the data onto S3 once it reaches them. Total time: 6-9 working days. Bandwidth used: 0.

</details>

### 10. wl-8

You are planning to build a fleet of EBS-optimized EC2 instances for your new application. Due to security compliance, your organization wants you to encrypt root volume which is used to boot the instances. How can this be achieved?

<details><summary>Answer</summary>

**A. Select the Encryption option for the root EBS volume while launching the EC2 instance.**

Root volume encryption is set at launch time: the root device in the block device mapping accepts an Encrypted setting together with a KMS key, and the console presents this as an encryption option on the volume. Turning on 'EBS encryption by default' for the account in a Region does the same thing fleet-wide, so every new volume and snapshot is encrypted without per-launch settings - the better fit for an organisation-wide compliance rule. Option B is impossible, because an existing unencrypted EBS volume cannot be encrypted in place; the only route is snapshot, copy with encryption, then restore. Option C is simply false, and option D describes the pre-2019 workaround, which still works but is needless extra effort today.

</details>

### 11. ce-10

A company plans to rehost an application to Amazon EC2 instances that use Amazon Elastic Block Store (Amazon EBS) as the attached storage A solutions architect must design a solution to ensure that all newly created Amazon EBS volumes are encrypted by default. The solution must also prevent the creation of unencrypted EBS volumes Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure the EC2 account attributes to always encrypt new EBS volumes.**

The most direct and effective method to meet the requirements is to enable "EBS encryption by default" for the AWS account on a per-region basis. This feature ensures that any new EBS volume created in that region is automatically encrypted at rest, without requiring any user action during creation. It also applies to snapshot copies. This setting acts as a preventive control, effectively blocking the creation of unencrypted volumes within the specified region and enforcing the company's security policy seamlessly. Why Incorrect Options are Wrong: B: AWS Config is a detective control service. It can identify unencrypted volumes after they have been created but cannot prevent their creation, which is a key requirement. C: This describes a complex and inefficient remediation process. The goal is to prevent unencrypted volumes from being created in the first place, not to fix them after the

</details>

### 12. wl-12

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

### 13. dt-13 `availability`

Content and Media Server is the latest requirement that you need to meet for a client. The client has been very specific about his requirements such as low latency, high availability, durability, and access control. Potentially there will be millions of views on this server and because of 'spiky' usage patterns, operations teams will need to provision static hardware, network, and management resources to support the maximum expected need. The Customer base will be initially low but is expected to grow and become more geographically distributed. Which of the following would be a good solution for content distribution?

<details><summary>Answer</summary>

**D. Amazon S3 as the origin server and Amazon CloudFront for caching.**

</details>

### 14. ce-15

A global company runs its workloads on AWS The company's application uses Amazon S3 buckets across AWS Regions for sensitive data storage and analysis. The company stores millions of objects in multiple S3 buckets daily. The company wants to identify all S3 buckets that are not versioning- enabled. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon S3 Storage Lens to identify all S3 buckets that are not versioning-enabled across Regions.**

Amazon S3 Storage Lens is the most suitable service for this requirement. It is an analytics feature designed to provide organization-wide visibility into object storage usage, activity trends, and data protection status. S3 Storage Lens aggregates metrics for all S3 buckets across all Regions within an AWS account or an entire AWS Organization. It includes specific data protection metrics that track the percentage of buckets with versioning enabled, allowing the company to easily identify all buckets where versioning is not enabled through its interactive dashboard or metrics export. Why Incorrect Options are Wrong: A. AWS CloudTrail records API activity. While it logs the PutBucketVersioning API call, it is not an efficient tool for auditing the current configuration state of all existing buckets across an organization. C. IAM Access Analyzer for S3 is a security tool that identifies S

</details>

### 15. wl-15

You will be launching and terminating EC2 instances on a need basis for your workloads. You need to run some shell scripts and perform certain checks connecting to the AWS S3 bucket when the instance is getting launched. Which of the following options will allow performing any tasks during launch? (choose multiple)

<details><summary>Answer</summary>

**A. Use Instance user data for shell scripts.; C. Use AutoScaling Group lifecycle hooks and trigger AWS Lambda function**

Option A is correct.
Option C is correct.
https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html#prepari
ng-for-notification

</details>

### 16. ce-16

A media company uses an Amazon CloudFront distribution to deliver content over the internet The company wants only premium customers to have access to the media streams and file content. The company stores all content in an Amazon S3 bucket. The company also delivers content on demand to customers for a specific purpose, such as movie rentals or music downloads. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Generate and provide CloudFront signed URLs to premium customers.**

The requirement is to restrict access to media content served via CloudFront to specific "premium" users, particularly for on-demand downloads like movie rentals. CloudFront signed URLs are the ideal solution for this use case. A signed URL is a special URL that includes additional information, such as an expiration time, to grant temporary access to a specific file. The application can generate these unique, short-lived URLs for authenticated premium customers, ensuring that only they can download the specific content for the allowed duration. This directly addresses the need to control access to individual files on demand. Why Incorrect Options are Wrong: A. S3 does not use signed cookies; this is a feature of CloudFront. S3 provides signed URLs to grant direct, time-limited access to objects, but not signed cookies. C. Origin access control (OAC) is used to restrict direct access to t

</details>

### 17. et-17

A company is implementing a new business application. The application runs on two Amazon EC2 instances and uses an Amazon S3 bucket for document storage. A solutions architect needs to ensure that the EC2 instances can access the S3 bucket. What should the solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Create an IAM role that grants access to the S3 bucket. Attach the role to the EC2 instances.**

An IAM role is an AWS resource that allows you to delegate access to AWS resources and services. You can create an IAM role that grants access to the S3 bucket and then attach the role to the EC2 instances. This will allow the EC2 instances to access the S3 bucket and the documents stored within it.

</details>

### 18. dt-18

Which of the following services natively encrypts data at rest within an AWS region? (Choose 2 answers)

<details><summary>Answer</summary>

**A. AWS Storage Gateway.; D. Amazon Glacier.**

</details>

### 19. dt-19

Which one of the following can't be used as an origin server with Amazon CloudFront?

<details><summary>Answer</summary>

**C. Amazon Glacier.**

</details>

### 20. ce-22 `least-ops` `security`

A company hosts its application on several Amazon EC2 instances inside a VPC. The company creates a dedicated Amazon S3 bucket for each customer to store their relevant information in Amazon S3. The company wants to ensure that the application running on EC2 instances can securely access only the S3 buckets that belong to the company's AWS account. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create a gateway endpoint for Amazon S3 that is attached to the VPC Update the IAM instance profile policy to provide access to only the specific buckets that the application needs.**

This solution correctly addresses both secure connectivity and granular access control with minimal operational overhead. A gateway VPC endpoint for Amazon S3 allows EC2 instances to access S3 using private IP addresses, keeping traffic within the AWS network and avoiding the public internet. This is more secure and cost-effective than using a NAT gateway. An IAM instance profile attached to the EC2 instances is the standard method for granting permissions. The associated IAM policy can be configured to grant access only to specific S3 buckets, enforcing the principle of least privilege. By using wildcards in the bucket ARN (e.g., arn:aws:s3:::company-customer-), the policy can automatically apply to new customer buckets without modification, thus ensuring low operational overhead. Why Incorrect Options are Wrong: B: A NAT gateway routes traffic over the public internet to reach S3, whic

</details>

### 21. dt-25

Just when you thought you knew every possible storage option on AWS you hear someone mention Reduced Redundancy Storage (RRS) within Amazon S3. What is the ideal scenario to use Reduced Redundancy Storage (RRS)?

<details><summary>Answer</summary>

**C. Non-critical or reproducible data.**

</details>

### 22. ce-26 `least-ops`

A company uses Amazon EC2 instances and stores data on Amazon Elastic Block Store (Amazon EBS) volumes. The company must ensure that all data is encrypted at rest by using AWS Key Management Service (AWS KMS). The company must be able to control rotation of the encryption keys. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create a customer managed key Use the key to encrypt the EBS volumes.**

The solution requires using AWS KMS for EBS encryption where the company can control key rotation with the least operational overhead. A customer managed key is the only KMS key type that meets these criteria. It allows the customer to manage the key's lifecycle, including enabling or disabling automatic key rotation, or performing manual rotation. By creating a customer managed key and enabling automatic rotation, the company gains full control over the rotation policy while minimizing the ongoing operational effort, as AWS handles the rotation process itself. Why Incorrect Options are Wrong: B. Use an AWS managed key to encrypt the EBS volumes. Use the key to configure automatic key rotation. AWS managed keys have automatic rotation enabled by default, and this setting cannot be changed by the customer. This fails the requirement to control rotation. C. Create an external KMS key with

</details>

### 23. dt-30

In Amazon EC2, if your EBS volume stays in the detaching state, you can force the detachment by clicking [...].

<details><summary>Answer</summary>

**A. Force Detach.**

</details>

### 24. et-40 `availability`

A company has thousands of edge devices that collectively generate 1 TB of status alerts each day. Each alert is approximately 2 KB in size. A solutions architect needs to implement a solution to ingest and store the alerts for future analysis. The company wants a highly available solution. However, the company needs to minimize costs and does not want to manage additional infrastructure. Additionally, the company wants to keep 14 days of data available for immediate analysis and archive any data older than 14 days. What is the MOST operationally efficient solution that meets these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon Kinesis Data Firehose delivery stream to ingest the alerts. Configure the Kinesis Data Firehose stream to deliver the alerts to an Amazon S3 bucket. Set up an S3 Lifecycle configuration to transition data to Amazon S3 Glacier after 14 days.**

Amazon Kinesis Data Firehose is a fully managed service that can capture, transform, and deliver streaming data into storage systems or analytics tools, making it an ideal solution for ingesting and storing status alerts. In this solution, the Kinesis Data Firehose delivery stream ingests the alerts and delivers them to an S3 bucket, which is a cost-effective storage solution. An S3 Lifecycle configuration is set up to transition the data to Amazon S3 Glacier after 14 days to minimize storage costs.

</details>

### 25. ce-41

A company wants to standardize its Amazon Elastic Block Store (Amazon EBS) volume encryption strategy. The company also wants to minimize the cost and configuration effort required to operate the volume encryption check. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an AWS Config rule for Amazon EBS to evaluate if a volume is encrypted and to flag the volume if it is not encrypted.**

AWS Config is the designated AWS service for assessing, auditing, and evaluating the configurations of AWS resources. It provides a managed rule, encrypted-volumes, specifically designed to check whether attached Amazon EBS volumes are encrypted. This solution directly meets the requirements by providing an automated, low-effort mechanism for checking encryption status. It minimizes configuration as it avoids writing custom code, managing infrastructure, or scheduling tasks. The cost is optimized as you pay only for the configuration items recorded and the number of rule evaluations, which is highly efficient for this specific compliance check. Why Incorrect Options are Wrong: A. This is a custom solution that requires writing, testing, and maintaining code for a Lambda function, which is significantly more configuration effort than using a managed AWS Config rule. B. Using AWS Fargate i

</details>

### 26. dt-41

A user has attached 1 EBS volume to a VPC instance. The user wants to achieve the best fault tolerance of data possible. Which of the below mentioned options can help achieve fault tolerance?

<details><summary>Answer</summary>

**A. Attach one more volume with RAID 1 configuration.**

</details>

### 27. dt-42

Which features can be used to restrict access to data in S3? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Set an S3 ACL on the bucket or the object.; C. Set an S3 bucket policy.**

</details>

### 28. et-43

A company has an on-premises application that generates a large amount of time-sensitive data that is backed up to Amazon S3. The application has grown and there are user complaints about internet bandwidth limitations. A solutions architect needs to design a long-term solution that allows for both timely backups to Amazon S3 and with minimal impact on internet connectivity for internal users. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Establish a new AWS Direct Connect connection and direct backup traffic through this new connection.**

AWS Direct Connect is a network service that allows you to establish a dedicated network connection from your on-premises data center to AWS. This connection bypasses the public Internet and can provide more reliable, lower-latency communication between your on-premises application and Amazon S3. By directing backup traffic through the AWS Direct Connect connection, you can minimize the impact on your internet bandwidth and ensure timely backups to S3.

</details>

### 29. et-44

A company has an Amazon S3 bucket that contains critical data. The company must protect the data from accidental deletion. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**Enable versioning on the S3 bucket, and enable MFA Delete on the S3 bucket.**

Versioning is the primary protection: with it on, an overwrite keeps the previous version and a delete writes a delete marker rather than destroying data, so any accidental change can be undone by restoring the earlier version or removing the delete marker. MFA Delete then guards the two actions that would undo that protection - permanently deleting a specific object version, and suspending or changing the bucket's versioning state - by requiring a code from an MFA device on the request. It does not prompt for MFA on an everyday object delete, because in a versioned bucket that delete is not destructive. MFA Delete is configured by the bucket owner's root user through the AWS CLI or API, not from the console.

</details>

### 30. et-46

A company has an application that provides marketing services to stores. The services are based on previous purchases by store customers. The stores upload transaction data to the company through SFTP, and the data is processed and analyzed to generate new marketing offers. Some of the files can exceed 200 GB in size. Recently, the company discovered that some of the stores have uploaded files that contain personally identifiable information (PII) that should not have been included. The company wants administrators to be alerted if PII is shared again. The company also wants to automate remediation. What should a solutions architect do to meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**Use an Amazon S3 bucket as a secure transfer point. Use Amazon Macie to scan the objects in the bucket. If objects contain PII, use Amazon Simple Notification Service (Amazon SNS) to trigger a notification to the administrators to remove the objects that contain PII.**

Amazon Macie is the managed service that discovers personally identifiable information in S3 objects, so no detection code has to be written or maintained - that is what makes this the least development effort. S3 is also the right landing point for the uploads: it handles 200 GB files comfortably (the object limit is 5 TB, with 5 GB being only the single-PUT limit), and AWS Transfer Family can front the bucket so the stores keep their existing SFTP workflow. Macie publishes its results as findings, so routing them to an SNS topic alerts the administrators, and the same event can drive an automated remediation step. Every alternative here requires building and operating custom scanning logic.

</details>

### 31. et-49 `cost`

A company stores call transcript files on a monthly basis. Users access the files randomly within 1 year of the call, but users access the files infrequently after 1 year. The company wants to optimize its solution by giving users the ability to query and retrieve files that are less than 1-year- old as quickly as possible. A delay in retrieving older files is acceptable. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Store individual files in Amazon S3 Intelligent-Tiering. Use S3 Lifecycle policies to move the files to S3 Glacier Flexible Retrieval after 1 year. Query and retrieve the files that are in Amazon S3 by using Amazon Athena.**

Access within the first year is random and therefore unpredictable, which is exactly the case S3 Intelligent-Tiering is built for: it tiers each object on its own access pattern and charges no retrieval fee, so cost falls without risking a charge on a file that turns out to be needed. After a year the requirement changes - a delay is acceptable - so a lifecycle rule moves the files to S3 Glacier Flexible Retrieval, the cheapest class that still allows retrieval in minutes to hours (Expedited 1-5 minutes, Standard 3-5 hours, Bulk 5-12 hours). Files from the last year stay directly queryable, and Athena is the service for querying them in place. Note that S3 Select and S3 Glacier Select, which older versions of this answer name, have been closed to new customers since July 2024; archived objects are now restored first and then queried with Athena.

</details>

### 32. dt-54

An existing application stores sensitive information on a non-boot Amazon EBS data volume attached to an Amazon Elastic Compute Cloud instance. Which of the following approaches would protect the sensitive data on an Amazon EBS volume?

<details><summary>Answer</summary>

**D. Create and mount a new, encrypted Amazon EBS volume. Move the data to the new volume. Delete the old Amazon EBS volume.**

</details>

### 33. dt-56

You have been asked to build AWS infrastructure for disaster recovery for your local applications and within that you should use an AWS Storage Gateway as part of the solution. Which of the following best describes the function of an AWS Storage Gateway?

<details><summary>Answer</summary>

**C. Connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between your on-premises IT environment and AWS's storage infrastructure.**

</details>

### 34. ce-61 `least-ops`

A company is using an AWS Lambda function in a VPC. The Lambda function needs to access dependencies that exceed the size of the Lambda layer quot a. The data that the Lambda function retrieves must be encrypted in transit. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Store the dependencies in an Amazon Elastic File System (Amazon EFS) file system. Mount the file system to the Lambda function. Retrieve the dependencies from the file system.**

Amazon EFS for AWS Lambda allows a function to mount an EFS file system, providing a persistent, scalable storage solution. This is the officially recommended approach for accessing large files or dependencies that exceed the 250 MB unzipped deployment package size limit. When Lambda mounts an EFS file system, all traffic is automatically encrypted in transit using TLS 1.2, fulfilling the security requirement. As both EFS and Lambda are fully managed services, this solution requires minimal configuration and no ongoing server management, representing the least operational overhead. Why Incorrect Options are Wrong: B: Using an EC2 instance requires managing the instance, its operating system, and web server software, which is significant operational overhead compared to the fully managed EFS service. C: This option has even higher operational overhead than B, as it requires managing an NF

</details>

### 35. dt-64

When an EC2 instance that is backed by an S3-based AMI is terminated, what happens to the data on the root volume?

<details><summary>Answer</summary>

**D. Data is automatically deleted.**

</details>

### 36. ce-66

A company creates operations data and stores the data in an Amazon S3 bucket for the company's annual audit, an external consultant needs to access an annual report that is stored in the S3 bucket. The external consultant needs to access the report for 7 days. The company must implement a solution to allow the external consultant access to only the report. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**D. Generate a presigned URL that has the required access to the location of the report on the S3 bucket. Share the presigned URL with the external consultant.**

A presigned URL provides a secure and time-limited method to grant access to a specific object in an Amazon S3 bucket. This solution is the most operationally efficient because it involves a single action to generate the URL with a built-in expiration (up to 7 days with IAM credentials). The consultant can access the report directly via the URL without needing AWS credentials. Access automatically revokes when the URL expires, eliminating the need for manual cleanup. This approach perfectly adheres to the principle of least privilege by scoping access to a single object. Why Incorrect Options are Wrong: A. Creating a new public bucket and migrating data is operationally inefficient and insecure, as it unnecessarily exposes data publicly. B. Enabling public access for the entire bucket is a severe security risk and violates the principle of least privilege. C. Creating an IAM user adds un

</details>

### 37. ce-67

How can a law firm make files publicly readable while preventing modifications or deletions until a specific future date?

<details><summary>Answer</summary>

**B. Create an S3 bucket. Enable S3 Versioning. Use S3 Object Lock with a retention period. Create a CloudFront distribution. Use a bucket policy to restrict access.**

This solution correctly addresses all requirements. S3 Object Lock provides Write-Once-Read-Many (WORM) protection, preventing object deletion or modification for a specified retention period, which satisfies the immutability requirement until a future date. S3 Versioning is a prerequisite for enabling S3 Object Lock. Using a CloudFront distribution is the best practice for securely and efficiently serving content to the public from an S3 bucket. A bucket policy is used to grant read-only access specifically to the CloudFront distribution (via Origin Access Control or Origin Access Identity), ensuring the bucket itself is not directly public, which enhances security. Why Incorrect Options are Wrong: A. IAM permissions only control access for AWS principals (users/roles) and do not prevent the account owner or other authorized users from modifying or deleting the files. C. This is a react

</details>

### 38. ce-70

A company wants to migrate hundreds of gigabytes of unstructured data from an on-premises location to an Amazon S3 bucket. The company has a 100-Mbps internet connection on premises. The company needs to encrypt the data in transit to the S3 bucket. The company will store new data directly in Amazon S3.

<details><summary>Answer</summary>

**B. Use AWS DataSync to migrate the data from the on-premises location to an S3 bucket.**

AWS DataSync is a service designed specifically for accelerating and simplifying online data transfers between on-premises storage systems and AWS Storage services, including Amazon S3. It is the most appropriate solution for this scenario as it can efficiently transfer hundreds of gigabytes over an existing 100-Mbps internet connection. DataSync automatically handles data encryption in transit using TLS, fulfilling the security requirement. It includes built-in optimizations and a purpose-built network protocol to maximize the use of available bandwidth, making it faster and more reliable than standard command-line tools for a one-time migration of this scale. Why Incorrect Options are Wrong: A. AWS Database Migration Service (AWS DMS) is designed for migrating structured data from databases, not for transferring unstructured file data as required by the scenario. C. An AWS Snowball Edg

</details>

### 39. dt-76

Can we attach an EBS volume to more than one EC2 instance at the same time?

<details><summary>Answer</summary>

**B. No.**

</details>

### 40. dt-77

You need to measure the performance of your EBS volumes as they seem to be under performing. You have come up with a measurement of 1,024 KB I/O but your colleague tells you that EBS volume performance is measured in IOPS. How many IOPS is equal to 1,024 KB I/O?

<details><summary>Answer</summary>

**D. 4.**

</details>

### 41. ce-80 `security`

A law firm needs to make hundreds of files readable for the general public. The law firm must prevent members of the public from modifying or deleting the files before a specified future date. Which solution will meet these requirements MOST securely?

<details><summary>Answer</summary>

**B. Create a new Amazon S3 bucket. Enable S3 Versioning. Use S3 Object Lock and set a retention period based on the specified date. Create an Amazon CloudFront distribution to serve content from the bucket. Use an S3 bucket policy to restrict access to the CloudFront origin access control (OAC).**

This solution is the most secure because it employs a defense-in-depth strategy. Amazon CloudFront with Origin Access Control (OAC) is the recommended best practice for securely serving content from a private Amazon S3 bucket to the public. This prevents users from bypassing CloudFront and accessing the S3 bucket directly. S3 Object Lock in compliance mode, combined with a retention period, provides Write-Once-Read-Many (WORM) protection, which directly meets the requirement to prevent modification or deletion of files until a specified date. S3 Versioning is a prerequisite for enabling S3 Object Lock and adds an additional layer of data protection. Why Incorrect Options are Wrong: A. Granting IAM permissions to AWS principals does not make files readable for the anonymous general public. Configuring the bucket for static website hosting makes it publicly accessible, which is less secure

</details>

### 42. dt-80

You need to configure an Amazon S3 bucket to serve static assets for your public-facing web application. Which methods ensure that all objects uploaded to the bucket are set to public read? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Set permissions on the object to public read during upload.; C. Configure the bucket policy to set all objects to public read.**

</details>

### 43. ce-81 `least-ops`

A media company hosts a web application on AWS. The application gives users the ability to upload and view videos. The application stores the videos in an Amazon S3 bucket. The company wants to ensure that only authenticated users can upload videos. Authenticated users must have the ability to upload videos only within a specified time frame after authentication. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an AWS Lambda function that generates pre-signed URLs when a user authenticates.**

An Amazon S3 pre-signed URL provides a secure and time-limited method for a user to upload a specific object to a bucket without requiring AWS security credentials. The application's backend can authenticate the user and then generate a pre-signed URL using its own IAM permissions. This URL, which includes a signature and an expiration time, is given to the client. The client can then perform the upload directly to S3. This approach minimizes operational overhead by using a serverless component like AWS Lambda for generation, offloading the data transfer from the application servers, and simplifying the client-side implementation to a standard HTTP PUT request. Why Incorrect Options are Wrong: A. This is less efficient than a pre-signed URL. It requires the client application to manage temporary credentials and use the AWS SDK for the upload, which is more complex and has higher overhead

</details>

### 44. dt-85

Amazon EBS provides the ability to create backups of any Amazon EC2 volume into what is known as [...].

<details><summary>Answer</summary>

**A. snapshots.**

</details>

### 45. ce-86

A healthcare provider is planning to store patient data on AWS as PDF files. To comply with regulations, the company must encrypt the data and store the files in multiple locations. The data must be available for immediate access from any environment.

<details><summary>Answer</summary>

**A. Store the files in an Amazon S3 bucket. Use the Standard storage class. Enable server-side encryption with Amazon S3 managed keys (SSE-S3) on the bucket. Configure cross-Region replication on the bucket.**

This solution correctly addresses all requirements. Amazon S3 is the ideal service for storing objects like PDF files and making them accessible from any environment via HTTP/S. The S3 Standard storage class is designed for frequently accessed data, providing the required "immediate access" with millisecond latency. Server-side encryption with S3-managed keys (SSE-S3) fulfills the encryption mandate by encrypting data at rest. Finally, configuring Cross-Region Replication (CRR) automatically and asynchronously copies the files to a bucket in a different AWS Region, satisfying the need to store files in multiple locations for disaster recovery and compliance. Why Incorrect Options are Wrong: B: Amazon EFS is a file system designed for access from EC2 instances within a VPC via the NFS protocol, not for immediate access from "any environment" over the internet. C: Amazon EBS provides block

</details>

### 46. dt-91

Which of the following are true regarding encrypted Amazon Elastic Block Store (EBS) volumes? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Supported on all Amazon EBS volume types.; B. Snapshots are automatically encrypted.**

</details>

### 47. dt-93

While creating the snapshots using the API, which Action should I be using?

<details><summary>Answer</summary>

**D. CreateSnapshot.**

</details>

### 48. ce-96

A solutions architect is building an Amazon S3 data lake for a company. The company uses Amazon Kinesis Data Firehose to ingest customer personally identifiable information (PII) and transactional data in near real-time to an S3 bucket. The company needs to mask all PII data before storing thedata in the data lake. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an AWS Lambda function to detect and mask PII. Invoke the function from Kinesis Data Firehose.**

Amazon Kinesis Data Firehose can be configured to perform data transformation on in-flight data before it is delivered to a destination like Amazon S3. This is achieved by invoking an AWS Lambda function. The Lambda function receives batches of records from Firehose, processes them to detect and mask the Personally Identifiable Information (PII), and then returns the transformed records to Firehose. Firehose then delivers the now-masked data to the S3 data lake. This solution directly meets the requirement to mask PII before it is stored. Why Incorrect Options are Wrong: B. Amazon Macie discovers sensitive data after it is already stored in S3. It does not perform in-flight data transformation or masking before the data is written. C. Server-side encryption (SSE) encrypts the entire data object at rest. It does not inspect or alter the content to mask specific PII fields within the objec

</details>

### 49. dt-98

A user wants to increase the durability and availability of the EBS volume. Which of the below mentioned actions should he perform?

<details><summary>Answer</summary>

**A. Take regular snapshots.**

</details>

### 50. dt-102

Do Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?

<details><summary>Answer</summary>

**D. Yes, they do.**

</details>

### 51. dt-105

In the 'Detailed' monitoring data available for your Amazon EBS volumes, Provisioned IOPS volumes automatically send [...] minute metrics to Amazon CloudWatch.

<details><summary>Answer</summary>

**B. 1.**

</details>

### 52. dt-109

A friend wants you to set up a small BitTorrent storage area for him on Amazon S3. You tell him it is highly unlikely that AWS would allow such a thing in their infrastructure. However you decide to investigate. Which of the following statements best describes using BitTorrent with Amazon S3?

<details><summary>Answer</summary>

**D. You can use the BitTorrent protocol but only for objects that are less than 5 GB in size.**

</details>

### 53. ce-110 `least-ops`

A financial service company has a two-tier consumer banking application. The frontend serves static web content. The backend consists of APIs. The company needs to migrate the frontendcomponent to AWS. The backend of the application will remain on premises. The company must protect the application from common web vulnerabilities and attacks. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Deploy the frontend as an Amazon CloudFront distribution that has multiple origins. Configure one origin to be an Amazon S3 bucket that serves the static web content. Configure a second origin to route traffic to the on-premises APIs based on the URL pattern. Associate AWS WAF rules with the distribution.**

This solution provides the lowest operational overhead by using serverless and managed AWS services. Amazon S3 is the ideal service for hosting static web content without managing servers. Amazon CloudFront acts as a single entry point, caching the static content from the S3 origin at edge locations for low latency and routing API requests to the on-premises backend via a custom origin. This is achieved using path-based routing. AWS WAF integrates directly with CloudFront, allowing for centralized protection against common web vulnerabilities for all traffic entering the application. This architecture avoids the need to provision, patch, and manage EC2 instances, thus minimizing operational effort while meeting all security and functional requirements. Why Incorrect Options are Wrong A. Migrate the frontend to Amazon EC2 instances... This option incurs high operational overhead due to th

</details>

### 54. dt-113

A user is storing a large number of objects on AWS S3. The user wants to implement the search functionality among the objects. How can the user achieve this?

<details><summary>Answer</summary>

**D. Make your own DB system which stores the S3 metadata for the search functionality.**

</details>

### 55. ce-114

A financial services company has a two-tier consumer banking application. The frontend serves static web content. The backend consists of APIs. The company needs to migrate the frontendcomponent to AWS. The backend of the application will remain on-premises. The company must protect the application from common web vulnerabilities and attacks.

<details><summary>Answer</summary>

**B. Deploy the frontend as an Amazon CloudFront distribution that has multiple origins. Configure one origin to be an Amazon S3 bucket that serves the static web content. Configure a second origin to route traffic to the on-premises APIs based on the URL pattern. Associate AWS WAF rules with the distribution.**

This architecture represents the most efficient and secure design for the given requirements. Amazon S3 is the optimal service for hosting static web content due to its durability, scalability, and low cost. Amazon CloudFront acts as a Content Delivery Network (CDN), caching the static content at edge locations globally for low-latency delivery to users. Crucially, CloudFront supports multiple origins. One origin can be the S3 bucket for the static frontend, while a second "custom origin" can be configured to point to the on-premises API endpoint. CloudFront can then use path-based routing (cache behaviors) to direct user requests, sending traffic for /api/ to the on-premises backend and all other traffic to the S3 bucket. AWS WAF integrates directly with CloudFront to provide protection against common web exploits at the network edge. Why Incorrect Options are Wrong: A: Using EC2 instan

</details>

### 56. dt-124

True or False: When you view the block device mapping for your instance, you can see only the EBS volumes, not the instance store volumes.

<details><summary>Answer</summary>

**D. True.**

</details>

### 57. ce-126

A financial services company must retain log data for 1 year. The company stores log files in an Amazon S3 bucket and wants to prevent any user from deleting or overwriting the log files during this period. The data must remain available for read-only requests.

<details><summary>Answer</summary>

**A. Enable S3 Versioning on the bucket. Use Object Lock in compliance mode with a 1-year retention period.**

The core requirement is to implement a Write-Once, Read-Many (WORM) model to prevent log files from being deleted or overwritten by any user for one year. Amazon S3 Object Lock is the feature designed for this purpose. When used in compliance mode, it enforces a fixed retention period during which an object version cannot be overwritten or deleted by any user, including the root user in the AWS account. S3 Versioning is a prerequisite for enabling Object Lock. This solution directly meets the company's immutability and retention requirements while keeping the data readily available for read requests. Why Incorrect Options are Wrong: B: S3 Transfer Acceleration is for speeding up data transfers, not for data protection. A Lifecycle rule to move data after 1 year does not protect it from deletion during that year. C: S3 Versioning alone does not prevent deletion. A user with sufficient per

</details>

### 58. ce-130

A company operates an online photo-sharing service and stores data in AWS Account A in a centralized Amazon S3 bucket. The company wants to grant a second AWS account named Account B access to the centralized S3 bucket. The company owns Account B. Options:

<details><summary>Answer</summary>

**D. Create a bucket policy that grants Account B permission to access the centralized S3 bucket in Account A.**

The most direct and standard method for granting one AWS account access to an Amazon S3 bucket in another account is by using a resource-based policy, specifically an S3 bucket policy. By attaching a bucket policy to the centralized S3 bucket in Account A, the owner can explicitly grant permissions (e.g., s3:GetObject, s3:ListBucket) to a specific principal in Account B, such as the account root user or a designated IAM role. This approach is secure, scalable, and directly addresses the requirement for cross-account access to the centralized data source without duplicating data or introducing unnecessary complexity. Why Incorrect Options are Wrong: A. S3 Transfer Acceleration is a feature that speeds up long-distance data transfers to and from S3 buckets using AWS edge locations; it does not manage access permissions. B. Cross-Region replication copies S3 objects to a bucket in another a

</details>

### 59. ce-133

A company recently migrated a large amount of research data to an Amazon S3 bucket. The company needs an automated solution to identify sensitive data in the bucket. A security team also needs to monitor access patterns for the data 24 hours a day, 7 days a week to identify suspicious activities or evidence of tampering with security controls. Options:

<details><summary>Answer</summary>

**B. Enable Amazon Macie and Amazon GuardDuty on the account. Grant the security team access to Macie and GuardDuty. Review the findings with the security team.**

This solution correctly addresses both requirements of the question using the most appropriate AWS services. Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect sensitive data in Amazon S3. This directly fulfills the need for an automated solution to identify sensitive data. Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior, including analyzing S3 data events from CloudTrail to detect suspicious access patterns and potential tampering. This provides the required 24/7 monitoring for suspicious activities. Why Incorrect Options are Wrong: A. Amazon S3 Inventory only provides metadata about objects (e.g., name, size, storage class), it does not scan object content to identify sensitive data. C. This approach is flawed because Ama

</details>

### 60. dt-137 `performance`

You have an application running on an Amazon Elastic Compute Cloud instance, that uploads 5 GB video objects to Amazon Simple Storage Service (S3). Video uploads are taking longer than expected, resulting in poor application performance. Which method will help improve performance of your application?

<details><summary>Answer</summary>

**B. Use Amazon S3 multipart upload.**

</details>

### 61. dt-138

You have been given a scope to set up an AWS Media Sharing Framework for a new start up photo sharing company similar to flickr. The first thing that comes to mind about this is that it will obviously need a huge amount of persistent data storage for this framework. Which of the following storage options would be appropriate for persistent storage?

<details><summary>Answer</summary>

**D. Amazon EBS volumes or Amazon S3.**

</details>

### 62. ce-142

A company uses AWS to host a public website. The load on the webservers recently increased. The company wants to learn more about the traffic flow and traffic sources. The company also wants to increase the overall security of the website. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy AWS WAF and set up logging. Use Amazon Data Firehose to deliver the log files to an Amazon S3 bucket for analysis.**

This solution directly addresses both requirements. AWS Web Application Firewall (WAF) is a service designed to protect web applications from common exploits like SQL injection and cross-site scripting, thus meeting the requirement to "increase the overall security." AWS WAF also provides full logging of all requests it inspects. These logs contain detailed information about traffic, such as source IP addresses, headers, and URIs, which satisfies the need to "learn more about the traffic flow and traffic sources." Using Amazon Data Firehose is an efficient, managed way to stream these logs directly to an Amazon S3 bucket for durable storage and subsequent analysis. Why Incorrect Options are Wrong: B. Deploy Amazon API Gateway and set up logging. Use Amazon Kinesis Data Streams to deliver the log files to an Amazon S3 bucket for analysis. API Gateway is for managing APIs, not for securing

</details>

### 63. dt-143

A customer wants to track access to their Amazon Simple Storage Service (S3) buckets and also use this information for their internal security and access audits. Which of the following will meet the Customer requirement?

<details><summary>Answer</summary>

**A. Enable AWS CloudTrail to audit all Amazon S3 bucket access.**

</details>

### 64. ce-146 `least-ops`

An ecommerce company stores terabytes of customer data in the AWS Cloud. The data contains personally identifiable information (PII). The company wants to use the data in three applications. Only one of the applications needs to process the PII. The PII must be removed before the other two applications process the data. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Store the data in an Amazon S3 bucket. Process and transform the data by using S3 Object Lambda before returning the data to the requesting application.**

The most efficient solution with the least operational overhead is to store the single, authoritative dataset in Amazon S3 and use S3 Object Lambda. S3 is the ideal service for storing terabytes of data cost-effectively. S3 Object Lambda allows you to invoke an AWS Lambda function to process and transform data as it is being retrieved. This enables on-the-fly redaction of personally identifiable information (PII) for the two applications that do not require it, while the third application can access the original data. This approach avoids creating and managing multiple copies of the data or building a separate proxy infrastructure, directly fulfilling the requirement for minimal operational overhead. Why Incorrect Options are Wrong: A. A custom proxy application layer must be built, scaled, and maintained, which creates significant operational overhead compared to a managed, serverless s

</details>

### 65. dt-146

A company is storing data on Amazon Simple Storage Service (S3). The company's security policy mandates that data is encrypted at rest. Which of the following methods can achieve this? (Choose 3 answers)

<details><summary>Answer</summary>

**A. Use Amazon S3 server-side encryption with AWS Key Management Service managed keys.; B. Use Amazon S3 server-side encryption with customer-provided keys.; E. Encrypt the data on the client-side before ingesting to Amazon S3 using their own master key.**

</details>

### 66. ce-149

A company needs to implement a new data retention policy for regulatory compliance. As part of this policy, sensitive documents that are stored in an Amazon S3 bucket must be protected from deletion or modification for a fixed period of time. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Activate S3 Object Lock on the required objects and enable compliance mode.**

The requirement is to protect sensitive documents from deletion or modification for a fixed period to meet regulatory compliance. Amazon S3 Object Lock is the feature designed for this Write-Once, Read-Many (WORM) model. S3 Object Lock has two retention modes: governance and compliance. Compliance mode is the stricter of the two. When an object is locked in compliance mode, its retention period cannot be shortened, and its retention mode cannot be changed. No user, including the root user in the AWS account, can overwrite or delete the protected object version until the retention period expires. This provides the highest level of immutability required for stringent regulatory compliance. Why Incorrect Options are Wrong: A. Governance mode allows users with special permissions (s3:BypassGovernanceRetention) to override the lock settings, which does not guarantee protection from all users

</details>

### 67. dt-151

What will be the status of the snapshot until the snapshot is complete?

<details><summary>Answer</summary>

**D. Pending.**

</details>

### 68. dt-163

What is one key difference between an Amazon EBS-backed and an instance-store backed instance?

<details><summary>Answer</summary>

**A. Amazon EBS-backed instances can be stopped and restarted.**

</details>

### 69. dt-166

To view information about an Amazon EBS volume, open the Amazon EC2 console at <https://console.aws.amazon.com/ec2/>, click in the Navigation panel.

<details><summary>Answer</summary>

**D. Volumes.**

</details>

### 70. ce-168

A company wants to migrate applications from its on-premises servers to AWS. As a first step, the company is modifying and migrating a non-critical application to a single Amazon EC2 instance. The application will store information in an Amazon S3 bucket. The company needs to follow security best practices when deploying the application on AWS. Which approach should the company take to allow the application to interact with Amazon S3?

<details><summary>Answer</summary>

**A. Store the files in an Amazon S3 bucket. Use the S3 Glacier Instant Retrieval storage class. Create an S3 Lifecycle policy to transition the files to the S3 Glacier Deep Archive storage class after 1 year.**

The question asks for an approach for a non-critical application on an EC2 instance to store information in Amazon S3, emphasizing best practices. While the prompt mentions security, the options provided focus on storage lifecycle management and cost optimization, which are also key operational best practices. For a "non-critical" application, data is often accessed infrequently but may need to be retained for long periods. The most cost-effective approach is to use storage classes designed for archival and infrequent access. Option A proposes using S3 Glacier Instant Retrieval, which is ideal for long-lived, rarely accessed data that still requires immediate retrieval. Transitioning the data to S3 Glacier Deep Archive after one year further minimizes costs for data that is almost never accessed again, aligning perfectly with a long-term retention strategy for non-critical information. W

</details>

### 71. dt-170

If I want to run a database in an Amazon instance, which is the most recommended Amazon storage option?

<details><summary>Answer</summary>

**B. Amazon EBS.**

</details>

### 72. dt-171

A customer is leveraging Amazon Simple Storage Service in eu-west-1 to store static content for a web-based property. The customer is storing objects using the Standard Storage class. Where are the customers objects replicated?

<details><summary>Answer</summary>

**C. Multiple facilities in eu-west-1.**

</details>

### 73. dt-172

You have set up an S3 bucket with a number of images in it and you have decided that you want anybody to be able to access these images, even anonymous users. To accomplish this you create a bucket policy. You will need to use an Amazon S3 bucket policy that specifies a [...] in the principal element, which means anyone can access the bucket.

<details><summary>Answer</summary>

**C. wildcard (*).**

</details>

### 74. dt-175

A photo-sharing service stores pictures in Amazon Simple Storage Service (S3) and allows application sign-in using an OpenID Connect-compatible identity provider. Which AWS Security Token Service approach to temporary access should you use for the Amazon S3 operations?

<details><summary>Answer</summary>

**D. Web Identity Federation.**

</details>

### 75. ce-180

A company uses an Amazon CloudFront distribution to serve thousands of media files to users. The CloudFront distribution uses a private Amazon S3 bucket as an origin. A solutions architect must prevent users in specific countries from accessing the company's files. Which solution will meet these requirements in the MOST operationally-efficient way?

<details><summary>Answer</summary>

**B. Configure geographic restrictions in CloudFront.**

Amazon CloudFront has a built-in feature called geographic restrictions (also known as geo-blocking) that is designed specifically for this use case. This feature allows you to either create an "allowlist" of countries where users can access your content or a "blocklist" of countries where users are denied access. Configuring this is a simple change within the CloudFront distribution's settings, making it the most direct and operationally efficient method to prevent access from specific countries without requiring any application-level changes. Why Incorrect Options are Wrong: A. Signed URLs are used to provide time-limited, private access to individual files for specific users, not to block entire geographic regions. C. Signed cookies function similarly to signed URLs but are used to provide access to multiple restricted files, not for implementing broad geographic blocking. D. Origin a

</details>

### 76. dt-180

You are building a system to distribute confidential documents to employees. Using CloudFront, what method could be used to serve content that is stored in S3, but not publically accessible from S3 directly?

<details><summary>Answer</summary>

**D. Create an Origin Access Identity (OAI) for CloudFront and grant access to the objects in your S3 bucket to that OA.**

</details>

### 77. dt-181

You require the ability to analyze a large amount of data, which is stored on Amazon S3 using Amazon Elastic MapReduce. You are using the cc2 8x large Instance type, whose CPUs are mostly idle during processing. Which of the below would be the most cost efficient way to reduce the runtime of the job?

<details><summary>Answer</summary>

**C. Use smaller instances that have higher aggregate 1/0 performance.**

</details>

### 78. dt-184

Do you need to shutdown your EC2 instance when you create a snapshot of EBS volumes that serve as root devices?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 79. et-188 `availability`

A company uses Amazon S3 as its data lake. The company has a new partner that must use SFTP to upload data files. A solutions architect needs to implement a highly available SFTP solution that minimizes operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Transfer Family to configure an SFTP-enabled server with a publicly accessible endpoint. Choose the S3 data lake as the destination.**

AWS Transfer Family is a fully managed service that allows you to set up a secure file transfer protocol (SFTP) server for transferring files into and out of Amazon S3. With AWS Transfer Family, you can avoid the operational overhead of managing traditional SFTP servers. This solution provides a highly available SFTP service with minimal effort, and the data can be directly transferred to the S3 data lake.

</details>

### 80. et-189 `least-ops`

A company needs to store contract documents. A contract lasts for 5 years. During the 5-year period, the company must ensure that the documents cannot be overwritten or deleted. The company needs to encrypt the documents at rest and rotate the encryption keys automatically every year. Which combination of steps should a solutions architect take to meet these requirements with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**B. Store the documents in Amazon S3. Use S3 Object Lock in compliance mode.**

S3 Object Lock in compliance mode enforces a "Write Once, Read Many" (WORM) model, preventing the objects (contract documents, in this case) from being deleted or overwritten for a specified retention period.  D. Use server-side encryption with AWS Key Management Service (AWS KMS) customer managed keys. Configure key rotation.  By using AWS KMS customer managed keys, you can configure key rotation to automatically rotate encryption keys, meeting the requirement of rotating encryption keys every year.

</details>

### 81. dt-194

What does Amazon S3 stand for?

<details><summary>Answer</summary>

**D. Simple Storage Service.**

</details>

### 82. ce-195 `least-ops`

A company has multiple AWS accounts with applications deployed in the us-west-2 Region. Application logs are stored within Amazon S3 buckets in each account. The company wants to build a centralized log analysis solution that uses a single S3 bucket. Logs must not leave us-west-2, and the company wants to incur minimal operational overhead.

<details><summary>Answer</summary>

**B. Use S3 Same-Region Replication to replicate logs from the S3 buckets to another S3 bucket in us- west-2. Use this S3 bucket for log analysis.**

The most efficient and operationally simple solution is to use Amazon S3 Same-Region Replication (SRR). SRR is a managed feature of S3 that automatically and asynchronously copies new objects from a source bucket to a destination bucket within the same AWS Region. It can be configured to replicate objects across different AWS accounts, which directly addresses the need to centralize logs from multiple accounts into a single bucket. Because SRR is a native, managed S3 feature, it requires only initial configuration and incurs minimal operational overhead compared to custom-scripted or event-driven solutions. This approach satisfies all requirements: centralization, staying within the us-west-2 Region, and minimal operational overhead. Why Incorrect Options are Wrong: A. S3 Lifecycle policies are used to manage the lifecycle of objects within a bucket, such as transitioning them to differe

</details>

### 83. ce-196

A solutions architect must design a solution that uses Amazon CloudFront with an Amazon S3 origin to serve a static website. The solution must use AWS WAF to inspect all website traffic.

<details><summary>Answer</summary>

**D. Configure CloudFront and Amazon S3 to use an origin access control (OAC) to secure the origin S3 bucket. Associate AWS WAF to the CloudFront distribution.**

This solution correctly implements a secure, multi-layered architecture. First, it uses an Origin Access Control (OAC) to restrict access to the Amazon S3 bucket. OAC creates a service principal that allows CloudFront to access the S3 bucket, while the S3 bucket policy is configured to deny all other access, preventing users from bypassing CloudFront. Second, it correctly associates AWS WAF with the CloudFront distribution. This ensures that all incoming HTTP/S requests are inspected by WAF at the AWS edge network before they are forwarded to the S3 origin, providing protection against common web exploits. Why Incorrect Options are Wrong: A. AWS WAF inspects traffic at CloudFront; it does not originate requests to S3. An S3 bucket policy cannot use a WAF ARN to grant access. B. The architectural flow is incorrect. You associate an AWS WAF web ACL with a CloudFront distribution, not forwa

</details>

### 84. ce-199

A company runs its legacy web application on AWS. The web application server runs on an Amazon EC2 instance in the public subnet of a VPC. The web application server collects images from customers and stores the image files in a locally attached Amazon Elastic Block Store (Amazon EBS) volume. The image files are uploaded every night to an Amazon S3 bucket for backup. A solutions architect discovers that the image files are being uploaded to Amazon S3 through the public endpoint. The solutions architect needs to ensure that traffic to Amazon S3 does not use the public endpoint.

<details><summary>Answer</summary>

**A. Create a gateway VPC endpoint for the S3 bucket that has the necessary permissions for the VPC. Configure the subnet route table to use the gateway VPC endpoint.**

A gateway VPC endpoint for Amazon S3 provides a secure, private connection between resources in a VPC and the S3 service. By creating a gateway endpoint and adding a route to the subnet's route table that directs S3-bound traffic to this endpoint, the EC2 instance can communicate with S3 without using an internet gateway or NAT device. This ensures that the data transfer remains entirely within the AWS network, directly addressing the requirement to avoid the public S3 endpoint. This is the standard, most direct, and cost-effective solution for this scenario. Why Incorrect Options are Wrong: B: Amazon S3 is a global service that does not reside within a VPC. It is architecturally impossible to move an S3 bucket "inside" a VPC. C: An S3 access point simplifies access management policies but does not create the private network path. A VPC endpoint is still required to route traffic private

</details>

### 85. dt-199

What is the type of monitoring data (for Amazon EBS volumes) which is available automatically in 5- minute periods at no charge called?

<details><summary>Answer</summary>

**A. Basic.**

</details>

### 86. dt-202

Making your snapshot public shares all snapshot data with everyone. Can the snapshots with AWS Market place product codes be made public?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 87. et-202 `least-ops`

A company is planning to move its data to an Amazon S3 bucket. The data must be encrypted when it is stored in the S3 bucket. Additionally, the encryption key must be automatically rotated every year. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an AWS Key Management Service (AWS KMS) customer managed key. Enable automatic key rotation. Set the S3 bucket’s default encryption behavior to use the customer managed KMS key. Move the data to the S3 bucket.**

In this option, you use AWS KMS to create a customer managed key, enable automatic key rotation, and set it as the default encryption key for the S3 bucket. This ensures that the data is encrypted with a key managed by AWS KMS, and the key rotation is handled automatically. This approach minimizes manual intervention and provides a secure and automated solution for data encryption with key rotation.

</details>

### 88. dt-204

You have launched an EC2 instance with four (4) 500 GB EBS Provisioned IOPS volumes attached. The EC2 instance is EBS-Optimized and supports 500 Mbps throughput between EC2 and EBS. The four EBS volumes are configured as a single RAID 0 device, and each Provisioned IOPS volume is provisioned with 4,000IOPS (4,000 16KB reads or writes), for a total of 16,000 random IOPS on the instance. The EC2 instance initially delivers the expected 16,000 IOPS random read and write performance. Sometime later, in order to increase the total random I/O performance of the instance, you add an additional two 500 GB EBS Provisioned IOPS volumes to the RAID. Each volume is provisioned to 4,000 IOPs like the original four, for a total of 24,000 IOPS on the EC2 instance. Monitoring shows that the EC2 instance CPU utilization increased from 50% to 70%, but the total random IOPS measured at the instance level does not increase at all. What is the problem and a valid solution?

<details><summary>Answer</summary>

**B. The EBS-Optimized throughput limits the total IOPS that can be utilized; use an EBS Optimized instance that provides larger throughput. Mo**

</details>

### 89. et-205 `cost`

A company hosts a marketing website in an on-premises data center. The website consists of static documents and runs on a single server. An administrator updates the website content infrequently and uses an SFTP client to upload new documents. The company decides to host its website on AWS and to use Amazon CloudFront. The company’s solutions architect creates a CloudFront distribution. The solutions architect must design the most cost-effective and resilient architecture for website hosting to serve as the CloudFront origin. Which solution will meet these requirements?

<details><summary>Answer</summary>

**Create a private Amazon S3 bucket. Use an S3 bucket policy that allows access only from the CloudFront distribution (Origin Access Control). Upload website content by using the AWS CLI.**

Static content in S3 behind CloudFront is the cheapest and most resilient option here: there are no servers to run or patch, and S3 stores objects across at least three Availability Zones in the Region. The bucket stays private with no public access, and a bucket policy grants read access only to the CloudFront distribution through Origin Access Control, so viewers can reach the content only via CloudFront. Origin Access Control is the current mechanism for this; Origin Access Identity did the same job and still works on older distributions, but AWS documents it as legacy and it cannot read SSE-KMS encrypted objects. Infrequent content updates are handled with the AWS CLI instead of SFTP.

</details>

### 90. dt-209

You run an ad-supported photo sharing website using Amazon S3 to serve photos to visitors of your site. At some point you find out that other sites have been linking to the photos on your site, causing loss to your business. What is an effective method to mitigate this?

<details><summary>Answer</summary>

**A. Remove public read access and use signed URLs with expiry dates.**

</details>

### 91. dt-210

Which of the following is not a true statement relating to the performance of your EBS volumes?

<details><summary>Answer</summary>

**A. Frequent snapshots provide a higher level of data durability and they will not degrade the performance of your application while the snapshot is in progress.**

</details>

### 92. ce-211

A healthcare company is designing a system to store and manage logs in the AWS Cloud. The system ingests and stores logs in JSON format that contain sensitive patient information. The company must identify any sensitive data and must be able to search the log data by using SQL queries. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Store the logs in an Amazon S3 bucket. Configure Amazon Macie to discover sensitive data. Use Amazon Athena to query the logs.**

This solution correctly aligns AWS services with the stated requirements. Amazon S3 is a highly scalable and durable object store, ideal for ingesting and storing large volumes of JSON log files. Amazon Macie is a purpose-built data security service that uses machine learning to automatically discover and classify sensitive data, such as patient information, within Amazon S3. Finally, Amazon Athena provides a serverless, interactive query service that allows users to run standard SQL queries directly on the JSON files stored in S3 without needing to load them into a separate database. This combination provides a complete, efficient, and scalable solution. Why Incorrect Options are Wrong: B. Amazon EBS is block storage for EC2 instances, not an appropriate service for querying log files directly. Amazon RDS cannot query files stored on an EBS volume. C. AWS Key Management Service (KMS) is

</details>

### 93. et-212 `cost`

A company needs to export its database once a day to Amazon S3 for other teams to access. The exported object size varies between 2 GB and 5 GB. The S3 access pattern for the data is variable and changes rapidly. The data must be immediately available and must remain accessible for up to 3 months. The company needs the most cost-effective solution that will not increase retrieval time. Which S3 storage class should the company use to meet these requirements?

<details><summary>Answer</summary>

**A. S3 Intelligent-Tiering**

S3 Intelligent-Tiering is designed to optimize costs by automatically moving objects between two access tiers: frequent and infrequent access. It is suitable for data with unknown or changing access patterns. With S3 Intelligent-Tiering, Amazon S3 automatically and transparently moves objects between access tiers based on changing access patterns. It is cost-effective for a wide range of storage access patterns. The objects can be immediately accessed, and the storage cost is lower than using S3 Standard, making it a suitable choice for varying access patterns.

</details>

### 94. ce-215 `least-ops`

A financial company is migrating banking applications to AWS accounts managed through AWS Organizations. The applications store sensitive customer data on Amazon EBS volumes, and the company takes regular snapshots for backups. The company must implement controls across all accounts to prevent sharing EBS snapshots publicly, with the least operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Enable block public access for EBS snapshots at the organization level.**

The most direct and efficient solution is to use the "Block public access for EBS snapshots" feature. This is a preventative security control designed specifically for this purpose. It can be enabled for individual accounts or set as a default for all new accounts at the AWS Organizations level. Once enabled, it blocks any attempts to make EBS snapshots public, regardless of the user's IAM permissions. This approach directly meets the requirement to prevent public sharing across the organization with the least operational overhead, as it's a simple setting rather than a complex policy or monitoring rule. Why Incorrect Options are Wrong: A. AWS Config rules are detective controls used for monitoring and alerting on non-compliant resources. They do not prevent the action of sharing a snapshot publicly. C. An IAM policy in the root (management) account only applies to principals within that

</details>

### 95. et-215 `cost`

A company has 700 TB of backup data stored in network attached storage (NAS) in its data center. This backup data need to be accessible for infrequent regulatory requests and must be retained 7 years. The company has decided to migrate this backup data from its data center to AWS. The migration must be complete within 1 month. The company has 500 Mbps of dedicated bandwidth on its public internet connection available for data transfer. What should a solutions architect do to migrate and store the data at the LOWEST cost?

<details><summary>Answer</summary>

**A. Order AWS Snowball devices to transfer the data. Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.**

AWS Snowball: AWS Snowball is a physical data transfer service that allows you to securely transfer large amounts of data into and out of AWS. In this scenario, with 700 TB of data, using Snowball devices can expedite the transfer process. It's a one-time cost-efficient solution for large data transfers. Amazon S3 Glacier Deep Archive: After transferring the data to Amazon S3 using Snowball, you can use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive. This storage class is designed for infrequently accessed data with a retention requirement of 7 years, aligning with the regulatory compliance needs.

</details>

### 96. et-216

A company has a serverless website with millions of objects in an Amazon S3 bucket. The company uses the S3 bucket as the origin for an Amazon CloudFront distribution. The company did not set encryption on the S3 bucket before the objects were loaded. A solutions architect needs to enable encryption for all existing objects and for all objects that are added to the S3 bucket in the future. Which solution will meet these requirements with the LEAST amount of effort?

<details><summary>Answer</summary>

**B. Turn on the default encryption settings for the S3 bucket. Use the S3 Inventory feature to create a .csv file that lists the unencrypted objects. Run an S3 Batch Operations job that uses the copy command to encrypt those objects.**

This option utilizes the S3 Inventory feature to generate a list of unencrypted objects in the S3 bucket. It then leverages S3 Batch Operations to perform a copy operation, allowing the encryption of the objects during the copy process. This approach is efficient and does not require downloading and re-uploading all existing objects.

</details>

### 97. ce-217

A company stores data in a centralized S3 bucket in Account A. It needs to grant Account B access to this bucket. Both accounts belong to the company. Which solution meets this requirement?

<details><summary>Answer</summary>

**D. Create a bucket policy granting Account B access to the bucket in Account A.**

The most direct and standard method for granting another AWS account access to an S3 bucket is by using a resource-based policy, specifically an S3 bucket policy. The policy is attached to the S3 bucket in the resource-owning account (Account A). Within this policy, the Principal element is used to specify the account that is granted access (Account B, identified by its account ID). The policy also defines the specific S3 actions (e.g., s3:GetObject) that Account B is allowed to perform on the resources within the bucket. This approach provides a clear, manageable, and secure way to share S3 resources across accounts. Why Incorrect Options are Wrong: A. S3 Transfer Acceleration is a network optimization feature that speeds up data transfers over long distances. It does not provide any access control capabilities. B. Cross-Region replication creates a copy of the S3 objects in a bucket in

</details>

### 98. ce-219

A solutions architect needs to ensure that only resources in VPC vpc-11aabb22 can access an S3 bucket in account 123456789012 with Block Public Access enabled. Which solution meets this requirement?

<details><summary>Answer</summary>

**A. Create a bucket policy with Deny and a Condition using "StringNotEquals": "aws:SourceVpc": "vpc-11aabb22".**

The most effective method to enforce that only resources from a specific VPC can access an S3 bucket is to use a bucket policy with an explicit Deny. The policy should deny all actions ("Action": "s3:") for all principals ("Principal": "") when the request does not originate from the specified VPC. This is achieved using a Condition with the StringNotEquals operator on the aws:SourceVpc global condition key. An explicit Deny in a policy always overrides any Allow permissions, making this a robust security control. For this policy to function, a VPC endpoint for S3 must be configured in the specified VPC. Why Incorrect Options are Wrong: B. The Resource element in an S3 bucket policy must specify an S3 ARN (e.g., arn:aws:s3:::bucket-name/), not a VPC ARN. This syntax is invalid. C. This policy would Allow access to any request where the source VPC is not vpc-11aabb22, which is the exact o

</details>

### 99. dt-221

You have a lot of data stored in the AWS Storage Gateway and your manager has come to you asking about how the billing is calculated, specifically the Virtual Tape Shelf usage. What would be a correct response to this?

<details><summary>Answer</summary>

**B. You are billed for the virtual tape data you store in Amazon Glacier and billed for the portion of virtual tape capacity that you use, not for the size of the virtual tape.**

</details>

### 100. ce-222

A company stores a file in an S3 bucket containing IP allow/deny lists. The file must be accessible via an HTTP endpoint. Firewalls outside AWS must read the file. The company wants to restrict access to only the firewall IP addresses. The S3 Block Public Access feature is enabled on the account. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Create a bucket policy that explicitly allows access only from the firewall IP addresses.**

An Amazon S3 bucket policy is the most direct and appropriate mechanism to control access to objects based on the source IP address. By using the aws:SourceIp condition key in the policy, you can explicitly grant s3:GetObject permission to a specific list of IP addresses (the firewalls). This method provides access via the standard S3 HTTP endpoint. Crucially, a bucket policy that restricts access to a specific set of IP addresses is not considered "public" by the S3 Block Public Access feature. Therefore, this solution is fully compatible with the account-level security setting and meets all requirements efficiently. Why Incorrect Options are Wrong: A. Hosting as a static website generally requires making objects public, which is prevented by the S3 Block Public Access setting enabled on the account. C. Origin Access Control (OAC) restricts access to the S3 bucket to the CloudFront dist

</details>

### 101. dt-225

How can you secure data at rest on an EBS volume?

<details><summary>Answer</summary>

**E. Use an encrypted file system on top of the EBS volume.**

</details>

### 102. et-226

A company collects data from thousands of remote devices by using a RESTful web services application that runs on an Amazon EC2 instance. The EC2 instance receives the raw data, transforms the raw data, and stores all the data in an Amazon S3 bucket. The number of remote devices will increase into the millions soon. The company needs a highly scalable solution that minimizes operational overhead. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use AWS Glue to process the raw data in Amazon S3.**

E. Use Amazon API Gateway to send the raw data to an Amazon Kinesis data stream. Configure Amazon Kinesis Data Firehose to use the data stream as a source to deliver the data to Amazon S3.  A. It automatically discovers the schema of the data and generates ETL code to transform it.  E. API Gateway can be used to receive the raw data from the remote devices via RESTful web services. It provides a scalable and managed infrastructure to handle the incoming requests. The data can then be sent to an Amazon Kinesis data stream, which is a highly scalable and durable real-time data streaming service. From there, Amazon Kinesis Data Firehose can be configured to use the data stream as a source and deliver the transformed data to Amazon S3. This combination of services allows for the seamless ingestion and processing of data while minimizing operational overhead.

</details>

### 103. et-227 `cost`

A company needs to retain its AWS CloudTrail logs for 3 years. The company is enforcing CloudTrail across a set of AWS accounts by using AWS Organizations from the parent account. The CloudTrail target S3 bucket is configured with S3 Versioning enabled. An S3 Lifecycle policy is in place to delete current objects after 3 years. After the fourth year of use of the S3 bucket, the S3 bucket metrics show that the number of objects has continued to rise. However, the number of new CloudTrail logs that are delivered to the S3 bucket has remained consistent. Which solution will delete objects that are older than 3 years in the MOST cost-effective manner?

<details><summary>Answer</summary>

**B. Configure the S3 Lifecycle policy to delete previous versions as well as current versions.**

S3 Lifecycle Policy: Enabling S3 versioning allows you to use a lifecycle policy to manage both current and previous versions of objects in the bucket. By configuring the S3 Lifecycle policy to delete objects older than 3 years, it will automatically delete both the current and previous versions that meet the specified criteria.

</details>

### 104. ce-228 `least-ops`

A financial company is migrating its banking applications to a set of AWS accounts managed by AWS Organizations. The applications will store sensitive customer data on Amazon Elastic Block Store (Amazon EBS) volumes. The company will take regular snapshots for backup purposes. The company wants to implement controls across all AWS accounts to prevent sharing EBS snapshots publicly. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Enable block public access for EBS snapshots at the organization level.**

The most effective and efficient solution is to use the "Block Public Access for EBS Snapshots" feature, enforced across the entire AWS Organization with a Service Control Policy (SCP). This is a preventive control that directly blocks API calls (ec2:ModifySnapshotAttribute) attempting to make an EBS snapshot public. Applying a single SCP at the organization's root or relevant Organizational Unit (OU) ensures that no user or role in any member account can publicly share snapshots. This approach directly satisfies the requirement to prevent public sharing with the least operational overhead. Why Incorrect Options are Wrong: A. AWS Config is a detective control. It can identify snapshots that are already public but does not prevent the action from occurring in the first place, creating a potential window of exposure. C. An IAM policy created in the management (root) account only applies to

</details>

### 105. ce-231 `least-ops`

A company is building a data analysis platform on AWS by using AWS Lake Formation. The platform will ingest data from different sources such as Amazon S3 and Amazon RDS. The company needs a secure solution to prevent access to portions of the data that contain sensitive information. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create data filters to implement row-level security and cell-level security.**

AWS Lake Formation provides native capabilities for fine-grained access control, including row-level and cell-level security, through a feature called "data filters." Data filters allow you to define policies that restrict which rows and columns users can see when they query the data. This is a managed, declarative approach that directly meets the requirement to prevent access to sensitive portions of data. Because it is a built-in feature of Lake Formation, it represents the solution with the least operational overhead compared to developing, deploying, and maintaining custom code with AWS Lambda. Why Incorrect Options are Wrong: A. IAM roles grant coarse-grained permissions (e.g., access to an entire table) and are insufficient for securing specific rows or cells within a table. C. Using a Lambda function to remove sensitive data before ingestion is a high-overhead solution that requir

</details>

### 106. dt-231

You are setting up some EBS volumes for a customer who has requested a setup which includes a RAID (redundant array of inexpensive disks). AWS has some recommendations for RAID setups. Which RAID setup is not recommended for Amazon EBS?

<details><summary>Answer</summary>

**B. RAID 5 and RAID 6.**

</details>

### 107. dt-232

Much of your company's data does not need to be accessed often, and can take several hours for retrieval time, so it's stored on Amazon Glacier. However someone within your organization has expressed concerns that his data is more sensitive than the other data, and is wondering whether the high level of encryption that he knows is on S3 is also used on the much cheaper Glacier service. Which of the following statements would be most applicable in regards to this concern?

<details><summary>Answer</summary>

**C. Amazon Glacier automatically encrypts the data using AES-256, the same as Amazon S3.**

</details>

### 108. dt-235

By default, EBS volumes that are created and attached to an instance at launch are deleted when that instance is terminated. You can modify this behavior by changing the value of the flag [...] to false when you launch the instance.

<details><summary>Answer</summary>

**A. Delete On Termination.**

</details>

### 109. dt-241

An AWS customer runs a public blogging website. The site users upload two million blog entries a month. The average blog entry size is 200 KB. The access rate to blog entries drops to negligible 6 months after publication and users rarely access a blog entry 1 year after publication. Additionally, blog entries have a high update rate during the first 3 months following publication, this drops to no updates after 6 months. The customer wants to use CloudFront to improve his user's load times. Which of the following recommendations would you make to the customer?

<details><summary>Answer</summary>

**C. Create a CloudFront distribution with S3 access restricted only to the CloudFront identity and partition the blog entry's location in S3 according to the month it was uploaded to be used withCloudFront behaviors.**

</details>

### 110. et-243

A medical research lab produces data that is related to a new study. The lab wants to make the data available with minimum latency to clinics across the country for their on-premises, file-based applications. The data files are stored in an Amazon S3 bucket that has read-only permissions for each clinic. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Deploy an AWS Storage Gateway file gateway as a virtual machine (VM) on premises at each clinic**

This option provides a way to present an S3 bucket as a file system to on-premises applications. Each clinic can deploy an AWS Storage Gateway file gateway as a VM on-premises, allowing them to access the data in the S3 bucket as if it were local files. It minimizes latency because the data is cached locally, and read-only permissions can be controlled at the S3 bucket level.

</details>

### 111. et-249

A company is implementing a shared storage solution for a media application that is hosted in the AWS Cloud. The company needs the ability to use SMB clients to access data. The solution must be fully managed. Which AWS solution meets these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Windows File Server file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Windows File Server is a fully managed file storage service that supports the SMB protocol. It provides a native Windows file system experience and is designed to be accessed by SMB clients. This option meets the requirements for a fully managed shared storage solution accessible via SMB.

</details>

### 112. gh-249

249Topic 1
A company is implementing a shared storage solution for a media application that is hosted in the AWS Cloud. The company needs the ability to use SMB clients to access data. The solution must be fully managed.
Which AWS solution meets these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Windows File Server file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Windows File Server is a fully managed file storage service that supports the SMB protocol. It provides a native Windows file system experience and is designed to be accessed by SMB clients. This option meets the requirements for a fully managed shared storage solution accessible via SMB.

</details>

### 113. et-250

A company’s security team requests that network traffic be captured in VPC Flow Logs. The logs will be frequently accessed for 90 days and then accessed intermittently. What should a solutions architect do to meet these requirements when configuring the logs?

<details><summary>Answer</summary>

**D. Use Amazon S3 as the target. Enable an S3 Lifecycle policy to transition the logs to S3 Standard-Infrequent Access (S3 Standard-IA) after 90 days.**

Amazon S3 is a scalable and cost-effective object storage service. Enabling an S3 Lifecycle policy to transition logs to S3 Standard-Infrequent Access (S3 Standard-IA) after 90 days is a suitable solution. This approach allows you to store the logs in a cost-effective manner, automatically moving them to a lower-cost storage class after the initial 90 days.

</details>

### 114. et-252

A solutions architect needs to design a system to store client case files. The files are core company assets and are important. The number of files will grow over time. The files must be simultaneously accessible from multiple application servers that run on Amazon EC2 instances. The solution must have built-in redundancy. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Amazon Elastic File System (Amazon EFS)**

</details>

### 115. et-256

A solutions architect is implementing a document review application using an Amazon S3 bucket for storage. The solution must prevent accidental deletion of the documents and ensure that all versions of the documents are available. Users must be able to download, modify, and upload documents. Which combination of actions should be taken to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Enable versioning on the bucket.**

D. Enable MFA Delete on the bucket. B. allows multiple versions of objects in the S3 bucket to be stored. This ensures that all versions of the documents are available, even if they are accidentally overwritten or deleted.  D. adds an extra layer of protection against accidental deletion of objects in the bucket. With MFA Delete enabled, a user would need to provide an additional authentication factor to successfully delete objects from the bucket. This helps prevent accidental or unauthorized deletions and provides an extra level of security for critical documents.

</details>

### 116. ce-257

A company must protect sensitive documents in Amazon S3 from deletion or modification for a fixed retention period to meet regulatory requirements. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Enable S3 Object Lock in compliance mode.**

To meet strict regulatory requirements for data retention, a Write-Once, Read-Many (WORM) model is needed. Amazon S3 Object Lock provides this capability. The "compliance mode" is the stricter of the two retention modes. In compliance mode, a protected object version cannot be overwritten or deleted by any user, including the root user in the AWS account, for the duration of the retention period. This ensures the object's immutability, which is essential for satisfying regulatory compliance mandates. Why Incorrect Options are Wrong: A. In governance mode, users with special IAM permissions can bypass retention settings, which may not be sufficient for strict regulatory compliance. C. S3 versioning protects against accidental deletion but does not prevent intentional deletion by a user with sufficient permissions. D. Transitioning objects to S3 Glacier is a storage tiering strategy for co

</details>

### 117. et-259

A company is implementing new data retention policies for all databases that run on Amazon RDS DB instances. The company must retain daily backups for a minimum period of 2 years. The backups must be consistent and restorable. Which solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Create a backup vault in AWS Backup to retain RDS backups. Create a new backup plan with a daily schedule and an expiration period of 2 years after creation. Assign the RDS DB instances to the backup plan.**

</details>

### 118. et-260

A company’s compliance team needs to move its file shares to AWS. The shares run on a Windows Server SMB file share. A self-managed on- premises Active Directory controls access to the files and folders. The company wants to use Amazon FSx for Windows File Server as part of the solution. The company must ensure that the on-premises Active Directory groups restrict access to the FSx for Windows File Server SMB compliance shares, folders, and files after the move to AWS. The company has created an FSx for Windows File Server file system. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Join the file system to the Active Directory to restrict access.**

Join the File System to Active Directory:  By joining the FSx for Windows File Server file system to the on-premises Active Directory, you extend the trust relationship to AWS. This ensures that access control is based on the on-premises Active Directory groups, allowing you to continue using the existing groups to restrict access to shares, folders, and files. After joining the file system to Active Directory, you can manage access controls using the existing Active Directory groups. Users and groups from the on-premises Active Directory can be granted appropriate permissions on the FSx file system.

</details>

### 119. et-270

A company is using a centralized AWS account to store log data in various Amazon S3 buckets. A solutions architect needs to ensure that the data is encrypted at rest before the data is uploaded to the S3 buckets. The data also must be encrypted in transit. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Use client-side encryption to encrypt the data that is being uploaded to the S3 buckets.**

</details>

### 120. dt-273

Your firm has uploaded a large amount of aerial image data to S3. In the past, in your on-premises environment, you used a dedicated group of servers to often process this data and used Rabbit MQ, an open source messaging system to get job information to the servers. Once processed, the data would go to tape and be shipped offsite. Your manager told you to stay with the current design, and leverage AWS archival storage and messaging services to minimize cost. Which is correct?

<details><summary>Answer</summary>

**D. Use SNS to pass job messages. Use Cloud Watch alarms to terminate spot worker instances when they become idle. Once data is processed, change the storage class of the S3 object to Glacier.**

</details>

### 121. et-278

A company wants to create an application to store employee data in a hierarchical structured relationship. The company needs a minimum-latency response to high-traffic queries for the employee data and must protect any sensitive data. The company also needs to receive monthly email messages if any financial information is present in the employee data. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Use Amazon DynamoDB to store the employee data in hierarchies. Export the data to Amazon S3 every month.**

E. Configure Amazon Macie for the AWS account. Integrate Macie with Amazon EventBridge to send monthly notifications through an Amazon Simple Notification Service (Amazon SNS) subscription.  Amazon DynamoDB is a highly scalable, low-latency NoSQL database that can efficiently store hierarchical data. Exporting the data to Amazon S3 every month allows further analysis and integration with other AWS services.  Amazon Macie is a security service that automatically discovers, classifies, and protects sensitive data. Integrating Macie with EventBridge allows you to set up monthly events and send notifications through Amazon SNS if financial information is detected.

</details>

### 122. dt-285

When controlling access to Amazon EC2 resources, each Amazon EBS Snapshot has a [...] attribute that controls which AWS accounts can use the snapshot.

<details><summary>Answer</summary>

**A. createVolumePermission.**

</details>

### 123. et-286

A company has a static website that is hosted on Amazon CloudFront in front of Amazon S3. The static website uses a database backend. The company notices that the website does not reflect updates that have been made in the website’s Git repository. The company checks the continuous integration and continuous delivery (CI/CD) pipeline between the Git repository and Amazon S3. The company verifies that the webhooks are configured properly and that the CI/CD pipeline is sending messages that indicate successful deployments. A solutions architect needs to implement a solution that displays the updates on the website. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Invalidate the CloudFront cache.**

When the website does not reflect updates that have been made in the Git repository, and the CI/CD pipeline is sending messages indicating successful deployments, it's likely that the issue is related to caching. Amazon CloudFront caches content to improve performance and reduce latency, and if the cache is not updated, it may serve stale content.  By invalidating the CloudFront cache, you ensure that the next request to CloudFront fetches the latest content from the origin (in this case, Amazon S3). This process forces CloudFront to re-fetch the content and update its cache.

</details>

### 124. et-288

A company is migrating a Linux-based web server group to AWS. The web servers must access files in a shared file store for some content. The company must not make any changes to the application. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Elastic File System (Amazon EFS) file system. Mount the EFS file system on all web servers.**

To meet the requirement of providing a shared file store for Linux-based web servers without making changes to the application, you can use Amazon Elastic File System (Amazon EFS). Amazon EFS is a scalable and fully managed file storage service that can be easily mounted on multiple EC2 instances.

</details>

### 125. ce-289 `least-ops`

A company temporarily stages transactional datasets in an Amazon S3 bucket before the company moves the datasets to their final destinations. Some datasets include personally identifiable information PII. The company must remove PII data during staging before the company moves the datasets to their destinations. A solutions architect needs to configure Amazon Macie to continuously monitor the datasets. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Set up Amazon Macie automated sensitive data discovery. Create an AWS Lambda function to remove the PII data that Macie finds. Configure an Amazon EventBridge rule to invoke the Lambda function when Macie discovers PII data.**

Amazon Macie's automated sensitive data discovery is designed for continuous, low-overhead monitoring of S3 buckets. It intelligently samples and analyzes objects as they are added or modified, minimizing cost and operational effort. When Macie generates a finding for PII, it can be published to Amazon EventBridge. An EventBridge rule can then trigger an AWS Lambda function to perform the remediation task of removing the identified PII. This creates a fully automated, event-driven, and serverless workflow with the least operational overhead compared to manual or scheduled approaches. Why Incorrect Options are Wrong: A. This requires custom logic to manage job execution state, which increases operational overhead compared to the built-in automated discovery feature. C. A daily scheduled job is not continuous monitoring and introduces significant delays (up to 24 hours) in detecting and re

</details>

### 126. dt-296

You are working with a customer who has 10 TB of archival data that they want to migrate to Amazon Glacier. The customer has a 1-Mbps connection to the Internet. Which service or feature provides the fastest method of getting the data into Amazon Glacier?

<details><summary>Answer</summary>

**A. Amazon Glacier multipart upload.**

</details>

### 127. et-299

A research laboratory needs to process approximately 8 TB of data. The laboratory requires sub-millisecond latencies and a minimum throughput of 6 GBps for the storage subsystem. Hundreds of Amazon EC2 instances that run Amazon Linux will distribute and process the data. Which solution will meet the performance requirements?

<details><summary>Answer</summary>

**B. Create an Amazon S3 bucket to store the raw data. Create an Amazon FSx for Lustre file system that uses persistent SSD storage. Select the option to import data from and export data to Amazon S3. Mount the file system on the EC2 instances.**

Amazon FSx for Lustre is a high-performance file system designed for use with compute-intensive workloads. It provides sub-millisecond latencies and is well-suited for scenarios where high throughput is required. Using persistent SSD storage for the Amazon FSx for Lustre file system ensures that it meets the minimum throughput requirement of 6 GBps. Storing the raw data in an Amazon S3 bucket allows for scalable and durable storage, and the integration with FSx for Lustre allows seamless importing and exporting of data to and from S3. This solution is designed to provide the required performance characteristics for processing large amounts of data with hundreds of EC2 instances.

</details>

### 128. ce-302

A company needs to allow AWS Account B and Account C to send AWS CloudTrail logs to a centralized Amazon S3 bucket in Account A. The company does not have full control over the source CloudTrail logs from Accounts B and C. The company needs to ensure that only CloudTrail logs can be written to the S3 bucket in Account A. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. In Account A, create an S3 bucket policy that allows the CloudTrail service principal to write to the S3 bucket. Use the aws:SourceAccount condition in the bucket policy to allow access to only Accounts B and C.**

This is the standard and most secure method for centralizing CloudTrail logs. The S3 bucket policy in the central account (Account A) should grant the CloudTrail service principal (cloudtrail.amazonaws.com) permission to write objects (s3:PutObject). To ensure that only CloudTrail logs from the specified source accounts (B and C) can be written, the policy must include a Condition block. The aws:SourceAccount global condition key restricts access to principals acting on behalf of the specified accounts, preventing unauthorized accounts or services from writing to the bucket. Why Incorrect Options are Wrong: A. S3 gateway endpoints control traffic from a VPC to S3. They do not control which AWS service or source account can write to a bucket. B. Using only aws:SourceAccount is insufficient. It would allow any principal from the source accounts to write to the bucket, not just the CloudTra

</details>

### 129. dt-304

EBS Snapshots occur [...].

<details><summary>Answer</summary>

**A. Asynchronously.**

</details>

### 130. et-304 `least-ops`

A company recently created a disaster recovery site in a different AWS Region. The company needs to transfer large amounts of data back and forth between NFS file systems in the two Regions on a periodic basis. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS DataSync.**

If we want to transfer large amount of data we can used AWS Datasync.

</details>

### 131. et-305

A company is designing a shared storage solution for a gaming application that is hosted in the AWS Cloud. The company needs the ability to use SMB clients to access data. The solution must be fully managed. Which AWS solution meets these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon FSx for Windows File Server file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Windows File Server is a fully managed file storage service that is compatible with the Server Message Block (SMB) protocol, making it suitable for use with SMB clients, including Windows-based systems. With Amazon FSx for Windows File Server, you can create a file system that can be mounted on application servers, providing shared storage for the gaming application. Amazon FSx for Windows File Server handles the management aspects such as server provisioning, maintenance, and backups, making it a fully managed solution.

</details>

### 132. ce-307

A company hosts a website on Amazon EC2 instances. The website processes classified data. The company stores the processed data in an Amazon S3 bucket. Because of security concerns, the company must ensure that traffic between the EC2 instances and the S3 bucket does not use public IP addresses. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a gateway endpoint for Amazon S3. Configure an S3 bucket policy to allow access from the endpoint.**

The core requirement is to ensure that traffic between EC2 instances in a VPC and an S3 bucket does not traverse the public internet. A gateway VPC endpoint for Amazon S3 is designed for this exact purpose. It provides a private connection by creating a target for a route in your VPC route table for traffic destined for S3. This ensures that all communication from the EC2 instances to S3 stays within the secure AWS network, without needing public IP addresses, an internet gateway, or a NAT gateway. Why Incorrect Options are Wrong: B. An EC2 instance profile grants permissions (authentication/authorization) to access S3 but does not control the network path the traffic takes. C. A NAT gateway is used to route traffic from a private subnet to the public internet, which is the opposite of the desired outcome. D. Using IAM user credentials on an EC2 instance is a security anti-pattern and, l

</details>

### 133. et-307

A company that primarily runs its application servers on premises has decided to migrate to AWS. The company wants to minimize its need to scale its Internet Small Computer Systems Interface (iSCSI) storage on premises. The company wants only its recently accessed data to remain stored locally. Which AWS solution should the company use to meet these requirements?

<details><summary>Answer</summary>

**D. AWS Storage Gateway Volume Gateway cached volumes**

AWS Storage Gateway provides a hybrid cloud storage service that enables on-premises applications to use cloud storage seamlessly. Volume Gateway offers two modes: cached volumes and stored volumes. In the cached volumes mode, the entire dataset is stored in Amazon S3, and the most frequently accessed data is cached on-premises. This allows the company to keep recently accessed data locally, minimizing the need for on-premises scaling.

</details>

### 134. ce-308

A company is building a compute-intensive application that will run on a fleet of Amazon EC2 instances. The application uses attached Amazon EBS volumes for storing data. The EBS volumes will be created at time of initial deployment. The application will process sensitive information. All of the data must be encrypted. The solution should not impact the application's performance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure the fleet of EC2 instances to use encrypted EBS volumes to store data.**

The most effective solution is to use Amazon EBS encryption. This feature provides seamless encryption of data at rest on the volume, data in transit between the EC2 instance and the volume, and all snapshots created from the volume. The encryption and decryption processes are handled transparently by the hardware on the underlying EC2 host server. This offloads the cryptographic processing from the instance's CPU, ensuring there is minimal impact on the performance of the compute-intensive application, thereby meeting all the stated requirements efficiently and securely. Why Incorrect Options are Wrong: B. This option changes the required storage architecture from block storage (EBS) to object storage (S3), which contradicts the scenario's explicit use of attached EBS volumes. C. Implementing custom, application-level encryption would consume significant CPU resources on the EC2 instanc

</details>

### 135. dt-310

A newspaper organization has a on-premises application which allows the public to search its back catalogue and retrieve individual newspaper pages via a website written in Java They have scanned the old newspapers into JPEGs (approx 17TB) and used Optical Character Recognition (OCR) to populate a commercial search product. The hosting platform and software are now end of life and the organization wants to migrate Its archive to AWS and produce a cost efficient architecture and still be designed for availability and durability. Which is the most appropriate?

<details><summary>Answer</summary>

**C. Use S3 with standard redundancy to store and serve the scanned files, use Cloud5earch for query processing, and use Elastic Beanstalk to host the website across multiple Availability Zones.**

</details>

### 136. et-310 `performance`

A company sells datasets to customers who do research in artificial intelligence and machine learning (AI/ML). The datasets are large, formatted files that are stored in an Amazon S3 bucket in the us-east-1 Region. The company hosts a web application that the customers use to purchase access to a given dataset. The web application is deployed on multiple Amazon EC2 instances behind an Application Load Balancer. After a purchase is made, customers receive an S3 signed URL that allows access to the files. The customers are distributed across North America and Europe. The company wants to reduce the cost that is associated with data transfers and wants to maintain or improve performance. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an Amazon CloudFront distribution with the existing S3 bucket as the origin. Direct customer requests to the CloudFront URL. Switch to CloudFront signed URLs for access control.**

Amazon CloudFront: CloudFront is a content delivery network (CDN) service that distributes content globally with low latency and high data transfer speeds. It helps reduce data transfer costs and improves performance by caching content at edge locations. S3 Bucket as the Origin: By configuring the existing S3 bucket as the origin for CloudFront, you allow CloudFront to cache and serve the datasets from edge locations around the world. CloudFront Signed URLs: CloudFront provides the ability to generate signed URLs, allowing you to control access to your content. You can use CloudFront signed URLs for access control, providing a secure way for customers to access datasets.

</details>

### 137. dt-311

A Provisioned IOPS volume must be at least [...] GB in size.

<details><summary>Answer</summary>

**D. 10.**

</details>

### 138. dt-312

In Amazon EC2, while sharing an Amazon EBS snapshot, can the snapshots with AWS Marketplace product codes be public?

<details><summary>Answer</summary>

**C. No, they cannot be made public.**

</details>

### 139. et-312

A company has an application that runs on several Amazon EC2 instances. Each EC2 instance has multiple Amazon Elastic Block Store (Amazon EBS) data volumes attached to it. The application’s EC2 instance configuration and data need to be backed up nightly. The application also needs to be recoverable in a different AWS Region. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create a backup plan by using AWS Backup to perform nightly backups. Copy the backups to another Region. Add the application’s EC2 instances as resources.**

AWS Backup: AWS Backup is a fully managed backup service that centralizes and automates the backup of data across AWS services. It provides a simple and efficient way to back up your EC2 instances and their associated EBS volumes. Backup Plan: With AWS Backup, you can create backup plans to define when and how your backups are performed. Backup plans allow you to schedule nightly backups and define retention policies. Explanation: Adding only the EBS volumes as resources backs up the data but not the instance configuration, so recovery would mean manually rebuilding the EC2 instance and reattaching volumes. Adding the EC2 instances themselves as resources backs up the instance and its attached volumes together, in one operationally simpler recovery step.

</details>

### 140. et-321

What should a solutions architect do to ensure that all objects uploaded to an Amazon S3 bucket are encrypted?

<details><summary>Answer</summary>

**D. Update the bucket policy to deny if the PutObject does not have an x-amz-server-side-encryption header set.**

x-amz-server-side-encryption header: This header specifies the server-side encryption algorithm to be used for the object. If an object is uploaded without the x-amz-server-side-encryption header or with an incorrect value, it can be denied.

</details>

### 141. dt-322

Which Amazon storage do you think is the best for my database-style applications that frequently encounter many random reads and writes across the dataset?

<details><summary>Answer</summary>

**D. Amazon EBS.**

</details>

### 142. et-324

A company wants to implement a disaster recovery plan for its primary on-premises file storage volume. The file storage volume is mounted from an Internet Small Computer Systems Interface (iSCSI) device on a local storage server. The file storage volume holds hundreds of terabytes (TB) of data. The company wants to ensure that end users retain immediate access to all file types from the on-premises systems without experiencing latency. Which solution will meet these requirements with the LEAST amount of change to the company's existing infrastructure?

<details><summary>Answer</summary>

**D. Provision an AWS Storage Gateway Volume Gateway stored volume with the same amount of disk space as the existing file storage volume. Mount the Volume Gateway stored volume to the existing file server by using iSCSI, and copy all files to the storage volume. Configure scheduled snapshots of the storage volume. To recover from a disaster, restore a snapshot to an Amazon Elastic Block Store (Amazon EBS) volume and attach the EBS volume to an Amazon EC2 instance.**

Explanation: A cached volume only keeps the most frequently accessed data locally — anything not in cache has to be fetched from S3 first, adding latency, so it fails the "immediate access to all file types" requirement. A stored volume keeps the entire dataset on-premises (with async backup to S3), giving true zero-latency access to every file.

</details>

### 143. dt-327

True or False: Manually created DB Snapshots are deleted after the DB Instance is deleted.

<details><summary>Answer</summary>

**A. True.**

</details>

### 144. dt-328

Amazon S3 doesn't automatically give a user who creates [...] permission to perform other actions on that bucket or object.

<details><summary>Answer</summary>

**B. a bucket or object.**

</details>

### 145. dt-329

A company wants to review the security requirements of Glacier. Which of the below mentioned statements is true with respect to the AWS Glacier data security?

<details><summary>Answer</summary>

**A. All data stored on Glacier is protected with AES-256 serverside encryption.**

</details>

### 146. dt-330

What does Amazon EBS stand for?

<details><summary>Answer</summary>

**D. Elastic Block Store.**

</details>

### 147. et-331

A company must migrate 20 TB of data from a data center to the AWS Cloud within 30 days. The company’s network bandwidth is limited to 15 Mbps and cannot exceed 70% utilization. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Snowball.**

AWS Snowball is a physical data transport solution that helps customers transfer large amounts of data into and out of AWS. It addresses challenges associated with large-scale data transfers, particularly when network constraints, transfer times, or security concerns make online data transfer less practical.

</details>

### 148. et-332 `security`

A company needs to provide its employees with secure access to confidential and sensitive files. The company wants to ensure that the files can be accessed only by authorized users. The files must be downloaded securely to the employees’ devices. The files are stored in an on-premises Windows file server. However, due to an increase in remote usage, the file server is running out of capacity. . Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the files to an Amazon FSx for Windows File Server file system. Integrate the Amazon FSx file system with the on-premises Active Directory. Configure AWS Client VPN.**

Amazon FSx for Windows File Server: It is a fully managed file storage service built on Windows Server. It is designed to be integrated with on-premises Active Directory, allowing for a seamless extension of your existing directory and authentication infrastructure to the AWS Cloud.  Integrate with On-Premises Active Directory: With Amazon FSx, you can integrate the file system with your on-premises Active Directory, ensuring that the same user accounts and permissions are used both on-premises and in the cloud.

</details>

### 149. et-334 `least-ops`

A company wants to give a customer the ability to use on-premises Microsoft Active Directory to download files that are stored in Amazon S3. The customer’s application uses an SFTP client to download the files. Which solution will meet these requirements with the LEAST operational overhead and no changes to the customer’s application?

<details><summary>Answer</summary>

**A. Set up AWS Transfer Family with SFTP for Amazon S3. Configure integrated Active Directory authentication.**

AWS Transfer Family with SFTP for Amazon S3: AWS Transfer Family is a fully managed service that allows you to set up an SFTP (Secure File Transfer Protocol) service for Amazon S3. It enables you to transfer files directly to and from Amazon S3 using the SFTP protocol.  Integrated Active Directory Authentication: AWS Transfer Family allows you to configure authentication with Microsoft Active Directory. By integrating with Active Directory, you can provide users with seamless access to S3 resources using their existing credentials without modifying their applications.

</details>

### 150. dt-342

One of the criteria for a new deployment is that the customer wants to use AWS Storage Gateway. However you are not sure whether you should use gateway-cached volumes or gateway-stored volumes or even what the differences are. Which statement below best describes those differences?

<details><summary>Answer</summary>

**A. Gateway-cached lets you store your data in Amazon Simple Storage Service (Amazon S3) and retain a copy of frequently accessed data subsets locally. Gateway-stored enables you to configure your on-premises gateway to store all your data locally and then asynchronously back up point-in-time snapshots of this data to Amazon S3.**

</details>

### 151. ce-345 `least-ops`

A company has a web application that stores user transactions in an Amazon DynamoDB table. To comply with regulations, the company must retain a copy of user transaction data for 7 years. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS Backup to create backup schedules and retention policies for the table.**

AWS Backup is a fully managed service designed to centralize and automate data protection across AWS services, including Amazon DynamoDB. It allows you to create backup plans that define backup schedules, retention policies, and lifecycle rules. A backup plan can be configured to take regular backups of the DynamoDB table and retain them for 7 years, automatically transitioning older backups to cold storage to reduce costs. This approach fully meets the requirements with the least operational overhead, as it eliminates the need for custom scripts, manual processes, or managing individual service integrations. Why Incorrect Options are Wrong: A. DynamoDB point-in-time recovery (PITR) only allows for restores to any point in time within the last 35 days, which does not meet the 7-year retention requirement. C. On-demand backups are manual, user-initiated processes. Relying on this method f

</details>

### 152. et-346

A company has an aging network-attached storage (NAS) array in its data center. The NAS array presents SMB shares and NFS shares to client workstations. The company does not want to purchase a new NAS array. The company also does not want to incur the cost of renewing the NAS array’s support contract. Some of the data is accessed frequently, but much of the data is inactive. A solutions architect needs to implement a solution that migrates the data to Amazon S3, uses S3 Lifecycle policies, and maintains the same look and feel for the client workstations. The solutions architect has identified AWS Storage Gateway as part of the solution. Which type of storage gateway should the solutions architect provision to meet these requirements?

<details><summary>Answer</summary>

**D. Amazon S3 File Gateway**

Amazon S3 File Gateway provides on-premises applications with access to virtually unlimited cloud storage using NFS and SMB file interfaces. It seamlessly moves frequently accessed data to a low-latency cache while storing colder data in Amazon S3, using S3 Lifecycle policies to transition data between storage classes over tim

</details>

### 153. dt-349

If an Amazon EBS volume is the root device of an instance, can I detach it without stopping the instance?

<details><summary>Answer</summary>

**C. No.**

</details>

### 154. dt-351

Before I delete an EBS volume, what can I do if I want to recreate the volume later?

<details><summary>Answer</summary>

**B. Store a snapshot of the volume.**

</details>

### 155. ce-352 `availability`

A company is testing an application that runs on an Amazon EC2 Linux instance. A single 500 GB Amazon Elastic Block Store (Amazon EBS) General Purpose SSD (gp2) volume is attached to the EC2 instance. The company will deploy the application on multiple EC2 instances in an Auto Scaling group. All instances require access to the data that is stored in the EBS volume. The company needs a highly available and resilient solution that does not introduce significant changes to the application's code. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Provision an Amazon Elastic File System (Amazon EFS) file system. Configure the file system to use General Purpose performance mode.**

The core requirement is to provide a highly available, shared file storage solution for multiple Linux EC2 instances. Amazon Elastic File System (Amazon EFS) is a fully managed service designed for this exact use case. EFS provides a simple, scalable, elastic file system for Linux-based workloads. It can be mounted concurrently on multiple EC2 instances across different Availability Zones using the standard NFSv4.1 protocol. This architecture is inherently highly available and resilient, meeting the requirements without needing application code modifications. The General Purpose performance mode is the default and suitable for a wide range of applications. Why Incorrect Options are Wrong: A: An EC2 instance configured as an NFS server represents a single point of failure, which does not meet the high availability and resilience requirement. B: Amazon FSx for Windows File Server is optimi

</details>

### 156. dt-352

An accountant asks you to design a small VPC network for him and, due to the nature of his business, just needs something where the workload on the network will be low, and dynamic data will be accessed infrequently. Being an accountant, low cost is also a major factor. Which EBS volume type would best suit his requirements?

<details><summary>Answer</summary>

**A. Magnetic.**

</details>

### 157. dt-354

A customer implemented AWS Storage Gateway with a gateway-cached volume at their main office. An event takes the link between the main and branch office offline. Which methods will enable the branch office to access their data? (Choose 3 answers)

<details><summary>Answer</summary>

**D. Launch a new AWS Storage Gateway instance AMI in Amazon EC2, and restore from a gateway snapshot.; E. Create an Amazon EBS volume from a gateway snapshot, and mount it to an Amazon EC2 instance.; F. Launch an AWS Storage Gateway virtual iSCSI device at the branch office, and restore from a gateway snapshot.**

</details>

### 158. ce-358

A company has an application that processes information from documents that users upload. When a user uploads a new document to an Amazon S3 bucket, an AWS Lambda function is invoked. The Lambda function processes information from the documents. The company discovers that the application did not process many recently uploaded documents. The company wants to ensure that the application processes each document with retries if there is an error during the first attempt to process the document. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure an Amazon Simple Queue Service (Amazon SQS) queue as an event source for the Lambda function. Configure an S3 event notification on the S3 bucket to send new document upload events to the SQS queue.**

This solution introduces an Amazon SQS queue between Amazon S3 and the AWS Lambda function, which effectively decouples the components and increases reliability. When a document is uploaded, S3 sends an event message to the SQS queue. The queue durably stores the message until the Lambda function successfully processes it. If the Lambda function fails, the message remains in the queue and will be retried after a configurable visibility timeout. This pattern ensures that events are not lost due to transient processing failures. By configuring a dead-letter queue (DLQ) on the SQS queue, messages that consistently fail can be isolated for analysis, preventing processing loops while guaranteeing no data is lost. Why Incorrect Options are Wrong: A. API Gateway is used for creating RESTful APIs that are invoked by HTTP requests. It is not a suitable trigger for events originating from an S3 bu

</details>

### 159. ce-359

A developer needs to export the contents of several Amazon DynamoDB tables into Amazon S3 buckets to comply with company data regulations. The developer uses the AWS CLI to runcommands to export from each table to the proper S3 bucket. The developer sets up AWS credentials correctly and grants resources appropriate permissions. However, the exports of some tables fail. What should the developer do to resolve this issue?

<details><summary>Answer</summary>

**A. Ensure that point-in-time recovery is enabled on the DynamoDB tables.**

The native DynamoDB export to Amazon S3 feature is built upon the Point-in-Time Recovery (PITR) mechanism. To perform an export, DynamoDB uses a snapshot of the table from a specific point in time. Therefore, a mandatory prerequisite for using the export-to-S3 functionality is that PITR must be enabled on the source DynamoDB table. The scenario states that some exports are failing while others succeed, which strongly suggests that this prerequisite is met for some tables but not for the ones that are failing. Why Incorrect Options are Wrong: B. The target S3 bucket does not need to be in the same AWS Region as the DynamoDB table; cross-region exports are supported. C. DynamoDB Streams are used for capturing a time-ordered sequence of item-level modifications, not for performing a full table export. D. DynamoDB Accelerator (DAX) is an in-memory cache for DynamoDB and is unrelated to the p

</details>

### 160. ce-364

An insurance company runs an application on premises to process contracts. The application processes jobs that are comprised of many tasks. The individual tasks run for up to 5 minutes. Some jobs can take up to 24 hours in total to finish. If a task fails, the task must be reprocessed. The company wants to migrate the application to AWS. The company will use Amazon S3 as part of the solution. The company wants to configure jobs to start automatically when a contract is uploaded to an S3 bucket. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use a state machine in AWS Step Functions to handle the overall contract processing job. Configure the S3 bucket to send an event notification to Amazon EventBridge. Create a rule in Amazon EventBridge to target the state machine.**

The scenario requires orchestrating a long-running workflow (up to 24 hours) composed of multiple, distinct tasks that need state management and retry capabilities. AWS Step Functions is the ideal service for this use case. A Standard Workflow in Step Functions can run for up to one year, easily accommodating the 24-hour requirement. It provides built-in state management, error handling, and retry logic, which directly addresses the need to reprocess failed tasks. Using an S3 event notification to Amazon EventBridge, which then triggers the Step Functions state machine, is a robust and recommended pattern for initiating such workflows automatically. Why Incorrect Options are Wrong: A. A primary AWS Lambda function cannot orchestrate a job for 24 hours because Lambda functions have a maximum execution timeout of 15 minutes. C. While AWS Batch can run long jobs, AWS Step Functions is the s

</details>

### 161. dt-364

Amazon S3 allows you to set per-file permissions to grant read and/or write access. However you have decided that you want an entire bucket with 100 files already in it to be accessible to the public. You don't want to go through 100 files individually and set permissions. What would be the best way to do this?

<details><summary>Answer</summary>

**B. Add a bucket policy to the bucket.**

</details>

### 162. dt-366

Which of the following are use cases for Amazon DynamoDB? (Choose 3 answers)

<details><summary>Answer</summary>

**B. Managing web sessions.; C. Storing JSON documents.; D. Storing metadata for Amazon S3 objects.**

</details>

### 163. dt-367

You have been asked to set up a database in AWS that will require frequent and granular updates. You know that you will require a reasonable amount of storage space but are not sure of the best option. What is the recommended storage option when you run a database on an instance with the above criteria?

<details><summary>Answer</summary>

**B. Amazon EBS.**

</details>

### 164. dt-369

An organization has developed a mobile application which allows end users to capture a photo on their mobile device, and store it inside an application. The application internally uploads the data to AWS S3. The organization wants each user to be able to directly upload data to S3 using their Google ID. How will the mobile app allow this?

<details><summary>Answer</summary>

**A. Use the AWS Web identity federation for mobile applications, and use it to generate temporary security credentials for each user.**

</details>

### 165. ce-370 `cost`

A company runs a website that allows users to connect with lawyers. Users and lawyers upload documents to the website frequently. The company hosts the website on a single Amazon EC2 instance. The website stores documents directly on the instance. The company scales the website by adding two more EC2 instances behind an Application Load Balancer ALB. Afterwards, users report 404 Resource Not Found errors when the users try to access their documents. The company must restore access to the documents. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**A. Set up an Amazon EFS file system. Mount the file system on all the instances. Copy all files from each instance to the file system. Update the application to use the file system.**

The root cause of the 404 errors is that each EC2 instance has its own local storage. When a user uploads a document, it is saved to one instance, but subsequent requests to retrieve it may be routed to other instances that do not have the file. The most direct and effective solution is to implement a shared file system. Amazon EFS provides a managed, scalable file system that can be mounted concurrently by multiple EC2 instances. By migrating the documents to a central EFS file system and updating the application to use this shared location, all instances will have access to all documents, resolving the 404 errors. Why Incorrect Options are Wrong: B. Migrating to Amazon S3 requires significant application refactoring from file system calls to API calls, which is more complex than mounting a shared file system. C. Using a cron job to sync files to EFS is inefficient and introduces data c

</details>

### 166. et-371 `least-ops`

A company needs to create an Amazon Elastic Kubernetes Service (Amazon EKS) cluster to host a digital media streaming application. The EKS cluster will use a managed node group that is backed by Amazon Elastic Block Store (Amazon EBS) volumes for storage. The company must encrypt all data at rest by using a customer managed key that is stored in AWS Key Management Service (AWS KMS). Which combination of actions will meet this requirement with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**C. Enable EBS encryption by default in the AWS Region where the EKS cluster will be created. Select the customer managed key as the default key.**

D. Create the EKS cluster. Create an IAM role that has a policy that grants permission to the customer managed key. Associate the role with the EKS cluster.  EBS encryption is set regionally. AWS account is global but it does not mean EBS encryption is enable by default at account level. default EBS encryption is a regional setting within your AWS account. Enabling it in a specific region ensures that all new EBS volumes created in that region are encrypted by default, using either the default AWS managed key or a customer managed key that you specify.

</details>

### 167. dt-373

True or False: When you perform a restore operation to a point in time or from a DB Snapshot, a new DB Instance is created with a new endpoint.

<details><summary>Answer</summary>

**A. True.**

</details>

### 168. et-373 `cost`

A company has an application that collects data from IoT sensors on automobiles. The data is streamed and stored in Amazon S3 through Amazon Kinesis Data Firehose. The data produces trillions of S3 objects each year. Each morning, the company uses the data from the previous 30 days to retrain a suite of machine learning (ML) models. Four times each year, the company uses the data from the previous 12 months to perform analysis and train other ML models. The data must be available with minimal delay for up to 1 year. After 1 year, the data must be retained for archival purposes. Which storage solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Use the S3 Standard storage class. Create an S3 Lifecycle policy to transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days, and then to S3 Glacier Deep Archive after 1 year.**

S3 Standard Storage Class:  Use S3 Standard for the first 30 days because it's the default storage class for frequently accessed data. This is suitable for the initial period when you need quick and frequent access to your data. S3 Standard-Infrequent Access (S3 Standard-IA) Storage Class: After the initial 30 days, transition the data to S3 Standard-IA. S3 Standard-IA is designed for data that is accessed less frequently but still requires quick retrieval when needed. It's more cost-effective for data that is accessed less often compared to S3 Standard. S3 Glacier Deep Archive: After 1 year, transition the data from S3 Standard-IA to S3 Glacier Deep Archive using an S3 Lifecycle policy. S3 Glacier Deep Archive is the most cost-effective option for long-term archival storage. This is suitable for storing data that you need to retain for compliance or archival purposes but don't need to access frequently.

</details>

### 169. dt-374

What is the Reduced Redundancy option in Amazon S3?

<details><summary>Answer</summary>

**A. Less redundancy for a lower cost.**

</details>

### 170. ce-381

A company runs a content management system on an Amazon Elastic Container Service (Amazon ECS) cluster. The system allows visitors to provide feedback about the company's products by uploading documents and photos of the products to an Amazon S3 bucket. The company has a workflow on AWS that processes uploaded documents to perform sentiment analysis of photos and text. The processing workflow calls multiple AWS services. The company needs a solution to automate the processing workflow. The solution must handle any failed uploads. Which solution will meet these requirements with the LEAST effort?

<details><summary>Answer</summary>

**D. Use S3 Event Notifications to invoke an Amazon EventBridge rule. Configure the rule to initiate an AWS Step Functions workflow that orchestrates the processing workflow.**

This solution represents the most efficient and robust design pattern for the stated requirements. AWS Step Functions is a serverless workflow orchestrator specifically designed to coordinate multiple AWS services. It provides built-in state management, error handling (e.g., retries and catch blocks), and visualization, which directly addresses the need to orchestrate a multi-step process and handle failures. Using Amazon S3 Event Notifications to trigger an Amazon EventBridge rule, which in turn initiates the Step Functions workflow, is a highly automated, event-driven approach. This method offloads the complex orchestration and error-handling logic to managed AWS services, thereby fulfilling the "LEAST effort" requirement. Why Incorrect Options are Wrong: A. This requires significant development effort to build, deploy, and maintain a custom web application on ECS just for workflow orc

</details>

### 171. ce-384

A company runs an application on several Amazon EC2 instances. Multiple Amazon Elastic Block Store (Amazon EBS) volumes are attached to each EC2 instance. The company needs to back up the configurations and the data of the EC2 instances every night. The application must be recoverable in a secondary AWS Region. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create a backup plan in AWS Backup to take nightly backups. Copy the backups to a secondary Region. Add the EC2 instances to a resource assignment as part of the backup plan.**

AWS Backup is a fully managed, policy-based service that simplifies data protection at scale. By creating a backup plan that targets the Amazon EC2 instances, you back up the entire instance as a single entity. This includes the root EBS volume, all attached data EBS volumes, and critical configuration information stored as an Amazon Machine Image (AMI). This approach is the most operationally efficient because it automates the entire process-nightly backups and cross-region copies for disaster recovery-without requiring custom scripts or manual intervention for a full instance restore, thus meeting all requirements comprehensively. Why Incorrect Options are Wrong: A. This solution requires writing and maintaining custom Lambda code, which is less operationally efficient than using a managed service. It also only backs up EBS volumes, not the EC2 configuration. C. While using the correct

</details>

### 172. et-384 `cost` `availability`

A company runs an application on Amazon EC2 Linux instances across multiple Availability Zones. The application needs a storage layer that is highly available and Portable Operating System Interface (POSIX)-compliant. The storage layer must provide maximum data durability and must be shareable across the EC2 instances. The data in the storage layer will be accessed frequently for the first 30 days and will be accessed infrequently after that time. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use the Amazon Elastic File System (Amazon EFS) Standard storage class. Create a lifecycle management policy to move infrequently accessed data to EFS Standard-Infrequent Access (EFS Standard-IA).**

Amazon EFS provides scalable and highly available file storage in the cloud. The Standard storage class is designed for frequently accessed data, making it suitable for the initial 30 days of frequent access.  You can create a lifecycle management policy for EFS that automatically transitions infrequently accessed files to the EFS Standard-Infrequent Access (EFS Standard-IA) storage class. This helps optimize costs by moving less frequently accessed data to a lower-cost storage tier.

</details>

### 173. ce-385

A company runs its critical storage application in the AWS Cloud. The application uses Amazon S3 in two AWS Regions. The company wants the application to send remote user data to the nearest S3 bucket with no public network congestion. The company also wants the application to fail over with the least amount of management of Amazon S3. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Set up Amazon S3 to use Multi-Region Access Points in an active-active configuration with a single global endpoint. Configure S3 Cross-Region Replication.**

Amazon S3 Multi-Region Access Points provide a single global endpoint that applications use to access data. This service automatically routes user requests over the AWS global network to the S3 bucket with the lowest latency, addressing the requirements for sending data to the nearest bucket and avoiding public network congestion. This architecture simplifies failover, as S3 will automatically route requests to a healthy region if one becomes unavailable, meeting the need for minimal management. S3 Cross-Region Replication (CRR) is a necessary component to ensure that data written to one regional bucket is synchronized with the other, maintaining data consistency in an active-active configuration. Why Incorrect Options are Wrong: A. Using regional S3 endpoints requires the application to contain logic to determine the closest region and to manage failover, which contradicts the requireme

</details>

### 174. dt-385

An organization has a statutory requirement to protect the data at rest for the S3 objects. Which of the below mentioned options need not be enabled by the organization to achieve data security?

<details><summary>Answer</summary>

**D. Data replication.**

</details>

### 175. ce-388

An ecommerce company hosts an analytics application on AWS. The company deployed the application to one AWS Region. The application generates 300 MB of data each month. The application stores the data in JSON format. The data must be accessible in milliseconds when needed. The company must retain the data for 30 days. The company requires a disaster recovery solution to back up the data.

<details><summary>Answer</summary>

**B. Deploy an Amazon S3 bucket in the primary Region and in a second Region. Enable versioning on both buckets. Use the Standard storage class. Configure S3 Lifecycle policies to expire objects after 30 days. Configure S3 Cross-Region Replication from the bucket in the primary bucket to the backup bucket.**

Amazon S3 is the most suitable service for this scenario. It is designed for durable, cost-effective storage of objects, such as JSON files. The S3 Standard storage class provides low-latency access, meeting the "milliseconds" requirement for data retrieval. For disaster recovery, S3 Cross-Region Replication (CRR) provides a managed, asynchronous method to copy objects to a bucket in a different AWS Region. Finally, S3 Lifecycle policies can be configured to automatically expire and delete objects after the required 30-day retention period. This solution is simple to manage, highly scalable, and the most cost-effective for the specified data volume. Why Incorrect Options are Wrong: A: Deploying and managing two Amazon OpenSearch Service clusters is overly complex and expensive for storing and backing up only 300 MB of data per month. C: An Amazon Aurora global database is a high-performa

</details>

### 176. dt-389

What does the AWS Storage Gateway provide?

<details><summary>Answer</summary>

**A. It allows to integrate on-premises IT environments with Cloud Storage.**

</details>

### 177. et-393

A payment processing company records all voice communication with its customers and stores the audio files in an Amazon S3 bucket. The company needs to capture the text from the audio files. The company must remove from the text any personally identifiable information (PII) that belongs to customers. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Configure an Amazon Transcribe transcription job with PII redaction turned on. When an audio file is uploaded to the S3 bucket, invoke an AWS Lambda function to start the transcription job. Store the output in a separate S3 bucket.**

Amazon Transcribe is a fully managed service provided by Amazon Web Services (AWS) that enables automatic speech recognition (ASR). It allows developers to convert spoken language into written text, making it useful for various applications such as transcription services, voice analytics, and content indexing.

</details>

### 178. dt-394

Which of the following features are provided by Amazon EC2?

<details><summary>Answer</summary>

**B. Instances, Amazon Machine Images (AMIs), Key Pairs, Amazon EBS Volumes, Firewall, Elastic IP address, Tags, and Virtual Private Clouds (VPCs).**

</details>

### 179. ce-395

A company hosts an application on AWS that uses an Amazon S3 bucket and an Amazon Aurora database. The company wants to implement a multi-Region disaster recovery (DR) strategy that minimizes potential data loss. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Migrate the database to an Aurora global database. Create a second S3 bucket in a second Region. Configure Cross-Region Replication.**

This solution provides the most effective multi-Region disaster recovery (DR) strategy with the lowest potential for data loss (low Recovery Point Objective - RPO). Amazon Aurora global database is specifically designed for this purpose, using dedicated infrastructure to replicate data to a secondary AWS Region with a typical lag of less than one second. This minimizes data loss during a failover. For Amazon S3, Cross-Region Replication (CRR) is the standard mechanism to asynchronously copy objects to a bucket in another Region. This ensures that a copy of the data is available in the DR region, fulfilling the multi-Region requirement and minimizing data loss. Why Incorrect Options are Wrong: A. This describes a single-Region, multi-Availability Zone high availability (HA) strategy, not a multi-Region disaster recovery plan. It does not protect against a regional failure. B. While an Aur

</details>

### 180. dt-402

Can I delete a snapshot of the root device of an EBS volume used by a registered AMI?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 181. ce-403 `availability`

A shipping company wants to run a Kubernetes container-based web application in disconnected mode while the company's ships are in transit at se a. The application must provide local users with high availability.

<details><summary>Answer</summary>

**A. Use AWS Snowball Edge as the primary and secondary sites.**

The core requirements are to run a Kubernetes application with high availability in a completely disconnected environment, such as a ship at sea. AWS Snowball Edge devices are specifically designed for edge computing in rugged, disconnected, or intermittently connected locations. By deploying two or more Snowball Edge devices, a local, multi-node cluster can be created. This setup allows for running containerized applications using services like Amazon EKS Anywhere directly on the devices, providing the necessary high availability and fault tolerance without requiring any connection to an AWS Region. Why Incorrect Options are Wrong: B. AWS Local Zones are extensions of an AWS Region and require a persistent, high-bandwidth network connection to the parent Region, making them unsuitable for disconnected maritime operations. C. AWS Outposts extends AWS infrastructure on-premises but requir

</details>

### 182. ce-404

A company runs an application that uses Docker containers in an on-premises data center. The application runs on a container host that stores persistent data files in a local volume. Container instances use the stored persistent data. The company wants to migrate the application to fully managed AWS services. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon Elastic Container Service (Amazon ECS) with the AWS Fargate launch type. Create an Amazon Elastic File System (Amazon EFS) volume. Mount the EFS volume on the containers to provide persistent storage.**

The solution requires a fully managed service for running containers and a method for providing persistent file storage. 1. Fully Managed Service: AWS Fargate is a serverless compute engine for containers that works with Amazon Elastic Container Service (ECS). It removes the need to provision and manage servers, making it a fully managed solution. This aligns perfectly with the requirement. 2. Persistent File Storage: The application currently uses a local volume for persistent data files. Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system. EFS is designed to be mounted by multiple containers (or tasks) simultaneously, making it the ideal solution for providing shared, persistent file storage for stateful applications running on Fargate. Why Incorrect Options are Wrong: A: EKS with self-managed nodes is not a fully managed solution

</details>

### 183. et-404

A company has deployed a serverless application that invokes an AWS Lambda function when new documents are uploaded to an Amazon S3 bucket. The application uses the Lambda function to process the documents. After a recent marketing campaign, the company noticed that the application did not process many of the documents. What should a solutions architect do to improve the architecture of this application?

<details><summary>Answer</summary>

**D. Create an Amazon Simple Queue Service (Amazon SQS) queue. Send the requests to the queue. Configure the queue as an event source for Lambda.**

Introducing Amazon SQS as a queue allows for better decoupling between the S3 events and the document processing. This ensures that the Lambda function is not overwhelmed with spikes in incoming events, leading to missed document processing.

</details>

### 184. et-407

A company is implementing a shared storage solution for a gaming application that is hosted in the AWS Cloud. The company needs the ability to use Lustre clients to access data. The solution must be fully managed. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Lustre file system. Attach the file system to the origin server. Connect the application server to the file system.**

Amazon FSx for Lustre: Amazon FSx for Lustre is a fully managed service that provides high-performance shared storage. It is specifically designed to be used with Lustre, making it a suitable solution for Lustre clients.  Fully Managed: Amazon FSx for Lustre is a fully managed service, meaning that AWS takes care of maintenance, updates, and other operational tasks, reducing the management overhead for the company.

</details>

### 185. et-410

A company is deploying a new application on Amazon EC2 instances. The application writes data to Amazon Elastic Block Store (Amazon EBS) volumes. The company needs to ensure that all data that is written to the EBS volumes is encrypted at rest. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Create the EBS volumes as encrypted volumes. Attach the EBS volumes to the EC2 instances.**

By creating the EBS volumes as encrypted volumes, you ensure that all data written to those volumes is automatically encrypted. This provides a straightforward and effective solution for meeting the encryption-at-rest requirement.

</details>

### 186. dt-413

You are building an automated transcription service in which Amazon EC2 worker instances process an uploaded audio file and generate a text file. You must store both of these files in the same durable storage until the text file is retrieved. You do not know what the storage capacity requirements are. Which storage option is both cost-efficient and scalable?

<details><summary>Answer</summary>

**C. A single Amazon S3 bucket.**

</details>

### 187. et-415

A company is storing petabytes of data in Amazon S3 Standard. The data is stored in multiple S3 buckets and is accessed with varying frequency. The company does not know access patterns for all the data. The company needs to implement a solution for each S3 bucket to optimize the cost of S3 usage. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**A. Create an S3 Lifecycle configuration with a rule to transition the objects in the S3 bucket to S3 Intelligent-Tiering.**

S3 Intelligent-Tiering: This storage class is designed to automatically and dynamically move objects between two access tiers – frequent and infrequent access – based on changing access patterns. It is a good fit for data with unknown or changing access patterns. It provides cost savings compared to S3 Standard while maintaining low-latency access to frequently accessed objects.

</details>

### 188. ce-416 `security`

A company has an on-premises volume backup solution that is end of life. The company wants to use AWS as part of a new backup solution while maintaining local access to all data. The data must be automatically and securely transferred to AWS. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use AWS Storage Gateway and configure a stored volume gateway. Run the appliance on premises, map the gateway storage to on-premises disks, and mount gateway volumes for local access.**

The solution that meets all requirements is the AWS Storage Gateway configured as a stored volume gateway. This configuration stores the entire dataset on-premises, providing low-latency local access to all data, which is a critical requirement. The gateway appliance, running on-premises, asynchronously and securely backs up point-in-time snapshots of the on-premises volumes to Amazon S3. This provides a durable, offsite backup on AWS while satisfying the need for complete local data availability, effectively replacing the legacy backup system. Why Incorrect Options are Wrong: A. AWS Snowball is a data migration service for large-scale, offline data transfers, not a continuous backup solution that provides persistent local access. B. AWS Snowball Edge is also for data migration and edge computing; it is not designed to function as a permanent hybrid storage gateway for ongoing backups. C

</details>

### 189. et-421 `availability`

A company runs a highly available SFTP service. The SFTP service uses two Amazon EC2 Linux instances that run with elastic IP addresses to accept traffic from trusted IP sources on the internet. The SFTP service is backed by shared storage that is attached to the instances. User accounts are created and managed as Linux users in the SFTP servers. The company wants a serverless option that provides high IOPS performance and highly configurable security. The company also wants to maintain control over user permissions. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an encrypted Amazon Elastic File System (Amazon EFS) volume. Create an AWS Transfer Family SFTP service with elastic IP addresses and a VPC endpoint that has internet-facing access. Attach a security group to the endpoint that allows only trusted IP addresses. Attach the EFS volume to the SFTP service endpoint. Grant users access to the SFTP service.**

</details>

### 190. ce-422 `security`

A company has an on-premises volume backup solution that has reached its end of life. The company wants to use AWS as part of a new backup solution and wants to maintain local access to all the data while it is backed up on AWS. The company wants to ensure that the data backed up on AWS is automatically and securely transferred. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use AWS Storage Gateway and configure a stored volume gateway. Run the Storage Gateway software appliance on premises and map the gateway storage volumes to on-premises storage. Mount the gateway storage volumes to provide local access to the data.**

The Stored Volume Gateway configuration of AWS Storage Gateway is the correct solution. It stores the primary data locally on-premises, ensuring low-latency access to the entire dataset. This gateway then asynchronously backs up point-in-time snapshots of the on-premises data to Amazon S3 (as Amazon EBS snapshots). This architecture directly meets the company's requirements to maintain local access to all data while having it automatically and securely backed up to AWS. Why Incorrect Options are Wrong: A. AWS Snowball is a data migration service for transferring large amounts of data, not a continuous backup solution that provides ongoing local access. B. AWS Snowball Edge is also for data migration or edge computing; it is not designed as a permanent gateway for a continuous backup strategy. C. A Cached Volume Gateway stores the primary dataset in Amazon S3 and caches only a frequently

</details>

### 191. dt-423

Which Amazon Storage behaves like raw, unformatted, external block devices that you can attach to your instances?

<details><summary>Answer</summary>

**C. Amazon EBS**

</details>

### 192. et-425 `cost`

A company uses high block storage capacity to runs its workloads on premises. The company's daily peak input and output transactions per second are not more than 15,000 IOPS. The company wants to migrate the workloads to Amazon EC2 and to provision disk performance independent of storage capacity. Which Amazon Elastic Block Store (Amazon EBS) volume type will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. GP3 volume type**

General Purpose SSD (gp3) volumes are designed to provide a balance of price and performance. They allow you to provision IOPS independently of storage capacity, making them suitable for workloads with varying performance requirements. GP3 volumes offer a lower price per IOPS compared to io1 volumes and are a good fit for general-purpose workloads.

</details>

### 193. et-426 `security`

A company needs to store data from its healthcare application. The application’s data frequently changes. A new regulation requires audit access at all levels of the stored data. The company hosts the application on an on-premises infrastructure that is running out of storage capacity. A solutions architect must securely migrate the existing data to AWS while satisfying the new regulation. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS DataSync to move the existing data to Amazon S3. Use AWS CloudTrail to log data events.**

Explanation: CloudTrail management events don't capture object-level (data) access, so they can't satisfy "audit access at all levels of the stored data." CloudTrail data events, which log individual object-level API activity on the S3 bucket, are needed instead.

</details>

### 194. et-430 `cost`

A manufacturing company has machine sensors that upload .csv files to an Amazon S3 bucket. These .csv files must be converted into images and must be made available as soon as possible for the automatic generation of graphical reports. The images become irrelevant after 1 month, but the .csv files must be kept to train machine learning (ML) models twice a year. The ML trainings and audits are planned weeks in advance. Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**B. Design an AWS Lambda function that converts the .csv files into images and stores the images in the S3 bucket. Invoke the Lambda function when a .csv file is uploaded.**

C. Create S3 Lifecycle rules for .csv files and image files in the S3 bucket. Transition the .csv files from S3 Standard to S3 Glacier 1 day after they are uploaded. Expire the image files after 30 days.

</details>

### 195. dt-432

How can an EBS volume that is currently attached to an EC2 instance be migrated from one Availability Zone to another?

<details><summary>Answer</summary>

**C. Create a snapshot of the volume, and create a new volume from the snapshot in the other AZ.**

</details>

### 196. dt-436

Can you encrypt EBS volumes?

<details><summary>Answer</summary>

**A. Yes, you can enable encryption when you create a new EBS volume using the AWS Management Console, API, or CLI.**

</details>

### 197. ce-441

A media company is migrating a Microsoft Windows-based application to the AWS Cloud. The company uses the application to analyze media files. The company requires a resilient shared storage solution that the company can access by using the SMB protocol. Which storage solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon FSx for Windows File Server in a Multi-AZ deployment as shared storage for the application servers.**

The requirements are for a resilient, shared storage solution for a Windows-based application using the SMB protocol. Amazon FSx for Windows File Server is a fully managed service that provides native Microsoft Windows file systems. It supports the SMB protocol, Active Directory integration, and Windows NTFS. A Multi-AZ deployment provides high availability and durability by maintaining a standby file server in a different Availability Zone, making it a resilient solution. This service is specifically designed for this use case. Why Incorrect Options are Wrong: A. Amazon S3 is an object storage service and does not natively support the SMB protocol for mounting as a shared file system. C. Amazon EBS provides block storage. A standard EBS volume can only be attached to a single EC2 instance, so it cannot be used as shared storage. D. An Amazon FSx File Gateway is a hybrid cloud component

</details>

### 198. ce-442

A company runs an application on premises. The application stores files that the application servers process in a shared storage system. The company uses Linux file system permissions to control access to the files. The company plans to migrate the application servers to Amazon EC2 instances across multiple Availability Zones. The company does not want to change the application code. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Migrate the files to an Amazon EFS file system. Mount the EFS file system to the EC2 instances.**

Amazon EFS (Elastic File System) is the correct solution because it provides a managed, scalable, shared file system that can be mounted concurrently by multiple EC2 instances across different Availability Zones. It uses the standard NFSv4 protocol and supports POSIX-compliant file system permissions, which is what Linux systems use. This allows the company to migrate its application without changing the code that relies on a shared file system and Linux permissions. EFS is designed for this exact "lift-and-shift" use case for applications requiring shared file storage. Why Incorrect Options are Wrong: A. Amazon S3 is an object store, not a file system. Mounting it requires extra tools and it does not natively support POSIX permissions, which would require application changes. B. EC2 instance store is ephemeral storage tied to a single EC2 instance and cannot be shared across multiple in

</details>

### 199. et-443

A company wants to host a scalable web application on AWS. The application will be accessed by users from different geographic regions of the world. Application users will be able to download and upload unique data up to gigabytes in size. The development team wants a cost-effective solution to minimize upload and download latency and maximize performance. What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**A. Use Amazon S3 with Transfer Acceleration to host the application.**

</details>

### 200. et-445

A company is storing 700 terabytes of data on a large network-attached storage (NAS) system in its corporate data center. The company has a hybrid environment with a 10 Gbps AWS Direct Connect connection. After an audit from a regulator, the company has 90 days to move the data to the cloud. The company needs to move the data efficiently and without disruption. The company still needs to be able to access and update the data during the transfer window. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an AWS DataSync agent in the corporate data center. Create a data transfer task Start the transfer to an Amazon S3 bucket.**

using AWS DataSync, which is designed for efficiently transferring large amounts of data between on-premises storage and Amazon S3. It allows you to create data transfer tasks and initiate the transfer to an Amazon S3 bucket.

</details>

### 201. et-446 `least-ops`

A company stores data in PDF format in an Amazon S3 bucket. The company must follow a legal requirement to retain all new and existing data in Amazon S3 for 7 years. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Turn on S3 Object Lock with compliance retention mode for the S3 bucket. Set the retention period to expire after 7 years. Use S3 Batch Operations to bring the existing data into compliance.**

</details>

### 202. ce-447 `availability`

A company wants to use a cloud storage service to store text and media files that are associated with active global marketing campaigns. The storage solution must be highly available. The company must protect the solution with a backup system that reduces the possibility of data loss as much as possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Store the text and media files in an Amazon S3 bucket. Set the S3 bucket as the origin for an Amazon CloudFront distribution. Use AWS Backup to take continuous backups of the S3 bucket.**

This solution provides a highly available, durable, and globally performant architecture with robust backup capabilities. Storing files in Amazon S3 ensures high durability (99.999999999%) and availability, as data is automatically replicated across multiple Availability Zones. Using Amazon CloudFront as a content delivery network (CDN) caches the files at edge locations worldwide, providing low-latency access for a global audience. AWS Backup can be configured for continuous backup of the S3 bucket, enabling point-in-time recovery and protecting against accidental data loss or corruption, thus meeting the requirement to reduce data loss as much as possible. Why Incorrect Options are Wrong: A. An EC2 instance store is ephemeral and not suitable for durable storage; data is lost when the instance stops or terminates. C. An EBS volume is tied to a single Availability Zone, making it less a

</details>

### 203. dt-449

Which of the following are true regarding AWS CloudTrail? (Choose 3 answers)

<details><summary>Answer</summary>

**C. CloudTrail is enabled on a per-region basis.; D. CloudTrail is enabled on a per-service basis.; E. Logs can be delivered to a single Amazon S3 bucket for aggregation.**

</details>

### 204. et-453

A company wants to implement a backup strategy for Amazon EC2 data and multiple Amazon S3 buckets. Because of regulatory requirements, the company must retain backup files for a specific time period. The company must not alter the files for the duration of the retention period. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Backup to create a backup vault that has a vault lock in compliance mode. Create the required backup plan.**

AWS Backup provides a centralized solution for managing backups across various AWS services, including Amazon EC2. By creating a backup vault with a vault lock in compliance mode, the company ensures that the backup files are retained and cannot be altered for the duration of the retention period. Compliance mode is designed to meet regulatory requirements for data retention.

</details>

### 205. dt-461

What does the 'Server Side Encryption' option on Amazon S3 provide?

<details><summary>Answer</summary>

**A. It provides an encrypted virtual disk in the Cloud.**

</details>

### 206. ce-462

A company hosts a single-page application in an Amazon S3 bucket. The company has replicated the application to a second S3 bucket in a separate AWS Region. The company has users in Asia and Europe. A solutions architect must design a solution that redirects each user's requests to the Region that is closest to the user. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Create an Amazon CloudFront distribution that uses the two S3 buckets as origins. Create an AWS Lambda@Edge function to set a specific header that indicates each user's location. Create behaviors for each S3 bucket origin to select the origin based on the added header.**

The requirement is to route users to the S3 bucket in the geographically closest AWS Region. Amazon CloudFront serves content from edge locations near the user, but the origin request logic needs to be customized. Lambda@Edge allows you to run code in response to CloudFront events. A viewer-request function can inspect request headers, such as CloudFront-Viewer-Country, to determine the user's location. Based on this location, the function can dynamically modify the request to route it to the appropriate S3 origin (Asia or Europe). This provides a robust and intelligent solution for geolocation-based origin routing. Why Incorrect Options are Wrong: A. S3 Event Notifications are triggered by object-level operations (like PUT or DELETE), not by user requests to view content (GET requests). B. An Application Load Balancer (ALB) is a regional service and cannot be used as a single global end

</details>

### 207. dt-463

You are checking the workload on some of your General Purpose (SSD) and Provisioned IOPS (SSD) volumes and it seems that the I/O latency is higher than you require. You should probably check the [...] to make sure that your application is not trying to drive more IOPS than you have provisioned.

<details><summary>Answer</summary>

**C. average queue length.**

</details>

### 208. et-463 `cost`

An IoT company is releasing a mattress that has sensors to collect data about a user’s sleep. The sensors will send data to an Amazon S3 bucket. The sensors collect approximately 2 MB of data every night for each mattress. The company must process and summarize the data for each mattress. The results need to be available as soon as possible. Data processing will require 1 GB of memory and will finish within 30 seconds. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use AWS Lambda with a Python script**

AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It automatically scales with the number of requests, making it well-suited for event-driven workloads like processing data from IoT devices.  Python is a lightweight and efficient language for data processing tasks.  Lambda allows you to execute code in response to events, such as data arriving in the S3 bucket.

</details>

### 209. et-465

A company is developing an application to support customer demands. The company wants to deploy the application on multiple Amazon EC2 Nitro-based instances within the same Availability Zone. The company also wants to give the application the ability to write to multiple block storage volumes in multiple EC2 Nitro-based instances simultaneously to achieve higher application availability. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Provisioned IOPS SSD (io2) EBS volumes with Amazon Elastic Block Store (Amazon EBS) Multi-Attach**

Provisioned IOPS SSD (io2) volumes do indeed support Multi-Attach, allowing you to attach a single volume to multiple Nitro-based instances in the same Availability Zone. This can be suitable for scenarios where multiple instances need simultaneous access to a shared volume with high performance.

</details>

### 210. et-469

A company stores raw collected data in an Amazon S3 bucket. The data is used for several types of analytics on behalf of the company's customers. The type of analytics requested determines the access pattern on the S3 objects. The company cannot predict or control the access pattern. The company wants to reduce its S3 costs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use S3 Lifecycle rules to transition objects from S3 Standard to S3 Intelligent-Tiering**

S3 Intelligent-Tiering is designed to optimize costs by automatically moving objects between two access tiers: frequent and infrequent access. It is well-suited for scenarios where access patterns are unpredictable. Using S3 Lifecycle rules to transition objects to S3 Intelligent-Tiering allows you to take advantage of automatic cost savings based on actual access patterns without the need for manual adjustments.

</details>

### 211. dt-470

What happens to the I/O operations while you take a database snapshot?

<details><summary>Answer</summary>

**D. I/O operations to the database are suspended for a few minutes while the backup is in progress.**

</details>

### 212. dt-471

When an EC2 EBS-backed (EBS root) instance is stopped, what happens to the data on any ephemeral store volumes?

<details><summary>Answer</summary>

**B. Data is unavailable until the instance is restarted.**

</details>

### 213. dt-472

[...] is a durable, block-level storage volume that you can attach to a single, running Amazon EC2 instance.

<details><summary>Answer</summary>

**B. Amazon EBS.**

</details>

### 214. et-475

A company is designing a containerized application that will use Amazon Elastic Container Service (Amazon ECS). The application needs to access a shared file system that is highly durable and can recover data to another AWS Region with a recovery point objective (RPO) of 8 hours. The file system needs to provide a mount target m each Availability Zone within a Region. A solutions architect wants to use AWS Backup to manage the replication to another Region. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Amazon Elastic File System (Amazon EFS) with the Standard storage class**

</details>

### 215. dt-477

Which of the following would you use to list your AWS Import/Export jobs?

<details><summary>Answer</summary>

**C. Amazon S3 REST API.**

</details>

### 216. dt-478

Company B is launching a new game app for mobile devices. Users will log into the game using their existing social media account to streamline data capture. Company B would like to directly save player data and scoring information from the mobile app to a DynamoDB table named Score Data. When a user saves their game, the progress data will be stored to the Game State S3 bucket. What is the best approach for storing data to DynamoDB and S3?

<details><summary>Answer</summary>

**B. Use temporary security credentials that assume a role providing access to the Score Data DynamoDB table and the Game State S3 bucket using web identity federation.**

</details>

### 217. et-478 `security`

A law firm needs to share information with the public. The information includes hundreds of files that must be publicly readable. Modifications or deletions of the files by anyone before a designated future date are prohibited. Which solution will meet these requirements in the MOST secure way?

<details><summary>Answer</summary>

**B. Create a new Amazon S3 bucket with S3 Versioning enabled. Use S3 Object Lock with a retention period in accordance with the designated date. Configure the S3 bucket for static website hosting. Set an S3 bucket policy to allow read-only access to the objects.**

S3 Versioning helps maintain multiple versions of an object over time. With S3 Object Lock, you can enforce retention periods during which the objects cannot be modified or deleted. This aligns with the requirement to prohibit modifications or deletions before a designated future date.

</details>

### 218. dt-479

If your DB instance runs out of storage space or file system resources, its status will change to [...] and your DB Instance will no longer be available.

<details><summary>Answer</summary>

**B. storage-full.**

</details>

### 219. et-482 `least-ops`

A company wants to migrate 100 GB of historical data from an on-premises location to an Amazon S3 bucket. The company has a 100 megabits per second (Mbps) internet connection on premises. The company needs to encrypt the data in transit to the S3 bucket. The company will store new data directly in Amazon S3. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS DataSync to migrate the data from the on-premises location to an S3 bucket**

AWS DataSync is a service designed for efficiently transferring large amounts of data between on-premises storage systems and Amazon S3. It supports encryption of data in transit, ensuring the security of the data during the migration process. AWS DataSync is specifically built for data transfer scenarios and minimizes operational overhead, providing an efficient and straightforward solution.

</details>

### 220. dt-485

You have been storing massive amounts of data on Amazon Glacier for the past 2 years and now start to wonder if there are any limitations on this. What is the correct answer to your question?

<details><summary>Answer</summary>

**C. The total volume of data and number of archives you can store are unlimited.**

</details>

### 221. et-485 `cost`

A company is looking for a solution that can store video archives in AWS from old news footage. The company needs to minimize costs and will rarely need to restore these files. When the files are needed, they must be available in a maximum of five minutes. What is the MOST cost-effective solution?

<details><summary>Answer</summary>

**A. Store the video archives in Amazon S3 Glacier and use Expedited retrievals.**

</details>

### 222. dt-486

How are the EBS snapshots saved on Amazon S3?

<details><summary>Answer</summary>

**B. Incrementally.**

</details>

### 223. ce-487

A company has several on-premises Internet Small Computer Systems Interface (iSCSI) network storage servers The company wants to reduce the number of these servers by moving to the AWS Cloud. A solutions architect must provide low-latency access to frequently used data and reduce the dependency on on-premises servers with a minimal number of infrastructure changes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Deploy an AWS Storage Gateway volume gateway that is configured with cached volumes.**

The optimal solution is an AWS Storage Gateway configured as a Volume Gateway with cached volumes. This configuration addresses all requirements: it presents iSCSI block storage targets to the on-premises network, ensuring minimal infrastructure changes. The primary data is stored durably in Amazon S3, which reduces the dependency on on-premises storage hardware. The gateway caches frequently accessed data locally, providing the required low-latency access for active workloads. This model effectively extends on-premises storage to the AWS Cloud while optimizing for performance and cost. Why Incorrect Options are Wrong: A. An S3 File Gateway provides file-level access (NFS/SMB), not the required iSCSI block-level access, necessitating significant application and infrastructure changes. B. Amazon EBS volumes are for EC2 instances and cannot be directly attached to on-premises servers via i

</details>

### 224. et-490

A gaming company uses Amazon DynamoDB to store user information such as geographic location, player data, and leaderboards. The company needs to configure continuous backups to an Amazon S3 bucket with a minimal amount of coding. The backups must not affect availability of the application and must not affect the read capacity units (RCUs) that are defined for the table. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Export the data directly from DynamoDB to Amazon S3 with continuous backups. Turn on point-in-time recovery for the table.**

</details>

### 225. ce-491 `availability`

A weather forecasting company needs to process hundreds of gigabytes of data with sub-millisecond latency. The company has a high performance computing (HPC) environment in its data center and wants to expand its forecasting capabilities. A solutions architect must identify a highly available cloud storage solution that can handle large amounts of sustained throughput Files that are stored in the solution should be accessible to thousands of compute instances that will simultaneously access and process the entire dataset. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon FSx for Lustre persistent file systems.**

The scenario describes a High-Performance Computing (HPC) workload that requires sub-millisecond latency, high sustained throughput, and massive parallel access from thousands of compute instances. Amazon FSx for Lustre is the AWS service specifically designed for these demanding HPC requirements. The question also specifies the need for a "highly available" solution. FSx for Lustre offers two deployment types: persistent and scratch. Persistent file systems are designed for longer-term workloads, providing high availability by replicating data and automatically replacing failed file servers within an Availability Zone. This directly meets all the requirements of the scenario. Why Incorrect Options are Wrong: A. Use Amazon FSx for Lustre scratch file systems: Scratch file systems are for temporary processing and are not highly available. Data is not replicated and is lost if a file serve

</details>

### 226. dt-493

You are signed in as root user on your account but there is an Amazon S3 bucket under your account that you cannot access. What is a possible reason for this?

<details><summary>Answer</summary>

**A. An IAM user assigned a bucket policy to an Amazon S3 bucket and didn't specify the root user as a principal**

</details>

### 227. dt-494

When creation of an EBS snapshot is initiated, but not completed, the EBS volume?

<details><summary>Answer</summary>

**D. Cannot be used until the snapshot completes.**

</details>

### 228. et-495

A company is conducting an internal audit. The company wants to ensure that the data in an Amazon S3 bucket that is associated with the company’s AWS Lake Formation data lake does not contain sensitive customer or employee data. The company wants to discover personally identifiable information (PII) or financial information, including passport numbers and credit card numbers. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure Amazon Macie to run a data discovery job that uses managed identifiers for the required data types.**

Amazon Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data like PII or financial information. By configuring Amazon Macie to run a data discovery job, you can use managed identifiers to search for specific types of sensitive data within the S3 bucket.

</details>

### 229. ce-496

A company currently stores 5 TB of data in on-premises block storage systems. The company's current storage solution provides limited space for additional dat a. The company runs applications on premises that must be able to retrieve frequently accessed data with low latency. The company requires a cloud-based storage solution. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**B. Use an AWS Storage Gateway Volume Gateway with cached volumes as iSCSt targets.**

The most operationally efficient solution is the AWS Storage Gateway's Volume Gateway configured with cached volumes. This configuration provides cloud-backed iSCSI block storage volumes that on-premises applications can use. The primary data is stored in Amazon S3, which solves the on-premises storage space limitation. A cache of the frequently accessed data is maintained locally on the gateway. This ensures that applications can retrieve this data with the required low latency, directly addressing all constraints of the scenario. Why Incorrect Options are Wrong: A. S3 File Gateway provides a file-level interface (NFS/SMB), which does not match the company's existing block storage systems and application requirements. C. Stored volumes maintain the entire dataset on-premises and only back up snapshots to S3. This does not solve the problem of limited local storage space. D. Tape Gateway

</details>

### 230. dt-496

You receive a bill from AWS but are confused because you see you are incurring different costs for the exact same storage size in different regions on Amazon S3. You ask AWS why this is so. What response would you expect to receive from AWS?

<details><summary>Answer</summary>

**B. We charge less where our costs are less.**

</details>

### 231. et-496

A company uses on-premises servers to host its applications. The company is running out of storage capacity. The applications use both block storage and NFS storage. The company needs a high-performing solution that supports local caching without re-architecting its existing applications. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Deploy an AWS Storage Gateway file gateway to replace NFS storage.**

D. Deploy an AWS Storage Gateway volume gateway to replace the block storage.

</details>

### 232. et-497 `cost`

A company has a service that reads and writes large amounts of data from an Amazon S3 bucket in the same AWS Region. The service is deployed on Amazon EC2 instances within the private subnet of a VPC. The service communicates with Amazon S3 over a NAT gateway in the public subnet. However, the company wants a solution that will reduce the data output costs. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Provision a VPC gateway endpoint. Configure the route table for the private subnet to use the gateway endpoint as the route for all S3 traffic.**

</details>

### 233. et-498 `least-ops`

A company uses Amazon S3 to store high-resolution pictures in an S3 bucket. To minimize application changes, the company stores the pictures as the latest version of an S3 object. The company needs to retain only the two most recent versions of the pictures. The company wants to reduce costs. The company has identified the S3 bucket as a large expense. Which solution will reduce the S3 costs with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use S3 Lifecycle to delete expired object versions and retain the two most recent versions.**

This approach allows you to automate the deletion of object versions based on lifecycle policies, reducing manual intervention and operational overhead.

</details>

### 234. et-500

A company has multiple Windows file servers on premises. The company wants to migrate and consolidate its files into an Amazon FSx for Windows File Server file system. File permissions must be preserved to ensure that access rights do not change. Which solutions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Deploy AWS DataSync agents on premises. Schedule DataSync tasks to transfer the data to the FSx for Windows File Server file system.**

D. Order an AWS Snowcone device. Connect the device to the on-premises network. Launch AWS DataSync agents on the device. Schedule DataSync tasks to transfer the data to the FSx for Windows File Server file system.

</details>

### 235. et-501

A company wants to ingest customer payment data into the company's data lake in Amazon S3. The company receives payment data every minute on average. The company wants to analyze the payment data in real time. Then the company wants to ingest the data into the data lake. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**Use Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) to ingest the data. Use Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics) to analyze the data in real time.**

Amazon Data Firehose is a fully managed delivery stream that buffers incoming records and writes them to Amazon S3 with no servers, shards or scaling to manage, which is what makes it the most operationally efficient way to land payment data in the data lake. Amazon Managed Service for Apache Flink reads the same stream and runs continuous queries over it, giving real-time analysis alongside delivery to S3. The alternatives - scheduled batch jobs, or custom consumers running on EC2 or in Lambda - add code and operational work for the same result.

</details>

### 236. ce-504

A company is running a media store across multiple Amazon EC2 instances distributed across multiple Availability Zones in a single VPC. The company wants a high-performing solution to share data between all the EC2 instances, and prefers to keep the data within the VPC only. What should a solutions architect recommend?

<details><summary>Answer</summary>

**D. Configure an Amazon Elastic File System (Amazon EFS) file system and mount It across all instances.**

Amazon Elastic File System (EFS) is the ideal solution for this scenario. It provides a fully managed, scalable, and high-performance Network File System (NFS) that can be concurrently mounted by thousands of Amazon EC2 instances. EFS is a regional service, meaning it stores data across multiple Availability Zones (AZs) for high availability. By creating EFS mount targets in the subnets of each AZ where the EC2 instances are running, all instances can share the same file system seamlessly. All data traffic between the EC2 instances and the EFS file system remains within the Virtual Private Cloud (VPC), satisfying the security requirement. Why Incorrect Options are Wrong: A. Amazon S3 is an object storage service, not a file system. Accessing data via API calls is fundamentally different from a mounted file system and may not be suitable or performant for applications expecting POSIX-comp

</details>

### 237. et-506

A social media company is building a feature for its website. The feature will give users the ability to upload photos. The company expects significant increases in demand during large events and must ensure that the website can handle the upload traffic from users. Which solution meets these requirements with the MOST scalability?

<details><summary>Answer</summary>

**C. Generate Amazon S3 presigned URLs in the application. Upload files directly from the user's browser into an S3 bucket.**

Amazon S3 Presigned URLs: This approach allows the client (user's browser) to directly upload files to Amazon S3 using a presigned URL generated by the server. This offloads the file transfer process from the application servers and enables a direct upload to S3 from the client side.

</details>

### 238. ce-509 `least-ops`

A digital image processing company wants to migrate its on-premises monolithic application to the AWS Cloud. The company processes thousands of images and generates large files as part of the processing workflow. The company needs a solution to manage the growing number of image processing jobs. The solution must also reduce the manual tasks in the image processing workflow. The company does not want to manage the underlying infrastructure of the solution. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS Batch jobs to process the images. Use AWS Step Functions to orchestrate the workflow. Store the processed files in an Amazon S3 bucket.**

This solution provides a fully managed, serverless architecture with the least operational overhead. AWS Batch is specifically designed to run batch computing jobs at scale without needing to manage the underlying compute resources. AWS Step Functions is a serverless orchestrator that automates the image processing workflow, handling sequencing, error handling, and retries, which reduces manual tasks. Amazon S3 is the most scalable, durable, and cost-effective storage solution for large, processed image files, which are best stored as objects. This combination directly addresses all the company's requirements for scalability, automation, and minimal infrastructure management. Why Incorrect Options are Wrong: A: This option requires managing the underlying EC2 instances for the Amazon ECS cluster, which increases operational overhead. Amazon SQS is a queue, not a complete workflow orchest

</details>

### 239. ce-510

A company needs a solution to automate email ingestion. The company needs to automatically parse email messages, look for email attachments, and save any attachments to an Amazon S3 bucket in near real time. Email volume varies significantly from day to day. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Set up email receiving in Amazon Simple Email Service Amazon SES). Create a rule set and a receipt rule. Create an AWS Lambda function that Amazon SES can invoke to process the email bodies and attachments.**

This solution leverages Amazon Simple Email Service (SES) for its core capability of receiving emails. By creating a receipt rule, you can define an automated action for incoming messages. The most flexible action for custom processing is to invoke an AWS Lambda function. Lambda is a serverless compute service that automatically scales with the volume of incoming emails, perfectly addressing the variable workload. The function can be coded to parse the email content, extract attachments, and write them directly to an Amazon S3 bucket, fulfilling all requirements in a cost-effective and scalable manner. Why Incorrect Options are Wrong: B: Content filtering in SES is for accepting or rejecting emails based on criteria like IP addresses or domains, not for processing email content and extracting attachments. C: While SES can save an entire email to S3, using S3 Event Notifications adds an u

</details>

### 240. et-512 `least-ops`

A company uses AWS Organizations with resources tagged by account. The company also uses AWS Backup to back up its AWS infrastructure resources. The company needs to back up all AWS resources. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Config to identify all untagged resources. Tag the identified resources programmatically. Use tags in the backup plan.**

AWS Config can be used to identify untagged resources, and it can provide a comprehensive view of the resource inventory across your AWS Organization.  AWS Backup supports the use of tags in backup plans. By utilizing tags, you can create a backup plan that automatically includes resources based on their tags.

</details>

### 241. ce-513

A company is deploying a new gaming application on Amazon EC2 instances. The gaming application needs to have access to shared storage. The company requires a high-performance solution to give the application the ability to use an existing custom protocol to access shared storage. The solution must ensure low latency and must be operationally efficient. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Lustre file system. Connect the EC2 instances that host the application to the file system.**

The question requires a high-performance, low-latency, and operationally efficient shared storage solution for a gaming application on EC2. Amazon FSx for Lustre is a fully managed service designed for high-performance computing (HPC) workloads, which share similar characteristics with demanding gaming applications. It provides sub-millisecond latencies, high throughput (hundreds of GB/s), and millions of IOPS. As a managed service, it is operationally efficient, eliminating the need to manage file servers and storage volumes. This makes it the ideal choice for performance-intensive applications requiring shared storage. The mention of a "custom protocol" is likely a distractor, as the primary focus is on performance characteristics, for which FSx for Lustre is the superior option. Why Incorrect Options are Wrong: A. Amazon FSx File Gateway is designed to provide on-premises access to cl

</details>

### 242. et-513 `availability`

A social media company wants to allow its users to upload images in an application that is hosted in the AWS Cloud. The company needs a solution that automatically resizes the images so that the images can be displayed on multiple device types. The application experiences unpredictable traffic patterns throughout the day. The company is seeking a highly available solution that maximizes scalability. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Create a static website hosted in Amazon S3 that invokes AWS Lambda functions to resize the images and store the images in an Amazon S3 bucket.**

Hosting a static website in Amazon S3 is a cost-effective and highly available solution. Amazon S3 provides scalable and durable object storage. A static website in S3 can serve as the front end for user interactions. In this option, Lambda functions can be triggered by events (e.g., new image uploads to an S3 bucket) to perform image resizing. Lambda can efficiently handle sporadic and unpredictable workloads.

</details>

### 243. dt-514

Which procedure for backing up a relational database on EC2 that is using a set of RAIDed EBS volumes for storage minimizes the time during which the database cannot be written to and results in a consistent backup?

<details><summary>Answer</summary>

**A. 1. Detach EBS volumes, 2. Start EBS snapshot of volumes, 3. Re-attach EBS volumes.**

</details>

### 244. dt-517

You have some very sensitive data stored on AWS S3 and want to try every possible alternative to keeping it secure in regards to access control. What are the mechanisms available for access control on AWS S3?

<details><summary>Answer</summary>

**A. (IAM) policies, Access Control Lists (ACLs), bucket policies, and query string authentication.**

</details>

### 245. et-517

A company wants to send all AWS Systems Manager Session Manager logs to an Amazon S3 bucket for archival purposes. Which solution will meet this requirement with the MOST operational efficiency?

<details><summary>Answer</summary>

**Enable S3 logging in the Systems Manager console. Choose an S3 bucket to send the session data to.**

Session logging is a configuration setting, not something that has to be built: in the Systems Manager console you edit Session Manager preferences, tick Enable under S3 logging and name the destination bucket, optionally with a key prefix and a requirement that the bucket be encrypted. From then on session output is delivered to that bucket for every session, which is why this is the most operationally efficient option. It needs no agent scripting, no log shipper and no scheduled copy job - the instance profile simply needs permission to write to the bucket. The alternatives, such as sending to CloudWatch Logs and then exporting, or scripting a copy from the instance, add moving parts for the same archive.

</details>

### 246. dt-523

Out of the stripping options available for the EBS volumes, which one has the following disadvantage: 'Doubles the amount of 1/0 required from the instance to EBS compared to RAID 0, because you're mirroring all writes to a pair of volumes, limiting how much you can stripe.'?

<details><summary>Answer</summary>

**B. RAID 1+0 (RAID 10).**

</details>

### 247. ce-528 `least-ops`

How can DynamoDB data be made available for long-term analytics with minimal operational overhead?

<details><summary>Answer</summary>

**A. Configure DynamoDB incremental exports to S3.**

The native DynamoDB "Export to Amazon S3" feature is a fully managed solution designed for this exact use case. It allows you to export data from a DynamoDB table to an S3 bucket with minimal effort. Incremental exports can be configured to capture data changes between two points in time, making it ideal for continuously populating a data lake for long-term analytics. This approach has the lowest operational overhead because it does not require managing compute resources, clusters, or custom application code. The data is exported in formats like JSON or Amazon Ion, which are easily consumable by analytics services like Amazon Athena. Why Incorrect Options are Wrong: B. Configuring DynamoDB Streams requires developing and maintaining a consumer, such as an AWS Lambda function, to process records and write them to S3, which increases operational overhead. C. Using Amazon EMR to copy data i

</details>

### 248. dt-529

What does RRS stand for when talking about S3?

<details><summary>Answer</summary>

**D. Reduced Redundancy Storage.**

</details>

### 249. dt-534

AWS Identity and Access Management is a web service that enables Amazon Web Services (AWS) customers to manage users and user permissions in AWS. In addition to supporting IAM user policies, some services support resource-based permissions. Which of the following services are supported by resource-based permissions?

<details><summary>Answer</summary>

**C. Amazon S3, Amazon SNS, Amazon SQS, Amazon Glacier and Amazon EB**

</details>

### 250. gh-534 `cost` `availability`

A company wants to build a logging solution for its multiple AWS accounts. The company currently stores the logs from all accounts in a centralized account. The company has created an Amazon S3 bucket in the centralized account to store the VPC flow logs and AWS CloudTrail logs. All logs must be highly available for 30 days for frequent analysis, retained for an additional 60 days for backup purposes, and deleted 90 days after creation.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Transition objects to an S3 infrequent-access storage class 30 days after creation, and write an expiration action that directs Amazon S3 to delete objects after 90 days - with no Glacier transition. Where S3 One Zone-Infrequent Access is offered, it is the cheapest valid choice, because high availability is only required for the first 30 days and the remaining 60 days are backup only; if One Zone-IA is not among the options, S3 Standard-Infrequent Access is the correct pick.**

The logs need frequent, highly available access for 30 days, so they stay in S3 Standard for that period. From day 30 to day 90 they are held only for backup, so an infrequent-access class costs less per GB, and One Zone-IA is cheaper still once the high-availability requirement has lapsed. Because everything is deleted at day 90, an expiration action at 90 days is all that is needed, and a Glacier transition on the same day is wasted: expiration wins over a same-day transition, and Glacier Flexible Retrieval would in any case bill a 90-day minimum for objects that no longer exist. Adding the Glacier step therefore raises cost and complexity without meeting any stated requirement.

</details>

### 251. ce-540 `least-ops`

A company has a large amount of data in an Amazon DynamoDB table. A large batch of data is appended to the table once each day. The company wants a solution that will make all the existing and future data in DynamoDB available for analytics on a long-term basis. Which solution meets these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure DynamoDB incremental exports to Amazon S3.**

The most efficient solution with the least operational overhead is to use the managed Amazon DynamoDB export to Amazon S3 feature. This feature allows for a full export of all existing data to an S3 bucket. For future data, incremental exports can be configured to run on a schedule (e.g., daily), exporting only the data that has been added or changed within a specific time window. This requires Point-in-Time Recovery (PITR) to be enabled on the table. The entire process is serverless and managed by AWS, minimizing configuration and maintenance, thus satisfying the "least operational overhead" requirement. S3 is the ideal destination for long-term data storage and analytics. Why Incorrect Options are Wrong: B. Configure Amazon DynamoDB Streams to write records to Amazon S3. DynamoDB Streams only captures data changes after it is enabled; it does not export existing data, requiring a separ

</details>

### 252. dt-543

Your fortune 500 company has undertaken a TCO analysis evaluating the use of Amazon S3 versus acquiring more hardware. The outcome was that all employees would be granted access to use Amazon S3 for storage of their personal documents. Which of the following will you need to consider so you can set up a solution that incorporates single sign-on from your corporate AD or LDAP directory and restricts access for each user to a designated user folder in a bucket? (Choose 3 answers)

<details><summary>Answer</summary>

**A. Setting up a federation proxy or identity provider.; B. Using AWS Security Token Service to generate temporary tokens.; D. Configuring IAM role.**

</details>

### 253. dt-544

Your company policies require encryption of sensitive data at rest. You are considering the possible options for protecting data while storing it at rest on an EBS data volume, attached to an EC2 instance. Which of these options would allow you to encrypt your data at rest? (Choose 3 answers)

<details><summary>Answer</summary>

**A. Implement third party volume encryption tools.; C. Encrypt data inside your applications before storing it on EBS.; D. Encrypt data using native data encryption drivers at the file system level.**

</details>

### 254. ce-545

A company stores 5 PB of archived data on physical tapes. The company needs to preserve the data for another 10 years. The data center that stores the tapes has a 10 Gbps Direct Connect connection to an AWS Region. The company wants to migrate the data to AWS within the next 6 months.

<details><summary>Answer</summary>

**D. Configure an on-premises AWS Storage Gateway Tape Gateway. Create virtual tapes in the AWS Cloud. Use backup software to copy the physical tapes to the virtual tapes. Move the virtual tapes to Amazon S3 Glacier Deep Archive storage.**

The most effective solution is to use AWS Storage Gateway's Tape Gateway. This service presents a virtual tape library (VTL) to the company's existing on-premises backup software, integrating seamlessly with their current tape-based workflows. The backup software can then copy data from the physical tapes to the new virtual tapes. The Tape Gateway caches the data locally and then efficiently transfers it over the 10 Gbps Direct Connect connection to Amazon S3. Once uploaded, the virtual tapes can be archived to Amazon S3 Glacier Deep Archive, which is the most cost-effective storage class for long-term (10-year) data retention with infrequent access, fulfilling all requirements of the scenario. Why Incorrect Options are Wrong: A. This is inefficient and costly. It requires staging 5 PB of data on local disk storage before migration, which is impractical. DataSync is not designed for tape

</details>

### 255. et-546

A recent analysis of a company's IT expenses highlights the need to reduce backup costs. The company's chief information officer wants to simplify the on-premises backup infrastructure and reduce costs by eliminating the use of physical backup tapes. The company must preserve the existing investment in the on-premises backup applications and workflows. What should a solutions architect recommend?

<details><summary>Answer</summary>

**D. Set up AWS Storage Gateway to connect with the backup applications using the iSCSI-virtual tape library (VTL) interface.**

AWS Storage Gateway provides a hybrid cloud storage service that enables on-premises applications to seamlessly use cloud storage. The iSCSI-virtual tape library (VTL) interface of AWS Storage Gateway is designed to integrate with existing backup applications that use tape-based workflows. It emulates a tape library, allowing you to store virtual tapes in Amazon S3 or Glacier, providing a cost-effective and scalable alternative to physical tapes.

</details>

### 256. dt-547

You want to use AWS Import/Export to send data from your S3 bucket to several of your branch offices. What should you do if you want to send 10 storage units to AWS?

<details><summary>Answer</summary>

**D. Make sure you submit a separate job request for each device.**

</details>

### 257. et-547 `least-ops`

A company has data collection sensors at different locations. The data collection sensors stream a high volume of data to the company. The company wants to design a platform on AWS to ingest and process high-volume streaming data. The solution must be scalable and support data collection in near real time. The company must store the data in Amazon S3 for future reporting. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Firehose to deliver streaming data to Amazon S3.**

Amazon Kinesis Data Firehose: It is a fully managed service for ingesting, transforming, and delivering streaming data to various destinations, including Amazon S3. Kinesis Data Firehose can scale automatically based on the volume of incoming data, and it simplifies the process of delivering data to S3 without the need for manual intervention.

</details>

### 258. dt-549

While performing the volume status checks, if the status is insufficient-data, what does it mean?

<details><summary>Answer</summary>

**A. The checks may still be in progress on the volume.**

</details>

### 259. dt-556

A customer wants to leverage Amazon Simple Storage Service (S3) and Amazon Glacier as part of their backup and archive infrastructure. The customer plans to use third-party software to support this integration. Which approach will limit the access of the third party software to only the Amazon S3 bucket named 'company-backup'?

<details><summary>Answer</summary>

**D. A custom IAM user policy limited to the Amazon S3 API in 'company-backup'.**

</details>

### 260. dt-557

A user needs to run a batch process which runs for 10 minutes. This will only be run once, or at maximum twice, in the next month, so the processes will be temporary only. The process needs 15 X-Large instances. The process downloads the code from S3 on each instance when it is launched, and then generates a temporary log file. Once the instance is terminated, all the data will be lost. Which of the below mentioned pricing models should the user choose in this case?

<details><summary>Answer</summary>

**A. Spot instance.**

</details>

### 261. dt-560

You are migrating an internal server on your DC to an EC2 instance with EBS volume. Your server disk usage is around 500GB so you just copied all your data to a 2TB disk to be used with AWS Import/Export. Where will the data be imported once it arrives at Amazon?

<details><summary>Answer</summary>

**B. To an S3 bucket with 2 objects of 1TB.**

</details>

### 262. ce-562

A solutions architect is designing the storage architecture for a new web application used for storing and viewing engineering drawings. All application components will be deployed on the AWS infrastructure. The application design must support caching to minimize the amount of time that users wait for the engineering drawings to load. The application must be able to store petabytes of data. Which combination of storage and caching should the solutions architect use?

<details><summary>Answer</summary>

**A. Amazon S3 with Amazon CloudFront**

The optimal solution must address two key requirements: storing petabytes of data and providing low-latency access through caching. Amazon S3 is an object storage service designed for massive scalability, capable of storing petabytes of data durably and cost-effectively, making it ideal for the engineering drawings. Amazon CloudFront is a global Content Delivery Network (CDN) that caches content, such as files stored in S3, at edge locations physically closer to the end-users. This architecture significantly reduces latency and minimizes the time users wait for drawings to load, directly fulfilling the application's caching requirement. Why Incorrect Options are Wrong: B. Amazon S3 Glacier Deep Archive with Amazon ElastiCache: S3 Glacier Deep Archive is for long-term archival with retrieval times of several hours, making it unsuitable for a web application requiring fast access. C. Amazo

</details>

### 263. dt-563

A client of yours has a huge amount of data stored on Amazon S3, but is concerned about someone stealing it while it is in transit. You know that all data is encrypted in transit on AWS, but which of the following is wrong when describing server-side encryption on AWS?

<details><summary>Answer</summary>

**C. In server-side encryption, you manage encryption/decryption of your data, the encryption keys, and related tools.**

</details>

### 264. ce-566

A company collects data for temperature, humidity, and atmospheric pressure in cities across multiple continents. The average volume of data that the company collects from each site daily is 500 GB. Each site has a high-speed internet connection. The company wants to aggregate the data from all these global sites as quickly as possible in a single Amazon S3 bucket. The solution must minimize operational complexity. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Turn on S3 Transfer Acceleration on the destination S3 bucket. Use multipart uploads to directly upload site data to the destination S3 bucket.**

The core requirements are to transfer large files (500 GB daily) from globally distributed locations to a single S3 bucket as quickly as possible, with minimal operational complexity. S3 Transfer Acceleration is designed for this exact use case. It leverages Amazon CloudFront's globally distributed edge locations to accelerate long-distance data transfers over the public internet to Amazon S3. Data from the global sites is routed to the nearest AWS edge location and then travels over the optimized AWS global network to the destination bucket. Combining this with multipart uploads, which is a best practice for large files, ensures maximum throughput and reliability. This solution is simple to implement by enabling a single setting on the bucket. Why Incorrect Options are Wrong: B: This approach adds operational complexity by requiring management of multiple S3 buckets, replication rules,

</details>

### 265. et-566

A company runs multiple Amazon EC2 Linux instances in a VPC across two Availability Zones. The instances host applications that use a hierarchical directory structure. The applications need to read and write rapidly and concurrently to shared storage. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create an Amazon Elastic File System (Amazon EFS) file system. Mount the EFS file system from each EC2 instance.**

Amazon EFS is a fully managed, scalable file storage service designed to provide shared access to files across multiple Amazon EC2 instances. It is particularly well-suited for use cases that require concurrent access from multiple instances.

</details>

### 266. dt-570

You're running an application on-premises due to its dependency on non-x86 hardware and want to use AWS for data backup. Your backup application is only able to write to POSIX-compatible block based storage. You have 140TB of data and would like to mount it as a single folder on your file server Users must be able to access portions of this data while the backups are taking place. What backup solution would be most appropriate for this use case?

<details><summary>Answer</summary>

**A. Use Storage Gateway and configure it to use Gateway Cached volumes.**

</details>

### 267. ce-571

A company hosts an application on AWS that gives users the ability to download photos. The company stores all photos in an Amazon S3 bucket that is located in the us-east-1 Region. The company wants to provide the photo download application to global customers with low latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure an Amazon CloudFront distribution in front of the S3 bucket. Use the distribution endpoint to access the photos that are in the S3 bucket.**

Amazon CloudFront is a global Content Delivery Network (CDN) service designed to deliver content, such as photos, with low latency and high transfer speeds. By creating a CloudFront distribution and setting the Amazon S3 bucket as the origin, content is cached at AWS Edge Locations around the world. When a user requests a photo, the request is routed to the nearest Edge Location, which serves the cached content. This process significantly reduces the distance the data has to travel, thereby minimizing latency for a global user base without needing to replicate the S3 bucket across multiple regions. Why Incorrect Options are Wrong: A. Routing to S3's public IP addresses is not a supported or reliable practice as they can change. Furthermore, latency-based routing requires resources in multiple regions to be effective; all traffic would still be directed to the single us-east-1 region. C.

</details>

### 268. dt-571

What happens to Amazon EBS root device volumes, by default, when an instance terminates?

<details><summary>Answer</summary>

**B. Amazon EBS root device volumes are copied into Amazon RD**

</details>

### 269. dt-576 `availability`

A company is deploying a two-tier, highly available web application to AWS. Which service provides durable storage for static content while utilizing lower Overall CPU resources for the web tier?

<details><summary>Answer</summary>

**B. Amazon S3.**

</details>

### 270. dt-578

An organization has a statutory requirement to protect the data at rest for data stored in EBS volumes. Which of the below mentioned options can the organization use to achieve data protection?

<details><summary>Answer</summary>

**D. All the options listed here.**

</details>

### 271. dt-579

A web design company currently runs several FTP servers that their 250 customers use to upload and download large graphic files. They wish to move this system to AWS to make it more scalable, but they wish to maintain customer privacy and keep costs to a minimum. What AWS architecture would you recommend?

<details><summary>Answer</summary>

**A. Ask their customers to use an S3 client instead of an FTP client. Create a single S3 bucket. Create an IAM user for each customer. Put the IAM Users in a Group that has an IAM policy that permits access to sub-directories within the bucket via use of the 'username' Policy variable.**

</details>

### 272. dt-580

Amazon RDS DB snapshots and automated backups are stored in:

<details><summary>Answer</summary>

**A. Amazon S3.**

</details>

### 273. et-580 `cost`

A company uses locally attached storage to run a latency-sensitive application on premises. The company is using a lift and shift method to move the application to the AWS Cloud. The company does not want to change the application architecture. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Host the application on an Amazon EC2 instance. Use an Amazon Elastic Block Store (Amazon EBS) GP3 volume to run the application.**

Amazon EC2 Instance with GP3 Volume (Option D): Amazon EBS GP3 volumes are designed to provide cost savings compared to GP2 volumes while still offering good performance for a broad range of workloads. GP3 volumes allow you to provision the IOPS (input/output operations per second) and throughput that your application needs, giving you flexibility and cost-effectiveness.

</details>

### 274. ce-581 `least-ops`

A company is migrating a large amount of data from on-premises storage to AWS. Windows, Mac, and Linux based Amazon EC2 instances in the same AWS Region will access the data by using SMB and NFS storage protocols. The company will access a portion of the data routinely. The company will access the remaining data infrequently. The company needs to design a solution to host the data. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Amazon FSx for ONTAP instance. Create an FSx for ONTAP file system with a root volume that uses the auto tiering policy. Migrate the data to the FSx for ONTAP volume.**

The solution requires a fully managed file system that supports both SMB and NFS protocols for Windows, Mac, and Linux clients. It must also automatically tier data to optimize costs for mixed (frequent and infrequent) access patterns with minimal operational effort. Amazon FSx for NetApp ONTAP is the only service that meets all these criteria. It is a fully managed service providing multi-protocol access via both NFS and SMB. Its automatic tiering policy transparently moves infrequently accessed data from high-performance SSD storage to a lower-cost capacity pool, directly addressing the cost-optimization and access pattern requirements with the least operational overhead. Why Incorrect Options are Wrong: A. Amazon EFS does not natively support the SMB protocol; it is an NFS-only file system, making it unsuitable for Windows clients without additional configuration. C. While S3 File Gat

</details>

### 275. dt-581

Can Amazon S3 uploads resume on failure or do they need to restart?

<details><summary>Answer</summary>

**C. Resume on failure.**

</details>

### 276. et-583 `cost`

A company has 5 PB of archived data on physical tapes. The company needs to preserve the data on the tapes for another 10 years for compliance purposes. The company wants to migrate to AWS in the next 6 months. The data center that stores the tapes has a 1 Gbps uplink internet connectivity. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Order multiple AWS Snowball devices that have Tape Gateway. Copy the physical tapes to virtual tapes in Snowball. Ship the Snowball devices to AWS. Create a lifecycle policy to move the tapes to Amazon S3 Glacier Deep Archive.**

AWS Snowball devices can be more cost-effective than transferring large amounts of data over a 1 Gbps internet connection, especially when dealing with petabytes of data.  AWS, a lifecycle policy can be configured to move the data to Amazon S3 Glacier Deep Archive, which is a cost-effective storage class designed for long-term archival.

</details>

### 277. dt-585

You are designing a web application that stores static assets in an Amazon Simple Storage Service (S3) bucket. You expect this bucket to immediately receive over 150 PUT requests per second. What should you do to ensure optimal performance?

<details><summary>Answer</summary>

**A. Use multi-part upload.**

</details>

### 278. dt-587

A customer has a single 3-TB volume on-premises that is used to hold a large repository of images and print layout files. This repository is growing at 500 GB a year and must be presented as a single logical volume. The customer is becoming increasingly constrained with their local storage capacity and wants an off-site backup of this data, while maintaining low-latency access to their frequently accessed data. Which AWS Storage Gateway configuration meets the customer requirements?

<details><summary>Answer</summary>

**D. Gateway-Virtual Tape Library with snapshots to Amazon Glacier.**

</details>

### 279. dt-591

You need to migrate a large amount of data into the cloud that you have stored on a hard disk and you decide that the best way to accomplish this is with AWS Import/Export and you mail the hard disk to AWS. Which of the following statements is incorrect in regards to AWS Import/Export?

<details><summary>Answer</summary>

**C. It can export from Amazon Glacier.**

</details>

### 280. et-592

A company uses AWS and sells access to copyrighted images. The company’s global customer base needs to be able to access these images quickly. The company must deny access to users from specific countries. The company wants to minimize costs as much as possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon S3 to store the images. Use Amazon CloudFront to distribute the images with geographic restrictions. Provide a signed URL for each customer to access the data in CloudFront.**

By using CloudFront, you can cache and serve the images from edge locations around the world, improving access speed for global customers. Geographic Restrictions in CloudFront: CloudFront allows you to set up geographic restrictions to deny access to users from specific countries.

</details>

### 281. dt-594

A user is running a batch process which runs for 1 hour every day. Which of the below mentioned options is the right instance type and costing model in this case if the user performs the same task for the whole year?

<details><summary>Answer</summary>

**A. EBS backed instance with on-demand instance pricing.**

</details>

### 282. ce-596

A company uses a single Amazon S3 bucket to store data that multiple business applications must access. The company hosts the applications on Amazon EC2 Windows instances that are in a VPC. The company configured a bucket policy for the S3 bucket to grant the applications access to the bucket. The company continually adds more business applications to the environment. As the number of business applications increases, the policy document becomes more difficult to manage. The S3 bucket policy document will soon reach its policy size quot a. The company needs a solution to scale its architecture to handle more business applications. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**D. Create an S3 access point for each application. Instruct application owners to use their respective S3 access points.**

The core issue is the single S3 bucket policy becoming unmanageable and approaching its size limit (20 KB) due to an increasing number of applications needing access. S3 Access Points are designed specifically for this scenario. An S3 access point is a unique hostname for a bucket that has its own distinct access policy. By creating an access point for each application, the single, large bucket policy can be broken down into smaller, manageable policies attached to each access point. This approach is highly scalable (up to 10,000 access points per bucket per Region) and is the most operationally efficient solution as it does not require data migration, replication, or deploying additional infrastructure. Why Incorrect Options are Wrong: A. Migrating to Amazon EFS is a major architectural change from object storage to file storage. It is operationally intensive and does not solve the S3 p

</details>

### 283. dt-597

What are characteristics of Amazon S3? (Choose 2 answers)

<details><summary>Answer</summary>

**C. Amazon S3 allows you to store unlimited amounts of data.; E. Objects are directly accessible via a URL.**

</details>

### 284. dt-601

Is it possible to access your EBS snapshots?

<details><summary>Answer</summary>

**B. Yes, through the Amazon EC2 APIs.**

</details>

### 285. ce-603

A company receives data transfers from a small number of external clients that use SFTP software on an Amazon EC2 instance. The clients use an SFTP client to upload dat a. The clients use SSH keys for authentication. Every hour, an automated script transfers new uploads to an Amazon S3 bucket for processing. The company wants to move the transfer process to an AWS managed service and to reduce the time required to start data processing. The company wants to retain the existing user management and SSH key generation process. The solution must not require clients to make significant changes to their existing processes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an AWS Transfer Family SFTP server that uses the existing S3 bucket as a target. Use service-managed users to enable authentication.**

AWS Transfer Family is a fully managed service that enables the transfer of files directly into and out of Amazon S3 using SFTP, FTPS, and FTP. This solution replaces the self-managed EC2 instance with a managed service. By configuring the Transfer Family server to use an S3 bucket as the storage backend, files uploaded by clients are immediately available in S3, significantly reducing the time to start data processing. The service-managed identity provider option allows the company to create users and upload their public SSH keys directly into the service, thus retaining the existing authentication method (SSH keys) with minimal changes for the clients, who only need to update the server endpoint address. Why Incorrect Options are Wrong: A: This option continues to use the self-managed EC2 instance, failing the requirement to move to a managed service. C: This requires clients to instal

</details>

### 286. dt-604

You are using an m1.small EC2 Instance with one 300GB EBS volume to host a relational database. You determined that write throughput to the database needs to be increased. Which of the following approaches can help achieve this? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Use an array of EBS volumes.; E. Increase the size of the EC2 Instance.**

</details>

### 287. dt-605

A user is hosting a website in the US West-1 region. The website has the highest client base from the Asia-Pacific (Singapore / Japan) region. The application is accessing data from S3 before serving it to client. Which of the below mentioned regions gives a better performance for S3 objects?

<details><summary>Answer</summary>

**D. US West-1.**

</details>

### 288. dt-607

Can a single EBS volume be attached to multiple EC2 instances at the same time?

<details><summary>Answer</summary>

**B. No.**

</details>

### 289. dt-608

You are planning and configuring some EBS volumes for an application. In order to get the most performance out of your EBS volumes, you should attach them to an instance with enough [...] to support your volumes.

<details><summary>Answer</summary>

**C. bandwidth.**

</details>

### 290. ce-611

A company runs a Windows-based ecommerce application on Amazon EC2 instances. The application has a very high transaction rate. The company requires a durable storage solution that can deliver 200,000 IOPS for each EC2 instance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Host the application on EC2 instances that have Provisioned IOPS SSD (io2) Block Express Amazon Elastic Block Store (Amazon EBS) volumes attached.**

The core requirements are for a durable storage solution capable of delivering 200,000 IOPS per EC2 instance for a high-transaction Windows application. Amazon EBS Provisioned IOPS SSD (io2) Block Express volumes are specifically designed for I/O-intensive, mission-critical applications requiring high durability and sub-millisecond latency. A single io2 Block Express volume can deliver up to 256,000 IOPS, which meets the 200,000 IOPS requirement. EBS volumes are inherently durable, with data being replicated within an Availability Zone to protect against component failure. This solution directly addresses all constraints of the question. Why Incorrect Options are Wrong: B: Amazon EMR is a big data processing service, not a platform for hosting transactional ecommerce applications. Also, gp3 EBS volumes max out at 16,000 IOPS, far below the required 200,000 IOPS. C: Amazon FSx for Lustre

</details>

### 291. dt-613

What is the durability of S3 RRS?

<details><summary>Answer</summary>

**A. 99.99%.**

</details>

### 292. ce-614

A company wants to run a hybrid workload for data processing. The data needs to be accessed by on- premises applications for local data processing using an NFS protocol, and must also be accessible from the AWS Cloud for further analytics and batch processing. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use an AWS Storage Gateway file gateway to provide file storage to AWS, then perform analytics on this data in the AWS Cloud.**

The requirement is for a hybrid solution that provides on-premises applications with file-based access using the NFS protocol, while also making the data available in AWS for analytics. The AWS Storage Gateway File Gateway is designed specifically for this purpose. It presents a standard NFS (or SMB) file interface to on-premises servers, while storing the data as objects in an Amazon S3 bucket. This makes the data natively accessible to AWS services like Amazon Athena, Amazon EMR, and Amazon SageMaker for analytics and batch processing, directly fulfilling all requirements of the scenario. Why Incorrect Options are Wrong: B. A Tape Gateway provides a virtual tape library (VTL) interface for backup and archival, not an NFS file interface for active data access. C. A Volume Gateway uses the iSCSI block protocol, not the required NFS file protocol. Data is stored as EBS snapshots, which ar

</details>

### 293. dt-614

Your organization is in the business of architecting complex transactional databases. For a variety of reasons, this has been done on EBS. What is AWS's recommendation for customers who have architected databases using EBS for backups?

<details><summary>Answer</summary>

**A. Backups to Amazon S3 be performed through the database management system.**

</details>

### 294. et-616

A company has deployed its newest product on AWS. The product runs in an Auto Scaling group behind a Network Load Balancer. The company stores the product’s objects in an Amazon S3 bucket. The company recently experienced malicious attacks against its systems. The company needs a solution that continuously monitors for malicious activity in the AWS account, workloads, and access patterns to the S3 bucket. The solution must also report suspicious activity and display the information on a dashboard. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure Amazon GuardDuty to monitor and report findings to AWS Security Hub.**

Amazon GuardDuty:  GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior in your AWS account. It analyzes events, such as API calls and network traffic, to detect potentially malicious activity. AWS Security Hub: AWS Security Hub is a comprehensive security service that aggregates and prioritizes security findings from various AWS services, including GuardDuty. It provides a centralized dashboard for security alerts and findings.

</details>

### 295. et-617 `cost`

A company wants to migrate an on-premises data center to AWS. The data center hosts a storage server that stores data in an NFS-based file system. The storage server holds 200 GB of data. The company needs to migrate the data without interruption to existing services. Multiple resources in AWS must be able to access the data by using the NFS protocol. Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon Elastic File System (Amazon EFS) file system.**

E. Install an AWS DataSync agent in the on-premises data center. Use a DataSync task between the on-premises location and AWS.  Amazon EFS is a scalable, fully managed file system that supports the NFSv4 protocol. It is designed to be highly available and can be mounted on multiple EC2 instances concurrently. Creating an Amazon EFS file system allows you to easily migrate the data and have multiple AWS resources access it concurrently. AWS DataSync is a service for efficiently transferring large amounts of data between on-premises storage and AWS. By installing a DataSync agent in the on-premises data center, you can use DataSync to perform the migration task. DataSync ensures efficient and secure transfer of data, making it suitable for migrating large amounts of data to AWS.

</details>

### 296. et-618

A company wants to use Amazon FSx for Windows File Server for its Amazon EC2 instances that have an SMB file share mounted as a volume in the us-east-1 Region. The company has a recovery point objective (RPO) of 5 minutes for planned system maintenance or unplanned service disruptions. The company needs to replicate the file system to the us-west-2 Region. The replicated data must not be deleted by any user for 5 years. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create an FSx for Windows File Server file system in us-east-1 that has a Multi-AZ deployment type. Use AWS Backup to create a daily backup plan that includes a backup rule that copies the backup to us-west-2. Configure AWS Backup Vault Lock in compliance mode for a target vault in us-west-2. Configure a minimum duration of 5 years.**

FSx for Windows File Server: Create an FSx for Windows File Server file system in the us-east-1 Region with a Multi-AZ deployment type. The Multi-AZ deployment type ensures high availability. AWS Backup: Use AWS Backup to create a daily backup plan for the FSx file system. Include a backup rule that copies the backup to the us-west-2 Region. This ensures that a backup is replicated to the us-west-2 Region regularly.

</details>

### 297. ce-619

A company needs to collect streaming data from several sources and store the data in the AWS Cloud. The dataset is heavily structured, but analysts need to perform several complex SQL queries and need consistent performance. Some of the data is queried more frequently than the rest. The company wants a solution that meets its performance requirements in a cost-effective manner. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Use Amazon Data Firehose to ingest the data to save it to Amazon S3. Load frequently queried data to Amazon Redshift using the COPY command. Use Amazon Redshift Spectrum for less frequently queried data.**

This solution provides the most cost-effective and performant architecture for the described scenario. Amazon Data Firehose is a fully managed service ideal for ingesting streaming data into an Amazon S3 data lake, which is a highly durable and low-cost storage solution. For the frequently queried "hot" data, loading it into Amazon Redshift local storage using the COPY command ensures the highest performance for complex SQL queries. For the less frequently queried "cold" data, Amazon Redshift Spectrum allows users to run SQL queries directly against the data in S3 without needing to load it into Redshift. This tiered approach perfectly balances consistent performance for critical queries with cost-effectiveness for the entire dataset. Why Incorrect Options are Wrong: A: Amazon Athena is designed for ad-hoc, serverless queries and may not provide the consistent performance required for co

</details>

### 298. et-620

A company is planning to deploy a business-critical application in the AWS Cloud. The application requires durable storage with consistent, low- latency performance. Which type of storage should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Provisioned IOPS SSD Amazon Elastic Block Store (Amazon EBS) volume**

Provisioned IOPS (Input/Output Operations Per Second) SSD volumes are designed to deliver predictable, consistent, and low-latency performance for critical applications. These volumes allow you to specify the amount of IOPS you need, providing a consistent level of performance regardless of the volume size.

</details>

### 299. dt-621

What happens to data on an ephemeral volume of an EBS-backed EC2 instance if it is terminated or if it fails?

<details><summary>Answer</summary>

**D. Data is deleted.**

</details>

### 300. et-621

An online photo-sharing company stores its photos in an Amazon S3 bucket that exists in the us-west-1 Region. The company needs to store a copy of all new photos in the us-east-1 Region. Which solution will meet this requirement with the LEAST operational effort?

<details><summary>Answer</summary>

**A. Create a second S3 bucket in us-east-1. Use S3 Cross-Region Replication to copy photos from the existing S3 bucket to the second S3 bucket.**

S3 Cross-Region Replication (CRR) is designed specifically for replicating objects across different AWS regions. It is a fully managed feature that automatically replicates objects from the source bucket to the destination bucket in a different region. This requires minimal operational effort as it is a built-in S3 feature for cross-region replication, and you don't have to manually trigger actions or configure additional services.

</details>

### 301. dt-623

You have just discovered that you can upload your objects to Amazon S3 using Multipart Upload API. You start to test it out but are unsure of the benefits that it would provide. Which of the following is not a benefit of using multipart uploads?

<details><summary>Answer</summary>

**D. It's more secure than normal upload.**

</details>

### 302. dt-625

Do the Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?

<details><summary>Answer</summary>

**C. Yes.**

</details>

### 303. ce-626

A solutions architect is provisioning an Amazon Elastic File System (Amazon EFS) file system to provide shared storage across multiple Amazon EC2 instances. The instances all exist in the same VPC across multiple Availability Zones. There are two instances in each Availability Zone. The solutions architect must make the file system accessible to each instance with the lowest possible latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a mount target in each Availability Zone of the VPC. Use the mount target to mount the EFS file system on the instances in the respective Availability Zone.**

To achieve the lowest possible latency when accessing an Amazon EFS file system from EC2 instances, it is a critical best practice to co-locate the EFS mount target and the EC2 instances in the same Availability Zone (AZ). An EFS mount target provides an in-VPC network endpoint for the file system within a specific AZ. By creating a mount target in each AZ where instances reside, traffic from an instance to the file system remains within that AZ. This avoids the latency overhead and data transfer costs associated with cross-AZ network communication, directly fulfilling the requirement for the lowest possible latency for all instances across the multi-AZ deployment. Why Incorrect Options are Wrong: A. Creating a single mount target in the VPC means instances in other AZs must communicate across AZ boundaries, which introduces higher latency. B. This explicitly creates a single point of ac

</details>

### 304. et-626

A company stores its data on premises. The amount of data is growing beyond the company's available capacity. The company wants to migrate its data from the on-premises location to an Amazon S3 bucket. The company needs a solution that will automatically validate the integrity of the data after the transfer. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an AWS DataSync agent on premises. Configure the DataSync agent to perform the online data transfer to an S3 bucket.**

AWS DataSync is a service designed for fast and secure online data transfer between on-premises storage and Amazon S3, Amazon EFS, or Amazon FSx for Windows File Server. DataSync automatically performs integrity validation by ensuring that the data transferred to S3 matches the source data. It uses checksums to validate the integrity of the files.

</details>

### 305. dt-631

By default, when an EBS volume is attached to a Windows instance, it may show up as any drive letter on the instance. You can change the settings of the [...] Service to set the drive letters of the EBS volumes per your specifications.

<details><summary>Answer</summary>

**C. EC2 Config Service.**

</details>

### 306. dt-632

Select the correct set of steps for exposing the snapshot only to specific AWS accounts.

<details><summary>Answer</summary>

**C. Select Public, enter the IDs of those AWS accounts, and click Save.**

</details>

### 307. et-632

A company is creating a new application that will store a large amount of data. The data will be analyzed hourly and will be modified by several Amazon EC2 Linux instances that are deployed across multiple Availability Zones. The needed amount of storage space will continue to grow for the next 6 months. Which storage solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Store the data in an Amazon Elastic File System (Amazon EFS) file system. Mount the file system on the application instances.**

Amazon EFS is a scalable and fully managed file storage service that can be mounted on multiple Amazon EC2 instances simultaneously. It provides a shared file system that can be accessed concurrently from different instances.Amazon EFS can automatically scale its file system capacity to accommodate growing data sets. It can handle a large amount of data and is designed to grow and shrink as needed.

</details>

### 308. et-634

A company collects 10 GB of telemetry data daily from various machines. The company stores the data in an Amazon S3 bucket in a source data account. The company has hired several consulting agencies to use this data for analysis. Each agency needs read access to the data for its analysts. The company must share the data from the source data account by choosing a solution that maximizes security and operational efficiency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure cross-account access for the S3 bucket to the accounts that the agencies own.**

By configuring cross-account access, you can grant permissions to specific AWS accounts (owned by the consulting agencies) to access the S3 bucket. This allows you to share the data securely with the agencies without making the data public or creating additional IAM users in the source data account.

</details>

### 309. ce-635 `availability`

An ecommerce company is redesigning a product catalog system to handle millions of products and provide fast access to product information. The system needs to store structured product data such as product name, price, description, and category. The system also needs to store unstructured data such as high-resolution product videos and user manuals. The architecture must be highly available and must be able to handle sudden spikes in traffic during large-scale sales events.

<details><summary>Answer</summary>

**B. Use Amazon DynamoDB to store product information. Store product videos and user manuals in Amazon S3.**

This solution represents a well-architected pattern for a modern, scalable ecommerce application. Amazon DynamoDB is a fully managed NoSQL database designed for applications that require single-digit millisecond latency at any scale. Its on-demand capacity mode allows it to seamlessly handle sudden traffic spikes without manual intervention, which is critical for sales events. For storing unstructured data like high-resolution videos and user manuals, Amazon S3 is the ideal choice. S3 provides highly durable, scalable, and cost-effective object storage. This separation of structured metadata (in DynamoDB) and large binary objects (in S3) is a standard best practice that optimizes for performance, scalability, and cost. Why Incorrect Options are Wrong: A: Amazon RDS, while highly available with Multi-AZ, is less suited for handling sudden, massive traffic spikes compared to DynamoDB's sea

</details>

### 310. dt-645

A company is running an SMB file server in its data center. The file server stores large files that are accessed frequently for the first few days after the files are created. After 7 days the files are rarely accessed. The total data size is increasing and is close to the company's total storage capacity. A solutions architect must increase the company's available storage space without losing low-latency access to the most recently accessed files. The solutions architect must also provide file lifecycle management to avoid future storage issues. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Install a utility on each user's computer to access Amazon S3. Create an S3 Lifecycle policy to transition the data to S3 Glacier Flexible Retrieval after 7 days.**

</details>

### 311. et-646

A solutions architect needs to host a high performance computing (HPC) workload in the AWS Cloud. The workload will run on hundreds of Amazon EC2 instances and will require parallel access to a shared file system to enable distributed processing of large datasets. Datasets will be accessed across multiple instances simultaneously. The workload requires access latency within 1 ms. After processing has completed, engineers will need access to the dataset for manual postprocessing. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon FSx for Lustre as a shared file system. Link the file system to an Amazon S3 bucket for postprocessing.**

FSx for Lustre is designed for high-performance computing workloads that require fast and scalable shared storage. It provides low-latency access to data and is well-suited for parallel processing across multiple instances.

</details>

### 312. gh-646

solutions architect needs to host a high performance computing (HPC) workload in the AWS Cloud. The workload will run on hundreds of Amazon EC2 instances and will require parallel access to a shared file system to enable distributed processing of large datasets. Datasets will be accessed across multiple instances simultaneously. The workload requires access latency within 1 ms. After processing has completed, engineers will need access to the dataset for manual postprocessing.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon FSx for Lustre as a shared file system. Link the file system to an Amazon S3 bucket for postprocessing.**

FSx for Lustre is designed for high-performance computing workloads that require fast and scalable shared storage. It provides low-latency access to data and is well-suited for parallel processing across multiple instances.

</details>

### 313. et-651 `cost`

A company stores a large volume of image files in an Amazon S3 bucket. The images need to be readily available for the first 180 days. The images are infrequently accessed for the next 180 days. After 360 days, the images need to be archived but must be available instantly upon request. After 5 years, only auditors can access the images. The auditors must be able to retrieve the images within 12 hours. The images cannot be lost during this process. A developer will use S3 Standard storage for the first 180 days. The developer needs to configure an S3 Lifecycle rule. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 180 days, S3 Glacier Instant Retrieval after 360 days, and S3 Glacier Deep Archive after 5 years.**

Each step matches one stated requirement. For the second 180 days the images are accessed infrequently but must not be lost, so S3 Standard-IA is right and S3 One Zone-IA is not, because One Zone-IA keeps the data in a single Availability Zone. After 360 days the images must still be available instantly, which is exactly what S3 Glacier Instant Retrieval provides - archive pricing with millisecond retrieval - whereas Glacier Flexible Retrieval would take minutes to hours and fails that requirement. After 5 years only auditors need the images and 12 hours is acceptable, so S3 Glacier Deep Archive, the cheapest class, is correct: its Standard retrieval completes within 12 hours, while Bulk can take up to 48. All of these classes store data redundantly across at least three Availability Zones, so nothing is at risk as the images move between them.

</details>

### 314. ce-655

A company has a business system that generates hundreds of reports each day. The business system saves the reports to a network share in CSV format. The company needs to store this data in the AWS Cloud in near-real time for analysis.

<details><summary>Answer</summary>

**B. Create an Amazon S3 File Gateway. Update the business system to use a new network share from the S3 File Gateway.**

Amazon S3 File Gateway is the ideal solution for this scenario. It provides a standard network file share (SMB or NFS) on-premises that can be used as a drop-in replacement for the existing network share. The business system can write reports to this gateway share with no application changes. The gateway then caches the data locally for low-latency access and asynchronously uploads the files as objects to Amazon S3 in near-real time. This architecture is simple, requires minimal operational overhead, and directly meets the requirement to get file-based data into S3 quickly for analysis. Why Incorrect Options are Wrong: A. A scheduled task running at the end of the day is a batch process and does not meet the "near-real time" requirement. C. Using the DataSync API to build a custom automation workflow is unnecessarily complex when a purpose-built gateway solution exists. D. This option re

</details>

### 315. dt-657

A company runs an application in the AWS Cloud that generates sensitive archival data files. The company wants to rearchitect the application's data storage. The company wants to encrypt the data files and to ensure that third parties do not have access to the data before the data is encrypted and sent to AWS. The company has already created an Amazon S3 bucket. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure the application to use client-side encryption with a key stored in AWS Key Management Service (AWS KMS). Configure the application to store the archival files in the S3 bucket.**

</details>

### 316. et-659 `security`

A company is relocating its data center and wants to securely transfer 50 TB of data to AWS within 2 weeks. The existing data center has a Site-to- Site VPN connection to AWS that is 90% utilized. Which AWS service should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**C. AWS Snowball Edge Storage Optimized**

Snowball Edge is ideal for large offline transfers (50 TB in 2 weeks) without VPN bottlenecks. DataSync (Option A) is for online transfers; Direct Connect (Option B) is too slow.

</details>

### 317. ce-661 `least-ops`

A company needs a solution to integrate transaction data from several Amazon DynamoDB tables into an existing Amazon Redshift data warehouse. The solution must maintain the provisioned throughput of DynamoDB. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create an Amazon S3 bucket. Configure DynamoDB to export to the bucket on a regular schedule. Use an Amazon Redshift COPY command to read from the S3 bucket.**

The most efficient solution with the least operational overhead is to use the managed DynamoDB export to Amazon S3 feature. This feature is specifically designed for bulk data export and does not consume any of the table's provisioned read capacity, thus having no impact on the performance of the production application. Once the data is in S3, the Amazon Redshift COPY command can be used to efficiently load the data into the data warehouse. This two-step process uses fully managed services, requires minimal configuration, and is the recommended pattern for this use case, satisfying all requirements. Why Incorrect Options are Wrong: B. Use an Amazon Redshift COPY command to read directly from each DynamoDB table. This approach directly consumes the provisioned read throughput of the DynamoDB tables, which violates a key requirement of the question. C. Create an Amazon S3 bucket. Configure

</details>

### 318. ce-663

An advertising company stores terabytes of data in an Amazon S3 data lake. The company wants to build its own foundation model (FM) and has deployed a training cluster on AWS. The company loads file-based data from Amazon S3 to the training cluster to train the FM. The company wants to reduce data loading time to optimize the overall deployment cycle. The company needs a storage solution that is natively integrated with Amazon S3. The solution must be scalable and provide high throughput. Which storage solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an Amazon FSx for Lustre file system and Amazon S3 with Data Repository Association (DRA). Preload the data from Amazon S3 to the Lustre file system to train the FM.**

Amazon FSx for Lustre is a high-performance file system optimized for compute-intensive workloads such as machine learning and high-performance computing (HPC). It provides the required high throughput and scalability. Its key feature is the native integration with Amazon S3 through a Data Repository Association (DRA). This allows the file system to be linked directly to an S3 bucket, transparently presenting S3 objects as files. The ability to preload data from S3 onto the file system before training begins directly addresses the core requirement of reducing data loading time and accelerating the overall deployment cycle. Why Incorrect Options are Wrong: A. Amazon EFS is a general-purpose file system. For this specific high-performance ML training use case, FSx for Lustre offers superior throughput and lower latency. C. Amazon EBS provides block storage attached to a single EC2 instance

</details>

### 319. ce-667

A company has deployed resources in the us-east-1 Region. The company also uses thousands of AWS Outposts servers deployed at remote locations around the world. These Outposts servers regularly download new software versions from us-east-1 that consist of hundreds of files. The company wants to improve the latency of the software download process. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an Amazon S3 bucket in us-east-1. Set up a CloudFront distribution using all edge locations with caching enabled. Configure the bucket as the origin. Download the software by using signed URLs.**

This solution correctly uses Amazon CloudFront, a content delivery network (CDN), to address the core requirement of reducing download latency for globally distributed clients (the Outposts servers). By configuring a CloudFront distribution with the S3 bucket as the origin, the software files are cached at AWS edge locations worldwide. When an Outposts server requests a file, it is routed to the nearest edge location. If the file is in the cache, it is delivered immediately, providing the lowest latency. If not, CloudFront retrieves it from the origin S3 bucket and caches it for subsequent requests from that region. This architecture is the standard AWS best practice for distributing content globally with low latency. Why Incorrect Options are Wrong: A. This option does not address the latency issue. All Outposts servers would still download directly from the single S3 bucket in us-east-

</details>

### 320. gh-667 `security`

A company is moving its data and applications to AWS during a multiyear migration project. The company wants to securely access data on
Amazon S3 from the company's AWS Region and from the company's on-premises location. The data must not traverse the internet. The company
has established an AWS Direct Connect connection between its Region and its on-premises location.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Create interface VPC endpoints (AWS PrivateLink) for Amazon S3.**

The deciding requirement is private access from on premises as well as from inside the Region. An interface endpoint places elastic network interfaces with private IP addresses in the VPC's subnets, and because those are ordinary private addresses, on-premises hosts can reach them across the existing Direct Connect connection without any traffic touching the internet. A gateway endpoint cannot do this: it is a route-table entry that only affects traffic starting inside the VPC, so requests arriving over Direct Connect or VPN cannot use it. Interface endpoints bill per endpoint-hour and per GB where gateway endpoints are free, which is why gateway endpoints stay the default when only in-VPC access is needed - but that is not the case here. On-premises clients also need DNS that resolves S3 names to the endpoint, typically through Route 53 Resolver inbound endpoints or the endpoint-specific DNS names.

</details>

### 321. gh-673

A company runs an SMB le server in its data center. The le server stores large les that the company frequently accesses for up to 7 days after
the le creation date. After 7 days, the company needs to be able to access the les with a maximum retrieval time of 24 hours.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use S3 File Gateway + Lifecycle policy to Glacier Deep Archive.**

File Gateway extends on-prem storage; Glacier Deep Archive is cost-effective for archives.
DataSync (Option A) doesn’t automate tiering.

</details>

### 322. ce-674

A company runs an HPC workload that uses a 200-TB file system on premises. The company needs to migrate this data to Amazon FSx for Lustre. Internet capacity is 10 Mbps, and all data must be migrated within 30 days. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Use an AWS Snowball Edge storage-optimized device to transfer data into S3 and link FSx for Lustre to the bucket.**

The primary constraint is transferring 200 TB of data over a 10 Mbps internet connection within 30 days. A simple calculation shows this is not feasible via the network, as it would take over five years. Therefore, an offline data transfer method is required. The AWS Snowball Edge Storage Optimized device is designed for petabyte-scale offline data migration. The process involves copying the on-premises data to the Snowball device, shipping it to AWS, and having AWS upload the data into an Amazon S3 bucket. Subsequently, an Amazon FSx for Lustre file system can be created and linked to this S3 bucket as a durable data repository. This approach bypasses the network bottleneck and meets the 30-day requirement. Why Incorrect Options are Wrong: A. AWS DMS is a service for migrating databases, not file systems. It is the incorrect tool for this type of data. B. AWS DataSync is an online data

</details>

### 323. et-675

A company uses Amazon EC2 instances and Amazon Elastic Block Store (Amazon EBS) volumes to run an application. The company creates one snapshot of each EBS volume every day to meet compliance requirements. The company wants to implement an architecture that prevents the accidental deletion of EBS volume snapshots. The solution must not change the administrative rights of the storage administrator user. Which solution will meet these requirements with the LEAST administrative effort?

<details><summary>Answer</summary>

**D. Lock the EBS snapshots to prevent deletion.**

Prevents accidental deletion without IAM changes. Recycle Bin (Option C) requires tagging; IAM (Option B) changes permissions.

</details>

### 324. dt-677 `performance`

A company is hosting a high-traffic static website on Amazon S3 with an Amazon CloudFront distribution that has a default TTL of 0 seconds. The company wants to implement caching to improve performance for the website. However, the company also wants to ensure that stale content is not served for more than a few minutes after a deployment. Which combination of caching methods should a solutions architect implement to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Set the CloudFront default TTL to 2 minutes.; E. Add a Cache-Control max-age directive of 24 hours to the objects in Amazon S3. On deployment, create a CloudFront invalidation to clear any changed files from edge caches.**

</details>

### 325. gh-680 `least-ops`

A solutions architect needs to copy les from an Amazon S3 bucket to an Amazon Elastic File System (Amazon EFS) le system and another S3
bucket. The les must be copied continuously. New les are added to the original S3 bucket consistently. The copied les should be overwritten
only if the source le changes.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Answer: A) Use DataSync with "changed data only" mode.**

Continuously syncs only modified files to S3/EFS.
Lambda (Option B) requires custom code; full syncs (Option C) are inefficient.

</details>

### 326. dt-684

A company wants to improve its ability to clone large amounts of production data into a test environment in the same AWS Region. The data is stored in Amazon EC2 instances on Amazon Elastic Block Store (Amazon EBS) volumes. Modifications to the cloned data must not affect the production environment. The software that accesses this data requires consistently high I/O performance. A solutions architect needs to minimize the time that is required to clone the production data into the test environment. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Take EBS snapshots of the production EBS volumes. Turn on the EBS fast snapshot restore feature on the EBS snapshots. Restore the snapshots into new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment.**

</details>

### 327. ce-685

A media company needs to migrate its Windows-based video editing environment to AWS. The company's current environment processes 4K video files that require sustained throughput of 2 GB per second across multiple concurrent users. The company's storage needs increase by 1 TB each week. The company needs a shared file system that supports SMB protocol and can scale automatically based on storage demands. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy an Amazon FSx for Windows File Server Multi-AZ file system with SSD storage.**

The solution requires a shared file system for a Windows-based environment that supports the SMB protocol and can deliver sustained throughput of 2 GB/s. Amazon FSx for Windows File Server is the only service that meets all these requirements. It is a fully managed native Windows file system, provides access over the SMB protocol, and can be configured with SSD storage to deliver throughput far exceeding the 2 GB/s requirement. It also allows for scaling storage capacity as data grows, fitting the company's needs for its video editing workload. Why Incorrect Options are Wrong: B. Amazon EFS does not natively support the SMB protocol; it uses the NFSv4 protocol and is primarily designed for Linux-based workloads. C. Amazon FSx for Lustre is a high-performance file system for Linux-based HPC and analytics workloads and does not provide native SMB support for Windows clients. D. Amazon S3 F

</details>

### 328. dt-685 `least-ops`

An ecommerce company wants to launch a one-deal-a-day website on AWS. Each day will feature exactly one product on sale for a period of 24 hours. The company wants to be able to handle millions of requests each hour with millisecond latency during peak hours. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use an Amazon S3 bucket to host the website's static content. Deploy an Amazon CloudFront distribution. Set the S3 bucket as the origin. Use Amazon API Gateway and AWS Lambda functions for the backend APIs. Store the data in Amazon DynamoDB.**

</details>

### 329. dt-686

A solutions architect is using Amazon S3 to design the storage architecture of a new digital media application. The media files must be resilient to the loss of an Availability Zone. Some files are accessed frequently while other files are rarely accessed in an unpredictable pattern. The solutions architect must minimize the costs of storing and retrieving the media files. Which storage option meets these requirements?

<details><summary>Answer</summary>

**B. S3 Intelligent-Tiering.**

</details>

### 330. dt-687 `cost`

A company is storing backup files by using Amazon S3 Standard storage. The files are accessed frequently for 1 month. However, the files are not accessed after 1 month. The company must keep the files indefinitely. Which storage solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create an S3 Lifecycle configuration to transition objects from S3 Standard to S3 Glacier Deep Archive after 1 month.**

</details>

### 331. dt-690

A company needs to review its AWS Cloud deployment to ensure that its Amazon S3 buckets do not have unauthorized configuration changes. What should a solutions architect do to accomplish this goal?

<details><summary>Answer</summary>

**A. Turn on AWS Config with the appropriate rules.**

</details>

### 332. dt-698 `least-ops`

A company is building an application in the AWS Cloud. The application will store data in Amazon S3 buckets in two AWS Regions. The company must use an AWS Key Management Service (AWS KMS) customer managed key to encrypt all data that is stored in the S3 buckets. The data in both S3 buckets must be encrypted and decrypted with the same KMS key. The data and the key must be stored in each of the two Regions. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a customer managed multi-Region KMS key. Create an S3 bucket in each Region. Configure replication between the S3 buckets. Configure the application to use the KMS key with client-side encryption.**

</details>

### 333. dt-700 `cost`

A development team needs to host a website that will be accessed by other teams. The website contents consist of HTML, CSS, client-side JavaScript, and images. Which method is the MOST cost-effective for hosting the website?

<details><summary>Answer</summary>

**B. Create an Amazon S3 bucket and host the website there.**

</details>

### 334. ce-705

A company is implementing a shared storage solution for a media application that the company hosts on AWS. The company needs the ability to use SMB clients to access stored data. Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**D. Create an Amazon FSx for Windows File Server file system. Connect the application server to the file system.**

Amazon FSx for Windows File Server is a fully managed, native Windows file system that provides shared storage with full support for the SMB protocol. It is designed to integrate seamlessly with Windows environments. As a managed service, AWS handles the administrative tasks of setting up, patching, and maintaining the file servers, including managing high availability and backups. This makes it the solution with the least administrative overhead compared to self-managing a file server on an EC2 instance, while directly meeting the SMB protocol requirement. Why Incorrect Options are Wrong: A. A Volume Gateway provides block-level storage via the iSCSI protocol, not file-level storage accessible via the SMB protocol. B. A Tape Gateway is a virtual tape library solution used for backup and archival purposes, not for active, shared file access. C. Creating a file share on an EC2 instance is

</details>

### 335. dt-711

A company's infrastructure consists of hundreds of Amazon EC2 instances that use Amazon Elastic Block Store (Amazon EBS) storage. A solutions architect must ensure that every EC2 instance can be recovered after a disaster. What should the solutions architect do to meet this requirement with the LEAST amount of effort?

<details><summary>Answer</summary>

**C. Use AWS Backup to set up a backup plan for the entire group of EC2 instances. Use the AWS Backup API or the AWS CLI to speed up the restore process for multiple EC2 instances.**

</details>

### 336. dt-712

A company recently migrated to the AWS Cloud. The company wants a serverless solution for large-scale parallel on-demand processing of a semistructured dataset. The data consists of logs, media files, sales transactions, and IoT sensor data that is stored in Amazon S3. The company wants the solution to process thousands of items in the dataset in parallel. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**B. Use the AWS Step Functions Map state in Distributed mode to process the data in parallel.**

</details>

### 337. dt-713

A company will migrate 10 PB of data to Amazon S3 in 6 weeks. The current data center has a 500 Mbps uplink to the internet. Other on-premises applications share the uplink. The company can use 80% of the internet bandwidth for this one-time migration task. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Order multiple AWS Snowball devices. Copy the data to the devices. Send the devices to AWS to copy the data to Amazon S3.**

</details>

### 338. dt-716

Cost Explorer is showing charges higher than expected for Amazon Elastic Block Store (Amazon EBS) volumes connected to application servers in a production account. A significant portion of the charges from Amazon EBS are from volumes that were created as Provisioned IOPS SSD (io2) volume types. Controlling costs is the highest priority for this application. Which steps should the user take to analyze and reduce the EBS costs without incurring any application downtime? (Select TWO.)

<details><summary>Answer</summary>

**B. Use the Amazon CloudWatch GetMetricData action to evaluate the read/write operations and read/write bytes of each volume.; D. Use the Amazon EC2 ModifyVolume action to change the volume type of the underutilized io2 volumes to General Purpose SSD (gp3).**

</details>

### 339. dt-718

A company is designing a website that will be hosted on Amazon S3. How should users be prevented from linking directly to the assets in the S3 bucket?

<details><summary>Answer</summary>

**B. Create an Amazon CloudFront distribution with an origin access control (OAC) and update the bucket policy to grant permission to the OAC only.**

</details>

### 340. ce-724 `least-ops`

A company wants to migrate an on-premises video processing application to AWS. Processing times range from 5 to 30 minutes. The application must run multiple jobs in parallel. The application processes videos that users upload to an Amazon S3 bucket. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure the S3 bucket to send S3 event notifications to an Amazon SQS standard queue. Deploy the application on an Amazon ECS cluster. Configure automatic scaling for AWS Fargate tasks based on the SQS queue size.**

The application's processing time can be up to 30 minutes, which exceeds the 15-minute maximum execution time for AWS Lambda functions. Therefore, a container-based solution is required. AWS Fargate is a serverless compute engine for containers that eliminates the operational overhead of managing servers. The architecture of using S3 event notifications to an SQS queue, which then triggers auto-scaled Fargate tasks, is a robust, scalable, and decoupled pattern for long-running, parallel batch processing jobs. This meets all requirements with the least operational overhead. Why Incorrect Options are Wrong: B. Using EC2 instances introduces significant operational overhead for patching and management, contradicting the "least operational overhead" requirement. A FIFO queue is unnecessary for this use case. C. This solution is not viable because the application's 30-minute runtime exceeds t

</details>

### 341. ce-726

A company is using Amazon CloudFront with its website. The company has enabled logging on the CloudFront distribution, and logs are saved in one of the company's Amazon S3 buckets. The company needs to perform advanced analyses on the logs and build visualizations. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Use standard SQL queries in Amazon Athena to analyze the CloudFront logs in the S3 bucket. Visualize the results with Amazon QuickSight.**

This solution uses the most appropriate AWS services for the task. Amazon Athena is a serverless, interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL. This avoids the need for complex ETL processes to load the CloudFront logs into a database. Amazon QuickSight is a scalable, serverless, business intelligence (BI) service that can natively connect to Athena as a data source. This allows for the creation of interactive dashboards and visualizations based on the results of the Athena queries, directly meeting the company's requirements. Why Incorrect Options are Wrong: A. AWS Glue is an ETL (extract, transform, and load) service used for data preparation and integration, not for creating visualizations or dashboards. C. Amazon DynamoDB is a NoSQL database and cannot be used to run standard SQL queries directly on log files stored in an S3 bu

</details>

### 342. ce-727

A financial services company needs to migrate an on-premises MySQL database workload to AWS. The database requires consistent low-latency performance with a baseline of 32,000 IOPS to process transactions. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Migrate the data to a Provisioned IOPS SSD io2 Amazon EBS Express volume.**

The key requirements are consistent low-latency performance and a baseline of 32,000 IOPS. Amazon EBS Provisioned IOPS SSD (io2 and io2 Block Express) volumes are designed for critical, I/O-intensive workloads like transactional databases that require low latency and high, consistent throughput. An io2 Block Express volume can be provisioned with up to 256,000 IOPS, easily meeting the 32,000 IOPS requirement. This makes it the only suitable choice among the options for a high-performance MySQL database workload. Why Incorrect Options are Wrong: A. Amazon S3 is an object storage service, not a block storage volume suitable for a transactional database file system. It does not provide IOPS guarantees. C. Amazon EFS is a network file system that generally has higher latency than direct-attached EBS block storage, making it less suitable for low-latency database transactions. D. A General Pu

</details>

### 343. dt-731 `cost`

A company wants to move its on-premises network attached storage (NAS) to AWS. The company wants to make the data available to any Linux instances within its VPC and ensure changes are automatically synchronized across all instances accessing the data store. The majority of the data is accessed very rarely, and some files are accessed by multiple users at the same time. Which solution meets these requirements and is MOST cost-effective?

<details><summary>Answer</summary>

**D. Create an Amazon Elastic File System (Amazon EFS) file system within the VPC. Set the lifecycle policy to transition the data to EFS Infrequent Access (EFS IA) after the appropriate number of days.**

</details>

### 344. ce-732 `least-ops`

A solutions architect needs to copy files from an Amazon S3 bucket to an Amazon EFS file system and another S3 bucket. The files must be copied continuously. New files are added to the original S3 bucket consistently. The copied files should be overwritten only if the source file changes. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create an AWS DataSync location for both the destination S3 bucket and the EFS file system. Create a task for the destination S3 bucket and the EFS file system. Set the transfer mode to transfer only data that has changed.**

AWS DataSync is a managed service designed for transferring large amounts of data between AWS storage services. It can be configured to run on a schedule to continuously copy new or modified files. By creating a DataSync task with locations for the source S3 bucket, destination S3 bucket, and the EFS file system, the process can be automated. The setting to "transfer only data that has changed" directly meets the requirement to overwrite files only if the source has been modified. This approach minimizes custom development and operational management, making it the solution with the least overhead. Why Incorrect Options are Wrong: B. A Lambda-based solution requires custom code to handle file copying, checksum comparisons, and error handling, which increases operational overhead compared to the managed DataSync service. C. Setting the transfer mode to "transfer all data" is inefficient an

</details>

### 345. ce-735

A solutions architect manages an analytics application. The application stores large amounts of semistructured data in an Amazon S3 bucket. The solutions architect wants to use parallel data processing to process the data more quickly. The solutions architect also wants to use information that is stored in an Amazon Redshift database to enrich the data. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon EMR to process the S3 data. Use Amazon EMR with the Amazon Redshift data to enrich the S3 data.**

The solution requires large-scale parallel data processing on S3 data and enrichment using data from Amazon Redshift. Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open-source tools such as Apache Spark and Hadoop. EMR is specifically designed for parallel processing of data stored in S3. Furthermore, EMR clusters can directly connect to Amazon Redshift using a JDBC driver to query the database and retrieve the data needed for enrichment within the same processing job. This provides a single, efficient, and powerful solution for both requirements. Why Incorrect Options are Wrong: A. Amazon Athena is an interactive query service, not a platform for large-scale, parallel ETL (Extract, Transform, Load) processing jobs. C. Amazon Kinesis Data Streams is for real-time data ingestion and streaming, not for batch processing or data enrichme

</details>

### 346. ce-738

A company is developing a photo sharing web application on AWS. The application allows users to upload, durably store, and share photos. The application processes uploaded photos into a variety of sizes. The company needs to ensure that the application can handle thousands of uploads each hour. The company wants to decouple upload operations from processing operations. Which solution will meet these requirements with the LEAST operational effort?

<details><summary>Answer</summary>

**B. Use an Amazon S3 bucket to store uploaded images. Use an S3 event notification to invoke an AWS Lambda function to process each image. Store the processed images in a second S3 bucket.**

This solution represents a classic serverless, event-driven architecture that is highly scalable, durable, and requires minimal operational effort. Using an Amazon S3 bucket for uploads provides a durable and highly available storage solution that can handle thousands of concurrent uploads. Configuring an S3 event notification to trigger an AWS Lambda function for processing decouples the upload and processing steps effectively. Lambda automatically scales to handle the processing load without requiring any server management, and you only pay for the compute time used. This design is the most efficient and serverless approach to meet all requirements. Why Incorrect Options are Wrong: A. Using EC2 instances directly for uploads and processing is not decoupled and requires significant operational effort to manage, scale, and maintain the instances. C. Polling an S3 bucket from an EC2 insta

</details>

### 347. dt-741 `cost`

A company provides an online service for posting video content and transcoding it for use by any mobile platform. The application architecture uses Amazon Elastic File System (Amazon EFS) Standard to collect and store the videos so that multiple Amazon EC2 Linux instances can access the video content for processing. As the popularity of the service has grown over time, the storage costs have become too expensive. Which storage solution is MOST cost-effective?

<details><summary>Answer</summary>

**D. Use Amazon S3 for storing the video content. Move the files temporarily over to an Amazon Elastic Block Store (Amazon EBS) volume attached to the server for processing.**

</details>

### 348. dt-743

A solutions architect is planning the deployment of a new static website. The solution must minimize costs and provide at least 99% availability. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Deploy the application to an Amazon S3 bucket in one AWS Region that has versioning disabled.**

</details>

### 349. ce-746 `performance`

A company has a video editing application that requires consistent sub-millisecond latency and high throughput to access media objects that are updated frequently. The company currently has an Amazon S3 bucket that uses the S3 Standard storage class. The company needs to improve performance while maintaining Amazon S3 API compatibility. The company needs to access the media objects within a single Availability Zone. Which storage solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an S3 directory bucket that uses the S3 Express One Zone storage class.**

The requirements for consistent sub-millisecond latency, high throughput, and single-AZ access point directly to the Amazon S3 Express One Zone storage class. This high-performance storage class is specifically designed for latency-sensitive applications, delivering single-digit millisecond request latency. It stores data in a new S3 bucket type called a directory bucket, which is optimized for performance. It maintains compatibility with common S3 APIs, meeting all the specified needs for the video editing application's frequently updated media objects. Why Incorrect Options are Wrong: A. S3 Transfer Acceleration speeds up long-distance data transfers to and from S3 buckets over the public internet; it does not reduce the access latency within the AWS region. C. "S3 table bucket and table namespace" is not a valid Amazon S3 concept or feature. This option is a distractor. D. S3 One Zone

</details>

### 350. dt-746 `cost`

A company stores call recordings on a monthly basis. Statistically, the recorded data may be referenced randomly within a year but accessed rarely after 1 year. Files that are newer than 1 year old must be queried and retrieved as quickly as possible. A delay in retrieving older files is acceptable. A solutions architect needs to store the recorded data at a minimal cost. Which solution is MOST cost-effective?

<details><summary>Answer</summary>

**B. Store individual files in Amazon S3. Use lifecycle policies to move the files to Amazon S3 Glacier after 1 year. Query and retrieve the files from Amazon S3 or S3 Glacier.**

</details>

### 351. ce-748

A research laboratory needs to process a multi-terabyte dataset multiple times each day. The laboratory requires sub-millisecond latency while processing the data. Hundreds of Amazon EC2 Linux instances will process the data from the source and store the data in a different location. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an Amazon S3 bucket to store the raw data. Create an Amazon FSx for Lustre file system that uses persistent SSD storage. Configure the FSx for Lustre file system to import data from and export data to Amazon S3. Mount the file system on the EC2 instances.**

The scenario describes a high-performance computing (HPC) workload requiring sub-millisecond latency for hundreds of EC2 instances processing a multi-terabyte dataset. Amazon FSx for Lustre is specifically designed for these types of workloads, providing a high-performance, parallel file system. Using persistent SSD storage ensures the required sub-millisecond latency and high IOPS. Integrating the file system with an Amazon S3 bucket allows for easy ingestion of the raw dataset and exporting the processed results, fitting the described workflow perfectly. Why Incorrect Options are Wrong: A. FSx for NetApp ONTAP is a general-purpose file system. While performant, FSx for Lustre is purpose-built and optimized for the massive parallelism described. C. Using HDD storage with FSx for Lustre would not meet the sub-millisecond latency requirement. A Gateway Load Balancer is irrelevant for this

</details>

### 352. dt-748

A company has no existing file share services. A new project requires access to file storage that is mountable as a drive for on-premises desktops. The file server must authenticate users to an Active Directory domain before they are able to access the storage. Which service will allow Active Directory users to mount storage as a drive on their desktops?

<details><summary>Answer</summary>

**D. AWS Storage Gateway**

</details>

### 353. ce-751

A company allows users to upload and store photos through its website. The website has users from all around the world. All images that users upload are stored in a centralized Amazon S3 bucket. The company wants to increase the speed in which its entire user base can upload photos through the website. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**D. Configure S3 Transfer Acceleration on the S3 bucket. Use the S3 Accelerate endpoint to upload files.**

The requirement is to increase upload speed for a global user base to a centralized S3 bucket. Amazon S3 Transfer Acceleration is a feature specifically designed for this purpose. It uses Amazon CloudFront's globally distributed edge locations to accelerate long-distance data transfers to Amazon S3. To utilize this feature, the application must be configured to use the special S3 Accelerate endpoint provided when the feature is enabled on the bucket. This routes traffic over an optimized network path to S3. Why Incorrect Options are Wrong: A. Amazon CloudFront is primarily optimized for content delivery (downloads) from edge locations to users, not for accelerating uploads from users to a central origin. B. This is incorrect for the same reason as option A. CloudFront's main purpose is to cache and serve content closer to users, reducing download latency. C. While configuring S3 Transfer

</details>

### 354. dt-751

A company is planning to transfer multiple terabytes of data to AWS. The data is collected offline from ships. The company wants to run complex transformation before transferring the data. Which AWS service should a solutions architect recommend for this migration?

<details><summary>Answer</summary>

**D. AWS Snowball Edge Compute Optimized**

</details>

### 355. ce-752

A company wants to build a generative AI (GenAI) model for a medical use case. The company has 50 TB of medical image data that is stored in an Amazon S3 bucket. The company plans to train the GenAI model by using Amazon SageMaker AI with multiple GPU-powered instances. The company needs a storage solution that helps ensure that the data can be loaded from storage fast enough to avoid GPU instance idle time. The storage solution needs to achieve tens of gigabits per second (Gbps) of throughput. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an Amazon FSx for Lustre file system. Move the data from Amazon S3 to Lustre by using data repository association. Mount the file system on the instances.**

The scenario requires a high-performance storage solution to feed a 50 TB dataset to multiple GPU instances for ML training, demanding tens of Gbps throughput to prevent GPU idle time. Amazon FSx for Lustre is a fully managed, high-performance file system designed for such workloads. It provides sub-millisecond latencies and hundreds of gigabytes per second of throughput. It can be linked to an S3 bucket as a data repository, allowing seamless access to the training data at the required high speeds. Why Incorrect Options are Wrong: A. Using an S3 bucket directly with file mode might not provide the consistent, low-latency, high-throughput performance needed to saturate modern GPUs, leading to I/O bottlenecks. C. "Fast file mode" is not a standard SageMaker data input mode. The primary modes are File, Pipe, and FastFile (which is for FSx for Lustre), but this option incorrectly applies it

</details>

### 356. dt-755 `cost`

A company has 700 TB of backup data stored in network attached storage (NAS) in its data center. This backup data needs to be accessible for infrequent regulatory requests and must be retained 7 years. The company has decided to migrate this backup data from its data center to AWS. The migration must be complete within 1 month. The company has 500 Mbps of dedicated bandwidth on its public internet connection available for data transfer. What should a solutions architect do to migrate and store the data at the LOWEST cost?

<details><summary>Answer</summary>

**A. Order AWS Snowball devices to transfer the data. Use a lifecycle policy to transition the files to Amazon S3 Glacier Deep Archive.**

</details>

### 357. dt-757 `cost`

A company has an application that generates a large number of files, each approximately 5 MB in size. The files are stored in Amazon S3. Company policy requires the files to be stored for 4 years before they can be deleted. Immediate accessibility is always required as the files contain critical business data that is not easy to reproduce. The files are frequently accessed in the first 30 days of the object creation but are rarely accessed after the first 30 days. Which storage solution is MOST cost-effective?

<details><summary>Answer</summary>

**C. Create an S3 bucket lifecycle policy to move files from S3 Standard to S3 Standard-Infrequent Access (S3 Standard-IA) 30 days from object creation. Delete the files 4 years after object creation.**

</details>

### 358. ce-760

A company wants to host a scalable web application on AWS. Users from around the world will access the application. Application users must have the ability to download and upload objects up to 5 GB in size. The company wants a cost-effective solution to minimize upload and download latency and maximize performance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon S3 with Transfer Acceleration to host the application.**

The core requirements are to minimize latency for both uploads and downloads of large files (up to 5 GB) for a global user base in a cost-effective manner. Amazon S3 Transfer Acceleration is specifically designed for this use case. It utilizes the globally distributed AWS Edge Locations to accelerate long-distance data transfers to and from Amazon S3. When a user uploads a file, the data is routed to the nearest Edge Location and then travels over the optimized AWS global network backbone to the S3 bucket, significantly reducing latency compared to transferring over the public internet. This directly addresses the need for fast, global uploads and downloads. Why Incorrect Options are Wrong: B. Use Amazon S3 with Cache-Control headers to host the application. Cache-Control headers are for browser/CDN caching of downloaded objects to speed up subsequent requests. They do not accelerate the

</details>

### 359. ce-764

A company wants to improve its ability to clone large amounts of production data into a test environment in the same AWS Region. The data is stored on Amazon EBS volumes that are attached to Amazon EC2 instances. Modifications to the cloned data must not affect the production environment. The software that accesses this data requires consistently high I/O performance. A solutions architect needs to minimize the time required to clone the production data into the test environment. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Take EBS snapshots of the production EBS volumes. Enable EBS fast snapshot restore on the snapshots. Restore the snapshots into new EBS volumes. Attach the new EBS volumes to EC2 instances in the test environment.**

The solution must provide an isolated, high-performance copy of production data in the shortest possible time. Creating an EBS snapshot and restoring it to a new volume ensures data isolation. However, standard restored volumes experience a performance "warm-up" period as data is lazily loaded from S3. This conflicts with the high I/O requirement. EBS Fast Snapshot Restore (FSR) is designed for this exact use case. By enabling FSR on the snapshot, any new EBS volumes created from it are fully initialized at creation. This eliminates the initial performance latency, ensuring the volume delivers its full provisioned performance immediately. This approach minimizes the time to get a fully performant test environment running. Why Incorrect Options are Wrong: A. Restoring a snapshot to an EC2 instance store is not a direct operation and would be slow. Instance store is also ephemeral, making

</details>

### 360. ce-770

A company has developed a new content-sharing application that runs on Amazon ECS. The application runs on Amazon Linux Docker tasks that use the Amazon EC2 launch type. The application requires a storage solution that has the following characteristics: • Accessibility for multiple ECS tasks through bind mounts • Resiliency across Availability Zones • Burstable throughput of up to 3 Gbps • Ability to scale up over time Which storage solution meets these requirements?

<details><summary>Answer</summary>

**B. Create an Amazon EFS file system. Configure the ECS task definitions to mount the EFS file-system volume at launch.**

Amazon EFS is the ideal solution as it meets all the specified requirements. It provides a managed, scalable, and shared file system based on the NFSv4 protocol, which is natively supported by Amazon Linux. EFS Standard storage is inherently resilient, storing data across multiple Availability Zones (AZs). It integrates seamlessly with Amazon ECS, allowing multiple tasks to mount and access the same file system concurrently. EFS offers Elastic Throughput mode, which automatically scales performance to meet application needs, and can provide throughput well in excess of the required 3 Gbps, making it suitable for burstable workloads. Why Incorrect Options are Wrong: A. Amazon FSx for Windows File Server is optimized for Windows workloads using the SMB protocol, not for the Amazon Linux environment specified in the scenario. C. Amazon EBS volumes with Multi-Attach are restricted to a singl

</details>

### 361. ce-771

A company runs multiple applications in multiple AWS accounts within the same organization in AWS Organizations. A content management system (CMS) runs on Amazon EC2 instances in a VPC. The CMS needs to access shared files from an Amazon Elastic File System (Amazon EFS) file system that is deployed in a separate AWS account. The EFS account is in a separate VPC. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Enable VPC sharing between the two accounts. Use the EFS mount helper to mount the file system on the EC2 instances. Redeploy the EFS file system in a shared subnet.**

The core of the problem is enabling network connectivity between two separate VPCs in different AWS accounts. Option B provides a complete and valid solution using AWS-native features. VPC sharing allows an account (the EFS owner) to share subnets with other accounts (the EC2 participant) within the same AWS Organization. By redeploying the EFS mount targets into a shared subnet, the EC2 instances in the other account can be launched into that same shared subnet. This places both the EC2 instances and the EFS mount targets within the same network boundary, establishing the required connectivity to mount the file system using the standard EFS mount helper. Why Incorrect Options are Wrong: A: Amazon EFS does not use Elastic IP addresses. File systems are accessed via DNS names that resolve to private IP addresses of mount targets within a VPC. C: AWS Systems Manager Run Command is a tool t

</details>

### 362. dt-772

A company hosts an application on AWS. The application gives users the ability to upload photos and store the photos in an Amazon S3 bucket. The company wants to use Amazon CloudFront and a custom domain name to upload the photo files to the S3 bucket in the eu-west-1 Region. Which solution will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use AWS Certificate Manager (ACM) to create a public certificate in the us-east-1 Region. Use the certificate in CloudFront.; D. Configure Amazon S3 to allow uploads from CloudFront origin access control (OAC).**

</details>

### 363. ce-775

A company uses an Amazon S3 bucket as its data lake storage platform The S3 bucket contains a massive amount of data that is accessed randomly by multiple teams and hundreds of applications. The company wants to reduce the S3 storage costs and provide immediate availability for frequently accessed objects What is the MOST operationally efficient solution that meets these requirements?

<details><summary>Answer</summary>

**A. Create an S3 Lifecycle rule to transition objects to the S3 Intelligent-Tiering storage class**

The S3 Intelligent-Tiering storage class is specifically designed for data with unknown, changing, or unpredictable access patterns, which matches the scenario of a data lake with random access. It automatically optimizes storage costs by moving objects between a frequent access tier and an infrequent access tier based on usage, without any performance impact, retrieval fees, or operational overhead. This solution directly addresses the need to reduce costs while maintaining immediate availability for frequently accessed objects in the most operationally efficient manner, as it requires only a simple lifecycle rule to enable and is fully managed by AWS. Why Incorrect Options are Wrong: B: S3 Glacier is an archive storage class with retrieval times ranging from minutes to hours. This violates the requirement for immediate availability for frequently accessed objects. C: Using S3 Storage C

</details>

### 364. ce-781 `availability`

A company stores user data in AWS. The data is used continuously with peak usage during business hours. Access patterns vary, with some data not being used for months at a time. A solutions architect must choose a cost-effective solution that maintains the highest level of durability while maintaining high availability. Which storage solution meets these requirements?

<details><summary>Answer</summary>

**B. Amazon S3 Intelligent-Tiering**

The scenario requires a storage solution that is cost-effective for data with unknown or changing access patterns, while also providing the highest levels of durability and availability. Amazon S3 Intelligent-Tiering is specifically designed for this use case. It automatically monitors access patterns and moves objects that have not been accessed to lower-cost access tiers, such as the Infrequent Access tier. This optimizes costs without performance impact, operational overhead, or compromising on the high durability (99.999999999%) and high availability provided by replicating data across multiple Availability Zones. This perfectly matches the requirement for continuous use with periods of inactivity. Why Incorrect Options are Wrong: A. Amazon S3 Standard is not the most cost-effective solution because it does not automatically reduce costs for data that becomes infrequently accessed. C

</details>

### 365. ce-782 `cost`

A weather forecasting company collects temperature readings from various sensors on a continuous basis. An existing data ingestion process collects the readings and aggregates the readings into larger Apache Parquet files. Then the process encrypts the files by using client-side encryption with KMS managed keys (CSE-KMS). Finally, the process writes the files to an Amazon S3 bucket with separate prefixes for each calendar day. The company wants to run occasional SQL queries on the data to take sample moving averages for a specific calendar day. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Configure Amazon Athena to read the encrypted files. Run SQL queries on the data directly in Amazon S3.**

Amazon Athena is a serverless, interactive query service designed for analyzing data directly in Amazon S3 using standard SQL. It is the most cost-effective solution for this scenario because its pricing model is pay-per-query, based on the amount of data scanned. Since the queries are occasional, there are no idle infrastructure costs. Athena natively supports querying data stored in Apache Parquet format and can decrypt data that was encrypted using client-side encryption with AWS KMS-managed keys (CSE-KMS), provided the query role has the necessary KMS permissions. This directly meets all the requirements of the scenario in the most economical way. Why Incorrect Options are Wrong: B. Amazon S3 Select cannot decrypt client-side encrypted objects. It only works with unencrypted or server-side encrypted objects, and it is designed for simple filtering on a single object. C. Amazon Redshi

</details>

### 366. ce-783

A company runs an environment where data is stored in an Amazon S3 bucket. The objects are accessed frequently throughout the day. The company has strict data encryption requirements fordata that is stored in the S3 bucket. The company currently uses AWS Key Management Service (AWS KMS) for encryption. The company wants to optimize costs associated with encrypting S3 objects without making additional calls to AWS KMS. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an S3 Bucket Key for server-side encryption with AWS KMS keys (SSE-KMS) on the new objects.**

The most effective way to reduce AWS Key Management Service (AWS KMS) costs for Amazon S3 is by using an S3 Bucket Key. When you enable an S3 Bucket Key for server-side encryption with KMS (SSE-KMS), Amazon S3 generates a short-lived, bucket-level key from AWS KMS. This bucket key is then used to create unique data keys for individual objects within the bucket. This process significantly reduces the request traffic from S3 to KMS because S3 does not need to make a request to KMS for every single object-level encryption operation. This directly addresses the requirement to optimize costs by reducing KMS API calls. Why Incorrect Options are Wrong: A. Using SSE-S3 removes the use of AWS KMS entirely. While this eliminates KMS costs, it may not meet the company's strict encryption requirements, which often involve the additional audit and control features of customer-managed KMS keys. C. Cli

</details>

### 367. ce-786 `cost`

A company is using AWS DataSync to migrate millions of files from an on-premises system to AWS. The files are 10 KB in size on average. The company wants to use Amazon S3 for file storage. For the first year after the migration the files will be accessed once or twice and must be immediately available. After 1 year the files must be archived for at least 7 years. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Use an archive tool lo group the files into large objects. Use DataSync to migrate the objects. Store the objects in S3 Glacier Instant Retrieval for the first year. Use a lifecycle configuration to transition the files to S3 Glacier Deep Archive after 1 year with a retention period of 7 years.**

This solution is the most cost-effective because it addresses two key cost drivers in the scenario: the high number of small files and the long-term archival requirement. 1. Aggregating Files: Using an archive tool (e.g., TAR, ZIP) to group millions of 10 KB files into larger objects significantly reduces costs. It minimizes the number of per-object charges for PUT requests during the initial migration and for lifecycle transition requests later. 2. Optimal Storage Classes: S3 Glacier Instant Retrieval is ideal for the first year, providing the required immediate access for infrequent use at a lower storage cost than S3 Standard-IA. For the subsequent 7-year archival period, transitioning to S3 Glacier Deep Archive provides the lowest possible storage cost, which is appropriate for data that will not be accessed again. Why Incorrect Options are Wrong: B: This option is less cost-effectiv

</details>

### 368. ce-788

A company has stored millions of objects across multiple prefixes in an Amazon S3 bucket by using the Amazon S3 Glacier Deep Archive storage class. The company needs to delete all data older than 3 years except for a subset of data that must be retained. The company has identified the data that must be retained and wants to implement a serverless solution. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Enable S3 Inventory. Create an AWS Lambda function to filter and delete objects. Invoke the Lambda function with S3 Batch Operations to delete objects by using the inventory reports.**

This solution is fully serverless and highly scalable, meeting all the requirements. Amazon S3 Inventory is the recommended service for generating lists of millions of objects and their metadata. S3 Batch Operations is a managed service specifically designed to perform bulk actions on objects listed in a manifest, such as an S3 Inventory report. By configuring the S3 Batch Operations job to invoke an AWS Lambda function, the company can implement custom logic to programmatically check each object's age and determine if it belongs to the subset that must be retained before issuing a delete command. This combination is the most efficient and purpose-built approach. Why Incorrect Options are Wrong: A. This solution is not serverless as it requires provisioning and managing an Amazon EC2 instance to run the deletion script, which directly contradicts the problem's requirements. B. While AWS

</details>

### 369. ce-797

A company runs its production workload on Amazon EC2 instances with Amazon Elastic Block Store (Amazon EBS) volumes. A solutions architect needs to analyze the current EBS volume cost and to recommend optimizations. The recommendations need to include estimated monthly saving opportunities. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Compute Optimizer to generate EBS volume recommendations for optimization.**

AWS Compute Optimizer is a service designed to analyze the configuration and utilization metrics of your AWS resources to recommend optimal configurations for reducing costs and improving performance. It specifically analyzes Amazon EBS volumes to identify opportunities for optimization, such as changing the volume type or size. Crucially, it provides data-driven recommendations that include estimated monthly savings, directly fulfilling the core requirements of the scenario. The service uses machine learning to analyze historical utilization data from Amazon CloudWatch to generate these recommendations. Why Incorrect Options are Wrong: A. Amazon Inspector is a security vulnerability assessment service. It scans for software vulnerabilities and unintended network exposure, not for cost optimization opportunities. B. AWS Systems Manager is an operational management service for patching, c

</details>

### 370. ce-799

A solutions architect is designing the architecture for a company website that is composed of static content. The company's target customers are located in the United States and Europe. Which architecture should the solutions architect recommend to MINIMIZE cost?

<details><summary>Answer</summary>

**A. Store the website files on Amazon S3 in the us-east-2 Region. Use an Amazon CloudFront distribution with the price class configured to limit the edge locations in use.**

The most cost-effective architecture for serving static content to users in the United States and Europe is to store the content in a single Amazon S3 bucket and use an Amazon CloudFront distribution. To minimize cost, the CloudFront distribution should be configured with a price class that only includes edge locations in the required regions (North America and Europe). This avoids paying higher data transfer rates for more expensive edge locations in other parts of the world where the target customers are not located. Using a single S3 bucket as the origin is simpler and cheaper than replicating data across multiple regions. Why Incorrect Options are Wrong: B: Maximizing the use of edge locations (PriceClassAll) is the most expensive option and provides no benefit since the target audience is limited to the US and Europe. C: This option introduces unnecessary cost and complexity by repl

</details>

### 371. ce-805 `cost`

A company is designing a new application that uploads files to an Amazon S3 bucket. The uploaded files are processed to extract metadata. Processing must take less than 5 seconds. The volume and frequency of the uploads vary from a few files each hour to hundreds of concurrent uploads. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Configure a new object created S3 event notification within the bucket to invoke an AWS Lambda function to process the files.**

The most cost-effective and efficient solution is to use an event-driven, serverless architecture. Configuring an S3 event notification to trigger an AWS Lambda function when a new object is created is the standard pattern for this use case. This approach is highly scalable, automatically handling hundreds of concurrent uploads without manual intervention. Since Lambda is a serverless compute service, you only pay for the compute time consumed during function execution (billed in milliseconds), making it extremely cost-effective for workloads with variable frequency. The invocation is nearly instantaneous, easily meeting the sub-5-second processing requirement. Why Incorrect Options are Wrong: A. AWS CloudTrail is an auditing service with event delivery latency of up to 15 minutes, failing the performance requirement. AWS AppSync is a managed GraphQL service, not a file processing tool.

</details>

### 372. ce-811

A company uses an AWS Transfer for SFTP public server endpoint and Amazon S3 storage to host large datasets for its customers. The company provides customers SSH private keys to authenticate and download their datasets. The Transfer for SFTP server is configured with structured logging that is saved to an S3 bucket. The company wants to charge customers based on their monthly data download usage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Run Amazon Athena queries on the logging S3 bucket monthly to identify customer usage and calculate costs. Add the charges to the customers' monthly bills.**

The scenario requires tracking data download usage per customer for billing. The AWS Transfer for SFTP server is configured with structured logging to an Amazon S3 bucket. These logs contain detailed, user-level information about each session, including the username, the type of activity (e.g., download), and the number of bytes transferred. Amazon Athena is a serverless, interactive query service designed to analyze data directly in Amazon S3 using standard SQL. By running monthly Athena queries against the S3 bucket containing the Transfer for SFTP logs, the company can aggregate the total data downloaded by each specific username. This provides the precise per-customer usage data needed to calculate costs and generate bills. Why Incorrect Options are Wrong: A. Configure VPC Flow Logs... VPC Flow Logs track IP traffic at the network interface level. They lack application-level details

</details>

### 373. ce-813 `least-ops`

A company uses AWS Cost Explorer to monitor its AWS costs. The company notices that Amazon Elastic Block Store (Amazon EBS) storage and snapshot costs increase every month. However, the company does not purchase additional EBS storage every month. The company wants to optimize monthly costs for its current storage usage. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Delete all nonessential snapshots. Use Amazon Data Lifecycle Manager to create and manage the snapshots according to the company's snapshot policy requirements.**

The primary cause of continuously increasing Amazon EBS costs, when no new volumes are being provisioned, is the accumulation of snapshots. Snapshots are incremental, but deleting a volume does not delete its snapshots. Over time, if old snapshots are not pruned, the storage costs will steadily rise. Amazon Data Lifecycle Manager (DLM) is a managed service designed to automate the creation, retention, and deletion of EBS snapshots. By creating a lifecycle policy, the company can define a retention schedule (e.g., keep daily snapshots for 7 days, weekly for 4 weeks). DLM will then automatically manage the snapshot lifecycle, deleting old ones as they expire. This directly addresses the cost issue with the least possible operational overhead, as it is a "set and forget" automated solution. Why Incorrect Options are Wrong: A. You cannot use Amazon EBS Elastic Volumes to reduce the size of a

</details>

### 374. ce-821

A company's expense tracking application gives users the ability to upload images of receipts. The application analyzes the receipts to extract information and stores the raw images in Amazon S3. The application is written in Java and runs on Amazon EC2 On-Demand Instances in an Auto Scaling group behind an Application Load Balancer. The compute costs and storage costs have increased with the popularity of the application. Which solution will provide the MOST cost savings without affecting application performance?

<details><summary>Answer</summary>

**D. Purchase a Compute Savings Plan for the minimum number of necessary EC2 instances. Use On- Demand Instances for peak scaling. Set up S3 Lifecycle policies to archive the raw images to lower- cost storage tiers after 30 days.**

This solution provides the most significant cost savings by addressing both compute and storage costs without impacting application performance. Purchasing a Compute Savings Plan for the minimum number of EC2 instances covers the baseline, predictable workload at a discounted rate. The Auto Scaling group can still scale out using On-Demand instances to handle peak traffic, ensuring performance is maintained. For storage, implementing S3 Lifecycle policies is the standard and most effective method to reduce costs. It automatically transitions older, less frequently accessed receipt images to lower-cost storage tiers like S3 Glacier Instant Retrieval or S3 Glacier Flexible Retrieval, directly addressing the rising storage costs mentioned in the scenario. Why Incorrect Options are Wrong: A. Purchasing a Savings Plan for the maximum number of instances is inefficient, as you would pay for un

</details>

### 375. ce-822 `cost`

A gaming company hosts a browser-based application on AWS. The users of the application consume a large number of videos and images that are stored in Amazon S3. This content is the same for all users. The application has increased in popularity, and millions of users worldwide are accessing these media files. The company wants to provide the files to the users while reducing the load on the origin. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Deploy an Amazon CloudFront web distribution in front of the S3 bucket.**

The scenario requires distributing static media files (videos, images) from an Amazon S3 bucket to a large, global user base while reducing the load on the S3 origin. Amazon CloudFront is a Content Delivery Network (CDN) specifically designed for this purpose. It caches copies of the S3 content at edge locations worldwide, physically closer to the users. When a user requests a file, it is served from the nearest edge location, which significantly reduces latency and improves performance. This caching mechanism also minimizes direct requests to the S3 bucket, thereby reducing origin load and often lowering data transfer costs. Why Incorrect Options are Wrong: A. AWS Global Accelerator improves network pathing to application endpoints but does not cache content. It would not reduce the request load on the S3 origin. C. Amazon ElastiCache (Redis OSS) is an in-memory caching service used to

</details>

### 376. ce-827 `cost`

A company recently migrated its application to AWS. The application runs on Amazon EC2 Linux instances in an Auto Scaling group across multiple Availability Zones. The application stores data in an Amazon Elastic File System (Amazon EFS) file system that uses EFS Standard-Infrequent Access storage. The application indexes the company's files, and the index is stored in an Amazon RDS database. The company needs to optimize storage costs with some application and services changes. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create an Amazon S3 bucket that uses an Intelligent-Tiering lifecycle policy. Copy all files to the S3 bucket. Update the application to use Amazon S3 API to store and retrieve files.**

The most cost-effective solution is to migrate the files from Amazon EFS to an Amazon S3 bucket and use the S3 Intelligent-Tiering storage class. S3 object storage is significantly less expensive per GB than EFS file storage, even when compared to EFS Infrequent Access (IA). The S3 Intelligent-Tiering storage class automatically optimizes costs by moving data between frequent and infrequent access tiers based on usage patterns, without performance impact or retrieval fees. While this requires updating the application to use the S3 API instead of a file system mount, the question explicitly allows for application changes to achieve the primary goal of cost optimization. This approach provides the lowest storage cost while maintaining high availability and immediate data access. Why Incorrect Options are Wrong: B. Amazon FSx for Windows File Server is designed for Windows-based application

</details>

### 377. ce-828

A company is migrating a data processing application to AWS. The application processes several short-lived batch jobs that cannot be disrupted. The process generates data after each batch job finishes running. The company accesses the data for 30 days following data generation. After 30 days, the company stores the data for 2 years. The company wants to optimize costs for the application and data storage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon EC2 On-Demand Instances to run the application. Store the data in Amazon S3 Standard. Move the data to S3 Glacier Deep Archive after 30 days. Configure an S3 Lifecycle configuration to delete the data after 2 years.**

The solution must address two key requirements: non-disruptible compute and cost-optimized, tiered data storage. 1. Compute: The batch jobs "cannot be disrupted," which makes Amazon EC2 On-Demand Instances the correct choice. Amazon EC2 Spot Instances are not suitable because they can be interrupted by AWS with a two-minute warning, which violates this core requirement. 2. Storage & Lifecycle: The data requires frequent access for the first 30 days, making Amazon S3 Standard the appropriate initial storage class. For long-term archival of 2 years with minimal expected access, Amazon S3 Glacier Deep Archive is the most cost-effective option. An S3 Lifecycle configuration is the standard, automated mechanism to transition objects between storage classes (e.g., from S3 Standard to S3 Glacier Deep Archive) and to permanently delete them (expire) after a specified period. Why Incorrect Option

</details>

### 378. ce-830

A company runs an online order management system on AWS. The company stores order and inventory data for the previous 5 years in an Amazon Aurora MySQL database. The company deletes inventory data after 5 years. The company wants to optimize costs to archive data. Options:

<details><summary>Answer</summary>

**B. Use the SELECT INTO OUTFILE S3 query on the Aurora database to export the data to Amazon S3. Configure S3 Lifecycle rules on the S3 bucket.**

The most direct and cost-effective method to archive data from Amazon Aurora MySQL is to use the native SELECT INTO OUTFILE S3 command. This feature allows you to run a SQL query to select the specific data for archiving (e.g., records older than five years) and save the results directly to an Amazon S3 bucket. This avoids the need for intermediate services or complex ETL jobs. Once the data is in S3, configuring S3 Lifecycle rules is the standard best practice to automatically transition the data to more cost-effective storage classes like S3 Glacier Instant Retrieval or S3 Glacier Deep Archive, and eventually delete it, optimizing storage costs over the long term. Why Incorrect Options are Wrong: A. An AWS Glue crawler's purpose is to discover data and populate the Glue Data Catalog, not to export data. An AWS Glue ETL job would be required for the export, making this solution unnecess

</details>

### 379. ce-832 `cost`

A company runs an application on several Amazon EC2 instances that store persistent data on an Amazon Elastic File System (Amazon EFS) file system. The company needs to replicate the data to another AWS Region by using an AWS managed service solution. Which solution will meet these requirements MOST cost-effectively? Options:

<details><summary>Answer</summary>

**D. Use AWS Backup to create a backup plan with a rule that takes a daily backup and replicates it to another Region. Assign the EFS file system resource to the backup plan.**

AWS Backup is a fully managed, centralized service designed to automate data protection across AWS services, including Amazon EFS. It allows you to create backup plans that define backup frequency, retention, and lifecycle policies. A key feature is the ability to copy backups to a different AWS Region, which directly addresses the replication requirement. This approach is highly cost-effective because AWS Backup performs incremental backups for EFS after the initial full backup, minimizing the amount of data transferred and stored. This eliminates the operational overhead and complexity of managing custom scripts or separate replication infrastructure, making it the most cost-effective and managed solution for this scenario. Why Incorrect Options are Wrong: A. The EFS-to-EFS backup solution is an AWS Solutions Implementation, not a native, fully managed service like AWS Backup. It requi

</details>

### 380. ce-836

A company wants to store a large amount of data as objects for analytics and long-term archiving. Resources from outside AWS need to access the dat a. The external resources need to access the data with unpredictable frequency. However, the external resource must have immediate access when necessary. The company needs a cost-optimized solution that provides high durability and data security. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Store the data in Amazon S3 Intelligent-Tiering.**

The Amazon S3 Intelligent-Tiering storage class is specifically designed for data with unknown, changing, or unpredictable access patterns. It automatically optimizes storage costs by moving objects between frequent and infrequent access tiers based on usage, without any performance impact or retrieval fees. This meets the core requirements of cost optimization for unpredictable access frequency while ensuring that data is always available for immediate access (millisecond latency) when needed for analytics. The high durability and security features of Amazon S3 are inherent to this storage class. Why Incorrect Options are Wrong: A. S3 Glacier Deep Archive has retrieval times of up to 12 hours, which violates the requirement for immediate access when necessary. C. S3 Glacier Flexible Retrieval is an archive class. While expedited retrievals are fast (1-5 minutes), they are not "immediate

</details>

### 381. ce-838

A company wants to share data that is collected from self-driving cars with the automobile community. The data will be made available from within an Amazon S3 bucket. The company wants to minimize its cost of making this data available to other AWS accounts. What should a solutions architect do to accomplish this goal?

<details><summary>Answer</summary>

**B. Configure the S3 bucket to be a Requester Pays bucket.**

The most direct and effective way to minimize the data provider's cost is to shift the financial responsibility for data access to the consumers. The Amazon S3 Requester Pays feature is designed for this exact scenario. When a bucket is configured as "Requester Pays," the AWS account that requests the data (the downloader) pays for the associated data transfer and request costs, not the bucket owner. This reduces the company's cost for sharing the data to nearly zero, directly fulfilling the primary requirement. Why Incorrect Options are Wrong: A. An S3 VPC endpoint provides a private connection from a VPC to S3, which can reduce data transfer costs for resources within that VPC, but it does not shift costs to external requesters. C. An Amazon CloudFront distribution can lower data transfer costs for the bucket owner by caching data, but the owner still incurs CloudFront's data egress ch

</details>

### 382. ce-841

A company runs an application on Amazon EC2 instances across multiple Availability Zones in the same AWS Region. The EC2 instances share an Amazon Elastic File System (Amazon EFS) volume that is mounted on all the instances. The EFS volume stores a variety of files such as installation media, third-party files, interface files, and other one-time files. The company accesses some EFS files frequently and needs to retrieve the files quickly. The company accesses other files rarely. The EFS volume is multiple terabytes in size. The company needs to optimize storage costs for Amazon EFS. Which solution will meet these requirements with the LEAST effort?

<details><summary>Answer</summary>

**B. Apply a lifecycle policy to the EFS files to move the files to EFS Infrequent Access.**

Amazon EFS Lifecycle Management is the most suitable solution as it is designed to optimize costs with the least effort. By enabling a lifecycle policy, files that are not accessed for a specified period are automatically and transparently moved from the EFS Standard storage class to the lower-cost EFS Infrequent Access (IA) storage class. This process requires no changes to the application, as the file system's structure and access methods remain the same. This directly addresses the need to reduce costs for rarely accessed files while maintaining high performance for frequently accessed ones, fulfilling all requirements with minimal administrative overhead. Why Incorrect Options are Wrong: A. Moving files to Amazon S3 requires re-architecting the application to use S3 APIs instead of file system mounts, which is a significant effort. C. Amazon EBS volumes cannot be mounted to multiple

</details>

### 383. ce-842

A company is creating a web application that will store a large number of images in Amazon S3. The images will be accessed by users over variable periods of time. The company wants to: Retain all the images. Incur no cost for retrieval. Have minimal management overhead. Have the images available with no impact on retrieval time. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Implement S3 Intelligent-Tiering.**

The S3 Intelligent-Tiering storage class is specifically designed for data with unknown or changing access patterns, which aligns with the scenario. It automatically moves objects between frequent and infrequent access tiers without performance impact, operational overhead, or retrieval fees. This solution meets all the company's requirements: it retains all images, has no retrieval costs, requires minimal management as it is automated, and provides the same low-latency access as S3 Standard, ensuring no impact on retrieval time. Why Incorrect Options are Wrong: B. Implement S3 storage class analysis: This is an analytics tool that provides recommendations for lifecycle policies. It does not store or move data itself and would increase management overhead, as an administrator must act on its findings. C. Implement an S3 Lifecycle policy to move data to S3 Standard-Infrequent Access (S3 S

</details>

### 384. ce-843

An adventure company has launched a new feature on its mobile app. Users can use the feature to upload their hiking and rafting photos and videos anytime. The photos and videos are stored in Amazon S3 Standard storage in an S3 bucket and are served through Amazon CloudFront. The company needs to optimize the cost of the storage. A solutions architect discovers that most of the uploaded photos and videos are accessed infrequently after 30 days. However, some of the uploaded photos and videos are accessed frequently after 30 days. The solutions architect needs to implement a solution that maintains millisecond retrieval availability of the photos and videos at the lowest possible cost. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure S3 Intelligent-Tiering on the S3 bucket.**

The scenario describes data with unpredictable access patterns: most objects become infrequently accessed after 30 days, but some remain frequently accessed. The solution must optimize storage costs while maintaining millisecond retrieval performance. S3 Intelligent-Tiering is specifically designed for this use case. It automatically monitors object access patterns and moves objects between a Frequent Access tier and an Infrequent Access tier without performance impact or retrieval fees. This provides the low-latency, high-throughput performance of S3 Standard while automatically reducing storage costs for objects that are not accessed, perfectly matching the requirements. Why Incorrect Options are Wrong: B. S3 Glacier Deep Archive has retrieval times of several hours, which violates the strict requirement for millisecond retrieval availability. C. Amazon EFS is a file storage service, w

</details>

### 385. ce-845

A company wants to create a long-term storage solution that will allow users to upload terabytes of images and videos. The company will use the images and videos to train machine learning (ML) models. The storage solution must be scalable and cost-optimized. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Provision an Amazon S3 bucket for users to upload images and videos. Configure the S3 bucket to make the data available to Amazon SageMaker AI training. Store the data in the S3 Intelligent-Tiering storage class.**

This solution meets all requirements effectively. Amazon S3 provides a highly scalable, durable, and cost-effective object storage solution suitable for terabytes of data. Using the S3 Intelligent-Tiering storage class automatically optimizes storage costs by moving data between frequent and infrequent access tiers based on usage patterns, which is ideal for long-term storage with unpredictable access. Amazon SageMaker natively integrates with Amazon S3, allowing ML models to be trained directly on the data stored in the S3 bucket without needing to copy it to a separate, more expensive file system. This architecture is scalable, cost-optimized, and purpose-built for ML workloads on AWS. Why Incorrect Options are Wrong: A. Copying terabytes of data to Amazon FSx for Lustre for long-term storage is not cost-optimized. FSx for Lustre is a high-performance file system designed for temporary

</details>

### 386. ce-847 `cost`

A company wants to release a new device that will collect data to track overnight sleep on an intelligent mattress. Sensors will send data that will be uploaded to an Amazon S3 bucket. Each mattress generates about 2 MB of data each night. An application must process the data and summarize the data for each user. The application must make the results available as soon as possible. Every invocation of the application will require about 1 GB of memory and will finish running within 30 seconds. Which solution will run the application MOST cost-effectively?

<details><summary>Answer</summary>

**A. AWS Lambda with a Python script**

The scenario describes an event-driven workload where small data files (2 MB) trigger a short-running process (30 seconds) with moderate memory needs (1 GB). AWS Lambda is perfectly suited for this use case. It can be configured to trigger automatically when a new object is created in the S3 bucket, satisfying the "as soon as possible" requirement. Lambda's pricing model is pay-per-invocation and compute duration (measured in milliseconds), meaning you only pay for the exact resources consumed. This serverless model eliminates costs for idle time, making it the most cost-effective solution for this specific pattern. Why Incorrect Options are Wrong: B. AWS Glue with a Scala job: AWS Glue is an ETL service designed for large-scale data processing. It has a minimum billing duration, making it significantly more expensive for a 30-second task on a small file. C. Amazon EMR with an Apache Spa

</details>

### 387. ce-848 `cost`

A company is building a new web application on AWS. The application needs to consume files from a legacy on-premises application that runs a batch process and outputs approximately 1 GB of data every night to an NFS file mount. A solutions architect needs to design a storage solution that requires minimal changes to the legacy application and keeps costs low. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Deploy an Amazon S3 File Gateway on premises. Point the legacy application to the File Gateway. Configure the web application to retrieve the files from the S3 bucket that the File Gateway uses.**

The most cost-effective solution that requires minimal changes is to use an Amazon S3 File Gateway. The File Gateway is deployed on-premises and presents a standard Network File System (NFS) endpoint. The legacy application can be pointed to this new NFS mount, which requires a trivial configuration change. The gateway then automatically and asynchronously uploads the files written to it as objects into a specified Amazon S3 bucket. The new web application running on AWS can then directly and natively access these file objects from the S3 bucket. This architecture perfectly bridges the on-premises file-based application with cloud-native object storage, meeting all requirements efficiently. Why Incorrect Options are Wrong: A. AWS Outposts involves deploying an entire rack of AWS-managed hardware on-premises. This is a very high-cost solution designed for low-latency workloads and is exce

</details>

### 388. ce-854 `cost`

A company is developing a SaaS solution for customers. The solution runs on Amazon EC2 instances that have Amazon Elastic Block Store (Amazon EBS) volumes attached. Within the SaaS application, customers can request how much storage they need. The application needs to allocate the amount of block storage each customer requests. A solutions architect must design an operationally efficient solution that meets the storage scaling requirement. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Invoke an AWS Lambda function to increase the size of EBS volumes based on user input by using EBS Elastic Volumes.**

The most operationally efficient and cost-effective solution is to use the existing Amazon EBS infrastructure and leverage the EBS Elastic Volumes feature. This feature allows for modifying the size, type, and IOPS of an EBS volume while it is attached to a running EC2 instance, without requiring downtime. An AWS Lambda function can be invoked by the SaaS application to programmatically call the ModifyVolume API action. This directly addresses the need to scale block storage based on customer requests, avoids a costly and complex data migration to a different storage type, and maintains the existing architecture. Why Incorrect Options are Wrong: A. Amazon S3 provides object storage, not the block storage required by the application running on EC2 instances. Migrating would require significant application re-architecture. B. Amazon EFS is a file storage service, not block storage. Further

</details>

### 389. ce-855 `least-ops`

A company needs to archive an on-premises relational database. The company wants to retain the dat a. The company needs to be able to run SQL queries on the archived data to create annual reports. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use AWS Database Migration Service (AWS DMS) to migrate the on-premises databases to Amazon S3 in Apache Parquet format. Store the data in S3 Glacier Flexible Retrieval. Use Amazon Athena to run reports.**

This solution provides the lowest operational overhead by leveraging serverless and managed services. AWS Database Migration Service (DMS) can migrate the on-premises data directly to Amazon S3 and convert it into an analytics-optimized format like Apache Parquet. Storing the data in S3 Glacier Flexible Retrieval provides low-cost archival storage suitable for infrequent access, such as annual reporting. When reports are needed, the data can be restored and queried directly from S3 using Amazon Athena, a serverless query engine. This avoids the need to provision, manage, patch, or maintain any database instances or servers, directly fulfilling the requirement for minimal operational overhead. Why Incorrect Options are Wrong: A. An Amazon RDS instance can only be stopped for a maximum of 7 days before it is automatically restarted. This is not a viable long-term archival solution for annu

</details>

### 390. ce-856

A company needs a data encryption solution for a machine learning (ML) process. The solution must use an AWS managed service. The ML process currently reads a large number of objects in Amazon S3 that are encrypted by a customer managed AWS KMS key. The current process incurs significant costs because of excessive calls to AWS Key Management Service (AWS KMS) to decrypt S3 objects. The company wants to reduce the costs of API calls to decrypt S3 objects.

<details><summary>Answer</summary>

**D. Use S3 Bucket Keys to perform server-side encryption with AWS KMS keys (SSE-KMS) to encrypt and decrypt objects from Amazon S3.**

The core issue is the high cost from numerous AWS KMS API calls made by Amazon S3 for decryption operations. S3 Bucket Keys are designed specifically to solve this problem. When enabled, S3 requests a short-lived bucket-level key from KMS. S3 then uses this bucket key to create data keys for individual objects within the bucket. This significantly reduces the request traffic from S3 to KMS because S3 no longer needs to make a decryption request to KMS for every single object. This directly addresses the requirement to reduce the costs of API calls while maintaining strong, AWS-managed encryption. Why Incorrect Options are Wrong: A. Switching from a customer managed key to an AWS managed key does not reduce the number of API calls. The per-request pricing for cryptographic operations is the same for both key types, so this would not solve the cost issue. B. A bucket policy is used to enfo

</details>

### 391. ce-864

A solutions architect needs to build a log storage solution for a client. The client has an application that produces user activity logs that track user API calls to the application. The application typically produces 50 GB of logs each day. The client needs a storage solution that makes the logs available for occasional querying and analytics.

<details><summary>Answer</summary>

**A. Store user activity logs in an Amazon S3 bucket. Use Amazon Athena to perform queries and analytics.**

This solution is the most cost-effective and scalable for the described use case. Amazon S3 provides durable, inexpensive, and virtually unlimited object storage, which is ideal for accumulating large volumes of log data (50 GB/day). Amazon Athena is a serverless query service that allows direct analysis of data in S3 using standard SQL. Since querying is "occasional," the pay-per-query model of Athena is significantly more economical than provisioning dedicated resources that run continuously. This architecture is a standard AWS pattern for building a serverless data lake for analytics. Why Incorrect Options are Wrong: B. Amazon OpenSearch Service is optimized for real-time, indexed searching and frequent analysis. Provisioning a cluster is more expensive and complex than necessary for "occasional" querying. C. Amazon RDS is a relational database (OLTP) and is not designed for storing o

</details>

### 392. ce-865

A company is developing a photo-hosting application in the us-east-1 Region. The application gives users across multiple countries the ability to upload and view photos. Some photos are heavily viewed for months, while other photos are viewed for less than a week. The application allows users to upload photos that are up to 20 MB in size. The application uses photo metadata to determine which photos to display to each user. The company needs a cost-effective storage solution to support the application.

<details><summary>Answer</summary>

**B. Store the photos in the Amazon S3 Intelligent-Tiering storage class. Store the photo metadata and the S3 location URLs in Amazon DynamoDB.**

This solution represents a well-architected pattern for media hosting applications. Amazon S3 is the ideal service for storing large binary objects like photos due to its durability, scalability, and low cost. The S3 Intelligent-Tiering storage class is specifically designed for data with unknown or changing access patterns, as described in the scenario. It automatically optimizes costs by moving objects between frequent and infrequent access tiers based on usage, without operational overhead. Amazon DynamoDB is a fully managed NoSQL database that provides fast, predictable, and scalable performance for storing and retrieving the photo metadata (e.g., user, date, tags) and the corresponding S3 location URL. This allows the application to quickly query for relevant photos without needing to scan the object storage itself. Why Incorrect Options are Wrong: A. Amazon DynamoDB has a maximum i

</details>

### 393. ce-871

A company that uses AWS Organizations runs 150 applications across 30 different AWS accounts. The company used AWS Cost and Usage Report to create a new report in the management account. The report is delivered to an Amazon S3 bucket that is replicated to a bucket in the data collection account. The company's senior leadership wants to view a custom dashboard that provides NAT gateway costs each day starting at the beginning of the current month. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Share an Amazon QuickSight dashboard that includes the requested table visual. Configure QuickSight to use Amazon Athena to query the new report.**

The most effective solution is to use Amazon Athena to query the AWS Cost and Usage Report (CUR) data stored in Amazon S3 and Amazon QuickSight to visualize the results. Amazon Athena is a serverless, interactive query service that makes it easy to analyze data in S3 using standard SQL. The CUR provides granular billing data, including costs for specific resources like NAT gateways. Amazon QuickSight is a business intelligence (BI) service that natively integrates with Athena, allowing for the creation of powerful, interactive dashboards suitable for senior leadership. This combination directly addresses the need to query detailed cost data and present it in a custom visual format. Why Incorrect Options are Wrong: A. AWS DataSync is a data migration and transfer service used to move data between storage systems; it is not a query engine and cannot be used to query reports. C. Amazon Clou

</details>

### 394. ce-873

A media company stores customer-uploaded videos in an Amazon S3 bucket with the Standard storage class. The company wants to create an S3 Lifecycle configuration. The company will set the maximum retention time to 7 days. However, the configuration must delete any video that is more than 1 TB in size after 48 hours.

<details><summary>Answer</summary>

**A. Create a single S3 Lifecycle configuration that has two rules. Configure the first rule to expire objects after 48 hours with a filter of ObjectSizeGreaterThan and a value of 1 TB. Configure the second rule to expire objects after 7 days.**

An Amazon S3 bucket can have only one lifecycle configuration, which can contain up to 1,000 rules. To meet the requirements, a single configuration with two rules is necessary. The first rule must use a filter to target a specific subset of objects-in this case, videos larger than 1 TB. The ObjectSizeGreaterThan filter is the correct mechanism for this, triggering an expiration action after 48 hours. The second rule can be configured without a filter to apply to all objects in the bucket, setting a maximum retention of 7 days. For objects that match both rules (those 1 TB), S3 will apply the action with the shorter time period, effectively expiring them after 48 hours as required. Why Incorrect Options are Wrong: B: An S3 bucket can only have one lifecycle configuration, not two. Additionally, a Prefix filter targets objects based on their name, not their size, which is incorrect for th

</details>

### 395. ce-877

A company is storing data that will not be frequently accessed in the AWS Cloud. If the company needs to access the data, the data must be retrieved within 12 hours. The company wants a solution that is cost-effective for storage costs per gigabyte. Which Amazon S3 storage class will meet these requirements?

<details><summary>Answer</summary>

**B. S3 Glacier Flexible Retrieval**

The requirements are for storing infrequently accessed data, ensuring retrieval within 12 hours, and prioritizing cost-effectiveness for storage. Amazon S3 Glacier Flexible Retrieval is designed for long-term archival data that is accessed infrequently. It offers the lowest storage cost among the given options. Its retrieval options include Standard (3-5 hours) and Bulk (5-12 hours), both of which meet the sub-12-hour retrieval requirement. This combination of very low storage cost and acceptable retrieval time makes it the optimal choice for this scenario. Why Incorrect Options are Wrong: A. S3 Standard is designed for frequently accessed data and has the highest storage cost, making it unsuitable and not cost-effective for this use case. C. S3 One Zone-Infrequent Access (S3 One Zone-IA) has a higher storage cost than S3 Glacier and is designed for data that can be easily recreated. D.

</details>

### 396. ce-897 `cost`

A company wants to use Amazon S3 to back up its on-premises file storage solution. The company's on-premises file storage solution uses NFS, and the company wants its new solution to support NFS. The company wants to archive the backup files after 5 days. If the company needs archived files for disaster recovery, the company is willing to wait a few days for the retrieval of those files. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Deploy an AWS Storage Gateway file gateway that is associated with an S3 bucket. Move the files from the on-premises file storage solution to the file gateway. Create an S3 Lifecycle rule to move the files to S3 Glacier Deep Archive after 5 days.**

The solution requires an on-premises NFS interface for a backup solution that archives to Amazon S3. AWS Storage Gateway's File Gateway provides a file interface using the NFS protocol, allowing it to be mounted as a network file share. This directly meets the protocol requirement. For the most cost-effective archival, an S3 Lifecycle policy should transition the files to the lowest-cost storage class that meets the retrieval requirements. The company is willing to wait a few days for retrieval. S3 Glacier Deep Archive is the lowest-cost S3 storage class, designed for long-term data archiving where retrieval times of 12-48 hours are acceptable, making it the most cost-effective choice for this scenario. Why Incorrect Options are Wrong: A. S3 Standard-IA is not the most cost-effective storage class for long-term archival when retrieval times of several hours or days are acceptable. B. A V

</details>

### 397. ce-902 `least-ops`

A solutions architect needs to optimize storage costs. The solutions architect must identify any Amazon S3 buckets that are no longer being accessed or are rarely accessed. Which solution will accomplish this goal with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Analyze bucket access patterns by using the S3 Storage Lens dashboard for advanced activity metrics.**

The goal is to identify rarely accessed S3 buckets with the least operational overhead. Amazon S3 Storage Lens is a purpose-built feature that provides organization-wide visibility into object storage usage and activity trends. It offers interactive dashboards with metrics on data access patterns, allowing an architect to easily identify cold or inactive data across many buckets without any complex setup. This is the most efficient and least operationally intensive method for achieving the stated goal. Why Incorrect Options are Wrong: B. The standard S3 dashboard in the console provides high-level summaries like total storage but lacks the detailed access pattern metrics needed for this analysis. C. This is a complex, manual solution requiring configuration of metrics, data pipelines, and query services like Athena, which is high operational overhead. D. Enabling CloudTrail data events f

</details>

### 398. ce-903 `cost`

A company is building a containerized application on AWS. The application uses the Linux operating system. The company needs to provide a persistent storage solution for the application. The company expects the storage solution to have varying data access patterns. The solution must have native storage tiering capabilities and must be scalable. The solution must not require the company to provision storage upfront. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**B. Use an Amazon EFS file system in Elastic throughput mode. Use the Intelligent Tiering lifecycle management feature.**

Amazon EFS is a fully managed, scalable file storage service for Linux-based workloads. It meets the requirements perfectly: it scales storage automatically without upfront provisioning. The "Elastic" throughput mode automatically scales performance based on workload. The "Intelligent-Tiering" lifecycle management feature addresses varying data access patterns and cost-effectiveness by automatically moving infrequently accessed files to a lower-cost storage class. This combination provides a scalable, persistent, and cost-optimized solution for containerized applications. Why Incorrect Options are Wrong: A. Amazon FSx for NetApp ONTAP is a powerful solution but is generally more complex and may not be the most cost-effective option for this use case compared to EFS. C. Amazon FSx for Windows File Server is designed for Windows, not the Linux operating system specified in the requirement,

</details>

### 399. ce-904 `cost` `availability`

A company is building an application that runs on several Linux-based containers in Amazon ECS. The containers must have shared access to log files and configuration dat a. The application requires a POSIX-compliant file system that provides high availability and scalability. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**A. Configure an Amazon EFS file system with elastic throughput.**

The scenario requires a POSIX-compliant, highly available, and scalable shared file system for containers running on Amazon ECS. Amazon Elastic File System (EFS) is a fully managed NFS file system designed for this exact use case. It provides shared access for thousands of concurrent clients, including ECS tasks, and scales automatically. It is the most cost-effective solution that meets all the specified requirements for shared configuration and log files, which typically do not require the extreme performance of more expensive options. Why Incorrect Options are Wrong: B. Amazon S3 is an object store, not a POSIX-compliant file system. It does not provide the native file system semantics required for shared log and configuration files. C. Amazon FSx for Lustre is a high-performance file system for HPC workloads. It is overkill and not the most cost-effective choice for sharing log and c

</details>

### 400. ce-906 `cost`

A company wants to use Amazon S3 to back up its on-premises file storage solution. The company's on-premises file storage solution supports NFS, and the company wants its new solution to support NFS. The company wants to archive the backup files after 5 days. If the company needs archived files for disaster recovery, the company is willing to wait a few days for the retrieval of those files. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Deploy an AWS Storage Gateway file gateway that is associated with an S3 bucket. Move the files from the on-premises file storage solution to the file gateway. Create an S3 Lifecycle rule to move the files to S3 Glacier Deep Archive after 5 days.**

The solution requires an NFS interface for the on-premises backup and cost-effective archiving where retrieval can take days. The AWS Storage Gateway File Gateway provides a file interface (NFS/SMB) that stores data in an associated S3 bucket. This meets the NFS requirement. To meet the archiving and cost requirements, an S3 Lifecycle policy should be configured to transition objects to S3 Glacier Deep Archive after 5 days. This is the lowest-cost S3 storage class, and its retrieval time of 12+ hours aligns with the "willing to wait a few days" requirement. Why Incorrect Options are Wrong: A. S3 Standard-IA is not the most cost-effective archival storage class when retrieval can take days; S3 Glacier Deep Archive is significantly cheaper for long-term storage. B. A Volume Gateway provides block storage via iSCSI, not the required NFS file interface. S3 Glacier Deep Archive is correct, bu

</details>

### 401. ce-908 `cost`

A company stores 5 PB of archived data on physical tapes in an on-premises data center. The company needs to retain the data for 10 years. The company does not want to change an existing backup workflow. The data center that stores the tapes has a 10 Gbps AWS Direct Connect connection to an AWS Region. The company wants to migrate the data to AWS as soon as possible. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**D. Configure an on-premises AWS Storage Gateway Tape Gateway. Create virtual tapes on AWS. Use backup software to copy the physical tapes to the virtual tapes. Move the virtual tapes to Amazon S3 Glacier Deep Archive storage.**

The key requirement is to migrate tape-based backups without changing the existing backup workflow. AWS Storage Gateway's Tape Gateway is specifically designed for this purpose. It presents a virtual tape library (VTL) to the on-premises backup application, which continues to operate as it always has. The Tape Gateway then handles the transfer of these virtual tapes to AWS, where they can be cost-effectively archived in Amazon S3 Glacier Deep Archive for long-term retention. This solution directly meets the primary requirements with minimal disruption. Why Incorrect Options are Wrong: A. Using AWS DataSync would require changing the workflow to read from a file system, not tapes, and involves a complex staging process. B. Writing directly to S3 Glacier Deep Archive requires the backup application to have native S3 integration, which constitutes a change to the existing workflow. C. Using

</details>

### 402. ce-909 `cost`

A company stores medical reports and images in Amazon S3 Standard storage. The company accesses each medical report only once each year. However, the company must be able to access the medical reports in real time when necessary. The company rarely accesses the medical images, but the company must retain each image for 7 years. The company can tolerate flexible retrieval times for the medical images. The company wants to optimize storage costs for the medical reports and images. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**B. Store the medical reports in S3 Glacier Instant Retrieval. Store the medical images in S3 Glacier Deep Archive.**

The solution requires optimizing storage costs based on specific access patterns. For medical reports accessed infrequently (once a year) but needing real-time (millisecond) retrieval, S3 Glacier Instant Retrieval is the most cost-effective choice. It offers the low storage costs of archival storage with the fast retrieval performance of standard storage tiers. For medical images that are rarely accessed, have a 7-year retention requirement, and can tolerate flexible retrieval times (hours), S3 Glacier Deep Archive is the ideal choice as it is the lowest-cost storage class in AWS. This combination precisely matches the requirements for each data type, maximizing cost savings. Why Incorrect Options are Wrong: A. S3 Glacier Deep Archive does not provide the real-time access required for the medical reports. C. S3 Intelligent-Tiering is for unknown or changing access patterns; here, the pat

</details>

### 403. ce-913 `cost`

A company runs a web application that stores user-generated images. The application currently stores 500 GB of images. The average file size of the images is 2 MB. The company expects the total amount of images to grow to 2 TB within 6 months. The application needs to serve all stored images with low latency to users from around the world. Which storage solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Store images in an Amazon S3 bucket. Integrate the S3 bucket with Amazon CloudFront. Integrate the web application with a CloudFront endpoint to provide global access.**

This solution is the standard, most cost-effective, and scalable architecture for serving static web content globally. Amazon S3 provides durable, inexpensive, and highly scalable object storage for the images. Integrating S3 with Amazon CloudFront, a global Content Delivery Network (CDN), caches the images at edge locations worldwide. When users request an image, it is served from the nearest edge location, significantly reducing latency. This combination scales automatically to handle traffic spikes and is priced on a pay-as-you-go basis, making it highly cost-effective for a growing application. Why Incorrect Options are Wrong: A. Amazon EBS is block storage for EC2 instances. It is not designed for direct web serving of objects and is more expensive and less scalable than S3 for this use case. C. Amazon EFS is a shared file storage service. It is significantly more expensive than S3

</details>

### 404. ce-928 `cost`

A company hosts a photo sharing web application on AWS. Users upload and share thousands of photos each hour. The company needs a durable storage solution that provides retrieval mechanisms for the photos. Most uploaded photos are not accessed often after 30 days, but the company does not want to delete older photos. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**B. Store the photos in an Amazon S3 bucket. Use Amazon S3 Lifecycle configurations to move photos that are older than 30 days to S3 Intelligent-Tiering.**

The most cost-effective and durable solution is to use Amazon S3 for storing photos. S3 is designed for high durability and scalability for object storage. An S3 Lifecycle configuration can automatically transition objects to more cost-effective storage classes based on their age. Using S3 Intelligent-Tiering is ideal for data with unknown or changing access patterns, as it automatically moves data to the most cost-effective access tier without performance impact or operational overhead. This directly addresses the requirement for photos that are not accessed often after 30 days, optimizing storage costs while keeping the photos retrievable. Why Incorrect Options are Wrong: A. Amazon EFS is a file storage service and is significantly more expensive than Amazon S3 for storing large amounts of infrequently accessed data. C. Amazon DynamoDB is a NoSQL database, not designed for storing larg

</details>

### 405. ce-935 `cost` `availability`

A company is migrating a document management application to AWS. The application runs on Linux servers. The company will migrate the application to Amazon EC2 instances in an Auto Scaling group. The company stores 7 TiB of documents in a shared storage file system. An external relational database tracks the documents. Documents are stored once and can be retrieved multiple times for reference at any time. The company cannot modify the application during the migration. The storage solution must be highly available and must support scaling over time. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Create an Amazon EFS file system with mount points in multiple Availability Zones. Use the EFS Standard-Infrequent Access (Standard-IA) storage class. Mount the NFS share on the EC2 instances in the Auto Scaling group.**

The scenario requires a highly available, scalable, and cost-effective shared file system for Linux-based EC2 instances without application modification. Amazon EFS is a fully managed NFS file system that is inherently highly available and scalable. It allows concurrent connections from thousands of EC2 instances. Using mount points in multiple Availability Zones ensures high availability. The EFS Standard-Infrequent Access (Standard-IA) storage class, combined with EFS Lifecycle Management, automatically moves infrequently accessed files to a lower-cost tier, meeting the cost-effectiveness requirement for the 7 TiB of documents that are stored once and retrieved multiple times. Why Incorrect Options are Wrong: A. A single EC2 instance acting as an NFS server is a single point of failure and is not a highly available solution as required. B. Amazon S3 is an object store, not a POSIX-comp

</details>

### 406. ce-936 `cost`

A company wants to migrate an application that processes logs to AWS. Currently, the application runs on an on-premises storage area network (SAN). The application reads and processes large log files sequentially. The application requires throughput of up to 500 MBps. A solutions architect needs to migrate the application with minimal change to the application architecture. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**B. Use a Throughput Optimized HDD (st1) Amazon EBS volume with provisioned storage based on the throughput requirement.**

The workload involves processing large log files sequentially, which is a throughput-intensive task with large, sequential I/O operations. Throughput Optimized HDD (st1) volumes are specifically designed for this use case. They provide high throughput at the lowest price point for frequently accessed, streaming workloads. An st1 volume can deliver up to 500 MBps of throughput, meeting the performance requirement. Given that the application architecture should have minimal changes (implying a block storage solution is preferred) and cost-effectiveness is key, st1 is the ideal choice over more expensive SSD-based options. Why Incorrect Options are Wrong: A. A General Purpose SSD (gp3) volume would work but is optimized for a mix of IOPS and throughput and would be more expensive than st1 for a purely throughput-bound workload. C. A Cold HDD (sc1) volume has a maximum throughput of 250 MBps

</details>

### 407. ce-937 `least-ops`

A video production company stores raw 4K video footage on an Amazon EFS file system by using the EFS Standard storage class. Each video file is around 100 GB. The EFS file system is mounted to an Auto Scaling group of Amazon EC2 instances that transcode the video files. Editors need to access each file frequently for up to 90 days. After 90 days, the files are rarely needed. However, the files must remain available with sub-second latency for on-demand edit requests. The company wants to reduce monthly storage costs without any changes to the existing mount points that the editors use. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Apply the Transition into IA lifecycle policy to the file system. Configure the policy to move the files that have not been accessed for 90 days.**

Amazon EFS lifecycle management automates the process of moving files that have not been accessed for a specific period to a lower-cost storage class, EFS Infrequent Access (IA). This meets the requirements perfectly: it reduces storage costs, the transition is transparent to users and applications (no change to mount points or file paths), and EFS IA still provides the required sub-second latency. Configuring a lifecycle policy is a one-time setup, representing the least operational overhead. Why Incorrect Options are Wrong: B. Migrating to S3 with File Gateway changes the entire architecture and access pattern, adding significant operational overhead for editors. C. Exporting to S3 and using S3 Glacier Instant Retrieval is complex, changes the access method, and requires a non-standard re-mount process, which is high operational overhead. D. A custom Lambda function for compression add

</details>

### 408. ce-945 `cost`

A company runs a non-production Oracle database on an Amazon EC2 instance. The database contains 1 TB of data. The EC2 instance runs in a private subnet of a VPC. A backup of the EC2 instance is taken every day and uploaded to an Amazon S3 bucket. The current backup process uses a NAT gateway to access the S3 bucket. The company does not want the backup process to use public IP addresses. Which solution will meet this requirement MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create a gateway endpoint for Amazon S3 in the VPC. Update the route tables.**

A VPC gateway endpoint for Amazon S3 provides a private, secure connection between a VPC and S3, keeping all traffic within the AWS network. By creating a gateway endpoint and updating the private subnet's route table to direct S3-bound traffic to it, the EC2 instance can access the S3 bucket without needing a NAT gateway or public IP addresses. This directly fulfills the core requirement. Furthermore, there are no data processing or hourly charges for using gateway endpoints, making this the most cost-effective solution as it eliminates the costs associated with the NAT gateway for this traffic. Why Incorrect Options are Wrong: B. S3 Transfer Acceleration is designed to speed up uploads over the public internet using AWS edge locations; it does not provide private connectivity. C. Amazon CloudFront is a content delivery network (CDN) for distributing content, not a solution for private

</details>

### 409. ce-951 `least-ops`

A company has an on-premises application that uses SFTP to collect financial data from multiple vendors. The company is migrating to the AWS Cloud. The company has created an application that uses Amazon S3 APIs to upload files from vendors. Some vendors run their systems on legacy applications that do not support S3 APIs. The vendors want to continue to use SFTP-based applications to upload dat a. The company wants to use managed services for the needs of the vendors that use legacy applications. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an AWS Transfer Family endpoint for vendors that use legacy applications.**

AWS Transfer Family is a fully managed service designed specifically for this use case. It provides a secure SFTP (as well as FTPS and FTP) endpoint that allows external parties, like the vendors, to upload files directly into an Amazon S3 bucket. This solution meets the requirement of using a managed service, which minimizes operational overhead as AWS handles the underlying infrastructure, scaling, and maintenance. The vendors can continue using their existing SFTP clients and workflows without any changes, while the company's new application can process the files directly from Amazon S3. Why Incorrect Options are Wrong: A. AWS Database Migration Service (AWS DMS) is used for migrating databases, not for handling file transfers via SFTP. It is the incorrect service for this scenario. C. Configuring an SFTP server on an Amazon EC2 instance would work, but it is not a managed service. Th

</details>

### 410. ce-954

A company is redesigning its data intake process. In the existing process, the company receives data transfers and uploads the data to an Amazon S3 bucket every night. The company uses AWS Glue crawlers and jobs to prepare the data for a machine learning (ML) workflow. The company needs a low-code solution to run multiple AWS Glue jobs in sequence and provide a visual workflow. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon EventBridge to call an AWS Step Functions workflow for the AWS Glue jobs. Use Step Functions to create a visual workflow.**

The solution requires a low-code method to run multiple AWS Glue jobs sequentially and provide a visual representation of the workflow. AWS Step Functions is a serverless, low-code, visual workflow service that is ideal for orchestrating multi-step processes. It allows you to build state machines that coordinate components like AWS Glue jobs and AWS Lambda functions. The Step Functions console provides a built-in graphical representation of the workflow's logic and its real-time execution status. Amazon EventBridge can be used to detect the nightly data upload to Amazon S3 and automatically trigger the Step Functions workflow, creating a fully automated and observable data pipeline. Why Incorrect Options are Wrong: A. This is not a low-code solution as it requires custom scripting on an EC2 instance. A CloudWatch dashboard shows metrics, but it does not provide a visual representation of

</details>

### 411. ce-961 `cost`

A company is building a new web application that serves static and dynamic content from an API. Users will access the application from around the world. The company wants to minimize latency in the most cost-effective way. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Deploy the static content to an Amazon S3 bucket. Use an Amazon API Gateway HTTP API to serve the dynamic content. Create an Amazon CloudFront distribution that uses the S3 bucket and the HTTP API as origins. Enable caching for static content.**

This solution provides a globally distributed, low-latency, and highly cost-effective architecture. Amazon CloudFront serves as the single entry point, caching static content from an Amazon S3 origin at edge locations close to users, which significantly reduces latency. For dynamic content, CloudFront forwards requests to the Amazon API Gateway HTTP API origin. This leverages the AWS global network to accelerate the connection to the API. The use of serverless services-S3 for storage, API Gateway for compute, and CloudFront for delivery-ensures a pay-per-use model with no idle infrastructure costs, making it the most cost-effective option. Why Incorrect Options are Wrong: B. This option fails to use CloudFront for static content, leading to high latency for users who are geographically distant from the S3 bucket's region. C. Using EC2 instances and an Application Load Balancer is less co

</details>

### 412. ce-963 `least-ops`

A company wants to migrate an on-premises video processing application to AWS. Processing times range from 5-30 minutes. The application must run multiple jobs in parallel. The application processes videos that users upload to an Amazon S3 bucket. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure the S3 bucket to send S3 event notifications to an Amazon SQS standard queue. Deploy the application on an Amazon ECS cluster. Configure automatic scaling for AWS Fargate tasks based on the SQS queue size.**

This solution effectively decouples the video upload from the processing, allowing for parallel and resilient job handling. Amazon SQS standard queues are ideal for high-throughput, asynchronous workloads. AWS Fargate provides serverless compute for containers, which eliminates the operational overhead of managing EC2 instances (OS patching, scaling). The application can run for the required 30 minutes. Configuring Fargate auto-scaling based on the SQS queue size (e.g., ApproximateNumberOfMessagesVisible) ensures that processing capacity scales with demand, meeting all requirements with minimal management. Why Incorrect Options are Wrong: B. SQS FIFO queues limit parallelism by design, which contradicts the requirement to run multiple jobs in parallel. EC2 instances also have higher operational overhead than Fargate. C. AWS Lambda has a maximum execution timeout of 15 minutes, which is i

</details>
