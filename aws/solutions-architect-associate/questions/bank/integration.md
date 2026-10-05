# Application integration — queues, topics, events, streams, APIs

26 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. gh-7

A company has an application that ingests incoming messages. Dozens of other applications and microservices then quickly consume these messages. The number of messages varies drastically and sometimes increases suddenly to 100,000 each second. The company wants to decouple the solution and increase scalability.
Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Publish the messages to an Amazon Simple Notification Service (Amazon SNS) topic with multiple Amazon Simple Queue Service (Amazon SOS) subscriptions. Configure the consumer applications to process the messages from the queues.**

A good practice is to also add message attributes when publishing to SNS. Each SQS subscription can have a filter policy that matches only the messages it cares about, so that only relevant messages are delivered to each SQS queue, and consumers only see/process what they need.

an SQS queue can handle a maximum of 3,000 messages per second. However, you can request higher throughput by contacting AWS Support. AWS can increase the message throughput for your queue beyond the default limits in increments of 300 messages per second, up to a maximum of 10,000 messages per second.

It's important to note that the maximum number of messages per second that a queue can handle is not the same as the maximum number of requests per second that the SQS API can handle. The SQS API is designed to handle a high volume of requests per second, so it can be used to send messages to your queue at a rate that exceeds the maximum message throughput of the queue.

</details>

### 2. wl-7

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

### 3. gh-10

A company is building an ecommerce web application on AWS. The application sends information about new orders to an Amazon API Gateway REST API to process. The company wants to ensure that orders are processed in the order that they are received.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use an API Gateway integration to send a message to an Amazon Simple Queue Service (Amazon SQS) FIFO queue when the application receives an order. Configure the SQS FIFO queue to invoke an AWS Lambda function for processing**

Use an API Gateway integration to send a message to an Amazon Simple Queue Service (Amazon SQS) FIFO queue when the application receives an order. Configure the SQS FIFO queue to invoke an AWS Lambda function for processing.

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

### 5. gh-25

A company is designing an application. The application uses an AWS Lambda function to receive information through Amazon API Gateway and to store the information in an Amazon Aurora PostgreSQL database.
During the proof-of-concept stage, the company has to increase the Lambda quotas significantly to handle the high volumes of data that the company needs to load into the database. A solutions architect must recommend a new design to improve scalability and minimize the configuration effort.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Set up two Lambda functions. Configure one function to receive the information. Configure the other function to load the information into the database. Integrate the Lambda functions by using an Amazon Simple Queue Service (Amazon SQS) queue.**

"By dividing the functionality into two Lambda functions, one for receiving the information and the other for loading it into the database, you can independently scale and optimize each function based on their specific requirements. This approach allows for more efficient resource allocation and reduces the potential impact of high volumes of data on the overall system.

</details>

### 6. gh-41 `least-ops`

A company's application integrates with multiple software-as-a-service (SaaS) sources for data collection. The company runs Amazon EC2 instances to receive the data and to upload the data to an Amazon S3 bucket for analysis. The same EC2 instance that receives and uploads the data also sends a notification to the user when an upload is complete. The company has noticed slow application performance and wants to improve the performance as much as possible.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Amazon AppFlow flow to transfer data between each SaaS source and the S3 bucket. Configure an S3 event notification to send events to an Amazon Simple Notification Service (Amazon SNS) topic when the upload to the S3 bucket is complete.**

Amazon AppFlow is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift.
The use of Appflow helps to remove the ec2 as the middle layer which slows down the process of data transmission and introduce an additional variable.
Appflow is also a fully managed AWS service, thus reducing the operational overhead.

</details>

### 7. gh-45

A company has a data ingestion workflow that consists of the following:
• An Amazon Simple Notification Service (Amazon SNS) topic for notifications about new data deliveries
• An AWS Lambda function to process the data and record metadata
The company observes that the ingestion workflow fails occasionally because of network connectivity issues. When such a failure occurs, the Lambda function does not ingest the corresponding data unless the company manually reruns the job.
Which combination of actions should a solutions architect take to ensure that the Lambda function ingests all data in the future? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon Simple Queue Service (Amazon SQS) queue, and subscribe it to the SNS topic.**

E. Modify the Lambda function to read from an Amazon Simple Queue Service (Amazon SQS) queue.

B. Create an Amazon Simple Queue Service (Amazon SQS) queue, and subscribe it to the SNS topic. This will decouple the ingestion workflow and provide a buffer to temporarily store the data in case of network connectivity issues.

E. Modify the Lambda function to read from an Amazon Simple Queue Service (Amazon SQS) queue. This will allow the Lambda function to process the data from the SQS queue at its own pace, decoupling the data ingestion from the data delivery and providing more flexibility and fault tolerance.

</details>

### 8. gh-201

A company is developing a marketing communications service that targets mobile app users. The company needs to send its users confirmation messages with Short Message Service (SMS). The users must be able to reply to the SMS messages. The company must store the responses for a year for analysis.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Build an Amazon Pinpoint journey. Configure Amazon Pinpoint to send events to an Amazon Kinesis data stream for analysis and archiving.**

Amazon Pinpoint is a fully managed service for sending messages to mobile app users. With Amazon Pinpoint journeys, you can create multi-step campaigns to engage with users. By configuring Amazon Pinpoint to send events to an Amazon Kinesis data stream, you can capture the responses for further analysis and archiving. This solution provides a comprehensive approach to managing SMS messages and their responses in a scalable and efficient manner.

</details>

### 9. gh-206 `least-ops`

A company wants to manage Amazon Machine Images (AMIs). The company currently copies AMIs to the same AWS Region where the AMIs were created. The company needs to design an application that captures AWS API calls and sends alerts whenever the Amazon EC2 CreateImage API operation is called within the company’s account.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create an Amazon EventBridge (Amazon CloudWatch Events) rule for the CreateImage API call. Configure the target as an Amazon Simple Notification Service (Amazon SNS) topic to send an alert when a CreateImage API call is detected.**

Amazon EventBridge (formerly CloudWatch Events) provides a simple and efficient way to respond to events in AWS services. By creating an EventBridge rule specifically for the CreateImage API call, you can easily configure an SNS topic as the target to send alerts when the event is detected.

</details>

### 10. gh-211

A company hosts multiple production applications. One of the applications consists of resources from Amazon EC2, AWS Lambda, Amazon RDS, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS) across multiple AWS Regions. All company resources are tagged with a tag name of “application” and a value that corresponds to each application. A solutions architect must provide the quickest solution for identifying all of the tagged components.
Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Run a query with the AWS Resource Groups Tag Editor to report on the resources globally with the application tag.**

AWS Resource Groups Tag Editor allows you to search and filter resources based on tags across multiple AWS Regions.
It provides a centralized view of resources and their corresponding tags, making it easier to identify and manage resources with specific tags.
This option provides a quick and efficient way to report on resources with the application tag globally.

</details>

### 11. gh-225 `least-ops` `availability`

A media company collects and analyzes user activity data on premises. The company wants to migrate this capability to AWS. The user activity data store will continue to grow and will be petabytes in size. The company needs to build a highly available data ingestion solution that facilitates on-demand analytics of existing data and new data with SQL.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Send activity data to an Amazon Kinesis Data Firehose delivery stream. Configure the stream to deliver the data to an Amazon Redshift cluster.**

Amazon Kinesis Data Firehose: It is a fully managed service that simplifies the delivery of streaming data to destinations such as Amazon S3, Amazon Redshift, or Amazon Elasticsearch Service. It handles the scaling, buffering, and delivery of data.

Amazon Redshift: It is a fully managed, petabyte-scale data warehouse service. It is optimized for high-performance analysis using standard SQL queries.

Least Operational Overhead: Kinesis Data Firehose takes care of many operational aspects, including scaling and buffering, reducing the operational overhead on your part. Configuring it to deliver data to Amazon Redshift provides a streamlined and managed solution.

</details>

### 12. gh-255

A company has an ecommerce checkout workflow that writes an order to a database and calls a service to process the payment. Users are experiencing timeouts during the checkout process. When users resubmit the checkout form, multiple unique orders are created for the same desired transaction.
How should a solutions architect refactor this workflow to prevent the creation of multiple orders?

<details><summary>Answer</summary>

**D. Store the order in the database. Send a message that includes the order number to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Set the payment service to retrieve the message and process the order. Delete the message from the queue.**

Storing the order in the database first ensures that the order information is saved, even if the payment processing is delayed or fails.
Sending a message to an SQS FIFO queue with the order number ensures that the processing is idempotent. If the same order number is sent multiple times, SQS guarantees that the messages are processed in order and only once.

</details>

### 13. gh-267 `least-ops`

A company has one million users that use its mobile app. The company must analyze the data usage in near-real time. The company also must encrypt the data in near-real time and must store the data in a centralized location in Apache Parquet format for further processing.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an Amazon Kinesis Data Firehose delivery stream to store the data in Amazon S3. Create an Amazon Kinesis Data Analytics application to analyze the data.**

</details>

### 14. gh-285 `cost`

A company hosts its static website by using Amazon S3. The company wants to add a contact form to its webpage. The contact form will have dynamic server-side components for users to input their name, email address, phone number, and user message. The company anticipates that there will be fewer than 100 site visits each month.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create an Amazon API Gateway endpoint with an AWS Lambda backend that makes a call to Amazon Simple Email Service (Amazon SES).**

Amazon API Gateway: Acts as the endpoint for the contact form. It enables you to create, publish, maintain, monitor, and secure APIs at any scale.
AWS Lambda: Serves as the backend for handling the dynamic components of the contact form. Lambda allows you to run code without provisioning or managing servers.
Amazon Simple Email Service (Amazon SES): Can be used to send emails, making it suitable for handling the form submissions.
This serverless architecture eliminates the need for managing and maintaining infrastructure, and costs are based on actual usage, making it cost-effective for low-traffic scenarios.

</details>

### 15. gh-292

A company is preparing a new data platform that will ingest real-time streaming data from multiple sources. The company needs to transform the data before writing the data to Amazon S3. The company needs the ability to use SQL to query the transformed data.
Which solutions will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Streams to stream the data. Use Amazon Kinesis Data Analytics to transform the data. Use Amazon Kinesis Data Firehose to write the data to Amazon S3. Use Amazon Athena to query the transformed data from Amazon S3.**

B. Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to stream the data. Use AWS Glue to transform the data and to write the data to Amazon S3. Use Amazon Athena to query the transformed data from Amazon S3.

Use Amazon Kinesis Data Streams to stream the data.
Use Amazon Kinesis Data Analytics to transform the data.
Use Amazon Kinesis Data Firehose to write the data to Amazon S3.
Use Amazon Athena to query the transformed data from Amazon S3.
This option uses the Kinesis suite for streaming, analytics, and Firehose for writing to S3, with Athena for querying.

Use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to stream the data.
Use AWS Glue to transform the data and write the data to Amazon S3.
Use Amazon Athena to query the transformed data from Amazon S3.
This option leverages Amazon MSK for streaming, AWS Glue for transformation, and Athena for querying, providing a comprehensive solution.

</details>

### 16. gh-316

A company uses an Amazon EC2 instance to run a script to poll for and process messages in an Amazon Simple Queue Service (Amazon SQS) queue. The company wants to reduce operational costs while maintaining its ability to process a growing number of messages that are added to the queue.
What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Migrate the script on the EC2 instance to an AWS Lambda function with the appropriate runtime.**

AWS Lambda: Lambda is a serverless computing service that allows you to run code without provisioning or managing servers. It automatically scales based on the number of incoming requests.
Cost-Efficiency: With Lambda, you only pay for the compute time consumed during code execution. This can be more cost-effective than running and maintaining an EC2 instance, especially for sporadic or event-driven workloads.
Automatic Scaling: Lambda automatically scales based on the number of incoming events. As the number of messages in the SQS queue grows, Lambda can scale out to handle the increased workload.
Event-Driven: Lambda is well-suited for event-driven architectures, making it a good fit for scenarios where messages are added to an SQS queue.

</details>

### 17. gh-322

A solutions architect is designing a multi-tier application for a company. The application's users upload images from a mobile device. The application generates a thumbnail of each image and returns a message to the user to confirm that the image was uploaded successfully.
The thumbnail generation can take up to 60 seconds, but the company wants to provide a faster response time to its users to notify them that the original image was received. The solutions architect must design the application to asynchronously dispatch requests to the different application tiers.
What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Simple Queue Service (Amazon SQS) message queue. As images are uploaded, place a message on the SQS queue for thumbnail generation. Alert the user through an application message that the image was received.**

Amazon SQS (Simple Queue Service): SQS is a fully managed message queuing service that enables decoupling of the components of a cloud application. By creating an SQS message queue, the image upload process can place messages in the queue for thumbnail generation.

</details>

### 18. gh-323 `availability`

A company’s facility has badge readers at every entrance throughout the building. When badges are scanned, the readers send a message over HTTPS to indicate who attempted to access that particular entrance.
A solutions architect must design a system to process these messages from the sensors. The solution must be highly available, and the results must be made available for the company’s security team to analyze.
Which system architecture should the solutions architect recommend?

<details><summary>Answer</summary>

**B. Create an HTTPS endpoint in Amazon API Gateway. Configure the API Gateway endpoint to invoke an AWS Lambda function to process the messages and save the results to an Amazon DynamoDB table.**

</details>

### 19. gh-344

A company has a Java application that uses Amazon Simple Queue Service (Amazon SQS) to parse messages. The application cannot parse messages that are larger than 256 KB in size. The company wants to implement a solution to give the application the ability to parse messages as large as 50 MB.
Which solution will meet these requirements with the FEWEST changes to the code?

<details><summary>Answer</summary>

**A. Use the Amazon SQS Extended Client Library for Java to host messages that are larger than 256 KB in Amazon S3.**

Amazon SQS Extended Client Library for Java: This library is specifically designed to handle larger messages in Amazon SQS by transparently offloading them to Amazon S3. It allows you to send a reference to the S3 object in the SQS message while keeping the actual payload in S3.

Minimal Code Changes: Using the Amazon SQS Extended Client Library for Java requires minimal changes to the existing code. Developers need to integrate the library, and the library itself handles the details of storing and retrieving large messages from Amazon S3.

</details>

### 20. gh-351

A company is moving its data management application to AWS. The company wants to transition to an event-driven architecture. The architecture needs to be more distributed and to use serverless concepts while performing the different aspects of the workflow. The company also wants to minimize operational overhead.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Build out the workflow in AWS Step Functions. Use Step Functions to create a state machine. Use the state machine to invoke AWS Lambda functions to process the workflow steps.**

AWS Step Functions allows you to coordinate the components of distributed applications using visual workflows. It is a fully managed service, which means you don't need to worry about operational overhead.

State machines in AWS Step Functions enable you to define the workflow of your application by specifying a series of steps. Each step can invoke an AWS Lambda function, among other things.

AWS Lambda is a serverless compute service, and it automatically scales with the workload. This aligns with the goal of using serverless concepts and minimizing operational overhead.

</details>

### 21. gh-362

A company uses a payment processing system that requires messages for a particular payment ID to be received in the same order that they were sent. Otherwise, the payments might be processed incorrectly.
Which actions should a solutions architect take to meet this requirement? (Choose two.)

<details><summary>Answer</summary>

**B. Write the messages to an Amazon Kinesis data stream with the payment ID as the partition key.**

E. Write the messages to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Set the message group to use the payment ID.

Amazon Kinesis data streams can be used with partition keys to ensure that messages with the same partition key are processed in order. In this case, using the payment ID as the partition key will help maintain the order of messages.

SQS FIFO queues ensure that messages are processed in the order they are received. By using message groups and setting the payment ID as the message group, you can guarantee that messages for the same payment ID will be processed sequentially.

</details>

### 22. gh-363

A company is building a game system that needs to send unique events to separate leaderboard, matchmaking, and authentication services concurrently. The company needs an AWS event-driven system that guarantees the order of the events.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Amazon Simple Notification Service (Amazon SNS) FIFO topics**

SNS FIFO also can send events or messages cocurrently to many subscribers while maintaining the order it receives. SNS fanout pattern is set in standard SNS which is commonly used to fan out events to large number of subscribers and usually for duplicated messages.

</details>

### 23. gh-400 `least-ops`

A meteorological startup company has a custom web application to sell weather data to its users online. The company uses Amazon DynamoDB to store its data and wants to build a new service that sends an alert to the managers of four internal teams every time a new weather event is recorded. The company does not want this new service to affect the performance of the current application.
What should a solutions architect do to meet these requirements with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**C. Enable Amazon DynamoDB Streams on the table. Use triggers to write to a single Amazon Simple Notification Service (Amazon SNS) topic to which the teams can subscribe.**

Using a single SNS topic simplifies the notification process. The trigger can publish a message to this topic, and each internal team can subscribe to this topic. This reduces the operational overhead compared to managing multiple SNS topics (Option B).

</details>

### 24. gh-489

An ecommerce company runs an application in the AWS Cloud that is integrated with an on-premises warehouse solution. The company uses Amazon Simple Notification Service (Amazon SNS) to send order messages to an on-premises HTTPS endpoint so the warehouse application can process the orders. The local data center team has detected that some of the order messages were not received.
A solutions architect needs to retain messages that are not delivered and analyze the messages for up to 14 days.
Which solution will meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**C. Configure an Amazon SNS dead letter queue that has an Amazon Simple Queue Service (Amazon SQS) target with a retention period of 14 days.**

Amazon SNS allows you to set up a dead letter queue to capture and retain messages that cannot be delivered to the intended endpoint.
When configuring a DLQ, you can specify an Amazon SQS queue as the target for messages that fail to be delivered.
Amazon SQS provides message retention settings, and in this case, you can set the retention period to 14 days.

</details>

### 25. gh-587

A company is designing a solution to capture customer activity in different web applications to process analytics and make predictions. Customer activity in the web applications is unpredictable and can increase suddenly. The company requires a solution that integrates with other web applications. The solution must include an authorization step for security purposes.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Configure an Amazon API Gateway endpoint in front of an Amazon Kinesis Data Firehose that stores the information that the company receives in an Amazon S3 bucket. Use an API Gateway Lambda authorizer to resolve authorization.**

Amazon API Gateway: It provides a fully managed service for creating, publishing, maintaining, monitoring, and securing APIs at any scale. It allows you to expose the capabilities of your backend services as APIs.
Amazon Kinesis Data Firehose: It can capture and load streaming data into storage services such as Amazon S3. It is well-suited for scenarios where you need to ingest and store large volumes of streaming data.
API Gateway Lambda Authorizer: It allows you to control access to your APIs using Lambda functions. It's used to resolve authorization before allowing access to the API.

</details>

### 26. gh-636

A development team is creating an event-based application that uses AWS Lambda functions. Events will be generated when files are added to an Amazon S3 bucket. The development team currently has Amazon Simple Notification Service (Amazon SNS) configured as the event target from Amazon S3.
What should a solutions architect do to process the events from Amazon S3 in a scalable way?

<details><summary>Answer</summary>

**C. Create an SNS subscription that sends the event to Amazon Simple Queue Service (Amazon SQS). Configure the SOS queue to trigger a Lambda function.**

</details>
