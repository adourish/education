# Compute — EC2, Lambda, containers, scaling

93 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. wl-1

You are an AWS Solutions Architect. Your company has a successful web application deployed in an AWS Auto Scaling group. The application attracts more and more global customers. However, the application’s performance is impacted. Your manager asks you how to improve the performance and availability of the application. Which of the following AWS services would you recommend?

<details><summary>Answer</summary>

**D. AWS Global Accelerator**

AWS Global accelerator provides static IP addresses that are anycast in the AWS
edge network. Incoming traffic is distributed across endpoints in AWS regions. The
performance and availability of the application are improved.
Option
A 
is
incorrect:
Because DataSync is a tool to automate the data
transfer and does not help to improve the performance.
Option
B 
is
incorrect:
DynamoDB is not mentioned in this question.
Option
C 
is
incorrect:
Because AWS Lake Formation is used to
manage a large amount of data in AWS which would not help in this situation.
Option
D 
is
CORRECT:
Check the AWS Global Accelerator use
cases. The Global Accelerator service can improve both application performance and
availability.

</details>

### 2. wl-4

Your company has an online game application deployed in an Auto Scaling group. The traffic of the application is predictable. Every Friday, the traffic starts to increase, remains high on weekends and then drops on Monday. You need to plan the scaling actions for the Auto Scaling group. Which method is the most suitable for the scaling policy?

<details><summary>Answer</summary>

**D. Configure a scheduled action in the Auto Scaling group by specifying the**

The correct scaling policy should be scheduled scaling as it defines your own scaling
schedule. Refer to
https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html for
details.
Option
A 
is
incorrect:
This option may work. However, you have to
configure a target such as a Lambda function to perform the scaling actions.
Option
B 
is
incorrect:
The target tracking scaling policy defines a
target for the ASG. The scaling actions do not happen based on a schedule.
Option
C 
is
incorrect:
The step scaling policy does not configure the
ASG to scale at a specified time.
Option
D 
is
CORRECT:
With scheduled scaling, users define a schedule
for the ASG to scale. This option can meet the requirements.

</details>

### 3. wl-5

You are creating several EC2 instances for a new application. For better performance of the application, both low network latency and high network throughput are required for the EC2 instances. All instances should be launched in a single availability zone. How would you configure this?

<details><summary>Answer</summary>

**A. Launch all EC2 instances in a placement group using a Cluster placement strategy.**

The Cluster placement strategy helps to achieve a low-latency and high throughput
network. The reference is in
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#pla
cement-groups-limitations-partition.
Option
A 
is
CORRECT:
The Cluster placement strategy can improve
network performance among EC2 instances. The strategy can be selected when
creating a placement group:
Option
B 
is
incorrect:
Because the public IP cannot improve network
performance.
Option
C 
is
incorrect:
The Spread placement strategy is recommended
when a number of critical instances should be kept separate from each other. This
strategy should not be used in this scenario.
Option
D 
is
incorrect:
The description in the option is inaccurate. The
correct method is creating a placement group with a suitable placement strategy.
Also Read: AWS OpsWorks

</details>

### 4. wl-6

You need to deploy a machine learning application in AWS EC2. The performance of inter-instance communication is very critical for the application and you want to attach a network device to the instance so that the performance can be greatly improved. Which option is the most appropriate to improve the performance?

<details><summary>Answer</summary>

**B. Configure Elastic Fabric Adapter (EFA) in the instance.**

With Elastic Fabric Adapter (EFA), users can get better performance if compared
with enhanced networking (Elastic Network Adapter) or Elastic Network Interface.
Check the differences between EFAs and ENAs in
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html.
Option
A 
is
incorrect:
Because with Elastic Fabric Adapter (EFA),
users can achieve a better network performance than enhanced networking.
Option
B 
is
CORRECT:
Because EFA is the most suitable method for
accelerating High-Performance Computing (HPC) and machine learning application.
Option
C 
is
incorrect:
Because Elastic Network Interface (ENI) cannot
improve the performance as required.
Option
D 
is
incorrect:
The Elastic File System (EFS) cannot accelerate
inter-instance communication.

</details>

### 5. q-8

A company is migrating a distributed application to AWS. The application serves variable workloads. The legacy platform consists of a primary server that coordinates jobs across multiple compute nodes. The company wants to modernize the application with a solution that maximizes resiliency and scalability. How should a solutions architect design the architecture to meet these requirements?

<details><summary>Answer</summary>

**B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination for the jobs. Implement the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure EC2 Auto Scaling based on the size of the queue.**

Option B: This option provides a decoupled architecture where the jobs are sent to an SQS queue. The compute nodes (EC2 instances in an Auto Scaling group) can then process these jobs. Scaling based on the size of the SQS queue (the number of messages) allows the architecture to adapt to variable workloads, scaling out when the queue depth increases and scaling in when the depth decreases.

</details>

### 6. wl-19

Which of the following are not backup and restore solutions provided by AWS? (choose multiple)

<details><summary>Answer</summary>

**C. AWS Elastic Beanstalk; E.**

Option A is snapshot based data backup solution.
Option B, AWS Storage Gateway provides multiple solutions for backup & recovery.
Option D can be used as a Database backup solution.

</details>

### 7. wl-20

Organization ABC has a requirement to send emails to multiple users from their application deployed on EC2 instance in a private VPC. Email receivers will not be IAM users. You have decided to use AWS Simple Email Service and configured from email address. You are using AWS SES API to send emails from your EC2 instance to multiple users. However, email sending getting failed. Which of the following options could be the reason?

<details><summary>Answer</summary>

**B. AWS SES is in sandbox mode by default which can send emails only to verified**

Amazon SES is an email platform that provides an easy, cost-effective way for you to
send and receive email using your own email addresses and domains.
For example, you can send marketing emails such as special offers, transactional
emails such as order confirmations, and other types of correspondence such as
newsletters. When you use Amazon SES to receive mail, you can develop software
solutions such as email autoresponders, email unsubscribe systems and applications
that generate customer support tickets from incoming emails.
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.ht
ml

</details>

### 8. q-24 `least-ops`

A company observes an increase in Amazon EC2 costs in its most recent bill. The billing team notices unwanted vertical scaling of instance types for a couple of EC2 instances. A solutions architect needs to create a graph comparing the last 2 months of EC2 costs and perform an in-depth analysis to identify the root cause of the vertical scaling. How should the solutions architect generate the information with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Cost Explorer's granular filtering feature to perform an in-depth analysis of EC2 costs based on instance types.**

</details>

### 9. q-47

A company needs guaranteed Amazon EC2 capacity in three specific Availability Zones in a specific AWS Region for an upcoming event that will last 1 week. What should the company do to guarantee the EC2 capacity?

<details><summary>Answer</summary>

**D. Create an On-Demand Capacity Reservation that specifies the Region and three Availability Zones needed.**

An On-Demand Capacity Reservation is a type of Amazon EC2 reservation that enables you to create and manage reserved capacity on Amazon EC2. With an On-Demand Capacity Reservation, you can specify the Region and Availability Zones where you want to reserve capacity, and the number of EC2 instances you want to reserve. This allows you to guarantee capacity in specific Availability Zones in a specific Region.

</details>

### 10. q-48 `availability`

A company's website uses an Amazon EC2 instance store for its catalog of items. The company wants to make sure that the catalog is highly available and that the catalog is stored in a durable location. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Move the catalog to an Amazon Elastic File System (Amazon EFS) file system.**

EFS is fully managed, durable, highly available, and shared file system.

</details>

### 11. q-51

A company is developing an application that provides order shipping statistics for retrieval by a REST API. The company wants to extract the shipping statistics, organize the data into an easy-to-read HTML format, and send the report to several email addresses at the same time every morning. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**Both of the following: (1) Create an Amazon EventBridge scheduled event that invokes an AWS Lambda function to query the application's API for the data; and (2) use Amazon Simple Email Service (Amazon SES) to send the report by email.**

The report has to go out at the same time every morning, which is exactly what an EventBridge schedule does, and the thing it triggers needs to call a REST API and build HTML, which is ordinary Lambda work with no servers to run. Amazon SES then delivers the HTML message to the list of recipients in one send, and it is the AWS service meant for sending application email to real mailboxes. An SNS topic can notify subscribers but is not suited to delivering a formatted HTML report, and a Glue job is for extract-transform-load work over data stores, not for calling an API and emailing a page.

</details>

### 12. q-190 `availability`

A company has a web application that is based on Java and PHP. The company plans to move the application from on premises to AWS. The company needs the ability to test new site features frequently. The company also needs a highly available and managed solution that requires minimum operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the web application to an AWS Elastic Beanstalk environment. Use URL swapping to switch between multiple Elastic Beanstalk environments for feature testing.**

Elastic Beanstalk allows you to perform blue-green deployments, which involve creating a new environment (green) with the updated code, testing it, and then swapping the URLs to direct traffic to the new environment. This enables you to test new features without affecting the production environment.

</details>

### 13. q-203

The customers of a finance company request appointments with financial advisors by sending text messages. A web application that runs on Amazon EC2 instances accepts the appointment requests. The text messages are published to an Amazon Simple Queue Service (Amazon SQS) queue through the web application. Another application that runs on EC2 instances then sends meeting invitations and meeting confirmation email messages to the customers. After successful scheduling, this application stores the meeting information in an Amazon DynamoDB database. As the company expands, customers report that their meeting invitations are taking longer to arrive. What should a solutions architect recommend to resolve this issue?

<details><summary>Answer</summary>

**D. Add an Auto Scaling group for the application that sends meeting invitations. Configure the Auto Scaling group to scale based on the depth of the SQS queue.**

To resolve the issue of longer delivery times for meeting invitations, the solutions architect can recommend adding an Auto Scaling group for the application that sends meeting invitations and configuring the Auto Scaling group to scale based on the depth of the SQS queue. This will allow the application to scale up as the number of appointment requests increases, improving the performance and delivery times of the meeting invitations.

</details>

### 14. q-209

A solutions architect is designing the architecture of a new application being deployed to the AWS Cloud. The application will run on Amazon EC2 On-Demand Instances and will automatically scale across multiple Availability Zones. The EC2 instances will scale up and down frequently throughout the day. An Application Load Balancer (ALB) will handle the load distribution. The architecture needs to support distributed session data management. The company is willing to make changes to code if needed. What should the solutions architect do to ensure that the architecture supports distributed session data management?

<details><summary>Answer</summary>

**A. Use Amazon ElastiCache to manage and store session data.**

Amazon ElastiCache is a fully managed, in-memory data store service. It is commonly used for caching and session management in distributed applications. By utilizing ElastiCache for session data management, you can store and retrieve session data in a scalable and high-performance manner. The use of ElastiCache allows for a distributed and shared data store for session management across multiple instances and Availability Zones.

</details>

### 15. q-220 `cost`

A solutions architect is designing a new API using Amazon API Gateway that will receive requests from users. The volume of requests is highly variable; several hours can pass without receiving a single request. The data processing will take place asynchronously, but should be completed within a few seconds after a request is made. Which compute service should the solutions architect have the API invoke to deliver the requirements at the lowest cost?

<details><summary>Answer</summary>

**B. An AWS Lambda function**

AWS Lambda supports asynchronous invocation, which is suitable for scenarios where data processing can take place independently of the API request and complete within a few seconds. This aligns with the requirement of processing data asynchronously.

</details>

### 16. q-242

A company hosts its web application on AWS using seven Amazon EC2 instances. The company requires that the IP addresses of all healthy EC2 instances be returned in response to DNS queries. Which policy should be used to meet this requirement?

<details><summary>Answer</summary>

**C. Multivalue routing policy**

The multivalue routing policy returns multiple healthy IP addresses for the resource in response to DNS queries. This is suitable for distributing traffic across multiple resources, such as EC2 instances, and meeting the specified requirement.  Simple Routing: Gives one answer (IP address). Latency Routing: Considers the fastest route but still gives one answer. Multivalue Routing: Gives multiple answers (multiple IP addresses). Geolocation Routing: Directs based on user location but typically gives one answer.

</details>

### 17. q-245 `cost`

A company is launching an application on AWS. The application uses an Application Load Balancer (ALB) to direct traffic to at least two Amazon EC2 instances in a single target group. The instances are in an Auto Scaling group for each environment. The company requires a development environment and a production environment. The production environment will have periods of high traffic. Which solution will configure the development environment MOST cost-effectively?

<details><summary>Answer</summary>

**Reduce the maximum number of EC2 instances in the development environment's Auto Scaling group.**

Development and production each have their own Auto Scaling group, and only production sees bursts of traffic. Capping the maximum size of the development group stops it from ever scaling out to a production-sized fleet, so development runs the minimum it needs and nothing more. Taking a target out of the development target group saves nothing, because the instance keeps running and billing - the Auto Scaling group still owns it and will simply register it again - and it also contradicts the requirement that the load balancer serve at least two instances. Shrinking instance sizes in both environments would change production as well, and the load balancing algorithm has no bearing on cost.

</details>

### 18. gh-248

Users report that some submitted data is not being processed Amazon CloudWatch reveals that the EC2 instances have a consistent CPU utilization at or near 100%. The company wants to improve system performance and scale the system based on user load.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Route incoming requests to Amazon Simple Queue Service (Amazon SQS). Configure an EC2 Auto Scaling group based on queue size. Update the software to read from the queue.**

This option addresses the issue by offloading incoming requests to an SQS queue, allowing for decoupling of processing and scaling based on queue size. This helps improve system performance and allows for scaling based on user load.

</details>

### 19. q-261

A company recently announced the deployment of its retail website to a global audience. The website runs on multiple Amazon EC2 instances behind an Elastic Load Balancer. The instances run in an Auto Scaling group across multiple Availability Zones. The company wants to provide its customers with different versions of content based on the devices that the customers use to access the website. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Configure Amazon CloudFront to cache multiple versions of the content.**

C. Configure a Lambda@Edge function to send specific objects to users based on the User-Agent header.  Amazon CloudFront is a content delivery network (CDN) service that can cache and deliver content globally. Configure CloudFront to cache different versions of content based on the device type or other criteria.  Lambda@Edge allows you to run code in response to CloudFront events globally. Use a Lambda@Edge function to inspect the User-Agent header and dynamically serve different versions of content based on the device type.

</details>

### 20. q-263

A company is building an application that consists of several microservices. The company has decided to use container technologies to deploy its software on AWS. The company needs a solution that minimizes the amount of ongoing effort for maintenance and scaling. The company cannot manage additional infrastructure. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Deploy an Amazon Elastic Container Service (Amazon ECS) cluster.**

D. Deploy an Amazon Elastic Container Service (Amazon ECS) service with a Fargate launch type. Specify a desired task number level of greater than or equal to 2.  An ECS cluster is necessary to organize and manage your Fargate tasks and services. It provides a logical grouping of tasks and services. When using Fargate, you don't need to manage the underlying EC2 instances; the cluster helps manage the Fargate tasks.  Fargate is a serverless compute engine for containers that eliminates the need to manage underlying infrastructure. With Fargate, you do not need to provision or manage EC2 instances; AWS takes care of the infrastructure, allowing you to focus solely on your containers.

</details>

### 21. q-266

A company has a popular gaming platform running on AWS. The application is sensitive to latency because latency can impact the user experience and introduce unfair advantages to some players. The application is deployed in every AWS Region. It runs on Amazon EC2 instances that are part of Auto Scaling groups configured behind Application Load Balancers (ALBs). A solutions architect needs to implement a mechanism to monitor the health of the application and redirect traffic to healthy endpoints. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Configure an accelerator in AWS Global Accelerator. Add a listener for the port that the application listens on, and attach it to a Regional endpoint in each Region. Add the ALB as the endpoint.**

AWS Global Accelerator is designed to provide static IP addresses for global applications and direct traffic over the AWS global network to optimal AWS endpoints based on health, geography, and routing policies. Configure an accelerator with a listener for the port that the application listens on. Attach the listener to a Regional endpoint in each AWS Region where the application is deployed.

</details>

### 22. q-271

A solutions architect observes that a nightly batch processing job is automatically scaled up for 1 hour before the desired Amazon EC2 capacity is reached. The peak capacity is the ‘same every night and the batch jobs always start at 1 AM. The solutions architect needs to find a cost-effective solution that will allow for the desired EC2 capacity to be reached quickly and allow the Auto Scaling group to scale down after the batch jobs are complete. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Configure scheduled scaling to scale up to the desired compute level.**

Scheduled scaling allows you to define specific times when your Auto Scaling group's desired capacity should be increased or decreased. In this case, you can schedule the scaling action to increase the capacity just before the nightly batch processing job starts at 1 AM and then scale it down after the job completes.

</details>

### 23. q-275

A company runs an internal browser-based application. The application runs on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales up to 20 instances during work hours, but scales down to 2 instances overnight. Staff are complaining that the application is very slow when the day begins, although it runs well by mid-morning. How should the scaling be changed to address the staff complaints and keep costs to a minimum?

<details><summary>Answer</summary>

**C. Implement a target tracking action triggered at a lower CPU threshold, and decrease the cooldown period.**

</details>

### 24. q-276

A company has a multi-tier application deployed on several Amazon EC2 instances in an Auto Scaling group. An Amazon RDS for Oracle instance is the application’ s data layer that uses Oracle-specific PL/SQL functions. Traffic to the application has been steadily increasing. This is causing the EC2 instances to become overloaded and the RDS instance to run out of storage. The Auto Scaling group does not have any scaling metrics and defines the minimum healthy instance count only. The company predicts that traffic will continue to increase at a steady but unpredictable rate before leveling off. What should a solutions architect do to ensure the system can automatically scale for the increased traffic? (Choose two.)

<details><summary>Answer</summary>

**A. Configure storage Auto Scaling on the RDS for Oracle instance.**

This option allows the RDS instance to automatically scale its storage based on the actual storage usage, ensuring that you don't run out of storage.  D. Configure the Auto Scaling group to use the average CPU as the scaling metric.  By using CPU utilization as a scaling metric, the Auto Scaling group can dynamically adjust the number of EC2 instances based on the application's demand. This helps in handling increased traffic and preventing overload on existing instances.

</details>

### 25. q-287

A company wants to migrate a Windows-based application from on premises to the AWS Cloud. The application has three tiers: an application tier, a business tier, and a database tier with Microsoft SQL Server. The company wants to use specific features of SQL Server such as native backups and Data Quality Services. The company also needs to share files for processing between the tiers. How should a solutions architect design the architecture to meet these requirements?

<details><summary>Answer</summary>

**B. Host all three tiers on Amazon EC2 instances. Use Amazon FSx for Windows File Server for file sharing between the tiers.**

hosting all three tiers on Amazon EC2 instances allows you to have flexibility and control over the entire application architecture. To address the file-sharing requirement between the tiers, you can use Amazon FSx for Windows File Server.  Amazon FSx for Windows File Server is a fully managed Windows file system that is accessible from Windows-based instances over the Server Message Block (SMB) protocol. It supports the specific features of Windows File Server, including features like native backups and access to Windows-specific services.

</details>

### 26. q-290

A company hosts a web application on multiple Amazon EC2 instances. The EC2 instances are in an Auto Scaling group that scales in response to user demand. The company wants to optimize cost savings without making a long-term commitment. Which EC2 instance purchasing option should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. A mix of On-Demand Instances and Spot Instances**

On-Demand Instances: These instances are charged per hour or per second of usage, without any upfront payment or long-term commitment. While they offer flexibility, they are usually more expensive compared to other purchasing options.  Spot Instances: These are spare compute capacity in the AWS cloud available at a lower price compared to On-Demand Instances. However, they can be terminated by AWS with little notice if the capacity is needed elsewhere. Spot Instances are suitable for workloads that are fault-tolerant and can handle interruptions.

</details>

### 27. gh-297

A solutions architect needs to implement a solution to automate the scalability of the application. The solution must optimize the cost of the architecture and must ensure that the application has enough CPU resources when surges occur.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an EC2 Auto Scaling group. Select the existing ALB as the load balancer and the existing target group as the target group. Set a target tracking scaling policy that is based on the ASGAverageCPUUtilization metric. Set the minimum instances to 2, the desired capacity to 3, the maximum instances to 6, and the target value to 50%. Add the EC2 instances to the Auto Scaling group.**

Option B utilizes EC2 Auto Scaling, which automatically adjusts the number of EC2 instances in the Auto Scaling group based on the specified target tracking scaling policy.
By setting a target tracking scaling policy based on the ASGAverageCPUUtilization metric with a target value of 50%, the Auto Scaling group will dynamically adjust the number of instances to maintain an average CPU utilization close to the target value.
This solution provides scalability when needed, ensures that there are enough CPU resources during surges, and optimizes costs by automatically adjusting the capacity based on demand.

</details>

### 28. q-300 `cost`

A company needs to migrate a legacy application from an on-premises data center to the AWS Cloud because of hardware capacity constraints. The application runs 24 hours a day, 7 days a week. The application’s database storage continues to grow over time. What should a solutions architect do to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Migrate the application layer to Amazon EC2 Reserved Instances. Migrate the data storage layer to Amazon Aurora Reserved Instances.**

Using Amazon EC2 Reserved Instances for the application layer provides cost savings compared to On-Demand Instances while ensuring availability for the 24/7 runtime. Migrating the data storage layer to Amazon Aurora Reserved Instances provides a fully managed relational database service with automatic scaling capabilities. Amazon Aurora is designed for high performance and cost efficiency. Reserved Instances provide cost savings compared to On-Demand Instances over an extended period, making them suitable for applications with continuous operation. Amazon Aurora, being a fully managed service, offloads much of the operational overhead associated with managing a traditional database, making it a cost-effective choice for growing database storage.

</details>

### 29. q-303

A company is launching a new application deployed on an Amazon Elastic Container Service (Amazon ECS) cluster and is using the Fargate launch type for ECS tasks. The company is monitoring CPU and memory usage because it is expecting high traffic to the application upon its launch. However, the company wants to reduce costs when utilization decreases. What should a solutions architect recommend?

<details><summary>Answer</summary>

**D. Use AWS Application Auto Scaling with target tracking policies to scale when ECS metric breaches trigger an Amazon CloudWatch alarm.**

AWS Application Auto Scaling is a service that can automatically adjust the number of running ECS tasks or services based on specified CloudWatch metrics. Target tracking policies allow you to set a target value for a specific metric, and AWS Application Auto Scaling automatically adjusts the desired task count to maintain the target. By using target tracking policies, you can ensure that the ECS cluster scales up or down based on the application's demand while maintaining a balance between cost efficiency and performance.

</details>

### 30. q-306

A company wants to run an in-memory database for a latency-sensitive application that runs on Amazon EC2 instances. The application processes more than 100,000 transactions each minute and requires high network throughput. A solutions architect needs to provide a cost- effective network design that minimizes data transfer charges. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Launch all EC2 instances in the same Availability Zone within the same AWS Region. Specify a placement group with cluster strategy when launching EC2 instances.**

A placement group is a logical grouping of instances within a single Availability Zone. The "cluster" strategy for placement groups places instances in close proximity to each other, providing low-latency, high-throughput communication between instances. By launching all EC2 instances in the same Availability Zone within the same AWS Region, you minimize data transfer charges because data transfer within the same Availability Zone is not subject to additional costs.

</details>

### 31. q-318

A company recently migrated its entire IT environment to the AWS Cloud. The company discovers that users are provisioning oversized Amazon EC2 instances and modifying security group rules without using the appropriate change control process. A solutions architect must devise a strategy to track and audit these inventory and configuration changes. Which actions should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Enable AWS CloudTrail and use it for auditing.**

D. Enable AWS Config and create rules for auditing and compliance purposes.  A. Enable AWS CloudTrail and use it for auditing. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS Command Line Interface (CLI), and AWS SDKs and APIs. By enabling CloudTrail, the company can track user activity and changes to AWS resources, and monitor compliance with internal policies and external regulations.  D. Enable AWS Config and create rules for auditing and compliance purposes. AWS Config provides a detailed inventory of the AWS resources in your account, and continuously records changes to the configurations of those resources. By creating rules in AWS Config, the company can automate the evaluation of resource configurations against desired state, and receive alerts when configurations drift from compliance.

</details>

### 32. q-320

A company is using a fleet of Amazon EC2 instances to ingest data from on-premises data sources. The data is in JSON format and ingestion rates can be as high as 1 MB/s. When an EC2 instance is rebooted, the data in-flight is lost. The company’s data science team wants to query ingested data in near-real time. Which solution provides near-real-time data querying that is scalable with minimal data loss?

<details><summary>Answer</summary>

**Publish the data to Amazon Kinesis Data Streams, and query the stream in near real time with Amazon Managed Service for Apache Flink (the service previously called Kinesis Data Analytics).**

Kinesis Data Streams accepts the 1 MB/s feed and holds every record durably across three Availability Zones for a retention period you choose, so a reboot of the producing EC2 instance no longer loses in-flight data, and throughput grows by adding shards. Amazon Managed Service for Apache Flink reads directly from the stream and runs continuous queries, which gives the data science team results seconds behind the source; SQL is still available through Flink SQL and Studio notebooks. Writing the feed to Amazon S3 with Firehose and querying it with Athena would work but adds minutes of buffering delay, which is not near real time.

</details>

### 33. q-328

A company is hosting a three-tier ecommerce application in the AWS Cloud. The company hosts the website on Amazon S3 and integrates the website with an API that handles sales requests. The company hosts the API on three Amazon EC2 instances behind an Application Load Balancer (ALB). The API consists of static and dynamic front-end content along with backend workers that process sales requests asynchronously. The company is expecting a significant and sudden increase in the number of sales requests during events for the launch of new products. What should a solutions architect recommend to ensure that all the requests are processed successfully?

<details><summary>Answer</summary>

**B. Add an Amazon CloudFront distribution for the static content. Place the EC2 instances in an Auto Scaling group to launch new instances based on network traffic.**

Amazon CloudFront for Static Content: By using CloudFront, you can distribute static content (like images, stylesheets) globally, reducing latency for end-users and offloading some of the traffic from your backend instances.  Auto Scaling Group: An Auto Scaling group allows you to automatically adjust the number of EC2 instances to handle changes in demand. By placing the EC2 instances in an Auto Scaling group, you can dynamically scale the number of instances based on network traffic, ensuring that the application can handle increased load during events.

</details>

### 34. q-333

A company’s application runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. On the first day of every month at midnight, the application becomes much slower when the month-end financial calculation batch runs. This causes the CPU utilization of the EC2 instances to immediately peak to 100%, which disrupts the application. What should a solutions architect recommend to ensure the application is able to handle the workload and avoid downtime?

<details><summary>Answer</summary>

**C. Configure an EC2 Auto Scaling scheduled scaling policy based on the monthly schedule.**

By configuring a scheduled scaling policy, the EC2 Auto Scaling group can proactively launch additional EC2 instances before the CPU utilization peaks to 100%. This will ensure that the application can handle the workload during the month-end financial calculation batch, and avoid any disruption or downtime.  Configuring a simple scaling policy based on CPU utilization or adding Amazon CloudFront distribution or Amazon ElastiCache will not directly address the issue of handling the monthly peak workload.

</details>

### 35. q-335

A company is experiencing sudden increases in demand. The company needs to provision large Amazon EC2 instances from an Amazon Machine Image (AMI). The instances will run in an Auto Scaling group. The company needs a solution that provides minimum initialization latency to meet the demand. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Enable Amazon Elastic Block Store (Amazon EBS) fast snapshot restore on a snapshot. Provision an AMI by using the snapshot. Replace the AMI in the Auto Scaling group with the new AMI.**

Amazon EBS Fast Snapshot Restore: Enabling fast snapshot restore allows you to provision Amazon EBS volumes based on snapshots with faster performance. This is particularly useful when creating AMIs from snapshots, as it reduces the time it takes to create EBS volumes from those snapshots.  Minimum Initialization Latency: Fast snapshot restore helps in minimizing initialization latency as it provides a way to quickly create EBS volumes from snapshots.  Provisioning AMI from Snapshot: You can create an Amazon Machine Image (AMI) from an Amazon EBS snapshot. This allows you to capture a point-in-time snapshot of the file system, and then use that snapshot to create new instances.

</details>

### 36. q-342 `least-ops`

A transaction processing company has weekly scripted batch jobs that run on Amazon EC2 instances. The EC2 instances are in an Auto Scaling group. The number of transactions can vary, but the baseline CPU utilization that is noted on each run is at least 60%. The company needs to provision the capacity 30 minutes before the jobs run. Currently, engineers complete this task by manually modifying the Auto Scaling group parameters. The company does not have the resources to analyze the required capacity trends for the Auto Scaling group counts. The company needs an automated way to modify the Auto Scaling group’s desired capacity. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create a predictive scaling policy for the Auto Scaling group. Configure the policy to scale based on forecast. Set the scaling metric to CPU utilization. Set the target value for the metric to 60%. In the policy, set the instances to pre-launch 30 minutes before the jobs run.**

In general, if you have regular patterns of traffic increases and applications that take a long time to initialize, you should consider using predictive scaling. Predictive scaling can help you scale faster by launching capacity in advance of forecasted load, compared to using only dynamic scaling, which is reactive in nature.

</details>

### 37. q-355 `least-ops`

A company is migrating an old application to AWS. The application runs a batch job every hour and is CPU intensive. The batch job takes 15 minutes on average with an on-premises server. The server has 64 virtual CPU (vCPU) and 512 GiB of memory. Which solution will run the batch job within 15 minutes with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use AWS Batch on Amazon EC2.**

AWS Batch on Amazon EC2: AWS Batch is a fully managed service for batch computing that dynamically provisions the optimal quantity and type of compute resources (Amazon EC2 instances) based on the volume and specific resource requirements of the batch jobs. If the batch job is CPU-intensive and can be parallelized, AWS Batch can efficiently manage the compute resources needed for the job, and it provides a higher level of control over the environment compared to serverless options like AWS Lambda.

</details>

### 38. q-369 `least-ops`

A company has migrated an application to Amazon EC2 Linux instances. One of these EC2 instances runs several 1-hour tasks on a schedule. These tasks were written by different teams and have no common programming language. The company is concerned about performance and scalability while these tasks run on a single instance. A solutions architect needs to implement a solution to resolve these concerns. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Batch to run the tasks as jobs. Schedule the jobs by using Amazon EventBridge (Amazon CloudWatch Events).**

AWS Batch: AWS Batch is a fully managed service for running batch computing workloads. It dynamically provisions the optimal quantity and type of compute resources based on the volume and specific resource requirements of the batch jobs. It allows you to run tasks written in different programming languages with minimal operational overhead.

</details>

### 39. q-375 `least-ops`

An ecommerce company is building a distributed application that involves several serverless functions and AWS services to complete order- processing tasks. These tasks require manual approvals as part of the workflow. A solutions architect needs to design an architecture for the order-processing application. The solution must be able to combine multiple AWS Lambda functions into responsive serverless applications. The solution also must orchestrate data and services that run on Amazon EC2 instances, containers, or on-premises servers. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Step Functions to build the application.**

Step Functions provide a way to coordinate and orchestrate multiple AWS services, including AWS Lambda functions, in a serverless workflow. They allow you to build applications by connecting various serverless functions and services without managing the underlying infrastructure.

</details>

### 40. q-377

A company recently deployed a new auditing system to centralize information about operating system versions, patching, and installed software for Amazon EC2 instances. A solutions architect must ensure all instances provisioned through EC2 Auto Scaling groups successfully send reports to the auditing system as soon as they are launched and terminated. Which solution achieves these goals MOST efficiently?

<details><summary>Answer</summary>

**B. Use EC2 Auto Scaling lifecycle hooks to run a custom script to send data to the audit system when instances are launched and terminated.**

</details>

### 41. q-380

A company is migrating its on-premises workload to the AWS Cloud. The company already uses several Amazon EC2 instances and Amazon RDS DB instances. The company wants a solution that automatically starts and stops the EC2 instances and DB instances outside of business hours. The solution must minimize cost and infrastructure maintenance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an AWS Lambda function that will start and stop the EC2 instances and DB instances. Configure Amazon EventBridge to invoke the Lambda function on a schedule.**

AWS Lambda Function: Create a Lambda function that contains the logic to start and stop the EC2 instances and DB instances. Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It is a cost-effective and maintenance-free solution.  Amazon EventBridge: Configure EventBridge (formerly CloudWatch Events) to invoke the Lambda function on a schedule. EventBridge provides a reliable and scalable way to schedule the execution of Lambda functions at specified intervals, such as starting and stopping instances during business hours.

</details>

### 42. q-382

A company has a three-tier application on AWS that ingests sensor data from its users’ devices. The traffic flows through a Network Load Balancer (NLB), then to Amazon EC2 instances for the web tier, and finally to EC2 instances for the application tier. The application tier makes calls to a database. What should a solutions architect do to improve the security of the data in transit?

<details><summary>Answer</summary>

**A. Configure a TLS listener. Deploy the server certificate on the NLB.**

TLS Listener on NLB: By configuring a TLS (Transport Layer Security) listener on the NLB, you can encrypt the traffic between the users' devices and the web tier EC2 instances. This helps protect the data in transit from eavesdropping and other potential security threats.

</details>

### 43. q-388

A company is deploying a two-tier web application in a VPC. The web tier is using an Amazon EC2 Auto Scaling group with public subnets that span multiple Availability Zones. The database tier consists of an Amazon RDS for MySQL DB instance in separate private subnets. The web tier requires access to the database to retrieve product information. The web application is not working as intended. The web application reports that it cannot connect to the database. The database is confirmed to be up and running. All configurations for the network ACLs, security groups, and route tables are still in their default states. What should a solutions architect recommend to fix the application?

<details><summary>Answer</summary>

**D. Add an inbound rule to the security group of the database tier’s RDS instance to allow traffic from the web tiers security group.**

Security Groups: Security groups act as virtual firewalls for your instances to control inbound and outbound traffic. By default, they deny all inbound traffic. In this scenario, the default security group associated with the RDS instance is likely denying incoming traffic from the web tier.  Inbound Rule: To allow traffic from the web tier's EC2 instances to the database tier's RDS instance, you need to add an inbound rule to the security group associated with the RDS instance. This rule should permit traffic from the security group associated with the web tier's EC2 instances.

</details>

### 44. q-391

A company needs a backup strategy for its three-tier stateless web application. The web application runs on Amazon EC2 instances in an Auto Scaling group with a dynamic scaling policy that is configured to respond to scaling events. The database tier runs on Amazon RDS for PostgreSQL. The web application does not require temporary local storage on the EC2 instances. The company’s recovery point objective (RPO) is 2 hours. The backup strategy must maximize scalability and optimize resource utilization for this environment. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Retain the latest Amazon Machine Images (AMIs) of the web and application tiers. Enable automated backups in Amazon RDS and use point-in-time recovery to meet the RPO.**

Snapshots of EBS volumes would be necessary if you want to back up the entire EC2 instance, including any applications and temporary data stored on the EBS volumes attached to the instances. When you take a snapshot of an EBS volume, it backs up the entire contents of that volume. This ensures that you can restore the entire EC2 instance to a specific point in time more quickly. However, if there is no temporary data stored on the EBS volumes, then snapshots of EBS volumes are not necessary.

</details>

### 45. q-397

An ecommerce company needs to run a scheduled daily job to aggregate and filter sales records for analytics. The company stores the sales records in an Amazon S3 bucket. Each object can be up to 10 GB in size. Based on the number of sales events, the job can take up to an hour to complete. The CPU and memory usage of the job are constant and are known in advance. A solutions architect needs to minimize the amount of operational effort that is needed for the job to run. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Elastic Container Service (Amazon ECS) cluster with an AWS Fargate launch type. Create an Amazon EventBridge scheduled event that launches an ECS task on the cluster to run the job.**

C. Amazon ECS with Fargate: Fargate allows you to run containers without managing the underlying infrastructure. You can schedule the ECS task with EventBridge, and since Fargate manages the resources, you don't need to worry about scaling or infrastructure maintenance. This is a good fit for long-running jobs.

</details>

### 46. q-405

A solutions architect is designing the architecture for a software demonstration environment. The environment will run on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer (ALB). The system will experience significant increases in traffic during working hours but is not required to operate on weekends. Which combination of actions should the solutions architect take to ensure that the system can scale to meet demand? (Choose two.)

<details><summary>Answer</summary>

**D. Use a target tracking scaling policy to scale the Auto Scaling group based on instance CPU utilization.**

E. Use scheduled scaling to change the Auto Scaling group minimum, maximum, and desired capacity to zero for weekends. Revert to the default values at the start of the week.  Explanation: An Application Load Balancer scales its own capacity automatically — you don't (and can't) attach an Auto Scaling policy to the ALB itself, so the old option A isn't a real configuration. The EC2 Auto Scaling group behind it is what needs a scaling policy (D), alongside scheduled scaling (E) to scale to zero on weekends.  This allows you to save costs and resources during weekends when the system is not required to operate. Scaling down the Auto Scaling group to zero instances during weekends and reverting to the default values at the start of the week ensures that you only incur costs when the system is actively in use.

</details>

### 47. q-409 `availability`

A solutions architect must migrate a Windows Internet Information Services (IIS) web application to AWS. The application currently relies on a file share hosted in the user's on-premises network-attached storage (NAS). The solutions architect has proposed migrating the IIS web servers to Amazon EC2 instances in multiple Availability Zones that are connected to the storage solution, and configuring an Elastic Load Balancer attached to the instances. Which replacement to the on-premises file share is MOST resilient and durable?

<details><summary>Answer</summary>

**C. Migrate the file share to Amazon FSx for Windows File Server.**

Amazon FSx for Windows File Server: Amazon FSx is a fully managed file storage service that is compatible with Windows file systems. Amazon FSx for Windows File Server is specifically designed for Windows workloads, including IIS web applications. It provides a highly available and durable file system that can be accessed by multiple EC2 instances in different Availability Zones.

</details>

### 48. q-413

An ecommerce company is experiencing an increase in user traffic. The company’s store is deployed on Amazon EC2 instances as a two-tier web application consisting of a web tier and a separate database tier. As traffic increases, the company notices that the architecture is causing significant delays in sending timely marketing and order confirmation email to users. The company wants to reduce the time it spends resolving complex email delivery issues and minimize operational overhead. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Configure the web instance to send email through Amazon Simple Email Service (Amazon SES).**

Amazon Simple Email Service (Amazon SES) is a fully managed email sending service. By configuring the web instances to send emails through Amazon SES, the ecommerce company can offload the complexity of email delivery to a reliable and scalable service.

</details>

### 49. q-422

A company is developing a new machine learning (ML) model solution on AWS. The models are developed as independent microservices that fetch approximately 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular. Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which design should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**Direct the requests from the API into an Amazon Simple Queue Service (Amazon SQS) queue. Deploy the models as Amazon Elastic Container Service (Amazon ECS) services that read from the queue. Enable AWS Auto Scaling on Amazon ECS for both the cluster and copies of the service based on the queue size.**

The API is asynchronous, so requests can sit in an SQS queue and be picked up when capacity exists; the queue absorbs a sudden batch of thousands of requests without dropping any and without the caller waiting. Scaling the ECS service on the number of messages waiting in the queue adds containers only when work arrives and scales back down through the days or weeks a model is unused, and scaling the cluster capacity alongside it means you are not paying for idle hosts. Long-running containers also keep the 1 GB of model data in memory between requests, whereas a design that fronts short-lived functions with a load balancer would re-download that 1 GB on every cold start and would make an asynchronous API behave synchronously.

</details>

### 50. q-424 `cost`

A company is running a custom application on Amazon EC2 On-Demand Instances. The application has frontend nodes that need to run 24 hours a day, 7 days a week and backend nodes that need to run only for a short time based on workload. The number of backend nodes varies during the day. The company needs to scale out and scale in more instances based on workload. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use Reserved Instances for the frontend nodes. Use Spot Instances for the backend nodes.**

Reserved Instances (RIs) for Frontend Nodes: Since the frontend nodes need to run 24/7, Reserved Instances provide a significant cost savings compared to On-Demand pricing. RIs are a commitment to a consistent usage pattern, making them suitable for instances that need to run continuously.  Spot Instances for Backend Nodes: Spot Instances are a cost-effective option for workloads that can be interrupted or are flexible regarding availability. As the number of backend nodes varies during the day, using Spot Instances allows you to take advantage of spare capacity at a lower cost. Spot Instances are suitable for short-lived, scalable, and flexible workloads.

</details>

### 51. q-427 `availability`

A solutions architect is implementing a complex Java application with a MySQL database. The Java application must be deployed on Apache Tomcat and must be highly available. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the application by using AWS Elastic Beanstalk. Configure a load-balanced environment and a rolling deployment policy.**

AWS Elastic Beanstalk: It is a fully managed service that simplifies the deployment and operation of applications, including web applications running Apache Tomcat. Elastic Beanstalk handles the deployment details, capacity provisioning, load balancing, auto-scaling, and application health monitoring, making it easier to deploy and manage your applications.

</details>

### 52. q-437

A company operates an ecommerce website on Amazon EC2 instances behind an Application Load Balancer (ALB) in an Auto Scaling group. The site is experiencing performance issues related to a high request rate from illegitimate external systems with changing IP addresses. The security team is worried about potential DDoS attacks against the website. The company must block the illegitimate incoming requests in a way that has a minimal impact on legitimate users. What should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Deploy AWS WAF, associate it with the ALB, and configure a rate-limiting rule.**

AWS WAF is a web application firewall service that helps protect your web applications from common web exploits. It allows you to create rules to filter and monitor HTTP and HTTPS traffic based on conditions that you define. By associating AWS WAF with the ALB, you can inspect and filter incoming traffic before it reaches your instances, providing a layer of protection against DDoS attacks and other malicious activities.

</details>

### 53. q-441 `cost`

A company hosts a multi-tier web application on Amazon Linux Amazon EC2 instances behind an Application Load Balancer. The instances run in an Auto Scaling group across multiple Availability Zones. The company observes that the Auto Scaling group launches more On-Demand Instances when the application's end users access high volumes of static web content. The company wants to optimize cost. What should a solutions architect do to redesign the application MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon CloudFront distribution to host the static web contents from an Amazon S3 bucket.**

Amazon CloudFront is a content delivery network (CDN) service that delivers static and dynamic web content, including images, videos, CSS, and JavaScript, with low latency and high transfer speeds. It can be used to cache and distribute static content globally, reducing the load on your web servers.  By creating a CloudFront distribution and hosting static web content in an Amazon S3 bucket, you offload the serving of static content to the CDN, which can significantly reduce the load on your EC2 instances.

</details>

### 54. q-444

A company has hired a solutions architect to design a reliable architecture for its application. The application consists of one Amazon RDS DB instance and two manually provisioned Amazon EC2 instances that run web servers. The EC2 instances are located in a single Availability Zone. An employee recently deleted the DB instance, and the application was unavailable for 24 hours as a result. The company is concerned with the overall reliability of its environment. What should the solutions architect do to maximize reliability of the application's infrastructure?

<details><summary>Answer</summary>

**B. Update the DB instance to be Multi-AZ, and enable deletion protection. Place the EC2 instances behind an Application Load Balancer, and run them in an EC2 Auto Scaling group across multiple Availability Zones.**

Multi-AZ RDS Instance: By updating the DB instance to be Multi-AZ, you ensure that there is a standby replica in a different Availability Zone, providing high availability and automatic failover in case of a failure in the primary zone.  Deletion Protection: Enabling deletion protection for the DB instance helps prevent accidental deletion, reducing the risk of downtime caused by human error.

</details>

### 55. q-451

A company is migrating its applications and databases to the AWS Cloud. The company will use Amazon Elastic Container Service (Amazon ECS), AWS Direct Connect, and Amazon RDS. Which activities will be managed by the company's operational team? (Choose three.)

<details><summary>Answer</summary>

**C. Configuration of additional software components on Amazon ECS for monitoring, patch management, log management, and host intrusion detection**

The company's operational team is responsible for configuring additional software components on Amazon ECS, such as monitoring tools, patch management tools, log management systems, and host intrusion detection systems. These components are often specific to the company's requirements and policies.  B. Creation of an Amazon RDS DB instance and configuring the scheduled maintenance window:  The operational team is responsible for creating Amazon RDS DB instances, configuring parameters, and setting up maintenance windows based on the company's operational needs. This includes decisions about the size and type of the RDS instance, storage configuration, and other relevant settings.  F. Encryption of the data that moves in transit through Direct Connect:  While AWS manages the physical infrastructure of Direct Connect, the company's operational team is responsible for configuring encryption for the data in transit over Direct Connect. This includes implementing encryption protocols and ensuring the security of data while it travels between the on-premises data center and AWS.

</details>

### 56. q-452

A company runs a Java-based job on an Amazon EC2 instance. The job runs every hour and takes 10 seconds to run. The job runs on a scheduled interval and consumes 1 GB of memory. The CPU utilization of the instance is low except for short surges during which the job uses the maximum CPU available. The company wants to optimize the costs to run the job. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Copy the code into an AWS Lambda function that has 1 GB of memory. Create an Amazon EventBridge scheduled rule to run the code each hour.**

AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It automatically scales based on the number of requests, making it cost-effective for sporadic workloads. Scheduled Rule with Amazon EventBridge:  Amazon EventBridge allows you to schedule events at specified intervals. By creating a scheduled rule, you can trigger the Lambda function to run the Java-based job every hour.

</details>

### 57. q-457

A company that uses AWS is building an application to transfer data to a product manufacturer. The company has its own identity provider (IdP). The company wants the IdP to authenticate application users while the users use the application to transfer data. The company must use Applicability Statement 2 (AS2) protocol. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Transfer Family to transfer the data. Create an AWS Lambda function for IdP authentication.**

AWS Transfer Family (Option C): AWS Transfer Family is a fully managed service that allows you to transfer files over the internet using a range of protocols, including AS2. You can integrate AWS Transfer Family with your IdP for user authentication. By using a Lambda function, you can customize the authentication process and integrate it with your own IdP.

</details>

### 58. q-461

A company is developing a mobile gaming app in a single AWS Region. The app runs on multiple Amazon EC2 instances in an Auto Scaling group. The company stores the app data in Amazon DynamoDB. The app communicates by using TCP traffic and UDP traffic between the users and the servers. The application will be used globally. The company wants to ensure the lowest possible latency for all users. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Global Accelerator to create an accelerator. Create a Network Load Balancer (NLB) behind an accelerator endpoint that uses Global Accelerator integration and listening on the TCP and UDP ports. Update the Auto Scaling group to register instances on the NLB.**

</details>

### 59. q-462

A company has an application that processes customer orders. The company hosts the application on an Amazon EC2 instance that saves the orders to an Amazon Aurora database. Occasionally when traffic is high the workload does not process orders fast enough. What should a solutions architect do to write the orders reliably to the database as quickly as possible?

<details><summary>Answer</summary>

**B. Write orders to an Amazon Simple Queue Service (Amazon SQS) queue. Use EC2 instances in an Auto Scaling group behind an Application Load Balancer to read from the SQS queue and process orders into the database.**

Amazon SQS, which is a fully managed message queuing service. Writing orders to an SQS queue allows for decoupling the EC2 instances processing the orders from the application writing the orders. EC2 instances in an Auto Scaling group can then read from the SQS queue, ensuring that the processing scales with demand.  Using an Auto Scaling group ensures that you can dynamically adjust the number of EC2 instances based on the workload. This can help handle high traffic efficiently.

</details>

### 60. q-466 `availability`

A company designed a stateless two-tier application that uses Amazon EC2 in a single Availability Zone and an Amazon RDS Multi-AZ DB instance. New company management wants to ensure the application is highly available. What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Configure the application to use Multi-AZ EC2 Auto Scaling and create an Application Load Balancer**

</details>

### 61. q-468

A company is developing a microservices application that will provide a search catalog for customers. The company must use REST APIs to present the frontend of the application to users. The REST APIs must access the backend services that the company hosts in containers in private VPC subnets. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Design a REST API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a private VPC link for API Gateway to access Amazon ECS.**

</details>

### 62. q-483 `cost`

A company containerized a Windows job that runs on .NET 6 Framework under a Windows container. The company wants to run this job in the AWS Cloud. The job runs every 10 minutes. The job’s runtime varies between 1 minute and 3 minutes. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use Amazon Elastic Container Service (Amazon ECS) on AWS Fargate to run the job. Create a scheduled task based on the container image of the job to run every 10 minutes.**

Amazon ECS is a fully managed container orchestration service, and AWS Fargate allows you to run containers without managing the underlying infrastructure. ECS on Fargate is a serverless option, which means you only pay for the vCPU and memory that you use, and it scales automatically to meet the needs of the job.

</details>

### 63. q-486

A company is building a three-tier application on AWS. The presentation tier will serve a static website The logic tier is a containerized application. This application will store data in a relational database. The company wants to simplify deployment and to reduce operational costs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon S3 to host static content. Use Amazon Elastic Container Service (Amazon ECS) with AWS Fargate for compute power. Use a managed Amazon RDS cluster for the database.**

Amazon S3 is a highly scalable and cost-effective storage service that can be used to host static content like a static website. It simplifies the storage and delivery of static assets. AWS Fargate is a serverless compute engine for containers. It allows you to run containers without managing the underlying infrastructure. This simplifies deployment and reduces operational overhead.

</details>

### 64. q-505 `cost`

A company has Amazon EC2 instances that run nightly batch jobs to process data. The EC2 instances run in an Auto Scaling group that uses On- Demand billing. If a job fails on one instance, another instance will reprocess the job. The batch jobs run between 12:00 AM and 06:00 AM local time every day. Which solution will provide EC2 instances to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a new launch template for the Auto Scaling group. Set the instances to Spot Instances. Set a policy to scale out based on CPU usage.**

Spot Instances: Spot Instances allow you to bid for unused EC2 capacity at a potentially lower cost than On-Demand pricing. This can result in significant cost savings for batch jobs that are fault-tolerant and can be interrupted or retried.  Scaling Policy: Setting a policy to scale out based on CPU usage ensures that additional Spot Instances are launched when the demand for processing power increases during batch job execution. This helps in handling varying workloads efficiently.

</details>

### 65. q-508

A company has migrated multiple Microsoft Windows Server workloads to Amazon EC2 instances that run in the us-west-1 Region. The company manually backs up the workloads to create an image as needed. In the event of a natural disaster in the us-west-1 Region, the company wants to recover workloads quickly in the us-west-2 Region. The company wants no more than 24 hours of data loss on the EC2 instances. The company also wants to automate any backups of the EC2 instances. Which solutions will meet these requirements with the LEAST administrative effort? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon EC2-backed Amazon Machine Image (AMI) lifecycle policy to create a backup based on tags. Schedule the backup to run twice daily. Configure the copy to the us-west-2 Region.**

D. Create a backup vault by using AWS Backup. Use AWS Backup to create a backup plan for the EC2 instances based on tag values. Define the destination for the copy as us-west-2. Specify the backup schedule to run twice daily.

</details>

### 66. gh-508

Topic 1
A company has migrated multiple Microsoft Windows Server workloads to Amazon EC2 instances that run in the us-west-1 Region. The company manually backs up the workloads to create an image as needed.
In the event of a natural disaster in the us-west-1 Region, the company wants to recover workloads quickly in the us-west-2 Region. The company wants no more than 24 hours of data loss on the EC2 instances. The company also wants to automate any backups of the EC2 instances.
Which solutions will meet these requirements with the LEAST administrative effort? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon EC2-backed Amazon Machine Image (AMI) lifecycle policy to create a backup based on tags. Schedule the backup to run twice daily. Configure the copy to the us-west-2 Region.**

D. Create a backup vault by using AWS Backup. Use AWS Backup to create a backup plan for the EC2 instances based on tag values. Define the destination for the copy as us-west-2. Specify the backup schedule to run twice daily.

</details>

### 67. q-516 `least-ops`

A company provides an API interface to customers so the customers can retrieve their financial information. Еhe company expects a larger number of requests during peak usage times of the year. The company requires the API to respond consistently with low latency to ensure customer satisfaction. The company needs to provide a compute host for the API. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon API Gateway and AWS Lambda functions with provisioned concurrency.**

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. AWS Lambda is a serverless computing service that automatically scales based on demand. Provisioned concurrency in AWS Lambda allows you to set a specific number of concurrent executions to ensure that the function is ready to respond quickly to incoming requests.

</details>

### 68. q-522 `least-ops`

A company runs container applications by using Amazon Elastic Kubernetes Service (Amazon EKS). The company's workload is not consistent throughout the day. The company wants Amazon EKS to scale in and out according to the workload. Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**B. Use the Kubernetes Metrics Server to activate horizontal pod autoscaling.**

Kubernetes supports Horizontal Pod Autoscaling (HPA) based on custom metrics or resource metrics. By using the Kubernetes Metrics Server, you can enable HPA to automatically adjust the number of pods in a deployment based on observed custom metrics (such as application-specific metrics) or resource metrics (such as CPU or memory usage).  C. Use the Kubernetes Cluster Autoscaler:  The Kubernetes Cluster Autoscaler automatically adjusts the size of the cluster by adding or removing nodes based on the resource utilization and pod scheduling requirements. This helps in scaling the cluster itself based on the overall demand.

</details>

### 69. q-523

A company runs a microservice-based serverless web application. The application must be able to retrieve data from multiple Amazon DynamoDB tables A solutions architect needs to give the application the ability to retrieve the data with no impact on the baseline performance of the application. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**Use AWS AppSync pipeline resolvers.**

AppSync is a managed GraphQL front end for serverless applications, and a pipeline resolver runs an ordered series of functions inside one request, each attached to its own data source. That lets a single request gather data from several DynamoDB tables in the managed service layer, so the application's existing code path is untouched and its baseline performance is unaffected, and there is no new infrastructure to run. Lambda@Edge would mean writing and deploying edge functions that still have to call DynamoDB back in the table's region, which is more work and slower, and an edge-optimized API Gateway endpoint only changes where the connection is terminated.

</details>

### 70. q-527

A company has a regional subscription-based streaming service that runs in a single AWS Region. The architecture consists of web servers and application servers on Amazon EC2 instances. The EC2 instances are in Auto Scaling groups behind Elastic Load Balancers. The architecture includes an Amazon Aurora global database cluster that extends across multiple Availability Zones. The company wants to expand globally and to ensure that its application has minimal downtime. Which solution will provide the MOST fault tolerance?

<details><summary>Answer</summary>

**D. Deploy the web tier and the application tier to a second Region. Use an Amazon Aurora global database to deploy the database in the primary Region and the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. Promote the secondary to primary as needed.**

An Aurora global database allows you to replicate your database across multiple AWS Regions. This ensures that you have a read-capable secondary database in the second Region, providing low-latency access to the database. Amazon Route 53 can be configured with health checks to monitor the health of the web and application tiers in both Regions. In the event of a failure in the primary Region, Route 53 can automatically route traffic to the healthy resources in the second Region.

</details>

### 71. q-531

A company needs to integrate with a third-party data feed. The data feed sends a webhook to notify an external service when new data is ready for consumption. A developer wrote an AWS Lambda function to retrieve data when the company receives a webhook callback. The developer must make the Lambda function available for the third party to call. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**Create a function URL for the Lambda function, and give that URL to the third party as the webhook target.**

A Lambda function URL is a built-in feature of the function: turning it on produces a permanent HTTPS address of the form https://<id>.lambda-url.<region>.on.aws that invokes the function directly, with no other service to create, configure or pay for. Access can be left open for a public webhook or restricted to signed IAM callers, which covers what a third-party feed needs. API Gateway in front of the function would also work and is the right choice when you need request throttling, API keys, custom authorizers, a custom domain or AWS WAF, but for simply handing a callback address to one partner it is extra setup for no benefit.

</details>

### 72. q-552

A company needs to optimize the cost of its Amazon EC2 instances. The company also needs to change the type and family of its EC2 instances every 2-3 months. What should the company do to meet these requirements?

<details><summary>Answer</summary>

**B. Purchase a No Upfront Compute Savings Plan for a 1-year term.**

WHat is Upfront --- You don't pay anything upfront. You receive a smaller discount, but you free up capital for other projects.  A No Upfront option means no upfront payment is required, which provides flexibility.  1-year Term: A 1-year term aligns with the company's need to change the type and family of its EC2 instances every 2-3 months. While Compute Savings Plans have a commitment term, choosing a 1-year term allows for more frequent adjustments compared to a 3-year term.

</details>

### 73. q-559

A company hosts multiple applications on AWS for different product lines. The applications use different compute resources, including Amazon EC2 instances and Application Load Balancers. The applications run in different AWS accounts under the same organization in AWS Organizations across multiple AWS Regions. Teams for each product line have tagged each compute resource in the individual accounts. The company wants more details about the cost for each product line from the consolidated billing feature in Organizations. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Select a specific user-defined tag in the AWS Billing console.**

E. Activate the selected tag from the Organizations management account.  User-defined tags are tags that you create and attach to your AWS resources. In this case, since teams for each product line have tagged each compute resource with user-defined tags, selecting a specific user-defined tag in the AWS Billing console allows you to filter costs based on those tags.  The consolidated billing feature in AWS Organizations allows you to view and manage costs across multiple AWS accounts. By activating the selected tag from the Organizations management account, you ensure that the tagged resources from all linked accounts are included in the consolidated billing report. This enables you to get detailed cost information for each product line.

</details>

### 74. gh-559

559Topic 1
A company hosts multiple applications on AWS for different product lines. The applications use different compute resources, including Amazon EC2 instances and Application Load Balancers. The applications run in different AWS accounts under the same organization in AWS Organizations across multiple AWS Regions. Teams for each product line have tagged each compute resource in the individual accounts.
The company wants more details about the cost for each product line from the consolidated billing feature in Organizations.
Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Select a specific user-defined tag in the AWS Billing console.**

E. Activate the selected tag from the Organizations management account.

User-defined tags are tags that you create and attach to your AWS resources. In this case, since teams for each product line have tagged each compute resource with user-defined tags, selecting a specific user-defined tag in the AWS Billing console allows you to filter costs based on those tags.

The consolidated billing feature in AWS Organizations allows you to view and manage costs across multiple AWS accounts. By activating the selected tag from the Organizations management account, you ensure that the tagged resources from all linked accounts are included in the consolidated billing report. This enables you to get detailed cost information for each product line.

</details>

### 75. q-562

A solutions architect needs to ensure that API calls to Amazon DynamoDB from Amazon EC2 instances in a VPC do not travel across the internet. Which combination of steps should the solutions architect take to meet this requirement? (Choose two.)

<details><summary>Answer</summary>

**A. Create a route table entry for the endpoint.**

B. Create a gateway endpoint for DynamoDB.

</details>

### 76. gh-563 `least-ops`

clusters and workloads from a central location.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Use Amazon EKS Connector to register and connect the Kubernetes clusters that run outside Amazon EKS, so every cluster can be seen and managed from the EKS console.**

EKS Connector installs a small agent into a Kubernetes cluster that AWS does not run - on premises, self-managed on EC2, or on another cloud provider - and registers that cluster with Amazon EKS, so it appears in the EKS console alongside the native EKS clusters with its nodes and workloads visible. That gives one place to see every cluster without standing up and maintaining a separate management tool, which is the least operational overhead of the options. EKS Anywhere is for running an AWS-supported Kubernetes distribution in your own data centre, and EKS Distro is only the open-source build of Kubernetes that EKS is based on; neither gives a single central view of clusters you already have.

</details>

### 77. q-570 `least-ops`

A company has a large workload that runs every Friday evening. The workload runs on Amazon EC2 instances that are in two Availability Zones in the us-east-1 Region. Normally, the company must run no more than two instances at all times. However, the company wants to scale up to six instances each Friday to handle a regularly repeating increased workload. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Auto Scaling group that has a scheduled action.**

By creating an Auto Scaling group with a scheduled action, you can configure the group to automatically adjust the desired capacity based on a specified schedule. In this case, you can set up a scheduled action to increase the desired capacity to six instances every Friday evening.

</details>

### 78. q-576

A company is building a RESTful serverless web application on AWS by using Amazon API Gateway and AWS Lambda. The users of this web application will be geographically distributed, and the company wants to reduce the latency of API requests to these users. Which type of endpoint should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**An edge-optimized API endpoint.**

With an edge-optimized endpoint, API Gateway puts a CloudFront distribution that it manages in front of your API, so a request from a geographically distant user enters the AWS network at the nearest edge location and travels the rest of the way over the AWS backbone instead of the public internet. That cuts the latency of connection setup and transit for scattered users, which is what the requirement asks for. A regional endpoint sends clients straight to the API in its own region and is the better choice when callers are in that same region or when you want to run your own CloudFront distribution; a private endpoint is reachable only from inside a VPC.

</details>

### 79. q-584

A company is deploying an application that processes large quantities of data in parallel. The company plans to use Amazon EC2 instances for the workload. The network architecture must be configurable to prevent groups of nodes from sharing the same underlying hardware. Which networking solution meets these requirements?

<details><summary>Answer</summary>

**A. Run the EC2 instances in a spread placement group.**

A spread placement group is a logical grouping of instances that are placed on distinct underlying hardware. This ensures that instances within the group are physically separated, reducing the risk of correlated failures. This option is suitable for applications that need to maximize the level of isolation.

</details>

### 80. q-589 `availability`

A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer that has sticky sessions enabled. The web server currently hosts the user session state. The company wants to ensure high availability and avoid user session state loss in the event of a web server outage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon ElastiCache for Redis to store the session state. Update the application to use ElastiCache for Redis to store the session state.**

ElastiCache for Redis is an in-memory data store service that is well-suited for storing session data. It provides high availability and durability. Using Redis allows the application to offload the session state from individual EC2 instances to a centralized and highly available Redis cluster.

</details>

### 81. q-594

A company plans to migrate to AWS and use Amazon EC2 On-Demand Instances for its application. During the migration testing phase, a technical team observes that the application takes a long time to launch and load memory to become fully productive. Which solution will reduce the launch time of the application during the next testing phase?

<details><summary>Answer</summary>

**C. Launch the EC2 On-Demand Instances with hibernation turned on. Configure EC2 Auto Scaling warm pools during the next testing phase.**

When you launch EC2 On-Demand Instances with hibernation turned on, the instances can be hibernated and resumed rather than terminated and launched.

</details>

### 82. q-595 `cost`

A company's applications run on Amazon EC2 instances in Auto Scaling groups. The company notices that its applications experience sudden traffic increases on random days of the week. The company wants to maintain application performance during sudden traffic increases. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use dynamic scaling to change the size of the Auto Scaling group.**

Dynamic Scaling: With dynamic scaling, the Auto Scaling group automatically adjusts its capacity based on real-time demand. It scales out during traffic spikes and scales in during periods of lower demand. This ensures that your application can handle sudden increases in traffic without manual intervention.

</details>

### 83. q-597

A company hosts an internal serverless application on AWS by using Amazon API Gateway and AWS Lambda. The company’s employees report issues with high latency when they begin using the application each day. The company wants to reduce latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up a scheduled scaling to increase Lambda provisioned concurrency before employees begin to use the application each day.**

Lambda Provisioned Concurrency: Provisioned concurrency is the number of simultaneous executions that your function can handle. By setting up a scheduled scaling to increase Lambda provisioned concurrency before employees begin using the application, you are proactively ensuring that there are enough resources available to handle the expected load.

</details>

### 84. q-611

A company has an application with a REST-based interface that allows data to be received in near-real time from a third-party vendor. Once received, the application processes and stores the data for further analysis. The application is running on Amazon EC2 instances. The third-party vendor has received many 503 Service Unavailable Errors when sending data to the application. When the data volume spikes, the compute capacity reaches its maximum limit and the application is unable to process all requests. Which design should a solutions architect recommend to provide a more scalable solution?

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Streams to ingest the data. Process the data using AWS Lambda functions.**

Kinesis Data Streams is designed for ingesting and processing real-time streaming data at scale. It can handle large volumes of data and provides the ability to scale horizontally.  Using Lambda functions allows for serverless, event-driven processing of the data. Lambda automatically scales based on the number of incoming events, providing the needed elasticity to handle spikes in data volume without the need to manage underlying infrastructure.

</details>

### 85. q-614

A company is designing a new multi-tier web application that consists of the following components: • Web and application servers that run on Amazon EC2 instances as part of Auto Scaling groups • An Amazon RDS DB instance for data storage A solutions architect needs to limit access to the application servers so that only the web servers can access them. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Deploy an Application Load Balancer with a target group that contains the application servers' Auto Scaling group. Configure the security group to allow only the web servers to access the application servers.**

An ALB is a load balancer service provided by AWS that allows you to distribute incoming application traffic across multiple targets, such as EC2 instances. In this scenario, the ALB is deployed in front of the application servers. The ALB is configured with a target group that includes the application servers' Auto Scaling group instances. The target group defines where the ALB directs traffic.

</details>

### 86. q-615

A company runs a critical, customer-facing application on Amazon Elastic Kubernetes Service (Amazon EKS). The application has a microservices architecture. The company needs to implement a solution that collects, aggregates, and summarizes metrics and logs from the application in a centralized location. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Configure Amazon CloudWatch Container Insights in the existing EKS cluster. View the metrics and logs in the CloudWatch console.**

CloudWatch Container Insights is specifically designed for monitoring containerized applications on Amazon EKS and ECS. It provides visibility into the performance of containers, clusters, and microservices.

</details>

### 87. q-630 `cost`

A solutions architect is creating a data processing job that runs once daily and can take up to 2 hours to complete. If the job is interrupted, it has to restart from the beginning. How should the solutions architect address this issue in the MOST cost-effective manner?

<details><summary>Answer</summary>

**C. Use an Amazon Elastic Container Service (Amazon ECS) Fargate task triggered by an Amazon EventBridge scheduled event.**

ECS Fargate is a serverless container service, and it abstracts away the underlying infrastructure. With Fargate, you don't need to manage or provision EC2 instances directly. You can run containers without worrying about the infrastructure, and AWS takes care of scaling and resource allocation.

</details>

### 88. q-635 `least-ops`

A company uses Amazon FSx for NetApp ONTAP in its primary AWS Region for CIFS and NFS file shares. Applications that run on Amazon EC2 instances access the file shares. The company needs a storage disaster recovery (DR) solution in a secondary Region. The data that is replicated in the secondary Region needs to be accessed by using the same protocols as the primary Region. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create an FSx for ONTAP instance in the secondary Region. Use NetApp SnapMirror to replicate data from the primary Region to the secondary Region.**

FSx for ONTAP supports NetApp SnapMirror, which is a robust data replication technology. You can use SnapMirror to replicate data from the primary FSx for ONTAP instance in the primary Region to an FSx for ONTAP instance in the secondary Region.

</details>

### 89. q-642

A company wants to run a gaming application on Amazon EC2 instances that are part of an Auto Scaling group in the AWS Cloud. The application will transmit data by using UDP packets. The company wants to ensure that the application can scale out and in as traffic increases and decreases. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Attach a Network Load Balancer to the Auto Scaling group.**

UDP is a connectionless protocol, and Network Load Balancers (NLB) support UDP, making them suitable for applications that use UDP for transmitting data.

</details>

### 90. q-660

A company hosts an application on Amazon EC2 On-Demand Instances in an Auto Scaling group. Application peak hours occur at the same time each day. Application users report slow application performance at the start of peak hours. The application performs normally 2-3 hours after peak hours begin. The company wants to ensure that the application works properly at the start of peak hours. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a scheduled scaling policy for the Auto Scaling group to launch new instances before peak hours.**

Proactively scales instances to handle predictable traffic spikes. Dynamic scaling (Options B/C) reacts too slowly for known peaks.

</details>

### 91. gh-664

A company has a web application that runs on premises. The application experiences latency issues during peak hours. The latency issues occur
twice each month. At the start of a latency issue, the application's CPU utilization immediately increases to 10 times its normal amount.
The company wants to migrate the application to AWS to improve latency. The company also wants to scale the application automatically when
application demand increases. The company will use AWS Elastic Beanstalk for application deployment.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: A) Use Elastic Beanstalk with burstable instances (unlimited mode) + request-based scaling.**

Burstable instances handle CPU spikes cost-effectively. Request-based scaling matches demand.
Compute-optimized instances (Option B) are overprovisioned for intermittent spikes.

</details>

### 92. gh-671

A company runs its applications on Amazon EC2 instances. The company performs periodic nancial assessments of its AWS costs. The
company recently identi ed unusual spending.
The company needs a solution to prevent unusual spending. The solution must monitor costs and notify responsible stakeholders in the event of
unusual spending.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Create an AWS Cost Anomaly Detection monitor.**

Cost Anomaly Detection applies machine learning to your AWS cost and usage data and raises an alert when spend departs from the learned pattern, naming the service, linked account, cost category or tag the unexpected charges came from. Alerts go to email or to an Amazon SNS topic, either one at a time or as a daily or weekly summary, so the responsible stakeholders hear about it without anyone running a manual review. CloudWatch can also detect anomalies in a metric, but the only billing data it holds is the coarse EstimatedCharges metric in us-east-1, so it cannot break spend down by service or account; AWS Budgets is useful alongside this but fires on thresholds you set yourself rather than on unusual patterns.

</details>

### 93. gh-677 `cost`

A company is developing an application that will run on a production Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster
has managed node groups that are provisioned with On-Demand Instances.
The company needs a dedicated EKS cluster for development work. The company will use the development cluster infrequently to test the
resiliency of the application. The EKS cluster must manage all the nodes.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Create an EKS managed node group that contains only Spot Instances.**

Spot Instances are the cheapest way to get EC2 capacity, at a steep discount to On-Demand, and the trade-off - the instance can be reclaimed at short notice - does not matter for a development cluster used occasionally to test how the application copes with failure. EKS managed node groups support Spot capacity directly and handle provisioning, draining on interruption and version upgrades, so the requirement that the cluster manage all the nodes is met. Mixing in On-Demand Instances raises the bill without meeting any stated requirement, and a self-managed Auto Scaling group with bootstrap scripts hands node management back to you.

</details>
