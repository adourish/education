# Application integration — queues, topics, events, streams, APIs

95 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. wl-7

You have an S3 bucket that receives photos uploaded by customers. When an object is uploaded, an event notification is sent to an SQS queue with the object details. You also have an ECS cluster that gets messages from the queue to do the batch processing. The queue size may change greatly depending on the number of incoming messages and backend processing speed. Which metric would you use to scale up/down the ECS cluster capacity?

<details><summary>Answer</summary>

**A. The number of messages in the SQS queue.**

In this scenario, the SQS queue is used to store the object details which is a highly
scalable and reliable service. ECS is ideal to perform batch processing and it should
scale up or down based on the number of messages in the queue. Details please check
https://github.com/aws-samples/ecs-refarch-batch-processing.
Option
A 
is
CORRECT:
Users can configure a CloudWatch alarm based
on the number of messages in the SQS queue and notify the ECS cluster to scale up or
down using the alarm.
Option
B 
is
incorrect:
Because memory usage may not be able to
reflect the workload.
Option
C 
is
incorrect:
Because the number of objects in S3 cannot
determine if the ECS cluster should change its capacity.
Option
D 
is
incorrect:
Because the number of containers cannot be
used as a metric to trigger an auto-scaling event.

</details>

### 2. et-10

A company is building an ecommerce web application on AWS. The application sends information about new orders to an Amazon API Gateway REST API to process. The company wants to ensure that orders are processed in the order that they are received. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an API Gateway integration to send a message to an Amazon Simple Queue Service (Amazon SQS) FIFO queue when the application receives an order. Configure the SQS FIFO queue to invoke an AWS Lambda function for processing.**

Use an API Gateway integration to send a message to an Amazon Simple Queue Service (Amazon SQS) FIFO queue when the application receives an order. Configure the SQS FIFO queue to invoke an AWS Lambda function for processing.

</details>

### 3. ce-17

A company uses Amazon API Gateway to manage its REST APIs that third-party service providers access The company must protect the REST APIs from SQL injection and cross-site scripting attacks. What is the MOST operationally efficient solution that meets these requirements?

<details><summary>Answer</summary>

**B. Configure AWS WAR**

AWS Web Application Firewall (WAF) is the service specifically designed to protect web applications and APIs from common web exploits that can affect availability, compromise security, or consume excessive resources. It allows you to configure rules to block common attack patterns, such as SQL injection and cross-site scripting (XSS). AWS WAF can be directly associated with an Amazon API Gateway REST API stage. This provides a direct and operationally efficient method to meet the security requirements without introducing additional services, thus simplifying the architecture and management overhead. Why Incorrect Options are Wrong: A. Configure AWS Shield. AWS Shield is a managed Distributed Denial of Service (DDoS) protection service. It does not provide protection against application-layer attacks like SQL injection or XSS. C. Set up API Gateway with an Amazon CloudFront distribution.

</details>

### 4. wl-21

You have configured AWS S3 event notification to send a message to AWS Simple Queue Service whenever an object is deleted. You are performing a ReceiveMessage API operation on the AWS SQS queue to receive the S3 delete object message onto AWS EC2 instance. For any successful message operations, you are deleting them from the queue. For failed operations, you are not deleting the messages. You have developed a retry mechanism which reruns the application every 5 minutes for failed ReceiveMessage operations. However, you are not receiving the messages again during the rerun. What could have caused this?

<details><summary>Answer</summary>

**D. Visibility Timeout on the SQS queue is set to 10 minutes.**

When a consumer receives and processes a message from a queue, the message
remains in the queue. Amazon SQS doesn't automatically delete the message. Because
Amazon SQS is a distributed system, there's no guarantee that the consumer actually
receives the message (for example, due to a connectivity issue, or due to an issue in
the consumer application). Thus, the consumer must delete the message from the
queue after receiving and processing it.
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/s
qs-visibility-timeout.html

</details>

### 5. dt-26

Which of the following AWS CLI commands is syntactically incorrect?

<details><summary>Answer</summary>

**C. `$ aws sns publish --topic-arn arn:aws:sns:us-east-1:546419318123:OperationsError -message "Script Failure"`.**

</details>

### 6. et-41 `least-ops`

A company's application integrates with multiple software-as-a-service (SaaS) sources for data collection. The company runs Amazon EC2 instances to receive the data and to upload the data to an Amazon S3 bucket for analysis. The same EC2 instance that receives and uploads the data also sends a notification to the user when an upload is complete. The company has noticed slow application performance and wants to improve the performance as much as possible. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Amazon AppFlow flow to transfer data between each SaaS source and the S3 bucket. Configure an S3 event notification to send events to an Amazon Simple Notification Service (Amazon SNS) topic when the upload to the S3 bucket is complete.**

Amazon AppFlow is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift. The use of Appflow helps to remove the ec2 as the middle layer which slows down the process of data transmission and introduce an additional variable. Appflow is also a fully managed AWS service, thus reducing the operational overhead.

</details>

### 7. et-45

A company has a data ingestion workflow that consists of the following: • An Amazon Simple Notification Service (Amazon SNS) topic for notifications about new data deliveries • An AWS Lambda function to process the data and record metadata The company observes that the ingestion workflow fails occasionally because of network connectivity issues. When such a failure occurs, the Lambda function does not ingest the corresponding data unless the company manually reruns the job. Which combination of actions should a solutions architect take to ensure that the Lambda function ingests all data in the future? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon Simple Queue Service (Amazon SQS) queue, and subscribe it to the SNS topic.**

E. Modify the Lambda function to read from an Amazon Simple Queue Service (Amazon SQS) queue.  B. Create an Amazon Simple Queue Service (Amazon SQS) queue, and subscribe it to the SNS topic. This will decouple the ingestion workflow and provide a buffer to temporarily store the data in case of network connectivity issues.  E. Modify the Lambda function to read from an Amazon Simple Queue Service (Amazon SQS) queue. This will allow the Lambda function to process the data from the SQS queue at its own pace, decoupling the data ingestion from the data delivery and providing more flexibility and fault tolerance.

</details>

### 8. ce-51

A company is developing an application in the AWS Cloud. The application's HTTP API contains critical information that is published in Amazon API Gateway. The critical information must be accessible from only a limited set of trusted IP addresses that belong to the company's internal network. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a resource policy for the API that denies access to any IP address that is not specifically allowed.**

Amazon API Gateway resource policies are the designated mechanism for controlling access to an API based on the source IP address of the request. By attaching a resource policy to the API, you can use IAM condition elements, specifically the aws:SourceIp condition key, to create rules. This allows you to define a policy that explicitly allows requests from the company's trusted IP address range while implicitly or explicitly denying all others, thereby fulfilling the security requirement directly and efficiently. Why Incorrect Options are Wrong: A. A private integration connects API Gateway to backend resources within a VPC. It does not control who can call the public-facing API endpoint. C. API Gateway is a managed service and is not deployed directly into a private subnet. Network ACLs control traffic at the subnet level and are not the correct tool for this. D. Security groups are not

</details>

### 9. ce-54 `least-ops`

A logistics company is creating a data exchange platform to share shipment status information with shippers. The logistics company can see all shipment information and metadat a. The company distributes shipment data updates to shippers. Each shipper should see only shipment updates that are relevant to their company. Shippers should not see the full detail that is visible to the logistics company. The company creates an Amazon Simple Notification Service (Amazon SNS) topic for each shipper to share data. Some shippers use a mobile app to submit shipment status updates. The company needs to create a data exchange platform that provides each shipper specific access to the data that is relevant to their company. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Ingest the shipment updates from the mobile app into Amazon Simple Queue Service (Amazon SQS). Use an AWS Lambda function to consume the updates from Amazon SQS and rewrite the body of each message. Publish the updates to the SNS topic.**

This solution effectively decouples the ingestion from the processing and distribution layers, which is a best practice for resilient systems. An Amazon SQS queue reliably captures all incoming shipment updates. An AWS Lambda function, triggered by messages in the SQS queue, provides the necessary compute to perform the custom transformation logic. The function can read the full message, remove or alter data to create a shipper-specific view, and then publish this rewritten message to the appropriate shipper's Amazon SNS topic. This serverless, event-driven architecture is highly scalable and minimizes operational overhead as there are no servers to manage. Why Incorrect Options are Wrong: A: Amazon SNS filter policies operate on message attributes, not the message body. They cannot be used to rewrite or transform the content of the message itself. C: This option has the same fundamental

</details>

### 10. et-206 `least-ops`

A company wants to manage Amazon Machine Images (AMIs). The company currently copies AMIs to the same AWS Region where the AMIs were created. The company needs to design an application that captures AWS API calls and sends alerts whenever the Amazon EC2 CreateImage API operation is called within the company’s account. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create an Amazon EventBridge (Amazon CloudWatch Events) rule for the CreateImage API call. Configure the target as an Amazon Simple Notification Service (Amazon SNS) topic to send an alert when a CreateImage API call is detected.**

Amazon EventBridge (formerly CloudWatch Events) provides a simple and efficient way to respond to events in AWS services. By creating an EventBridge rule specifically for the CreateImage API call, you can easily configure an SNS topic as the target to send alerts when the event is detected.

</details>

### 11. et-211

A company hosts multiple production applications. One of the applications consists of resources from Amazon EC2, AWS Lambda, Amazon RDS, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS) across multiple AWS Regions. All company resources are tagged with a tag name of “application” and a value that corresponds to each application. A solutions architect must provide the quickest solution for identifying all of the tagged components. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Run a query with the AWS Resource Groups Tag Editor to report on the resources globally with the application tag.**

AWS Resource Groups Tag Editor allows you to search and filter resources based on tags across multiple AWS Regions. It provides a centralized view of resources and their corresponding tags, making it easier to identify and manage resources with specific tags. This option provides a quick and efficient way to report on resources with the application tag globally.

</details>

### 12. dt-223

[...] is a fast, flexible, fully managed push messaging service.

<details><summary>Answer</summary>

**A. Amazon SNS.**

</details>

### 13. et-225 `least-ops` `availability`

A media company collects and analyzes user activity data on premises. The company wants to migrate this capability to AWS. The user activity data store will continue to grow and will be petabytes in size. The company needs to build a highly available data ingestion solution that facilitates on-demand analytics of existing data and new data with SQL. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Send activity data to an Amazon Kinesis Data Firehose delivery stream. Configure the stream to deliver the data to an Amazon Redshift cluster.**

Amazon Kinesis Data Firehose: It is a fully managed service that simplifies the delivery of streaming data to destinations such as Amazon S3, Amazon Redshift, or Amazon Elasticsearch Service. It handles the scaling, buffering, and delivery of data.  Amazon Redshift: It is a fully managed, petabyte-scale data warehouse service. It is optimized for high-performance analysis using standard SQL queries.  Least Operational Overhead: Kinesis Data Firehose takes care of many operational aspects, including scaling and buffering, reducing the operational overhead on your part. Configuring it to deliver data to Amazon Redshift provides a streamlined and managed solution.

</details>

### 14. dt-236

Which AWS service helps this functionality?

<details><summary>Answer</summary>

**A. AWS Simple Queue Service.**

</details>

### 15. ce-243

A company generates SSL certificates from a third-party provider. The company imports the certificates into AWS Certificate Manager (ACM) to use with public web applications. A solutions architect must implement a solution to notify the company's security team 30 days before an imported certificate expires. The company already has an Amazon Simple Queue Service (Amazon SQS) queue. The company also has an Amazon Simple Notification Service (Amazon SNS) topic that has the security team's email address as a subscriber. Which solution will provide the security team with the required notification about certificates?

<details><summary>Answer</summary>

**D. Create an Amazon EventBridge rule that specifies the ACM Certificate Approaching Expiration event type. Set the SNS topic as the rule's target.**

This is the most efficient and automated solution. AWS Certificate Manager (ACM) integrates with Amazon EventBridge to automatically emit an "ACM Certificate Approaching Expiration" event for imported certificates. This event is triggered a configurable number of days before expiration. By creating an EventBridge rule that listens for this specific event type, you can define a target to take action. Setting the existing Amazon SNS topic as the target will cause EventBridge to forward the event notification directly to the SNS topic, which then sends an email to the subscribed security team. This approach is serverless, requires no custom code, and is highly reliable. Why Incorrect Options are Wrong: A. This requires writing and maintaining a custom Lambda function to poll ACM. Sending the message to SQS does not directly notify the team and adds an unnecessary step. B. While a Lambda fun

</details>

### 16. et-255

A company has an ecommerce checkout workflow that writes an order to a database and calls a service to process the payment. Users are experiencing timeouts during the checkout process. When users resubmit the checkout form, multiple unique orders are created for the same desired transaction. How should a solutions architect refactor this workflow to prevent the creation of multiple orders?

<details><summary>Answer</summary>

**D. Store the order in the database. Send a message that includes the order number to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Set the payment service to retrieve the message and process the order. Delete the message from the queue.**

Storing the order in the database first ensures that the order information is saved, even if the payment processing is delayed or fails. Sending a message to an SQS FIFO queue with the order number ensures that the processing is idempotent. If the same order number is sent multiple times, SQS guarantees that the messages are processed in order and only once.

</details>

### 17. gh-267 `least-ops`

A company has one million users that use its mobile app. The company must analyze the data usage in near-real time. The company also must encrypt the data in near-real time and must store the data in a centralized location in Apache Parquet format for further processing.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an Amazon Data Firehose delivery stream (formerly Amazon Kinesis Data Firehose) to store the data in Amazon S3. Create an Amazon Managed Service for Apache Flink application (formerly Amazon Kinesis Data Analytics) to analyze the data.**

Firehose is fully managed with no shards to size or scale, it can encrypt data with a KMS key, and its record format conversion feature rewrites incoming JSON into Apache Parquet using a schema from the AWS Glue Data Catalog before writing to S3, which covers the encryption, the format and the centralised location in one managed hop. Firehose buffers for roughly 60 seconds before delivering, which is why this counts as near-real-time rather than real-time, and that satisfies the requirement as worded. Managed Service for Apache Flink reads the stream and runs the analysis without any cluster to operate. Two names changed after this question was written: Kinesis Data Firehose is now Amazon Data Firehose, and Kinesis Data Analytics is now Amazon Managed Service for Apache Flink.

</details>

### 18. et-292

A company is preparing a new data platform that will ingest real-time streaming data from multiple sources. The company needs to transform the data before writing the data to Amazon S3. The company needs the ability to use SQL to query the transformed data. Which solutions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Streams to stream the data. Use Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics) to transform the data. Use Amazon Data Firehose to write the data to Amazon S3. Use Amazon Athena to query the transformed data from Amazon S3. AND B. Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to stream the data. Use AWS Glue to transform the data and to write the data to Amazon S3. Use Amazon Athena to query the transformed data from Amazon S3.**

Both answers follow the same shape the requirement calls for: ingest a stream, transform in flight, land the result in S3, then query it with SQL. In A, Kinesis Data Streams takes the ingest, Managed Service for Apache Flink applies the transformation, Firehose handles delivery to S3, and Athena provides the SQL layer over the objects in the bucket. In B, MSK takes the ingest and an AWS Glue streaming ETL job reads from the Kafka topic, transforms and writes to S3, with Athena again supplying SQL. Athena is what satisfies 'use SQL to query the transformed data' in both cases, because it queries S3 directly with no database to provision. Kinesis Data Analytics was renamed Amazon Managed Service for Apache Flink in August 2023.

</details>

### 19. ce-303

A company wants to receive an email notification when IAM users are added to or deleted from an AWS account. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Enable management events in AWS CloudTrail. Create an Amazon EventBridge rule that responds to AWS API calls through CloudTrail. Configure an event pattern for CreateUser and DeleteUser actions. Set the target as an Amazon SNS topic. Set the company's email address as a subscriber to the SNS topic.**

The requirement is to trigger a notification for specific IAM user management actions. AWS CloudTrail captures AWS API calls, including CreateUser and DeleteUser, as events. These are classified as management events, which should be enabled. Amazon EventBridge can then be used to create a rule that filters for these specific event names from the CloudTrail service. The rule's target can be an Amazon SNS topic. Subscribing an email address to this SNS topic will ensure an email notification is sent whenever a user is created or deleted, directly fulfilling the requirement. Why Incorrect Options are Wrong: A. Amazon Inspector is a vulnerability management service that scans workloads for software vulnerabilities and unintended network exposure; it does not track IAM API calls. B. Amazon GuardDuty is a threat detection service. While it can detect anomalous IAM activity, it is not designed

</details>

### 20. et-316

A company uses an Amazon EC2 instance to run a script to poll for and process messages in an Amazon Simple Queue Service (Amazon SQS) queue. The company wants to reduce operational costs while maintaining its ability to process a growing number of messages that are added to the queue. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Migrate the script on the EC2 instance to an AWS Lambda function with the appropriate runtime.**

AWS Lambda: Lambda is a serverless computing service that allows you to run code without provisioning or managing servers. It automatically scales based on the number of incoming requests. Cost-Efficiency: With Lambda, you only pay for the compute time consumed during code execution. This can be more cost-effective than running and maintaining an EC2 instance, especially for sporadic or event-driven workloads. Automatic Scaling: Lambda automatically scales based on the number of incoming events. As the number of messages in the SQS queue grows, Lambda can scale out to handle the increased workload. Event-Driven: Lambda is well-suited for event-driven architectures, making it a good fit for scenarios where messages are added to an SQS queue.

</details>

### 21. et-322

A solutions architect is designing a multi-tier application for a company. The application's users upload images from a mobile device. The application generates a thumbnail of each image and returns a message to the user to confirm that the image was uploaded successfully. The thumbnail generation can take up to 60 seconds, but the company wants to provide a faster response time to its users to notify them that the original image was received. The solutions architect must design the application to asynchronously dispatch requests to the different application tiers. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Simple Queue Service (Amazon SQS) message queue. As images are uploaded, place a message on the SQS queue for thumbnail generation. Alert the user through an application message that the image was received.**

Amazon SQS (Simple Queue Service): SQS is a fully managed message queuing service that enables decoupling of the components of a cloud application. By creating an SQS message queue, the image upload process can place messages in the queue for thumbnail generation.

</details>

### 22. et-323 `availability`

A company’s facility has badge readers at every entrance throughout the building. When badges are scanned, the readers send a message over HTTPS to indicate who attempted to access that particular entrance. A solutions architect must design a system to process these messages from the sensors. The solution must be highly available, and the results must be made available for the company’s security team to analyze. Which system architecture should the solutions architect recommend?

<details><summary>Answer</summary>

**B. Create an HTTPS endpoint in Amazon API Gateway. Configure the API Gateway endpoint to invoke an AWS Lambda function to process the messages and save the results to an Amazon DynamoDB table.**

</details>

### 23. ce-325

A solutions architect is designing an application that helps users fill out and submit registration forms. The solutions architect plans to use a two-tier architecture that includes a web application server tier and a worker tier. The application needs to process submitted forms quickly. The application needs to process each form exactly once. The solution must ensure that no data is lost. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use an Amazon Simple Queue Service Amazon SQS) FIFO queue between the web application server tier and the worker tier to store and forward form data.**

The scenario requires a durable, decoupled solution that guarantees messages (form submissions) are processed exactly once. Amazon SQS is a managed message queuing service designed for decoupling microservices, distributed systems, and serverless applications. SQS offers two queue types: Standard and FIFO. SQS FIFO (First-In, First-Out) queues are specifically designed to process messages exactly once and preserve the order in which they are sent. This directly meets the core requirements of the application, ensuring no data is lost and each form is processed without duplication. Why Incorrect Options are Wrong: B. Use an Amazon API Gateway HTTP API...: API Gateway is a service for creating and managing APIs. It is not a durable message queue and does not inherently guarantee exactly-once processing for backend workers. C. Use an Amazon Simple Queue Service (Amazon SQS) standard queue...

</details>

### 24. ce-339

A company has an ecommerce application that users access through multiple mobile apps and web applications. The company needs a solution that will receive requests from the mobile apps and web applications through an API. Request traffic volume varies significantly throughout each day. Traffic spikes during sales events. The solution must be loosely coupled and ensure that no requests are lost.

<details><summary>Answer</summary>

**B. Set up an Amazon API Gateway REST API with an integration to an Amazon Simple Queue Service (Amazon SQS) queue. Configure a dead-letter queue. Create an AWS Lambda function to poll the queue to process the requests.**

This solution provides a highly scalable, resilient, and loosely coupled architecture ideal for variable e-commerce traffic. Amazon API Gateway acts as a managed, scalable entry point for all requests. Integrating it with an Amazon SQS queue decouples the request ingestion from the processing logic. The SQS queue serves as a durable buffer, absorbing traffic spikes and ensuring that no requests are lost, even if the downstream processing service is temporarily unavailable. An AWS Lambda function can then poll the queue and process messages asynchronously. The use of a dead-letter queue (DLQ) further enhances reliability by capturing any messages that fail processing, preventing data loss. Why Incorrect Options are Wrong: A. This is a tightly coupled architecture. If the Elastic Beanstalk environment is overwhelmed by a traffic spike and cannot scale fast enough, the Application Load Bala

</details>

### 25. ce-341 `availability`

A company is building a serverless application to process orders from an ecommerce site. The application needs to handle bursts of traffic during peak usage hours and to maintain high availability. The orders must be processed asynchronously in the order the application receives them. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an Amazon Simple Queue Service (Amazon SQS) FIFO queue to receive orders. Use an AWS Lambda function to process the orders.**

The core requirements are asynchronous processing, handling traffic bursts, and maintaining the exact order of operations. Amazon SQS FIFO (First-In, First-Out) queues are specifically designed to guarantee that messages are processed exactly once, in the precise order that they are sent. By placing orders into an SQS FIFO queue, the application can decouple the order ingestion from the processing logic, effectively buffering bursts of traffic. An AWS Lambda function can then be configured to poll the queue and process the orders asynchronously. This combination creates a fully serverless, scalable, and highly available solution that strictly preserves the order of transactions as required. Why Incorrect Options are Wrong: A. Amazon SNS standard topics do not guarantee the order of message delivery, which violates the strict "in order" processing requirement. C. Amazon SQS standard queue

</details>

### 26. et-344

A company has a Java application that uses Amazon Simple Queue Service (Amazon SQS) to parse messages. The application cannot parse messages that are larger than 256 KB in size. The company wants to implement a solution to give the application the ability to parse messages as large as 50 MB. Which solution will meet these requirements with the FEWEST changes to the code?

<details><summary>Answer</summary>

**A. Use the Amazon SQS Extended Client Library for Java to host messages that are larger than 256 KB in Amazon S3.**

Amazon SQS Extended Client Library for Java: This library is specifically designed to handle larger messages in Amazon SQS by transparently offloading them to Amazon S3. It allows you to send a reference to the S3 object in the SQS message while keeping the actual payload in S3.  Minimal Code Changes: Using the Amazon SQS Extended Client Library for Java requires minimal changes to the existing code. Developers need to integrate the library, and the library itself handles the details of storing and retrieving large messages from Amazon S3.

</details>

### 27. ce-346

A company wants to create a payment processing application. The application must run when a payment record arrives in an existing Amazon S3 bucket. The application must process each payment record exactly once. The company wants to use an AWS Lambda function to process the payments. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure the existing S3 bucket to send object creation events to Amazon EventBridge. Configure EventBridge to route events to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Configure the Lambda function to run when a new event arrives in the SQS queue.**

The core requirement is to process each payment record exactly once. Amazon SQS FIFO (First-In, First-Out) queues are specifically designed for this purpose. They prevent duplicate messages from being sent and ensure that messages are processed in the exact order they are received. By routing S3 object creation events through Amazon EventBridge to an SQS FIFO queue, and then triggering the Lambda function from this queue, the architecture guarantees that each payment event is processed exactly once. This design decouples the components and provides the necessary transactional integrity for a payment processing system. Why Incorrect Options are Wrong: B. Amazon SNS topics, like standard SQS queues, provide at-least-once delivery, which can result in duplicate Lambda invocations and does not meet the "exactly once" processing requirement. C. Standard Amazon SQS queues provide at-least-once

</details>

### 28. ce-349

A developer is creating an ecommerce workflow in an AWS Step Functions state machine that includes an HTTP Task state. The task passes shipping information and order details to an endpoint. The developer needs to test the workflow to confirm that the HTTP headers and body are correct and that the responses meet expectations. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Change the log level of the state machine to ALL. Run the state machine.**

Setting CloudWatch Logs for the state machine to LogLevel = ALL records every event for each state, including the complete JSON request that the HTTP Task sends (headers, body) and the full JSON response that the endpoint returns. By executing the workflow once with this log level, the developer can inspect the CloudWatch log stream to verify that both the outbound HTTP request and the inbound response match expectations, while exercising the task against the real endpoint. Why Incorrect Options are Wrong: A. TestState runs only a single state and, by design, does not actually invoke service/HTTP integrations; it returns stubbed data, so real headers and responses are unavailable. B. TestState cannot execute an entire state machine; it is limited to individual states and returns simulated data, not the real HTTP exchange. C. The Data flow simulator evaluates paths and intrinsic functions

</details>

### 29. dt-355

Your customer is willing to consolidate their log streams (access logs, application logs, security logs, etc.) in one single system. Once consolidated, the customer wants to analyze these logs in real-time based on heuristics. From time to time, the customer needs to validate heuristics, which requires going back to data samples extracted from the last 12 hours. What is the best approach to meet your customer's requirements?

<details><summary>Answer</summary>

**B. Send all the log events to Amazon Kinesis. Develop a client process to apply heuristics on the logs.**

</details>

### 30. ce-360

A company is building a serverless application that processes large volumes of data from a mobile app. The application uses an AWS Lambda function to process the data and store the data in an Amazon DynamoDB table. The company needs to ensure that the application can recover from failures and continue processing data without losing any records. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure the Lambda function to use a dead-letter queue with an Amazon Simple Queue Service (Amazon SQS) queue. Configure Lambda to retry failed records from the dead-letter queue. Use a retry mechanism by implementing an exponential backoff algorithm.**

The most reliable and standard AWS pattern for handling asynchronous AWS Lambda invocation failures is to configure a dead-letter queue (DLQ). When a Lambda function fails after its configured retries, the event payload is sent to the DLQ. Using an Amazon SQS queue as the DLQ target ensures that failed events are durably stored. A separate process, such as another Lambda function, can then be used to process messages from this DLQ, allowing for analysis and reprocessing. Implementing an exponential backoff algorithm for retries is a best practice to prevent overwhelming downstream services that may be temporarily unavailable. Why Incorrect Options are Wrong: B: Amazon Data Firehose is a data ingestion service. While it has its own retry logic for delivery, it is not the correct tool for managing failures within the Lambda function's processing logic. C: Amazon OpenSearch Service is desig

</details>

### 31. ce-361

A company wants to enhance its ecommerce order-processing application that is deployed on AWS. The application must process each order exactly once without affecting the customer experience during unpredictable traffic surges. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Put all the orders in the SQS queue. Configure an AWS Lambda function as the target to process the orders.**

The solution requires a system that can buffer incoming orders during traffic surges and ensure each order is processed exactly once. Amazon SQS FIFO (First-In, First-Out) queues are designed for this specific purpose. SQS decouples the order submission front-end from the back-end processing, allowing it to absorb unpredictable traffic spikes without impacting the customer experience. The FIFO queue type specifically provides features for exactly-once processing and message deduplication, which prevents duplicate orders. Integrating the SQS FIFO queue with an AWS Lambda function creates a scalable, serverless, and resilient architecture for processing the orders as they arrive in the queue. Why Incorrect Options are Wrong: B: Amazon SNS standard topics provide at-least-once message delivery, which can result in duplicate messages and does not meet the "exactly-once" processing requiremen

</details>

### 32. dt-361 `cost`

A customer has a 10 GB AWS Direct Connect connection to an AWS region where they have a web application hosted on Amazon Elastic Computer Cloud (EC2). The application has dependencies on an on-premises mainframe database that uses a BASE (Basic Available. Sort stale Eventual consistency) rather than an ACID (Atomicity. Consistency isolation. Durability) consistency model. The application is exhibiting undesirable behavior because the database is not able to handle the volume of writes. How can you reduce the load on your on-premises database resources in the most cost-effective way?

<details><summary>Answer</summary>

**B. Modify the application to write to an Amazon SQS queue and develop a worker process to flush the queue to the on-premises database.**

</details>

### 33. et-362

A company uses a payment processing system that requires messages for a particular payment ID to be received in the same order that they were sent. Otherwise, the payments might be processed incorrectly. Which actions should a solutions architect take to meet this requirement? (Choose two.)

<details><summary>Answer</summary>

**B. Write the messages to an Amazon Kinesis data stream with the payment ID as the partition key.**

E. Write the messages to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Set the message group to use the payment ID.  Amazon Kinesis data streams can be used with partition keys to ensure that messages with the same partition key are processed in order. In this case, using the payment ID as the partition key will help maintain the order of messages.  SQS FIFO queues ensure that messages are processed in the order they are received. By using message groups and setting the payment ID as the message group, you can guarantee that messages for the same payment ID will be processed sequentially.

</details>

### 34. et-363

A company is building a game system that needs to send unique events to separate leaderboard, matchmaking, and authentication services concurrently. The company needs an AWS event-driven system that guarantees the order of the events. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Amazon Simple Notification Service (Amazon SNS) FIFO topics**

SNS FIFO also can send events or messages cocurrently to many subscribers while maintaining the order it receives. SNS fanout pattern is set in standard SNS which is commonly used to fan out events to large number of subscribers and usually for duplicated messages.

</details>

### 35. ce-375

A company's application receives requests from customers in JSON format. The company uses Amazon Simple Queue Service (Amazon SQS) to handle the requests. After the application's most recent update, the company's customers reported that requests were being duplicated. A solutions architect discovers that the application is consuming messages from the SQS queue more than once. What is the root cause of the issue?

<details><summary>Answer</summary>

**D. The visibility timeout is shorter than the time it takes the application to process messages from the queue.**

In Amazon SQS, when a consumer retrieves a message, the message is not deleted but becomes temporarily invisible for a period known as the visibility timeout. The consumer is expected to process and then explicitly delete the message within this timeframe. If the application's processing time exceeds the visibility timeout, the message will not be deleted in time. Consequently, the visibility timeout expires, and the message reappears in the queue, making it available for another consumer to retrieve and process. This results in the same message being processed more than once, causing the reported duplication. Why Incorrect Options are Wrong: A. A visibility timeout that is longer than the processing time is the correct configuration, as it provides sufficient time for the application to process and delete the message, thus preventing duplicates. B. Unescaped Unicode characters might cau

</details>

### 36. ce-389

An ecommerce company experiences a surge in mobile application traffic every Monday at 8 AM during the company's weekly sales events. The application's backend uses an Amazon API Gateway HTTP API and AWS Lambda functions to process user requests. During peak sales periods, users report encountering TooManyRequestsException errors from the Lambda functions. The errors result in a degraded user experience. A solutions architect needs to design a scalable and resilient solution that minimizes the errors and ensures that the application's overall functionality remains unaffected.

<details><summary>Answer</summary>

**A. Create an Amazon Simple Queue Service (Amazon SQS) queue. Send user requests to the SQS queue. Configure the Lambda function with provisioned concurrency. Set the SQS queue as the event source trigger.**

The core issue is that a synchronous invocation pattern (API Gateway - Lambda) cannot handle the sudden burst of traffic, leading to Lambda throttling and TooManyRequestsException errors. The most effective solution is to decouple the components using a message queue. Amazon SQS is designed for this purpose. By placing an SQS queue between API Gateway and the Lambda function, the queue acts as a buffer, absorbing the traffic spike. The Lambda function can then pull messages from the queue and process them at a sustainable rate, preventing throttling. Using provisioned concurrency ensures that a specified number of Lambda execution environments are pre-warmed and ready, minimizing cold-start latency and further improving responsiveness for the requests processed from the queue. Why Incorrect Options are Wrong: B: AWS Step Functions is an orchestration service for multi-step workflows. It

</details>

### 37. ce-390

A solutions architect has an application container, an AWS Lambda function, and an Amazon Simple Queue Service (Amazon SQS) queue. The Lambda function uses the SQS queue as an event source. The Lambda function makes a call to a third-party machine learning (ML) API when the function is invoked. The response from the third-party API can take up to 60 seconds to return. The Lambda function's timeout value is currently 65 seconds. The solutions architect has noticed that the Lambda function sometimes processes duplicate messages from the SQS queue. What should the solutions architect do to ensure that the Lambda function does not process duplicate messages?

<details><summary>Answer</summary>

**D. Configure the SQS queue's visibility timeout value to be greater than the maximum time it takes to call the third-party API.**

Duplicate message processing occurs when a message is received by a Lambda function, but the function does not delete the message from the Amazon SQS queue before the queue's visibility timeout expires. The default visibility timeout is 30 seconds. In this scenario, the API call can take up to 60 seconds. If the visibility timeout is less than the total processing time, the message will reappear in the queue and be picked up by another Lambda invocation, resulting in a duplicate process. To resolve this, the SQS queue's visibility timeout must be configured to be longer than the total processing time of the Lambda function, which includes the API call duration. Why Incorrect Options are Wrong: A. Increasing the Lambda function's memory will not reduce the latency of the external third-party API call, which is the root cause of the long processing time. B. The Lambda function's timeout is

</details>

### 38. dt-399

After deciding that EMR will be useful in analysing vast amounts of data for a gaming website that you are architecting you have just deployed an Amazon EMR Cluster and wish to monitor the cluster performance. Which of the following tools cannot be used to monitor the cluster performance?

<details><summary>Answer</summary>

**A. Kinesis.**

</details>

### 39. et-400 `least-ops`

A meteorological startup company has a custom web application to sell weather data to its users online. The company uses Amazon DynamoDB to store its data and wants to build a new service that sends an alert to the managers of four internal teams every time a new weather event is recorded. The company does not want this new service to affect the performance of the current application. What should a solutions architect do to meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Enable Amazon DynamoDB Streams on the table. Use triggers to write to a single Amazon Simple Notification Service (Amazon SNS) topic to which the teams can subscribe.**

Using a single SNS topic simplifies the notification process. The trigger can publish a message to this topic, and each internal team can subscribe to this topic. This reduces the operational overhead compared to managing multiple SNS topics (Option B).

</details>

### 40. dt-405

A user has deployed an application on his private cloud. The user is using his own monitoring tool. He wants to configure it so that whenever there is an error, the monitoring tool will notify him via SMS. Which of the below mentioned AWS services will help in this scenario?

<details><summary>Answer</summary>

**B. AWS SNS.**

</details>

### 41. ce-417

A company is building a serverless application that processes large volumes of data from a mobile app. A Lambda function processes the data and stores it in DynamoDB. The company must ensure the application can recover from failures and continue processing without losing records. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure the Lambda function with a dead-letter queue (DLQ) using SQS. Retry failed records from the DLQ with exponential backoff.**

The most reliable and standard AWS pattern for handling asynchronous Lambda invocation failures is to configure a dead-letter queue (DLQ). When a Lambda function, invoked asynchronously, fails after its built-in retries are exhausted, the event payload is sent to the configured DLQ. Using an Amazon SQS queue as the DLQ ensures that the failed event is durably stored and not lost. A separate process, such as another Lambda function, can then be used to process messages from the DLQ for analysis or to retry the operation, often with an exponential backoff strategy to handle transient errors effectively. This directly addresses the requirement to recover from failures without losing records. Why Incorrect Options are Wrong: B: Amazon Data Firehose is a data delivery service, not an event source queue for Lambda. It does not have a native mechanism to replay individual failed records in the

</details>

### 42. ce-420

A retail company is building an order fulfillment system using a microservices architecture on AWS. The system must store incoming orders durably until processing completes successfully. Multiple teams' services process orders according to a defined workflow. Services must be scalable, loosely coupled, and able to handle sudden surges in order volume. The processing steps of each order must be centrally tracked. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Send incoming orders to an Amazon Simple Queue Service (Amazon SQS) queue. Start an AWS Step Functions workflow for each order that orchestrates the microservices. Use AWS Lambda functions for each microservice.**

This solution effectively meets all requirements. Amazon SQS provides a durable and scalable queue to buffer incoming orders, ensuring no data is lost during volume surges and decoupling the ingestion layer from the processing services. AWS Step Functions is an orchestration service that is ideal for managing a defined, multi-step workflow. It centrally tracks the state of each order as it moves through the various microservices (implemented as AWS Lambda functions), providing the required visibility and state management. This combination creates a resilient, scalable, and observable system. Why Incorrect Options are Wrong: A. Amazon SNS is a pub/sub messaging service, not a durable queue. While it can handle surges, it is not the optimal choice for durably storing messages until processing is complete, unlike SQS. C. Amazon EventBridge is an event bus used for choreography (event-driven

</details>

### 43. ce-426

A company has built an application that uses an Amazon Simple Queue Service (Amazon SQS) standard queue and an AWS Lambda function. The Lambda function writes messages to the SQS queue. The company needs a solution to ensure that the consumer of the SQS queue never receives duplicate messages. Which solution will meet this requirement with the FEWEST changes to the current architecture?

<details><summary>Answer</summary>

**B. Delete the existing SQS queue. Recreate the queue as a FIFO queue. Enable content-based deduplication for the queue.**

The core requirement is to prevent duplicate messages, which necessitates exactly-once processing. Amazon SQS Standard queues, by design, provide at-least-once delivery, meaning duplicates are possible. SQS FIFO (First-In, First-Out) queues are specifically designed to provide exactly-once processing and prevent duplicates. The type of an SQS queue (Standard or FIFO) cannot be modified after its creation. Therefore, the existing Standard queue must be deleted and a new FIFO queue created in its place. Enabling content-based deduplication on the new FIFO queue is the simplest way for the producer (the Lambda function) to ensure deduplication without needing to generate and manage a unique MessageDeduplicationId for each message. This solution directly addresses the requirement with the fewest necessary architectural changes. Why Incorrect Options are Wrong: A. Long polling is an optimizat

</details>

### 44. ce-427

A company runs an ecommerce platform with a monolithic architecture on Amazon EC2 instances. The platform runs web and API services. The company wants to decouple the architecture and enhance scalability. The company also wants the ability to track orders and reprocess any failed orders. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Send orders to an Amazon Simple Queue Service (Amazon SQS) queue. Configure AWS Lambda functions to consume the queue and process orders. Implement an SQS dead-letter queue.**

Publishing each order as a message to Amazon SQS immediately decouples the web/API tier from order-processing logic. AWS Lambda polls the queue and scales concurrency automatically, so the system can elastically meet any surge in order volume without manual capacity planning. Configuring an SQS dead-letter queue (DLQ) provides a native, durable store for messages that exceed the maximum-receive count, letting operations staff inspect, track, and replay failed orders. The solution therefore satisfies all three requirements: decoupling, horizontal scalability, and reliable tracking/reprocessing of failures, by using fully managed services that require no server management. Why Incorrect Options are Wrong: B. Visibility timeout only hides a message temporarily; it gives no persistent record of permanently failed orders and provides no simple replay mechanism. C. Kinesis lacks a built-in DLQ

</details>

### 45. ce-433

A company is building a serverless application to process ecommerce orders. The application must handle bursts of traffic and process orders asynchronously in the order received. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon SQS FIFO with AWS Lambda.**

The application requires asynchronous processing of orders in the exact order they are received (First-In, First-Out) while handling traffic bursts. Amazon SQS FIFO (First-In-First-Out) queues are specifically designed for use cases where the order of operations is critical. They guarantee that messages are processed exactly once, in the exact order that they are sent. Integrating an SQS FIFO queue with an AWS Lambda function provides a fully serverless, scalable, and asynchronous architecture that meets all the stated requirements. Why Incorrect Options are Wrong: A. Amazon SNS is a pub/sub service and does not guarantee the order of message delivery to subscribers, failing the FIFO requirement. C. Amazon SQS standard queues provide at-least-once delivery but only make a best-effort attempt at preserving order, which is insufficient for this use case. D. Amazon SNS does not guarantee me

</details>

### 46. ce-446

A company is developing an ecommerce application that uses an Amazon API Gateway HTTP API. When a customer creates an order in the application, three downstream consumers must process the order event. The downstream consumers include a billing service that uses AWS Lambda functions, an email messaging service that uses AWS Lambda functions, and an inventory service that uses Amazon EC2 instances. Each consumer must receive every event. The service must absorb traffic bursts with durable buffering for each consumer. The company must be able to add new consumers without changing the producer or existing consumers. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Publish order events to an Amazon SNS topic. Subscribe one Amazon SQS queue to the SNS topic for each consumer. Configure each consumer to process events from its own SQS queue.**

This solution effectively decouples the producer from the consumers and meets all requirements. Amazon SNS provides a publish/subscribe (pub/sub) model, allowing the API to publish a single order event to an SNS topic. This topic can then fan out the event to multiple subscribers. By subscribing a dedicated Amazon SQS queue for each of the three consumers, every consumer receives a copy of the event. The SQS queues provide durable buffering, absorbing traffic bursts and retaining messages if a consumer is temporarily unavailable. New consumers can be added by simply subscribing a new queue to the topic, with no changes to the existing architecture. Why Incorrect Options are Wrong: B. A single SQS queue does not support a fan-out pattern; once a message is consumed by one consumer, it is unavailable to others. C. While EventBridge supports fan-out, targeting consumers directly does not pr

</details>

### 47. ce-455

A company is building an ecommerce web service on AWS. The web service sends information about new orders to an Amazon API Gateway REST API for processing. The company wants to eliminate duplicate orders within a 5-minute processing window. Which solution will meet this requirement with the LEAST amount of development effort?

<details><summary>Answer</summary>

**B. Configure API Gateway to send a message to an Amazon SQS FIFO queue when API Gateway receives an order. Include a MessageDeduplicationId token in the order requests. Configure the queue to invoke an AWS Lambda function for processing.**

Amazon SQS FIFO (First-In, First-Out) queues are designed for exactly-once processing and preserving the order of messages. They have a built-in content-based deduplication feature that uses a MessageDeduplicationId. When a message is sent with a MessageDeduplicationId that has been successfully processed within the 5-minute deduplication interval, the new message is accepted but not delivered. This directly meets the requirement to eliminate duplicates within a 5-minute window with minimal development effort, as the deduplication logic is handled by the SQS service itself rather than custom application code. Why Incorrect Options are Wrong: A. SNS FIFO topics provide deduplication, but this is more complex than SQS for this use case. Standard SNS topics do not offer message deduplication. C. SQS standard queues do not guarantee order or provide automatic deduplication. This would requir

</details>

### 48. ce-472

A company's platform has reported multiple instances of duplicate orders in its order-processing system. The company uses Amazon SQS FIFO queues to ensure that orders are processed in the order in which they were received. The company needs to identify the root cause of the duplicate orders to prevent future occurrences. The company also needs to determine whether the duplicate orders originate from the company's message producers. Which Amazon CloudWatch metric for Amazon SQS should the company analyze?

<details><summary>Answer</summary>

**B. NumberOfDeduplicatedSentMessages**

Amazon SQS FIFO (First-In, First-Out) queues provide content-based deduplication. If a producer sends a message with a message deduplication ID that has already been successfully processed within the 5-minute deduplication interval, SQS will accept the message but will not deliver it again. The NumberOfDeduplicatedSentMessages CloudWatch metric specifically tracks the number of messages that were sent to the queue but were identified as duplicates and therefore discarded. Analyzing this metric will directly confirm if the message producers are sending duplicate messages to the SQS queue, which is the root cause the company wants to investigate. Why Incorrect Options are Wrong: A. ApproximateNumberOfMessagesVisible shows the number of messages in the queue ready for processing, not duplicates. C. ApproximateNumberOfGroupsWithInflightMessages is a FIFO-specific metric related to message gr

</details>

### 49. dt-474

You have a number of image files to encode. In an Amazon SQS worker queue, you create an Amazon SQS message for each file specifying the command (jpeg-encode) and the location of the file in Amazon S3. Which of the following statements best describes the functionality of Amazon SQS?

<details><summary>Answer</summary>

**A. Amazon SQS is a distributed queuing system that is optimized for horizontal scalability, not for single-threaded sending or receiving speeds.**

</details>

### 50. ce-475 `availability`

A company is migrating its order processing system to the AWS Cloud. The order processing system must use exact message ordering, a highly available architecture, and loosely coupled components. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Ingest the orders in an Amazon SQS FIFO queue. Invoke an AWS Lambda function to process the orders.**

The core requirements are exact message ordering, high availability, and loose coupling. Amazon SQS FIFO (First-In, First-Out) queues are specifically designed to guarantee that messages are processed exactly once, in the exact order that they are sent. This directly satisfies the "exact message ordering" requirement. Invoking an AWS Lambda function from the SQS FIFO queue creates a highly available, serverless, and loosely coupled architecture. Lambda scales automatically and integrates seamlessly with SQS, meeting all stated requirements effectively. Why Incorrect Options are Wrong: A. Amazon SQS standard queues provide at-least-once delivery but only best-effort ordering, which violates the exact ordering requirement. B. Amazon SNS is a pub/sub service and does not guarantee the order in which messages are delivered to subscribers. C. While Kinesis Data Streams maintains order within

</details>

### 51. dt-489

You are the new IT architect in a company that operates a mobile sleep tracking application. When activated at night, the mobile app is sending collected data points of 1 kilobyte every 5 minutes to your backend. The backend takes care of authenticating the user and writing the data points into an Amazon DynamoDB table. Every morning, you scan the table to extract and aggregate last night's data on a per user basis, and store the results in Amazon S3. Users are notified via Amazon SNS mobile push notifications that new data is available, which is parsed and visualized by the mobile app. Currently you have around 100k users who are mostly based out of North America. You have been tasked to optimize the architecture of the backend system to lower cost. What would you recommend? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Create a new Amazon DynamoDB table each day and drop the one for the previous day after its data is on Amazon S3.; C. Introduce an Amazon SQS queue to buffer writes to the Amazon DynamoDB table and reduce provisioned write throughput.**

</details>

### 52. et-489

An ecommerce company runs an application in the AWS Cloud that is integrated with an on-premises warehouse solution. The company uses Amazon Simple Notification Service (Amazon SNS) to send order messages to an on-premises HTTPS endpoint so the warehouse application can process the orders. The local data center team has detected that some of the order messages were not received. A solutions architect needs to retain messages that are not delivered and analyze the messages for up to 14 days. Which solution will meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**C. Configure an Amazon SNS dead letter queue that has an Amazon Simple Queue Service (Amazon SQS) target with a retention period of 14 days.**

Amazon SNS allows you to set up a dead letter queue to capture and retain messages that cannot be delivered to the intended endpoint. When configuring a DLQ, you can specify an Amazon SQS queue as the target for messages that fail to be delivered. Amazon SQS provides message retention settings, and in this case, you can set the retention period to 14 days.

</details>

### 53. ce-497

A company has a three-tier web application that processes orders from customers. The web tier consists of Amazon EC2 instances behind an Application Load Balancer. The processing tier consists of EC2 instances. The company decoupled the web tier and processing tier by using Amazon Simple Queue Service (Amazon SQS). The storage layer uses Amazon DynamoDB. At peak times some users report order processing delays and halts. The company has noticed that during these delays, the EC2 instances are running at 100% CPU usage, and the SQS queue fills up. The peak times are variable and unpredictable. The company needs to improve the performance of the application Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use an Amazon EC2 Auto Scaling target tracking policy to scale out the processing tier instances. Use the ApproximateNumberOfMessages attribute to determine when to scale.**

The problem describes a bottleneck in the processing tier, where EC2 instances are overwhelmed by messages from an SQS queue during unpredictable peak times. This leads to 100% CPU usage and a growing queue backlog. The most effective solution is to dynamically scale the number of processing instances based on the workload. An Amazon EC2 Auto Scaling group with a target tracking policy is designed for this exact scenario. By setting the SQS queue's ApproximateNumberOfMessagesVisible attribute as the scaling metric, the system can automatically add more EC2 instances when the number of messages in the queue increases and remove them as the queue drains. This directly ties the processing capacity to the demand, ensuring timely order processing even during unpredictable peaks. Why Incorrect Options are Wrong: A: Scheduled scaling is ineffective because the peak times are "variable and unpre

</details>

### 54. ce-511

A company tracks customer satisfaction by using surveys that the company hosts on its website. The surveys sometimes reach thousands of customers every hour. Survey results are currently sent in email messages to the company so company employees can manually review results and assess customer sentiment. The company wants to automate the customer survey process. Survey results must be available for the previous 12 months. Which solution will meet these requirements in the MOST scalable way?

<details><summary>Answer</summary>

**A. Send the survey results data to an Amazon API Gateway endpoint that is connected to an Amazon Simple Queue Service (Amazon SQS) queue. Create an AWS Lambda function to poll the SQS queue, call Amazon Comprehend for sentiment analysis, and save the results to an Amazon DynamoDB table. Set the TTL for all records to 365 days in the future.**

This solution provides the most scalable and resilient architecture for the described workload. Using Amazon API Gateway with Amazon Simple Queue Service (SQS) decouples the ingestion layer from the processing layer. This allows the system to handle thousands of hourly survey submissions by buffering them in the SQS queue, preventing data loss during traffic spikes. An AWS Lambda function, triggered by messages in the queue, processes the data. It correctly uses Amazon Comprehend for sentiment analysis of the survey text. The results are stored in Amazon DynamoDB, a highly scalable NoSQL database, and DynamoDB Time to Live (TTL) is used to automatically expire records after 12 months (365 days), meeting the data retention requirement. Why Incorrect Options are Wrong: B: Using an Amazon EC2 instance for the API is less scalable and requires more operational overhead than the serverless AP

</details>

### 55. ce-522

A company has developed an API using Amazon API Gateway REST API and AWS Lambd a. How can latency be reduced for users worldwide?

<details><summary>Answer</summary>

**A. Deploy the REST API as an edge-optimized API endpoint. Enable caching. Enable content encoding to compress data in transit.**

To reduce latency for a global user base, a multi-faceted approach is required. 1. Edge-Optimized API Endpoint: This endpoint type uses the Amazon CloudFront content delivery network (CDN) to route user requests to the nearest edge location. This significantly reduces network latency for geographically distributed users by minimizing the distance data travels over the public internet. 2. API Caching: Enabling caching within API Gateway stores responses for a defined period (TTL). Subsequent identical requests are served directly from the low-latency cache, avoiding the need to invoke the backend Lambda function, which reduces both latency and backend load. 3. Content Encoding: Enabling payload compression (e.g., Gzip) reduces the size of the data transferred between the API and the user. Smaller payloads are transmitted faster, decreasing download times and improving perceived latency. W

</details>

### 56. ce-524

A company is developing a social media application that must scale to meet demand spikes and handle ordered processes. Which AWS services meet these requirements?

<details><summary>Answer</summary>

**A. ECS with Fargate, RDS, and SQS for decoupling.**

This architecture effectively meets all requirements. Amazon ECS with AWS Fargate provides a serverless, container-based compute layer that automatically scales to handle demand spikes without requiring server management. Amazon RDS is a suitable managed relational database for a social media application's structured data. Most importantly, Amazon SQS (Simple Queue Service) FIFO (First-In, First-Out) queues are specifically designed to decouple application components while preserving the exact order of messages. This directly fulfills the requirement to "handle ordered processes," making this combination the most appropriate solution. Why Incorrect Options are Wrong: B. ECS with Fargate, RDS, and SNS for decoupling. Amazon SNS is a pub/sub messaging service and does not guarantee the order of message delivery, failing the "ordered processes" requirement. C. DynamoDB, Lambda, DynamoDB Str

</details>

### 57. ce-530

A solutions architect needs to implement a solution that can handle up to 5,000 messages per second. The solution must publish messages as events to multiple consumers. The messages are upto 500 KB in size. The message consumers need to have the ability to use multiple programming languages to consume the messages with minimal latency. The solution must retain published messages for more than 3 months. The solution must enforce strict ordering of the messages. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Publish messages to an Amazon Kinesis Data Streams data stream. Enable enhanced fan-out. Ensure that consumers ingest the data stream by using dedicated throughput.**

Amazon Kinesis Data Streams is the optimal choice as it meets all specified requirements. It can handle high throughput (thousands of messages per second) by scaling the number of shards. It supports a fan-out model for multiple consumers, which is made more efficient and low-latency (around 70ms) with enhanced fan-out, providing dedicated throughput to each consumer. Kinesis supports message payloads up to 1 MB, accommodating the 500 KB requirement. Crucially, it provides strict message ordering within each shard based on a partition key and allows data retention for up to 365 days, satisfying the "more than 3 months" and ordering constraints. The Kinesis Client Library (KCL) and AWS SDKs support multiple programming languages. Why Incorrect Options are Wrong: B. This solution fails because the maximum message size for Amazon SNS and SQS is 256 KB, and the maximum message retention peri

</details>

### 58. dt-533

Which of the following notification endpoints or clients are supported by Amazon Simple Notification Service? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Email.; D. Short Message Service.**

</details>

### 59. ce-536

A company is developing a social media application. The company anticipates rapid and unpredictable growth in users and data volume. The application needs to handle a continuous high volume of user requests. User requests include long-running processes that store large amounts of user-generated content and user profiles in a relational format. The processes must run in a specific order. The company requires an architecture that can scale resources to meet demand spikes without downtime or performance degradation. The company must ensure that the components of the application can evolve independently without affecting other parts of the system. Which combination of AWS services will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application on Amazon Elastic Container Service (Amazon ECS) with the AWS Fargate launch type. Use Amazon RDS as the database. Use Amazon Simple Queue Service (Amazon SQS) to decouple message processing between components.**

This architecture effectively meets all the specified requirements. Amazon ECS with the AWS Fargate launch type provides a serverless container orchestration service that automatically scales to handle unpredictable traffic spikes without managing underlying servers. This is ideal for long-running processes. Amazon RDS satisfies the explicit requirement for a database that stores data in a relational format. Amazon Simple Queue Service (Amazon SQS), specifically using FIFO (First-In-First-Out) queues, decouples application components and ensures that processes are executed in the specific order they are received, which is a critical requirement. This combination creates a scalable, resilient, and loosely coupled system. Why Incorrect Options are Wrong: B: Amazon SNS is a publish/subscribe service, not a queue. It does not guarantee the order in which messages are processed by subscribers

</details>

### 60. dt-542

Your company has been storing a lot of data in Amazon Glacier and has asked for an inventory of what is in there exactly. So you have decided that you need to download a vault inventory. Which of the following statements is incorrect in relation to Vault Operations in Amazon Glacier?

<details><summary>Answer</summary>

**C. You can use Amazon Simple Queue Service (Amazon SQS) notifications to notify you when the job completes.**

</details>

### 61. ce-547

A company is using microservices to build an ecommerce application on AWS. The company wants to preserve customer transaction information after customers submit orders. The company wants to store transaction data in an Amazon Aurora database. The company expects sales volumes to vary throughout each year.

<details><summary>Answer</summary>

**A. Use an Amazon API Gateway REST API to invoke an AWS Lambda function to send transaction data to the Aurora database. Send transaction data to an Amazon Simple Queue Service (Amazon SQS) queue that has a dead-letter queue. Use a second Lambda function to read from the SQS queue and to update the Aurora database.**

This architecture effectively addresses the core requirements of reliability and scalability for variable workloads. Using Amazon SQS to decouple the transaction ingestion from the database write process is a key design pattern. It acts as a buffer, absorbing spikes in order submissions during high-volume sales events. This prevents the Aurora database from being overwhelmed and ensures that no transaction data is lost. The Dead-Letter Queue (DLQ) enhances reliability by capturing any messages that the consumer Lambda function fails to process, allowing for later analysis and reprocessing, thus preserving all transaction information. The serverless components (API Gateway, Lambda) scale automatically with demand. Why Incorrect Options are Wrong: B: This is a synchronous pattern. A sudden spike in traffic could overwhelm the ECS tasks or the Aurora database, leading to failed transactions

</details>

### 62. dt-548

You are deploying an application to track GPS coordinates of delivery trucks in the United States. Coordinates are transmitted from each delivery truck once every three seconds. You need to design an architecture that will enable real-time processing of these coordinates from multiple consumers. Which service should you use to implement data ingestion?

<details><summary>Answer</summary>

**A. Amazon Kinesis.**

</details>

### 63. ce-555

A company runs a container application on a Kubernetes cluster in the company's data center. The application uses Advanced Message Queuing Protocol (AMQP) to communicate with a message queue. The data center cannot scale fast enough to meet the company's expanding business needs. The company wants to migrate the workloads to AWS. Which solution will meet these requirements with the LEAST overhead?

<details><summary>Answer</summary>

**B. Migrate the container application to Amazon EKS. Use Amazon MQ to retrieve the messages.**

The goal is to migrate a containerized application from an on-premises Kubernetes cluster with the least overhead. Amazon EKS is a managed Kubernetes service, providing a direct migration path from an existing Kubernetes environment. This minimizes changes to the container orchestration and deployment configurations. The application uses the AMQP protocol, which is natively supported by Amazon MQ, a managed message broker service. Using Amazon MQ allows the application to connect to the message queue without requiring code changes, thus fulfilling the "least overhead" requirement for both the container platform and the messaging component. Why Incorrect Options are Wrong: A. Migrating from Kubernetes to Amazon ECS requires re-architecting deployment manifests. SQS does not support AMQP, so the application code would need significant changes. This is high overhead. C. Running containers d

</details>

### 64. ce-556 `least-ops`

A company is building a new application that uses multiple serverless architecture components. The application architecture includes an Amazon API Gateway REST API and AWS Lambda functions to manage incoming requests. The company needs a service to send messages that the REST API receives to multiple target Lambda functions for processing. The service must filter messages so each target Lambda function receives only the messages the function needs. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Send the requests from the REST API to an Amazon Simple Notification Service (Amazon SNS) topic. Subscribe multiple Amazon Simple Queue Service (Amazon SQS) queues to the SNS topic. Configure the target Lambda functions to poll the SQS queues.**

This solution describes the "fan-out" serverless design pattern. Amazon SNS is a fully managed publish/subscribe service that is ideal for decoupling microservices and distributing messages to multiple subscribers. By sending the message from API Gateway to a single SNS topic, the message can be fanned out to multiple SQS queues. Crucially, SNS subscription filter policies can be used to ensure that each SQS queue only receives messages with specific attributes, fulfilling the filtering requirement. The SQS queues then provide a durable and reliable buffer for the Lambda functions, which can process the messages asynchronously. This entire architecture is serverless, highly scalable, and has the least operational overhead. Why Incorrect Options are Wrong: B: Using EC2 instances introduces significant operational overhead for managing servers, patching, and scaling, which directly contrad

</details>

### 65. ce-570

A company collects data from sensors. The company needs a cloud-based solution to store and transform the sensor data to make critical decisions. The solution must store the data for up to 2 days. After 2 days, the solution must delete the dat a. The company needs to use the transformeddata in an automated workflow that has manual approval steps. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Load the data into an Amazon Simple Queue Service (Amazon SQS) queue that has a retention period of 2 days. Use an Amazon EventBridge pipe to retrieve data from the queue, transform the data, and pass the data to an AWS Step Functions workflow.**

This solution correctly addresses all requirements. Amazon SQS is ideal for decoupling components and can be configured with a message retention period of up to 14 days, satisfying the 2-day storage and subsequent deletion requirement. Amazon EventBridge Pipes provide a simple, managed way to connect a source (the SQS queue) to a target, with a built-in option to transform the data en route. AWS Step Functions is the designated AWS service for orchestrating workflows, particularly those that require manual intervention, such as approval steps. This architecture is efficient, scalable, and uses the most appropriate services for each task. Why Incorrect Options are Wrong: B: AWS DataSync is a data migration service, not a message queue or temporary data store for sensor data. Using Lambda for a workflow with manual steps is overly complex compared to Step Functions. C: Amazon SNS is a pub/

</details>

### 66. dt-572

You require the ability to analyze a customer's clickstream data on a website so they can do behavioral analysis. Your customer needs to know what sequence of pages and ads their customer clicked on. This data will be used in real time to modify the page layouts as customers click through the site to increase stickiness and advertising click-through. Which option meets the requirements for captioning and analyzing this data?

<details><summary>Answer</summary>

**B. Push web clicks by session to Amazon Kinesis and analyze behavior using Kinesis workers.**

</details>

### 67. ce-573

A solutions architect is designing the architecture for a web application that has a frontend and a backend. The backend services must receive data from the frontend services for processing. The frontend must manage access to the application by using API keys. The backend must scale without affecting the frontend. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an Amazon API Gateway REST API as the frontend to direct traffic to an Amazon Simple Queue Service (Amazon SQS) queue. Use Amazon Elastic Container Service (Amazon ECS) on AWS Fargate as the backend to read from the queue.**

This solution correctly addresses all requirements. An Amazon API Gateway REST API is the most suitable choice for the frontend as it provides built-in support for API keys and usage plans, directly meeting the access management requirement. Integrating API Gateway with an Amazon SQS queue effectively decouples the frontend from the backend. This allows the backend services to pull messages from the queue and scale independently without impacting the frontend's availability or performance. Amazon ECS on AWS Fargate is a serverless container compute engine that can run the backend services, automatically scaling the number of tasks based on the SQS queue depth, thus fulfilling the scaling requirement. Why Incorrect Options are Wrong: A. Amazon API Gateway HTTP APIs do not have the same built-in support for API keys as REST APIs, making them less suitable for this specific requirement. C.

</details>

### 68. dt-573

What happens when you create a topic on Amazon SNS?

<details><summary>Answer</summary>

**B. An ARN (Amazon Resource Name) is created.**

</details>

### 69. et-587

A company is designing a solution to capture customer activity in different web applications to process analytics and make predictions. Customer activity in the web applications is unpredictable and can increase suddenly. The company requires a solution that integrates with other web applications. The solution must include an authorization step for security purposes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure an Amazon API Gateway endpoint in front of an Amazon Kinesis Data Firehose that stores the information that the company receives in an Amazon S3 bucket. Use an API Gateway Lambda authorizer to resolve authorization.**

Amazon API Gateway: It provides a fully managed service for creating, publishing, maintaining, monitoring, and securing APIs at any scale. It allows you to expose the capabilities of your backend services as APIs. Amazon Kinesis Data Firehose: It can capture and load streaming data into storage services such as Amazon S3. It is well-suited for scenarios where you need to ingest and store large volumes of streaming data. API Gateway Lambda Authorizer: It allows you to control access to your APIs using Lambda functions. It's used to resolve authorization before allowing access to the API.

</details>

### 70. dt-588

You are architecting an auto-scalable batch processing system using video processing pipelines and Amazon Simple Queue Service (Amazon SQS) for a customer. You are unsure of the limitations of SQS and need to find out. What do you think is a correct statement about the limitations of Amazon SQS?

<details><summary>Answer</summary>

**B. It supports an unlimited number of queues and unlimited number of messages per queue for each user but automatically deletes messages that have been in the queue for more than 4 days.**

</details>

### 71. ce-602

An ecommerce company wants to collect user clickstream data from the company's website for real- time analysis. The website experiences fluctuating traffic patterns throughout the day. The company needs a scalable solution that can adapt to varying levels of traffic. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use a data stream in Amazon Kinesis Data Streams in on-demand mode to capture the clickstream data. Use AWS Lambda to process the data in real time.**

Amazon Kinesis Data Streams is designed for real-time ingestion of high-volume streaming data, such as website clickstreams. The on-demand capacity mode automatically manages the scaling of stream capacity (shards) in response to fluctuating traffic, eliminating the need for manual provisioning. This directly addresses the requirements for a scalable solution that adapts to varying traffic levels. AWS Lambda integrates natively with Kinesis Data Streams, allowing for serverless, real-time processing of incoming data records as they arrive. This combination provides a highly scalable, cost-effective, and fully managed solution for real-time analysis. Why Incorrect Options are Wrong: B: Amazon Data Firehose is a data delivery service that batches records, introducing latency (typically 60 seconds minimum). AWS Glue is primarily a batch ETL service, making this combination unsuitable for re

</details>

### 72. ce-622

A company hosts an industrial control application that receives sensor input through Amazon Kinesis Data Streams. The application needs to support new sensors for real-time anomaly detection in monitored equipment. The company wants to integrate new sensors in a loosely-coupled, fully managed, and serverless way. The company cannot modify the application code. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Forward the existing stream in Kinesis Data Streams to Amazon Managed Service for Apache Flink for anomaly detection. Use a second stream in Kinesis Data Streams to send the Flink output to the application.**

The solution requires a real-time, fully managed, and serverless approach for anomaly detection on a Kinesis Data Stream. Amazon Managed Service for Apache Flink is a fully managed, serverless service designed for real-time, complex stream processing, including anomaly detection. It can natively use a Kinesis Data Stream as a source for input and another Kinesis Data Stream as a sink for output. This architecture creates a loosely-coupled system that inserts the new anomaly detection logic without modifying the existing application's code, assuming the application can be reconfigured to read from the new output stream. Why Incorrect Options are Wrong: B. This architecture is not real-time. Kinesis Data Firehose introduces buffering latency, and Amazon Redshift Spectrum is a query service for data at rest in S3, not a stream processing engine. C. Using Amazon EC2 instances is not a server

</details>

### 73. ce-628

A company is building a gaming application that needs to send unique events to multiple leaderboards, player matchmaking systems, and authentication services concurrently. The company requires an AWS-based event-driven system that delivers events in order and supports a publish- subscribe model. The gaming application must be the publisher, and the leaderboards, matchmaking systems, and authentication services must be the subscribers. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Amazon Simple Notification Service (Amazon SNS) FIFO topics**

The solution requires a publish-subscribe (pub/sub) model that can send events to multiple, independent systems concurrently while strictly preserving the order of events. Amazon SNS FIFO topics are specifically designed for this purpose. They provide a pub/sub messaging pattern with strict message ordering and exactly-once delivery to subscribed Amazon SQS FIFO queues. The gaming application can publish an event once to the SNS FIFO topic, and SNS will ensure it is delivered in the correct sequence to all subscribers (leaderboards, matchmaking, etc.), meeting all the stated requirements. Why Incorrect Options are Wrong: A. Amazon EventBridge event buses do not guarantee the order in which events are delivered to targets, which violates the "in order" requirement. C. Amazon SNS standard topics provide a pub/sub model but only offer best-effort ordering, meaning the sequence of messages i

</details>

### 74. ce-632

A company runs game applications on AWS. The company needs to collect, visualize, and analyze telemetry data from the company's game servers. The company wants to gain insights into the behavior, performance, and health of game servers in near real time. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Streams to collect telemetry data. Use Amazon Managed Service for Apache Flink to process the data in near real time and publish custom metrics to Amazon CloudWatch. Use Amazon CloudWatch to create dashboards and alarms from the custom metrics.**

This solution provides a complete, serverless, and near real-time analytics pipeline. Amazon Kinesis Data Streams is the ideal service for ingesting high-volume, continuous telemetry data from game servers. Amazon Managed Service for Apache Flink is purpose-built for processing and analyzing such data streams in near real-time. It can perform computations (like aggregations or anomaly detection) and publish the results as custom metrics to Amazon CloudWatch. CloudWatch is the native AWS service for monitoring, creating dashboards for visualization, and setting alarms to monitor the health and performance of the game servers, fulfilling all requirements of the scenario. Why Incorrect Options are Wrong: B: AWS Glue is a serverless ETL service primarily designed for batch data processing, which does not meet the "near real time" analysis requirement. C: Amazon Athena is an interactive, ad-h

</details>

### 75. et-636

A development team is creating an event-based application that uses AWS Lambda functions. Events will be generated when files are added to an Amazon S3 bucket. The development team currently has Amazon Simple Notification Service (Amazon SNS) configured as the event target from Amazon S3. What should a solutions architect do to process the events from Amazon S3 in a scalable way?

<details><summary>Answer</summary>

**C. Create an SNS subscription that sends the event to Amazon Simple Queue Service (Amazon SQS). Configure the SOS queue to trigger a Lambda function.**

</details>

### 76. ce-652

A company needs a solution to ingest streaming sensor data from 100,000 devices, transform the data in near real time, and load the data into Amazon S3 for analysis. The solution must be fully managed, scalable, and maintain sub-second ingestion latency.

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Streams to ingest the data. Use Amazon Managed Service for Apache Flink to process the data in near real time. Use an Amazon Data Firehose stream to send processed data to Amazon S3.**

This solution presents a canonical, fully managed architecture for real-time streaming data processing on AWS. Amazon Kinesis Data Streams is designed for ingesting high-volume, high-velocity data from numerous sources like IoT devices with sub-second latency. Amazon Managed Service for Apache Flink provides a powerful, serverless framework for performing complex transformations on this streaming data in near real time. Finally, Amazon Data Firehose is the simplest, fully managed way to take the processed stream and reliably load it into Amazon S3 for long-term storage and analysis. This combination directly addresses all requirements for a scalable, managed, low-latency solution. Why Incorrect Options are Wrong: B: Amazon SQS is a message queuing service, not a streaming data platform. It is better suited for decoupling applications than for continuous, ordered, real-time data stream in

</details>

### 77. ce-658

A company is designing an application on AWS that provides real-time dashboards. The dashboard data comes from on-premises databases that use a variety of schemas and formats. The company needs a solution to transfer and transform the data to AWS with minimal latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Integrate the dashboard with Amazon Managed Streaming for Apache Kafka (Amazon MSK) to transfer and transform the data from the on-premises databases to the dashboards.**

The core requirements are to transfer data from various on-premises databases, transform it, and feed it into real-time dashboards with minimal latency. Amazon Managed Streaming for Apache Kafka (Amazon MSK) is an ideal solution for this use case. Apache Kafka is a distributed streaming platform designed for high-throughput, low-latency data pipelines. Using Kafka Connect, data can be ingested from various on-premises databases (Change Data Capture). The data streams can then be processed and transformed in real-time using frameworks like Kafka Streams or Apache Flink before being consumed by the dashboard application. This architecture directly supports the need for a continuous, low-latency data flow from heterogeneous sources. Why Incorrect Options are Wrong: B. Use Amazon Data Firehose...: Firehose delivers data in batches, with a minimum buffer interval of 60 seconds. The proposed p

</details>

### 78. dt-673 `cost`

A company hosts its static website by using Amazon S3. The company wants to add a contact form to its webpage. The contact form will have dynamic server-side components for users to input their name, email address, phone number, and user message. The company anticipates that there will be fewer than 100 site visits each month. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create an Amazon API Gateway endpoint that returns the contact form from an AWS Lambda function. Configure another Lambda function on the API Gateway to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic.**

</details>

### 79. dt-681

A company has an application that ingests incoming messages. Dozens of other applications and microservices then quickly consume these messages. The number of messages varies drastically and sometimes increases suddenly to 100,000 each second. The company wants to decouple the solution and increase scalability. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Publish the messages to an Amazon Simple Notification Service (Amazon SNS) topic with multiple Amazon Simple Queue Service (Amazon SOS) subscriptions. Configure the consumer applications to process the messages from the queues.**

</details>

### 80. dt-682

An application development team is designing a microservice that will convert large images to smaller, compressed images. When a user uploads an image through the web interface, the microservice should store the image in an Amazon S3 bucket, process and compress the image with an AWS Lambda function, and store the image in its compressed form in a different S3 bucket. A solutions architect needs to design a solution that uses durable, stateless components to process the images automatically. Which combination of actions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Create an Amazon Simple Queue Service (Amazon SQS) queue. Configure the S3 bucket to send a notification to the SQS queue when an image is uploaded to the S3 bucket.; B. Configure the Lambda function to use the Amazon Simple Queue Service (Amazon SQS) queue as the invocation source. When the SQS message is successfully processed, delete the message in the queue.**

</details>

### 81. ce-689

A company is moving its data management application to AWS. The company wants to transition to an event-driven architecture. The architecture needs to be more distributed and to use serverless concepts while performing the different aspects of the workflow. The company also wants to minimize operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Build out the workflow in AWS Step Functions. Use Step Functions to create a state machine. Use the state machine to invoke AWS Lambda functions to process the workflow steps.**

The requirements call for an event-driven, distributed, serverless workflow with minimal operational overhead. The combination of AWS Step Functions and AWS Lambda is the ideal solution. AWS Step Functions is a serverless orchestrator that allows you to build and visualize workflows (state machines) composed of discrete steps. Each step can invoke an AWS Lambda function to perform a specific task. This architecture is inherently event-driven, distributed, and fully serverless, as both services are managed by AWS. This eliminates the need to manage any underlying infrastructure, thus minimizing operational overhead and perfectly meeting all stated requirements. Why Incorrect Options are Wrong: A. AWS Glue is a managed ETL service. While it has workflow capabilities, it is specialized for data integration tasks, not for general-purpose application orchestration. B. Using Amazon EC2 instanc

</details>

### 82. dt-689

A company is designing an application. The application uses an AWS Lambda function to receive information through Amazon API Gateway and to store the information in an Amazon Aurora PostgreSQL database. During the proof-of-concept stage, the company has to increase the Lambda quotas significantly to handle the high volumes of data that the company needs to load into the database. A solutions architect must recommend a new design to improve scalability and minimize the configuration effort. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Set up two Lambda functions. Configure one function to receive the information. Configure the other function to load the information into the database. Integrate the Lambda functions by using an Amazon Simple Queue Service (Amazon SQS) queue.**

</details>

### 83. ce-718

A company wants to build a serverless application in which multiple microservices need to exchange messages. The company needs to ensure that messages that the microservices send to one another are processed exactly once in the exact order the messages are sent. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**A. Create an Amazon SQS FIFO queue. Configure the microservices to use the SQS queue to exchange messages.**

Amazon SQS FIFO (First-In-First-Out) queues are specifically designed to meet the requirements of exactly-once message processing and strict message ordering. By using a FIFO queue, the microservices can exchange messages with the guarantee that they will be delivered once and in the precise sequence they were sent. As a fully managed, serverless service, SQS provides the most operationally efficient solution compared to managing streaming infrastructure or using services that don't guarantee order. Why Incorrect Options are Wrong: B. Standard Amazon SNS topics do not guarantee message ordering. While SNS FIFO topics exist, they require an SQS FIFO queue as a subscriber to preserve order. C. Amazon SQS standard queues provide at-least-once delivery and best-effort ordering, which does not meet the strict "exactly-once" and "exact order" requirements. D. Amazon MSK is a managed service fo

</details>

### 84. ce-721

A company is building an ecommerce platform that will allow customers to place orders online. Customer traffic varies significantly. An order-processing microservice is running on a group of Amazon EC2 instances. A solutions architect must ensure that the application remains responsive and decoupled from the frontend. The application must also be able to reprocess orders that the application fails to process on the first attempt. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an Amazon SQS queue to integrate the frontend and the order-processing microservice. Configure the frontend to send messages to the queue. Configure the EC2 instances to process messages from the queue.**

Using an Amazon SQS queue decouples the frontend from the order-processing microservice. The frontend can quickly send order messages to the queue and remain responsive to the customer, even if the backend is busy. The EC2 instances can then pull messages from the queue and process them independently. This architecture naturally handles variable traffic by allowing orders to queue up during spikes. For failed orders, SQS can be configured with a dead-letter queue (DLQ) to automatically capture and store messages that fail processing, allowing for later analysis and reprocessing. Why Incorrect Options are Wrong: A. An Application Load Balancer does not decouple the frontend. If the backend instances are overwhelmed, the frontend will still experience errors or timeouts, failing the responsiveness requirement. C. Direct HTTPS connections create a tightly coupled system that is not resilien

</details>

### 85. ce-730

An ecommerce company runs a transaction processing system within a large application on a set of Amazon EC2 instances behind an Application Load Balancer ALB. The transaction process handles order creation, payment initiation, and inventory updates. The company has observed performance issues in the transaction workflow as the volume of transactions has increased. The company wants to re-architect the transaction process to introduce horizontal scalability and to improve cost efficiency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Decouple the transaction system into microservices that run on AWS Lambda functions. Expose the microservices through a central Amazon API Gateway REST API. Use Amazon SQS queues to decouple order creation and payment processing.**

This solution directly addresses the requirements for horizontal scalability and cost efficiency by adopting a serverless, microservices architecture. Decoupling the monolithic application into discrete AWS Lambda functions for each task (order creation, payment) allows each component to scale independently and automatically based on demand. Amazon SQS queues provide a durable buffer between services, improving resilience and enabling asynchronous processing. Amazon API Gateway provides a managed, scalable entry point for the microservices. This serverless approach is highly cost-efficient, as you only pay for the compute time you consume, eliminating costs associated with idle EC2 instances. Why Incorrect Options are Wrong: B. The Kubernetes Vertical Pod Autoscaler adjusts a pod's resource requests (CPU/memory), which is vertical scaling. Horizontal scaling (more pods) is handled by the

</details>

### 86. dt-732

A company plans to host a survey website on AWS. The company anticipates an unpredictable amount of traffic. This traffic results in asynchronous updates to the database. The company wants to ensure that writes to the database hosted on AWS do not get dropped. How should the company write its application to handle these database requests?

<details><summary>Answer</summary>

**D. Use Amazon Simple Queue Service (Amazon SQS) FIFO queues for capturing the writes and draining the queue as each write is made to the database.**

</details>

### 87. dt-737

A development team is collaborating with another company to create an integrated product. The other company needs to access an Amazon Simple Queue Service (Amazon SQS) queue that is contained in the development team's account. The other company wants to poll the queue without giving up its own account permissions to do so. How should a solutions architect provide access to the SQS queue?

<details><summary>Answer</summary>

**C. Create an SQS access policy that provides the other company access to the SQS queue.**

</details>

### 88. dt-738 `cost`

A company is developing a video conversion application hosted on AWS. The application will be available in two tiers: a free tier and a paid tier. Users in the paid tier will have their videos converted first and then the free tier users will have their videos converted. Which solution meets these requirements and is MOST cost-effective?

<details><summary>Answer</summary>

**D. Two standard Amazon Simple Queue Service (Amazon SQS) queues with one for the paid tier and one for the free tier.**

</details>

### 89. ce-753

A solutions architect is migrating an on-premises application to AWS. The application currently runs on containers. The components of the application are loosely coupled. The application consumes messages from a message queue. The solutions architect needs to design a new architecture for the application on AWS. The solutions architect wants to use fully managed AWS services for the new architecture. The new architecture must provide unlimited scalability for the message queue's throughput. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon SQS to create a new message queue. Subscribe the SQS queue to an Amazon SNS topic. Use Amazon ECS containers on AWS Fargate to consume messages from the message queue.**

The solution requires fully managed services for a containerized application with a message queue that has unlimited scalability. Amazon SQS is a fully managed message queue that offers virtually unlimited throughput and scales automatically. Amazon ECS with AWS Fargate is a fully managed, serverless compute engine for containers, eliminating the need to manage underlying servers. This combination perfectly meets the requirements for a fully managed, highly scalable, container-based architecture. Subscribing the SQS queue to an SNS topic is a common and valid fan-out pattern. Why Incorrect Options are Wrong: A. Using EC2 Reserved Instances means the underlying servers must be managed, which is not a "fully managed" compute solution compared to Fargate. B. Amazon MQ is a managed message broker, but its throughput is limited by the chosen broker instance size and does not offer the "unlimi

</details>

### 90. dt-759

A mobile gaming company runs application servers on Amazon EC2 instances. The servers receive updates from players every 15 minutes. The mobile game creates a JSON object of the progress made in the game since the last update, and sends the JSON object to an Application Load Balancer. As the mobile game is played, game updates are being lost. The company wants to create a durable way to get the updates in order. What should a solutions architect recommend to decouple the system?

<details><summary>Answer</summary>

**C. Use Amazon Simple Queue Service (Amazon SQS) FIFO queues to capture the data and EC2 instances to process the messages in the queue.**

</details>

### 91. dt-765

A company has an API-based inventory reporting application running on Amazon EC2 instances. The application stores information in an Amazon DynamoDB table. The company's distribution centers have an on-premises shipping application that calls an API to update the inventory before printing shipping labels. The company has been experiencing application interruptions several times each day, resulting in lost transactions. What should a solutions architect recommend to improve application resiliency?

<details><summary>Answer</summary>

**D. Modify the application to send inventory updates using Amazon Simple Queue Service (Amazon SQS).**

</details>

### 92. ce-817 `cost`

A company is building a serverless web application with multiple interdependent workflows that millions of users worldwide will access. The application needs to handle bursts of traffic. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Deploy an Amazon API Gateway HTTP API with a usage plan and throttle settings. Use AWS Step Functions with an Express Workflow.**

The scenario requires a highly scalable, serverless solution for interdependent workflows that is also cost-effective for millions of users and traffic bursts. AWS Step Functions Express Workflows are designed for high-volume, short-duration, event-driven workloads, making them significantly more cost-effective than Standard Workflows for this use case. Their pricing is based on execution count, duration, and memory, which is ideal for handling millions of requests. Amazon API Gateway HTTP APIs are a low-latency and cost-effective choice compared to REST APIs, suitable for serving high-volume traffic. Implementing throttle settings is a crucial best practice to protect backend services from being overwhelmed during traffic bursts and to manage costs. This combination provides the most scalable and cost-effective architecture for the described requirements. Why Incorrect Options are Wrong

</details>

### 93. ce-819

A company wants to optimize costs for its AWS infrastructure. The company wants to receive notifications when actual costs or forecasted costs exceed a specified budget. The company does not want to develop a custom solution. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a budget in AWS Budgets that has a specified cost threshold. Configure AWS Budgets to send budget alerts to an Amazon Simple Notification Service (Amazon SNS) topic. Use AWS Cost Explorer to monitor costs.**

AWS Budgets is the designated service for setting custom cost and usage budgets and receiving alerts. It allows users to configure notifications when costs or usage exceed, or are forecasted to exceed, a specified threshold. This directly addresses the requirement for alerts on both actual and forecasted costs. Notifications can be sent to an Amazon Simple Notification Service (Amazon SNS) topic, which can then distribute the alert to subscribers (e.g., email, SMS). This is a native, managed feature, avoiding the need for a custom solution. AWS Cost Explorer is the appropriate tool for visualizing and analyzing cost trends, complementing the alerting function of AWS Budgets. Why Incorrect Options are Wrong: A. This is incorrect because AWS Trusted Advisor provides optimization recommendations, not budget alerts. It also proposes a custom machine learning solution, which the requirements

</details>

### 94. ce-825 `cost`

A company uses Amazon S3 to host its static website. The company wants to add a contact form to the webpage. The contact form will have dynamic server-side components for users to input their name, email address, phone number, and user message. The company expects fewer than 100 site visits each month. The contact form must notify the company by email when a customer fills out the form. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create an Amazon API Gateway endpoint that returns the contact form from an AWS Lambda function. Configure another Lambda function on the API Gateway to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic.**

This solution represents a classic serverless pattern that is highly cost-effective for low and infrequent traffic. Amazon API Gateway provides a managed HTTP endpoint for the form submission. It triggers an AWS Lambda function to process the form data. Lambda's pay-per-request model, combined with its generous free tier, means costs will be minimal or zero for fewer than 100 submissions per month. The Lambda function then publishes a message to an Amazon Simple Notification Service (SNS) topic, which can directly send an email notification to a subscribed company email address. This architecture requires no server management and perfectly aligns with the cost-optimization requirement. Why Incorrect Options are Wrong: A. Hosting a container on Amazon ECS, even with AWS Fargate, incurs higher costs than Lambda for this low-traffic scenario and is overly complex for a simple contact form.

</details>

### 95. ce-970

A company runs an application that consists of multiple microservices. The company mandates that the microservices use messages to communicate with each other. The application must archive the microservices' messages for 30 days. Which solution will meet these requirements with the LEAST amount of development effort?

<details><summary>Answer</summary>

**A. Use an Amazon EventBridge event bus to route messages between the microservices. Use message filtering to ensure that each microservice receives only messages that are relevant to each microservice. Create an archive in Amazon EventBridge to store the messages for 30 days.**

The requirements are message-based communication, archiving for 30 days, and minimal development effort. Amazon EventBridge is an event bus service ideal for decoupling microservices. It has a native "Archive" feature that can store all or filtered events for a specified retention period, which can be set to 30 days. This is a simple configuration step. EventBridge rules can filter and route messages to specific microservices. This solution directly meets all requirements with configuration rather than custom code, representing the least development effort. Why Incorrect Options are Wrong: B. Amazon SQS queues have a maximum message retention period of 14 days, which does not meet the 30-day archiving requirement. C. This requires adding a component like AWS Kinesis Data Firehose or a Lambda function to write SNS messages to S3, increasing development effort. D. This solution requires bu

</details>
