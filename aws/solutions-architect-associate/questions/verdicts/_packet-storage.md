# Flagged questions to adjudicate: storage

12 questions. For each: establish the truth, then decide keep / fix / drop.


---

## gh-205  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: Private S3 bucket with a bucket policy allowing a CloudFront origin access identity (OAI). Now: Origin Access Control (OAC) replaced OAI in August 2022 and is what AWS recommends for S3 origins; OAI is documented as legacy and does not support SSE-KMS, dynamic requests, or all Regions. The shape of the answer (private bucket, CloudFront-only access) is still right, but the mechanism

**Question:**

A company hosts a marketing website in an on-premises data center. The website consists of static documents and runs on a single server. An administrator updates the website content infrequently and uses an SFTP client to upload new documents.
The company decides to host its website on AWS and to use Amazon CloudFront. The company’s solutions architect creates a CloudFront distribution. The solutions architect must design the most cost-effective and resilient architecture for website hosting to serve as the CloudFront origin.
Which solution will meet these requirements?

**Stated answer:** C. Create a private Amazon S3 bucket. Use an S3 bucket policy to allow access from a CloudFront origin access identity (OAI). Upload website content by using the AWS CLI.

**Stated explanation:** This option leverages Amazon S3 as the origin for CloudFront. By creating a private S3 bucket and using a bucket policy to allow access from a CloudFront origin access identity (OAI), you ensure that the content is served securely from S3 and that only CloudFront can access the bucket.


---

## gh-22  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation states that S3 Intelligent-Tiering "can store objects in two access tiers: the frequent access tier and the infrequent access tier". Since November 2021 the automatic tiers are Frequent Access, Infrequent Access and Archive Instant Access, with optional Archive Access and Deep Archive Access tiers on top. The answer is right; the tier description is out of date, and the same

**Question:**

A solutions architect is using Amazon S3 to design the storage architecture of a new digital media application. The media files must be resilient to the loss of an Availability Zone. Some files are accessed frequently while other files are rarely accessed in an unpredictable pattern. The solutions architect must minimize the costs of storing and retrieving the media files.
Which storage option meets these requirements?

**Stated answer:** B. S3 Intelligent-Tiering

**Stated explanation:** Amazon S3 Intelligent Tiering is a storage class that automatically moves data to the most cost-effective storage tier based on access patterns. It can store objects in two access tiers: the frequent access tier and the infrequent access tier. The frequent access tier is optimized for frequently accessed objects and is charged at the same rate as S3 Standard. The infrequent access tier is optimized for objects that are not accessed frequently and are charged at a lower rate than S3 Standard.

S3 Intelligent Tiering is a good choice for storing media files that are accessed frequently and infrequently in an unpredictable pattern because it automatically moves data to the most cost-effective storage tier based on access patterns, minimizing storage and retrieval costs. It is also resilient to the loss of an Availability Zone because it stores objects in multiple Availability Zones within a


---

## gh-302  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: CloudFront for delivery plus Amazon Elastic Transcoder to convert the video files. Now: Amazon Elastic Transcoder is retired — AWS stopped accepting new customers in 2024 and the service reached end of support on 13 November 2025. The current service for this job is AWS Elemental MediaConvert.

**Question:**

A company wants to create a mobile app that allows users to stream slow-motion video clips on their mobile devices. Currently, the app captures video clips and uploads the video clips in raw format into an Amazon S3 bucket. The app retrieves these video clips directly from the S3 bucket. However, the videos are large in their raw format.
Users are experiencing issues with buffering and playback on mobile devices. The company wants to implement solutions to maximize the performance and scalability of the app while minimizing operational overhead.
Which combination of solutions will meet these requirements? (Choose two.)

**Stated answer:** A. Deploy Amazon CloudFront for content delivery and caching.

**Stated explanation:** C. Use Amazon Elastic Transcoder to convert the video files to more appropriate formats.

Amazon CloudFront is a content delivery network (CDN) that can distribute your video content globally, reducing latency and improving the speed of delivery.
CloudFront can cache the video content at edge locations, which helps in minimizing the load on the S3 bucket and improves playback performance for users.

Amazon Elastic Transcoder can convert the raw video files into more appropriate formats suitable for streaming, reducing the size of the videos.
By using Elastic Transcoder, you can create different versions of the video files optimized for different devices, bitrates, and resolutions, which can significantly improve the playback experience on mobile devices


---

## gh-44  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation says MFA Delete "requires you to enter a one-time password from a multi-factor authentication (MFA) device before you can delete an object". That is not how it works. In a versioned bucket a plain DELETE just writes a delete marker and needs no MFA; MFA is required only to permanently delete a specific object version or to change the bucket's versioning state. The same incor

**Question:**

A company has an Amazon S3 bucket that contains critical data. The company must protect the data from accidental deletion.
Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

**Stated answer:** A. Enable versioning on the S3 bucket

**Stated explanation:** B. Enable MFA Delete on the S3 bucket

The two most effective steps a solutions architect can take to protect an Amazon S3 bucket from accidental deletion are:

A. Enable versioning on the S3 bucket.
B. Enable MFA Delete on the S3 bucket.

Versioning keeps multiple versions of objects in the S3 bucket, even when they are overwritten or deleted. This allows you to recover objects that have been accidentally deleted.

MFA Delete requires you to enter a one-time password from a multi-factor authentication (MFA) device before you can delete an object in the S3 bucket. This helps to prevent accidental deletions.


---

## gh-46  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation has nothing to do with the question or the answer — it is boilerplate text about requesting service quota increases through the Service Quotas console. There is no justification given for using S3 as a transfer point with Macie scanning and SNS alerting.

**Question:**

A company has an application that provides marketing services to stores. The services are based on previous purchases by store customers. The stores upload transaction data to the company through SFTP, and the data is processed and analyzed to generate new marketing offers. Some of the files can exceed 200 GB in size.
Recently, the company discovered that some of the stores have uploaded files that contain personally identifiable information (PII) that should not have been included. The company wants administrators to be alerted if PII is shared again. The company also wants to automate remediation.
What should a solutions architect do to meet these requirements with the LEAST development effort?

**Stated answer:** B. Use an Amazon S3 bucket as a secure transfer point. Use Amazon Macie to scan the objects in the bucket. If objects contain PII, use Amazon Simple Notification Service (Amazon SNS) to trigger a notification to the administrators to remove the objects that contain PII.

**Stated explanation:** Some quotas can be increased, while others cannot. To request an increase to a quota, use the Service Quotas console. To learn how to request an increase, see Requesting a quota increase in the Service Quotas User Guide. If a quota isn't available on the Service Quotas console, use the service limit increase form on the AWS Support Center Console to request an increase to the quota.


---

## gh-49  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: S3 Intelligent-Tiering, lifecycle to S3 Glacier Flexible Retrieval after 1 year, Athena for recent files, S3 Glacier Select for archived files. Now: S3 Glacier Select (and S3 Select) is no longer available to new customers as of mid-2024; existing users were grandfathered. The storage-class part of the answer is still the best of the options, but the retrieval mechanism named has be

**Question:**

A company stores call transcript files on a monthly basis. Users access the files randomly within 1 year of the call, but users access the files infrequently after 1 year. The company wants to optimize its solution by giving users the ability to query and retrieve files that are less than 1-year-old as quickly as possible. A delay in retrieving older files is acceptable.
Which solution will meet these requirements MOST cost-effectively?

**Stated answer:** B. Store individual files in Amazon S3 Intelligent-Tiering. Use S3 Lifecycle policies to move the files to S3 Glacier Flexible Retrieval after 1 year. Query and retrieve the files that are in Amazon S3 by using Amazon Athena. Query and retrieve the files that are in S3 Glacier by using S3 Glacier Select.

**Stated explanation:** S3 Intelligent-Tiering is the ideal storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. You can use S3 Intelligent-Tiering as the default storage class for virtually any workload, especially data lakes, data analytics, new applications, and user-generated content.


---

## gh-501  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: Amazon Kinesis Data Firehose to ingest, Amazon Kinesis Data Analytics to analyse in real time. Now: Both services have been renamed. Kinesis Data Analytics became Amazon Managed Service for Apache Flink in August 2023, and Kinesis Data Firehose became Amazon Data Firehose in February 2024. The architecture is still correct; only the names are stale. The old Firehose name also appear

**Question:**

A company wants to ingest customer payment data into the company's data lake in Amazon S3. The company receives payment data every minute on average. The company wants to analyze the payment data in real time. Then the company wants to ingest the data into the data lake.
Which solution will meet these requirements with the MOST operational efficiency?

**Stated answer:** C. Use Amazon Kinesis Data Firehose to ingest data. Use Amazon Kinesis Data Analytics to analyze the data in real time.

**Stated explanation:** Amazon Kinesis Data Firehose:

It is a fully managed service that can reliably load streaming data into data lakes, data stores, and analytics tools.
It can automatically scale to handle varying data throughput.
It simplifies the data delivery process, making it easy to ingest data into Amazon S3.

Amazon Kinesis Data Analytics:

It enables you to analyze streaming data in real-time with SQL queries.
It integrates seamlessly with other AWS services, including Kinesis Data Firehose.
It provides the capability to perform real-time analytics on the streaming data before storing it in Amazon S3.


---

## gh-517  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation argues against the stated answer. It says Systems Manager S3 logging "is primarily for storing the output of commands... not specifically for Session Manager logs" and "may not capture all the detailed session logs", which would rule out the option the answer picks. It is also wrong: Session Manager has a built-in S3 logging preference that writes full session output to a ch

**Question:**

A company wants to send all AWS Systems Manager Session Manager logs to an Amazon S3 bucket for archival purposes.
Which solution will meet this requirement with the MOST operational efficiency?

**Stated answer:** A. Enable S3 logging in the Systems Manager console. Choose an S3 bucket to send the session data to.

**Stated explanation:** While AWS Systems Manager supports logging command output to an S3 bucket, this is primarily for storing the output of commands executed through Systems Manager, not specifically for Session Manager logs.
It may not capture all the detailed session logs, including interactive session input/output and other session-specific details.


---

## gh-534  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: Transition to S3 Standard-IA after 30 days, move all objects to S3 Glacier Flexible Retrieval after 90 days, and expire objects after 90 days. Should be: The option that transitions to an infrequent-access class at day 30 and expires objects at day 90, with no Glacier step. Since high availability is only required for the first 30 days and the remaining 60 days are backup only, S3 O

**Question:**

A company wants to build a logging solution for its multiple AWS accounts. The company currently stores the logs from all accounts in a centralized account. The company has created an Amazon S3 bucket in the centralized account to store the VPC flow logs and AWS CloudTrail logs. All logs must be highly available for 30 days for frequent analysis, retained for an additional 60 days for backup purposes, and deleted 90 days after creation.
Which solution will meet these requirements MOST cost-effectively?

**Stated answer:** B. Transition objects to the S3 Standard-Infrequent Access (S3 Standard-IA) storage class 30 days after creation. Move all objects to the S3 Glacier Flexible Retrieval storage class after 90 days. Write an expiration action that directs Amazon S3 to delete objects after 90 days.

**Stated explanation:** (none)


---

## gh-651  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation ends with a stray block answering a completely different question — "Answer: C) Configure the General Purpose SSD (gp3) EBS volume storage type and provision 15,000 IOPS", with notes about gp2 and magnetic volumes. It appears to be copy-paste contamination from an EBS question and has no bearing on the S3 lifecycle answer above it.

**Question:**

A company stores a large volume of image files in an Amazon S3 bucket. The images need to be readily available for the first 180 days. The images are infrequently accessed for the next 180 days. After 360 days, the images need to be archived but must be available instantly upon request. After 5 years, only auditors can access the images. The auditors must be able to retrieve the images within 12 hours. The images cannot be lost during this process.

**Stated answer:** C. Transition the objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 180 days, S3 Glacier Instant Retrieval after 360 days, and S3 Glacier Deep Archive after 5 years.

**Stated explanation:** Explanation:
S3 Standard-IA (instead of One Zone-IA) ensures high durability across multiple AZs for infrequent access.
Glacier Instant Retrieval meets the "instant availability" requirement after 360 days, while Glacier Deep Archive is cost-effective for audits after 5 years.
(Option A/B use less durable One Zone-IA, and Option D uses slower Glacier Flexible Retrieval, which violates the "instant" requirement.)

Answer: C) Configure the General Purpose SSD (gp3) EBS volume storage type and provision 15,000 IOPS.
gp3 allows independent provisioning of IOPS (unlike gp2) and is more cost-effective than io1 for 15,000 IOPS.
Magnetic volumes (Option D) are outdated and cannot meet the performance requirement.


---

## gh-667  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: Create S3 gateway endpoints, with the note "Interface endpoints are for private-link services, not S3." Should be: Create interface endpoints (AWS PrivateLink) for Amazon S3. Why: A gateway endpoint is only reachable from inside the VPC that holds the route-table entry — it cannot be used from an on-premises network over Direct Connect or VPN. Amazon S3 has supported interface endpo

**Question:**

A company is moving its data and applications to AWS during a multiyear migration project. The company wants to securely access data on
Amazon S3 from the company's AWS Region and from the company's on-premises location. The data must not traverse the internet. The company
has established an AWS Direct Connect connection between its Region and its on-premises location.
Which solution will meet these requirements?

**Stated answer:** Answer: A) Create S3 gateway endpoints.

**Stated explanation:** Gateway endpoints allow secure S3 access via Direct Connect/VPC without internet.
Interface endpoints (Option C) are for private-link services, not S3.


---

## wl-8  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: Launch an unencrypted EC2 instance, snapshot the root volume, then copy the snapshot with encryption — because "when launching an EC2 instance, the EBS volume for root cannot be encrypted." Now: That restriction was removed in February 2019. You can turn on "EBS encryption by default" for an account in a Region, or set `Encrypted: true` (with a KMS key) on the root device in the lau

**Question:**

You are planning to build a fleet of EBS-optimized EC2 instances for your new application. Due to security compliance, your organization wants you to encrypt root volume which is used to boot the instances. How can this be achieved?

**Options given by the source:**

- A. Select the Encryption option for the root EBS volume while launching the EC2
- B. Once the EC2 instances are launched, encrypt the root volume using AWS KMS
- C. Root volumes cannot be encrypted. Add another EBS volume with an encryption
- D. Launch an unencrypted EC2 instance and create a snapshot of the root volume.

**Stated answer:** D. Launch an unencrypted EC2 instance and create a snapshot of the root volume.

**Stated explanation:** When launching an EC2 instance, the EBS volume for root cannot be encrypted.
You can launch the instance with unencrypted root volume and create a snapshot of
the root volume. Once the snapshot is created, you can copy the snapshot where you
can make the new snapshot encrypted.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html#AMI
Encryption
