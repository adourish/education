# Flagged questions to adjudicate: compute

12 questions. For each: establish the truth, then decide keep / fix / drop.


---

## gh-245  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: A. Reconfigure the target group in the development environment to have only one EC2 instance as a target. Should be: D. Reduce the maximum number of EC2 instances in the development environment's Auto Scaling group. Why: The question states the application uses the ALB to direct traffic to *at least two* EC2 instances in a single target group, so dropping the development environment

**Question:**

A company is launching an application on AWS. The application uses an Application Load Balancer (ALB) to direct traffic to at least two Amazon EC2 instances in a single target group. The instances are in an Auto Scaling group for each environment. The company requires a development environment and a production environment. The production environment will have periods of high traffic.
Which solution will configure the development environment MOST cost-effectively?

**Stated answer:** A. Reconfigure the target group in the development environment to have only one EC2 instance as a target.

**Stated explanation:** For a development environment, where high availability and scalability might not be as critical as in production, having only one EC2 instance as a target in the target group could be a cost-effective solution. This reduces the number of running instances in the development environment when compared to production.


---

## gh-320  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: A. Publish data to Amazon Kinesis Data Streams, use Kinesis Data Analytics to query the data. Now: The service was renamed Amazon Managed Service for Apache Flink in August 2023. The SQL variant the explanation actually describes ("provides an SQL-like language for querying") — Kinesis Data Analytics for SQL Applications — is gone: no new applications could be created after 15 Octob

**Question:**

A company is using a fleet of Amazon EC2 instances to ingest data from on-premises data sources. The data is in JSON format and ingestion rates can be as high as 1 MB/s. When an EC2 instance is rebooted, the data in-flight is lost. The company’s data science team wants to query ingested data in near-real time.
Which solution provides near-real-time data querying that is scalable with minimal data loss?

**Stated answer:** A. Publish data to Amazon Kinesis Data Streams, Use Kinesis Data Analytics to query the data.

**Stated explanation:** Amazon Kinesis Data Streams: It is a scalable and durable real-time data streaming service. It allows you to ingest, buffer, and process streaming data in real time. In this scenario, you can publish data to a Kinesis Data Stream from your EC2 instances.

Kinesis Data Analytics: It provides an SQL-like language for querying and analyzing data in real time. You can use Kinesis Data Analytics to process and analyze the ingested data directly within the Kinesis pipeline.


---

## gh-422  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation does not describe the stated answer. The answer is SQS plus ECS services scaled on queue depth, but the explanation discusses an Application Load Balancer "to direct requests from the API to the ECS services" and claims "AWS App Mesh can be used to scale the instances of the ECS cluster based on the SQS queue size". App Mesh is a service mesh for service-to-service traffic a

**Question:**

A company is developing a new machine learning (ML) model solution on AWS. The models are developed as independent microservices that fetch approximately 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent.
The company provides models to hundreds of users. The usage patterns for the models are irregular. Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time.
Which design should a solutions architect recommend to meet these requirements?

**Stated answer:** D. Direct the requests from the API into an Amazon Simple Queue Service (Amazon SQS) queue. Deploy the models as Amazon Elastic Container Service (Amazon ECS) services that read from the queue. Enable AWS Auto Scaling on Amazon ECS for both the cluster and copies of the service based on the queue size.

**Stated explanation:** Amazon ECS Services: Deploying the models as Amazon ECS services allows for flexibility in managing the containerized applications. ECS services can efficiently handle the startup process of fetching model data from Amazon S3 and loading it into memory.

Application Load Balancer (ALB): The ALB is used to direct requests from the API to the ECS services. ALB provides advanced routing capabilities and can handle the asynchronous API requirements.

AWS App Mesh: AWS App Mesh can be used to scale the instances of the ECS cluster based on the SQS queue size. This allows for dynamic scaling based on demand, helping to efficiently use resources.


---

## gh-51  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The answer block is corrupted. After the two correct choices (the EventBridge/Lambda query and Amazon SES for the email) it continues with the full text and answers of three unrelated source questions — numbered 52, 53 and 54, covering EFS storage, S3 Object Lock and Windows file shares — and the last one is cut off mid-sentence. Anyone opening the toggle gets three other questions' answers

**Question:**

A company is developing an application that provides order shipping statistics for retrieval by a REST API. The company wants to extract the shipping statistics, organize the data into an easy-to-read HTML format, and send the report to several email addresses at the same time every morning.
Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

**Stated answer:** D. Create an Amazon EventBridge (Amazon CloudWatch Events) scheduled event that invokes an AWS Lambda function to query the application's API for the data.

**Stated explanation:** B. Use Amazon Simple Email Service (Amazon SES) to format the data and to send the report by email.

52.A company wants to migrate its on-premises application to AWS. The application produces output files that vary in size from tens of gigabytes to hundreds of terabytes. The application data must be stored in a standard file system structure. The company wants a solution that scales automatically. is highly available, and requires minimum operational overhead.
Which solution will meet these requirements?
C. Migrate the application to Amazon EC2 instances in a Multi-AZ Auto Scaling group. Use Amazon Elastic File System (Amazon EFS) for storage.

53.A company needs to store its accounting records in Amazon S3. The records must be immediately accessible for 1 year and then must be archived for an additional 9 years. No one at the company, including administrative users and root users, can b


---

## gh-523  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: B. Amazon CloudFront with Lambda@Edge functions. Should be: A. AWS AppSync pipeline resolvers. Why: AppSync pipeline resolvers chain several data-source calls — here several DynamoDB tables — inside a single GraphQL request, which is exactly "retrieve data from multiple DynamoDB tables" with no change to baseline performance and nothing to operate. Lambda@Edge is for rewriting reque

**Question:**

A company runs a microservice-based serverless web application. The application must be able to retrieve data from multiple Amazon DynamoDB tables A solutions architect needs to give the application the ability to retrieve the data with no impact on the baseline performance of the application.
Which solution will meet these requirements in the MOST operationally efficient way?

**Stated answer:** B. Amazon CloudFront with Lambda@Edge functions

**Stated explanation:** Amazon CloudFront is a content delivery network (CDN) service that can distribute content globally with low latency.
Lambda@Edge allows you to run custom code in response to CloudFront events, such as viewer requests, origin requests, and more.
By using Lambda@Edge functions, you can customize and augment the behavior of CloudFront.


---

## gh-531  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation opens with "AWS Lambda supports API Gateway integration, which allows you to create an HTTP endpoint (URL) for your Lambda function," which describes the wrong mechanism. The stated answer is a Lambda function URL — a built-in Lambda feature that gives the function its own dedicated HTTPS endpoint with no API Gateway in the path. The later sentences about avoiding extra serv

**Question:**

A company needs to integrate with a third-party data feed. The data feed sends a webhook to notify an external service when new data is ready for consumption. A developer wrote an AWS Lambda function to retrieve data when the company receives a webhook callback. The developer must make the Lambda function available for the third party to call.
Which solution will meet these requirements with the MOST operational efficiency?

**Stated answer:** A. Create a function URL for the Lambda function. Provide the Lambda function URL to the third party for the webhook.

**Stated explanation:** AWS Lambda supports API Gateway integration, which allows you to create an HTTP endpoint (URL) for your Lambda function.
Operational Efficiency:
Directly exposing the Lambda function through a URL eliminates the need for additional services, such as load balancers or message queues, for simple webhook integration.
Simplicity:
This approach is straightforward and easy to implement. It provides a direct URL that the third party can use to invoke the Lambda function when the webhook is triggered.


---

## gh-563  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation says Amazon EKS Connector is for centralizing "multiple Amazon EKS clusters" and for "register and connect multiple EKS clusters". EKS Connector exists to register Kubernetes clusters that are *not* EKS — on-premises, self-managed on EC2, or on another cloud — so they show up alongside EKS clusters in the EKS console. EKS clusters in the account already appear there and need

**Question:**

clusters and workloads from a central location.
Which solution will meet these requirements with the LEAST operational overhead?

**Stated answer:** B. Use Amazon EKS Connector to register and connect all Kubernetes clusters.

**Stated explanation:** Amazon EKS Connector is designed to help centralize the management of multiple Amazon Elastic Kubernetes Service (EKS) clusters. It allows you to register and connect multiple EKS clusters, providing a unified view of the clusters from the AWS Management Console. This solution aligns well with the requirement of managing clusters and workloads from a central location with the least operational overhead.


---

## gh-576  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation says edge-optimized API Gateway endpoints "leverage the AWS Global Accelerator and CloudFront". Global Accelerator is not involved in any way. An edge-optimized endpoint is fronted by an API Gateway-managed CloudFront distribution, and that is the whole mechanism.

**Question:**

A company is building a RESTful serverless web application on AWS by using Amazon API Gateway and AWS Lambda. The users of this web application will be geographically distributed, and the company wants to reduce the latency of API requests to these users.
Which type of endpoint should a solutions architect use to meet these requirements?

**Stated answer:** D. Edge-optimized endpoint

**Stated explanation:** Edge-optimized endpoints use the global CloudFront network to distribute API traffic across multiple edge locations. This reduces latency for users by serving API requests from the edge locations closest to the users. It leverages the AWS Global Accelerator and CloudFront to automatically route requests to the nearest AWS endpoint.


---

## gh-584  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: A. Run the EC2 instances in a spread placement group. Should be: The partition placement group option. Why: AWS defines a partition placement group as one where "groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions" — the question's wording about preventing *groups of nodes* from sharing hardware, and about the ar

**Question:**

A company is deploying an application that processes large quantities of data in parallel. The company plans to use Amazon EC2 instances for the workload. The network architecture must be configurable to prevent groups of nodes from sharing the same underlying hardware.
Which networking solution meets these requirements?

**Stated answer:** A. Run the EC2 instances in a spread placement group.

**Stated explanation:** A spread placement group is a logical grouping of instances that are placed on distinct underlying hardware. This ensures that instances within the group are physically separated, reducing the risk of correlated failures. This option is suitable for applications that need to maximize the level of isolation.


---

## gh-671  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation justifies the answer with "CloudWatch (Option D) lacks built-in anomaly detection", which is false — CloudWatch has had metric anomaly detection (machine-learning bands on any metric, usable as an alarm) since 2019. The correct reason to choose AWS Cost Anomaly Detection is that it is purpose-built for cost and usage data, segments spend by service, account and tag, and noti

**Question:**

A company runs its applications on Amazon EC2 instances. The company performs periodic nancial assessments of its AWS costs. The
company recently identi ed unusual spending.
The company needs a solution to prevent unusual spending. The solution must monitor costs and notify responsible stakeholders in the event of
unusual spending.
Which solution will meet these requirements?

**Stated answer:** Answer: B) Create a Cost Anomaly Detection monitor.

**Stated explanation:** Automatically detects and alerts on unusual spending.
CloudWatch (Option D) lacks built-in anomaly detection.


---

## gh-677  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: B. Use mixed On-Demand and Spot Instances in managed node groups. Should be: A. Use Spot Instances in managed node groups (all Spot). Why: The qualifier is MOST cost-effective, and the cluster is a development cluster used infrequently whose stated purpose is testing the application's resiliency — Spot interruptions are tolerable there, and are arguably the point. Managed node group

**Question:**

A company is developing an application that will run on a production Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster
has managed node groups that are provisioned with On-Demand Instances.
The company needs a dedicated EKS cluster for development work. The company will use the development cluster infrequently to test the
resiliency of the application. The EKS cluster must manage all the nodes.
Which solution will meet these requirements MOST cost-effectively?

**Stated answer:** Answer: B) Use mixed On-Demand + Spot Instances in managed node groups.

**Stated explanation:** Balances cost (Spot) and reliability (On-Demand) for infrequent dev workloads.
All-Spot (Option A) risks interruptions; self-managed ASG (Option C) adds overhead.


---

## wl-10  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: D. AWS Lambda (as the option that is *not* a CloudFront origin), with the explanation "AWS Lambda is not supported directly as the CloudFront origin". Now: A Lambda function URL is a supported CloudFront origin type and is listed as such in the CloudFront console. CloudFront added Origin Access Control for Lambda function URL origins on 11 April 2024, so you can both point a distrib

**Question:**

When creating an AWS CloudFront distribution, which of the following is not an origin?

**Options given by the source:**

- A. Elastic Load Balancer
- B. AWS S3 bucket
- C. AWS MediaPackage channel endpoint
- D. AWS Lambda

**Stated answer:** D. AWS Lambda

**Stated explanation:** Explanation: AWS Lambda is not supported directly as the CloudFront origin.
However, Lambda can be invoked through API Gateway which can be set as the
origin for AWS CloudFront. Read more here:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.
html
