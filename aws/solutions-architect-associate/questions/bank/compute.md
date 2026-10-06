# Compute — EC2, Lambda, containers, scaling

262 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

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

### 2. dt-3

A user has launched an EC2 instance. The instance got terminated as soon as it was launched. Which of the below mentioned options is not a possible reason for this?

<details><summary>Answer</summary>

**D. The user account has reached the maximum EC2 instance limit.**

</details>

### 3. wl-4

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

### 4. wl-5

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

### 5. wl-6

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

### 6. q-8

A company is migrating a distributed application to AWS. The application serves variable workloads. The legacy platform consists of a primary server that coordinates jobs across multiple compute nodes. The company wants to modernize the application with a solution that maximizes resiliency and scalability. How should a solutions architect design the architecture to meet these requirements?

<details><summary>Answer</summary>

**B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination for the jobs. Implement the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure EC2 Auto Scaling based on the size of the queue.**

Option B: This option provides a decoupled architecture where the jobs are sent to an SQS queue. The compute nodes (EC2 instances in an Auto Scaling group) can then process these jobs. Scaling based on the size of the SQS queue (the number of messages) allows the architecture to adapt to variable workloads, scaling out when the queue depth increases and scaling in when the depth decreases.

</details>

### 7. dt-12

In Amazon EC2 Container Service, are other container types supported?

<details><summary>Answer</summary>

**C. No, Docker is the only container platform supported by EC2 Container Service presently.**

</details>

### 8. dt-14

Name the disk storage supported by Amazon Elastic Compute Cloud (EC2)

<details><summary>Answer</summary>

**D. Amazon Instance Store.**

</details>

### 9. wl-19

Which of the following are not backup and restore solutions provided by AWS? (choose multiple)

<details><summary>Answer</summary>

**C. AWS Elastic Beanstalk; E.**

Option A is snapshot based data backup solution.
Option B, AWS Storage Gateway provides multiple solutions for backup & recovery.
Option D can be used as a Database backup solution.

</details>

### 10. dt-20

Select the most correct The device name /dev/sdal (within Amazon EC2) is [...].

<details><summary>Answer</summary>

**B. reserved for the root device.**

</details>

### 11. wl-20

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

### 12. dt-29

What is the network performance offered by the c4.8xlarge instance in Amazon EC2?

<details><summary>Answer</summary>

**B. 10 Gigabit.**

</details>

### 13. dt-35

What does Amazon Elastic Beanstalk provide?

<details><summary>Answer</summary>

**B. An application container on top of Amazon Web Services.**

</details>

### 14. dt-45 `availability`

A user is planning a highly available application deployment with EC2. Which of the below mentioned options will not help to achieve HA?

<details><summary>Answer</summary>

**B. PIOPS.**

</details>

### 15. dt-47

Which of the following statements is true of tagging an Amazon EC2 resource?

<details><summary>Answer</summary>

**C. You can't terminate, stop, or delete a resource based solely on its tags.**

</details>

### 16. q-47

A company needs guaranteed Amazon EC2 capacity in three specific Availability Zones in a specific AWS Region for an upcoming event that will last 1 week. What should the company do to guarantee the EC2 capacity?

<details><summary>Answer</summary>

**D. Create an On-Demand Capacity Reservation that specifies the Region and three Availability Zones needed.**

An On-Demand Capacity Reservation is a type of Amazon EC2 reservation that enables you to create and manage reserved capacity on Amazon EC2. With an On-Demand Capacity Reservation, you can specify the Region and Availability Zones where you want to reserve capacity, and the number of EC2 instances you want to reserve. This allows you to guarantee capacity in specific Availability Zones in a specific Region.

</details>

### 17. q-48 `availability`

A company's website uses an Amazon EC2 instance store for its catalog of items. The company wants to make sure that the catalog is highly available and that the catalog is stored in a durable location. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Move the catalog to an Amazon Elastic File System (Amazon EFS) file system.**

EFS is fully managed, durable, highly available, and shared file system.

</details>

### 18. dt-49

Are Reserved Instances available for Multi-AZ Deployments?

<details><summary>Answer</summary>

**B. Yes for all instance types.**

</details>

### 19. q-51

A company is developing an application that provides order shipping statistics for retrieval by a REST API. The company wants to extract the shipping statistics, organize the data into an easy-to-read HTML format, and send the report to several email addresses at the same time every morning. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**Both of the following: (1) Create an Amazon EventBridge scheduled event that invokes an AWS Lambda function to query the application's API for the data; and (2) use Amazon Simple Email Service (Amazon SES) to send the report by email.**

The report has to go out at the same time every morning, which is exactly what an EventBridge schedule does, and the thing it triggers needs to call a REST API and build HTML, which is ordinary Lambda work with no servers to run. Amazon SES then delivers the HTML message to the list of recipients in one send, and it is the AWS service meant for sending application email to real mailboxes. An SNS topic can notify subscribers but is not suited to delivering a formatted HTML report, and a Glue job is for extract-transform-load work over data stores, not for calling an API and emailing a page.

</details>

### 20. dt-53 `cost`

To serve Web traffic for a popular product your chief financial officer and IT director have purchased 10 ml large heavy utilization Reserved Instances (RIs) evenly spread across two Availability Zones. Route 53 is used to deliver the traffic to an Elastic Load Balancer (ELB). After several months, the product grows even more popular and you need additional capacity. As a result, your company purchases two C3.2xlarge medium utilization RIs. You register the two c3 2xlarge instances with your ELB and quickly find that the ml large instances are at 100% of capacity and the c3 2xlarge instances have significant capacity that's unused. Which option is the most cost effective and uses EC2 capacity most effectively?

<details><summary>Answer</summary>

**A. Use a separate ELB for each instance type and distribute load to ELBs with Route 53 weighted round robin.**

</details>

### 21. dt-55

A user has launched one EC2 instance in the US West region. The user wants to access the RDS instance launched in the US East region from that EC2 instance. How can the user configure the access for that EC2 instance?

<details><summary>Answer</summary>

**A. Configure the IP range of the US West region instance as the ingress security rule of RDS.**

</details>

### 22. dt-57

While creating an Amazon RDS DB, your first task is to set up a DB [...] that controls which IP address or EC2 instance can access your DB Instance.

<details><summary>Answer</summary>

**D. security group.**

</details>

### 23. dt-59

In the context of AWS support, why must an EC2 instance be unreachable for 20 minutes rather than allowing customers to open tickets immediately?

<details><summary>Answer</summary>

**A. Because most reachability issues are resolved by automated processes in less than 20 minutes.**

</details>

### 24. dt-62

While creating the snapshots using the command line tools, which command should I be using?

<details><summary>Answer</summary>

**C. ec2-create-snapshot.**

</details>

### 25. dt-63

All Amazon EC2 instances are assigned two IP addresses at launch, out of which one can only be reached from within the Amazon EC2 network?

<details><summary>Answer</summary>

**C. Private IP address.**

</details>

### 26. dt-65

You've created your first load balancer and have registered your EC2 instances with the load balancer. Elastic Load Balancing routinely performs health checks on all the registered EC2 instances and automatically distributes all incoming requests to the DNS name of your load balancer across your registered, healthy EC2 instances. By default, the load balancer uses the [...] protocol for checking the health of your instances.

<details><summary>Answer</summary>

**B. HTTP.**

</details>

### 27. dt-66

Amazon Elastic Load Balancing is used to manage traffic on a fleet of Amazon EC2 instances, distributing traffic to instances across all Availability Zones within a region. Elastic Load Balancing has all the advantages of an on-premises load balancer, plus several security benefits. Which of the following is not an advantage of ELB over an on-premise load balancer?

<details><summary>Answer</summary>

**A. ELB uses a four-tier, key-based architecture for encryption.**

</details>

### 28. dt-67 `availability`

A web company is looking to implement an external payment service into their highly available application deployed in a VPC. Their application EC2 instances are behind a public facing ELB. Auto scaling is used to add additional instances as traffic increases. Under normal load the application runs 2 instances in the Auto Scaling group but at peak it can scale 3x in size. The application instances need to communicate with the payment service over the Internet which requires whitelisting of all public IP addresses used to communicate with it. A maximum of 4 whitelisting IP addresses are allowed at a time and can be added through an API. How should they architect their solution?

<details><summary>Answer</summary>

**A. Route payment requests through two NAT instances setup for High Availability and whitelist the Elastic IP addresses attached to the NAT instances.**

</details>

### 29. dt-74

You are trying to launch an EC2 instance, however the instance seems to go into a terminated status immediately. What would probably not be a reason that this is happening?

<details><summary>Answer</summary>

**C. You need to create storage in EBS first.**

</details>

### 30. dt-78

Your company produces customer commissioned one-of-a-kind skiing helmets combining high fashion with custom technical enhancements. Customers can show off their Individuality on the ski slopes and have access to head-up-displays. GPS rear-view cams and any other technical innovation they wish to embed in the helmet. The current manufacturing process is data rich and complex including assessments to ensure that the custom electronics and materials used to assemble the helmets are to the highest standards. Assessments are a mixture of human and automated assessments you need to add a new set of assessment to model the failure modes of the custom electronics using GPUs with CUDA, across a cluster of servers with low latency networking. What architecture would allow you to automate the existing process using a hybrid approach and ensure that the architecture can support the evolution of processes over time?

<details><summary>Answer</summary>

**B. Use Amazon Simple Workflow (SWF) to manages assessments, movement of data & meta-data Use an auto-scaling group of G2 instances in a placement group.**

</details>

### 31. dt-89

A user is aware that a huge download is occurring on his instance. He has already set the Auto Scaling policy to increase the instance count when the network I/O increases beyond a certain limit. How can the user ensure that this temporary event does not result in scaling?

<details><summary>Answer</summary>

**D. Suspend scaling.**

</details>

### 32. dt-90

The Amazon EC2 web service can be accessed using the [...] web services messaging protocol. This interface is described by a Web Services Description Language (WSDL) document.

<details><summary>Answer</summary>

**A. SOAP.**

</details>

### 33. dt-103

What is a Security Group?

<details><summary>Answer</summary>

**D. A firewall for inbound traffic, built-in around every Amazon EC2 instance.**

</details>

### 34. dt-111

You have been given a scope to deploy some AWS infrastructure for a large organization. The requirements are that you will have a lot of EC2 instances but may need to add more when the average utilization of your Amazon EC2 fleet is high and conversely remove them when CPU utilization is low. Which AWS services would be best to use to accomplish this?

<details><summary>Answer</summary>

**B. Auto Scaling, Amazon CloudWatch and Elastic Load Balancing.**

</details>

### 35. dt-112

When does the billing of an Amazon EC2 system begin?

<details><summary>Answer</summary>

**D. It starts when Amazon EC2 initiates the boot sequence of an AMI instance.**

</details>

### 36. dt-117

Can you move a Reserved Instance from one Availability Zone to another?

<details><summary>Answer</summary>

**A. Yes, but each Reserved Instance is associated with a specific Region that cannot be changed.**

</details>

### 37. dt-121

Which of the following statements best describes the differences between Elastic Beanstalk and CloudFormation?

<details><summary>Answer</summary>

**D. CloudFormation is much more powerful than Elastic Beanstalk, because you can actually design and script custom resources.**

</details>

### 38. dt-125

Does AWS CloudFormation support Amazon EC2 tagging?

<details><summary>Answer</summary>

**A. Yes, AWS CloudFormation supports Amazon EC2 tagging.**

</details>

### 39. dt-128

To specify a resource in a policy statement, in Amazon EC2, can you use its Amazon Resource Name (ARN)?

<details><summary>Answer</summary>

**A. Yes, you can.**

</details>

### 40. dt-130

By default what are ENIs that are automatically created and attached to instances using the EC2 console set to do when the attached instance terminates?

<details><summary>Answer</summary>

**B. Terminate.**

</details>

### 41. dt-131

In EC2, what happens to the data in an instance store if an instance reboots (either intentionally or unintentionally)?

<details><summary>Answer</summary>

**B. Data persists in the instance store.**

</details>

### 42. dt-141

All Amazon EC2 instances are assigned two IP addresses at launch. Which are those?

<details><summary>Answer</summary>

**D. A private IP address and a public IP address.**

</details>

### 43. dt-142

You need to pass a custom script to new Amazon Linux instances created in your Auto Scaling group. Which feature allows you to accomplish this?

<details><summary>Answer</summary>

**A. User data.**

</details>

### 44. dt-144

Which DNS name can only be resolved within Amazon EC2?

<details><summary>Answer</summary>

**B. Internal DNS name.**

</details>

### 45. dt-145

An AWS customer is deploying an application that is composed of an AutoScaling group of EC2 Instances. The customers security policy requires that every outbound connection from these instances to any other service within the customers Virtual Private Cloud must be authenticated using a unique x 509 certificate that contains the specific instance-id. In addition an x 509 certificates must be designed by the customer's Key management service in order to be trusted for authentication. Which of the following configurations will support these requirements?

<details><summary>Answer</summary>

**C. Configure the Auto Scaling group to send an SNS notification of the launch of a new instance to the trusted key management service. Have the Key management service generate a signed certificate and send it directly to the newly launched instance.**

</details>

### 46. dt-147

In Amazon EC2, you are billed instance-hours when [...].

<details><summary>Answer</summary>

**A. your EC2 instance is in a running state.**

</details>

### 47. dt-149

In Amazon EC2 Container Service components, what is the name of a logical grouping of container instances on which you can place tasks?

<details><summary>Answer</summary>

**A. A cluster.**

</details>

### 48. dt-164

A major customer has asked you to set up his AWS infrastructure so that it will be easy to recover in the case of a disaster of some sort. Which of the following statements is true of Amazon EC2 security groups?

<details><summary>Answer</summary>

**D. All items listed here are important when thinking about disaster recovery.**

</details>

### 49. dt-165

Select a true statement about Amazon EC2 Security Groups (EC2-Classic).

<details><summary>Answer</summary>

**A. After you launch an instance in EC2-Classic, you can't change its security groups.**

</details>

### 50. dt-168

You have an EC2 Security Group with several running EC2 instances. You change the Security Group rules to allow inbound traffic on a new port and protocol, and launch several new instances in the same Security Group. The new rules apply:

<details><summary>Answer</summary>

**A. Immediately to all instances in the security group.**

</details>

### 51. dt-173

You try to connect via SSH to a newly created Amazon EC2 instance and get one of the following error messages: 'Network error: Connection timed out' or 'Error connecting to [instance], reason: -> Connection timed out: connect,' You have confirmed that the network and security group rules are configured correctly and the instance is passing status checks. What steps should you take to identify the source of the behavior? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Verify that the private key file corresponds to the Amazon EC2 key pair assigned at launch.; C. Verify that you are connecting with the appropriate user name for your AMI.**

</details>

### 52. dt-174

An Auto-Scaling group spans 3 AZs and currently has 4 running EC2 instances. When Auto Scaling needs to terminate an EC2 instance by default, AutoScaling will: (Choose 2 answers)

<details><summary>Answer</summary>

**C. Send an SNS notification, if configured to do so.; D. Terminate an instance in the AZ which currently has 2 running EC2 instances.**

</details>

### 53. q-190 `availability`

A company has a web application that is based on Java and PHP. The company plans to move the application from on premises to AWS. The company needs the ability to test new site features frequently. The company also needs a highly available and managed solution that requires minimum operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the web application to an AWS Elastic Beanstalk environment. Use URL swapping to switch between multiple Elastic Beanstalk environments for feature testing.**

Elastic Beanstalk allows you to perform blue-green deployments, which involve creating a new environment (green) with the updated code, testing it, and then swapping the URLs to direct traffic to the new environment. This enables you to test new features without affecting the production environment.

</details>

### 54. dt-201

Which Amazon Elastic Compute Cloud feature can you query from within the instance to access instance properties?

<details><summary>Answer</summary>

**C. Instance metadata.**

</details>

### 55. q-203

The customers of a finance company request appointments with financial advisors by sending text messages. A web application that runs on Amazon EC2 instances accepts the appointment requests. The text messages are published to an Amazon Simple Queue Service (Amazon SQS) queue through the web application. Another application that runs on EC2 instances then sends meeting invitations and meeting confirmation email messages to the customers. After successful scheduling, this application stores the meeting information in an Amazon DynamoDB database. As the company expands, customers report that their meeting invitations are taking longer to arrive. What should a solutions architect recommend to resolve this issue?

<details><summary>Answer</summary>

**D. Add an Auto Scaling group for the application that sends meeting invitations. Configure the Auto Scaling group to scale based on the depth of the SQS queue.**

To resolve the issue of longer delivery times for meeting invitations, the solutions architect can recommend adding an Auto Scaling group for the application that sends meeting invitations and configuring the Auto Scaling group to scale based on the depth of the SQS queue. This will allow the application to scale up as the number of appointment requests increases, improving the performance and delivery times of the meeting invitations.

</details>

### 56. q-209

A solutions architect is designing the architecture of a new application being deployed to the AWS Cloud. The application will run on Amazon EC2 On-Demand Instances and will automatically scale across multiple Availability Zones. The EC2 instances will scale up and down frequently throughout the day. An Application Load Balancer (ALB) will handle the load distribution. The architecture needs to support distributed session data management. The company is willing to make changes to code if needed. What should the solutions architect do to ensure that the architecture supports distributed session data management?

<details><summary>Answer</summary>

**A. Use Amazon ElastiCache to manage and store session data.**

Amazon ElastiCache is a fully managed, in-memory data store service. It is commonly used for caching and session management in distributed applications. By utilizing ElastiCache for session data management, you can store and retrieve session data in a scalable and high-performance manner. The use of ElastiCache allows for a distributed and shared data store for session management across multiple instances and Availability Zones.

</details>

### 57. dt-214

What is the minimum charge for the data transferred between Amazon RDS and Amazon EC2 Instances in the same Availability Zone?

<details><summary>Answer</summary>

**B. No charge. It is free.**

</details>

### 58. dt-219

[...] let you categorize your EC2 resources in different ways, for example, by purpose, owner, or environment.

<details><summary>Answer</summary>

**C. tags.**

</details>

### 59. dt-220

Which of the below mentioned options is not available when an instance is launched by Auto Scaling with EC2 Classic?

<details><summary>Answer</summary>

**B. Elastic IP.**

</details>

### 60. q-220 `cost`

A solutions architect is designing a new API using Amazon API Gateway that will receive requests from users. The volume of requests is highly variable; several hours can pass without receiving a single request. The data processing will take place asynchronously, but should be completed within a few seconds after a request is made. Which compute service should the solutions architect have the API invoke to deliver the requirements at the lowest cost?

<details><summary>Answer</summary>

**B. An AWS Lambda function**

AWS Lambda supports asynchronous invocation, which is suitable for scenarios where data processing can take place independently of the API request and complete within a few seconds. This aligns with the requirement of processing data asynchronously.

</details>

### 61. dt-228

Which services allow the customer to retain full administrative privileges of the underlying EC2 instances? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Amazon Elastic MapReduce.; E. AWS Elastic Beanstalk.**

</details>

### 62. dt-238

The one-time payment for Reserved Instances is [...] refundable if the reservation is cancelled.

<details><summary>Answer</summary>

**C. never.**

</details>

### 63. dt-239

Is it possible to get a history of all EC2 API calls made on your account for security analysis and operational troubleshooting purposes?

<details><summary>Answer</summary>

**B. Yes, you should turn on the CloudTrail in the AWS console.**

</details>

### 64. dt-243

What are the Amazon EC2 API tools?

<details><summary>Answer</summary>

**B. Command-line tools to the Amazon EC2 web service.**

</details>

### 65. q-245 `cost`

A company is launching an application on AWS. The application uses an Application Load Balancer (ALB) to direct traffic to at least two Amazon EC2 instances in a single target group. The instances are in an Auto Scaling group for each environment. The company requires a development environment and a production environment. The production environment will have periods of high traffic. Which solution will configure the development environment MOST cost-effectively?

<details><summary>Answer</summary>

**Reduce the maximum number of EC2 instances in the development environment's Auto Scaling group.**

Development and production each have their own Auto Scaling group, and only production sees bursts of traffic. Capping the maximum size of the development group stops it from ever scaling out to a production-sized fleet, so development runs the minimum it needs and nothing more. Taking a target out of the development target group saves nothing, because the instance keeps running and billing - the Auto Scaling group still owns it and will simply register it again - and it also contradicts the requirement that the load balancer serve at least two instances. Shrinking instance sizes in both environments would change production as well, and the load balancing algorithm has no bearing on cost.

</details>

### 66. dt-248

Which of the following cannot be used in Amazon EC2 to control who has access to specific Amazon EC2 instances?

<details><summary>Answer</summary>

**B. IAM System.**

</details>

### 67. gh-248

Users report that some submitted data is not being processed Amazon CloudWatch reveals that the EC2 instances have a consistent CPU utilization at or near 100%. The company wants to improve system performance and scale the system based on user load.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Route incoming requests to Amazon Simple Queue Service (Amazon SQS). Configure an EC2 Auto Scaling group based on queue size. Update the software to read from the queue.**

This option addresses the issue by offloading incoming requests to an SQS queue, allowing for decoupling of processing and scaling based on queue size. This helps improve system performance and allows for scaling based on user load.

</details>

### 68. dt-254 `availability`

You have a web application running on six Amazon EC2 instances, consuming about 45% of resources on each instance. You are using auto-scaling to make sure that six instances are running at all times. The number of requests this application processes is consistent and does not experience spikes. The application is critical to your business and you want high availability at all times. You want the load to be distributed evenly between all instances. You also want to use the same Amazon Machine Image (AMI) for all instances. Which of the following architectural choices should you make?

<details><summary>Answer</summary>

**C. Deploy 3 EC2 instances in one Availability Zone and 3 in another Availability Zone and use Amazon Elastic Load Balancer.**

</details>

### 69. dt-257

Amazon EC2 provides a repository of public data sets that can be seamlessly integrated into AWS cloud-based applications. What is the monthly charge for using the public data sets?

<details><summary>Answer</summary>

**D. There is no charge for using the public data sets.**

</details>

### 70. dt-261

You have set up an Auto Scaling group. The cool down period for the Auto Scaling group is 7 minutes. The first instance is launched after 3 minutes, while the second instance is launched after 4 minutes. How many minutes after the first instance is launched will Auto Scaling accept another scaling activity request?

<details><summary>Answer</summary>

**A. 11 minutes.**

</details>

### 71. q-261

A company recently announced the deployment of its retail website to a global audience. The website runs on multiple Amazon EC2 instances behind an Elastic Load Balancer. The instances run in an Auto Scaling group across multiple Availability Zones. The company wants to provide its customers with different versions of content based on the devices that the customers use to access the website. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Configure Amazon CloudFront to cache multiple versions of the content.**

C. Configure a Lambda@Edge function to send specific objects to users based on the User-Agent header.  Amazon CloudFront is a content delivery network (CDN) service that can cache and deliver content globally. Configure CloudFront to cache different versions of content based on the device type or other criteria.  Lambda@Edge allows you to run code in response to CloudFront events globally. Use a Lambda@Edge function to inspect the User-Agent header and dynamically serve different versions of content based on the device type.

</details>

### 72. q-263

A company is building an application that consists of several microservices. The company has decided to use container technologies to deploy its software on AWS. The company needs a solution that minimizes the amount of ongoing effort for maintenance and scaling. The company cannot manage additional infrastructure. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Deploy an Amazon Elastic Container Service (Amazon ECS) cluster.**

D. Deploy an Amazon Elastic Container Service (Amazon ECS) service with a Fargate launch type. Specify a desired task number level of greater than or equal to 2.  An ECS cluster is necessary to organize and manage your Fargate tasks and services. It provides a logical grouping of tasks and services. When using Fargate, you don't need to manage the underlying EC2 instances; the cluster helps manage the Fargate tasks.  Fargate is a serverless compute engine for containers that eliminates the need to manage underlying infrastructure. With Fargate, you do not need to provision or manage EC2 instances; AWS takes care of the infrastructure, allowing you to focus solely on your containers.

</details>

### 73. dt-264

Your system recently experienced down time during the troubleshooting process. You found that a new administrator mistakenly terminated several production EC2 instances. Which of the following strategies will help prevent a similar situation in the future? The administrator still must be able to: Launch, start stop, and terminate development resources. Launch and start production instances.

<details><summary>Answer</summary>

**B. Leverage resource based tagging along with an IAM user, which can prevent specific users from terminating production EC2 resources.**

</details>

### 74. q-266

A company has a popular gaming platform running on AWS. The application is sensitive to latency because latency can impact the user experience and introduce unfair advantages to some players. The application is deployed in every AWS Region. It runs on Amazon EC2 instances that are part of Auto Scaling groups configured behind Application Load Balancers (ALBs). A solutions architect needs to implement a mechanism to monitor the health of the application and redirect traffic to healthy endpoints. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Configure an accelerator in AWS Global Accelerator. Add a listener for the port that the application listens on, and attach it to a Regional endpoint in each Region. Add the ALB as the endpoint.**

AWS Global Accelerator is designed to provide static IP addresses for global applications and direct traffic over the AWS global network to optimal AWS endpoints based on health, geography, and routing policies. Configure an accelerator with a listener for the port that the application listens on. Attach the listener to a Regional endpoint in each AWS Region where the application is deployed.

</details>

### 75. dt-268

You have a periodic Image analysis application that gets some files in input, analyzes them and for each file writes some data in output to a text file. The number of files in input per day is high and concentrated in a few hours of the day. Currently you have a server on EC2 with a large EBS volume that hosts the input data and the results. It takes almost 20 hours per day to complete the process. What services could be used to reduce the elaboration time and improve the availability of the solution?

<details><summary>Answer</summary>

**D. EBS with Provisioned IOPS (PIOPS) to store I/O files. SQS to distribute elaboration commands to a group of hosts working in parallel. Auto Scaling to dynamically size the group of hosts depending on the length of the SQS queue.**

</details>

### 76. dt-269

While controlling access to Amazon EC2 resources, which of the following acts as a firewall that controls the traffic allowed to reach one or more instances?

<details><summary>Answer</summary>

**A. A security group.**

</details>

### 77. dt-271

While using the EC2 GET requests as URLs, the [...] is the URL that serves as the entry point for the web service.

<details><summary>Answer</summary>

**B. endpoint.**

</details>

### 78. q-271

A solutions architect observes that a nightly batch processing job is automatically scaled up for 1 hour before the desired Amazon EC2 capacity is reached. The peak capacity is the ‘same every night and the batch jobs always start at 1 AM. The solutions architect needs to find a cost-effective solution that will allow for the desired EC2 capacity to be reached quickly and allow the Auto Scaling group to scale down after the batch jobs are complete. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Configure scheduled scaling to scale up to the desired compute level.**

Scheduled scaling allows you to define specific times when your Auto Scaling group's desired capacity should be increased or decreased. In this case, you can schedule the scaling action to increase the capacity just before the nightly batch processing job starts at 1 AM and then scale it down after the job completes.

</details>

### 79. dt-274

A user has launched 10 EC2 instances inside a placement group. Which of the below mentioned statements is true with respect to the placement group?

<details><summary>Answer</summary>

**A. All instances must be in the same AZ.**

</details>

### 80. dt-275

A user has created a CloudFormation stack. The stack creates AWS services, such as EC2 instances, ELB, AutoScaling, and RDS. While creating the stack it created EC2, ELB and AutoScaling but failed to create RDS. What will CloudFormation do in this scenario?

<details><summary>Answer</summary>

**A. Rollback all the changes and terminate all the created services.**

</details>

### 81. q-275

A company runs an internal browser-based application. The application runs on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales up to 20 instances during work hours, but scales down to 2 instances overnight. Staff are complaining that the application is very slow when the day begins, although it runs well by mid-morning. How should the scaling be changed to address the staff complaints and keep costs to a minimum?

<details><summary>Answer</summary>

**C. Implement a target tracking action triggered at a lower CPU threshold, and decrease the cooldown period.**

</details>

### 82. dt-276

You have been asked to design the storage layer for an application. The application requires disk performance of at least 100,000 IOPS. In addition, the storage layer must be able to survive the loss of an individual disk, EC2 instance, or Availability Zone without any data loss. The volume you provide must have a capacity of at least 3 TB. Which of the following designs will meet these objectives?

<details><summary>Answer</summary>

**E. Instantiate an i2.8xlarge instance in us-east-1a. Create a RAID 0 volume using the four 800GB SSD ephemeral disks provided with the instance. Configure synchronous, block-level replication to an identically configured instance in us-east-1b.**

</details>

### 83. q-276

A company has a multi-tier application deployed on several Amazon EC2 instances in an Auto Scaling group. An Amazon RDS for Oracle instance is the application’ s data layer that uses Oracle-specific PL/SQL functions. Traffic to the application has been steadily increasing. This is causing the EC2 instances to become overloaded and the RDS instance to run out of storage. The Auto Scaling group does not have any scaling metrics and defines the minimum healthy instance count only. The company predicts that traffic will continue to increase at a steady but unpredictable rate before leveling off. What should a solutions architect do to ensure the system can automatically scale for the increased traffic? (Choose two.)

<details><summary>Answer</summary>

**A. Configure storage Auto Scaling on the RDS for Oracle instance.**

This option allows the RDS instance to automatically scale its storage based on the actual storage usage, ensuring that you don't run out of storage.  D. Configure the Auto Scaling group to use the average CPU as the scaling metric.  By using CPU utilization as a scaling metric, the Auto Scaling group can dynamically adjust the number of EC2 instances based on the application's demand. This helps in handling increased traffic and preventing overload on existing instances.

</details>

### 84. dt-278

Your startup wants to implement an order fulfillment process for selling a personalized gadget that needs an average of 3-4 days to produce with some orders taking up to 6 months. You expect 10 orders per day on your first day, 1000 orders per day after 6 months and 10,000 orders after 12 months. Orders coming in are checked for consistency, then dispatched to your manufacturing plant for production, quality control, packaging, shipment and payment processing. If the product does not meet the quality standards at any stage of the process, employees may force the process to repeat a step. Customers are notified via email about order status and any critical issues with their orders such as payment failure. Your base architecture includes AWS Elastic Beanstalk for your website with an RDS MySQL instance for customer data and orders. How can you implement the order fulfillment process while making sure that the emails are delivered reliably?

<details><summary>Answer</summary>

**C. Use SWF with an Auto Scaling group of activity workers and a decider instance in another Auto Scaling group with min/max=1. Use SES to send emails to customers.**

</details>

### 85. dt-280

A user is accessing an EC2 instance on the SSH port for IP 10.20.30.40. Which one is a secure way to configure that the instance can be accessed only from this IP?

<details><summary>Answer</summary>

**B. In the security group, open port 22 for IP 10.20.30.40/32.**

</details>

### 86. dt-283

You have a content management system running on an Amazon EC2 instance that is approaching 100% CPU utilization. Which option will reduce load on the Amazon EC2 instance?

<details><summary>Answer</summary>

**B. Create a CloudFront distribution, and configure the Amazon EC2 instance as the origin.**

</details>

### 87. dt-286

You have decided to change the instance type for instances running in your application tier that is using Auto Scaling. In which area below would you change the instance type definition?

<details><summary>Answer</summary>

**D. Auto Scaling launch configuration.**

</details>

### 88. dt-287

Which of the following statements is true of creating a launch configuration using an EC2 instance?

<details><summary>Answer</summary>

**B. Auto Scaling automatically creates a launch configuration directly from an EC2 instance.**

</details>

### 89. q-287

A company wants to migrate a Windows-based application from on premises to the AWS Cloud. The application has three tiers: an application tier, a business tier, and a database tier with Microsoft SQL Server. The company wants to use specific features of SQL Server such as native backups and Data Quality Services. The company also needs to share files for processing between the tiers. How should a solutions architect design the architecture to meet these requirements?

<details><summary>Answer</summary>

**B. Host all three tiers on Amazon EC2 instances. Use Amazon FSx for Windows File Server for file sharing between the tiers.**

hosting all three tiers on Amazon EC2 instances allows you to have flexibility and control over the entire application architecture. To address the file-sharing requirement between the tiers, you can use Amazon FSx for Windows File Server.  Amazon FSx for Windows File Server is a fully managed Windows file system that is accessible from Windows-based instances over the Server Message Block (SMB) protocol. It supports the specific features of Windows File Server, including features like native backups and access to Windows-specific services.

</details>

### 90. q-290

A company hosts a web application on multiple Amazon EC2 instances. The EC2 instances are in an Auto Scaling group that scales in response to user demand. The company wants to optimize cost savings without making a long-term commitment. Which EC2 instance purchasing option should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. A mix of On-Demand Instances and Spot Instances**

On-Demand Instances: These instances are charged per hour or per second of usage, without any upfront payment or long-term commitment. While they offer flexibility, they are usually more expensive compared to other purchasing options.  Spot Instances: These are spare compute capacity in the AWS cloud available at a lower price compared to On-Demand Instances. However, they can be terminated by AWS with little notice if the capacity is needed elsewhere. Spot Instances are suitable for workloads that are fault-tolerant and can handle interruptions.

</details>

### 91. dt-293

A user has launched 10 EC2 instances inside a placement group. Which of the following statements is true in regards to what ability launching your instances into a VPC instead of EC2-Classic gives you?

<details><summary>Answer</summary>

**A. All of the things listed here.**

</details>

### 92. dt-295

What is the average IOPS that the user will get for most of the year as per EC2 SLA if the instance is attached to the EBS optimized instance?

<details><summary>Answer</summary>

**D. 900.**

</details>

### 93. gh-297

A solutions architect needs to implement a solution to automate the scalability of the application. The solution must optimize the cost of the architecture and must ensure that the application has enough CPU resources when surges occur.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an EC2 Auto Scaling group. Select the existing ALB as the load balancer and the existing target group as the target group. Set a target tracking scaling policy that is based on the ASGAverageCPUUtilization metric. Set the minimum instances to 2, the desired capacity to 3, the maximum instances to 6, and the target value to 50%. Add the EC2 instances to the Auto Scaling group.**

Option B utilizes EC2 Auto Scaling, which automatically adjusts the number of EC2 instances in the Auto Scaling group based on the specified target tracking scaling policy.
By setting a target tracking scaling policy based on the ASGAverageCPUUtilization metric with a target value of 50%, the Auto Scaling group will dynamically adjust the number of instances to maintain an average CPU utilization close to the target value.
This solution provides scalability when needed, ensures that there are enough CPU resources during surges, and optimizes costs by automatically adjusting the capacity based on demand.

</details>

### 94. dt-299

Please select the Amazon EC2 resource which can be tagged.

<details><summary>Answer</summary>

**C. Placement groups.**

</details>

### 95. q-300 `cost`

A company needs to migrate a legacy application from an on-premises data center to the AWS Cloud because of hardware capacity constraints. The application runs 24 hours a day, 7 days a week. The application’s database storage continues to grow over time. What should a solutions architect do to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Migrate the application layer to Amazon EC2 Reserved Instances. Migrate the data storage layer to Amazon Aurora Reserved Instances.**

Using Amazon EC2 Reserved Instances for the application layer provides cost savings compared to On-Demand Instances while ensuring availability for the 24/7 runtime. Migrating the data storage layer to Amazon Aurora Reserved Instances provides a fully managed relational database service with automatic scaling capabilities. Amazon Aurora is designed for high performance and cost efficiency. Reserved Instances provide cost savings compared to On-Demand Instances over an extended period, making them suitable for applications with continuous operation. Amazon Aurora, being a fully managed service, offloads much of the operational overhead associated with managing a traditional database, making it a cost-effective choice for growing database storage.

</details>

### 96. q-303

A company is launching a new application deployed on an Amazon Elastic Container Service (Amazon ECS) cluster and is using the Fargate launch type for ECS tasks. The company is monitoring CPU and memory usage because it is expecting high traffic to the application upon its launch. However, the company wants to reduce costs when utilization decreases. What should a solutions architect recommend?

<details><summary>Answer</summary>

**D. Use AWS Application Auto Scaling with target tracking policies to scale when ECS metric breaches trigger an Amazon CloudWatch alarm.**

AWS Application Auto Scaling is a service that can automatically adjust the number of running ECS tasks or services based on specified CloudWatch metrics. Target tracking policies allow you to set a target value for a specific metric, and AWS Application Auto Scaling automatically adjusts the desired task count to maintain the target. By using target tracking policies, you can ensure that the ECS cluster scales up or down based on the application's demand while maintaining a balance between cost efficiency and performance.

</details>

### 97. q-306

A company wants to run an in-memory database for a latency-sensitive application that runs on Amazon EC2 instances. The application processes more than 100,000 transactions each minute and requires high network throughput. A solutions architect needs to provide a cost- effective network design that minimizes data transfer charges. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Launch all EC2 instances in the same Availability Zone within the same AWS Region. Specify a placement group with cluster strategy when launching EC2 instances.**

A placement group is a logical grouping of instances within a single Availability Zone. The "cluster" strategy for placement groups places instances in close proximity to each other, providing low-latency, high-throughput communication between instances. By launching all EC2 instances in the same Availability Zone within the same AWS Region, you minimize data transfer charges because data transfer within the same Availability Zone is not subject to additional costs.

</details>

### 98. dt-307

If you want to launch Amazon Elastic Compute Cloud (EC2) instances and assign each instance a predetermined private IP address you should:

<details><summary>Answer</summary>

**B. Assign a group of sequential Elastic IP address to the instances.**

</details>

### 99. dt-309

You have a Business support plan with AWS. One of your EC2 instances is running Microsoft Windows Server 2008 R2 and you are having problems with the software. Can you receive support from AWS for this software?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 100. dt-314

The [...] service is targeted at organizations with multiple users or systems that use AWS products such as Amazon EC2, Amazon SimpleDB, and the AWS Management Console.

<details><summary>Answer</summary>

**C. AWS Identity and Access Management.**

</details>

### 101. dt-317

You have written a CloudFormation template that creates 1 Elastic Load Balancer fronting 2 EC2 Instances. Which section of the template should you edit so that the DNS of the load balancer is returned upon creation of the stack?

<details><summary>Answer</summary>

**B. Outputs.**

</details>

### 102. dt-318

AWS CloudFormation is a service that helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and AWS CloudFormation takes care of provisioning and configuring those resources for you. What formatting is required for this template?

<details><summary>Answer</summary>

**A. JSON-formatted document.**

</details>

### 103. q-318

A company recently migrated its entire IT environment to the AWS Cloud. The company discovers that users are provisioning oversized Amazon EC2 instances and modifying security group rules without using the appropriate change control process. A solutions architect must devise a strategy to track and audit these inventory and configuration changes. Which actions should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Enable AWS CloudTrail and use it for auditing.**

D. Enable AWS Config and create rules for auditing and compliance purposes.  A. Enable AWS CloudTrail and use it for auditing. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS Command Line Interface (CLI), and AWS SDKs and APIs. By enabling CloudTrail, the company can track user activity and changes to AWS resources, and monitor compliance with internal policies and external regulations.  D. Enable AWS Config and create rules for auditing and compliance purposes. AWS Config provides a detailed inventory of the AWS resources in your account, and continuously records changes to the configurations of those resources. By creating rules in AWS Config, the company can automate the evaluation of resource configurations against desired state, and receive alerts when configurations drift from compliance.

</details>

### 104. dt-320

After setting up an EC2 security group with a cluster of 20 EC2 instances, you find an error in the security group settings. You quickly make changes to the security group settings. When will the changes to the settings be effective?

<details><summary>Answer</summary>

**A. The settings will be effective immediately for all the instances in the security group.**

</details>

### 105. q-320

A company is using a fleet of Amazon EC2 instances to ingest data from on-premises data sources. The data is in JSON format and ingestion rates can be as high as 1 MB/s. When an EC2 instance is rebooted, the data in-flight is lost. The company’s data science team wants to query ingested data in near-real time. Which solution provides near-real-time data querying that is scalable with minimal data loss?

<details><summary>Answer</summary>

**Publish the data to Amazon Kinesis Data Streams, and query the stream in near real time with Amazon Managed Service for Apache Flink (the service previously called Kinesis Data Analytics).**

Kinesis Data Streams accepts the 1 MB/s feed and holds every record durably across three Availability Zones for a retention period you choose, so a reboot of the producing EC2 instance no longer loses in-flight data, and throughput grows by adding shards. Amazon Managed Service for Apache Flink reads directly from the stream and runs continuous queries, which gives the data science team results seconds behind the source; SQL is still available through Flink SQL and Studio notebooks. Writing the feed to Amazon S3 with Firehose and querying it with Athena would work but adds minutes of buffering delay, which is not near real time.

</details>

### 106. dt-321

Can a user get a notification of each instance start / terminate configured with Auto Scaling?

<details><summary>Answer</summary>

**C. Yes, if configured with the Auto Scaling group.**

</details>

### 107. dt-326

In an experiment, if the minimum size for an Auto Scaling group is 1 instance, which of the following statements holds true when you terminate the running instance?

<details><summary>Answer</summary>

**A. Auto Scaling must launch a new instance to replace it.**

</details>

### 108. q-328

A company is hosting a three-tier ecommerce application in the AWS Cloud. The company hosts the website on Amazon S3 and integrates the website with an API that handles sales requests. The company hosts the API on three Amazon EC2 instances behind an Application Load Balancer (ALB). The API consists of static and dynamic front-end content along with backend workers that process sales requests asynchronously. The company is expecting a significant and sudden increase in the number of sales requests during events for the launch of new products. What should a solutions architect recommend to ensure that all the requests are processed successfully?

<details><summary>Answer</summary>

**B. Add an Amazon CloudFront distribution for the static content. Place the EC2 instances in an Auto Scaling group to launch new instances based on network traffic.**

Amazon CloudFront for Static Content: By using CloudFront, you can distribute static content (like images, stylesheets) globally, reducing latency for end-users and offloading some of the traffic from your backend instances.  Auto Scaling Group: An Auto Scaling group allows you to automatically adjust the number of EC2 instances to handle changes in demand. By placing the EC2 instances in an Auto Scaling group, you can dynamically scale the number of instances based on network traffic, ensuring that the application can handle increased load during events.

</details>

### 109. dt-331 `cost`

You have a distributed application that periodically processes large volumes of data across multiple Amazon EC2 Instances. The application is designed to recover gracefully from Amazon EC2 instance failures. You are required to accomplish this task in the most cost-effective way. Which of the following will meet your requirements?

<details><summary>Answer</summary>

**A. Spot Instances.**

</details>

### 110. q-333

A company’s application runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. On the first day of every month at midnight, the application becomes much slower when the month-end financial calculation batch runs. This causes the CPU utilization of the EC2 instances to immediately peak to 100%, which disrupts the application. What should a solutions architect recommend to ensure the application is able to handle the workload and avoid downtime?

<details><summary>Answer</summary>

**C. Configure an EC2 Auto Scaling scheduled scaling policy based on the monthly schedule.**

By configuring a scheduled scaling policy, the EC2 Auto Scaling group can proactively launch additional EC2 instances before the CPU utilization peaks to 100%. This will ensure that the application can handle the workload during the month-end financial calculation batch, and avoid any disruption or downtime.  Configuring a simple scaling policy based on CPU utilization or adding Amazon CloudFront distribution or Amazon ElastiCache will not directly address the issue of handling the monthly peak workload.

</details>

### 111. q-335

A company is experiencing sudden increases in demand. The company needs to provision large Amazon EC2 instances from an Amazon Machine Image (AMI). The instances will run in an Auto Scaling group. The company needs a solution that provides minimum initialization latency to meet the demand. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Enable Amazon Elastic Block Store (Amazon EBS) fast snapshot restore on a snapshot. Provision an AMI by using the snapshot. Replace the AMI in the Auto Scaling group with the new AMI.**

Amazon EBS Fast Snapshot Restore: Enabling fast snapshot restore allows you to provision Amazon EBS volumes based on snapshots with faster performance. This is particularly useful when creating AMIs from snapshots, as it reduces the time it takes to create EBS volumes from those snapshots.  Minimum Initialization Latency: Fast snapshot restore helps in minimizing initialization latency as it provides a way to quickly create EBS volumes from snapshots.  Provisioning AMI from Snapshot: You can create an Amazon Machine Image (AMI) from an Amazon EBS snapshot. This allows you to capture a point-in-time snapshot of the file system, and then use that snapshot to create new instances.

</details>

### 112. q-342 `least-ops`

A transaction processing company has weekly scripted batch jobs that run on Amazon EC2 instances. The EC2 instances are in an Auto Scaling group. The number of transactions can vary, but the baseline CPU utilization that is noted on each run is at least 60%. The company needs to provision the capacity 30 minutes before the jobs run. Currently, engineers complete this task by manually modifying the Auto Scaling group parameters. The company does not have the resources to analyze the required capacity trends for the Auto Scaling group counts. The company needs an automated way to modify the Auto Scaling group’s desired capacity. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create a predictive scaling policy for the Auto Scaling group. Configure the policy to scale based on forecast. Set the scaling metric to CPU utilization. Set the target value for the metric to 60%. In the policy, set the instances to pre-launch 30 minutes before the jobs run.**

In general, if you have regular patterns of traffic increases and applications that take a long time to initialize, you should consider using predictive scaling. Predictive scaling can help you scale faster by launching capacity in advance of forecasted load, compared to using only dynamic scaling, which is reactive in nature.

</details>

### 113. dt-343

In Amazon RDS, security groups are ideally used to:

<details><summary>Answer</summary>

**D. Control what IP addresses or EC2 instances can connect to your databases on a DB instance.**

</details>

### 114. dt-344

How long does an AWS free usage tier EC2 last for?

<details><summary>Answer</summary>

**B. 12 Months upon signup.**

</details>

### 115. dt-346

You can seamlessly join an EC2 instance to your directory domain. What connectivity do you need to be able to connect remotely to this instance?

<details><summary>Answer</summary>

**A. You must have IP connectivity to the instance from the network you are connecting from.**

</details>

### 116. dt-348 `performance`

You have multiple Amazon EC2 instances running in a cluster across multiple Availability Zones within the same region. What combination of the following should be used to ensure the highest network performance (packets per second), lowest latency, and lowest jitter? (Choose 3 answers)

<details><summary>Answer</summary>

**A. Amazon EC2 placement groups.; B. Enhanced networking.; D. Amazon HVM AMI.**

</details>

### 117. q-355 `least-ops`

A company is migrating an old application to AWS. The application runs a batch job every hour and is CPU intensive. The batch job takes 15 minutes on average with an on-premises server. The server has 64 virtual CPU (vCPU) and 512 GiB of memory. Which solution will run the batch job within 15 minutes with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use AWS Batch on Amazon EC2.**

AWS Batch on Amazon EC2: AWS Batch is a fully managed service for batch computing that dynamically provisions the optimal quantity and type of compute resources (Amazon EC2 instances) based on the volume and specific resource requirements of the batch jobs. If the batch job is CPU-intensive and can be parallelized, AWS Batch can efficiently manage the compute resources needed for the job, and it provides a higher level of control over the environment compared to serverless options like AWS Lambda.

</details>

### 118. dt-357

You are configuring your company's application to use Auto Scaling and need to move user state information. Which of the following AWS services provides a shared data store with durability and low latency?

<details><summary>Answer</summary>

**B. Amazon Simple Storage Service.**

</details>

### 119. dt-360

You deployed your company website using Elastic Beanstalk and you enabled log file rotation to S3. An Elastic MapReduce job is periodically analyzing the logs on S3 to build a usage dashboard that you share with your CIO. You recently improved overall performance of the website using CloudFront for dynamic content delivery and your website as the origin. After this architectural change, the usage dashboard shows that the traffic on your website dropped by an order of magnitude. How do you fix your usage dashboard?

<details><summary>Answer</summary>

**A. Enable CloudFront to deliver access logs to S3 and use them as input of the Elastic MapReduce job.**

</details>

### 120. dt-368

An application hosted at the EC2 instance receives an HTTP request from ELB. The same request has an X-Forwarded-For header, which has three IP addresses. Which system's IP will be a part of this header?

<details><summary>Answer</summary>

**C. All of the answers listed here.**

</details>

### 121. q-369 `least-ops`

A company has migrated an application to Amazon EC2 Linux instances. One of these EC2 instances runs several 1-hour tasks on a schedule. These tasks were written by different teams and have no common programming language. The company is concerned about performance and scalability while these tasks run on a single instance. A solutions architect needs to implement a solution to resolve these concerns. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Batch to run the tasks as jobs. Schedule the jobs by using Amazon EventBridge (Amazon CloudWatch Events).**

AWS Batch: AWS Batch is a fully managed service for running batch computing workloads. It dynamically provisions the optimal quantity and type of compute resources based on the volume and specific resource requirements of the batch jobs. It allows you to run tasks written in different programming languages with minimal operational overhead.

</details>

### 122. dt-372

After setting up a Virtual Private Cloud (VPC) network, a more experienced cloud engineer suggests that to achieve low network latency and high network throughput you should look into setting up a placement group. You know nothing about this, but begin to do some research about it and are especially curious about its limitations. Which of the below statements is wrong in describing the limitations of a placement group?

<details><summary>Answer</summary>

**B. A placement group can span multiple Availability Zones.**

</details>

### 123. q-375 `least-ops`

An ecommerce company is building a distributed application that involves several serverless functions and AWS services to complete order- processing tasks. These tasks require manual approvals as part of the workflow. A solutions architect needs to design an architecture for the order-processing application. The solution must be able to combine multiple AWS Lambda functions into responsive serverless applications. The solution also must orchestrate data and services that run on Amazon EC2 instances, containers, or on-premises servers. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Step Functions to build the application.**

Step Functions provide a way to coordinate and orchestrate multiple AWS services, including AWS Lambda functions, in a serverless workflow. They allow you to build applications by connecting various serverless functions and services without managing the underlying infrastructure.

</details>

### 124. dt-376

For which of the following use cases are Simple Workflow Service (SWF) and Amazon EC2 an appropriate solution? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Managing a multi-step and multi-decision checkout process of an e-commerce website.; C. Orchestrating the execution of distributed and auditable business processes.**

</details>

### 125. dt-377

Which of the following instance types are available as Amazon EBS-backed only? (Choose 2 answers)

<details><summary>Answer</summary>

**A. General purpose T2.; D. Compute-optimized C3.**

</details>

### 126. q-377

A company recently deployed a new auditing system to centralize information about operating system versions, patching, and installed software for Amazon EC2 instances. A solutions architect must ensure all instances provisioned through EC2 Auto Scaling groups successfully send reports to the auditing system as soon as they are launched and terminated. Which solution achieves these goals MOST efficiently?

<details><summary>Answer</summary>

**B. Use EC2 Auto Scaling lifecycle hooks to run a custom script to send data to the audit system when instances are launched and terminated.**

</details>

### 127. q-380

A company is migrating its on-premises workload to the AWS Cloud. The company already uses several Amazon EC2 instances and Amazon RDS DB instances. The company wants a solution that automatically starts and stops the EC2 instances and DB instances outside of business hours. The solution must minimize cost and infrastructure maintenance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an AWS Lambda function that will start and stop the EC2 instances and DB instances. Configure Amazon EventBridge to invoke the Lambda function on a schedule.**

AWS Lambda Function: Create a Lambda function that contains the logic to start and stop the EC2 instances and DB instances. Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It is a cost-effective and maintenance-free solution.  Amazon EventBridge: Configure EventBridge (formerly CloudWatch Events) to invoke the Lambda function on a schedule. EventBridge provides a reliable and scalable way to schedule the execution of Lambda functions at specified intervals, such as starting and stopping instances during business hours.

</details>

### 128. dt-381

In Amazon AWS, which of the following statements is true of key pairs?

<details><summary>Answer</summary>

**B. Key pairs are used only for Amazon EC2 and Amazon CloudFront.**

</details>

### 129. q-382

A company has a three-tier application on AWS that ingests sensor data from its users’ devices. The traffic flows through a Network Load Balancer (NLB), then to Amazon EC2 instances for the web tier, and finally to EC2 instances for the application tier. The application tier makes calls to a database. What should a solutions architect do to improve the security of the data in transit?

<details><summary>Answer</summary>

**A. Configure a TLS listener. Deploy the server certificate on the NLB.**

TLS Listener on NLB: By configuring a TLS (Transport Layer Security) listener on the NLB, you can encrypt the traffic between the users' devices and the web tier EC2 instances. This helps protect the data in transit from eavesdropping and other potential security threats.

</details>

### 130. dt-388

You have a video transcoding application running on Amazon EC2. Each instance polls a queue to find out which video should be transcoded, and then runs a transcoding process. If this process is interrupted, the video will be transcoded by another instance based on the queuing system. You have a large backlog of videos which need to be transcoded and would like to reduce this backlog by adding more instances. You will need these instances only until the backlog is reduced. Which type of Amazon EC2 instances should you use to reduce the backlog in the most cost efficient way?

<details><summary>Answer</summary>

**B. Spot instances.**

</details>

### 131. q-388

A company is deploying a two-tier web application in a VPC. The web tier is using an Amazon EC2 Auto Scaling group with public subnets that span multiple Availability Zones. The database tier consists of an Amazon RDS for MySQL DB instance in separate private subnets. The web tier requires access to the database to retrieve product information. The web application is not working as intended. The web application reports that it cannot connect to the database. The database is confirmed to be up and running. All configurations for the network ACLs, security groups, and route tables are still in their default states. What should a solutions architect recommend to fix the application?

<details><summary>Answer</summary>

**D. Add an inbound rule to the security group of the database tier’s RDS instance to allow traffic from the web tiers security group.**

Security Groups: Security groups act as virtual firewalls for your instances to control inbound and outbound traffic. By default, they deny all inbound traffic. In this scenario, the default security group associated with the RDS instance is likely denying incoming traffic from the web tier.  Inbound Rule: To allow traffic from the web tier's EC2 instances to the database tier's RDS instance, you need to add an inbound rule to the security group associated with the RDS instance. This rule should permit traffic from the security group associated with the web tier's EC2 instances.

</details>

### 132. q-391

A company needs a backup strategy for its three-tier stateless web application. The web application runs on Amazon EC2 instances in an Auto Scaling group with a dynamic scaling policy that is configured to respond to scaling events. The database tier runs on Amazon RDS for PostgreSQL. The web application does not require temporary local storage on the EC2 instances. The company’s recovery point objective (RPO) is 2 hours. The backup strategy must maximize scalability and optimize resource utilization for this environment. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Retain the latest Amazon Machine Images (AMIs) of the web and application tiers. Enable automated backups in Amazon RDS and use point-in-time recovery to meet the RPO.**

Snapshots of EBS volumes would be necessary if you want to back up the entire EC2 instance, including any applications and temporary data stored on the EBS volumes attached to the instances. When you take a snapshot of an EBS volume, it backs up the entire contents of that volume. This ensures that you can restore the entire EC2 instance to a specific point in time more quickly. However, if there is no temporary data stored on the EBS volumes, then snapshots of EBS volumes are not necessary.

</details>

### 133. dt-393

Per the AWS Acceptable Use Policy, penetration testing of EC2 instances

<details><summary>Answer</summary>

**B. May be performed by AWS, and is periodically performed by AWS.**

</details>

### 134. dt-396

You decide that you need to create a number of Auto Scaling groups to try and save some money as you have noticed that at certain times most of your EC2 instances are not being used. By default, what is the maximum number of Auto Scaling groups that AWS will allow you to create?

<details><summary>Answer</summary>

**C. 20.**

</details>

### 135. dt-397

After moving an E-Commerce website for a client from a dedicated server to AWS you have also set up auto scaling to perform health checks on the instances in your group and replace instances that fail these checks. Your client has come to you with his own health check system that he wants you to use as it has proved to be very useful prior to his site running on AWS. What do you think would be an appropriate response to this given all that you know about auto scaling?

<details><summary>Answer</summary>

**C. It is possible to implement your own health check system and then send the instance's health information directly from your system to Cloud Watch.**

</details>

### 136. q-397

An ecommerce company needs to run a scheduled daily job to aggregate and filter sales records for analytics. The company stores the sales records in an Amazon S3 bucket. Each object can be up to 10 GB in size. Based on the number of sales events, the job can take up to an hour to complete. The CPU and memory usage of the job are constant and are known in advance. A solutions architect needs to minimize the amount of operational effort that is needed for the job to run. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Elastic Container Service (Amazon ECS) cluster with an AWS Fargate launch type. Create an Amazon EventBridge scheduled event that launches an ECS task on the cluster to run the job.**

C. Amazon ECS with Fargate: Fargate allows you to run containers without managing the underlying infrastructure. You can schedule the ECS task with EventBridge, and since Fargate manages the resources, you don't need to worry about scaling or infrastructure maintenance. This is a good fit for long-running jobs.

</details>

### 137. q-405

A solutions architect is designing the architecture for a software demonstration environment. The environment will run on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer (ALB). The system will experience significant increases in traffic during working hours but is not required to operate on weekends. Which combination of actions should the solutions architect take to ensure that the system can scale to meet demand? (Choose two.)

<details><summary>Answer</summary>

**D. Use a target tracking scaling policy to scale the Auto Scaling group based on instance CPU utilization.**

E. Use scheduled scaling to change the Auto Scaling group minimum, maximum, and desired capacity to zero for weekends. Revert to the default values at the start of the week.  Explanation: An Application Load Balancer scales its own capacity automatically — you don't (and can't) attach an Auto Scaling policy to the ALB itself, so the old option A isn't a real configuration. The EC2 Auto Scaling group behind it is what needs a scaling policy (D), alongside scheduled scaling (E) to scale to zero on weekends.  This allows you to save costs and resources during weekends when the system is not required to operate. Scaling down the Auto Scaling group to zero instances during weekends and reverting to the default values at the start of the week ensures that you only incur costs when the system is actively in use.

</details>

### 138. dt-408

In Amazon EC2, partial instance-hours are billed [...].

<details><summary>Answer</summary>

**D. as full hours.**

</details>

### 139. dt-409

In Amazon EC2, what is the limit of Reserved Instances per Availability Zone each month?

<details><summary>Answer</summary>

**B. 20.**

</details>

### 140. q-409 `availability`

A solutions architect must migrate a Windows Internet Information Services (IIS) web application to AWS. The application currently relies on a file share hosted in the user's on-premises network-attached storage (NAS). The solutions architect has proposed migrating the IIS web servers to Amazon EC2 instances in multiple Availability Zones that are connected to the storage solution, and configuring an Elastic Load Balancer attached to the instances. Which replacement to the on-premises file share is MOST resilient and durable?

<details><summary>Answer</summary>

**C. Migrate the file share to Amazon FSx for Windows File Server.**

Amazon FSx for Windows File Server: Amazon FSx is a fully managed file storage service that is compatible with Windows file systems. Amazon FSx for Windows File Server is specifically designed for Windows workloads, including IIS web applications. It provides a highly available and durable file system that can be accessed by multiple EC2 instances in different Availability Zones.

</details>

### 141. dt-412

A user wants to use an EBS-backed Amazon EC2 instance for a temporary job. Based on the input data, the job is most likely to finish within a week. Which of the following steps should be followed to terminate the instance automatically once the job is finished?

<details><summary>Answer</summary>

**C. Configure the Cloud Watch alarm on the instance that should perform the termination action once the instance is idle.**

</details>

### 142. q-413

An ecommerce company is experiencing an increase in user traffic. The company’s store is deployed on Amazon EC2 instances as a two-tier web application consisting of a web tier and a separate database tier. As traffic increases, the company notices that the architecture is causing significant delays in sending timely marketing and order confirmation email to users. The company wants to reduce the time it spends resolving complex email delivery issues and minimize operational overhead. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Configure the web instance to send email through Amazon Simple Email Service (Amazon SES).**

Amazon Simple Email Service (Amazon SES) is a fully managed email sending service. By configuring the web instances to send emails through Amazon SES, the ecommerce company can offload the complexity of email delivery to a reliable and scalable service.

</details>

### 143. dt-416

A t2.medium EC2 instance type must be launched with what type of Amazon Machine Image (AMI)?

<details><summary>Answer</summary>

**C. An Amazon EBS-backed Hardware Virtual Machine AMI.**

</details>

### 144. dt-419

Amazon EC2 provides a [...]. It is an HTTP or HTTPS request that uses the HTTP verbs GET or POST.

<details><summary>Answer</summary>

**C. Query API.**

</details>

### 145. dt-420

Which of the following requires a custom Cloud Watch metric to monitor?

<details><summary>Answer</summary>

**C. Disk usage activity of an EC2 instance.**

</details>

### 146. dt-422

An Elastic IP address (EIP) is a static IP address designed for dynamic cloud computing. With an EIP, you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account. Your EIP is associated with your AWS account, not a particular EC2 instance, and it remains associated with your account until you choose to explicitly release it. By default how many EIPs is each AWS account limited to on a per region basis?

<details><summary>Answer</summary>

**B. 5.**

</details>

### 147. q-422

A company is developing a new machine learning (ML) model solution on AWS. The models are developed as independent microservices that fetch approximately 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular. Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which design should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**Direct the requests from the API into an Amazon Simple Queue Service (Amazon SQS) queue. Deploy the models as Amazon Elastic Container Service (Amazon ECS) services that read from the queue. Enable AWS Auto Scaling on Amazon ECS for both the cluster and copies of the service based on the queue size.**

The API is asynchronous, so requests can sit in an SQS queue and be picked up when capacity exists; the queue absorbs a sudden batch of thousands of requests without dropping any and without the caller waiting. Scaling the ECS service on the number of messages waiting in the queue adds containers only when work arrives and scales back down through the days or weeks a model is unused, and scaling the cluster capacity alongside it means you are not paying for idle hosts. Long-running containers also keep the 1 GB of model data in memory between requests, whereas a design that fronts short-lived functions with a load balancer would re-download that 1 GB on every cold start and would make an asynchronous API behave synchronously.

</details>

### 148. q-424 `cost`

A company is running a custom application on Amazon EC2 On-Demand Instances. The application has frontend nodes that need to run 24 hours a day, 7 days a week and backend nodes that need to run only for a short time based on workload. The number of backend nodes varies during the day. The company needs to scale out and scale in more instances based on workload. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use Reserved Instances for the frontend nodes. Use Spot Instances for the backend nodes.**

Reserved Instances (RIs) for Frontend Nodes: Since the frontend nodes need to run 24/7, Reserved Instances provide a significant cost savings compared to On-Demand pricing. RIs are a commitment to a consistent usage pattern, making them suitable for instances that need to run continuously.  Spot Instances for Backend Nodes: Spot Instances are a cost-effective option for workloads that can be interrupted or are flexible regarding availability. As the number of backend nodes varies during the day, using Spot Instances allows you to take advantage of spare capacity at a lower cost. Spot Instances are suitable for short-lived, scalable, and flexible workloads.

</details>

### 149. dt-426

Which of the following is true of Amazon EC2 security group?

<details><summary>Answer</summary>

**D. You can modify the rules for a security group at any time.**

</details>

### 150. q-427 `availability`

A solutions architect is implementing a complex Java application with a MySQL database. The Java application must be deployed on Apache Tomcat and must be highly available. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the application by using AWS Elastic Beanstalk. Configure a load-balanced environment and a rolling deployment policy.**

AWS Elastic Beanstalk: It is a fully managed service that simplifies the deployment and operation of applications, including web applications running Apache Tomcat. Elastic Beanstalk handles the deployment details, capacity provisioning, load balancing, auto-scaling, and application health monitoring, making it easier to deploy and manage your applications.

</details>

### 151. dt-428

A user is trying to launch a similar EC2 instance from an existing instance with the option 'Launch More like this'. The AMI of the selected instance is deleted. What will happen in this case?

<details><summary>Answer</summary>

**D. AWS will throw an error saying that the AMI is deregistered.**

</details>

### 152. dt-434 `availability`

A client application requires operating system privileges on a relational database server. What is an appropriate configuration for a highly available database architecture?

<details><summary>Answer</summary>

**D. Amazon EC2 instances in a replication configuration utilizing two different Availability Zones.**

</details>

### 153. q-437

A company operates an ecommerce website on Amazon EC2 instances behind an Application Load Balancer (ALB) in an Auto Scaling group. The site is experiencing performance issues related to a high request rate from illegitimate external systems with changing IP addresses. The security team is worried about potential DDoS attacks against the website. The company must block the illegitimate incoming requests in a way that has a minimal impact on legitimate users. What should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Deploy AWS WAF, associate it with the ALB, and configure a rate-limiting rule.**

AWS WAF is a web application firewall service that helps protect your web applications from common web exploits. It allows you to create rules to filter and monitor HTTP and HTTPS traffic based on conditions that you define. By associating AWS WAF with the ALB, you can inspect and filter incoming traffic before it reaches your instances, providing a layer of protection against DDoS attacks and other malicious activities.

</details>

### 154. dt-440

Regarding Amazon Route 53, if your application is running on Amazon EC2 instances in two or more Amazon EC2 regions and if you have more than one Amazon EC2 instance in one or more regions, you can use [...] to route traffic to the correct region and then use [...] route traffic to instances within the region, based on probabilities that you specify.

<details><summary>Answer</summary>

**B. latency-based routing; weighted resource record sets.**

</details>

### 155. q-441 `cost`

A company hosts a multi-tier web application on Amazon Linux Amazon EC2 instances behind an Application Load Balancer. The instances run in an Auto Scaling group across multiple Availability Zones. The company observes that the Auto Scaling group launches more On-Demand Instances when the application's end users access high volumes of static web content. The company wants to optimize cost. What should a solutions architect do to redesign the application MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon CloudFront distribution to host the static web contents from an Amazon S3 bucket.**

Amazon CloudFront is a content delivery network (CDN) service that delivers static and dynamic web content, including images, videos, CSS, and JavaScript, with low latency and high transfer speeds. It can be used to cache and distribute static content globally, reducing the load on your web servers.  By creating a CloudFront distribution and hosting static web content in an Amazon S3 bucket, you offload the serving of static content to the CDN, which can significantly reduce the load on your EC2 instances.

</details>

### 156. dt-442 `availability`

When using the following AWS services, which should be implemented in multiple Availability Zones for high availability solutions? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Amazon Elastic Compute Cloud (EC2).; C. Amazon Elastic Load Balancing.**

</details>

### 157. q-444

A company has hired a solutions architect to design a reliable architecture for its application. The application consists of one Amazon RDS DB instance and two manually provisioned Amazon EC2 instances that run web servers. The EC2 instances are located in a single Availability Zone. An employee recently deleted the DB instance, and the application was unavailable for 24 hours as a result. The company is concerned with the overall reliability of its environment. What should the solutions architect do to maximize reliability of the application's infrastructure?

<details><summary>Answer</summary>

**B. Update the DB instance to be Multi-AZ, and enable deletion protection. Place the EC2 instances behind an Application Load Balancer, and run them in an EC2 Auto Scaling group across multiple Availability Zones.**

Multi-AZ RDS Instance: By updating the DB instance to be Multi-AZ, you ensure that there is a standby replica in a different Availability Zone, providing high availability and automatic failover in case of a failure in the primary zone.  Deletion Protection: Enabling deletion protection for the DB instance helps prevent accidental deletion, reducing the risk of downtime caused by human error.

</details>

### 158. dt-445

Which of the following features ensures even distribution of traffic to Amazon EC2 instances in multiple Availability Zones registered with a load balancer?

<details><summary>Answer</summary>

**A. Elastic Load Balancing request routing.**

</details>

### 159. dt-447

You have been using T2 instances as your CPU requirements have not been that intensive. However you now start to think about larger instance types and start looking at M1 and M3 instances. You are a little confused as to the differences between them as they both seem to have the same ratio of CPU and memory. Which statement below is incorrect as to why you would use one over the other?

<details><summary>Answer</summary>

**B. M3 instances are configured with more swap memory than M1 instances.**

</details>

### 160. dt-450

If you're unable to connect via SSH to your EC2 instance, which of the following should you check and possibly correct to restore connectivity?

<details><summary>Answer</summary>

**D. Adjust the instance's Security Group to permit ingress traffic over port 22 from your IP.**

</details>

### 161. q-451

A company is migrating its applications and databases to the AWS Cloud. The company will use Amazon Elastic Container Service (Amazon ECS), AWS Direct Connect, and Amazon RDS. Which activities will be managed by the company's operational team? (Choose three.)

<details><summary>Answer</summary>

**C. Configuration of additional software components on Amazon ECS for monitoring, patch management, log management, and host intrusion detection**

The company's operational team is responsible for configuring additional software components on Amazon ECS, such as monitoring tools, patch management tools, log management systems, and host intrusion detection systems. These components are often specific to the company's requirements and policies.  B. Creation of an Amazon RDS DB instance and configuring the scheduled maintenance window:  The operational team is responsible for creating Amazon RDS DB instances, configuring parameters, and setting up maintenance windows based on the company's operational needs. This includes decisions about the size and type of the RDS instance, storage configuration, and other relevant settings.  F. Encryption of the data that moves in transit through Direct Connect:  While AWS manages the physical infrastructure of Direct Connect, the company's operational team is responsible for configuring encryption for the data in transit over Direct Connect. This includes implementing encryption protocols and ensuring the security of data while it travels between the on-premises data center and AWS.

</details>

### 162. q-452

A company runs a Java-based job on an Amazon EC2 instance. The job runs every hour and takes 10 seconds to run. The job runs on a scheduled interval and consumes 1 GB of memory. The CPU utilization of the instance is low except for short surges during which the job uses the maximum CPU available. The company wants to optimize the costs to run the job. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Copy the code into an AWS Lambda function that has 1 GB of memory. Create an Amazon EventBridge scheduled rule to run the code each hour.**

AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It automatically scales based on the number of requests, making it cost-effective for sporadic workloads. Scheduled Rule with Amazon EventBridge:  Amazon EventBridge allows you to schedule events at specified intervals. By creating a scheduled rule, you can trigger the Lambda function to run the Java-based job every hour.

</details>

### 163. dt-455

A user has hosted an application on EC2 instances. The EC2 instances are configured with ELB and Auto Scaling. The application server session time out is 2 hours. The user wants to configure connection draining to ensure that all in-flight requests are supported by ELB even though the instance is being deregistered. What time out period should the user specify for connection draining?

<details><summary>Answer</summary>

**A. 1 hour.**

</details>

### 164. dt-456

What does the following command do with respect to the Amazon EC2 security groups? ec2-create-group CreateSecurityGroup

<details><summary>Answer</summary>

**B. Creates a new security group for use with your account.**

</details>

### 165. q-457

A company that uses AWS is building an application to transfer data to a product manufacturer. The company has its own identity provider (IdP). The company wants the IdP to authenticate application users while the users use the application to transfer data. The company must use Applicability Statement 2 (AS2) protocol. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Transfer Family to transfer the data. Create an AWS Lambda function for IdP authentication.**

AWS Transfer Family (Option C): AWS Transfer Family is a fully managed service that allows you to transfer files over the internet using a range of protocols, including AS2. You can integrate AWS Transfer Family with your IdP for user authentication. By using a Lambda function, you can customize the authentication process and integrate it with your own IdP.

</details>

### 166. dt-458

Which of the following are characteristics of a reserved instance? (Choose 3 answers)

<details><summary>Answer</summary>

**A. It can be migrated across Availability Zones.; D. It is specific to an instance Type.; E. It can be used to lower Total Cost of Ownership (TCO) of a system.**

</details>

### 167. q-461

A company is developing a mobile gaming app in a single AWS Region. The app runs on multiple Amazon EC2 instances in an Auto Scaling group. The company stores the app data in Amazon DynamoDB. The app communicates by using TCP traffic and UDP traffic between the users and the servers. The application will be used globally. The company wants to ensure the lowest possible latency for all users. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Global Accelerator to create an accelerator. Create a Network Load Balancer (NLB) behind an accelerator endpoint that uses Global Accelerator integration and listening on the TCP and UDP ports. Update the Auto Scaling group to register instances on the NLB.**

</details>

### 168. dt-462

What is a placement group?

<details><summary>Answer</summary>

**B. A feature that enables EC2 instances to interact with each other via high bandwidth, low latency connections.**

</details>

### 169. q-462

A company has an application that processes customer orders. The company hosts the application on an Amazon EC2 instance that saves the orders to an Amazon Aurora database. Occasionally when traffic is high the workload does not process orders fast enough. What should a solutions architect do to write the orders reliably to the database as quickly as possible?

<details><summary>Answer</summary>

**B. Write orders to an Amazon Simple Queue Service (Amazon SQS) queue. Use EC2 instances in an Auto Scaling group behind an Application Load Balancer to read from the SQS queue and process orders into the database.**

Amazon SQS, which is a fully managed message queuing service. Writing orders to an SQS queue allows for decoupling the EC2 instances processing the orders from the application writing the orders. EC2 instances in an Auto Scaling group can then read from the SQS queue, ensuring that the processing scales with demand.  Using an Auto Scaling group ensures that you can dynamically adjust the number of EC2 instances based on the workload. This can help handle high traffic efficiently.

</details>

### 170. dt-466

A user is planning to make a mobile game which can be played online or offline and will be hosted on EC2. The user wants to ensure that if someone breaks the highest score or they achieve some milestone they can inform all their colleagues through email. Which of the below mentioned AWS services helps achieve this goal?

<details><summary>Answer</summary>

**B. AWS Simple Email Service.**

</details>

### 171. q-466 `availability`

A company designed a stateless two-tier application that uses Amazon EC2 in a single Availability Zone and an Amazon RDS Multi-AZ DB instance. New company management wants to ensure the application is highly available. What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Configure the application to use Multi-AZ EC2 Auto Scaling and create an Application Load Balancer**

</details>

### 172. dt-468

Which of the following is NOT a characteristic of Amazon Elastic Compute Cloud (Amazon EC2)?

<details><summary>Answer</summary>

**B. It increases the need to forecast traffic by providing dynamic IP addresses for static cloud computing.**

</details>

### 173. q-468

A company is developing a microservices application that will provide a search catalog for customers. The company must use REST APIs to present the frontend of the application to users. The REST APIs must access the backend services that the company hosts in containers in private VPC subnets. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Design a REST API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a private VPC link for API Gateway to access Amazon ECS.**

</details>

### 174. dt-469

A user has launched one EC2 instance in the US East region and one in the US West region. The user has launched an RDS instance in the US East region. How can the user configure access from both the EC2 instances to RDS?

<details><summary>Answer</summary>

**C. Configure the security group of the US East region to allow traffic from the US West region's instance and configure the RDS security group's ingress rule for the US East EC2 group.**

</details>

### 175. dt-475

While creating an Amazon RDS DB, your first task is to set up a DB [...] that controls what IP addresses or EC2 instances have access to your DB Instance.

<details><summary>Answer</summary>

**D. Security Group.**

</details>

### 176. dt-482

What would be the best way to retrieve the public IP address of your EC2 instance using the CLI?

<details><summary>Answer</summary>

**D. Using instance metadata.**

</details>

### 177. dt-483

A company is building a two-tier web application to serve dynamic transaction-based content. The data tier is leveraging an Online Transactional Processing (OLTP) database. What services should you leverage to enable an elastic and scalable web tier?

<details><summary>Answer</summary>

**A. Elastic Load Balancing, Amazon EC2, and Auto Scaling.**

</details>

### 178. q-483 `cost`

A company containerized a Windows job that runs on .NET 6 Framework under a Windows container. The company wants to run this job in the AWS Cloud. The job runs every 10 minutes. The job’s runtime varies between 1 minute and 3 minutes. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use Amazon Elastic Container Service (Amazon ECS) on AWS Fargate to run the job. Create a scheduled task based on the container image of the job to run every 10 minutes.**

Amazon ECS is a fully managed container orchestration service, and AWS Fargate allows you to run containers without managing the underlying infrastructure. ECS on Fargate is a serverless option, which means you only pay for the vCPU and memory that you use, and it scales automatically to meet the needs of the job.

</details>

### 179. q-486

A company is building a three-tier application on AWS. The presentation tier will serve a static website The logic tier is a containerized application. This application will store data in a relational database. The company wants to simplify deployment and to reduce operational costs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon S3 to host static content. Use Amazon Elastic Container Service (Amazon ECS) with AWS Fargate for compute power. Use a managed Amazon RDS cluster for the database.**

Amazon S3 is a highly scalable and cost-effective storage service that can be used to host static content like a static website. It simplifies the storage and delivery of static assets. AWS Fargate is a serverless compute engine for containers. It allows you to run containers without managing the underlying infrastructure. This simplifies deployment and reduces operational overhead.

</details>

### 180. dt-488

You have three Amazon EC2 instances with Elastic IP addresses in the US East (Virginia) region, and you want to distribute requests across all three IPs evenly for users for whom US East (Virginia) is the appropriate region. How many EC2 instances would be sufficient to distribute requests in other regions?

<details><summary>Answer</summary>

**D. 1.**

</details>

### 181. dt-490

You are implementing a URL whitelisting system for a company that wants to restrict outbound HTTPS connections to specific domains from their EC2-hosted applications. You deploy a single EC2 instance running proxy software and configure it to accept traffic from all subnets and EC2 instances in the VPC. You configure the proxy to only pass through traffic to domains that you define in its whitelist configuration. You have a nightly maintenance window of 10 minutes where all instances fetch new software updates. Each update is about 200MB in size and there are 500 instances in the VPC that routinely fetch updates. After a few days you notice that some machines are failing to successfully download some, but not all of their updates within the maintenance window. The download URLs used for these updates are correctly listed in the proxy's whitelist configuration and you are able to access them manually using a web browser on the instances. What might be happening? (Choose 2 answers)

<details><summary>Answer</summary>

**A. You are running the proxy on an undersized EC2 instance type so network throughput is not sufficient for all instances to download their updates in time.; B. You are running the proxy on a sufficiently-sized EC2 instance in a private subnet and its network throughput is being throttled by a NAT running on an undersized EC2 instance.**

</details>

### 182. dt-498

A user has launched a large EBS backed EC2 instance in the US-East-1a region. The user wants to achieve Disaster Recovery (DR) for that instance by creating another small instance in Europe. How can the user achieve DR?

<details><summary>Answer</summary>

**D. Create an AMI of the instance and copy the AMI to the EU region. Then launch the instance from the EU AMI.**

</details>

### 183. dt-502

Select the correct statement: Within Amazon EC2, when using Linux instances, the device name /dev/sda1 is [...].

<details><summary>Answer</summary>

**D. reserved for the root device.**

</details>

### 184. dt-504

Your web application front end consists of multiple EC2 instances behind an Elastic Load Balancer. You configured ELB to perform health checks on these EC2 instances, if an instance fails to pass health checks, which statement will be true?

<details><summary>Answer</summary>

**D. The ELB stops sending traffic to the instance that failed its health check.**

</details>

### 185. dt-505

George has launched three EC2 instances inside the US-East-1a zone with his AWS account. Ray has launched two EC2 instances in the US-East-1a zone with his AWS account. Which of the below mentioned statements will help George and Ray understand the Availability Zone (AZ) concept better?

<details><summary>Answer</summary>

**B. The US-East-1a region of George and Ray can be different Availability Zones.**

</details>

### 186. q-505 `cost`

A company has Amazon EC2 instances that run nightly batch jobs to process data. The EC2 instances run in an Auto Scaling group that uses On- Demand billing. If a job fails on one instance, another instance will reprocess the job. The batch jobs run between 12:00 AM and 06:00 AM local time every day. Which solution will provide EC2 instances to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a new launch template for the Auto Scaling group. Set the instances to Spot Instances. Set a policy to scale out based on CPU usage.**

Spot Instances: Spot Instances allow you to bid for unused EC2 capacity at a potentially lower cost than On-Demand pricing. This can result in significant cost savings for batch jobs that are fault-tolerant and can be interrupted or retried.  Scaling Policy: Setting a policy to scale out based on CPU usage ensures that additional Spot Instances are launched when the demand for processing power increases during batch job execution. This helps in handling varying workloads efficiently.

</details>

### 187. dt-508

Which AWS instance address has the following characteristics? 'If you stop an instance, its Elastic IP address is unmapped, and you must remap it when you restart the instance.'

<details><summary>Answer</summary>

**D. EC2 Addresses.**

</details>

### 188. q-508

A company has migrated multiple Microsoft Windows Server workloads to Amazon EC2 instances that run in the us-west-1 Region. The company manually backs up the workloads to create an image as needed. In the event of a natural disaster in the us-west-1 Region, the company wants to recover workloads quickly in the us-west-2 Region. The company wants no more than 24 hours of data loss on the EC2 instances. The company also wants to automate any backups of the EC2 instances. Which solutions will meet these requirements with the LEAST administrative effort? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon EC2-backed Amazon Machine Image (AMI) lifecycle policy to create a backup based on tags. Schedule the backup to run twice daily. Configure the copy to the us-west-2 Region.**

D. Create a backup vault by using AWS Backup. Use AWS Backup to create a backup plan for the EC2 instances based on tag values. Define the destination for the copy as us-west-2. Specify the backup schedule to run twice daily.

</details>

### 189. gh-508

Topic 1
A company has migrated multiple Microsoft Windows Server workloads to Amazon EC2 instances that run in the us-west-1 Region. The company manually backs up the workloads to create an image as needed.
In the event of a natural disaster in the us-west-1 Region, the company wants to recover workloads quickly in the us-west-2 Region. The company wants no more than 24 hours of data loss on the EC2 instances. The company also wants to automate any backups of the EC2 instances.
Which solutions will meet these requirements with the LEAST administrative effort? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon EC2-backed Amazon Machine Image (AMI) lifecycle policy to create a backup based on tags. Schedule the backup to run twice daily. Configure the copy to the us-west-2 Region.**

D. Create a backup vault by using AWS Backup. Use AWS Backup to create a backup plan for the EC2 instances based on tag values. Define the destination for the copy as us-west-2. Specify the backup schedule to run twice daily.

</details>

### 190. q-516 `least-ops`

A company provides an API interface to customers so the customers can retrieve their financial information. Еhe company expects a larger number of requests during peak usage times of the year. The company requires the API to respond consistently with low latency to ensure customer satisfaction. The company needs to provide a compute host for the API. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon API Gateway and AWS Lambda functions with provisioned concurrency.**

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. AWS Lambda is a serverless computing service that automatically scales based on demand. Provisioned concurrency in AWS Lambda allows you to set a specific number of concurrent executions to ensure that the function is ready to respond quickly to incoming requests.

</details>

### 191. q-522 `least-ops`

A company runs container applications by using Amazon Elastic Kubernetes Service (Amazon EKS). The company's workload is not consistent throughout the day. The company wants Amazon EKS to scale in and out according to the workload. Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**B. Use the Kubernetes Metrics Server to activate horizontal pod autoscaling.**

Kubernetes supports Horizontal Pod Autoscaling (HPA) based on custom metrics or resource metrics. By using the Kubernetes Metrics Server, you can enable HPA to automatically adjust the number of pods in a deployment based on observed custom metrics (such as application-specific metrics) or resource metrics (such as CPU or memory usage).  C. Use the Kubernetes Cluster Autoscaler:  The Kubernetes Cluster Autoscaler automatically adjusts the size of the cluster by adding or removing nodes based on the resource utilization and pod scheduling requirements. This helps in scaling the cluster itself based on the overall demand.

</details>

### 192. q-523

A company runs a microservice-based serverless web application. The application must be able to retrieve data from multiple Amazon DynamoDB tables A solutions architect needs to give the application the ability to retrieve the data with no impact on the baseline performance of the application. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**Use AWS AppSync pipeline resolvers.**

AppSync is a managed GraphQL front end for serverless applications, and a pipeline resolver runs an ordered series of functions inside one request, each attached to its own data source. That lets a single request gather data from several DynamoDB tables in the managed service layer, so the application's existing code path is untouched and its baseline performance is unaffected, and there is no new infrastructure to run. Lambda@Edge would mean writing and deploying edge functions that still have to call DynamoDB back in the table's region, which is more work and slower, and an edge-optimized API Gateway endpoint only changes where the connection is terminated.

</details>

### 193. dt-525

Which of the following items are required to allow an application deployed on an EC2 instance to write data to a DynamoDB table? Assume that no security keys are allowed to be stored on the EC2 instance. (Choose 3 answers)

<details><summary>Answer</summary>

**A. Create an IAM Role that allows write access to the DynamoDB table.; B. Add an IAM Role to a running EC2 instance.; E. Launch an EC2 Instance with the IAM Role included in the launch configuration.**

</details>

### 194. dt-526

Identify a true statement about the On-Demand instances purchasing option provided by Amazon EC2.

<details><summary>Answer</summary>

**A. Pay for the instances that you use by the hour, with no long-term commitments or up-front payments.**

</details>

### 195. q-527

A company has a regional subscription-based streaming service that runs in a single AWS Region. The architecture consists of web servers and application servers on Amazon EC2 instances. The EC2 instances are in Auto Scaling groups behind Elastic Load Balancers. The architecture includes an Amazon Aurora global database cluster that extends across multiple Availability Zones. The company wants to expand globally and to ensure that its application has minimal downtime. Which solution will provide the MOST fault tolerance?

<details><summary>Answer</summary>

**D. Deploy the web tier and the application tier to a second Region. Use an Amazon Aurora global database to deploy the database in the primary Region and the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. Promote the secondary to primary as needed.**

An Aurora global database allows you to replicate your database across multiple AWS Regions. This ensures that you have a read-capable secondary database in the second Region, providing low-latency access to the database. Amazon Route 53 can be configured with health checks to monitor the health of the web and application tiers in both Regions. In the event of a failure in the primary Region, Route 53 can automatically route traffic to the healthy resources in the second Region.

</details>

### 196. dt-530

Can I change the EC2 security groups after an instance is launched in EC2-Classic?

<details><summary>Answer</summary>

**B. No, you cannot change security groups after you launch an instance in EC2-Classic.**

</details>

### 197. dt-531

Please select the Amazon EC2 resource which cannot be tagged.

<details><summary>Answer</summary>

**C. Elastic IP addresses.**

</details>

### 198. q-531

A company needs to integrate with a third-party data feed. The data feed sends a webhook to notify an external service when new data is ready for consumption. A developer wrote an AWS Lambda function to retrieve data when the company receives a webhook callback. The developer must make the Lambda function available for the third party to call. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**Create a function URL for the Lambda function, and give that URL to the third party as the webhook target.**

A Lambda function URL is a built-in feature of the function: turning it on produces a permanent HTTPS address of the form https://<id>.lambda-url.<region>.on.aws that invokes the function directly, with no other service to create, configure or pay for. Access can be left open for a public webhook or restricted to signed IAM callers, which covers what a third-party feed needs. API Gateway in front of the function would also work and is the right choice when you need request throttling, API keys, custom authorizers, a custom domain or AWS WAF, but for simply handing a callback address to one partner it is extra setup for no benefit.

</details>

### 199. dt-535

What does the following policy for Amazon EC2 do? { 'Statement':[{ 'Effect': 'Allow', 'Action':'ec2: Describe*', 'Resource':'*' }] }

<details><summary>Answer</summary>

**A. Allow users to use actions that start with 'Describe' over all the EC2 resources.**

</details>

### 200. dt-538

In Amazon Elastic Compute Cloud, which of the following is used for communication between instances in the same network (EC2-Classic or a VPC)?

<details><summary>Answer</summary>

**A. Private IP addresses.**

</details>

### 201. dt-539

A user is planning to host a mobile game on EC2 which sends notifications to active users on either high score or the addition of new features. The user should get this notification when he is online on his mobile device. Which of the below mentioned AWS services can help achieve this functionality?

<details><summary>Answer</summary>

**A. AWS Simple Notification Service.**

</details>

### 202. dt-540

You need to create an Amazon Machine Image (AMI) for a customer for an application which does not appear to be part of the standard AWS AMI template that you can see in the AWS console. What are the alternative possibilities for creating an AMI on AWS?

<details><summary>Answer</summary>

**B. You can purchase an AMIs from a third party or can create your own AMI.**

</details>

### 203. dt-551

Can I move a Reserved Instance from one Region to another?

<details><summary>Answer</summary>

**A. No.**

</details>

### 204. q-552

A company needs to optimize the cost of its Amazon EC2 instances. The company also needs to change the type and family of its EC2 instances every 2-3 months. What should the company do to meet these requirements?

<details><summary>Answer</summary>

**B. Purchase a No Upfront Compute Savings Plan for a 1-year term.**

WHat is Upfront --- You don't pay anything upfront. You receive a smaller discount, but you free up capital for other projects.  A No Upfront option means no upfront payment is required, which provides flexibility.  1-year Term: A 1-year term aligns with the company's need to change the type and family of its EC2 instances every 2-3 months. While Compute Savings Plans have a commitment term, choosing a 1-year term allows for more frequent adjustments compared to a 3-year term.

</details>

### 205. dt-558

You have been doing a lot of testing of your VPC Network by deliberately failing EC2 instances to test whether instances are failing over properly. Your customer who will be paying the AWS bill for all this asks you if he being charged for all these instances. You try to explain to him how the billing works on EC2 instances to the best of your knowledge. What would be an appropriate response to give to the customer in regards to this?

<details><summary>Answer</summary>

**C. Billing commences when Amazon EC2 initiates the boot sequence of an AMI instance and billing ends when the instance shuts down.**

</details>

### 206. dt-559

Refer to the architecture diagram above of a batch processing solution using Simple Queue Service (SQS) to set up a message queue between EC2 instances which are used as batch processors Cloud Watch monitors the number of Job requests (queued messages) and an Auto Scaling group adds or deletes batch servers automatically based on parameters set in Cloud Watch alarms. You can use this architecture to implement which of the following features in a cost effective and efficient manner?

<details><summary>Answer</summary>

**C. Implement message passing between EC2 instances within a batch by exchanging messages through SQS.**

</details>

### 207. q-559

A company hosts multiple applications on AWS for different product lines. The applications use different compute resources, including Amazon EC2 instances and Application Load Balancers. The applications run in different AWS accounts under the same organization in AWS Organizations across multiple AWS Regions. Teams for each product line have tagged each compute resource in the individual accounts. The company wants more details about the cost for each product line from the consolidated billing feature in Organizations. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Select a specific user-defined tag in the AWS Billing console.**

E. Activate the selected tag from the Organizations management account.  User-defined tags are tags that you create and attach to your AWS resources. In this case, since teams for each product line have tagged each compute resource with user-defined tags, selecting a specific user-defined tag in the AWS Billing console allows you to filter costs based on those tags.  The consolidated billing feature in AWS Organizations allows you to view and manage costs across multiple AWS accounts. By activating the selected tag from the Organizations management account, you ensure that the tagged resources from all linked accounts are included in the consolidated billing report. This enables you to get detailed cost information for each product line.

</details>

### 208. gh-559

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

### 209. dt-562

Which of the following strategies can be used to control access to your Amazon EC2 instances?

<details><summary>Answer</summary>

**D. EC2 security groups.**

</details>

### 210. q-562

A solutions architect needs to ensure that API calls to Amazon DynamoDB from Amazon EC2 instances in a VPC do not travel across the internet. Which combination of steps should the solutions architect take to meet this requirement? (Choose two.)

<details><summary>Answer</summary>

**A. Create a route table entry for the endpoint.**

B. Create a gateway endpoint for DynamoDB.

</details>

### 211. gh-563 `least-ops`

clusters and workloads from a central location.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Use Amazon EKS Connector to register and connect the Kubernetes clusters that run outside Amazon EKS, so every cluster can be seen and managed from the EKS console.**

EKS Connector installs a small agent into a Kubernetes cluster that AWS does not run - on premises, self-managed on EC2, or on another cloud provider - and registers that cluster with Amazon EKS, so it appears in the EKS console alongside the native EKS clusters with its nodes and workloads visible. That gives one place to see every cluster without standing up and maintaining a separate management tool, which is the least operational overhead of the options. EKS Anywhere is for running an AWS-supported Kubernetes distribution in your own data centre, and EKS Distro is only the open-source build of Kubernetes that EKS is based on; neither gives a single central view of clusters you already have.

</details>

### 212. dt-565

In Amazon EC2, how many Elastic IP addresses can you have by default?

<details><summary>Answer</summary>

**C. 5.**

</details>

### 213. dt-566

A user has created photo editing software and hosted it on EC2. The software accepts requests from the user about the photo format and resolution and sends a message to S3 to enhance the picture accordingly. Which of the below mentioned AWS services will help make a scalable software with the AWS infrastructure in this scenario?

<details><summary>Answer</summary>

**B. AWS Simple Queue Service.**

</details>

### 214. dt-569

A user is running a webserver on EC2. The user wants to receive the SMS when the EC2 instance utilization is above the threshold limit. Which AWS services should the user configure in this case?

<details><summary>Answer</summary>

**B. AWS CloudWatch + AWS SNS.**

</details>

### 215. q-570 `least-ops`

A company has a large workload that runs every Friday evening. The workload runs on Amazon EC2 instances that are in two Availability Zones in the us-east-1 Region. Normally, the company must run no more than two instances at all times. However, the company wants to scale up to six instances each Friday to handle a regularly repeating increased workload. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Auto Scaling group that has a scheduled action.**

By creating an Auto Scaling group with a scheduled action, you can configure the group to automatically adjust the desired capacity based on a specified schedule. In this case, you can set up a scheduled action to increase the desired capacity to six instances every Friday evening.

</details>

### 216. dt-575 `cost`

You are designing a multi-platform web application for AWS. The application will run on EC2 instances and will be accessed from PCs, tablets and smart phones. Supported accessing platforms are Windows, macOS, iOS and Android. Separate sticky session and SSL certificate setups are required for different platform types. Which of the following describes the most cost effective and performance efficient architecture setup?

<details><summary>Answer</summary>

**D. Assign multiple ELBs to an EC2 instance or group of EC2 instances running the common components of the web application, one ELB for each platform type. Session stickiness and SSL termination are done at the ELBs.**

</details>

### 217. q-576

A company is building a RESTful serverless web application on AWS by using Amazon API Gateway and AWS Lambda. The users of this web application will be geographically distributed, and the company wants to reduce the latency of API requests to these users. Which type of endpoint should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**An edge-optimized API endpoint.**

With an edge-optimized endpoint, API Gateway puts a CloudFront distribution that it manages in front of your API, so a request from a geographically distant user enters the AWS network at the nearest edge location and travels the rest of the way over the AWS backbone instead of the public internet. That cuts the latency of connection setup and transit for scattered users, which is what the requirement asks for. A regional endpoint sends clients straight to the API in its own region and is the better choice when callers are in that same region or when you want to run your own CloudFront distribution; a private endpoint is reachable only from inside a VPC.

</details>

### 218. dt-583

A company has a workflow that sends video files from their on-premise system to AWS for transcoding. They use EC2 worker instances that pull transcoding jobs from SQS. Why is SQS an appropriate service for this scenario?

<details><summary>Answer</summary>

**D. SQS helps to facilitate horizontal scaling of encoding tasks.**

</details>

### 219. q-584

A company is deploying an application that processes large quantities of data in parallel. The company plans to use Amazon EC2 instances for the workload. The network architecture must be configurable to prevent groups of nodes from sharing the same underlying hardware. Which networking solution meets these requirements?

<details><summary>Answer</summary>

**A. Run the EC2 instances in a spread placement group.**

A spread placement group is a logical grouping of instances that are placed on distinct underlying hardware. This ensures that instances within the group are physically separated, reducing the risk of correlated failures. This option is suitable for applications that need to maximize the level of isolation.

</details>

### 220. dt-586

What does Amazon EC2 provide?

<details><summary>Answer</summary>

**A. Virtual servers in the Cloud.**

</details>

### 221. q-594

A company plans to migrate to AWS and use Amazon EC2 On-Demand Instances for its application. During the migration testing phase, a technical team observes that the application takes a long time to launch and load memory to become fully productive. Which solution will reduce the launch time of the application during the next testing phase?

<details><summary>Answer</summary>

**C. Launch the EC2 On-Demand Instances with hibernation turned on. Configure EC2 Auto Scaling warm pools during the next testing phase.**

When you launch EC2 On-Demand Instances with hibernation turned on, the instances can be hibernated and resumed rather than terminated and launched.

</details>

### 222. q-595 `cost`

A company's applications run on Amazon EC2 instances in Auto Scaling groups. The company notices that its applications experience sudden traffic increases on random days of the week. The company wants to maintain application performance during sudden traffic increases. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use dynamic scaling to change the size of the Auto Scaling group.**

Dynamic Scaling: With dynamic scaling, the Auto Scaling group automatically adjusts its capacity based on real-time demand. It scales out during traffic spikes and scales in during periods of lower demand. This ensures that your application can handle sudden increases in traffic without manual intervention.

</details>

### 223. q-597

A company hosts an internal serverless application on AWS by using Amazon API Gateway and AWS Lambda. The company’s employees report issues with high latency when they begin using the application each day. The company wants to reduce latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up a scheduled scaling to increase Lambda provisioned concurrency before employees begin to use the application each day.**

Lambda Provisioned Concurrency: Provisioned concurrency is the number of simultaneous executions that your function can handle. By setting up a scheduled scaling to increase Lambda provisioned concurrency before employees begin using the application, you are proactively ensuring that there are enough resources available to handle the expected load.

</details>

### 224. dt-602

How many types of block devices does Amazon EC2 support?

<details><summary>Answer</summary>

**C. 2.**

</details>

### 225. q-611

A company has an application with a REST-based interface that allows data to be received in near-real time from a third-party vendor. Once received, the application processes and stores the data for further analysis. The application is running on Amazon EC2 instances. The third-party vendor has received many 503 Service Unavailable Errors when sending data to the application. When the data volume spikes, the compute capacity reaches its maximum limit and the application is unable to process all requests. Which design should a solutions architect recommend to provide a more scalable solution?

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Streams to ingest the data. Process the data using AWS Lambda functions.**

Kinesis Data Streams is designed for ingesting and processing real-time streaming data at scale. It can handle large volumes of data and provides the ability to scale horizontally.  Using Lambda functions allows for serverless, event-driven processing of the data. Lambda automatically scales based on the number of incoming events, providing the needed elasticity to handle spikes in data volume without the need to manage underlying infrastructure.

</details>

### 226. q-614

A company is designing a new multi-tier web application that consists of the following components: • Web and application servers that run on Amazon EC2 instances as part of Auto Scaling groups • An Amazon RDS DB instance for data storage A solutions architect needs to limit access to the application servers so that only the web servers can access them. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Deploy an Application Load Balancer with a target group that contains the application servers' Auto Scaling group. Configure the security group to allow only the web servers to access the application servers.**

An ALB is a load balancer service provided by AWS that allows you to distribute incoming application traffic across multiple targets, such as EC2 instances. In this scenario, the ALB is deployed in front of the application servers. The ALB is configured with a target group that includes the application servers' Auto Scaling group instances. The target group defines where the ALB directs traffic.

</details>

### 227. q-615

A company runs a critical, customer-facing application on Amazon Elastic Kubernetes Service (Amazon EKS). The application has a microservices architecture. The company needs to implement a solution that collects, aggregates, and summarizes metrics and logs from the application in a centralized location. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Configure Amazon CloudWatch Container Insights in the existing EKS cluster. View the metrics and logs in the CloudWatch console.**

CloudWatch Container Insights is specifically designed for monitoring containerized applications on Amazon EKS and ECS. It provides visibility into the performance of containers, clusters, and microservices.

</details>

### 228. dt-617

A web-startup runs its very successful social news application on Amazon EC2 with an Elastic Load Balancer, an Auto-Scaling group of Java/Tomcat application-servers, and DynamoDB as data store. The main web-application best runs on m2 x large instances since it is highly memory- bound Each new deployment requires semi-automated creation and testing of a new AMI for the application servers which takes quite a while and is therefore only done once per week. Recently, a new chat feature has been implemented in nodejs and waits to be integrated in the architecture. First tests show that the new component is CPU bound Because the company has some experience with using Chef, they decided to streamline the deployment process and use AWS OpsWorks as an application life cycle tool to simplify management of the application and reduce the deployment cycles. What configuration in AWS OpsWorks is necessary to integrate the new chat module in the most cost-efficient and flexible way?

<details><summary>Answer</summary>

**C. Create two AWS OpsWorks stacks create two AWS OpsWorks layers create one custom recipe.**

</details>

### 229. dt-619

A user is currently building a website which will require a large number of instances in six months, when a demonstration of the new site will be given upon launch. Which of the below mentioned options allows the user to procure the resources beforehand so that they need not worry about infrastructure availability during the demonstration?

<details><summary>Answer</summary>

**A. Procure all the instances as reserved instances beforehand.**

</details>

### 230. dt-624

To help you manage your Amazon EC2 instances, images, and other Amazon EC2 resources, you can assign your own metadata to each resource in the form of [...].

<details><summary>Answer</summary>

**C. tags.**

</details>

### 231. dt-626

If I write the below command, what does it do? ec2-run ami-e3a5408a -n 20 -g appserver

<details><summary>Answer</summary>

**A. Start twenty instances as members of appserver group.**

</details>

### 232. dt-628

In order to optimize performance for a compute cluster that requires low inter-node latency, which of the following feature should you use?

<details><summary>Answer</summary>

**D. Placement Groups.**

</details>

### 233. q-630 `cost`

A solutions architect is creating a data processing job that runs once daily and can take up to 2 hours to complete. If the job is interrupted, it has to restart from the beginning. How should the solutions architect address this issue in the MOST cost-effective manner?

<details><summary>Answer</summary>

**C. Use an Amazon Elastic Container Service (Amazon ECS) Fargate task triggered by an Amazon EventBridge scheduled event.**

ECS Fargate is a serverless container service, and it abstracts away the underlying infrastructure. With Fargate, you don't need to manage or provision EC2 instances directly. You can run containers without worrying about the infrastructure, and AWS takes care of scaling and resource allocation.

</details>

### 234. dt-633

How can you apply more than 100 rules to an Amazon EC2-Classic?

<details><summary>Answer</summary>

**D. You can't add more than 100 rules to security groups for an Amazon EC2 instance.**

</details>

### 235. dt-634

A user has created an ELB with Auto Scaling. Which of the below mentioned offerings from ELB helps the user to stop sending new requests traffic from the load balancer to the EC2 instance when the instance is being deregistered while continuing in-flight requests?

<details><summary>Answer</summary>

**D. ELB connection draining.**

</details>

### 236. q-635 `least-ops`

A company uses Amazon FSx for NetApp ONTAP in its primary AWS Region for CIFS and NFS file shares. Applications that run on Amazon EC2 instances access the file shares. The company needs a storage disaster recovery (DR) solution in a secondary Region. The data that is replicated in the secondary Region needs to be accessed by using the same protocols as the primary Region. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create an FSx for ONTAP instance in the secondary Region. Use NetApp SnapMirror to replicate data from the primary Region to the secondary Region.**

FSx for ONTAP supports NetApp SnapMirror, which is a robust data replication technology. You can use SnapMirror to replicate data from the primary FSx for ONTAP instance in the primary Region to an FSx for ONTAP instance in the secondary Region.

</details>

### 237. dt-637

A user is launching an EC2 instance in the US East region. Which of the below mentioned options is recommended by AWS with respect to the selection of the Availability Zone?

<details><summary>Answer</summary>

**C. Do not select the AZ; instead let AWS select the AZ.**

</details>

### 238. dt-638

ec2-revoke RevokeSecurityGroup Ingress

<details><summary>Answer</summary>

**C. Removes one or more rules from a security group.**

</details>

### 239. dt-641

A large real-estate brokerage is exploring the option of adding a cost-effective location based alert to their existing mobile application. The application backend infrastructure currently runs on AWS. Users who opt in to this service will receive alerts on their mobile device regarding real-estate offers in proximity to their location. For the alerts to be relevant delivery time needs to be in the low minute count. The existing mobile app has 5 million users across the US. Which one of the following architectural suggestions would you make to the customer?

<details><summary>Answer</summary>

**A. The mobile application will submit its location to a web service endpoint utilizing Elastic Load Balancing and EC2 instances. DynamoDB will be used to store and retrieve relevant offers. EC2 instances will communicate with mobile carriers/device providers to push alerts back to mobile application.**

</details>

### 240. q-642

A company wants to run a gaming application on Amazon EC2 instances that are part of an Auto Scaling group in the AWS Cloud. The application will transmit data by using UDP packets. The company wants to ensure that the application can scale out and in as traffic increases and decreases. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Attach a Network Load Balancer to the Auto Scaling group.**

UDP is a connectionless protocol, and Network Load Balancers (NLB) support UDP, making them suitable for applications that use UDP for transmitting data.

</details>

### 241. dt-644

What is a placement group in Amazon EC2?

<details><summary>Answer</summary>

**A. It is a group of EC2 instances within a single Availability Zone.**

</details>

### 242. dt-647

A company is building a web application that serves a content management system. The content management system runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The EC2 instances run in an Auto Scaling group across multiple Availability Zones. Users are constantly adding and updating files, blogs, and other website assets in the content management system. A solutions architect must implement a solution in which all the EC2 instances share up-to-date website content with the least possible lag time. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Copy the website assets to an Amazon Elastic File System (Amazon EFS) file system. Configure each EC2 instance to mount the EFS file system locally. Configure the website hosting application to reference the website assets that are stored in the EFS file system.**

</details>

### 243. dt-652

A company plans to run a high performance computing (HPC) workload on Amazon EC2 Instances. The workload requires low-latency network performance and high network throughput with tightly coupled node-to-node communication. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure the EC2 instances to be part of a cluster placement group.**

</details>

### 244. q-660

A company hosts an application on Amazon EC2 On-Demand Instances in an Auto Scaling group. Application peak hours occur at the same time each day. Application users report slow application performance at the start of peak hours. The application performs normally 2-3 hours after peak hours begin. The company wants to ensure that the application works properly at the start of peak hours. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a scheduled scaling policy for the Auto Scaling group to launch new instances before peak hours.**

Proactively scales instances to handle predictable traffic spikes. Dynamic scaling (Options B/C) reacts too slowly for known peaks.

</details>

### 245. dt-661

A company's near-real-time streaming application is running on AWS. As the data is ingested, a job runs on the data and takes 30 minutes to complete. The workload frequently experiences high latency due to large amounts of incoming data. A solutions architect needs to design a scalable and serverless solution to enhance performance. Which combination of steps should the solutions architect take? (Choose two.)

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Firehose to ingest the data.; E. Use AWS Fargate with Amazon Elastic Container Service (Amazon ECS) to process the data.**

</details>

### 246. gh-664

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

### 247. dt-670

A company hosts its application in the AWS Cloud. The application runs on Amazon EC2 instances behind an Elastic Load Balancer in an Auto Scaling group and with an Amazon DynamoDB table. The company wants to ensure the application can be made available in another AWS Region with minimal downtime. What should a solutions architect do to meet these requirements with the LEAST amount of downtime?

<details><summary>Answer</summary>

**A. Create an Auto Scaling group and a load balancer in the disaster recovery Region. Configure the DynamoDB table as a global table. Configure DNS failover to point to the new disaster recovery Region's load balancer.**

</details>

### 248. gh-671

A company runs its applications on Amazon EC2 instances. The company performs periodic nancial assessments of its AWS costs. The
company recently identi ed unusual spending.
The company needs a solution to prevent unusual spending. The solution must monitor costs and notify responsible stakeholders in the event of
unusual spending.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Create an AWS Cost Anomaly Detection monitor.**

Cost Anomaly Detection applies machine learning to your AWS cost and usage data and raises an alert when spend departs from the learned pattern, naming the service, linked account, cost category or tag the unexpected charges came from. Alerts go to email or to an Amazon SNS topic, either one at a time or as a daily or weekly summary, so the responsible stakeholders hear about it without anyone running a manual review. CloudWatch can also detect anomalies in a metric, but the only billing data it holds is the coarse EstimatedCharges metric in us-east-1, so it cannot break spend down by service or account; AWS Budgets is useful alongside this but fires on thresholds you set yourself rather than on unusual patterns.

</details>

### 249. dt-672 `cost` `availability`

A company hosts an application on Amazon EC2 instances that run in a single Availability Zone. The application is accessible by using the transport layer of the Open Systems Interconnection (OSI) model. The company needs the application architecture to have high availability. Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**B. Configure a Network Load Balancer in front of the EC2 instances.; D. Create an Auto Scaling group for the EC2 instances. Configure the Auto Scaling group to use multiple Availability Zones. Configure the Auto Scaling group to run application health checks on the instances.**

</details>

### 250. dt-675 `cost`

A company runs an ecommerce application on AWS. Amazon EC2 instances process purchases and store the purchase details in an Amazon Aurora PostgreSQL DB cluster. Customers are experiencing application timeouts during times of peak usage. A solutions architect needs to rearchitect the application so that the application can scale to meet peak usage demands. Which combination of actions will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**A. Configure an Auto Scaling group of new EC2 instances to retry the purchases until the processing is complete. Update the applications to connect to the DB cluster by using Amazon RDS Proxy.; C. Update the application to send the purchase requests to an Amazon Simple Queue Service (Amazon SQS) queue. Configure an Auto Scaling group of new EC2 instances that read from the SQS queue.**

</details>

### 251. gh-677 `cost`

A company is developing an application that will run on a production Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster
has managed node groups that are provisioned with On-Demand Instances.
The company needs a dedicated EKS cluster for development work. The company will use the development cluster infrequently to test the
resiliency of the application. The EKS cluster must manage all the nodes.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Create an EKS managed node group that contains only Spot Instances.**

Spot Instances are the cheapest way to get EC2 capacity, at a steep discount to On-Demand, and the trade-off - the instance can be reclaimed at short notice - does not matter for a development cluster used occasionally to test how the application copes with failure. EKS managed node groups support Spot capacity directly and handle provisioning, draining on interruption and version upgrades, so the requirement that the cluster manage all the nodes is met. Mixing in On-Demand Instances raises the bill without meeting any stated requirement, and a self-managed Auto Scaling group with bootstrap scripts hands node management back to you.

</details>

### 252. dt-678

A company uses Amazon EC2 instances and AWS Lambda functions to run its application. The company has VPCs with public subnets and private subnets in its AWS account. The EC2 instances run in a private subnet in one of the VPCs. The Lambda functions need direct network access to the EC2 instances for the application to work. The application will run for at least 1 year. The company expects the number of Lambda functions that the application uses to increase during that time. The company wants to maximize its savings on all application resources and to keep network latency between the services low. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Purchase a Compute Savings Plan. Optimize the Lambda functions' duration and memory usage, the number of invocations, and the amount of data that is transferred. Connect the Lambda functions to the private subnet that contains the EC2 instances.**

</details>

### 253. dt-688 `least-ops`

A company observes an increase in Amazon EC2 costs in its most recent bill. The billing team notices unwanted vertical scaling of instance types for a couple of EC2 instances. A solutions architect needs to create a graph comparing the last 2 months of EC2 costs and perform an in-depth analysis to identify the root cause of the vertical scaling. How should the solutions architect generate the information with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Cost Explorer's granular filtering feature to perform an in-depth analysis of EC2 costs based on instance types.**

</details>

### 254. dt-707

A company has released a new version of its production application. The company's workload uses Amazon EC2, AWS Lambda, AWS Fargate, and Amazon SageMaker. The company wants to cost optimize the workload now that usage is at a steady state. The company wants to cover the most services with the fewest savings plans. Which combination of savings plans will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Purchase a SageMaker Savings Plan.; D. Purchase a Compute Savings Plan for Lambda, Fargate, and Amazon EC2.**

</details>

### 255. dt-742

A company wants to host its web application on AWS using multiple Amazon EC2 instances across different AWS Regions. Since the application content will be specific to each geographic region, the client requests need to be routed to the server that hosts the content for that clients Region. What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**C. Configure Amazon Route 53 with a geolocation routing policy.**

</details>

### 256. dt-744

A recently created startup built a three-tier web application. The front end has static content. The application layer is based on microservices. User data is stored as JSON documents that need to be accessed with low latency. The company expects regular traffic to be low during the first year, with peaks in traffic when it publicizes new features every month. The startup team needs to minimize operational overhead costs. What should a solutions architect recommend to accomplish this?

<details><summary>Answer</summary>

**C. Use Amazon S3 static website hosting to store and serve the front end. Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon DynamoDB to store user data.**

</details>

### 257. dt-747

A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular. Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. The requests from the API are sent to the model's Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue. AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size.**

</details>

### 258. dt-754

A company hosts its web application on AWS using seven Amazon EC2 instances. The company requires that the IP addresses of all healthy EC2 instances be returned in response to DNS queries. Which policy should be used to meet this requirement?

<details><summary>Answer</summary>

**C. Multivalue answer routing policy**

</details>

### 259. dt-763

An ecommerce website is deploying its web application as Amazon Elastic Container Service (Amazon ECS) container instances behind an Application Load Balancer (ALB). During periods of high activity, the website slows down and availability is reduced. A solutions architect uses Amazon CloudWatch alarms to receive notifications whenever there is an availability issue so they can scale out resources. Company management wants a solution that automatically responds to such events. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Set up AWS Auto Scaling to scale out the ECS service when the service's CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.**

</details>

### 260. dt-766

A company has a three-tier environment on AWS that ingests sensor data from its users' devices. The traffic flows through a Network Load Balancer (NLB) then to Amazon EC2 instances for the web tier, and finally to EC2 instances for the application tier that makes database calls. What should a solutions architect do to improve the security of data in transit to the web tier?

<details><summary>Answer</summary>

**A. Configure a TLS listener and add the server certificate on the NLB.**

</details>

### 261. dt-769

A company runs a web application on Amazon EC2 instances in an Auto Scaling group that has a target group. The company designed the application to work with session affinity (sticky sessions) for a better user experience. The application must be available publicly over the internet as an endpoint. A WAF must be applied to the endpoint for additional security. Session affinity (sticky sessions) must be configured on the endpoint. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Create a public Application Load Balancer. Specify the application target group.; E. Create a web ACL in AWS WAF. Associate the web ACL with the endpoint.**

</details>

### 262. dt-770 `availability`

A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer that has sticky sessions enabled. The web server currently hosts the user session state. The company wants to ensure high availability and avoid user session state loss in the event of a web server outage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon ElastiCache for Redis to store the session state. Update the application to use ElastiCache for Redis to store the session state.**

</details>
