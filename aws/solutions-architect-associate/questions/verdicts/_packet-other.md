# Flagged questions to adjudicate: other

7 questions. For each: establish the truth, then decide keep / fix / drop.


---

## gh-201  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: B. Build an Amazon Pinpoint journey. Configure Amazon Pinpoint to send events to an Amazon Kinesis data stream for analysis and archiving. Now: This was the accepted answer when the question was written, and streaming Pinpoint events into Kinesis so they can be retained and analysed is still the right *shape* of solution. But the product has been split and renamed: the SMS, voice an

**Question:**

A company is developing a marketing communications service that targets mobile app users. The company needs to send its users confirmation messages with Short Message Service (SMS). The users must be able to reply to the SMS messages. The company must store the responses for a year for analysis.
What should a solutions architect do to meet these requirements?

**Stated answer:** B. Build an Amazon Pinpoint journey. Configure Amazon Pinpoint to send events to an Amazon Kinesis data stream for analysis and archiving.

**Stated explanation:** Amazon Pinpoint is a fully managed service for sending messages to mobile app users. With Amazon Pinpoint journeys, you can create multi-step campaigns to engage with users. By configuring Amazon Pinpoint to send events to an Amazon Kinesis data stream, you can capture the responses for further analysis and archiving. This solution provides a comprehensive approach to managing SMS messages and their responses in a scalable and efficient manner.


---

## gh-267  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: D. Create an Amazon Kinesis Data Firehose delivery stream to store the data in Amazon S3. Create an Amazon Kinesis Data Analytics application to analyze the data. Now: The architecture is still the right one — Firehose can encrypt on the way through and convert records to Apache Parquet before landing them in S3, which is the "near-real time" and "centralized Parquet" part of the re

**Question:**

A company has one million users that use its mobile app. The company must analyze the data usage in near-real time. The company also must encrypt the data in near-real time and must store the data in a centralized location in Apache Parquet format for further processing.
Which solution will meet these requirements with the LEAST operational overhead?

**Stated answer:** D. Create an Amazon Kinesis Data Firehose delivery stream to store the data in Amazon S3. Create an Amazon Kinesis Data Analytics application to analyze the data.

**Stated explanation:** (none)


---

## gh-292  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: A (Kinesis Data Streams → Amazon Kinesis Data Analytics to transform → Firehose to S3 → Athena) and B (Amazon MSK → AWS Glue → S3 → Athena). Now: Both answer choices are still correct, so a candidate would score this right. The wording carries the same stale name as gh-267: "Amazon Kinesis Data Analytics" is now "Amazon Managed Service for Apache Flink" (renamed August 2023). Worth

**Question:**

A company is preparing a new data platform that will ingest real-time streaming data from multiple sources. The company needs to transform the data before writing the data to Amazon S3. The company needs the ability to use SQL to query the transformed data.
Which solutions will meet these requirements? (Choose two.)

**Stated answer:** A. Use Amazon Kinesis Data Streams to stream the data. Use Amazon Kinesis Data Analytics to transform the data. Use Amazon Kinesis Data Firehose to write the data to Amazon S3. Use Amazon Athena to query the transformed data from Amazon S3.

**Stated explanation:** B. Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to stream the data. Use AWS Glue to transform the data and to write the data to Amazon S3. Use Amazon Athena to query the transformed data from Amazon S3.

Use Amazon Kinesis Data Streams to stream the data.
Use Amazon Kinesis Data Analytics to transform the data.
Use Amazon Kinesis Data Firehose to write the data to Amazon S3.
Use Amazon Athena to query the transformed data from Amazon S3.
This option uses the Kinesis suite for streaming, analytics, and Firehose for writing to S3, with Athena for querying.

Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to stream the data.
Use AWS Glue to transform the data and write the data to Amazon S3.
Use Amazon Athena to query the transformed data from Amazon S3.
This option leverages Amazon MSK for streaming, AWS Glue for transformation, and Athena for querying, providing a


---

## gh-454  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The answer (Workload Discovery on AWS) is correct, but the explanation invents a relationship between two products: "AWS has a service called AWS Well-Architected Tool, which includes Workload Discovery." It does not. **Workload Discovery on AWS** is a standalone AWS Solutions Library implementation that you deploy into your own account from a CloudFormation template; it inventories resourc

**Question:**

A company has resources across multiple AWS Regions and accounts. A newly hired solutions architect discovers a previous employee did not provide details about the resources inventory. The solutions architect needs to build and map the relationship details of the various workloads across all accounts.
Which solution will meet these requirements in the MOST operationally efficient way?

**Stated answer:** C. Use Workload Discovery on AWS to generate architecture diagrams of the workloads.

**Stated explanation:** AWS has a service called AWS Well-Architected Tool, which includes Workload Discovery. Workload Discovery automatically discovers and visualizes the architecture of your workloads. It provides architecture diagrams, best practice recommendations, and insights into your workloads.


---

## gh-50  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The answer (Systems Manager Run Command) is correct — it is the quickest way to push an ad hoc patch command to 1,000 instances at once, which is what the question asks for. The reasoning used to reject the other options is wrong on two counts. First, it says "Patch Manager is not designed to apply third-party software patches." Patch Manager **does** patch third-party applications (applica

**Question:**

A company has a production workload that runs on 1,000 Amazon EC2 Linux instances. The workload is powered by third-party software. The company needs to patch the third-party software on all EC2 instances as quickly as possible to remediate a critical security vulnerability.
What should a solutions architect do to meet these requirements?

**Stated answer:** D. Use AWS Systems Manager Run Command to run a custom command that applies the patch to all EC2 instances.

**Stated explanation:** AWS Systems Manager Run Command allows the company to run commands or scripts on multiple EC2 instances. By using Run Command, the company can quickly and easily apply the patch to all 1,000 EC2 instances to remediate the security vulnerability.

Creating an AWS Lambda function to apply the patch to all EC2 instances would not be a suitable solution, as Lambda functions are not designed to run on EC2 instances. Configuring AWS Systems Manager Patch Manager to apply the patch to all EC2 instances would not be a suitable solution, as Patch Manager is not designed to apply third-party software patches. Scheduling an AWS Systems Manager maintenance window to apply the patch to all EC2 instances would not be a suitable solution, as maintenance windows are not designed to apply patches to third-party software.


---

## gh-585  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The answer (purchase a Capacity Reservation in the failover Region) is correct, but the explanation misstates how On-Demand Capacity Reservations work: "Capacity Reservations offer flexibility, allowing you to launch different instance types and sizes within the reserved capacity." An On-Demand Capacity Reservation is pinned to a **specific instance type, platform/OS, tenancy and single Ava

**Question:**

A solutions architect is designing a disaster recovery (DR) strategy to provide Amazon EC2 capacity in a failover AWS Region. Business requirements state that the DR strategy must meet capacity in the failover Region.
Which solution will meet these requirements?

**Stated answer:** D. Purchase a Capacity Reservation in the failover Region.

**Stated explanation:** A Capacity Reservation allows you to reserve a specific amount of EC2 instance capacity in a given region without purchasing specific instances. This reserved capacity is dedicated to your account and can be utilized for launching instances when needed. Capacity Reservations offer flexibility, allowing you to launch different instance types and sizes within the reserved capacity.


---

## gh-7  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The answer (publish to an SNS topic with multiple SQS queue subscriptions, one per consumer) is correct, but the second half of the explanation states throughput limits that do not exist for the queue type being used. It claims "an SQS queue can handle a maximum of 3,000 messages per second... AWS can increase the message throughput... up to a maximum of 10,000 messages per second." Standar

**Question:**

A company has an application that ingests incoming messages. Dozens of other applications and microservices then quickly consume these messages. The number of messages varies drastically and sometimes increases suddenly to 100,000 each second. The company wants to decouple the solution and increase scalability.
Which solution meets these requirements?

**Stated answer:** D. Publish the messages to an Amazon Simple Notification Service (Amazon SNS) topic with multiple Amazon Simple Queue Service (Amazon SOS) subscriptions. Configure the consumer applications to process the messages from the queues.

**Stated explanation:** A good practice is to also add message attributes when publishing to SNS. Each SQS subscription can have a filter policy that matches only the messages it cares about, so that only relevant messages are delivered to each SQS queue, and consumers only see/process what they need.

an SQS queue can handle a maximum of 3,000 messages per second. However, you can request higher throughput by contacting AWS Support. AWS can increase the message throughput for your queue beyond the default limits in increments of 300 messages per second, up to a maximum of 10,000 messages per second.

It's important to note that the maximum number of messages per second that a queue can handle is not the same as the maximum number of requests per second that the SQS API can handle. The SQS API is designed to handle a high volume of requests per second, so it can be used to send messages to your queue at a rate 
