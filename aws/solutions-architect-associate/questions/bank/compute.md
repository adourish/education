# Compute — EC2, Lambda, containers, scaling

366 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

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

### 6. q-7

A company has applications that run on Amazon EC2 instances in a VPC One of the applications needs to call the Amazon S3 API to store and read objects. According to the company's security regulations, no traffic from the applications is allowed to travel across the internet. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Publish the messages to an Amazon Simple Notification Service (Amazon SNS) topic with multiple Amazon Simple Queue Service (Amazon SQS) queue subscriptions. Configure the consumer applications to process the messages from the queues.**

The fan-out pattern has the producer publish each message once to an SNS topic, which then delivers a copy into every subscribed SQS queue, so each of the dozens of consumers reads from its own queue and can scale, slow down or fail without affecting the others. The queues absorb the sudden spikes, which is what decouples the producer from consumer speed. Standard SQS queues give at-least-once delivery, best-effort ordering, and a nearly unlimited number of transactions per second, so a burst of 100,000 messages per second needs no quota request; it is FIFO queues that are capped, at 300 API calls per second per action or 3,000 messages per second when batching, with high throughput mode raising that further. Optionally give each subscription a filter policy so a consumer's queue only receives the message types it cares about.

</details>

### 7. q-12

A company is designing a new multi-tier web application that consists of the following components: • Web and application servers that run on Amazon EC2 instances as part of Auto Scaling groups • An Amazon RDS DB instance for data storage A solutions architect needs to limit access to the application servers so that only the web servers can access them. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Deploy an Application Load Balancer with a target group that contains the application servers' Auto Scaling group. Configure the security group to allow only the web servers to access the application servers.**

This solution describes a standard, secure, and scalable multi-tier architecture. An Application Load Balancer (ALB) is designed to operate at the application layer (HTTP/HTTPS), making it the ideal choice for distributing traffic to application servers. The core requirement is to restrict access between tiers. Security groups are stateful firewalls that operate at the instance level and are the best practice for this purpose. By creating a rule in the application servers' security group that specifies the web servers' security group as the source, access is precisely limited to only instances within that web server group. This method is highly manageable, especially with Auto Scaling, as new instances automatically inherit the correct permissions. Why Incorrect Options are Wrong: A. AWS PrivateLink is primarily for providing private connectivity between VPCs or to AWS services, not for

</details>

### 8. dt-12

In Amazon EC2 Container Service, are other container types supported?

<details><summary>Answer</summary>

**C. No, Docker is the only container platform supported by EC2 Container Service presently.**

</details>

### 9. dt-14

Name the disk storage supported by Amazon Elastic Compute Cloud (EC2)

<details><summary>Answer</summary>

**D. Amazon Instance Store.**

</details>

### 10. wl-19

Which of the following are not backup and restore solutions provided by AWS? (choose multiple)

<details><summary>Answer</summary>

**C. AWS Elastic Beanstalk; E.**

Option A is snapshot based data backup solution.
Option B, AWS Storage Gateway provides multiple solutions for backup & recovery.
Option D can be used as a Database backup solution.

</details>

### 11. q-20

A company has an application that serves clients that are deployed in more than 20.000 retail storefront locations around the world. The application consists of backend web services that are exposed over HTTPS on port 443 The application is hosted on Amazon EC2 Instances behind an Application Load Balancer (ALB). The retail locations communicate with the web application over the public internet. The company allows each retail location to register the IP address that the retail location has been allocated by its local ISP. The company's security team recommends to increase the security of the application endpoint by restricting access to only the IP addresses registered by the retail locations. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Associate an AWS WAF web ACL with the ALB Use IP rule sets on the ALB to filter traffic Update the IP addresses in the rule to Include the registered IP addresses**

The most appropriate solution is to use AWS WAF (Web Application Firewall) with an IP set match rule. AWS WAF is designed to protect web applications from common exploits and can filter traffic based on various conditions, including the source IP address. A solutions architect can create one or more IP sets containing the 20,000+ registered IP addresses. This IP set is then used in a rule within a web ACL, which is associated directly with the Application Load Balancer (ALB). This approach efficiently filters traffic at the edge, allowing only requests from known retail locations to reach the application, fulfilling the security requirement in a scalable and manageable way. Why Incorrect Options are Wrong: B: AWS Firewall Manager is a service for centrally managing security policies (like WAF rules) across multiple accounts and resources, not the primary tool for creating the IP filterin

</details>

### 12. dt-20

Select the most correct The device name /dev/sdal (within Amazon EC2) is [...].

<details><summary>Answer</summary>

**B. reserved for the root device.**

</details>

### 13. wl-20

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

### 14. q-27

A developer is creating a serverless application that performs video encoding. The encoding process runs as background jobs and takes several minutes to encode each video. The process must not send an immediate result to users. The developer is using Amazon API Gateway to manage an API for the application. The developer needs to run test invocations and request validations. The developer must distribute API keys to control access to the API. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a REST API with the default endpoint type. Create an AWS Lambda function to handle the encoding jobs. Integrate the function with the REST API. Use the Event invocation type to call the Lambda function.**

The solution requires an API that supports test invocations, request validation, and API keys. Amazon API Gateway REST APIs provide these features, whereas HTTP APIs do not. The video encoding process is a long-running background job that takes several minutes, exceeding the 29-second synchronous timeout of API Gateway. Therefore, the AWS Lambda function must be invoked asynchronously. The Event invocation type is used for asynchronous execution, where the caller does not wait for the function to complete. This combination of a REST API and the Event invocation type meets all the specified requirements. Why Incorrect Options are Wrong: A. HTTP APIs do not support API keys, request validation, or test invocations from the AWS Management Console, which are explicit requirements of the scenario. C. This option is incorrect for two reasons: HTTP APIs lack the required features (API keys, val

</details>

### 15. dt-29

What is the network performance offered by the c4.8xlarge instance in Amazon EC2?

<details><summary>Answer</summary>

**B. 10 Gigabit.**

</details>

### 16. dt-35

What does Amazon Elastic Beanstalk provide?

<details><summary>Answer</summary>

**B. An application container on top of Amazon Web Services.**

</details>

### 17. dt-45 `availability`

A user is planning a highly available application deployment with EC2. Which of the below mentioned options will not help to achieve HA?

<details><summary>Answer</summary>

**B. PIOPS.**

</details>

### 18. dt-47

Which of the following statements is true of tagging an Amazon EC2 resource?

<details><summary>Answer</summary>

**C. You can't terminate, stop, or delete a resource based solely on its tags.**

</details>

### 19. q-47

A company needs guaranteed Amazon EC2 capacity in three specific Availability Zones in a specific AWS Region for an upcoming event that will last 1 week. What should the company do to guarantee the EC2 capacity?

<details><summary>Answer</summary>

**D. Create an On-Demand Capacity Reservation that specifies the Region and three Availability Zones needed.**

An On-Demand Capacity Reservation is a type of Amazon EC2 reservation that enables you to create and manage reserved capacity on Amazon EC2. With an On-Demand Capacity Reservation, you can specify the Region and Availability Zones where you want to reserve capacity, and the number of EC2 instances you want to reserve. This allows you to guarantee capacity in specific Availability Zones in a specific Region.

</details>

### 20. q-48

A company runs its workloads on Amazon Elastic Container Service (Amazon ECS). The container images that the ECS task definition uses need to be scanned for Common Vulnerabilities and Exposures (CVEs). New container images that are created also need to be scanned. Which solution will meet these requirements with the FEWEST changes to the workloads?

<details><summary>Answer</summary>

**A. Use Amazon Elastic Container Registry (Amazon ECR) as a private image repository to store the container images. Specify scan on push filters for the ECR basic scan.**

Amazon Elastic Container Registry (ECR) is the native AWS fully-managed container registry that integrates seamlessly with Amazon Elastic Container Service (ECS). ECR provides a built-in vulnerability scanning feature that can be configured to automatically scan images upon being pushed to a repository ("scan on push"). This directly addresses the requirement to scan new container images for Common Vulnerabilities and Exposures (CVEs) as they are created. This solution requires the fewest changes to the existing ECS workload, as it only involves pointing the ECS task definition to the ECR repository, which is a standard and minimal configuration change. Why Incorrect Options are Wrong: B: Amazon Macie is a data security service designed to discover and protect sensitive data (like PII or financial data) within Amazon S3, not to scan container images for software vulnerabilities (CVEs). C

</details>

### 21. q-48 `availability`

A company's website uses an Amazon EC2 instance store for its catalog of items. The company wants to make sure that the catalog is highly available and that the catalog is stored in a durable location. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Move the catalog to an Amazon Elastic File System (Amazon EFS) file system.**

EFS is fully managed, durable, highly available, and shared file system.

</details>

### 22. dt-49

Are Reserved Instances available for Multi-AZ Deployments?

<details><summary>Answer</summary>

**B. Yes for all instance types.**

</details>

### 23. q-51

A company is developing an application that provides order shipping statistics for retrieval by a REST API. The company wants to extract the shipping statistics, organize the data into an easy-to-read HTML format, and send the report to several email addresses at the same time every morning. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**Both of the following: (1) Create an Amazon EventBridge scheduled event that invokes an AWS Lambda function to query the application's API for the data; and (2) use Amazon Simple Email Service (Amazon SES) to send the report by email.**

The report has to go out at the same time every morning, which is exactly what an EventBridge schedule does, and the thing it triggers needs to call a REST API and build HTML, which is ordinary Lambda work with no servers to run. Amazon SES then delivers the HTML message to the list of recipients in one send, and it is the AWS service meant for sending application email to real mailboxes. An SNS topic can notify subscribers but is not suited to delivering a formatted HTML report, and a Glue job is for extract-transform-load work over data stores, not for calling an API and emailing a page.

</details>

### 24. q-53

A company wants to implement new security compliance requirements for its development team to limit the use of approved Amazon Machine Images (AMIs). The company wants to provide access to only the approved operating system and software for all its Amazon EC2 instances. The company wants the solution to have the least amount of lead time for launching EC2 instances. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a portfolio by using AWS Service Catalog that includes only EC2 instances launched with approved AMIs. Ensure that all required software is preinstalled on the AMIs. Create the necessary permissions for developers to use the portfolio.**

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. By creating a portfolio with a product that launches EC2 instances from a pre-approved, "golden" Amazon Machine Image (AMI), the company can enforce compliance. This AMI would have the required operating system and software pre-installed. This approach provides a governed, self-service model for developers while meeting the "least amount of lead time" requirement, as instances launch quickly from a fully configured image without needing post-launch installations. Why Incorrect Options are Wrong: B. This option lacks the governance and enforcement layer. Simply giving developers access to an AMI does not prevent them from using other, unapproved AMIs they might have access to. C. This solution increases the lead time for an instance to become fully operational because so

</details>

### 25. dt-53 `cost`

To serve Web traffic for a popular product your chief financial officer and IT director have purchased 10 ml large heavy utilization Reserved Instances (RIs) evenly spread across two Availability Zones. Route 53 is used to deliver the traffic to an Elastic Load Balancer (ELB). After several months, the product grows even more popular and you need additional capacity. As a result, your company purchases two C3.2xlarge medium utilization RIs. You register the two c3 2xlarge instances with your ELB and quickly find that the ml large instances are at 100% of capacity and the c3 2xlarge instances have significant capacity that's unused. Which option is the most cost effective and uses EC2 capacity most effectively?

<details><summary>Answer</summary>

**A. Use a separate ELB for each instance type and distribute load to ELBs with Route 53 weighted round robin.**

</details>

### 26. dt-55

A user has launched one EC2 instance in the US West region. The user wants to access the RDS instance launched in the US East region from that EC2 instance. How can the user configure the access for that EC2 instance?

<details><summary>Answer</summary>

**A. Configure the IP range of the US West region instance as the ingress security rule of RDS.**

</details>

### 27. dt-57

While creating an Amazon RDS DB, your first task is to set up a DB [...] that controls which IP address or EC2 instance can access your DB Instance.

<details><summary>Answer</summary>

**D. security group.**

</details>

### 28. dt-59

In the context of AWS support, why must an EC2 instance be unreachable for 20 minutes rather than allowing customers to open tickets immediately?

<details><summary>Answer</summary>

**A. Because most reachability issues are resolved by automated processes in less than 20 minutes.**

</details>

### 29. dt-62

While creating the snapshots using the command line tools, which command should I be using?

<details><summary>Answer</summary>

**C. ec2-create-snapshot.**

</details>

### 30. dt-63

All Amazon EC2 instances are assigned two IP addresses at launch, out of which one can only be reached from within the Amazon EC2 network?

<details><summary>Answer</summary>

**C. Private IP address.**

</details>

### 31. dt-65

You've created your first load balancer and have registered your EC2 instances with the load balancer. Elastic Load Balancing routinely performs health checks on all the registered EC2 instances and automatically distributes all incoming requests to the DNS name of your load balancer across your registered, healthy EC2 instances. By default, the load balancer uses the [...] protocol for checking the health of your instances.

<details><summary>Answer</summary>

**B. HTTP.**

</details>

### 32. dt-66

Amazon Elastic Load Balancing is used to manage traffic on a fleet of Amazon EC2 instances, distributing traffic to instances across all Availability Zones within a region. Elastic Load Balancing has all the advantages of an on-premises load balancer, plus several security benefits. Which of the following is not an advantage of ELB over an on-premise load balancer?

<details><summary>Answer</summary>

**A. ELB uses a four-tier, key-based architecture for encryption.**

</details>

### 33. dt-67 `availability`

A web company is looking to implement an external payment service into their highly available application deployed in a VPC. Their application EC2 instances are behind a public facing ELB. Auto scaling is used to add additional instances as traffic increases. Under normal load the application runs 2 instances in the Auto Scaling group but at peak it can scale 3x in size. The application instances need to communicate with the payment service over the Internet which requires whitelisting of all public IP addresses used to communicate with it. A maximum of 4 whitelisting IP addresses are allowed at a time and can be added through an API. How should they architect their solution?

<details><summary>Answer</summary>

**A. Route payment requests through two NAT instances setup for High Availability and whitelist the Elastic IP addresses attached to the NAT instances.**

</details>

### 34. q-68 `least-ops`

A media company hosts a web application on AWS for uploading videos. Only authenticated users should upload within a specified time frame after authentication. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an AWS Lambda function that generates pre-signed URLs when a user authenticates.**

Generating a pre-signed URL is the most efficient and secure method for this scenario. After a user authenticates with the web application, a backend process (like an AWS Lambda function) can generate a short-lived, pre-signed URL. This URL grants the user temporary permission to perform a specific action (e.g., PUT Object) on a specific S3 object key. The client can then upload the video directly to S3 using this URL, which offloads the data transfer from the application server. This serverless approach using Lambda and S3's native pre-signed URL feature perfectly meets the requirements of time-limited access for authenticated users with the least operational overhead. Why Incorrect Options are Wrong: A. This is less efficient than a pre-signed URL. It requires the client application to manage temporary credentials (access key, secret key, session token) and use the AWS SDK to sign the

</details>

### 35. dt-74

You are trying to launch an EC2 instance, however the instance seems to go into a terminated status immediately. What would probably not be a reason that this is happening?

<details><summary>Answer</summary>

**C. You need to create storage in EBS first.**

</details>

### 36. dt-78

Your company produces customer commissioned one-of-a-kind skiing helmets combining high fashion with custom technical enhancements. Customers can show off their Individuality on the ski slopes and have access to head-up-displays. GPS rear-view cams and any other technical innovation they wish to embed in the helmet. The current manufacturing process is data rich and complex including assessments to ensure that the custom electronics and materials used to assemble the helmets are to the highest standards. Assessments are a mixture of human and automated assessments you need to add a new set of assessment to model the failure modes of the custom electronics using GPUs with CUDA, across a cluster of servers with low latency networking. What architecture would allow you to automate the existing process using a hybrid approach and ensure that the architecture can support the evolution of processes over time?

<details><summary>Answer</summary>

**B. Use Amazon Simple Workflow (SWF) to manages assessments, movement of data & meta-data Use an auto-scaling group of G2 instances in a placement group.**

</details>

### 37. dt-89

A user is aware that a huge download is occurring on his instance. He has already set the Auto Scaling policy to increase the instance count when the network I/O increases beyond a certain limit. How can the user ensure that this temporary event does not result in scaling?

<details><summary>Answer</summary>

**D. Suspend scaling.**

</details>

### 38. dt-90

The Amazon EC2 web service can be accessed using the [...] web services messaging protocol. This interface is described by a Web Services Description Language (WSDL) document.

<details><summary>Answer</summary>

**A. SOAP.**

</details>

### 39. q-94

A company is designing a new Amazon Elastic Kubernetes Service (Amazon EKS) deployment to host multi-tenant applications that use a single cluster. The company wants to ensure that each pod has its own hosted environment. The environments must not share CPU, memory, storage, or elastic network interfaces. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon EKS with AWS Fargate. Use Fargate to manage resources and to enforce isolation boundaries.**

The question requires a solution where each pod in a multi-tenant Amazon EKS cluster has its own completely isolated environment, with no shared CPU, memory, storage, or elastic network interface (ENI). AWS Fargate is a serverless compute engine for containers that meets these requirements by design. When used with Amazon EKS, each pod scheduled on Fargate runs in its own dedicated, isolated compute environment. This provides a virtual machine-like boundary, ensuring that pods do not share the underlying kernel or any hardware resources, which is the highest level of isolation available for pods within a single EKS cluster. Why Incorrect Options are Wrong: A. Taints and tolerations are Kubernetes scheduling mechanisms that control pod placement, not resource isolation. Pods on the same self-managed EC2 node still share the kernel and resources. C. Using self-managed node groups with EKS

</details>

### 40. dt-103

What is a Security Group?

<details><summary>Answer</summary>

**D. A firewall for inbound traffic, built-in around every Amazon EC2 instance.**

</details>

### 41. dt-111

You have been given a scope to deploy some AWS infrastructure for a large organization. The requirements are that you will have a lot of EC2 instances but may need to add more when the average utilization of your Amazon EC2 fleet is high and conversely remove them when CPU utilization is low. Which AWS services would be best to use to accomplish this?

<details><summary>Answer</summary>

**B. Auto Scaling, Amazon CloudWatch and Elastic Load Balancing.**

</details>

### 42. dt-112

When does the billing of an Amazon EC2 system begin?

<details><summary>Answer</summary>

**D. It starts when Amazon EC2 initiates the boot sequence of an AMI instance.**

</details>

### 43. q-116

An e-commerce company stores inventory, order, and user information in multiple Amazon Redshift clusters. The Redshift clusters must comply with the company's security policies. The company must receive notifications about any security configuration violations. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an AWS Lambda function to check the Redshift clusters for any violation of the security configurations. Create an AWS Config custom rule to invoke the Lambda function when Redshift cluster security configurations are modified. Provide the compliance state of each Redshift cluster to AWS Config. Configure AWS Config to notify the company of any violations of the security policies.**

This solution correctly uses AWS Config, the service designed for assessing, auditing, and evaluating the configurations of AWS resources. By creating a custom AWS Config rule, the company can define its specific security policies. This rule triggers an AWS Lambda function whenever a Redshift cluster's configuration is modified. The Lambda function contains the custom logic to check for violations. It then reports the compliance status (compliant or non-compliant) back to the AWS Config dashboard. AWS Config can be integrated with Amazon SNS to send notifications automatically when a resource is flagged as non-compliant, meeting all the stated requirements for continuous monitoring and alerting. Why Incorrect Options are Wrong: A. Amazon EventBridge for Redshift primarily captures high-level state change events (e.g., cluster created, snapshot started), not the detailed configuration cha

</details>

### 44. dt-117

Can you move a Reserved Instance from one Availability Zone to another?

<details><summary>Answer</summary>

**A. Yes, but each Reserved Instance is associated with a specific Region that cannot be changed.**

</details>

### 45. q-121

A company wants to create an Amazon EMR cluster that multiple teams will use. The company wants to ensure that each team's big data workloads can access only the AWS services that each team needs to interact with. The company does not want the workloads to have access to Instance Metadata Service Version 2 (IMDSv2) on the cluster's underlying EC2 instances. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create EMR runtime roles. Configure the cluster to use the runtime roles. Use the runtime roles to submit the big data workloads.**

Amazon EMR runtime roles are the designated feature for providing granular, least-privilege permissions in a multi-tenant cluster environment. By assigning a specific IAM role to each EMR step (workload), each team's job acquires only the permissions defined in its associated runtime role. This isolates permissions on a per-job basis, preventing one team's workload from accessing another team's resources. This mechanism provides credentials directly to the application, decoupling it from the broader permissions of the EC2 instance profile, which aligns with the requirement to not rely on the instance metadata service for workload-specific credentials. Why Incorrect Options are Wrong: A. Interface VPC endpoints are a networking feature for private connectivity to AWS services. They do not control or assign IAM permissions to applications. C. An EC2 instance profile applies a single IAM ro

</details>

### 46. dt-121

Which of the following statements best describes the differences between Elastic Beanstalk and CloudFormation?

<details><summary>Answer</summary>

**D. CloudFormation is much more powerful than Elastic Beanstalk, because you can actually design and script custom resources.**

</details>

### 47. dt-125

Does AWS CloudFormation support Amazon EC2 tagging?

<details><summary>Answer</summary>

**A. Yes, AWS CloudFormation supports Amazon EC2 tagging.**

</details>

### 48. dt-128

To specify a resource in a policy statement, in Amazon EC2, can you use its Amazon Resource Name (ARN)?

<details><summary>Answer</summary>

**A. Yes, you can.**

</details>

### 49. dt-130

By default what are ENIs that are automatically created and attached to instances using the EC2 console set to do when the attached instance terminates?

<details><summary>Answer</summary>

**B. Terminate.**

</details>

### 50. dt-131

In EC2, what happens to the data in an instance store if an instance reboots (either intentionally or unintentionally)?

<details><summary>Answer</summary>

**B. Data persists in the instance store.**

</details>

### 51. dt-141

All Amazon EC2 instances are assigned two IP addresses at launch. Which are those?

<details><summary>Answer</summary>

**D. A private IP address and a public IP address.**

</details>

### 52. dt-142

You need to pass a custom script to new Amazon Linux instances created in your Auto Scaling group. Which feature allows you to accomplish this?

<details><summary>Answer</summary>

**A. User data.**

</details>

### 53. dt-144

Which DNS name can only be resolved within Amazon EC2?

<details><summary>Answer</summary>

**B. Internal DNS name.**

</details>

### 54. dt-145

An AWS customer is deploying an application that is composed of an AutoScaling group of EC2 Instances. The customers security policy requires that every outbound connection from these instances to any other service within the customers Virtual Private Cloud must be authenticated using a unique x 509 certificate that contains the specific instance-id. In addition an x 509 certificates must be designed by the customer's Key management service in order to be trusted for authentication. Which of the following configurations will support these requirements?

<details><summary>Answer</summary>

**C. Configure the Auto Scaling group to send an SNS notification of the launch of a new instance to the trusted key management service. Have the Key management service generate a signed certificate and send it directly to the newly launched instance.**

</details>

### 55. dt-147

In Amazon EC2, you are billed instance-hours when [...].

<details><summary>Answer</summary>

**A. your EC2 instance is in a running state.**

</details>

### 56. dt-149

In Amazon EC2 Container Service components, what is the name of a logical grouping of container instances on which you can place tasks?

<details><summary>Answer</summary>

**A. A cluster.**

</details>

### 57. q-157

A company needs an automated solution to detect cryptocurrency mining activity on Amazon EC2 instances. The solution must automatically isolate any identified EC2 instances for forensic analysis. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon EventBridge rule that runs when Amazon GuardDuty detects cryptocurrency mining activity. Configure the rule to invoke an AWS Lambda function to isolate the identified EC2 instances.**

Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity, including cryptocurrency mining. When GuardDuty detects a threat, it generates a finding and sends it as an event to Amazon EventBridge. An EventBridge rule can be configured to filter for specific GuardDuty finding types (e.g., CryptoCurrency:EC2/BitcoinTool.B!DNS). This rule can then automatically invoke an AWS Lambda function as a target. The Lambda function can contain the necessary code to perform remediation actions, such as modifying security groups or network ACLs to isolate the compromised EC2 instance for forensic analysis. This provides a fully automated detection and response solution. Why Incorrect Options are Wrong: B: AWS Security Hub custom actions are designed for manual, user-initiated responses from the console, not for automated, event-driven remediation as required by th

</details>

### 58. q-163

A company runs an application on Amazon EC2 instances behind an Application Load Balancer (ALB). The company wants to create a public API for the application that uses JSON Web Tokens (JWT) for authentication. The company wants the API to integrate directly with the ALB. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon API Gateway to create an HTTP API.**

Amazon API Gateway HTTP APIs are the ideal solution for this scenario. They are designed for building low-latency and cost-effective APIs that proxy requests to HTTP endpoints, such as an Application Load Balancer (ALB). A key feature of HTTP APIs is the built-in support for JSON Web Token (JWT) authorizers. This allows for native integration with OpenID Connect (OIDC) and OAuth 2.0-compliant identity providers to secure the API, directly fulfilling the authentication requirement without the need for custom AWS Lambda authorizers. The API can then be configured with a private integration to forward authorized requests directly to the ALB. Why Incorrect Options are Wrong: A. While a REST API can integrate with an ALB and use authorizers, it does not have the same streamlined, built-in JWT authorizer as an HTTP API, often requiring a more complex Lambda or Cognito authorizer setup. C. A We

</details>

### 59. dt-164

A major customer has asked you to set up his AWS infrastructure so that it will be easy to recover in the case of a disaster of some sort. Which of the following statements is true of Amazon EC2 security groups?

<details><summary>Answer</summary>

**D. All items listed here are important when thinking about disaster recovery.**

</details>

### 60. dt-165

Select a true statement about Amazon EC2 Security Groups (EC2-Classic).

<details><summary>Answer</summary>

**A. After you launch an instance in EC2-Classic, you can't change its security groups.**

</details>

### 61. dt-168

You have an EC2 Security Group with several running EC2 instances. You change the Security Group rules to allow inbound traffic on a new port and protocol, and launch several new instances in the same Security Group. The new rules apply:

<details><summary>Answer</summary>

**A. Immediately to all instances in the security group.**

</details>

### 62. dt-173

You try to connect via SSH to a newly created Amazon EC2 instance and get one of the following error messages: 'Network error: Connection timed out' or 'Error connecting to [instance], reason: -> Connection timed out: connect,' You have confirmed that the network and security group rules are configured correctly and the instance is passing status checks. What steps should you take to identify the source of the behavior? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Verify that the private key file corresponds to the Amazon EC2 key pair assigned at launch.; C. Verify that you are connecting with the appropriate user name for your AMI.**

</details>

### 63. dt-174

An Auto-Scaling group spans 3 AZs and currently has 4 running EC2 instances. When Auto Scaling needs to terminate an EC2 instance by default, AutoScaling will: (Choose 2 answers)

<details><summary>Answer</summary>

**C. Send an SNS notification, if configured to do so.; D. Terminate an instance in the AZ which currently has 2 running EC2 instances.**

</details>

### 64. q-190 `availability`

A company has a web application that is based on Java and PHP. The company plans to move the application from on premises to AWS. The company needs the ability to test new site features frequently. The company also needs a highly available and managed solution that requires minimum operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the web application to an AWS Elastic Beanstalk environment. Use URL swapping to switch between multiple Elastic Beanstalk environments for feature testing.**

Elastic Beanstalk allows you to perform blue-green deployments, which involve creating a new environment (green) with the updated code, testing it, and then swapping the URLs to direct traffic to the new environment. This enables you to test new features without affecting the production environment.

</details>

### 65. q-192

A developer creates a web application that runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances are in an Auto Scaling group. The developer reviews the deployment and notices some suspicious traffic to the application. The traffic is malicious and is coming from a single public IP address. A solutions architect must block the public IP address. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Add the malicious IP address to an IP set in AWS WAF. Create a web ACL. Include an IP set rule with the action set to BLOCK. Associate the web ACL with the ALB.**

AWS Web Application Firewall (WAF) is a service designed to protect web applications from common exploits that could affect availability or security. The most direct and effective method to block a specific malicious IP address for an application behind an Application Load Balancer (ALB) is by using AWS WAF. The process involves creating an IP set containing the malicious IP address, defining a rule within a web access control list (web ACL) to block requests from that IP set, and then associating this web ACL with the ALB. This solution filters traffic at the application layer before it reaches the EC2 instances. Why Incorrect Options are Wrong: A. Security groups do not support explicit deny rules. They are stateful and only allow the creation of allow rules. B. Amazon Detective is a security investigation service used for analyzing and visualizing security data to identify the root ca

</details>

### 66. dt-201

Which Amazon Elastic Compute Cloud feature can you query from within the instance to access instance properties?

<details><summary>Answer</summary>

**C. Instance metadata.**

</details>

### 67. q-209

A solutions architect is designing the architecture of a new application being deployed to the AWS Cloud. The application will run on Amazon EC2 On-Demand Instances and will automatically scale across multiple Availability Zones. The EC2 instances will scale up and down frequently throughout the day. An Application Load Balancer (ALB) will handle the load distribution. The architecture needs to support distributed session data management. The company is willing to make changes to code if needed. What should the solutions architect do to ensure that the architecture supports distributed session data management?

<details><summary>Answer</summary>

**A. Use Amazon ElastiCache to manage and store session data.**

Amazon ElastiCache is a fully managed, in-memory data store service. It is commonly used for caching and session management in distributed applications. By utilizing ElastiCache for session data management, you can store and retrieve session data in a scalable and high-performance manner. The use of ElastiCache allows for a distributed and shared data store for session management across multiple instances and Availability Zones.

</details>

### 68. dt-214

What is the minimum charge for the data transferred between Amazon RDS and Amazon EC2 Instances in the same Availability Zone?

<details><summary>Answer</summary>

**B. No charge. It is free.**

</details>

### 69. dt-219

[...] let you categorize your EC2 resources in different ways, for example, by purpose, owner, or environment.

<details><summary>Answer</summary>

**C. tags.**

</details>

### 70. dt-220

Which of the below mentioned options is not available when an instance is launched by Auto Scaling with EC2 Classic?

<details><summary>Answer</summary>

**B. Elastic IP.**

</details>

### 71. q-220 `cost`

A solutions architect is designing a new API using Amazon API Gateway that will receive requests from users. The volume of requests is highly variable; several hours can pass without receiving a single request. The data processing will take place asynchronously, but should be completed within a few seconds after a request is made. Which compute service should the solutions architect have the API invoke to deliver the requirements at the lowest cost?

<details><summary>Answer</summary>

**B. An AWS Lambda function**

AWS Lambda supports asynchronous invocation, which is suitable for scenarios where data processing can take place independently of the API request and complete within a few seconds. This aligns with the requirement of processing data asynchronously.

</details>

### 72. dt-228

Which services allow the customer to retain full administrative privileges of the underlying EC2 instances? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Amazon Elastic MapReduce.; E. AWS Elastic Beanstalk.**

</details>

### 73. q-229

A company hosts dozens of multi-tier applications on AWS. The presentation layer and logic layer are comprised of Amazon EC2 Linux instances that use Amazon Elastic Block Store (Amazon EBS) volumes. The company needs a solution to ensure that operating system vulnerabilities are not introduced to the EC2 instances when the company deploys new features. The company uses custom AMIs to deploy the EC2 instances in an Auto Scaling group. The solution must scale to handle all applications that the company hosts. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use EC2 Image Builder to create new AMIs when the company deploys new features. Include the update-linux component in the build components of the new AMIs. Use the existing Auto Scaling group to deploy the new AMIs.**

EC2 Image Builder is a fully managed AWS service designed to automate the creation, management, and deployment of customized, secure, and up-to-date server images. The service allows for the creation of an automated pipeline that produces new Amazon Machine Images (AMIs). By including the AWS-managed update-linux component in the image recipe, the pipeline will automatically apply all available operating system updates during the build process. This ensures that any new AMI created for feature deployment is patched against known vulnerabilities. The resulting patched AMI can then be used to update the launch template for the Auto Scaling group, providing a scalable and repeatable solution for maintaining security. Why Incorrect Options are Wrong: A. Amazon Inspector is a vulnerability assessment service that scans for vulnerabilities; it does not patch or remediate them. B. This describe

</details>

### 74. dt-238

The one-time payment for Reserved Instances is [...] refundable if the reservation is cancelled.

<details><summary>Answer</summary>

**C. never.**

</details>

### 75. dt-239

Is it possible to get a history of all EC2 API calls made on your account for security analysis and operational troubleshooting purposes?

<details><summary>Answer</summary>

**B. Yes, you should turn on the CloudTrail in the AWS console.**

</details>

### 76. dt-243

What are the Amazon EC2 API tools?

<details><summary>Answer</summary>

**B. Command-line tools to the Amazon EC2 web service.**

</details>

### 77. q-245 `cost`

A company is launching an application on AWS. The application uses an Application Load Balancer (ALB) to direct traffic to at least two Amazon EC2 instances in a single target group. The instances are in an Auto Scaling group for each environment. The company requires a development environment and a production environment. The production environment will have periods of high traffic. Which solution will configure the development environment MOST cost-effectively?

<details><summary>Answer</summary>

**Reduce the maximum number of EC2 instances in the development environment's Auto Scaling group.**

Development and production each have their own Auto Scaling group, and only production sees bursts of traffic. Capping the maximum size of the development group stops it from ever scaling out to a production-sized fleet, so development runs the minimum it needs and nothing more. Taking a target out of the development target group saves nothing, because the instance keeps running and billing - the Auto Scaling group still owns it and will simply register it again - and it also contradicts the requirement that the load balancer serve at least two instances. Shrinking instance sizes in both environments would change production as well, and the load balancing algorithm has no bearing on cost.

</details>

### 78. dt-248

Which of the following cannot be used in Amazon EC2 to control who has access to specific Amazon EC2 instances?

<details><summary>Answer</summary>

**B. IAM System.**

</details>

### 79. gh-248

Users report that some submitted data is not being processed Amazon CloudWatch reveals that the EC2 instances have a consistent CPU utilization at or near 100%. The company wants to improve system performance and scale the system based on user load.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Route incoming requests to Amazon Simple Queue Service (Amazon SQS). Configure an EC2 Auto Scaling group based on queue size. Update the software to read from the queue.**

This option addresses the issue by offloading incoming requests to an SQS queue, allowing for decoupling of processing and scaling based on queue size. This helps improve system performance and allows for scaling based on user load.

</details>

### 80. q-252

A company has an application that runs on Amazon EC2 instances in an Auto Scaling group. The application uses hardcoded credentials to access an Amazon RDS database. To comply with new regulations, the company needs to automatically rotate the database password for the application service account every 90 days. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a secret for the database credentials in AWS Secrets Manager. Enable rotation every 90 days. Modify the application to retrieve credentials from Secrets Manager.**

The most secure and efficient way to manage and automatically rotate database credentials is by using AWS Secrets Manager. This service is purpose-built for this scenario. By storing the credentials as a secret in Secrets Manager and enabling automatic rotation, the company can meet the 90-day rotation policy without manual intervention. The application code must be modified to retrieve the credentials from Secrets Manager using the AWS SDK, which eliminates hardcoded credentials and improves the application's security posture. This is the standard, best-practice solution. Why Incorrect Options are Wrong: A. This is a complex, custom solution that requires managing SSH access to instances and is less secure and reliable than using a managed AWS service. C. Using an Amazon ECS task is another custom, overly complex solution for a problem that AWS Secrets Manager is designed to solve nativ

</details>

### 81. dt-254 `availability`

You have a web application running on six Amazon EC2 instances, consuming about 45% of resources on each instance. You are using auto-scaling to make sure that six instances are running at all times. The number of requests this application processes is consistent and does not experience spikes. The application is critical to your business and you want high availability at all times. You want the load to be distributed evenly between all instances. You also want to use the same Amazon Machine Image (AMI) for all instances. Which of the following architectural choices should you make?

<details><summary>Answer</summary>

**C. Deploy 3 EC2 instances in one Availability Zone and 3 in another Availability Zone and use Amazon Elastic Load Balancer.**

</details>

### 82. dt-257

Amazon EC2 provides a repository of public data sets that can be seamlessly integrated into AWS cloud-based applications. What is the monthly charge for using the public data sets?

<details><summary>Answer</summary>

**D. There is no charge for using the public data sets.**

</details>

### 83. dt-261

You have set up an Auto Scaling group. The cool down period for the Auto Scaling group is 7 minutes. The first instance is launched after 3 minutes, while the second instance is launched after 4 minutes. How many minutes after the first instance is launched will Auto Scaling accept another scaling activity request?

<details><summary>Answer</summary>

**A. 11 minutes.**

</details>

### 84. q-261

A company recently announced the deployment of its retail website to a global audience. The website runs on multiple Amazon EC2 instances behind an Elastic Load Balancer. The instances run in an Auto Scaling group across multiple Availability Zones. The company wants to provide its customers with different versions of content based on the devices that the customers use to access the website. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Configure Amazon CloudFront to cache multiple versions of the content.**

C. Configure a Lambda@Edge function to send specific objects to users based on the User-Agent header.  Amazon CloudFront is a content delivery network (CDN) service that can cache and deliver content globally. Configure CloudFront to cache different versions of content based on the device type or other criteria.  Lambda@Edge allows you to run code in response to CloudFront events globally. Use a Lambda@Edge function to inspect the User-Agent header and dynamically serve different versions of content based on the device type.

</details>

### 85. q-263

A company is building an application that consists of several microservices. The company has decided to use container technologies to deploy its software on AWS. The company needs a solution that minimizes the amount of ongoing effort for maintenance and scaling. The company cannot manage additional infrastructure. Which combination of actions should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Deploy an Amazon Elastic Container Service (Amazon ECS) cluster.**

D. Deploy an Amazon Elastic Container Service (Amazon ECS) service with a Fargate launch type. Specify a desired task number level of greater than or equal to 2.  An ECS cluster is necessary to organize and manage your Fargate tasks and services. It provides a logical grouping of tasks and services. When using Fargate, you don't need to manage the underlying EC2 instances; the cluster helps manage the Fargate tasks.  Fargate is a serverless compute engine for containers that eliminates the need to manage underlying infrastructure. With Fargate, you do not need to provision or manage EC2 instances; AWS takes care of the infrastructure, allowing you to focus solely on your containers.

</details>

### 86. dt-264

Your system recently experienced down time during the troubleshooting process. You found that a new administrator mistakenly terminated several production EC2 instances. Which of the following strategies will help prevent a similar situation in the future? The administrator still must be able to: Launch, start stop, and terminate development resources. Launch and start production instances.

<details><summary>Answer</summary>

**B. Leverage resource based tagging along with an IAM user, which can prevent specific users from terminating production EC2 resources.**

</details>

### 87. q-266

A company has a popular gaming platform running on AWS. The application is sensitive to latency because latency can impact the user experience and introduce unfair advantages to some players. The application is deployed in every AWS Region. It runs on Amazon EC2 instances that are part of Auto Scaling groups configured behind Application Load Balancers (ALBs). A solutions architect needs to implement a mechanism to monitor the health of the application and redirect traffic to healthy endpoints. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Configure an accelerator in AWS Global Accelerator. Add a listener for the port that the application listens on, and attach it to a Regional endpoint in each Region. Add the ALB as the endpoint.**

AWS Global Accelerator is designed to provide static IP addresses for global applications and direct traffic over the AWS global network to optimal AWS endpoints based on health, geography, and routing policies. Configure an accelerator with a listener for the port that the application listens on. Attach the listener to a Regional endpoint in each AWS Region where the application is deployed.

</details>

### 88. dt-268

You have a periodic Image analysis application that gets some files in input, analyzes them and for each file writes some data in output to a text file. The number of files in input per day is high and concentrated in a few hours of the day. Currently you have a server on EC2 with a large EBS volume that hosts the input data and the results. It takes almost 20 hours per day to complete the process. What services could be used to reduce the elaboration time and improve the availability of the solution?

<details><summary>Answer</summary>

**D. EBS with Provisioned IOPS (PIOPS) to store I/O files. SQS to distribute elaboration commands to a group of hosts working in parallel. Auto Scaling to dynamically size the group of hosts depending on the length of the SQS queue.**

</details>

### 89. dt-269

While controlling access to Amazon EC2 resources, which of the following acts as a firewall that controls the traffic allowed to reach one or more instances?

<details><summary>Answer</summary>

**A. A security group.**

</details>

### 90. q-271

A company regularly receives route status updates from its delivery trucks as events in Amazon EventBridge. The company is building an API-based application in a VPC that will consume and process the events to create a delivery status dashboard. The API application must not be available by using public IP addresses because of security and compliance requirements. How should the company send events from EventBridge to the API application?

<details><summary>Answer</summary>

**A. Create an AWS Lambda function that runs in the same VPC as the API application. Configure the function as an EventBridge target. Use the function to send events to the API.**

The API application must not have a public IP address. Amazon EventBridge can target an AWS Lambda function. By placing this Lambda function within the same VPC as the API application, the function can communicate with the application using private IP addresses. This pattern uses the Lambda function as a secure proxy, receiving events from EventBridge and forwarding them to the private API endpoint without exposing the application to the internet. This is a standard and secure architecture for this use case. Why Incorrect Options are Wrong: B. An internet-facing ALB has a public endpoint, which directly violates the requirement that the application must not be available via public IP addresses. C. An internet-facing NLB also has a public endpoint, which violates the security and compliance requirement of having no public accessibility. D. EventBridge cannot directly send events to a priv

</details>

### 91. dt-271

While using the EC2 GET requests as URLs, the [...] is the URL that serves as the entry point for the web service.

<details><summary>Answer</summary>

**B. endpoint.**

</details>

### 92. q-271

A solutions architect observes that a nightly batch processing job is automatically scaled up for 1 hour before the desired Amazon EC2 capacity is reached. The peak capacity is the ‘same every night and the batch jobs always start at 1 AM. The solutions architect needs to find a cost-effective solution that will allow for the desired EC2 capacity to be reached quickly and allow the Auto Scaling group to scale down after the batch jobs are complete. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Configure scheduled scaling to scale up to the desired compute level.**

Scheduled scaling allows you to define specific times when your Auto Scaling group's desired capacity should be increased or decreased. In this case, you can schedule the scaling action to increase the capacity just before the nightly batch processing job starts at 1 AM and then scale it down after the job completes.

</details>

### 93. dt-274

A user has launched 10 EC2 instances inside a placement group. Which of the below mentioned statements is true with respect to the placement group?

<details><summary>Answer</summary>

**A. All instances must be in the same AZ.**

</details>

### 94. dt-275

A user has created a CloudFormation stack. The stack creates AWS services, such as EC2 instances, ELB, AutoScaling, and RDS. While creating the stack it created EC2, ELB and AutoScaling but failed to create RDS. What will CloudFormation do in this scenario?

<details><summary>Answer</summary>

**A. Rollback all the changes and terminate all the created services.**

</details>

### 95. q-275

A company runs an internal browser-based application. The application runs on Amazon EC2 instances behind an Application Load Balancer. The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. The Auto Scaling group scales up to 20 instances during work hours, but scales down to 2 instances overnight. Staff are complaining that the application is very slow when the day begins, although it runs well by mid-morning. How should the scaling be changed to address the staff complaints and keep costs to a minimum?

<details><summary>Answer</summary>

**C. Implement a target tracking action triggered at a lower CPU threshold, and decrease the cooldown period.**

</details>

### 96. dt-276

You have been asked to design the storage layer for an application. The application requires disk performance of at least 100,000 IOPS. In addition, the storage layer must be able to survive the loss of an individual disk, EC2 instance, or Availability Zone without any data loss. The volume you provide must have a capacity of at least 3 TB. Which of the following designs will meet these objectives?

<details><summary>Answer</summary>

**E. Instantiate an i2.8xlarge instance in us-east-1a. Create a RAID 0 volume using the four 800GB SSD ephemeral disks provided with the instance. Configure synchronous, block-level replication to an identically configured instance in us-east-1b.**

</details>

### 97. q-276

A company has a multi-tier application deployed on several Amazon EC2 instances in an Auto Scaling group. An Amazon RDS for Oracle instance is the application’ s data layer that uses Oracle-specific PL/SQL functions. Traffic to the application has been steadily increasing. This is causing the EC2 instances to become overloaded and the RDS instance to run out of storage. The Auto Scaling group does not have any scaling metrics and defines the minimum healthy instance count only. The company predicts that traffic will continue to increase at a steady but unpredictable rate before leveling off. What should a solutions architect do to ensure the system can automatically scale for the increased traffic? (Choose two.)

<details><summary>Answer</summary>

**A. Configure storage Auto Scaling on the RDS for Oracle instance.**

This option allows the RDS instance to automatically scale its storage based on the actual storage usage, ensuring that you don't run out of storage.  D. Configure the Auto Scaling group to use the average CPU as the scaling metric.  By using CPU utilization as a scaling metric, the Auto Scaling group can dynamically adjust the number of EC2 instances based on the application's demand. This helps in handling increased traffic and preventing overload on existing instances.

</details>

### 98. dt-278

Your startup wants to implement an order fulfillment process for selling a personalized gadget that needs an average of 3-4 days to produce with some orders taking up to 6 months. You expect 10 orders per day on your first day, 1000 orders per day after 6 months and 10,000 orders after 12 months. Orders coming in are checked for consistency, then dispatched to your manufacturing plant for production, quality control, packaging, shipment and payment processing. If the product does not meet the quality standards at any stage of the process, employees may force the process to repeat a step. Customers are notified via email about order status and any critical issues with their orders such as payment failure. Your base architecture includes AWS Elastic Beanstalk for your website with an RDS MySQL instance for customer data and orders. How can you implement the order fulfillment process while making sure that the emails are delivered reliably?

<details><summary>Answer</summary>

**C. Use SWF with an Auto Scaling group of activity workers and a decider instance in another Auto Scaling group with min/max=1. Use SES to send emails to customers.**

</details>

### 99. dt-280

A user is accessing an EC2 instance on the SSH port for IP 10.20.30.40. Which one is a secure way to configure that the instance can be accessed only from this IP?

<details><summary>Answer</summary>

**B. In the security group, open port 22 for IP 10.20.30.40/32.**

</details>

### 100. dt-283

You have a content management system running on an Amazon EC2 instance that is approaching 100% CPU utilization. Which option will reduce load on the Amazon EC2 instance?

<details><summary>Answer</summary>

**B. Create a CloudFront distribution, and configure the Amazon EC2 instance as the origin.**

</details>

### 101. q-284

A company is designing an application to run in a VPC on AWS. The application consists of Amazon EC2 instances that run in private subnets as part of an Auto Scaling group. The application stores data in an Amazon RDS DB instance. The company attaches a security group named web-servers to the EC2 instances. The company attaches a security group named database to the DB instance. The company needs a solution to establish communication between the EC2 instances and the DB instance. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Configure the inbound rule of the database security group to allow access from the web-servers security group. Configure an outbound rule for the web-servers security group to allow access to the database security group.**

The most secure and scalable method for allowing communication between AWS resources within a VPC is to reference security groups. By configuring the database security group's inbound rule to allow traffic from the web-servers security group ID, you create a dynamic rule. This rule automatically permits traffic from any EC2 instance associated with the web-servers security group, even as instances are terminated and launched by the Auto Scaling group, causing their private IP addresses to change. Security groups are stateful, so an explicit outbound rule is often not needed if the default "allow all" outbound rule is in place, but specifying it ensures connectivity. Why Incorrect Options are Wrong: A. Using IP addresses is not scalable because instances in an Auto Scaling group have dynamic IPs that change as instances are launched or terminated. C. An Auto Scaling group ID cannot be use

</details>

### 102. dt-286

You have decided to change the instance type for instances running in your application tier that is using Auto Scaling. In which area below would you change the instance type definition?

<details><summary>Answer</summary>

**D. Auto Scaling launch configuration.**

</details>

### 103. dt-287

Which of the following statements is true of creating a launch configuration using an EC2 instance?

<details><summary>Answer</summary>

**B. Auto Scaling automatically creates a launch configuration directly from an EC2 instance.**

</details>

### 104. q-287

A company wants to migrate a Windows-based application from on premises to the AWS Cloud. The application has three tiers: an application tier, a business tier, and a database tier with Microsoft SQL Server. The company wants to use specific features of SQL Server such as native backups and Data Quality Services. The company also needs to share files for processing between the tiers. How should a solutions architect design the architecture to meet these requirements?

<details><summary>Answer</summary>

**B. Host all three tiers on Amazon EC2 instances. Use Amazon FSx for Windows File Server for file sharing between the tiers.**

hosting all three tiers on Amazon EC2 instances allows you to have flexibility and control over the entire application architecture. To address the file-sharing requirement between the tiers, you can use Amazon FSx for Windows File Server.  Amazon FSx for Windows File Server is a fully managed Windows file system that is accessible from Windows-based instances over the Server Message Block (SMB) protocol. It supports the specific features of Windows File Server, including features like native backups and access to Windows-specific services.

</details>

### 105. q-290

A company is deploying a new SFTP service. The service consists of Amazon EC2 instances in an Auto Scaling group that spans two Availability Zones and a shared Amazon EFS file system. The service is behind a Network Load Balancer NLB that has a security group attached. A solutions architect needs to grant a list of IP addresses access to the new service. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Add an inbound rule to the NLB security group that allows TCP Port 22 traffic from the IP addresses. Add an inbound rule to the security group referenced by the Auto Scaling group that allows TCP Port 22 traffic from the NLB security group.**

This solution correctly implements a layered security approach using the principle of least privilege. The first layer is the Network Load Balancer's (NLB) security group, which acts as the perimeter defense, allowing SFTP traffic (TCP port 22) only from the specified list of IP addresses. The second layer is the EC2 instances' security group, which allows traffic on TCP port 22 only from the NLB's security group. This ensures that traffic must originate from an approved IP and pass through the NLB to reach the instances, providing a secure and well-architected configuration. Why Incorrect Options are Wrong: A. Network ACLs are less precise than security groups for this use case and require managing complex stateless rules for ephemeral ports. C. Allowing all traffic from the NLB to the EC2 instances is overly permissive and violates the principle of least privilege. Only port 22 is requ

</details>

### 106. q-290

A company hosts a web application on multiple Amazon EC2 instances. The EC2 instances are in an Auto Scaling group that scales in response to user demand. The company wants to optimize cost savings without making a long-term commitment. Which EC2 instance purchasing option should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. A mix of On-Demand Instances and Spot Instances**

On-Demand Instances: These instances are charged per hour or per second of usage, without any upfront payment or long-term commitment. While they offer flexibility, they are usually more expensive compared to other purchasing options.  Spot Instances: These are spare compute capacity in the AWS cloud available at a lower price compared to On-Demand Instances. However, they can be terminated by AWS with little notice if the capacity is needed elsewhere. Spot Instances are suitable for workloads that are fault-tolerant and can handle interruptions.

</details>

### 107. dt-293

A user has launched 10 EC2 instances inside a placement group. Which of the following statements is true in regards to what ability launching your instances into a VPC instead of EC2-Classic gives you?

<details><summary>Answer</summary>

**A. All of the things listed here.**

</details>

### 108. dt-295

What is the average IOPS that the user will get for most of the year as per EC2 SLA if the instance is attached to the EBS optimized instance?

<details><summary>Answer</summary>

**D. 900.**

</details>

### 109. gh-297

A solutions architect needs to implement a solution to automate the scalability of the application. The solution must optimize the cost of the architecture and must ensure that the application has enough CPU resources when surges occur.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an EC2 Auto Scaling group. Select the existing ALB as the load balancer and the existing target group as the target group. Set a target tracking scaling policy that is based on the ASGAverageCPUUtilization metric. Set the minimum instances to 2, the desired capacity to 3, the maximum instances to 6, and the target value to 50%. Add the EC2 instances to the Auto Scaling group.**

Option B utilizes EC2 Auto Scaling, which automatically adjusts the number of EC2 instances in the Auto Scaling group based on the specified target tracking scaling policy.
By setting a target tracking scaling policy based on the ASGAverageCPUUtilization metric with a target value of 50%, the Auto Scaling group will dynamically adjust the number of instances to maintain an average CPU utilization close to the target value.
This solution provides scalability when needed, ensures that there are enough CPU resources during surges, and optimizes costs by automatically adjusting the capacity based on demand.

</details>

### 110. dt-299

Please select the Amazon EC2 resource which can be tagged.

<details><summary>Answer</summary>

**C. Placement groups.**

</details>

### 111. q-300 `cost`

A company needs to migrate a legacy application from an on-premises data center to the AWS Cloud because of hardware capacity constraints. The application runs 24 hours a day, 7 days a week. The application’s database storage continues to grow over time. What should a solutions architect do to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Migrate the application layer to Amazon EC2 Reserved Instances. Migrate the data storage layer to Amazon Aurora Reserved Instances.**

Using Amazon EC2 Reserved Instances for the application layer provides cost savings compared to On-Demand Instances while ensuring availability for the 24/7 runtime. Migrating the data storage layer to Amazon Aurora Reserved Instances provides a fully managed relational database service with automatic scaling capabilities. Amazon Aurora is designed for high performance and cost efficiency. Reserved Instances provide cost savings compared to On-Demand Instances over an extended period, making them suitable for applications with continuous operation. Amazon Aurora, being a fully managed service, offloads much of the operational overhead associated with managing a traditional database, making it a cost-effective choice for growing database storage.

</details>

### 112. q-303

A company is launching a new application deployed on an Amazon Elastic Container Service (Amazon ECS) cluster and is using the Fargate launch type for ECS tasks. The company is monitoring CPU and memory usage because it is expecting high traffic to the application upon its launch. However, the company wants to reduce costs when utilization decreases. What should a solutions architect recommend?

<details><summary>Answer</summary>

**D. Use AWS Application Auto Scaling with target tracking policies to scale when ECS metric breaches trigger an Amazon CloudWatch alarm.**

AWS Application Auto Scaling is a service that can automatically adjust the number of running ECS tasks or services based on specified CloudWatch metrics. Target tracking policies allow you to set a target value for a specific metric, and AWS Application Auto Scaling automatically adjusts the desired task count to maintain the target. By using target tracking policies, you can ensure that the ECS cluster scales up or down based on the application's demand while maintaining a balance between cost efficiency and performance.

</details>

### 113. q-306

A company wants to run an in-memory database for a latency-sensitive application that runs on Amazon EC2 instances. The application processes more than 100,000 transactions each minute and requires high network throughput. A solutions architect needs to provide a cost- effective network design that minimizes data transfer charges. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Launch all EC2 instances in the same Availability Zone within the same AWS Region. Specify a placement group with cluster strategy when launching EC2 instances.**

A placement group is a logical grouping of instances within a single Availability Zone. The "cluster" strategy for placement groups places instances in close proximity to each other, providing low-latency, high-throughput communication between instances. By launching all EC2 instances in the same Availability Zone within the same AWS Region, you minimize data transfer charges because data transfer within the same Availability Zone is not subject to additional costs.

</details>

### 114. dt-307

If you want to launch Amazon Elastic Compute Cloud (EC2) instances and assign each instance a predetermined private IP address you should:

<details><summary>Answer</summary>

**B. Assign a group of sequential Elastic IP address to the instances.**

</details>

### 115. dt-309

You have a Business support plan with AWS. One of your EC2 instances is running Microsoft Windows Server 2008 R2 and you are having problems with the software. Can you receive support from AWS for this software?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 116. dt-314

The [...] service is targeted at organizations with multiple users or systems that use AWS products such as Amazon EC2, Amazon SimpleDB, and the AWS Management Console.

<details><summary>Answer</summary>

**C. AWS Identity and Access Management.**

</details>

### 117. q-315 `security`

A company has a prototype application that runs in a Linux container on Amazon ECS. The company needs to provide sensitive environment variables to the container before the application starts. What is the MOST secure way to load the environment variables into the running container?

<details><summary>Answer</summary>

**D. Add the environment variables to AWS Systems Manager Parameter Store. Update the task execution role to include the ssm:GetParameters permission.**

The most secure method to manage sensitive data for Amazon ECS containers is to use a dedicated secrets management service like AWS Systems Manager Parameter Store or AWS Secrets Manager. By storing the environment variables as SecureString parameters in Parameter Store, the data is encrypted at rest. The ECS task definition can then reference these parameters. At launch, the ECS agent uses the permissions granted to the task execution IAM role (specifically ssm:GetParameters) to securely fetch the decrypted values and inject them as environment variables into the container. This approach avoids hardcoding secrets in task definitions, container images, or source code, and provides centralized, auditable, and granular access control via IAM. Why Incorrect Options are Wrong: A. Storing secrets in task definitions and checking them into Git exposes sensitive data in plaintext, which is a se

</details>

### 118. q-317

A company serves its website by using an Auto Scaling group of Amazon EC2 instances in a single AWS Region. The website does not require a database The company is expanding, and the company's engineering team deploys the website to a second Region. The company wants to distribute traffic across both Regions to accommodate growth and for disaster recovery purposes The solution should not serve traffic from a Region in which the website is unhealthy. Which policy or resource should the company use to meet these requirements?

<details><summary>Answer</summary>

**B. An Amazon Route 53 multivalue answer routing policy**

Amazon Route 53 is the appropriate service for directing traffic to multiple AWS Regions. The multivalue answer routing policy allows Route 53 to respond to DNS queries with up to eight healthy records selected at random. By creating a record for the endpoint in each Region (e.g., the regional Application Load Balancer) and associating a Route 53 health check with each record, the requirements are met. This configuration distributes traffic across both Regions. If the health check for one Region fails, Route 53 will stop returning that Region's record in DNS responses, effectively routing traffic away from the unhealthy endpoint and providing disaster recovery. Why Incorrect Options are Wrong: A. A simple routing policy routes traffic to a single resource. While you can specify multiple values, it does not perform health checks to remove unhealthy endpoints from responses. C. An Applicat

</details>

### 119. dt-317

You have written a CloudFormation template that creates 1 Elastic Load Balancer fronting 2 EC2 Instances. Which section of the template should you edit so that the DNS of the load balancer is returned upon creation of the stack?

<details><summary>Answer</summary>

**B. Outputs.**

</details>

### 120. dt-318

AWS CloudFormation is a service that helps you model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and AWS CloudFormation takes care of provisioning and configuring those resources for you. What formatting is required for this template?

<details><summary>Answer</summary>

**A. JSON-formatted document.**

</details>

### 121. q-318

A company recently migrated its entire IT environment to the AWS Cloud. The company discovers that users are provisioning oversized Amazon EC2 instances and modifying security group rules without using the appropriate change control process. A solutions architect must devise a strategy to track and audit these inventory and configuration changes. Which actions should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Enable AWS CloudTrail and use it for auditing.**

D. Enable AWS Config and create rules for auditing and compliance purposes.  A. Enable AWS CloudTrail and use it for auditing. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS Command Line Interface (CLI), and AWS SDKs and APIs. By enabling CloudTrail, the company can track user activity and changes to AWS resources, and monitor compliance with internal policies and external regulations.  D. Enable AWS Config and create rules for auditing and compliance purposes. AWS Config provides a detailed inventory of the AWS resources in your account, and continuously records changes to the configurations of those resources. By creating rules in AWS Config, the company can automate the evaluation of resource configurations against desired state, and receive alerts when configurations drift from compliance.

</details>

### 122. dt-320

After setting up an EC2 security group with a cluster of 20 EC2 instances, you find an error in the security group settings. You quickly make changes to the security group settings. When will the changes to the settings be effective?

<details><summary>Answer</summary>

**A. The settings will be effective immediately for all the instances in the security group.**

</details>

### 123. q-320

A company is using a fleet of Amazon EC2 instances to ingest data from on-premises data sources. The data is in JSON format and ingestion rates can be as high as 1 MB/s. When an EC2 instance is rebooted, the data in-flight is lost. The company’s data science team wants to query ingested data in near-real time. Which solution provides near-real-time data querying that is scalable with minimal data loss?

<details><summary>Answer</summary>

**Publish the data to Amazon Kinesis Data Streams, and query the stream in near real time with Amazon Managed Service for Apache Flink (the service previously called Kinesis Data Analytics).**

Kinesis Data Streams accepts the 1 MB/s feed and holds every record durably across three Availability Zones for a retention period you choose, so a reboot of the producing EC2 instance no longer loses in-flight data, and throughput grows by adding shards. Amazon Managed Service for Apache Flink reads directly from the stream and runs continuous queries, which gives the data science team results seconds behind the source; SQL is still available through Flink SQL and Studio notebooks. Writing the feed to Amazon S3 with Firehose and querying it with Athena would work but adds minutes of buffering delay, which is not near real time.

</details>

### 124. dt-321

Can a user get a notification of each instance start / terminate configured with Auto Scaling?

<details><summary>Answer</summary>

**C. Yes, if configured with the Auto Scaling group.**

</details>

### 125. dt-326

In an experiment, if the minimum size for an Auto Scaling group is 1 instance, which of the following statements holds true when you terminate the running instance?

<details><summary>Answer</summary>

**A. Auto Scaling must launch a new instance to replace it.**

</details>

### 126. q-328

A company is hosting a three-tier ecommerce application in the AWS Cloud. The company hosts the website on Amazon S3 and integrates the website with an API that handles sales requests. The company hosts the API on three Amazon EC2 instances behind an Application Load Balancer (ALB). The API consists of static and dynamic front-end content along with backend workers that process sales requests asynchronously. The company is expecting a significant and sudden increase in the number of sales requests during events for the launch of new products. What should a solutions architect recommend to ensure that all the requests are processed successfully?

<details><summary>Answer</summary>

**B. Add an Amazon CloudFront distribution for the static content. Place the EC2 instances in an Auto Scaling group to launch new instances based on network traffic.**

Amazon CloudFront for Static Content: By using CloudFront, you can distribute static content (like images, stylesheets) globally, reducing latency for end-users and offloading some of the traffic from your backend instances.  Auto Scaling Group: An Auto Scaling group allows you to automatically adjust the number of EC2 instances to handle changes in demand. By placing the EC2 instances in an Auto Scaling group, you can dynamically scale the number of instances based on network traffic, ensuring that the application can handle increased load during events.

</details>

### 127. dt-331 `cost`

You have a distributed application that periodically processes large volumes of data across multiple Amazon EC2 Instances. The application is designed to recover gracefully from Amazon EC2 instance failures. You are required to accomplish this task in the most cost-effective way. Which of the following will meet your requirements?

<details><summary>Answer</summary>

**A. Spot Instances.**

</details>

### 128. q-333

A company’s application runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instances run in an Amazon EC2 Auto Scaling group across multiple Availability Zones. On the first day of every month at midnight, the application becomes much slower when the month-end financial calculation batch runs. This causes the CPU utilization of the EC2 instances to immediately peak to 100%, which disrupts the application. What should a solutions architect recommend to ensure the application is able to handle the workload and avoid downtime?

<details><summary>Answer</summary>

**C. Configure an EC2 Auto Scaling scheduled scaling policy based on the monthly schedule.**

By configuring a scheduled scaling policy, the EC2 Auto Scaling group can proactively launch additional EC2 instances before the CPU utilization peaks to 100%. This will ensure that the application can handle the workload during the month-end financial calculation batch, and avoid any disruption or downtime.  Configuring a simple scaling policy based on CPU utilization or adding Amazon CloudFront distribution or Amazon ElastiCache will not directly address the issue of handling the monthly peak workload.

</details>

### 129. q-335

A company is experiencing sudden increases in demand. The company needs to provision large Amazon EC2 instances from an Amazon Machine Image (AMI). The instances will run in an Auto Scaling group. The company needs a solution that provides minimum initialization latency to meet the demand. Which solution meets these requirements?

<details><summary>Answer</summary>

**B. Enable Amazon Elastic Block Store (Amazon EBS) fast snapshot restore on a snapshot. Provision an AMI by using the snapshot. Replace the AMI in the Auto Scaling group with the new AMI.**

Amazon EBS Fast Snapshot Restore: Enabling fast snapshot restore allows you to provision Amazon EBS volumes based on snapshots with faster performance. This is particularly useful when creating AMIs from snapshots, as it reduces the time it takes to create EBS volumes from those snapshots.  Minimum Initialization Latency: Fast snapshot restore helps in minimizing initialization latency as it provides a way to quickly create EBS volumes from snapshots.  Provisioning AMI from Snapshot: You can create an Amazon Machine Image (AMI) from an Amazon EBS snapshot. This allows you to capture a point-in-time snapshot of the file system, and then use that snapshot to create new instances.

</details>

### 130. q-340 `availability`

A company is developing a containerized web application that needs to be highly available and scalable. The application requires access to GPU resources.

<details><summary>Answer</summary>

**D. Run the application on Amazon EC2 instances from a GPU instance family by using Amazon Elastic Container Service (Amazon ECS) for orchestration.**

The most effective solution is to use Amazon Elastic Container Service (Amazon ECS) with the EC2 launch type. This approach allows for the creation of an ECS cluster using EC2 instances from a GPU-optimized instance family (e.g., P-series, G-series). ECS provides the necessary container orchestration for high availability and scalability by managing the placement and lifecycle of container tasks. By launching these tasks on a cluster of GPU-enabled EC2 instances, the application gains the required access to GPU resources for its workloads. Why Incorrect Options are Wrong: A. AWS Lambda does not natively support GPU acceleration, making it unsuitable for applications that require direct access to GPU hardware. B. AWS Fargate, the serverless compute engine for containers, does not currently support GPU-equipped instances. It is designed for general-purpose workloads. C. Amazon Elastic Cont

</details>

### 131. q-342

A company has an application that runs only on Amazon EC2 Spot Instances. The instances run in an Amazon EC2 Auto Scaling group with scheduled scaling actions. However, the capacity does not always increase at the scheduled times, and instances terminate many times a day. A solutions architect must ensure that the instances launch on time and have fewer interruptions. Which action will meet these requirements?

<details><summary>Answer</summary>

**A. Specify the capacity-optimized allocation strategy for Spot Instances. Add more instance types to the Auto Scaling group.**

The capacity-optimized allocation strategy is designed to fulfill Spot Instance requests from pools with the most available capacity, which directly addresses the problem of instances failing to launch on schedule. This strategy also inherently lowers the chance of interruption because it sources instances from the deepest capacity pools. Combining this with adding more instance types to the Auto Scaling group configuration further improves reliability. By diversifying the instance types, the Auto Scaling group has more potential Spot capacity pools to choose from, significantly increasing the probability of acquiring and maintaining the desired capacity. Why Incorrect Options are Wrong B. Increasing the instance size does not provide the same benefit as diversifying instance types. It limits the number of available pools and may not improve capacity acquisition. C. The lowest-price allo

</details>

### 132. q-342 `least-ops`

A transaction processing company has weekly scripted batch jobs that run on Amazon EC2 instances. The EC2 instances are in an Auto Scaling group. The number of transactions can vary, but the baseline CPU utilization that is noted on each run is at least 60%. The company needs to provision the capacity 30 minutes before the jobs run. Currently, engineers complete this task by manually modifying the Auto Scaling group parameters. The company does not have the resources to analyze the required capacity trends for the Auto Scaling group counts. The company needs an automated way to modify the Auto Scaling group’s desired capacity. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create a predictive scaling policy for the Auto Scaling group. Configure the policy to scale based on forecast. Set the scaling metric to CPU utilization. Set the target value for the metric to 60%. In the policy, set the instances to pre-launch 30 minutes before the jobs run.**

In general, if you have regular patterns of traffic increases and applications that take a long time to initialize, you should consider using predictive scaling. Predictive scaling can help you scale faster by launching capacity in advance of forecasted load, compared to using only dynamic scaling, which is reactive in nature.

</details>

### 133. dt-343

In Amazon RDS, security groups are ideally used to:

<details><summary>Answer</summary>

**D. Control what IP addresses or EC2 instances can connect to your databases on a DB instance.**

</details>

### 134. dt-344

How long does an AWS free usage tier EC2 last for?

<details><summary>Answer</summary>

**B. 12 Months upon signup.**

</details>

### 135. dt-346

You can seamlessly join an EC2 instance to your directory domain. What connectivity do you need to be able to connect remotely to this instance?

<details><summary>Answer</summary>

**A. You must have IP connectivity to the instance from the network you are connecting from.**

</details>

### 136. dt-348 `performance`

You have multiple Amazon EC2 instances running in a cluster across multiple Availability Zones within the same region. What combination of the following should be used to ensure the highest network performance (packets per second), lowest latency, and lowest jitter? (Choose 3 answers)

<details><summary>Answer</summary>

**A. Amazon EC2 placement groups.; B. Enhanced networking.; D. Amazon HVM AMI.**

</details>

### 137. q-355

A company runs a critical public application on Amazon Elastic Kubernetes Service (Amazon EKS) clusters. The application has a microservices architecture. The company needs to implement a solution that collects, aggregates, and summarizes metrics and logs from the application in a centralized location. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**D. Configure Amazon CloudWatch Container Insights in the existing EKS cluster. Use a CloudWatch dashboard to view the metrics and logs.**

Amazon CloudWatch Container Insights is a purpose-built feature for monitoring, troubleshooting, and setting alarms for containerized applications on services like Amazon EKS. It automatically collects, aggregates, and summarizes metrics (such as CPU, memory, disk, and network utilization) and logs at various levels including cluster, node, pod, and service. It provides pre-built, automatic dashboards in the CloudWatch console, which visualizes this data. This turnkey solution is the most operationally efficient method as it minimizes configuration overhead and provides immediate, actionable insights specific to container environments, directly meeting all the requirements of the question. Why Incorrect Options are Wrong: A. The standard CloudWatch agent can collect logs and system-level metrics, but it requires significant manual configuration to gather container-specific performance me

</details>

### 138. q-355 `least-ops`

A company is migrating an old application to AWS. The application runs a batch job every hour and is CPU intensive. The batch job takes 15 minutes on average with an on-premises server. The server has 64 virtual CPU (vCPU) and 512 GiB of memory. Which solution will run the batch job within 15 minutes with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use AWS Batch on Amazon EC2.**

AWS Batch on Amazon EC2: AWS Batch is a fully managed service for batch computing that dynamically provisions the optimal quantity and type of compute resources (Amazon EC2 instances) based on the volume and specific resource requirements of the batch jobs. If the batch job is CPU-intensive and can be parallelized, AWS Batch can efficiently manage the compute resources needed for the job, and it provides a higher level of control over the environment compared to serverless options like AWS Lambda.

</details>

### 139. dt-357

You are configuring your company's application to use Auto Scaling and need to move user state information. Which of the following AWS services provides a shared data store with durability and low latency?

<details><summary>Answer</summary>

**B. Amazon Simple Storage Service.**

</details>

### 140. dt-360

You deployed your company website using Elastic Beanstalk and you enabled log file rotation to S3. An Elastic MapReduce job is periodically analyzing the logs on S3 to build a usage dashboard that you share with your CIO. You recently improved overall performance of the website using CloudFront for dynamic content delivery and your website as the origin. After this architectural change, the usage dashboard shows that the traffic on your website dropped by an order of magnitude. How do you fix your usage dashboard?

<details><summary>Answer</summary>

**A. Enable CloudFront to deliver access logs to S3 and use them as input of the Elastic MapReduce job.**

</details>

### 141. q-363

A company needs to design a resilient web application to process customer orders. The web application must automatically handle increases in web traffic and application usage without affecting the customer experience or losing customer orders. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use an Application Load Balancer to manage web traffic. Use Amazon EC2 Auto Scaling groups to receive and process customer orders. Use Amazon Simple Queue Service (Amazon SQS) to store unprocessed orders. Use Amazon RDS with a Multi-AZ deployment to store processed customer orders.**

This solution describes a classic, well-architected, and decoupled three-tier web application. An Application Load Balancer (ALB) is ideal for distributing HTTP/S web traffic. Amazon EC2 Auto Scaling groups allow the compute layer to scale in and out automatically based on traffic, ensuring a good customer experience. Amazon SQS provides a durable and highly available queue to buffer incoming orders, decoupling the web front-end from the back-end processing. This ensures that no orders are lost, even if the processing instances are temporarily unavailable or overwhelmed. Finally, an Amazon RDS Multi-AZ deployment provides a highly available and resilient database for storing processed orders. Why Incorrect Options are Wrong A: A NAT gateway is used for enabling outbound internet connectivity from private subnets, not for managing inbound web traffic. This is a fundamental misuse of the s

</details>

### 142. q-368

A company uses an Amazon EC2 instance to handle requests for a public web application. The application routes traffic to multiple application pages by using URL paths. The company begins to experience large surges of traffic at unpredictable times. The traffic surges cause the web application to experience issues and to occasionally become unavailable. The company needs to make the web application more scalable to handle sudden increases in traffic. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Create an Amazon Machine Image (AMI) of the web application instance. Use the AMI to create an Auto Scaling group of EC2 instances that has a minimum capacity of two. Create an Application Load Balancer. Set the Auto Scaling group as the target group.**

This solution directly addresses the core requirements of scalability and high availability for a web application. An Application Load Balancer (ALB) is designed to handle HTTP/HTTPS traffic and can perform path-based routing, which matches the application's needs. An Auto Scaling group (ASG) automatically adjusts the number of EC2 instances based on traffic demand, providing the necessary elasticity to handle unpredictable surges. By launching instances from a pre-configured Amazon Machine Image (AMI) and setting a minimum capacity of two, the architecture ensures both consistent application deployment and immediate high availability across multiple instances. Why Incorrect Options are Wrong: B: A Network Load Balancer (NLB) operates at Layer 4 (TCP/UDP) and is not ideal for the application's Layer 7 (HTTP) path-based routing requirement. An ALB is the correct choice. C: This is a manua

</details>

### 143. dt-368

An application hosted at the EC2 instance receives an HTTP request from ELB. The same request has an X-Forwarded-For header, which has three IP addresses. Which system's IP will be a part of this header?

<details><summary>Answer</summary>

**C. All of the answers listed here.**

</details>

### 144. q-369 `least-ops`

A company has migrated an application to Amazon EC2 Linux instances. One of these EC2 instances runs several 1-hour tasks on a schedule. These tasks were written by different teams and have no common programming language. The company is concerned about performance and scalability while these tasks run on a single instance. A solutions architect needs to implement a solution to resolve these concerns. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Batch to run the tasks as jobs. Schedule the jobs by using Amazon EventBridge (Amazon CloudWatch Events).**

AWS Batch: AWS Batch is a fully managed service for running batch computing workloads. It dynamically provisions the optimal quantity and type of compute resources based on the volume and specific resource requirements of the batch jobs. It allows you to run tasks written in different programming languages with minimal operational overhead.

</details>

### 145. q-372

A company is building a critical data processing application that will run on Amazon EC2 instances. The company must not run any two nodes on the same underlying hardware. The company requires at least 99.99% availability for the application. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the application to three Availability Zones by using a spread placement group strategy.**

The solution must meet two key requirements: high availability (99.99%) and hardware isolation for each node. 1. High Availability (99.99%): The Amazon EC2 Service Level Agreement (SLA) guarantees 99.99% uptime for instances deployed across two or more Availability Zones (AZs) within the same region. Deploying the application across three AZs meets this stringent availability requirement by protecting against the failure of a single AZ. 2. Hardware Isolation: A spread placement group is specifically designed to place each instance on distinct underlying hardware (such as a separate rack with its own power and network). This strategy directly fulfills the requirement that no two nodes run on the same hardware, minimizing the risk of simultaneous failures due to hardware issues. Why Incorrect Options are Wrong: A. A cluster placement group co-locates instances on the same hardware for low

</details>

### 146. dt-372

After setting up a Virtual Private Cloud (VPC) network, a more experienced cloud engineer suggests that to achieve low network latency and high network throughput you should look into setting up a placement group. You know nothing about this, but begin to do some research about it and are especially curious about its limitations. Which of the below statements is wrong in describing the limitations of a placement group?

<details><summary>Answer</summary>

**B. A placement group can span multiple Availability Zones.**

</details>

### 147. q-375 `least-ops`

An ecommerce company is building a distributed application that involves several serverless functions and AWS services to complete order- processing tasks. These tasks require manual approvals as part of the workflow. A solutions architect needs to design an architecture for the order-processing application. The solution must be able to combine multiple AWS Lambda functions into responsive serverless applications. The solution also must orchestrate data and services that run on Amazon EC2 instances, containers, or on-premises servers. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Step Functions to build the application.**

Step Functions provide a way to coordinate and orchestrate multiple AWS services, including AWS Lambda functions, in a serverless workflow. They allow you to build applications by connecting various serverless functions and services without managing the underlying infrastructure.

</details>

### 148. dt-376

For which of the following use cases are Simple Workflow Service (SWF) and Amazon EC2 an appropriate solution? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Managing a multi-step and multi-decision checkout process of an e-commerce website.; C. Orchestrating the execution of distributed and auditable business processes.**

</details>

### 149. dt-377

Which of the following instance types are available as Amazon EBS-backed only? (Choose 2 answers)

<details><summary>Answer</summary>

**A. General purpose T2.; D. Compute-optimized C3.**

</details>

### 150. q-377

A company recently deployed a new auditing system to centralize information about operating system versions, patching, and installed software for Amazon EC2 instances. A solutions architect must ensure all instances provisioned through EC2 Auto Scaling groups successfully send reports to the auditing system as soon as they are launched and terminated. Which solution achieves these goals MOST efficiently?

<details><summary>Answer</summary>

**B. Use EC2 Auto Scaling lifecycle hooks to run a custom script to send data to the audit system when instances are launched and terminated.**

</details>

### 151. q-380

A company is migrating its on-premises workload to the AWS Cloud. The company already uses several Amazon EC2 instances and Amazon RDS DB instances. The company wants a solution that automatically starts and stops the EC2 instances and DB instances outside of business hours. The solution must minimize cost and infrastructure maintenance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an AWS Lambda function that will start and stop the EC2 instances and DB instances. Configure Amazon EventBridge to invoke the Lambda function on a schedule.**

AWS Lambda Function: Create a Lambda function that contains the logic to start and stop the EC2 instances and DB instances. Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It is a cost-effective and maintenance-free solution.  Amazon EventBridge: Configure EventBridge (formerly CloudWatch Events) to invoke the Lambda function on a schedule. EventBridge provides a reliable and scalable way to schedule the execution of Lambda functions at specified intervals, such as starting and stopping instances during business hours.

</details>

### 152. dt-381

In Amazon AWS, which of the following statements is true of key pairs?

<details><summary>Answer</summary>

**B. Key pairs are used only for Amazon EC2 and Amazon CloudFront.**

</details>

### 153. q-382

A company has a three-tier application on AWS that ingests sensor data from its users’ devices. The traffic flows through a Network Load Balancer (NLB), then to Amazon EC2 instances for the web tier, and finally to EC2 instances for the application tier. The application tier makes calls to a database. What should a solutions architect do to improve the security of the data in transit?

<details><summary>Answer</summary>

**A. Configure a TLS listener. Deploy the server certificate on the NLB.**

TLS Listener on NLB: By configuring a TLS (Transport Layer Security) listener on the NLB, you can encrypt the traffic between the users' devices and the web tier EC2 instances. This helps protect the data in transit from eavesdropping and other potential security threats.

</details>

### 154. dt-388

You have a video transcoding application running on Amazon EC2. Each instance polls a queue to find out which video should be transcoded, and then runs a transcoding process. If this process is interrupted, the video will be transcoded by another instance based on the queuing system. You have a large backlog of videos which need to be transcoded and would like to reduce this backlog by adding more instances. You will need these instances only until the backlog is reduced. Which type of Amazon EC2 instances should you use to reduce the backlog in the most cost efficient way?

<details><summary>Answer</summary>

**B. Spot instances.**

</details>

### 155. q-388

A company is deploying a two-tier web application in a VPC. The web tier is using an Amazon EC2 Auto Scaling group with public subnets that span multiple Availability Zones. The database tier consists of an Amazon RDS for MySQL DB instance in separate private subnets. The web tier requires access to the database to retrieve product information. The web application is not working as intended. The web application reports that it cannot connect to the database. The database is confirmed to be up and running. All configurations for the network ACLs, security groups, and route tables are still in their default states. What should a solutions architect recommend to fix the application?

<details><summary>Answer</summary>

**D. Add an inbound rule to the security group of the database tier’s RDS instance to allow traffic from the web tiers security group.**

Security Groups: Security groups act as virtual firewalls for your instances to control inbound and outbound traffic. By default, they deny all inbound traffic. In this scenario, the default security group associated with the RDS instance is likely denying incoming traffic from the web tier.  Inbound Rule: To allow traffic from the web tier's EC2 instances to the database tier's RDS instance, you need to add an inbound rule to the security group associated with the RDS instance. This rule should permit traffic from the security group associated with the web tier's EC2 instances.

</details>

### 156. q-391

A company needs a backup strategy for its three-tier stateless web application. The web application runs on Amazon EC2 instances in an Auto Scaling group with a dynamic scaling policy that is configured to respond to scaling events. The database tier runs on Amazon RDS for PostgreSQL. The web application does not require temporary local storage on the EC2 instances. The company’s recovery point objective (RPO) is 2 hours. The backup strategy must maximize scalability and optimize resource utilization for this environment. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Retain the latest Amazon Machine Images (AMIs) of the web and application tiers. Enable automated backups in Amazon RDS and use point-in-time recovery to meet the RPO.**

Snapshots of EBS volumes would be necessary if you want to back up the entire EC2 instance, including any applications and temporary data stored on the EBS volumes attached to the instances. When you take a snapshot of an EBS volume, it backs up the entire contents of that volume. This ensures that you can restore the entire EC2 instance to a specific point in time more quickly. However, if there is no temporary data stored on the EBS volumes, then snapshots of EBS volumes are not necessary.

</details>

### 157. q-393

A company is moving a legacy data processing application to the AWS Cloud. The application needs to run on Amazon EC2 instances behind an Application Load Balancer (ALB). The application must handle incoming traffic spikes and continue to work in the event of an application fault in one Availability Zone. The company requires that a Web Application Firewall (WAF) must be attached to the ALB. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the application to EC2 instances in an Auto Scaling group across multiple Availability Zones. Use an ALB to distribute traffic. Use AWS WAF.**

The solution requires high availability, automatic scaling, and web application security. An Auto Scaling group configured across multiple Availability Zones (AZs) ensures the application can handle traffic spikes and remains operational even if one AZ fails. An Application Load Balancer (ALB) is designed to distribute incoming HTTP/HTTPS traffic across these instances in multiple AZs. AWS WAF integrates directly with an ALB to protect the web application from common exploits and bots, fulfilling all the stated requirements in a cohesive and standard architectural pattern. Why Incorrect Options are Wrong: A. A single Availability Zone deployment is not resilient to an AZ failure, which violates the high availability requirement of the question. C. This describes a multi-Region architecture, which is overly complex for the stated requirement of surviving a single AZ failure. Also, AWS WAF

</details>

### 158. dt-393

Per the AWS Acceptable Use Policy, penetration testing of EC2 instances

<details><summary>Answer</summary>

**B. May be performed by AWS, and is periodically performed by AWS.**

</details>

### 159. dt-396

You decide that you need to create a number of Auto Scaling groups to try and save some money as you have noticed that at certain times most of your EC2 instances are not being used. By default, what is the maximum number of Auto Scaling groups that AWS will allow you to create?

<details><summary>Answer</summary>

**C. 20.**

</details>

### 160. dt-397

After moving an E-Commerce website for a client from a dedicated server to AWS you have also set up auto scaling to perform health checks on the instances in your group and replace instances that fail these checks. Your client has come to you with his own health check system that he wants you to use as it has proved to be very useful prior to his site running on AWS. What do you think would be an appropriate response to this given all that you know about auto scaling?

<details><summary>Answer</summary>

**C. It is possible to implement your own health check system and then send the instance's health information directly from your system to Cloud Watch.**

</details>

### 161. q-397

An ecommerce company needs to run a scheduled daily job to aggregate and filter sales records for analytics. The company stores the sales records in an Amazon S3 bucket. Each object can be up to 10 GB in size. Based on the number of sales events, the job can take up to an hour to complete. The CPU and memory usage of the job are constant and are known in advance. A solutions architect needs to minimize the amount of operational effort that is needed for the job to run. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Create an Amazon Elastic Container Service (Amazon ECS) cluster with an AWS Fargate launch type. Create an Amazon EventBridge scheduled event that launches an ECS task on the cluster to run the job.**

C. Amazon ECS with Fargate: Fargate allows you to run containers without managing the underlying infrastructure. You can schedule the ECS task with EventBridge, and since Fargate manages the resources, you don't need to worry about scaling or infrastructure maintenance. This is a good fit for long-running jobs.

</details>

### 162. q-398

A disaster response team is using drones to collect images of recent storm damage. The response team's laptops lack the storage and compute capacity to transfer the images and process the data. While the team has Amazon EC2 instances for processing and Amazon S3 buckets for storage, network connectivity is intermittent and unreliable. The images need to be processed to evaluate the damage. What should a solutions architect recommend?

<details><summary>Answer</summary>

**A. Use AWS Snowball Edge devices to process and store the images.**

The scenario describes a need for local storage and compute power in an environment with unreliable and intermittent network connectivity. AWS Snowball Edge devices are specifically designed for this use case. They provide both storage capacity and onboard compute resources (EC2-compatible instances and AWS Lambda functions) in a ruggedized, portable appliance. This allows the disaster response team to store the large drone images and process them locally at the edge, without relying on a stable connection to the AWS cloud. Once processing is complete or connectivity is restored, the device can be shipped to AWS to transfer the data securely and efficiently into Amazon S3. Why Incorrect Options are Wrong: B: Amazon SQS is a message queuing service for small payloads (up to 256 KB) and is not suitable for storing large image files. C: Amazon Data Firehose is a data streaming service that

</details>

### 163. q-405

A company is migrating a distributed application to AWS. The application serves variable workloads. The legacy platform consists of a primary server that coordinates jobs across multiple compute nodes. The company wants to modernize the application with a solution that maximizes resiliency and scalability. How should a solutions architect design the architecture to meet these requirements?

<details><summary>Answer</summary>

**B. Configure an Amazon Simple Queue Service (Amazon SQS) queue as a destination for the jobs. Implement the compute nodes with Amazon EC2 instances that are managed in an Auto Scaling group. Configure EC2 Auto Scaling based on the size of the queue.**

This architecture effectively modernizes the legacy application by decoupling the job submission and processing components using an Amazon SQS queue. This enhances resiliency, as jobs are durably stored in the queue until a compute node successfully processes them. Using an Amazon EC2 Auto Scaling group for the compute nodes provides scalability. Configuring the Auto Scaling group to scale based on the SQS queue size (e.g., the ApproximateNumberOfMessagesVisible metric) is the most effective strategy for variable workloads. This ensures that the number of compute nodes automatically adjusts to match the volume of pending jobs, optimizing both performance and cost. Why Incorrect Options are Wrong: A. Scheduled scaling is unsuitable for unpredictable, variable workloads; it is designed for predictable traffic patterns that occur on a recurring schedule. C. AWS CloudTrail is a service for l

</details>

### 164. q-405

A solutions architect is designing the architecture for a software demonstration environment. The environment will run on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer (ALB). The system will experience significant increases in traffic during working hours but is not required to operate on weekends. Which combination of actions should the solutions architect take to ensure that the system can scale to meet demand? (Choose two.)

<details><summary>Answer</summary>

**D. Use a target tracking scaling policy to scale the Auto Scaling group based on instance CPU utilization.**

E. Use scheduled scaling to change the Auto Scaling group minimum, maximum, and desired capacity to zero for weekends. Revert to the default values at the start of the week.  Explanation: An Application Load Balancer scales its own capacity automatically — you don't (and can't) attach an Auto Scaling policy to the ALB itself, so the old option A isn't a real configuration. The EC2 Auto Scaling group behind it is what needs a scaling policy (D), alongside scheduled scaling (E) to scale to zero on weekends.  This allows you to save costs and resources during weekends when the system is not required to operate. Scaling down the Auto Scaling group to zero instances during weekends and reverting to the default values at the start of the week ensures that you only incur costs when the system is actively in use.

</details>

### 165. dt-408

In Amazon EC2, partial instance-hours are billed [...].

<details><summary>Answer</summary>

**D. as full hours.**

</details>

### 166. dt-409

In Amazon EC2, what is the limit of Reserved Instances per Availability Zone each month?

<details><summary>Answer</summary>

**B. 20.**

</details>

### 167. q-409 `availability`

A solutions architect must migrate a Windows Internet Information Services (IIS) web application to AWS. The application currently relies on a file share hosted in the user's on-premises network-attached storage (NAS). The solutions architect has proposed migrating the IIS web servers to Amazon EC2 instances in multiple Availability Zones that are connected to the storage solution, and configuring an Elastic Load Balancer attached to the instances. Which replacement to the on-premises file share is MOST resilient and durable?

<details><summary>Answer</summary>

**C. Migrate the file share to Amazon FSx for Windows File Server.**

Amazon FSx for Windows File Server: Amazon FSx is a fully managed file storage service that is compatible with Windows file systems. Amazon FSx for Windows File Server is specifically designed for Windows workloads, including IIS web applications. It provides a highly available and durable file system that can be accessed by multiple EC2 instances in different Availability Zones.

</details>

### 168. dt-412

A user wants to use an EBS-backed Amazon EC2 instance for a temporary job. Based on the input data, the job is most likely to finish within a week. Which of the following steps should be followed to terminate the instance automatically once the job is finished?

<details><summary>Answer</summary>

**C. Configure the Cloud Watch alarm on the instance that should perform the termination action once the instance is idle.**

</details>

### 169. q-413

An ecommerce company is experiencing an increase in user traffic. The company’s store is deployed on Amazon EC2 instances as a two-tier web application consisting of a web tier and a separate database tier. As traffic increases, the company notices that the architecture is causing significant delays in sending timely marketing and order confirmation email to users. The company wants to reduce the time it spends resolving complex email delivery issues and minimize operational overhead. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Configure the web instance to send email through Amazon Simple Email Service (Amazon SES).**

Amazon Simple Email Service (Amazon SES) is a fully managed email sending service. By configuring the web instances to send emails through Amazon SES, the ecommerce company can offload the complexity of email delivery to a reliable and scalable service.

</details>

### 170. dt-416

A t2.medium EC2 instance type must be launched with what type of Amazon Machine Image (AMI)?

<details><summary>Answer</summary>

**C. An Amazon EBS-backed Hardware Virtual Machine AMI.**

</details>

### 171. dt-419

Amazon EC2 provides a [...]. It is an HTTP or HTTPS request that uses the HTTP verbs GET or POST.

<details><summary>Answer</summary>

**C. Query API.**

</details>

### 172. dt-420

Which of the following requires a custom Cloud Watch metric to monitor?

<details><summary>Answer</summary>

**C. Disk usage activity of an EC2 instance.**

</details>

### 173. q-421 `cost`

A company deployed a three-tier web application in a single Availability Zone in the us-east-1 Region on a single Amazon EC2 instance. Usage of the application is growing. A solutions architect needs to ensure that the application can handle the growing amount of traffic. The solutions architect also needs to ensure the application is resilient. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Create an EC2 Auto Scaling group that contains a minimum of three EC2 instances spread across Availability Zones. Create an Application Load Balancer (ALB). Configure the ALB to route traffic to a target group that contains all the instances. Create an Amazon CloudWatch alarm to scale the EC2 instances horizontally to handle the application traffic.**

This solution correctly addresses all requirements. An EC2 Auto Scaling group configured across multiple Availability Zones (AZs) provides both high availability and resilience by ensuring the application can withstand the failure of a single AZ. The Application Load Balancer (ALB) distributes incoming traffic across the instances in all configured AZs. Using an Amazon CloudWatch alarm to trigger horizontal scaling (adding or removing EC2 instances) is the most effective method to handle variable traffic loads. This dynamic scaling approach ensures that compute capacity matches demand, thereby meeting the scalability requirement in the most cost-effective manner by avoiding over-provisioning. Why Incorrect Options are Wrong: A. Vertical scaling (changing instance size) is less agile for handling traffic spikes than horizontal scaling and can lead to service interruptions during resizing.

</details>

### 174. dt-422

An Elastic IP address (EIP) is a static IP address designed for dynamic cloud computing. With an EIP, you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account. Your EIP is associated with your AWS account, not a particular EC2 instance, and it remains associated with your account until you choose to explicitly release it. By default how many EIPs is each AWS account limited to on a per region basis?

<details><summary>Answer</summary>

**B. 5.**

</details>

### 175. q-422

A company is developing a new machine learning (ML) model solution on AWS. The models are developed as independent microservices that fetch approximately 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular. Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which design should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**Direct the requests from the API into an Amazon Simple Queue Service (Amazon SQS) queue. Deploy the models as Amazon Elastic Container Service (Amazon ECS) services that read from the queue. Enable AWS Auto Scaling on Amazon ECS for both the cluster and copies of the service based on the queue size.**

The API is asynchronous, so requests can sit in an SQS queue and be picked up when capacity exists; the queue absorbs a sudden batch of thousands of requests without dropping any and without the caller waiting. Scaling the ECS service on the number of messages waiting in the queue adds containers only when work arrives and scales back down through the days or weeks a model is unused, and scaling the cluster capacity alongside it means you are not paying for idle hosts. Long-running containers also keep the 1 GB of model data in memory between requests, whereas a design that fronts short-lived functions with a load balancer would re-download that 1 GB on every cold start and would make an asynchronous API behave synchronously.

</details>

### 176. q-424 `cost`

A company is running a custom application on Amazon EC2 On-Demand Instances. The application has frontend nodes that need to run 24 hours a day, 7 days a week and backend nodes that need to run only for a short time based on workload. The number of backend nodes varies during the day. The company needs to scale out and scale in more instances based on workload. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use Reserved Instances for the frontend nodes. Use Spot Instances for the backend nodes.**

Reserved Instances (RIs) for Frontend Nodes: Since the frontend nodes need to run 24/7, Reserved Instances provide a significant cost savings compared to On-Demand pricing. RIs are a commitment to a consistent usage pattern, making them suitable for instances that need to run continuously.  Spot Instances for Backend Nodes: Spot Instances are a cost-effective option for workloads that can be interrupted or are flexible regarding availability. As the number of backend nodes varies during the day, using Spot Instances allows you to take advantage of spare capacity at a lower cost. Spot Instances are suitable for short-lived, scalable, and flexible workloads.

</details>

### 177. dt-426

Which of the following is true of Amazon EC2 security group?

<details><summary>Answer</summary>

**D. You can modify the rules for a security group at any time.**

</details>

### 178. q-427 `availability`

A solutions architect is implementing a complex Java application with a MySQL database. The Java application must be deployed on Apache Tomcat and must be highly available. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy the application by using AWS Elastic Beanstalk. Configure a load-balanced environment and a rolling deployment policy.**

AWS Elastic Beanstalk: It is a fully managed service that simplifies the deployment and operation of applications, including web applications running Apache Tomcat. Elastic Beanstalk handles the deployment details, capacity provisioning, load balancing, auto-scaling, and application health monitoring, making it easier to deploy and manage your applications.

</details>

### 179. dt-428

A user is trying to launch a similar EC2 instance from an existing instance with the option 'Launch More like this'. The AMI of the selected instance is deleted. What will happen in this case?

<details><summary>Answer</summary>

**D. AWS will throw an error saying that the AMI is deregistered.**

</details>

### 180. dt-434 `availability`

A client application requires operating system privileges on a relational database server. What is an appropriate configuration for a highly available database architecture?

<details><summary>Answer</summary>

**D. Amazon EC2 instances in a replication configuration utilizing two different Availability Zones.**

</details>

### 181. q-437

A company operates an ecommerce website on Amazon EC2 instances behind an Application Load Balancer (ALB) in an Auto Scaling group. The site is experiencing performance issues related to a high request rate from illegitimate external systems with changing IP addresses. The security team is worried about potential DDoS attacks against the website. The company must block the illegitimate incoming requests in a way that has a minimal impact on legitimate users. What should a solutions architect recommend?

<details><summary>Answer</summary>

**B. Deploy AWS WAF, associate it with the ALB, and configure a rate-limiting rule.**

AWS WAF is a web application firewall service that helps protect your web applications from common web exploits. It allows you to create rules to filter and monitor HTTP and HTTPS traffic based on conditions that you define. By associating AWS WAF with the ALB, you can inspect and filter incoming traffic before it reaches your instances, providing a layer of protection against DDoS attacks and other malicious activities.

</details>

### 182. dt-440

Regarding Amazon Route 53, if your application is running on Amazon EC2 instances in two or more Amazon EC2 regions and if you have more than one Amazon EC2 instance in one or more regions, you can use [...] to route traffic to the correct region and then use [...] route traffic to instances within the region, based on probabilities that you specify.

<details><summary>Answer</summary>

**B. latency-based routing; weighted resource record sets.**

</details>

### 183. q-441 `cost`

A company hosts a multi-tier web application on Amazon Linux Amazon EC2 instances behind an Application Load Balancer. The instances run in an Auto Scaling group across multiple Availability Zones. The company observes that the Auto Scaling group launches more On-Demand Instances when the application's end users access high volumes of static web content. The company wants to optimize cost. What should a solutions architect do to redesign the application MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create an Amazon CloudFront distribution to host the static web contents from an Amazon S3 bucket.**

Amazon CloudFront is a content delivery network (CDN) service that delivers static and dynamic web content, including images, videos, CSS, and JavaScript, with low latency and high transfer speeds. It can be used to cache and distribute static content globally, reducing the load on your web servers.  By creating a CloudFront distribution and hosting static web content in an Amazon S3 bucket, you offload the serving of static content to the CDN, which can significantly reduce the load on your EC2 instances.

</details>

### 184. dt-442 `availability`

When using the following AWS services, which should be implemented in multiple Availability Zones for high availability solutions? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Amazon Elastic Compute Cloud (EC2).; C. Amazon Elastic Load Balancing.**

</details>

### 185. q-444

A company has hired a solutions architect to design a reliable architecture for its application. The application consists of one Amazon RDS DB instance and two manually provisioned Amazon EC2 instances that run web servers. The EC2 instances are located in a single Availability Zone. An employee recently deleted the DB instance, and the application was unavailable for 24 hours as a result. The company is concerned with the overall reliability of its environment. What should the solutions architect do to maximize reliability of the application's infrastructure?

<details><summary>Answer</summary>

**B. Update the DB instance to be Multi-AZ, and enable deletion protection. Place the EC2 instances behind an Application Load Balancer, and run them in an EC2 Auto Scaling group across multiple Availability Zones.**

Multi-AZ RDS Instance: By updating the DB instance to be Multi-AZ, you ensure that there is a standby replica in a different Availability Zone, providing high availability and automatic failover in case of a failure in the primary zone.  Deletion Protection: Enabling deletion protection for the DB instance helps prevent accidental deletion, reducing the risk of downtime caused by human error.

</details>

### 186. dt-445

Which of the following features ensures even distribution of traffic to Amazon EC2 instances in multiple Availability Zones registered with a load balancer?

<details><summary>Answer</summary>

**A. Elastic Load Balancing request routing.**

</details>

### 187. dt-447

You have been using T2 instances as your CPU requirements have not been that intensive. However you now start to think about larger instance types and start looking at M1 and M3 instances. You are a little confused as to the differences between them as they both seem to have the same ratio of CPU and memory. Which statement below is incorrect as to why you would use one over the other?

<details><summary>Answer</summary>

**B. M3 instances are configured with more swap memory than M1 instances.**

</details>

### 188. dt-450

If you're unable to connect via SSH to your EC2 instance, which of the following should you check and possibly correct to restore connectivity?

<details><summary>Answer</summary>

**D. Adjust the instance's Security Group to permit ingress traffic over port 22 from your IP.**

</details>

### 189. q-451

A company is migrating its applications and databases to the AWS Cloud. The company will use Amazon Elastic Container Service (Amazon ECS), AWS Direct Connect, and Amazon RDS. Which activities will be managed by the company's operational team? (Choose three.)

<details><summary>Answer</summary>

**C. Configuration of additional software components on Amazon ECS for monitoring, patch management, log management, and host intrusion detection**

The company's operational team is responsible for configuring additional software components on Amazon ECS, such as monitoring tools, patch management tools, log management systems, and host intrusion detection systems. These components are often specific to the company's requirements and policies.  B. Creation of an Amazon RDS DB instance and configuring the scheduled maintenance window:  The operational team is responsible for creating Amazon RDS DB instances, configuring parameters, and setting up maintenance windows based on the company's operational needs. This includes decisions about the size and type of the RDS instance, storage configuration, and other relevant settings.  F. Encryption of the data that moves in transit through Direct Connect:  While AWS manages the physical infrastructure of Direct Connect, the company's operational team is responsible for configuring encryption for the data in transit over Direct Connect. This includes implementing encryption protocols and ensuring the security of data while it travels between the on-premises data center and AWS.

</details>

### 190. q-452 `least-ops`

A company is developing a microservices-based application to manage the company's delivery operations. The application consists of microservices that process orders, manage a fleet of delivery vehicles, and optimize delivery routes. The microservices must be able to scale independently and must be able to handle bursts of traffic without any data loss. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon SQS to establish communication between microservices. Deploy the application on Amazon ECS containers on AWS Fargate.**

This solution effectively meets all requirements. Amazon SQS provides a durable, asynchronous queue that decouples the microservices, handles traffic bursts by buffering requests, and prevents data loss. Deploying the application on AWS Fargate, a serverless compute engine for containers, allows each microservice to scale independently based on demand without the need to manage underlying EC2 instances. This combination offers high scalability and resilience with the lowest operational overhead, as server and cluster management is handled by AWS. Why Incorrect Options are Wrong: A. API Gateway with EC2 uses synchronous communication, which can lead to data loss if a downstream service is unavailable. Managing EC2 instances incurs higher operational overhead than Fargate. C. WebSocket is for persistent, real-time communication, which is not the typical pattern for decoupling backend micro

</details>

### 191. dt-455

A user has hosted an application on EC2 instances. The EC2 instances are configured with ELB and Auto Scaling. The application server session time out is 2 hours. The user wants to configure connection draining to ensure that all in-flight requests are supported by ELB even though the instance is being deregistered. What time out period should the user specify for connection draining?

<details><summary>Answer</summary>

**A. 1 hour.**

</details>

### 192. dt-456

What does the following command do with respect to the Amazon EC2 security groups? ec2-create-group CreateSecurityGroup

<details><summary>Answer</summary>

**B. Creates a new security group for use with your account.**

</details>

### 193. q-457

A company that uses AWS is building an application to transfer data to a product manufacturer. The company has its own identity provider (IdP). The company wants the IdP to authenticate application users while the users use the application to transfer data. The company must use Applicability Statement 2 (AS2) protocol. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Transfer Family to transfer the data. Create an AWS Lambda function for IdP authentication.**

AWS Transfer Family (Option C): AWS Transfer Family is a fully managed service that allows you to transfer files over the internet using a range of protocols, including AS2. You can integrate AWS Transfer Family with your IdP for user authentication. By using a Lambda function, you can customize the authentication process and integrate it with your own IdP.

</details>

### 194. dt-458

Which of the following are characteristics of a reserved instance? (Choose 3 answers)

<details><summary>Answer</summary>

**A. It can be migrated across Availability Zones.; D. It is specific to an instance Type.; E. It can be used to lower Total Cost of Ownership (TCO) of a system.**

</details>

### 195. q-460

A solutions architect is designing a web application that will run on Amazon EC2 instances behind an Application Load Balancer (ALB). The company strictly requires that the application be resilient against malicious internet activity and attacks, and protect against new common vulnerabilities and exposures. What should the solutions architect recommend?

<details><summary>Answer</summary>

**B. Deploy an appropriate managed rule for AWS WAF and associate it with the ALB.**

AWS WAF (Web Application Firewall) is the service designed to protect web applications from common exploits that could affect availability, compromise security, or consume excessive resources. By deploying AWS WAF with an AWS Managed Rule group, such as the Core rule set (CRS) or Known bad inputs rule group, and associating it with the Application Load Balancer (ALB), the application is protected against a wide range of threats. AWS Managed Rules are curated and maintained by AWS threat intelligence teams, ensuring they are updated to protect against new and emerging threats, including those listed in Common Vulnerabilities and Exposures (CVEs). This directly meets the strict requirement for protection against malicious activity and new vulnerabilities. Why Incorrect Options are Wrong: A. Amazon CloudFront is a content delivery network (CDN) that improves performance and provides some DD

</details>

### 196. q-461

A company is developing a mobile gaming app in a single AWS Region. The app runs on multiple Amazon EC2 instances in an Auto Scaling group. The company stores the app data in Amazon DynamoDB. The app communicates by using TCP traffic and UDP traffic between the users and the servers. The application will be used globally. The company wants to ensure the lowest possible latency for all users. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Global Accelerator to create an accelerator. Create a Network Load Balancer (NLB) behind an accelerator endpoint that uses Global Accelerator integration and listening on the TCP and UDP ports. Update the Auto Scaling group to register instances on the NLB.**

</details>

### 197. dt-462

What is a placement group?

<details><summary>Answer</summary>

**B. A feature that enables EC2 instances to interact with each other via high bandwidth, low latency connections.**

</details>

### 198. q-462

A company has an application that processes customer orders. The company hosts the application on an Amazon EC2 instance that saves the orders to an Amazon Aurora database. Occasionally when traffic is high the workload does not process orders fast enough. What should a solutions architect do to write the orders reliably to the database as quickly as possible?

<details><summary>Answer</summary>

**B. Write orders to an Amazon Simple Queue Service (Amazon SQS) queue. Use EC2 instances in an Auto Scaling group behind an Application Load Balancer to read from the SQS queue and process orders into the database.**

Amazon SQS, which is a fully managed message queuing service. Writing orders to an SQS queue allows for decoupling the EC2 instances processing the orders from the application writing the orders. EC2 instances in an Auto Scaling group can then read from the SQS queue, ensuring that the processing scales with demand.  Using an Auto Scaling group ensures that you can dynamically adjust the number of EC2 instances based on the workload. This can help handle high traffic efficiently.

</details>

### 199. dt-466

A user is planning to make a mobile game which can be played online or offline and will be hosted on EC2. The user wants to ensure that if someone breaks the highest score or they achieve some milestone they can inform all their colleagues through email. Which of the below mentioned AWS services helps achieve this goal?

<details><summary>Answer</summary>

**B. AWS Simple Email Service.**

</details>

### 200. q-466 `availability`

A company designed a stateless two-tier application that uses Amazon EC2 in a single Availability Zone and an Amazon RDS Multi-AZ DB instance. New company management wants to ensure the application is highly available. What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Configure the application to use Multi-AZ EC2 Auto Scaling and create an Application Load Balancer**

</details>

### 201. dt-468

Which of the following is NOT a characteristic of Amazon Elastic Compute Cloud (Amazon EC2)?

<details><summary>Answer</summary>

**B. It increases the need to forecast traffic by providing dynamic IP addresses for static cloud computing.**

</details>

### 202. q-468

A company is developing a microservices application that will provide a search catalog for customers. The company must use REST APIs to present the frontend of the application to users. The REST APIs must access the backend services that the company hosts in containers in private VPC subnets. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Design a REST API by using Amazon API Gateway. Host the application in Amazon Elastic Container Service (Amazon ECS) in a private subnet. Create a private VPC link for API Gateway to access Amazon ECS.**

</details>

### 203. q-469

A company wants to use AWS to scale up the number of its long-running critical simulations. The company wants to perform large-scale parallel simulations that run for days. The simulations cannot be stopped. The company must store the output for later review by using durable and fault-tolerant storage. The output includes structured and unstructured data. The structured data includes simulation results. The unstructured data includes images up to 1 MB in size. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Batch to perform simulations. Store structured data in Amazon RDS. Store unstructured data in Amazon S3.**

The requirement is for long-running, parallel simulations that cannot be interrupted. AWS Batch is the ideal service for this, as it dynamically provisions compute resources (like On-Demand EC2 instances) and manages the execution of batch jobs, making it suitable for workloads that run for days. For storing the output, a combination of Amazon RDS for structured results and Amazon S3 for unstructured data (images) provides a durable, fault-tolerant, and scalable solution. This architecture separates compute from storage and uses the best-fit service for each data type. Why Incorrect Options are Wrong: A. AWS Lambda functions have a maximum execution timeout of 15 minutes, making them unsuitable for simulations that run for days. C. Amazon EC2 Spot Instances can be terminated with a two-minute notice, which violates the requirement that the simulations cannot be stopped. D. Storing all da

</details>

### 204. dt-469

A user has launched one EC2 instance in the US East region and one in the US West region. The user has launched an RDS instance in the US East region. How can the user configure access from both the EC2 instances to RDS?

<details><summary>Answer</summary>

**C. Configure the security group of the US East region to allow traffic from the US West region's instance and configure the RDS security group's ingress rule for the US East EC2 group.**

</details>

### 205. q-471 `least-ops` `availability`

A company wants to deploy its containerized application workloads to a VPC across three Availability Zones. The company needs a solution that is highly available across Availability Zones. The solution must require minimal changes to the application. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon ECS. Configure Amazon ECS Service Auto Scaling to use target tracking scaling. Set the minimum capacity to 3. Set the task placement strategy type to spread with an Availability Zone attribute.**

The requirement is for a highly available, containerized application with minimal operational overhead. Amazon ECS is a fully managed container orchestration service that simplifies deployment. Using the spread task placement strategy with an AvailabilityZone attribute ensures that tasks are distributed evenly across the specified AZs, providing high availability. Service Auto Scaling with target tracking automatically adjusts the number of tasks based on a specified metric, meeting the scaling requirement. This combination provides a robust, highly available solution for containerized workloads with less management effort compared to managing a Kubernetes cluster or EC2 instances directly. Why Incorrect Options are Wrong: B. Amazon EKS with self-managed nodes requires managing the Kubernetes worker nodes, which incurs more operational overhead than using the more managed Amazon ECS serv

</details>

### 206. q-474

A company runs a critical data analysis job each week before the first day of the work week. The job requires at least 1 hour to complete the analysis. The job is stateful and cannot tolerate interruptions. The company needs a solution to run the job on AWS. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a container for the job. Schedule the job to run as an AWS Fargate task on an Amazon ECS cluster by using Amazon EventBridge Scheduler.**

The job is stateful, cannot be interrupted, and runs for over an hour. AWS Fargate is a serverless compute engine for containers that removes the need to manage servers. Fargate tasks can run for extended periods, meeting the 1 hour requirement. They are not subject to interruptions like Spot Instances. Amazon EventBridge Scheduler is a serverless scheduler that can reliably invoke AWS services, making it the ideal choice to trigger the weekly Fargate task. This combination provides a reliable, non-interruptible, and scheduled compute environment. Why Incorrect Options are Wrong: B. AWS Lambda functions have a maximum execution timeout of 15 minutes, which is insufficient for a job that runs for at least one hour. C. Amazon EC2 Spot Instances can be terminated with a two-minute notice, which violates the requirement that the job cannot tolerate interruptions. D. AWS DataSync is a data mi

</details>

### 207. dt-475

While creating an Amazon RDS DB, your first task is to set up a DB [...] that controls what IP addresses or EC2 instances have access to your DB Instance.

<details><summary>Answer</summary>

**D. Security Group.**

</details>

### 208. q-477 `least-ops`

A company is running a web application on AWS Elastic Beanstalk. The web application is deployed across multiple Amazon EC2 instances that are behind an Application Load Balancer (ALB). The company plans to release a new version of the application. The company wants to test the new version of the application by using a subset of production traffic before a full rollout. The company needs to design a solution that helps ensure minimal disruption during testing. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Launch the new version of the application as a separate environment in Elastic Beanstalk. Configure the Elastic Beanstalk traffic-splitting feature to route a percentage of live traffic to the new environment.**

The goal is to test a new application version with a subset of production traffic on Elastic Beanstalk with minimal operational overhead. Elastic Beanstalk's traffic-splitting deployment policy is designed specifically for this use case (canary testing). This feature allows you to launch the new version in a separate environment and configure Elastic Beanstalk to automatically route a specified percentage of traffic to it. Elastic Beanstalk manages the underlying Application Load Balancer listener rules, providing the lowest operational overhead compared to manual configuration. Why Incorrect Options are Wrong: A. Manually updating ALB listener rules after creating a new environment has higher operational overhead than using the built-in Elastic Beanstalk traffic-splitting feature. C. Replacing existing instances is a rolling update or all-at-once deployment, not a test on a subset of tr

</details>

### 209. dt-482

What would be the best way to retrieve the public IP address of your EC2 instance using the CLI?

<details><summary>Answer</summary>

**D. Using instance metadata.**

</details>

### 210. dt-483

A company is building a two-tier web application to serve dynamic transaction-based content. The data tier is leveraging an Online Transactional Processing (OLTP) database. What services should you leverage to enable an elastic and scalable web tier?

<details><summary>Answer</summary>

**A. Elastic Load Balancing, Amazon EC2, and Auto Scaling.**

</details>

### 211. q-483 `cost`

A company containerized a Windows job that runs on .NET 6 Framework under a Windows container. The company wants to run this job in the AWS Cloud. The job runs every 10 minutes. The job’s runtime varies between 1 minute and 3 minutes. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use Amazon Elastic Container Service (Amazon ECS) on AWS Fargate to run the job. Create a scheduled task based on the container image of the job to run every 10 minutes.**

Amazon ECS is a fully managed container orchestration service, and AWS Fargate allows you to run containers without managing the underlying infrastructure. ECS on Fargate is a serverless option, which means you only pay for the vCPU and memory that you use, and it scales automatically to meet the needs of the job.

</details>

### 212. q-486

A company is building a three-tier application on AWS. The presentation tier will serve a static website The logic tier is a containerized application. This application will store data in a relational database. The company wants to simplify deployment and to reduce operational costs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon S3 to host static content. Use Amazon Elastic Container Service (Amazon ECS) with AWS Fargate for compute power. Use a managed Amazon RDS cluster for the database.**

Amazon S3 is a highly scalable and cost-effective storage service that can be used to host static content like a static website. It simplifies the storage and delivery of static assets. AWS Fargate is a serverless compute engine for containers. It allows you to run containers without managing the underlying infrastructure. This simplifies deployment and reduces operational overhead.

</details>

### 213. dt-488

You have three Amazon EC2 instances with Elastic IP addresses in the US East (Virginia) region, and you want to distribute requests across all three IPs evenly for users for whom US East (Virginia) is the appropriate region. How many EC2 instances would be sufficient to distribute requests in other regions?

<details><summary>Answer</summary>

**D. 1.**

</details>

### 214. dt-490

You are implementing a URL whitelisting system for a company that wants to restrict outbound HTTPS connections to specific domains from their EC2-hosted applications. You deploy a single EC2 instance running proxy software and configure it to accept traffic from all subnets and EC2 instances in the VPC. You configure the proxy to only pass through traffic to domains that you define in its whitelist configuration. You have a nightly maintenance window of 10 minutes where all instances fetch new software updates. Each update is about 200MB in size and there are 500 instances in the VPC that routinely fetch updates. After a few days you notice that some machines are failing to successfully download some, but not all of their updates within the maintenance window. The download URLs used for these updates are correctly listed in the proxy's whitelist configuration and you are able to access them manually using a web browser on the instances. What might be happening? (Choose 2 answers)

<details><summary>Answer</summary>

**A. You are running the proxy on an undersized EC2 instance type so network throughput is not sufficient for all instances to download their updates in time.; B. You are running the proxy on a sufficiently-sized EC2 instance in a private subnet and its network throughput is being throttled by a NAT running on an undersized EC2 instance.**

</details>

### 215. q-492

A company plans to run a high performance computing (HPC) workload on Amazon EC2 Instances The workload requires low-latency network performance and high network throughput with tightly coupled node-to-node communication. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Organizations to organize the accounts into organizational units (OUs). Define and attach a service control policy (SCP) to control the usage of EC2 instance types.**

An SCP is a guardrail, not a grant: it sets the maximum permissions available to principals in the accounts it applies to, and a user still needs an IAM identity-based policy that allows the action before anything works. Writing one SCP that denies ec2:RunInstances unless the ec2:InstanceType condition matches an approved list, then attaching it to the OUs holding the development accounts, stops oversized launches everywhere in those accounts at once, including by account administrators. That is far less work than maintaining IAM policies account by account or building a detection-and-remediation pipeline. Two limits to remember: an SCP never restricts the organization's management account, so keep workloads out of it, and SCPs have no effect unless all features are enabled in the organization.

</details>

### 216. dt-498

A user has launched a large EBS backed EC2 instance in the US-East-1a region. The user wants to achieve Disaster Recovery (DR) for that instance by creating another small instance in Europe. How can the user achieve DR?

<details><summary>Answer</summary>

**D. Create an AMI of the instance and copy the AMI to the EU region. Then launch the instance from the EU AMI.**

</details>

### 217. q-502

A company recently migrated a monolithic application to an Amazon EC2 instance and Amazon RDS. The application has tightly coupled modules. The existing design of the application gives the application the ability to run on only a single EC2 instance. The company has noticed high CPU utilization on the EC2 instance during peak usage times. The high CPU utilization corresponds to degraded performance on Amazon RDS for read requests. The company wants to reduce the high CPU utilization and improve read request performance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Resize the EC2 instance to an EC2 instance type that has more CPU capacity. Configure an Auto Scaling group with a minimum and maximum size of 1. Configure an RDS read replica for read requests.**

The solution must address two distinct issues: high CPU on a single EC2 instance and poor read performance on RDS. 1. EC2 High CPU: Since the monolithic application is constrained to a single instance, horizontal scaling (adding more instances) is not an option. Therefore, vertical scaling by resizing the EC2 instance to a type with more CPU capacity is the correct approach. An Auto Scaling group with a minimum and maximum size of 1 ensures the instance is self-healing without violating the single-instance constraint. 2. RDS Read Performance: The problem specifically mentions degraded performance for read requests. The most effective and targeted solution for this is to create an Amazon RDS read replica. This offloads the read traffic from the primary database instance, allowing it to dedicate its resources to write operations, thereby improving read performance and reducing the load on

</details>

### 218. dt-502

Select the correct statement: Within Amazon EC2, when using Linux instances, the device name /dev/sda1 is [...].

<details><summary>Answer</summary>

**D. reserved for the root device.**

</details>

### 219. dt-504

Your web application front end consists of multiple EC2 instances behind an Elastic Load Balancer. You configured ELB to perform health checks on these EC2 instances, if an instance fails to pass health checks, which statement will be true?

<details><summary>Answer</summary>

**D. The ELB stops sending traffic to the instance that failed its health check.**

</details>

### 220. dt-505

George has launched three EC2 instances inside the US-East-1a zone with his AWS account. Ray has launched two EC2 instances in the US-East-1a zone with his AWS account. Which of the below mentioned statements will help George and Ray understand the Availability Zone (AZ) concept better?

<details><summary>Answer</summary>

**B. The US-East-1a region of George and Ray can be different Availability Zones.**

</details>

### 221. q-505 `cost`

A company has Amazon EC2 instances that run nightly batch jobs to process data. The EC2 instances run in an Auto Scaling group that uses On- Demand billing. If a job fails on one instance, another instance will reprocess the job. The batch jobs run between 12:00 AM and 06:00 AM local time every day. Which solution will provide EC2 instances to meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Create a new launch template for the Auto Scaling group. Set the instances to Spot Instances. Set a policy to scale out based on CPU usage.**

Spot Instances: Spot Instances allow you to bid for unused EC2 capacity at a potentially lower cost than On-Demand pricing. This can result in significant cost savings for batch jobs that are fault-tolerant and can be interrupted or retried.  Scaling Policy: Setting a policy to scale out based on CPU usage ensures that additional Spot Instances are launched when the demand for processing power increases during batch job execution. This helps in handling varying workloads efficiently.

</details>

### 222. dt-508

Which AWS instance address has the following characteristics? 'If you stop an instance, its Elastic IP address is unmapped, and you must remap it when you restart the instance.'

<details><summary>Answer</summary>

**D. EC2 Addresses.**

</details>

### 223. q-508

A company has migrated multiple Microsoft Windows Server workloads to Amazon EC2 instances that run in the us-west-1 Region. The company manually backs up the workloads to create an image as needed. In the event of a natural disaster in the us-west-1 Region, the company wants to recover workloads quickly in the us-west-2 Region. The company wants no more than 24 hours of data loss on the EC2 instances. The company also wants to automate any backups of the EC2 instances. Which solutions will meet these requirements with the LEAST administrative effort? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon EC2-backed Amazon Machine Image (AMI) lifecycle policy to create a backup based on tags. Schedule the backup to run twice daily. Configure the copy to the us-west-2 Region.**

D. Create a backup vault by using AWS Backup. Use AWS Backup to create a backup plan for the EC2 instances based on tag values. Define the destination for the copy as us-west-2. Specify the backup schedule to run twice daily.

</details>

### 224. gh-508

Topic 1
A company has migrated multiple Microsoft Windows Server workloads to Amazon EC2 instances that run in the us-west-1 Region. The company manually backs up the workloads to create an image as needed.
In the event of a natural disaster in the us-west-1 Region, the company wants to recover workloads quickly in the us-west-2 Region. The company wants no more than 24 hours of data loss on the EC2 instances. The company also wants to automate any backups of the EC2 instances.
Which solutions will meet these requirements with the LEAST administrative effort? (Choose two.)

<details><summary>Answer</summary>

**B. Create an Amazon EC2-backed Amazon Machine Image (AMI) lifecycle policy to create a backup based on tags. Schedule the backup to run twice daily. Configure the copy to the us-west-2 Region.**

D. Create a backup vault by using AWS Backup. Use AWS Backup to create a backup plan for the EC2 instances based on tag values. Define the destination for the copy as us-west-2. Specify the backup schedule to run twice daily.

</details>

### 225. q-516 `cost`

An online education platform experiences lag and buffering during peak usage hours, when thousands of students access video lessons concurrently. A solutions architect needs to improve the performance of the education platform. The platform needs to handle unpredictable traffic surges without losing responsiveness. The platform must provide smooth video playback performance at all times. The platform must create multiple copies of each video lesson and store the copies in various bitrates to serve users who have different internet speeds. The smallest video size is 7 GB. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create an Auto Scaling group that includes Amazon EC2 instances that are sized to meet peak loads. Use the Auto Scaling group to serve videos. Use the Auto Scaling group to convert the videos to the required bitrates.**

The solution must handle unpredictable traffic surges for thousands of concurrent users while ensuring smooth video playback. Option B, using an Auto Scaling group of Amazon EC2 instances, directly addresses the requirement for scalability. The Auto Scaling group can automatically add or remove instances based on demand, ensuring the platform can handle peak loads without performance degradation. While not as optimal as a CDN-based approach, it is the only option presented that provides a viable mechanism to scale the video serving and processing tiers to meet the specified performance and traffic requirements. The other options contain fundamental technical flaws that make them unsuitable. Why Incorrect Options are Wrong: A. Amazon ElastiCache is an in-memory cache designed for small, frequently accessed data, not for caching multi-gigabyte video files. It is technically unsuitable and

</details>

### 226. q-516 `least-ops`

A company provides an API interface to customers so the customers can retrieve their financial information. Еhe company expects a larger number of requests during peak usage times of the year. The company requires the API to respond consistently with low latency to ensure customer satisfaction. The company needs to provide a compute host for the API. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon API Gateway and AWS Lambda functions with provisioned concurrency.**

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. AWS Lambda is a serverless computing service that automatically scales based on demand. Provisioned concurrency in AWS Lambda allows you to set a specific number of concurrent executions to ensure that the function is ready to respond quickly to incoming requests.

</details>

### 227. q-518

A company hosts its main public web application in one AWS Region across multiple Availability Zones. The application uses an Amazon EC2 Auto Scaling group and an Application Load Balancer (ALB). A web development team needs a cost-optimized compute solution to improve the company's ability to serve dynamic content globally to millions of customers. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon CloudFront distribution. Configure the existing ALB as the origin.**

Amazon CloudFront is a global Content Delivery Network (CDN) designed to provide low-latency, high-speed content delivery to users worldwide. By configuring the existing Application Load Balancer (ALB) as the origin for a CloudFront distribution, the company can serve both static and dynamic content from edge locations closer to its customers. This setup significantly reduces latency for dynamic requests by terminating user connections at the edge and leveraging AWS's optimized global network to reach the origin. Caching static assets at the edge also offloads the origin servers, reducing the load on the EC2 instances and lowering data transfer out costs, thereby meeting all the requirements for a cost-optimized, global solution. Why Incorrect Options are Wrong: B: Route 53 routing policies are effective for directing traffic to different regional endpoints. Since the application exists

</details>

### 228. q-522 `least-ops`

A company runs container applications by using Amazon Elastic Kubernetes Service (Amazon EKS). The company's workload is not consistent throughout the day. The company wants Amazon EKS to scale in and out according to the workload. Which combination of steps will meet these requirements with the LEAST operational overhead? (Choose two.)

<details><summary>Answer</summary>

**B. Use the Kubernetes Metrics Server to activate horizontal pod autoscaling.**

Kubernetes supports Horizontal Pod Autoscaling (HPA) based on custom metrics or resource metrics. By using the Kubernetes Metrics Server, you can enable HPA to automatically adjust the number of pods in a deployment based on observed custom metrics (such as application-specific metrics) or resource metrics (such as CPU or memory usage).  C. Use the Kubernetes Cluster Autoscaler:  The Kubernetes Cluster Autoscaler automatically adjusts the size of the cluster by adding or removing nodes based on the resource utilization and pod scheduling requirements. This helps in scaling the cluster itself based on the overall demand.

</details>

### 229. q-523

A company runs a microservice-based serverless web application. The application must be able to retrieve data from multiple Amazon DynamoDB tables A solutions architect needs to give the application the ability to retrieve the data with no impact on the baseline performance of the application. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**Use AWS AppSync pipeline resolvers.**

AppSync is a managed GraphQL front end for serverless applications, and a pipeline resolver runs an ordered series of functions inside one request, each attached to its own data source. That lets a single request gather data from several DynamoDB tables in the managed service layer, so the application's existing code path is untouched and its baseline performance is unaffected, and there is no new infrastructure to run. Lambda@Edge would mean writing and deploying edge functions that still have to call DynamoDB back in the table's region, which is more work and slower, and an edge-optimized API Gateway endpoint only changes where the connection is terminated.

</details>

### 230. dt-525

Which of the following items are required to allow an application deployed on an EC2 instance to write data to a DynamoDB table? Assume that no security keys are allowed to be stored on the EC2 instance. (Choose 3 answers)

<details><summary>Answer</summary>

**A. Create an IAM Role that allows write access to the DynamoDB table.; B. Add an IAM Role to a running EC2 instance.; E. Launch an EC2 Instance with the IAM Role included in the launch configuration.**

</details>

### 231. q-526 `performance`

An online SaaS platform serves customers across North America, Europe, and Asia-Pacific regions. Users report slow API response times during peak hours, and the company needs to improve performance without redesigning their core application. The API responses are mostly static content that does not change frequently. Which approach best optimizes performance for a global audience?

<details><summary>Answer</summary>

**B. Implement Amazon CloudFront with the application origin, and enable edge caching with an appropriate TTL for the static API responses. Increase the compute capacity (EC2 instance size) in the primary region to handle all global traffic more quickly.**

Amazon CloudFront is a global Content Delivery Network (CDN) that caches static and dynamic content at edge locations worldwide. Because the API responses are mostly static and change infrequently, caching them at the edge using an appropriate Time to Live (TTL) significantly reduces latency for global users by serving requests from the nearest edge location. This approach directly addresses the slow response times during peak hours by offloading traffic from the origin servers. It is the most cost-effective and efficient solution because it requires no core application redesign while simultaneously solving both the geographic latency and peak-load capacity issues. Why Incorrect Options are Wrong: A: Deploying the application across multiple regions introduces significant architectural complexity, data synchronization challenges, and operational overhead, violating the constraint to avoi

</details>

### 232. dt-526

Identify a true statement about the On-Demand instances purchasing option provided by Amazon EC2.

<details><summary>Answer</summary>

**A. Pay for the instances that you use by the hour, with no long-term commitments or up-front payments.**

</details>

### 233. q-527

How can trade data from DynamoDB be ingested into an S3 data lake for near real-time analysis?

<details><summary>Answer</summary>

**B. Use DynamoDB Streams to invoke a Lambda function that writes to Data Firehose, which writes to S3.**

This architecture leverages DynamoDB Streams to capture item-level changes in near real-time. A Lambda function, acting as a stream consumer, is triggered by these changes. The function's role is simplified to forwarding the data to a Kinesis Data Firehose delivery stream. Firehose then reliably handles the buffering, optional data transformation (e.g., to Parquet), and batch delivery to the S3 data lake. This pattern is highly scalable, serverless, and offloads the complexity of S3 delivery to a managed service, making it a robust and efficient solution for near real-time ingestion. It also provides a flexible integration point in Lambda for future data transformation needs. Why Incorrect Options are Wrong: A. This approach requires complex custom Lambda code to manage batching, error handling, and file optimization for S3, which is less robust than using the purpose-built Kinesis Data

</details>

### 234. q-527

A company has a regional subscription-based streaming service that runs in a single AWS Region. The architecture consists of web servers and application servers on Amazon EC2 instances. The EC2 instances are in Auto Scaling groups behind Elastic Load Balancers. The architecture includes an Amazon Aurora global database cluster that extends across multiple Availability Zones. The company wants to expand globally and to ensure that its application has minimal downtime. Which solution will provide the MOST fault tolerance?

<details><summary>Answer</summary>

**D. Deploy the web tier and the application tier to a second Region. Use an Amazon Aurora global database to deploy the database in the primary Region and the second Region. Use Amazon Route 53 health checks with a failover routing policy to the second Region. Promote the secondary to primary as needed.**

An Aurora global database allows you to replicate your database across multiple AWS Regions. This ensures that you have a read-capable secondary database in the second Region, providing low-latency access to the database. Amazon Route 53 can be configured with health checks to monitor the health of the web and application tiers in both Regions. In the event of a failure in the primary Region, Route 53 can automatically route traffic to the healthy resources in the second Region.

</details>

### 235. dt-530

Can I change the EC2 security groups after an instance is launched in EC2-Classic?

<details><summary>Answer</summary>

**B. No, you cannot change security groups after you launch an instance in EC2-Classic.**

</details>

### 236. dt-531

Please select the Amazon EC2 resource which cannot be tagged.

<details><summary>Answer</summary>

**C. Elastic IP addresses.**

</details>

### 237. q-533

A company has developed an API using an Amazon API Gateway REST API and AWS Lambda functions. The API serves static and dynamic content to users worldwide. The company wants to decrease the latency of transferring content for API requests. Options:

<details><summary>Answer</summary>

**A. Deploy the REST API as an edge-optimized API endpoint. Enable caching. Enable content encoding in the API definition to compress the application data in transit.**

To decrease latency for a global user base, an edge-optimized API endpoint is the best choice. This endpoint type leverages the Amazon CloudFront content delivery network (CDN) to route requests to the nearest edge location, minimizing network latency. Enabling API caching serves frequently requested data from the cache at the edge, further reducing latency by avoiding calls to the backend Lambda function. Additionally, enabling content encoding compresses the API payload, which reduces the amount of data transferred over the network. This smaller payload size decreases transfer time, directly contributing to lower overall latency for the end-user. Why Incorrect Options are Wrong: B. A Regional API endpoint is not suitable for a global user base as it does not use the CloudFront CDN, leading to higher latency for users geographically distant from the deployment region. C. Reserved concur

</details>

### 238. q-534

A company has developed an API by using an Amazon API Gateway REST API and AWS Lambda functions. The API serves static content and dynamic content to users worldwide. The company wants to decrease the latency of transferring the content for API requests. Which solution will meet these requirements?

<details><summary>Answer</summary>

**Transition objects to an S3 infrequent-access storage class 30 days after creation, and write an expiration action that directs Amazon S3 to delete objects after 90 days - with no Glacier transition. Where S3 One Zone-Infrequent Access is offered, it is the cheapest valid choice, because high availability is only required for the first 30 days and the remaining 60 days are backup only; if One Zone-IA is not among the options, S3 Standard-Infrequent Access is the correct pick.**

The logs need frequent, highly available access for 30 days, so they stay in S3 Standard for that period. From day 30 to day 90 they are held only for backup, so an infrequent-access class costs less per GB, and One Zone-IA is cheaper still once the high-availability requirement has lapsed. Because everything is deleted at day 90, an expiration action at 90 days is all that is needed, and a Glacier transition on the same day is wasted: expiration wins over a same-day transition, and Glacier Flexible Retrieval would in any case bill a 90-day minimum for objects that no longer exist. Adding the Glacier step therefore raises cost and complexity without meeting any stated requirement.

</details>

### 239. dt-535

What does the following policy for Amazon EC2 do? { 'Statement':[{ 'Effect': 'Allow', 'Action':'ec2: Describe*', 'Resource':'*' }] }

<details><summary>Answer</summary>

**A. Allow users to use actions that start with 'Describe' over all the EC2 resources.**

</details>

### 240. dt-538

In Amazon Elastic Compute Cloud, which of the following is used for communication between instances in the same network (EC2-Classic or a VPC)?

<details><summary>Answer</summary>

**A. Private IP addresses.**

</details>

### 241. q-539 `least-ops`

A company provides a trading platform to customers. The platform uses an Amazon API Gateway REST API, AWS Lambda functions, and an Amazon DynamoDB table. Each trade that the platform processes invokes a Lambda function that stores the trade data in Amazon DynamoDB. The company wants to ingest trade data into a data lake in Amazon S3 for near real-time analysis. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon DynamoDB Streams to capture the trade data changes. Configure DynamoDB Streams to invoke a Lambda function that writes the data to Amazon S3.**

The most efficient solution with the least operational overhead is to use Amazon DynamoDB Streams to capture item-level changes in the DynamoDB table. A stream is an ordered flow of information about changes to items. This stream can be configured to trigger an AWS Lambda function in near real-time for each modification event. The Lambda function can then process these events and write the trade data directly to an Amazon S3 bucket. This architecture is fully serverless, requires no management of servers or stream shards, and automatically scales with the volume of trades, perfectly aligning with the requirement for minimal operational overhead. Why Incorrect Options are Wrong: B: This option adds Amazon Data Firehose, which is an unnecessary component. The Lambda function can write directly to S3, so inserting Firehose adds complexity and configuration overhead without providing a signi

</details>

### 242. dt-539

A user is planning to host a mobile game on EC2 which sends notifications to active users on either high score or the addition of new features. The user should get this notification when he is online on his mobile device. Which of the below mentioned AWS services can help achieve this functionality?

<details><summary>Answer</summary>

**A. AWS Simple Notification Service.**

</details>

### 243. dt-540

You need to create an Amazon Machine Image (AMI) for a customer for an application which does not appear to be part of the standard AWS AMI template that you can see in the AWS console. What are the alternative possibilities for creating an AMI on AWS?

<details><summary>Answer</summary>

**B. You can purchase an AMIs from a third party or can create your own AMI.**

</details>

### 244. q-542

A company runs a containerized application on a Kubernetes cluster in an on-premises data center. The company is using a MongoDB database for data storage. The company wants to migrate some of these environments to AWS, but no code changes or deployment method changes are possible at this time. The company needs a solution that minimizes operational overhead.

<details><summary>Answer</summary>

**D. Use Amazon Elastic Kubernetes Service (Amazon EKS) with AWS Fargate for compute and Amazon DocumentDB (with MongoDB compatibility) for data storage.**

The solution must accommodate an existing Kubernetes application using MongoDB without code or deployment changes, while minimizing operational overhead. 1. Compute: Amazon Elastic Kubernetes Service (Amazon EKS) is the appropriate managed service for migrating Kubernetes workloads, satisfying the "no deployment method changes" requirement. Using AWS Fargate with EKS provides serverless compute, which abstracts away server management and directly addresses the need to minimize operational overhead. 2. Database: Amazon DocumentDB is a managed database service with MongoDB compatibility. This allows the application to connect to the new database without requiring code changes, fulfilling a critical constraint. As a fully managed service, it also minimizes database administration overhead. Why Incorrect Options are Wrong: A. Amazon ECS is not Kubernetes, which would require changing deploym

</details>

### 245. q-548

A company has an application that receives and processes purchase orders. The application supports only XML dat a. The company needs to configure the application to accept orders in JSON format. The company does not want to modify the application. A solutions architect is using an Amazon API Gateway HTTP API to create a new purchase order API. The solutions architect needs to modify the application DNS record to point to the new HTTP API.

<details><summary>Answer</summary>

**B. Use an HTTP proxy integration to pass XML requests to the application. For JSON requests, use an AWS Lambda function that is integrated with API Gateway to convert the purchase orders from JSON to XML and to call the application.**

This solution correctly addresses the two distinct requirements using the features of an Amazon API Gateway HTTP API. For existing XML requests, an HTTP proxy integration is the most efficient method. It forwards the original request, including the body, headers, and methods, directly to the backend application without modification. For new JSON requests, a Lambda integration is required. The Lambda function acts as a transformation layer, converting the incoming JSON payload into the XML format that the backend application expects before invoking the application endpoint. This approach meets all requirements without modifying the original application. Why Incorrect Options are Wrong: A: API Gateway HTTP APIs do not have the advanced mapping template capabilities (like VTL in REST APIs) to perform complex body transformations such as converting JSON to XML. C: This option is incorrect fo

</details>

### 246. q-550

A company is migrating an online marketplace application from a mainframe system to an Auto Scaling group of Amazon EC2 instances. The EC2 instances access an Amazon Aurora cluster. The application requires a scalable, persistent caching solution to store the results of in-progress transactions and SQL queries.

<details><summary>Answer</summary>

**A. Use an Amazon ElastiCache (Redis OSS) cluster to serve transaction and query results.**

The core requirements are for a scalable and persistent caching solution that is shared among multiple EC2 instances. Amazon ElastiCache for Redis OSS is the ideal choice as it is a managed, scalable in-memory data store that supports data persistence. Redis can persist data to disk through snapshots and Append Only Files (AOF), ensuring that cached data like transaction results is not lost during node failures or restarts. This single, centralized service can effectively cache both in-progress transactions and SQL query results for all instances in the Auto Scaling group, meeting all the application's requirements. Why Incorrect Options are Wrong: B: Amazon CloudFront is a content delivery network (CDN) for web content, not an application-level transaction cache. EC2 instance stores are ephemeral and lose data upon instance termination, violating the persistence requirement. C: Amazon E

</details>

### 247. dt-551

Can I move a Reserved Instance from one Region to another?

<details><summary>Answer</summary>

**A. No.**

</details>

### 248. q-552

A company needs to optimize the cost of its Amazon EC2 instances. The company also needs to change the type and family of its EC2 instances every 2-3 months. What should the company do to meet these requirements?

<details><summary>Answer</summary>

**B. Purchase a No Upfront Compute Savings Plan for a 1-year term.**

WHat is Upfront --- You don't pay anything upfront. You receive a smaller discount, but you free up capital for other projects.  A No Upfront option means no upfront payment is required, which provides flexibility.  1-year Term: A 1-year term aligns with the company's need to change the type and family of its EC2 instances every 2-3 months. While Compute Savings Plans have a commitment term, choosing a 1-year term allows for more frequent adjustments compared to a 3-year term.

</details>

### 249. q-557 `least-ops`

A company wants to design a microservices architecture for an application. Each microservice must perform operations that can be completed within 30 seconds. The microservices need to expose RESTful APIs and must automatically scale in response to varying loads. The APIs must also provide client access control and rate limiting to maintain equitable usage and service availability. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Deploy each microservice as a set of AWS Lambda functions. Use Amazon API Gateway to manage the RESTful API requests.**

The combination of AWS Lambda and Amazon API Gateway provides a fully serverless solution that directly meets all the requirements with the least operational overhead. Lambda functions are ideal for short-running operations (well under the 30-second requirement) and scale automatically based on demand without any server management. Amazon API Gateway acts as a fully managed "front door" for the Lambda functions, providing essential features for creating RESTful APIs, including client access control (e.g., IAM, Cognito, API Keys) and rate limiting through usage plans and throttling. This architecture eliminates the need to provision, patch, or manage servers, minimizing operational tasks. Why Incorrect Options are Wrong: A. Using Amazon ECS on EC2 requires managing the underlying EC2 instances (OS patching, security), which incurs more operational overhead than the serverless Lambda model

</details>

### 250. q-558 `least-ops`

A company currently runs a Linux-based application in a self-managed Docker container that runs on Amazon EC2 instances. The application runs a lightweight data processing tool that always completes its job within 3 minutes. The company wants an alternative deployment solution for the application to reduce infrastructure management overhead. The company is willing to make any required changes to the image. Which solution will meet this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Deploy the application as an AWS Lambda function that uses the container image.**

Deploying the application as an AWS Lambda function using a container image is the solution with the least operational overhead. Lambda is a serverless compute service, which means AWS manages the entire underlying infrastructure, including servers, patching, and scaling. The developer only needs to provide the code or container image. Since the job completes within 3 minutes, it fits well within Lambda's 15-minute maximum execution time. This approach completely eliminates the need to manage clusters, task definitions, or virtual servers, directly addressing the goal of reducing infrastructure management. Why Incorrect Options are Wrong: B. Amazon EKS with Fargate still requires management of Kubernetes clusters, services, and deployments, which is more operational overhead than Lambda. C. Amazon ECS with Fargate removes server management but still requires managing ECS clusters, servic

</details>

### 251. dt-558

You have been doing a lot of testing of your VPC Network by deliberately failing EC2 instances to test whether instances are failing over properly. Your customer who will be paying the AWS bill for all this asks you if he being charged for all these instances. You try to explain to him how the billing works on EC2 instances to the best of your knowledge. What would be an appropriate response to give to the customer in regards to this?

<details><summary>Answer</summary>

**C. Billing commences when Amazon EC2 initiates the boot sequence of an AMI instance and billing ends when the instance shuts down.**

</details>

### 252. dt-559

Refer to the architecture diagram above of a batch processing solution using Simple Queue Service (SQS) to set up a message queue between EC2 instances which are used as batch processors Cloud Watch monitors the number of Job requests (queued messages) and an Auto Scaling group adds or deletes batch servers automatically based on parameters set in Cloud Watch alarms. You can use this architecture to implement which of the following features in a cost effective and efficient manner?

<details><summary>Answer</summary>

**C. Implement message passing between EC2 instances within a batch by exchanging messages through SQS.**

</details>

### 253. q-559

A company hosts multiple applications on AWS for different product lines. The applications use different compute resources, including Amazon EC2 instances and Application Load Balancers. The applications run in different AWS accounts under the same organization in AWS Organizations across multiple AWS Regions. Teams for each product line have tagged each compute resource in the individual accounts. The company wants more details about the cost for each product line from the consolidated billing feature in Organizations. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Select a specific user-defined tag in the AWS Billing console.**

E. Activate the selected tag from the Organizations management account.  User-defined tags are tags that you create and attach to your AWS resources. In this case, since teams for each product line have tagged each compute resource with user-defined tags, selecting a specific user-defined tag in the AWS Billing console allows you to filter costs based on those tags.  The consolidated billing feature in AWS Organizations allows you to view and manage costs across multiple AWS accounts. By activating the selected tag from the Organizations management account, you ensure that the tagged resources from all linked accounts are included in the consolidated billing report. This enables you to get detailed cost information for each product line.

</details>

### 254. gh-559

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

### 255. q-560

A company has a legacy mainframe system that can retrieve data only from systems that provide synchronous RESTful APIs. A developer at the company creates a new web service to calculate stock prices. The new web service takes 3 minutes on average to process each request. The developer must integrate the new web service with the legacy mainframe system. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a URL for an AWS Lambda function. Configure the legacy mainframe to use the Lambda function URL endpoint.**

The core requirement is to handle a synchronous API call that takes 3 minutes (180 seconds) to process. Amazon API Gateway REST and HTTP APIs have a maximum integration timeout of 29 and 30 seconds, respectively. Therefore, any solution using API Gateway for a synchronous integration will fail with a timeout error. AWS Lambda functions, however, can have a maximum execution time of 15 minutes (900 seconds). A Lambda function URL provides a direct HTTPS endpoint for a Lambda function and inherits the function's configured timeout. This is the only option that can handle a 3-minute synchronous request. Why Incorrect Options are Wrong: A. An Amazon API Gateway REST API has a maximum integration timeout of 29 seconds, which is too short for the 3-minute processing time, causing the request to fail. B. An Amazon API Gateway HTTP API has a maximum integration timeout of 30 seconds, which is al

</details>

### 256. q-561

A company has a serverless web application that is comprised of AWS Lambda functions. The application experiences spikes in traffic that cause increased latency because of cold starts. The company wants to improve the application's ability to handle traffic spikes and to minimize latency. The solution must optimize costs during periods when traffic is low. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure provisioned concurrency for the Lambda functions. Use AWS Application Auto Scaling to adjust the provisioned concurrency.**

The question requires a solution to mitigate AWS Lambda cold start latency during traffic spikes while optimizing costs during low traffic periods. Provisioned Concurrency is the specific Lambda feature designed to address this by keeping a configured number of execution environments initialized and ready to respond instantly. This eliminates cold start latency. Combining this with AWS Application Auto Scaling allows the level of provisioned concurrency to be adjusted dynamically based on traffic demand. This ensures that enough functions are warm during spikes and that the company is not over-provisioning (and over-paying) during periods of low traffic, thereby meeting both the performance and cost-optimization requirements. Why Incorrect Options are Wrong: B. This option proposes migrating from a serverless Lambda architecture to a server-based EC2 architecture, which does not address

</details>

### 257. dt-562

Which of the following strategies can be used to control access to your Amazon EC2 instances?

<details><summary>Answer</summary>

**D. EC2 security groups.**

</details>

### 258. q-562

A solutions architect needs to ensure that API calls to Amazon DynamoDB from Amazon EC2 instances in a VPC do not travel across the internet. Which combination of steps should the solutions architect take to meet this requirement? (Choose two.)

<details><summary>Answer</summary>

**A. Create a route table entry for the endpoint.**

B. Create a gateway endpoint for DynamoDB.

</details>

### 259. gh-563 `least-ops`

clusters and workloads from a central location.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Use Amazon EKS Connector to register and connect the Kubernetes clusters that run outside Amazon EKS, so every cluster can be seen and managed from the EKS console.**

EKS Connector installs a small agent into a Kubernetes cluster that AWS does not run - on premises, self-managed on EC2, or on another cloud provider - and registers that cluster with Amazon EKS, so it appears in the EKS console alongside the native EKS clusters with its nodes and workloads visible. That gives one place to see every cluster without standing up and maintaining a separate management tool, which is the least operational overhead of the options. EKS Anywhere is for running an AWS-supported Kubernetes distribution in your own data centre, and EKS Distro is only the open-source build of Kubernetes that EKS is based on; neither gives a single central view of clusters you already have.

</details>

### 260. dt-565

In Amazon EC2, how many Elastic IP addresses can you have by default?

<details><summary>Answer</summary>

**C. 5.**

</details>

### 261. dt-566

A user has created photo editing software and hosted it on EC2. The software accepts requests from the user about the photo format and resolution and sends a message to S3 to enhance the picture accordingly. Which of the below mentioned AWS services will help make a scalable software with the AWS infrastructure in this scenario?

<details><summary>Answer</summary>

**B. AWS Simple Queue Service.**

</details>

### 262. dt-569

A user is running a webserver on EC2. The user wants to receive the SMS when the EC2 instance utilization is above the threshold limit. Which AWS services should the user configure in this case?

<details><summary>Answer</summary>

**B. AWS CloudWatch + AWS SNS.**

</details>

### 263. q-570 `least-ops`

A company has a large workload that runs every Friday evening. The workload runs on Amazon EC2 instances that are in two Availability Zones in the us-east-1 Region. Normally, the company must run no more than two instances at all times. However, the company wants to scale up to six instances each Friday to handle a regularly repeating increased workload. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Auto Scaling group that has a scheduled action.**

By creating an Auto Scaling group with a scheduled action, you can configure the group to automatically adjust the desired capacity based on a specified schedule. In this case, you can set up a scheduled action to increase the desired capacity to six instances every Friday evening.

</details>

### 264. dt-575 `cost`

You are designing a multi-platform web application for AWS. The application will run on EC2 instances and will be accessed from PCs, tablets and smart phones. Supported accessing platforms are Windows, macOS, iOS and Android. Separate sticky session and SSL certificate setups are required for different platform types. Which of the following describes the most cost effective and performance efficient architecture setup?

<details><summary>Answer</summary>

**D. Assign multiple ELBs to an EC2 instance or group of EC2 instances running the common components of the web application, one ELB for each platform type. Session stickiness and SSL termination are done at the ELBs.**

</details>

### 265. q-576 `cost`

A company hosts a public web application on AWS. The website has a three-tier architecture. The frontend web tier is comprised of Amazon EC2 instances in an Auto Scaling group. The application tier is a second Auto Scaling group. The database tier is an Amazon RDS database. The company has configured the Auto Scaling groups to handle the application's normal level of demand. During an unexpected spike in demand, the company notices a long delay in the startup time when the frontend and application layers scale out. The company needs to improve the scaling performance of the application without negatively affecting the user experience. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**An edge-optimized API endpoint.**

With an edge-optimized endpoint, API Gateway puts a CloudFront distribution that it manages in front of your API, so a request from a geographically distant user enters the AWS network at the nearest edge location and travels the rest of the way over the AWS backbone instead of the public internet. That cuts the latency of connection setup and transit for scattered users, which is what the requirement asks for. A regional endpoint sends clients straight to the API in its own region and is the better choice when callers are in that same region or when you want to run your own CloudFront distribution; a private endpoint is reachable only from inside a VPC.

</details>

### 266. q-583

A solutions architect manages a web application for a company. The application runs on Amazon EC2 instances in an Auto Scaling group. The Auto Scaling group configuration includes a minimum of 3 instances and a maximum of 300 instances. The maximum helps handle unpredictable, short-lived traffic surges. The application must scale to meet demand. However, to help manage costs, the number of running instances should not exceed 180 for longer than 1 continuous hour. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Add a step scaling policy that uses an Amazon CloudWatch alarm. Trigger the alarm when the Auto Scaling group includes more than 180 instances for longer than 1 hour. Configure the alarm to reduce the group capacity to 180 when triggered.**

The requirement is to allow scaling up to 300 instances for short-lived surges but reduce capacity to 180 if the high load persists for over an hour. A step scaling policy triggered by a custom Amazon CloudWatch alarm is the ideal solution. The alarm can monitor the GroupInServiceInstances metric for the Auto Scaling group. If this metric's value is greater than 180 for a continuous period of one hour, the alarm will trigger. The associated step scaling policy can then be configured to reduce the group's maximum and desired capacity to 180, meeting the cost management requirement without preventing necessary short-term scaling. Why Incorrect Options are Wrong: A. Scheduled scaling is for predictable traffic patterns, not the unpredictable surges described in the scenario. B. Terminating instances directly via a CloudWatch alarm is an abrupt action that bypasses Auto Scaling's managed sca

</details>

### 267. dt-583

A company has a workflow that sends video files from their on-premise system to AWS for transcoding. They use EC2 worker instances that pull transcoding jobs from SQS. Why is SQS an appropriate service for this scenario?

<details><summary>Answer</summary>

**D. SQS helps to facilitate horizontal scaling of encoding tasks.**

</details>

### 268. q-584

A company is deploying an application that processes large quantities of data in parallel. The company plans to use Amazon EC2 instances for the workload. The network architecture must be configurable to prevent groups of nodes from sharing the same underlying hardware. Which networking solution meets these requirements?

<details><summary>Answer</summary>

**A. Run the EC2 instances in a spread placement group.**

A spread placement group is a logical grouping of instances that are placed on distinct underlying hardware. This ensures that instances within the group are physically separated, reducing the risk of correlated failures. This option is suitable for applications that need to maximize the level of isolation.

</details>

### 269. q-585

A company has an application with a REST-based interface that allows data to be received in near- real time from a third-party vendor. Once received, the application processes and stores the data for further analysis. The application is running on Amazon EC2 instances. The third-party vendor has received many 503 Service Unavailable Errors when sending data to the application. When the data volume spikes, the compute capacity reaches its maximum limit and the application is unable to process all requests. Which design should a solutions architect recommend to provide a more scalable solution?

<details><summary>Answer</summary>

**D. Purchase a Capacity Reservation in the failover Region.**

An On-Demand Capacity Reservation holds EC2 capacity for your account in one Availability Zone for a stated instance type, platform and tenancy, and that capacity stays held whether or not you have instances running in it, so it is there when you declare a disaster and fail over. Because it is pinned that tightly, you must create the reservation for the exact instance types and the exact AZ your DR plan will launch into, and you pay the On-Demand rate for the reserved capacity for as long as it exists. The key distinction the question is testing: Savings Plans and regional Reserved Instances are billing discounts and reserve no capacity at all, so they cannot guarantee a failover launch will succeed. If you want the discount as well, a Capacity Reservation can be combined with a Savings Plan or a Reserved Instance, which then applies to the reserved capacity's charges.

</details>

### 270. q-586

A company has an industrial application that controls a process in real time. The company plans to rearchitect the application to distribute jobs across several Amazon EC2 instances in a VPC. The solution needs to maximize the network throughput and minimize the network latency between the instances.

<details><summary>Answer</summary>

**D. Place the instances in a cluster placement group. Choose instance types that support enhanced networking.**

A cluster placement group is the only strategy that logically groups instances within a single Availability Zone, placing them in close physical proximity on the same rack. This architecture is specifically designed to minimize network latency and maximize throughput between instances, making it ideal for tightly-coupled, real-time applications like the one described. Combining this with instance types that support enhanced networking ensures the highest possible packet per second (PPS) performance and the lowest network jitter, directly addressing the core requirements of the scenario. Why Incorrect Options are Wrong: A: Partition placement groups are designed for high availability by spreading instances across different hardware racks, which inherently increases inter-instance network latency. B: Using a partition placement group is counterproductive for low-latency requirements, as it

</details>

### 271. dt-586

What does Amazon EC2 provide?

<details><summary>Answer</summary>

**A. Virtual servers in the Cloud.**

</details>

### 272. q-589

A genomics research company is designing a scalable architecture for a loosely coupled workload. Tasks in the workload are independent and can be processed in parallel. The architecture needs to minimize management overhead and provide automatic scaling based on demand. Options:

<details><summary>Answer</summary>

**B. Implement a serverless architecture that uses AWS Lambda functions.**

The scenario requires an architecture for a loosely coupled workload with independent, parallel tasks, prioritizing automatic scaling and minimal management overhead. A serverless architecture using AWS Lambda is the ideal solution. Lambda functions are invoked for each task, automatically scaling in parallel to meet demand without requiring any server provisioning or management. This model directly addresses the core requirements by abstracting away the underlying infrastructure, which significantly minimizes operational overhead and aligns perfectly with event-driven, parallel processing needs common in genomics data analysis. Why Incorrect Options are Wrong: A. A cluster of EC2 instances requires significant management for the OS, software, and scaling policies, which contradicts the "minimize management overhead" requirement. C. AWS ParallelCluster is designed for tightly coupled Hig

</details>

### 273. q-591

An ecommerce company hosts an API that handles sales requests. The company hosts the API frontend on Amazon EC2 instances that run behind an Application Load Balancer (ALB). The company hosts the API backend on EC2 instances that perform the transactions. The backend tiers are loosely coupled by an Amazon Simple Queue Service (Amazon SQS) queue. The company anticipates a significant increase in request volume during a new product launch event. The company wants to ensure that the API can handle increased loads successfully. Options:

<details><summary>Answer</summary>

**D. Place the frontend and backend EC2 instances into separate Auto Scaling groups. Create a policy for the frontend Auto Scaling group to launch instances based on incoming network traffic. Create a policy for the backend Auto Scaling group to launch instances based on the SQS queue backlog.**

This solution provides a comprehensive and elastic approach for the decoupled, two-tier architecture. Placing both the frontend and backend EC2 instances into separate Auto Scaling groups allows each tier to scale independently based on its specific workload. The frontend tier's load is directly related to incoming user requests, making network traffic an appropriate scaling metric. The backend tier's workload is determined by the number of messages in the Amazon SQS queue. Scaling the backend based on the queue backlog (e.g., using the ApproximateNumberOfMessagesVisible metric) is the standard and most efficient method. This ensures that processing capacity dynamically matches the number of queued transactions, preventing bottlenecks. Why Incorrect Options are Wrong: A. Manually doubling instances is static provisioning, not elastic scaling. It is inefficient and risks being either insu

</details>

### 274. q-594

A company plans to migrate to AWS and use Amazon EC2 On-Demand Instances for its application. During the migration testing phase, a technical team observes that the application takes a long time to launch and load memory to become fully productive. Which solution will reduce the launch time of the application during the next testing phase?

<details><summary>Answer</summary>

**C. Launch the EC2 On-Demand Instances with hibernation turned on. Configure EC2 Auto Scaling warm pools during the next testing phase.**

When you launch EC2 On-Demand Instances with hibernation turned on, the instances can be hibernated and resumed rather than terminated and launched.

</details>

### 275. q-595 `cost`

A company's applications run on Amazon EC2 instances in Auto Scaling groups. The company notices that its applications experience sudden traffic increases on random days of the week. The company wants to maintain application performance during sudden traffic increases. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Use dynamic scaling to change the size of the Auto Scaling group.**

Dynamic Scaling: With dynamic scaling, the Auto Scaling group automatically adjusts its capacity based on real-time demand. It scales out during traffic spikes and scales in during periods of lower demand. This ensures that your application can handle sudden increases in traffic without manual intervention.

</details>

### 276. q-597

An ecommerce company is launching a new marketing campaign. The company anticipates the campaign to generate ten times the normal number of daily orders through the company's ecommerce application. The campaign will last 3 days. The ecommerce application architecture is based on Amazon EC2 instances in an Auto Scaling group and an Amazon RDS for MySQL database. The application writes order transactions to an Amazon Elastic File System (Amazon EFS) file system before the application writes orders to the database. During normal operations, the application write operations peak at 5,000 IOPS. A solutions architect needs to ensure that the application can handle the anticipated workload during the marketing campaign. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. For the duration of the campaign, increase the provisioned IOPS for the RDS for MySQL database. Set the Amazon EFS throughput mode to Elastic throughput.**

The scenario requires scaling both the database and the file system to handle a temporary but significant (10x) increase in write operations. 1. Amazon RDS: The database is a critical bottleneck for write-intensive operations. Increasing the Provisioned IOPS (PIOPS) for the RDS instance is the direct and most effective way to scale its I/O capacity to handle the anticipated 50,000 IOPS (5,000 IOPS x 10). 2. Amazon EFS: The application writes to EFS first. For a spiky and unpredictable workload like a marketing campaign, Elastic throughput is the ideal mode. It automatically scales throughput performance up or down based on the application's needs, ensuring performance without manual intervention or the risk of depleting burst credits, which would likely occur with Bursting throughput mode under a sustained 10x load. Why Incorrect Options are Wrong: A. EFS Bursting throughput is not suita

</details>

### 277. q-597

A company hosts an internal serverless application on AWS by using Amazon API Gateway and AWS Lambda. The company’s employees report issues with high latency when they begin using the application each day. The company wants to reduce latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up a scheduled scaling to increase Lambda provisioned concurrency before employees begin to use the application each day.**

Lambda Provisioned Concurrency: Provisioned concurrency is the number of simultaneous executions that your function can handle. By setting up a scheduled scaling to increase Lambda provisioned concurrency before employees begin using the application, you are proactively ensuring that there are enough resources available to handle the expected load.

</details>

### 278. dt-602

How many types of block devices does Amazon EC2 support?

<details><summary>Answer</summary>

**C. 2.**

</details>

### 279. q-608

A company is deploying an application that processes streaming data in near-real time. The company plans to use Amazon EC2 instances for the workload. The network architecture must be configurable to provide the lowest possible latency between nodes. Which networking solution meets these requirements?

<details><summary>Answer</summary>

**B. Attach an Elastic Fabric Adapter (EFA) to each EC2 instance.**

An Elastic Fabric Adapter (EFA) is a network interface for Amazon EC2 instances that enables customers to run applications requiring high levels of inter-node communication at scale on AWS. EFA's custom-built OS-bypass hardware interface enhances inter-instance communications by allowing the application to communicate directly with the network interface. This reduces latency and makes it ideal for tightly coupled workloads like High Performance Computing (HPC) and streaming data analysis, which demand the lowest possible latency between nodes. Why Incorrect Options are Wrong: A. VPC peering connects VPCs, but it does not provide the specialized low-latency, high-throughput network fabric that EFA offers for communication within a workload. C. A spread placement group is designed for high availability by placing instances on distinct underlying hardware, which can increase inter-node late

</details>

### 280. q-615

A company runs a critical, customer-facing application on Amazon Elastic Kubernetes Service (Amazon EKS). The application has a microservices architecture. The company needs to implement a solution that collects, aggregates, and summarizes metrics and logs from the application in a centralized location. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Configure Amazon CloudWatch Container Insights in the existing EKS cluster. View the metrics and logs in the CloudWatch console.**

CloudWatch Container Insights is specifically designed for monitoring containerized applications on Amazon EKS and ECS. It provides visibility into the performance of containers, clusters, and microservices.

</details>

### 281. dt-617

A web-startup runs its very successful social news application on Amazon EC2 with an Elastic Load Balancer, an Auto-Scaling group of Java/Tomcat application-servers, and DynamoDB as data store. The main web-application best runs on m2 x large instances since it is highly memory- bound Each new deployment requires semi-automated creation and testing of a new AMI for the application servers which takes quite a while and is therefore only done once per week. Recently, a new chat feature has been implemented in nodejs and waits to be integrated in the architecture. First tests show that the new component is CPU bound Because the company has some experience with using Chef, they decided to streamline the deployment process and use AWS OpsWorks as an application life cycle tool to simplify management of the application and reduce the deployment cycles. What configuration in AWS OpsWorks is necessary to integrate the new chat module in the most cost-efficient and flexible way?

<details><summary>Answer</summary>

**C. Create two AWS OpsWorks stacks create two AWS OpsWorks layers create one custom recipe.**

</details>

### 282. dt-619

A user is currently building a website which will require a large number of instances in six months, when a demonstration of the new site will be given upon launch. Which of the below mentioned options allows the user to procure the resources beforehand so that they need not worry about infrastructure availability during the demonstration?

<details><summary>Answer</summary>

**A. Procure all the instances as reserved instances beforehand.**

</details>

### 283. dt-624

To help you manage your Amazon EC2 instances, images, and other Amazon EC2 resources, you can assign your own metadata to each resource in the form of [...].

<details><summary>Answer</summary>

**C. tags.**

</details>

### 284. dt-626

If I write the below command, what does it do? ec2-run ami-e3a5408a -n 20 -g appserver

<details><summary>Answer</summary>

**A. Start twenty instances as members of appserver group.**

</details>

### 285. dt-628

In order to optimize performance for a compute cluster that requires low inter-node latency, which of the following feature should you use?

<details><summary>Answer</summary>

**D. Placement Groups.**

</details>

### 286. q-629

A company runs multiple web applications on Amazon EC2 instances behind a single Application Load Balancer (ALB). The application experiences unpredictable traffic spikes throughout each day. The traffic spikes cause high latency. The unpredictable spikes last less than 3 hours. The company needs a solution to resolve the latency issue caused by traffic spikes.

<details><summary>Answer</summary>

**A. Use EC2 instances in an Auto Scaling group. Configure the ALB and Auto Scaling group to use a target tracking scaling policy.**

The most effective solution for handling unpredictable traffic spikes and associated latency is to use an Amazon EC2 Auto Scaling group with a dynamic scaling policy. A target tracking scaling policy is ideal for this scenario. It automatically adjusts the number of EC2 instances to keep a specified metric, such as average CPU utilization or the request count per target from the Application Load Balancer (ALB), at a desired level. When traffic spikes, the metric increases, triggering the policy to scale out (add instances), thereby distributing the load and reducing latency. When the spike subsides, it scales in to reduce costs. Why Incorrect Options are Wrong: B: Scheduled scaling is ineffective because the traffic spikes are unpredictable, not recurring at specific times. This policy would fail to respond to traffic outside its predefined schedule. C: This option is incorrect for the s

</details>

### 287. q-630

A company hosts an application in an Amazon EC2 Auto Scaling group. The company has observed that during periods of high demand, new instances take too long to join the Auto Scaling group and serve the increased demand. The company determines that the root cause of the issue is the long boot time of the instances in the Auto Scaling group. The company needs to reduce the time required to launch new instances to respond to demand. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Create a warm pool for the Auto Scaling group. Use the default specification for the warm pool size.**

The core issue is the long boot time for new EC2 instances, which delays their ability to serve traffic during scale-out events. An Amazon EC2 Auto Scaling warm pool is the ideal solution for this scenario. A warm pool maintains a set of pre-initialized EC2 instances that are ready to be put into service quickly. When the Auto Scaling group needs to scale out, it pulls an instance from the warm pool rather than launching a new one from scratch. This bypasses the lengthy boot and configuration process, significantly reducing the time it takes for a new instance to start handling application traffic. Why Incorrect Options are Wrong: A. Increasing the maximum capacity allows the group to scale to a larger size, but it does not decrease the time it takes for each individual instance to launch and become healthy. C. Increasing the health check grace period would have the opposite effect; it w

</details>

### 288. q-630 `cost`

A solutions architect is creating a data processing job that runs once daily and can take up to 2 hours to complete. If the job is interrupted, it has to restart from the beginning. How should the solutions architect address this issue in the MOST cost-effective manner?

<details><summary>Answer</summary>

**C. Use an Amazon Elastic Container Service (Amazon ECS) Fargate task triggered by an Amazon EventBridge scheduled event.**

ECS Fargate is a serverless container service, and it abstracts away the underlying infrastructure. With Fargate, you don't need to manage or provision EC2 instances directly. You can run containers without worrying about the infrastructure, and AWS takes care of scaling and resource allocation.

</details>

### 289. q-633

A company is designing an application to maintain a record of customer orders. The application will generate events. The company wants to use an Amazon EventBridge event bus to send the application's events to an Amazon DynamoDB table. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an EventBridge custom event bus. Create an AWS Lambda function as a target. Configure the Lambda function to forward the customer order data to the DynamoDB table.**

The most appropriate solution is to use a custom event bus for the company's application events, which is a best practice for isolating event sources. Amazon EventBridge cannot directly write to an Amazon DynamoDB table as a target. Therefore, an intermediary service is required. An AWS Lambda function is a standard and efficient target for EventBridge. The Lambda function can be configured to receive the event, parse the customer order data from the event payload, and then use the AWS SDK to perform a PutItem operation to write the record into the specified DynamoDB table. This architecture is a common serverless pattern that is scalable, decoupled, and meets all the stated requirements. Why Incorrect Options are Wrong: A. DynamoDB Streams captures item-level modifications from a DynamoDB table to be processed by other services; it does not write data to the table. C. A partner event bu

</details>

### 290. dt-633

How can you apply more than 100 rules to an Amazon EC2-Classic?

<details><summary>Answer</summary>

**D. You can't add more than 100 rules to security groups for an Amazon EC2 instance.**

</details>

### 291. dt-634

A user has created an ELB with Auto Scaling. Which of the below mentioned offerings from ELB helps the user to stop sending new requests traffic from the load balancer to the EC2 instance when the instance is being deregistered while continuing in-flight requests?

<details><summary>Answer</summary>

**D. ELB connection draining.**

</details>

### 292. q-635 `least-ops`

A company uses Amazon FSx for NetApp ONTAP in its primary AWS Region for CIFS and NFS file shares. Applications that run on Amazon EC2 instances access the file shares. The company needs a storage disaster recovery (DR) solution in a secondary Region. The data that is replicated in the secondary Region needs to be accessed by using the same protocols as the primary Region. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Create an FSx for ONTAP instance in the secondary Region. Use NetApp SnapMirror to replicate data from the primary Region to the secondary Region.**

FSx for ONTAP supports NetApp SnapMirror, which is a robust data replication technology. You can use SnapMirror to replicate data from the primary FSx for ONTAP instance in the primary Region to an FSx for ONTAP instance in the secondary Region.

</details>

### 293. dt-637

A user is launching an EC2 instance in the US East region. Which of the below mentioned options is recommended by AWS with respect to the selection of the Availability Zone?

<details><summary>Answer</summary>

**C. Do not select the AZ; instead let AWS select the AZ.**

</details>

### 294. dt-638

ec2-revoke RevokeSecurityGroup Ingress

<details><summary>Answer</summary>

**C. Removes one or more rules from a security group.**

</details>

### 295. dt-641

A large real-estate brokerage is exploring the option of adding a cost-effective location based alert to their existing mobile application. The application backend infrastructure currently runs on AWS. Users who opt in to this service will receive alerts on their mobile device regarding real-estate offers in proximity to their location. For the alerts to be relevant delivery time needs to be in the low minute count. The existing mobile app has 5 million users across the US. Which one of the following architectural suggestions would you make to the customer?

<details><summary>Answer</summary>

**A. The mobile application will submit its location to a web service endpoint utilizing Elastic Load Balancing and EC2 instances. DynamoDB will be used to store and retrieve relevant offers. EC2 instances will communicate with mobile carriers/device providers to push alerts back to mobile application.**

</details>

### 296. q-642

A company wants to run a gaming application on Amazon EC2 instances that are part of an Auto Scaling group in the AWS Cloud. The application will transmit data by using UDP packets. The company wants to ensure that the application can scale out and in as traffic increases and decreases. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Attach a Network Load Balancer to the Auto Scaling group.**

UDP is a connectionless protocol, and Network Load Balancers (NLB) support UDP, making them suitable for applications that use UDP for transmitting data.

</details>

### 297. dt-644

What is a placement group in Amazon EC2?

<details><summary>Answer</summary>

**A. It is a group of EC2 instances within a single Availability Zone.**

</details>

### 298. q-647

A solutions architect needs to design a solution for a high performance computing (HPC) workload. The solution must include multiple Amazon EC2 instances. Each EC2 instance requires 10 Gbps of bandwidth individually for single-flow traffic. The EC2 instances require an aggregate throughput of 100 Gbps of bandwidth across all EC2 instances. Communication between the EC2 instances must have low latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Place the EC2 instances in a single subnet of a VPC. Configure a cluster placement group. Ensure that the latest Elastic Fabric Adapter (EFA) drivers are installed on the EC2 instances with a supported operating system.**

The question requires a solution for a High Performance Computing (HPC) workload with stringent low-latency and high-throughput requirements. The optimal AWS architecture for this involves co-locating instances for minimal network latency and using a specialized network adapter for high-bandwidth, inter-node communication. A cluster placement group places instances in a single Availability Zone on the same rack, providing the lowest possible latency between them. An Elastic Fabric Adapter (EFA) is a network interface specifically designed for HPC and machine learning. It uses OS-bypass, allowing applications to communicate directly with the network hardware, which significantly reduces latency and provides higher, more consistent throughput compared to standard TCP/IP over an Elastic Network Adapter (ENA). This combination directly addresses all the requirements of the HPC workload. Why

</details>

### 299. q-656

A company is building a web application that serves a content management system. The content management system runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The EC2 instances run in an Auto Scaling group across multiple Availability Zones. Users are constantly adding and updating files, blogs, and other website assets in the content management system. A solutions architect must implement a solution in which all the EC2 instances share up-to-date website content with the least possible lag time.

<details><summary>Answer</summary>

**B. Copy the website assets to an Amazon Elastic File System (Amazon EFS) file system. Configure each EC2 instance to mount the EFS file system locally. Configure the website hosting application to reference the website assets that are stored in the EFS file system.**

The most effective solution is to use Amazon Elastic File System (Amazon EFS). EFS provides a scalable, shared, and POSIX-compliant file system that can be mounted concurrently by multiple EC2 instances across different Availability Zones. When a user updates content on one instance, the changes are written to the central EFS file system and are immediately visible to all other instances. This architecture provides a strongly consistent, low-latency shared storage layer, perfectly aligning with the requirements of a multi-instance content management system and satisfying the need for the "least possible lag time." Why Incorrect Options are Wrong: A. This approach is complex, not fault-tolerant, and creates a single point of failure on the newest instance. It is not a standard or reliable architectural pattern. C. Using Amazon S3 with an hourly sync command introduces significant latency

</details>

### 300. q-657

A company is building a serverless web application that will serve customers globally by using REST API endpoints. The application must minimize latency regardless of the application us-er's geographic location. The initial amount of traffic that the application will handle is un-known.

<details><summary>Answer</summary>

**A. Deploy an Amazon API Gateway REST API with edge-optimized API endpoints for all cus-tomers. Create AWS Lambda functions. Optimize Lambda performance by adjusting the memory settings and configuring provisioned concurrency.**

The most effective solution to minimize latency for a global user base is to use an Amazon API Gateway with an edge-optimized endpoint. This endpoint type leverages the Amazon CloudFront global network of edge locations to serve API requests from the location nearest to the user, significantly reducing round-trip time. AWS Lambda is the appropriate serverless backend for the REST API. To further minimize latency, especially with unknown traffic patterns, configuring provisioned concurrency for Lambda pre-warms execution environments, eliminating cold-start latency for incoming requests. This combination directly addresses all requirements of the scenario. Why Incorrect Options are Wrong: B: Regional API endpoints are designed for clients within the same AWS Region and do not provide low-latency access for a global user base. Reserved concurrency manages scaling limits, but does not reduc

</details>

### 301. q-660

The customers of a finance company request appointments with financial advisors by sending text messages. A web application that runs on Amazon EC2 instances accepts the appointment requests. The text messages are published to an Amazon Simple Queue Service (Amazon SQS) queue through the web application. Another application that runs on EC2 instances then sends meeting invitations and meeting confirmation email messages to the customers. After successful scheduling, this application stores the meeting information in an Amazon DynamoDB database. As the company expands, customers report that their meeting invitations are taking longer to arrive. What should a solutions architect recommend to resolve this issue?

<details><summary>Answer</summary>

**D. Add an Auto Scaling group for the application that sends meeting invitations. Configure the Auto Scaling group to scale based on the depth of the SQS queue.**

The delay in sending meeting invitations indicates that the backend application responsible for processing requests is unable to keep up with the volume of messages being added to the Amazon SQS queue. This creates a processing bottleneck. By placing the EC2 instances that run this application into an Auto Scaling group and configuring a scaling policy based on the SQS queue depth (specifically, the ApproximateNumberOfMessagesVisible metric), the system can automatically add more instances when the queue grows. This increases the parallel processing capacity, reduces the message backlog, and ensures that customer invitations are sent in a timely manner. This is a common and recommended architectural pattern for scaling decoupled workloads. Why Incorrect Options are Wrong: A. DynamoDB Accelerator (DAX) is an in-memory cache that improves DynamoDB read performance. The bottleneck is in mes

</details>

### 302. q-660

A company hosts an application on Amazon EC2 On-Demand Instances in an Auto Scaling group. Application peak hours occur at the same time each day. Application users report slow application performance at the start of peak hours. The application performs normally 2-3 hours after peak hours begin. The company wants to ensure that the application works properly at the start of peak hours. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a scheduled scaling policy for the Auto Scaling group to launch new instances before peak hours.**

Proactively scales instances to handle predictable traffic spikes. Dynamic scaling (Options B/C) reacts too slowly for known peaks.

</details>

### 303. dt-661

A company's near-real-time streaming application is running on AWS. As the data is ingested, a job runs on the data and takes 30 minutes to complete. The workload frequently experiences high latency due to large amounts of incoming data. A solutions architect needs to design a scalable and serverless solution to enhance performance. Which combination of steps should the solutions architect take? (Choose two.)

<details><summary>Answer</summary>

**A. Use Amazon Kinesis Data Firehose to ingest the data.; E. Use AWS Fargate with Amazon Elastic Container Service (Amazon ECS) to process the data.**

</details>

### 304. q-662

A company hosts a web application on an on-premises server that processes incoming requests. Processing time for each request varies from 5 minutes to 20 minutes. The number of requests is growing. The company wants to move the application to AWS. The company wants to update the architecture to scale automatically.

<details><summary>Answer</summary>

**A. Convert the application to a microservices architecture that uses containers. Use Amazon Elastic Container Service (Amazon ECS) with the AWS Fargate launch type to run the containerized web application. Configure Service Auto Scaling. Use an Application Load Balancer to distribute incoming requests.**

The core requirements are to handle long-running processes (up to 20 minutes) and to scale automatically. Option A is the best fit. Amazon ECS with the AWS Fargate launch type is designed to run containerized applications, including those with long-running tasks, without requiring management of the underlying server infrastructure. Service Auto Scaling in ECS can automatically adjust the number of running tasks based on metrics like CPU utilization or request count, directly addressing the need for automatic scaling. An Application Load Balancer is the standard and most effective way to distribute incoming web traffic across the container tasks. This solution is modern, scalable, and resilient. Why Incorrect Options are Wrong: B: This describes vertical scaling (increasing instance size), which is often disruptive and not as elastic or automated as the horizontal scaling (adding more ins

</details>

### 305. gh-664

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

### 306. dt-670

A company hosts its application in the AWS Cloud. The application runs on Amazon EC2 instances behind an Elastic Load Balancer in an Auto Scaling group and with an Amazon DynamoDB table. The company wants to ensure the application can be made available in another AWS Region with minimal downtime. What should a solutions architect do to meet these requirements with the LEAST amount of downtime?

<details><summary>Answer</summary>

**A. Create an Auto Scaling group and a load balancer in the disaster recovery Region. Configure the DynamoDB table as a global table. Configure DNS failover to point to the new disaster recovery Region's load balancer.**

</details>

### 307. gh-671

A company runs its applications on Amazon EC2 instances. The company performs periodic nancial assessments of its AWS costs. The
company recently identi ed unusual spending.
The company needs a solution to prevent unusual spending. The solution must monitor costs and notify responsible stakeholders in the event of
unusual spending.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Create an AWS Cost Anomaly Detection monitor.**

Cost Anomaly Detection applies machine learning to your AWS cost and usage data and raises an alert when spend departs from the learned pattern, naming the service, linked account, cost category or tag the unexpected charges came from. Alerts go to email or to an Amazon SNS topic, either one at a time or as a daily or weekly summary, so the responsible stakeholders hear about it without anyone running a manual review. CloudWatch can also detect anomalies in a metric, but the only billing data it holds is the coarse EstimatedCharges metric in us-east-1, so it cannot break spend down by service or account; AWS Budgets is useful alongside this but fires on thresholds you set yourself rather than on unusual patterns.

</details>

### 308. dt-672 `cost` `availability`

A company hosts an application on Amazon EC2 instances that run in a single Availability Zone. The application is accessible by using the transport layer of the Open Systems Interconnection (OSI) model. The company needs the application architecture to have high availability. Which combination of steps will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**B. Configure a Network Load Balancer in front of the EC2 instances.; D. Create an Auto Scaling group for the EC2 instances. Configure the Auto Scaling group to use multiple Availability Zones. Configure the Auto Scaling group to run application health checks on the instances.**

</details>

### 309. dt-675 `cost`

A company runs an ecommerce application on AWS. Amazon EC2 instances process purchases and store the purchase details in an Amazon Aurora PostgreSQL DB cluster. Customers are experiencing application timeouts during times of peak usage. A solutions architect needs to rearchitect the application so that the application can scale to meet peak usage demands. Which combination of actions will meet these requirements MOST cost-effectively? (Choose two.)

<details><summary>Answer</summary>

**A. Configure an Auto Scaling group of new EC2 instances to retry the purchases until the processing is complete. Update the applications to connect to the DB cluster by using Amazon RDS Proxy.; C. Update the application to send the purchase requests to an Amazon Simple Queue Service (Amazon SQS) queue. Configure an Auto Scaling group of new EC2 instances that read from the SQS queue.**

</details>

### 310. gh-677 `cost`

A company is developing an application that will run on a production Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster
has managed node groups that are provisioned with On-Demand Instances.
The company needs a dedicated EKS cluster for development work. The company will use the development cluster infrequently to test the
resiliency of the application. The EKS cluster must manage all the nodes.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Create an EKS managed node group that contains only Spot Instances.**

Spot Instances are the cheapest way to get EC2 capacity, at a steep discount to On-Demand, and the trade-off - the instance can be reclaimed at short notice - does not matter for a development cluster used occasionally to test how the application copes with failure. EKS managed node groups support Spot capacity directly and handle provisioning, draining on interruption and version upgrades, so the requirement that the cluster manage all the nodes is met. Mixing in On-Demand Instances raises the bill without meeting any stated requirement, and a self-managed Auto Scaling group with bootstrap scripts hands node management back to you.

</details>

### 311. q-678 `least-ops` `availability`

A global ecommerce company is designing a three-tier application on AWS. The application includes a web tier that serves static content. An application tier handles business logic. A database tier stores product information and user data. The application interacts with a relational database. The company needs a highly available application architecture to serve global users with the low latency. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Set up an Amazon CloudFront distribution that uses an Amazon S3 bucket as the origin. Use Amazon Elastic Container Service (Amazon ECS) containers on AWS Fargate to deploy the application tier to each AWS Region where the company operates. Use an Amazon Aurora global database for the database tier.**

This solution comprehensively addresses all requirements with the least operational overhead. Amazon CloudFront serves static content from an S3 origin globally with low latency via its edge network. AWS Fargate provides a serverless compute engine for containers, eliminating the need to manage EC2 instances for the application tier across multiple regions. Amazon Aurora Global Database is a managed relational database designed specifically for globally distributed applications, offering low-latency reads in multiple regions and fast disaster recovery. This combination of managed and serverless services creates a highly available, low-latency global architecture while minimizing administrative tasks. Why Incorrect Options are Wrong: A. This architecture is confined to a single AWS Region, which fails to provide low latency for global users. C. Using EC2 Spot Instances for the application

</details>

### 312. dt-678

A company uses Amazon EC2 instances and AWS Lambda functions to run its application. The company has VPCs with public subnets and private subnets in its AWS account. The EC2 instances run in a private subnet in one of the VPCs. The Lambda functions need direct network access to the EC2 instances for the application to work. The application will run for at least 1 year. The company expects the number of Lambda functions that the application uses to increase during that time. The company wants to maximize its savings on all application resources and to keep network latency between the services low. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Purchase a Compute Savings Plan. Optimize the Lambda functions' duration and memory usage, the number of invocations, and the amount of data that is transferred. Connect the Lambda functions to the private subnet that contains the EC2 instances.**

</details>

### 313. q-680

A company is building a solution to provide customers with an API that accesses financial data. The API backend needs to compute tax data for each request. The company anticipates greater demand to access the data during the last 3 months of each year. A solutions architect needs to design a scalable solution that can meet the regular demand and the peak demand at the end of each year. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy an Amazon API Gateway REST API. Create an AWS Lambda function to perform tax computations. Integrate the Lambda function with the REST API.**

This solution uses a serverless architecture, which is ideal for workloads with variable or unpredictable demand. Amazon API Gateway provides a fully managed, scalable entry point for the API. AWS Lambda offers a serverless compute service that automatically scales in response to the number of incoming requests from API Gateway. This combination ensures that the solution can handle both regular and peak demand without manual intervention or the cost of maintaining idle infrastructure during periods of lower traffic. The pay-per-request model of both services makes this a highly cost-effective and scalable design. Why Incorrect Options are Wrong: A. A single Amazon EC2 instance is not a scalable or highly available solution. It represents a single point of failure and cannot handle significant increases in demand. C. While an Application Load Balancer with EC2 instances is a scalable patt

</details>

### 314. q-684

A company runs container applications by using Amazon Elastic Kubernetes Service (Amazon EKS) and the Kubernetes Horizontal Pod Autoscaler. The workload is not consistent throughout the day. A solutions architect notices that the number of nodes does not automatically scale out when the existing nodes have reached maximum capacity in the cluster, which causes performance issues. Which solution will resolve this issue with the LEAST administrative overhead?

<details><summary>Answer</summary>

**B. Use the Kubernetes Cluster Autoscaler to manage the number of nodes in the cluster.**

The scenario describes a situation where the Horizontal Pod Autoscaler (HPA) is scaling pods, but the underlying EC2 nodes are not scaling to accommodate them. The Kubernetes Cluster Autoscaler is the purpose-built component designed to solve this exact problem. It integrates with the Kubernetes scheduler and the AWS EC2 Auto Scaling group that manages the EKS nodes. When it detects pods that cannot be scheduled due to insufficient resources on existing nodes, it automatically increases the desired capacity of the Auto Scaling group to add new nodes. This is the standard, most efficient, and lowest-overhead method for node autoscaling in EKS. Why Incorrect Options are Wrong: A. This option describes a scaling metric (memory usage) but fails to specify the automated mechanism needed to scale the nodes, which is the core requirement. C. Using a custom AWS Lambda function would require sign

</details>

### 315. q-687 `least-ops`

A company wants to re-architect a large-scale web application to a serverless microservices architecture. The application uses Amazon EC2 instances and is written in Python. The company selected one component of the web application to test as a microservice. The component supports hundreds of requests per second. The company wants to create and test the microservice on an AWS solution that supports Python. The solution must also scale automatically and require minimal infrastructure and minimal operational support. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use an AWS Lambda function that runs custom-developed code.**

The requirements specify a serverless microservices architecture that scales automatically with minimal operational support for a Python application. AWS Lambda is a serverless compute service that runs code in response to events and automatically manages the underlying compute resources. It natively supports Python, scales precisely with the number of requests, and eliminates the need for infrastructure provisioning or management, perfectly aligning with all the stated requirements. Why Incorrect Options are Wrong: A. A Spot Fleet of EC2 instances is not serverless and requires significant operational overhead for managing instances, scaling, and handling interruptions. B. AWS Elastic Beanstalk simplifies deployment but is a PaaS, not a serverless compute service; it still requires management of the underlying environment and EC2 instances. C. Amazon EKS with self-managed EC2 instances

</details>

### 316. dt-688 `least-ops`

A company observes an increase in Amazon EC2 costs in its most recent bill. The billing team notices unwanted vertical scaling of instance types for a couple of EC2 instances. A solutions architect needs to create a graph comparing the last 2 months of EC2 costs and perform an in-depth analysis to identify the root cause of the vertical scaling. How should the solutions architect generate the information with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Cost Explorer's granular filtering feature to perform an in-depth analysis of EC2 costs based on instance types.**

</details>

### 317. q-704

An events company runs a web application on Amazon EKS that uses an Amazon DynamoDB table. The table has 1,000 RCUs and 500 WCUs provisioned. The application uses eventually consistent reads. Traffic is usually low but occasionally spikes. During spikes, DynamoDB throttles requests, causing user-facing errors. What should a solutions architect do to reduce these errors?

<details><summary>Answer</summary>

**A. Change the DynamoDB table to on-demand capacity mode.**

The application experiences throttling during occasional traffic spikes, indicating that the provisioned capacity is insufficient for peak loads but likely excessive during normal, low-traffic periods. DynamoDB on-demand capacity mode is the ideal solution for this scenario. It automatically scales read and write throughput to meet the application's needs without any capacity planning. The application pays per request, which is cost-effective for unpredictable or spiky workloads and completely eliminates throttling errors caused by exceeding provisioned capacity limits. Why Incorrect Options are Wrong: B. DynamoDB does not have "read replicas" like RDS. Global Tables are for multi-region deployments and do not solve single-region capacity throttling. C. Purchasing reserved capacity provides a discount on provisioned capacity but does not solve the throttling problem. You would still need

</details>

### 318. q-706

A company is developing a social media application that must scale rapidly and handle long-running, ordered processes that store large amounts of relational data. Components must scale independently and evolve without downtime. Which combination of AWS services will meet these requirements?

<details><summary>Answer</summary>

**A. Amazon ECS with Fargate, Amazon RDS, and Amazon SQS**

The architecture requires independently scalable components, pointing to a microservices approach using containers. Amazon ECS with AWS Fargate provides serverless container orchestration, meeting the rapid scaling and independent evolution needs. The requirement for "large amounts of relational data" is directly met by Amazon RDS. For "long-running, ordered processes," Amazon SQS FIFO (First-In, First-Out) queues are the ideal service. They provide a durable, decoupled buffer between microservices and guarantee that messages are processed exactly once, in the exact order that they are sent. This combination effectively addresses all stated requirements for the social media application. Why Incorrect Options are Wrong: B. Amazon SNS is a pub/sub messaging service, not a queue. It does not guarantee the ordered processing of tasks required by the scenario. C. Amazon DynamoDB is a NoSQL da

</details>

### 319. dt-707

A company has released a new version of its production application. The company's workload uses Amazon EC2, AWS Lambda, AWS Fargate, and Amazon SageMaker. The company wants to cost optimize the workload now that usage is at a steady state. The company wants to cover the most services with the fewest savings plans. Which combination of savings plans will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Purchase a SageMaker Savings Plan.; D. Purchase a Compute Savings Plan for Lambda, Fargate, and Amazon EC2.**

</details>

### 320. q-711

An insurance company wants to migrate an application that calculates insurance premiums to AWS. The company must run calculations immediately when a customer submits information through the application. The application usually takes 10 seconds to process a calculation. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Set up an Amazon API Gateway HTTP API to receive the data. Use an AWS Lambda function to process the data immediately.**

The requirement is for immediate, on-demand processing of customer data that takes about 10 seconds. The serverless pattern using Amazon API Gateway and AWS Lambda is perfectly suited for this. API Gateway provides a scalable, managed HTTP endpoint to receive customer submissions. It can then synchronously invoke a Lambda function, which executes the calculation logic immediately. Lambda is designed for short-running, event-driven tasks, and a 10-second execution time is well within its limits, providing a cost-effective and highly available solution without managing any servers. Why Incorrect Options are Wrong: B. Starting an EC2 Spot Instance for each submission introduces significant latency (minutes), failing the "immediately" requirement. This is a pattern for batch processing, not real-time requests. C. AWS Transfer Family is for file transfers (SFTP/FTP), not API-based data submis

</details>

### 321. q-712

A company runs an ecommerce website on AWS. The website architecture uses a single Amazon EC2 instance to run a custom application that handles the website's functions. The website functions include product catalog management and customer checkout. The company's website traffic and transaction volume are increasing rapidly. The company wants to re-architect the application from its current monolithic architecture to a loosely coupled architecture to enable independent scaling. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Refactor the application into microservices that run on Amazon ECS containers. Deploy each service to its own container. Use an Application Load Balancer (ALB) to distribute traffic.**

The goal is to create a loosely coupled architecture where components can scale independently. Refactoring the monolithic application into microservices, with each service (e.g., product catalog, checkout) running in its own Amazon ECS container, directly achieves this. This pattern allows each distinct function to be developed, deployed, and scaled independently based on its specific demand, which is the core principle of a microservices architecture. Why Incorrect Options are Wrong: A. This approach scales the entire monolith horizontally. It does not create a loosely coupled architecture or allow for independent scaling of different application functions. C. Splitting into frontend and backend tiers is a form of decoupling but is too coarse. It does not allow for independent scaling of individual business functions within the backend. D. Moving the entire application into a single con

</details>

### 322. q-715

A company hosts an application on Amazon EC2 On-Demand Instances in an Auto Scaling group. Application peak hours occur at the same time each day. Application users experience slow application performance at the start of peak hours. The application performs normally 2-3 hours after peak hours begin. The company wants to ensure that the application works properly at the start of peak hours. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a scheduled scaling policy for the Auto Scaling group to launch new instances before peak hours.**

The problem states that peak hours are predictable, occurring at the same time each day, and performance suffers at the beginning of this period. This indicates a reactive scaling problem. A scheduled scaling policy is the ideal solution because it is proactive. It allows you to configure the Auto Scaling group to increase the number of instances at a specific time, just before the anticipated peak load begins. This ensures that sufficient capacity is available when the traffic surge starts, preventing the initial performance degradation experienced by users. Dynamic scaling would be too slow as it only reacts after the load has already increased. Why Incorrect Options are Wrong: A. An Application Load Balancer distributes traffic but does not add compute capacity. It cannot solve performance issues caused by insufficient instances. B. A dynamic scaling policy based on memory is reactive

</details>

### 323. q-720

A company needs to integrate with a third-party data feed. The data feed sends a webhook to notify an external service when new data is ready for consumption. A developer wrote an AWS Lambda function to retrieve data when the company receives a webhook callback. The developer must make the Lambda function available for the third party to call. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**A. Create a function URL for the Lambda function. Provide the Lambda function URL to the third party for the webhook.**

A Lambda function URL provides a dedicated HTTPS endpoint for a Lambda function, which is the most direct and operationally efficient way to expose it for a webhook. This method eliminates the need for managing additional infrastructure like an Application Load Balancer (ALB) or Amazon API Gateway. The third party can directly invoke the function via a simple POST request to the provided URL. This solution is serverless, scalable, and requires minimal configuration, aligning perfectly with the principle of operational efficiency. Why Incorrect Options are Wrong: B. An ALB is a more complex and costly solution. It requires configuring a VPC, target groups, and listeners, which is excessive overhead for simply invoking a Lambda function. C. SNS is a pub/sub messaging service, not a direct invocation endpoint. A third party cannot directly call an SNS topic via a simple webhook; it would re

</details>

### 324. q-722 `least-ops`

A company provides an API interface to customers so the customers can retrieve their financial information. The company expects a larger number of requests during peak usage times of the year. The company requires the API to respond consistently with low latency to ensure customer satisfaction. The company needs to provide a compute host for the API. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon API Gateway and AWS Lambda functions with provisioned concurrency.**

The solution requires consistent low latency and the least operational overhead. AWS Lambda and Amazon API Gateway are serverless services, which inherently minimize operational overhead as there are no servers to manage. Lambda Provisioned Concurrency is specifically designed to address latency issues (cold starts) by keeping functions initialized and ready to respond in double-digit milliseconds. This combination directly meets the requirements for a scalable, low-latency API with minimal management effort, especially for predictable peak usage times. Why Incorrect Options are Wrong: A. Using an Application Load Balancer and Amazon ECS involves managing clusters, services, and tasks, which creates more operational overhead than a serverless approach. C. An Amazon EKS cluster generally has even higher operational overhead than ECS due to the complexity of managing a Kubernetes environme

</details>

### 325. q-728

A company operates a food delivery service. Because of recent growth, the company's order processing system is experiencing scaling problems during peak traffic hours. The current architecture includes Amazon EC2 instances in an Auto Scaling group that collect orders from an application. A second group of EC2 instances in an Auto Scaling group fulfills the orders. The order collection process occurs quickly, but the order fulfillment process can take longer. Data must not be lost because of a scaling event. A solutions architect must ensure that the order collection process and the order fulfillment process can both scale adequately during peak traffic hours. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Provision two Amazon SQS queues. Use one SQS queue for order collection. Use the second SQS queue for order fulfillment. Configure the EC2 instances to poll their respective queues. Scale the Auto Scaling groups based on the number of messages in each queue.**

This solution effectively decouples the fast order collection from the slower order fulfillment using two separate SQS queues. This prevents the fulfillment process from becoming a bottleneck. Scaling the Auto Scaling groups based on the number of messages in their respective queues (a metric like ApproximateNumberOfMessagesVisible) is a standard and efficient pattern. It ensures that the number of consumer instances (EC2) matches the current workload, preventing data loss during scaling events and handling traffic peaks gracefully. Why Incorrect Options are Wrong: A. Setting minimum capacity to peak workload is not cost-effective as it leads to over-provisioning during non-peak hours. B. Creating additional Auto Scaling groups on demand is an overly complex and non-standard architecture for this use case. C. Scaling based on "notifications" is imprecise. Auto Scaling requires a specific

</details>

### 326. q-734

A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer ALB. The application is served at one hostname that has two dynamic paths. The first path is named /reports and performs CPU-intensive work that has unpredictable traffic. The second path is named /generateToken and must always respond in less than 1 second. All requests currently go to a single target group. The /generateToken path latency exceeds 1 second during periods when the /reports usage is high. The company must ensure that latency for /generateToken remains under 1 second. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Configure ALB path-based routing to send traffic for /reports and /generateToken to separate target groups. Link each target group to its own Auto Scaling group.**

The core issue is resource contention on the EC2 instances between the CPU-intensive /reports workload and the latency-sensitive /generateToken workload. The most effective solution is to isolate these workloads. By configuring Application Load Balancer (ALB) path-based routing, requests for /reports and /generateToken can be sent to two separate target groups. Each target group can then be backed by its own Auto Scaling group. This allows the compute resources for each path to scale independently, ensuring that a surge in /reports traffic does not consume resources needed by /generateToken, thereby protecting its latency. Why Incorrect Options are Wrong: A. Adding API Gateway does not solve the backend resource contention issue; it simply adds another layer in front of the already overloaded instances. C. Using larger instances (vertical scaling) might provide temporary relief but does

</details>

### 327. q-736 `performance`

A company hosts a website on multiple Amazon EC2 instances that run in an Auto Scaling group. Users are reporting slow responses during peak times between 6 PM and 11 PM every weekend. A solutions architect must implement a solution to improve performance during these peak times. What is the MOST operationally efficient solution that meets these requirements?

<details><summary>Answer</summary>

**B. Configure a scheduled scaling action with a recurrence option to change the desired capacity before and after peak times.**

The scenario describes a predictable, recurring traffic pattern (peak times on weekends). The most operationally efficient solution for this is scheduled scaling, a native feature of Amazon EC2 Auto Scaling. A scheduled scaling action can be configured with a recurrence option (e.g., using a cron expression) to automatically increase the desired capacity of the Auto Scaling group before the peak period begins and decrease it after the period ends. This approach is fully automated, requires no custom code or additional services, and is designed specifically for handling predictable load changes, making it the most efficient solution. Why Incorrect Options are Wrong: A. Using EventBridge and Lambda is a valid but more complex solution. It requires writing, deploying, and maintaining custom code, making it less operationally efficient than the native scheduled scaling feature. C. Target tra

</details>

### 328. dt-742

A company wants to host its web application on AWS using multiple Amazon EC2 instances across different AWS Regions. Since the application content will be specific to each geographic region, the client requests need to be routed to the server that hosts the content for that clients Region. What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**C. Configure Amazon Route 53 with a geolocation routing policy.**

</details>

### 329. q-743

A company's application is experiencing a sudden increase in demand. The company needs to provision Amazon EC2 instances by using a large Amazon Machine Image AMI. The EC2 instances must run in an Auto Scaling group. The company needs a solution that provides minimum initialization latency to meet the demand. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up Amazon EBS fast snapshot restore FSR for a snapshot. Use the snapshot to provision a new AMI. Replace the AMI in the Auto Scaling group with the new AMI.**

When an EC2 instance launches from a standard AMI, the data from the underlying EBS snapshot is loaded lazily, causing significant initialization latency for large volumes (a "first-touch penalty"). Amazon EBS Fast Snapshot Restore (FSR) is designed to eliminate this latency. By enabling FSR on the snapshot used for the AMI, EBS volumes created from it are fully initialized at creation. This ensures that the EC2 instances achieve maximum performance immediately upon launch, which is the most direct way to meet the requirement for minimum initialization latency. Why Incorrect Options are Wrong: A. This describes an AMI creation and deployment workflow but does not include any step to reduce the initialization latency of the large AMI. C. Amazon Data Lifecycle Manager automates snapshot and AMI management but does not inherently reduce the launch time or I/O latency of instances. D. AWS Ba

</details>

### 330. dt-744

A recently created startup built a three-tier web application. The front end has static content. The application layer is based on microservices. User data is stored as JSON documents that need to be accessed with low latency. The company expects regular traffic to be low during the first year, with peaks in traffic when it publicizes new features every month. The startup team needs to minimize operational overhead costs. What should a solutions architect recommend to accomplish this?

<details><summary>Answer</summary>

**C. Use Amazon S3 static website hosting to store and serve the front end. Use Amazon API Gateway and AWS Lambda functions for the application layer. Use Amazon DynamoDB to store user data.**

</details>

### 331. dt-747

A company is developing a new machine learning model solution in AWS. The models are developed as independent microservices that fetch about 1 GB of model data from Amazon S3 at startup and load the data into memory. Users access the models through an asynchronous API. Users can send a request or a batch of requests and specify where the results should be sent. The company provides models to hundreds of users. The usage patterns for the models are irregular. Some models could be unused for days or weeks. Other models could receive batches of thousands of requests at a time. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. The requests from the API are sent to the model's Amazon Simple Queue Service (Amazon SQS) queue. Models are deployed as Amazon Elastic Container Service (Amazon ECS) services reading from the queue. AWS Auto Scaling is enabled on Amazon ECS for both the cluster and copies of the service based on the queue size.**

</details>

### 332. dt-754

A company hosts its web application on AWS using seven Amazon EC2 instances. The company requires that the IP addresses of all healthy EC2 instances be returned in response to DNS queries. Which policy should be used to meet this requirement?

<details><summary>Answer</summary>

**C. Multivalue answer routing policy**

</details>

### 333. q-756 `least-ops`

A company has deployed an application that uses Amazon EC2 Auto Scaling. The Auto Scaling group is associated with a Network Load Balancer and has a minimum desired capacity of 1 and a maximum desired capacity of 6. The CPU utilization of the single running EC2 instance occasionally reaches 90%, which causes the application to become unstable. Which solution will resolve the stability issue with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a target tracking scaling policy. Set the ASGAverageCPUUtilization target value to 75%.**

The application becomes unstable when a single instance's CPU utilization reaches 90%. The most effective solution with the least operational overhead is to implement a target tracking scaling policy. This policy automatically manages the scaling process. By setting the ASGAverageCPUUtilization target to 75%, the Auto Scaling group will automatically launch a new EC2 instance whenever the average CPU across all instances exceeds 75%. This proactive scaling prevents any single instance from reaching the 90% instability threshold, ensuring application stability without requiring any manual intervention. Why Incorrect Options are Wrong: A. Manually adjusting the desired capacity whenever the application is unstable is a reactive approach with high operational overhead, violating a key requirement. C. Setting the target value to 90% is ineffective. The Auto Scaling group would only begin to

</details>

### 334. q-757

A company hosts a public product catalog. The product catalog is accessible through an Amazon API Gateway REST API with AWS Lambda function integrations in a single AWS Region. Most traffic consists of read-only GET requests to the /products resource from global users. The catalog changes approximately once every hour. The company needs to lower latency for global users and reduce the load on the Lambda functions. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Place an Amazon CloudFront distribution in front of API Gateway. Cache GET responses with a 1- hour TTL.**

The solution requires addressing two issues: high latency for global users and high load on the backend Lambda functions. Amazon CloudFront is a global content delivery network (CDN) that caches content in edge locations closer to users, which directly reduces latency for global requests. By caching the GET responses with a 1-hour TTL that matches the data's change frequency, CloudFront serves requests from its cache, preventing them from reaching the origin API Gateway and Lambda functions. This simultaneously reduces the load on the backend and improves performance for users worldwide. Why Incorrect Options are Wrong: A. API Gateway caching is regional. It would reduce Lambda load but would not solve the network latency issue for users far from the API's AWS Region. C. Increasing Lambda memory might improve compute time but does not reduce the number of invocations or address the netwo

</details>

### 335. q-759

A company runs code compilation tasks that span many virtual machines (VMs) in its on-premises data center. These tasks require low latency and high bandwidth between servers. The company wants to migrate this workload to run on Amazon EC2 instances in the AWS Cloud. After the migration, the workload must maintain low latency and high bandwidth between EC2 instances. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy Amazon EC2 instances in a cluster placement group. Enable enhanced networking on the EC2 instances.**

The solution must provide low latency and high bandwidth between EC2 instances for a tightly coupled workload. A cluster placement group is the ideal strategy as it places instances in close physical proximity within a single Availability Zone, minimizing network latency. Enhanced networking provides significantly higher packet per second (PPS) performance, lower inter-instance latency, and higher bandwidth by using single root I/O virtualization (SR-IOV). Combining these two features directly addresses the core requirements of the high-performance computing (HPC) workload described in the scenario. Why Incorrect Options are Wrong: B: A partition placement group is designed for high availability by spreading instances across different hardware racks, which increases inter-instance latency and is unsuitable for this workload. C: Amazon EKS is a container orchestration service. While it ru

</details>

### 336. dt-763

An ecommerce website is deploying its web application as Amazon Elastic Container Service (Amazon ECS) container instances behind an Application Load Balancer (ALB). During periods of high activity, the website slows down and availability is reduced. A solutions architect uses Amazon CloudWatch alarms to receive notifications whenever there is an availability issue so they can scale out resources. Company management wants a solution that automatically responds to such events. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Set up AWS Auto Scaling to scale out the ECS service when the service's CPU utilization is too high. Set up AWS Auto Scaling to scale out the ECS cluster when the CPU or memory reservation is too high.**

</details>

### 337. dt-766

A company has a three-tier environment on AWS that ingests sensor data from its users' devices. The traffic flows through a Network Load Balancer (NLB) then to Amazon EC2 instances for the web tier, and finally to EC2 instances for the application tier that makes database calls. What should a solutions architect do to improve the security of data in transit to the web tier?

<details><summary>Answer</summary>

**A. Configure a TLS listener and add the server certificate on the NLB.**

</details>

### 338. q-767

A company is building a RESTful serverless web application on AWS by using Amazon API Gateway and AWS Lambda. The users of this web application will be geographically distributed, and the company wants to reduce the latency of API requests to these users. Which type of endpoint should a solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**D. Edge-optimized endpoint**

An edge-optimized API endpoint is the ideal choice for serving geographically distributed users. This endpoint type leverages a managed Amazon CloudFront distribution to route client requests to the nearest Point of Presence (PoP). By terminating the initial connection at an edge location closer to the user, it significantly reduces network latency. The request then travels over the optimized AWS global network to the backend API Gateway service in its home region. This architecture is specifically designed to improve performance for a global user base, directly addressing the company's requirement. Why Incorrect Options are Wrong: A. Private endpoints are only accessible from within a Virtual Private Cloud (VPC) and are not suitable for a public-facing web application with global users. B. Regional endpoints are deployed in a specific AWS Region and are best for users located in the sam

</details>

### 339. dt-769

A company runs a web application on Amazon EC2 instances in an Auto Scaling group that has a target group. The company designed the application to work with session affinity (sticky sessions) for a better user experience. The application must be available publicly over the internet as an endpoint. A WAF must be applied to the endpoint for additional security. Session affinity (sticky sessions) must be configured on the endpoint. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**C. Create a public Application Load Balancer. Specify the application target group.; E. Create a web ACL in AWS WAF. Associate the web ACL with the endpoint.**

</details>

### 340. dt-770 `availability`

A company runs a web application on Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer that has sticky sessions enabled. The web server currently hosts the user session state. The company wants to ensure high availability and avoid user session state loss in the event of a web server outage. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon ElastiCache for Redis to store the session state. Update the application to use ElastiCache for Redis to store the session state.**

</details>

### 341. q-791

A company has an employee web portal. Employees log in to the portal to view payroll details. The company is developing a new system to give employees the ability to upload scanned documents for reimbursement. The company runs a program to extract text-based data from the documents and attach the extracted information to each employee's reimbursement IDs for processing. The employee web portal requires 100% uptime. The document extract program runs infrequently throughout the day on an on-demand basis. The company wants to build a scalable and cost-effective new system that will require minimal changes to the existing web portal. The company does not want to make any code changes. Which solution will meet these requirements with the LEAST implementation effort?

<details><summary>Answer</summary>

**A. Run Amazon EC2 On-Demand Instances in an Auto Scaling group for the web portal. Use an AWS Lambda function to run the document extract program. Invoke the Lambda function when an employee uploads a new reimbursement document.**

This solution meets all requirements by effectively separating the new and existing workloads. Using Amazon EC2 On-Demand Instances within an Auto Scaling group is a standard, robust pattern for achieving high availability for the web portal, satisfying the 100% uptime requirement. For the new document extraction feature, AWS Lambda is the most suitable choice. It is a serverless compute service designed for infrequent, event-driven workloads. This approach is highly scalable and cost-effective because you only pay for the compute time when the extraction code is running. Triggering the Lambda function upon a document upload (e.g., to an Amazon S3 bucket) requires minimal changes to the existing portal's front end, thus adhering to the constraints. Why Incorrect Options are Wrong: B: EC2 Spot Instances are unsuitable for the web portal because they can be terminated with short notice, wh

</details>

### 342. q-798 `least-ops`

A company has multiple Amazon RDS DB instances that run in a development AWS account. All the instances have tags to identify them as development resources. The company needs the development DB instances to run on a schedule only during business hours. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an Amazon EventBridge rule that invokes AWS Lambda functions to start and stop the RDS instances.**

This solution represents a standard, serverless, and automated pattern for scheduled tasks. Amazon EventBridge is designed to trigger events on a schedule using cron or rate expressions. Two EventBridge rules can be created: one to start the instances at the beginning of business hours and another to stop them at the end. These rules will invoke AWS Lambda functions. The Lambda functions will contain the logic to identify the RDS instances by their tags using the AWS SDK and then execute the StartDBInstance or StopDBInstance API calls. This approach is fully automated, serverless (no infrastructure to manage), and thus has the least operational overhead. Why Incorrect Options are Wrong: A. Amazon CloudWatch alarms are triggered by metric thresholds (e.g., high CPU), not by a time-based schedule. This is an incorrect trigger mechanism for this requirement. B. AWS Trusted Advisor provides

</details>

### 343. q-803

A company hosts a multi-tier inventory reporting application on AWS. The company needs a cost- effective solution to generate inventory reports on demand. Admin users need to have the ability to generate new reports. Reports take approximately 5-10 minutes to finish. The application must send reports to the email address of the admin user who generates each report. Options:

<details><summary>Answer</summary>

**D. Create an AWS Lambda function to generate the reports. Use a function URL to invoke the function. Use Amazon Simple Email Service (Amazon SES) to send the reports to admin users.**

This solution is the most cost-effective and architecturally sound for the given requirements. AWS Lambda is a serverless compute service that is ideal for on-demand, event-driven workloads. Its maximum execution timeout of 15 minutes comfortably accommodates the 5-10 minute report generation time. Lambda Function URLs provide a simple, built-in HTTPS endpoint to invoke the function directly, eliminating the need for a separate API Gateway for this use case. Amazon Simple Email Service (Amazon SES) is the dedicated, cost-effective service for sending application-generated emails. This combination creates a fully serverless, pay-per-use model that directly meets all requirements with minimal operational overhead. Why Incorrect Options are Wrong: A. An Amazon API Gateway integration has a maximum timeout of 29 seconds, which is too short for a report that takes 5-10 minutes to generate, ma

</details>

### 344. q-807 `cost`

A solutions architect is investigating compute options for a critical analytics application. The application uses long-running processes to prepare and aggregate dat a. The processes cannot be interrupted. The application has a known baseline load. The application needs to handle occasional usage surges. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create an Amazon EC2 Auto Scaling group. Set the Min capacity and Desired capacity parameters to the number of instances required to handle the baseline load. Purchase Reserved Instances for the Auto Scaling group.**

This scenario requires a solution that is both cost-effective and reliable for a workload with a consistent baseline and occasional surges. The processes are long-running and cannot be interrupted. The most cost-effective approach is to use a combination of pricing models. Reserved Instances (RIs) offer significant discounts over On-Demand pricing and are ideal for the known, constant baseline load. An Amazon EC2 Auto Scaling group provides the elasticity needed to handle usage surges by launching additional instances. When the Auto Scaling group scales out beyond the number of purchased RIs, the new instances are launched as On-Demand by default, which are not subject to interruption. This hybrid approach ensures the baseline is handled at the lowest cost while reliably accommodating unpredictable peaks. Why Incorrect Options are Wrong: B: Setting Min, Max, and Desired capacity to the s

</details>

### 345. q-808 `cost`

A company hosts a website analytics application on a single Amazon EC2 On-Demand Instance. The analytics application is highly resilient and is designed to run in stateless mode. The company notices that the application is showing signs of performance degradation during busy times and is presenting 5xx errors. The company needs to make the application scale seamlessly. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Create an Amazon Machine Image (AMI) of the web application. Apply the AMI to a launch template. Create an Auto Scaling group that includes the launch template. Configure the launch template to use a Spot Fleet. Attach an Application Load Balancer to the Auto Scaling group.**

This solution provides a comprehensive, automated, and highly cost-effective architecture. An Auto Scaling group enables the application to "scale seamlessly" by automatically adding or removing instances based on real-time demand, addressing the performance degradation and 5xx errors. Attaching an Application Load Balancer (ALB) effectively distributes incoming traffic across the instances. The use of a Spot Fleet within the launch template is the key to meeting the "MOST cost-effectively" requirement. Spot Instances offer significant discounts over On-Demand prices and are ideal for stateless, fault-tolerant applications like the one described, which can handle the potential for instance interruption. Why Incorrect Options are Wrong: A. This is a manual scaling solution. It does not "scale seamlessly" as it requires manual intervention to add more instances if the load increases furthe

</details>

### 346. q-812

A company operates a web application that experiences predictable traffic patterns: high demand during business hours (9 AM-5 PM, 500 instances) and low demand outside those hours (50 instances). The company wants to optimize costs while maintaining performance. Current infrastructure uses On-Demand EC2 instances with a fixed capacity, costing $8,000 per month. Which cost optimization strategy would deliver the greatest savings?

<details><summary>Answer</summary>

**A. Purchase a mix of Reserved Instances for the baseline 50 instances and use On-Demand instances for peak hours, supplemented by Spot Instances for non-critical workloads.**

Option A perfectly aligns with the AWS Well-Architected Framework's Cost Optimization pillar. For workloads with predictable patterns, AWS recommends purchasing Reserved Instances (or Compute Savings Plans) for the always-on baseline capacity (the 50 instances) to achieve up to 72% discounts compared to On-Demand pricing. For the predictable peak hours, using Auto Scaling with On-Demand instances ensures performance and availability without paying for idle capacity during off-hours. Supplementing with Spot Instances for non-critical, fault-tolerant tasks further reduces costs. This hybrid purchasing model maximizes financial savings while guaranteeing compute resources are available when needed, directly addressing the predictable traffic pattern while maintaining application performance. Why Incorrect Options are Wrong: B: Disabling the application during off-peak times would cause an o

</details>

### 347. q-835 `cost`

A company needs to run a critical data processing workload that uses a Python script every night. The workload takes 1 hour to finish. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Deploy an Amazon Elastic Container Service (Amazon ECS) cluster with the AWS Fargate launch type. Use the Fargate Spot capacity provider. Schedule the job to run once every night.**

The most cost-effective solution is to use AWS Fargate with the Spot capacity provider. Fargate is a serverless compute engine for containers, meaning you only pay for the vCPU and memory resources consumed by the application during its one-hour runtime, eliminating costs for idle server time. Using the Fargate Spot capacity provider offers substantial savings (up to 70%) compared to Fargate On-Demand prices. This combination is ideal for interrupt-tolerant, scheduled batch jobs like this nightly data processing task, providing the lowest possible operational cost. Why Incorrect Options are Wrong: B: Using the EC2 launch type requires provisioning and paying for EC2 instances 24/7, even when the 1-hour job is not running, making it significantly less cost-effective. C: AWS Lambda functions have a maximum execution timeout of 15 minutes (900 seconds). This option is technically infeasible

</details>

### 348. q-857 `cost`

A company has a batch processing application that runs every day. The process typically takes an average 3 hours to complete. The application can handle interruptions and can resume the process after a restart. Currently, the company runs the application on Amazon EC2 On-Demand Instances. The company wants to optimize costs while maintaining the same performance level. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Determine the appropriate instance family and size to meet the requirements of the application. Convert the application to run on AWS Batch with EC2 Spot Instances.**

The application is described as a batch process that is fault-tolerant and can handle interruptions. This characteristic makes it an ideal candidate for Amazon EC2 Spot Instances, which offer the most significant cost savings (up to 90% off On-Demand prices) by utilizing spare EC2 capacity. AWS Batch is a fully managed service specifically designed to orchestrate and run batch computing workloads efficiently. By combining AWS Batch with Spot Instances, the company can automate the provisioning of the cheapest available compute resources for its 3-hour daily job, directly meeting the requirement for the MOST cost-effective solution without compromising performance. Why Incorrect Options are Wrong: A. An EC2 Instance Savings Plan involves a 1-year commitment to a consistent usage level, which is not cost-effective for a workload that runs for only 3 hours per day. B. On-Demand Capacity Res

</details>

### 349. q-858

A company's packaged application dynamically creates and returns single-use text files in response to user requests. The company is using Amazon CloudFront for distribution, but wants to further reduce data transfer costs. The company cannot modify the application's source code. What should a solutions architect do to reduce costs?

<details><summary>Answer</summary>

**A. Use Lambda@Edge to compress the files as they are sent to users.**

The most effective way to reduce data transfer costs without modifying the application is to compress the data before it is sent to the user. Lambda@Edge can be configured to trigger on an origin-response event. This allows a Lambda function to intercept the dynamically generated text file from the origin, compress it (e.g., using gzip or Brotli), and add the appropriate Content-Encoding header. CloudFront then delivers the smaller, compressed file to the user. This directly reduces the amount of data transferred over the internet, which is a primary component of CloudFront costs, and it meets the constraint of not changing the application's source code. Why Incorrect Options are Wrong: B. Amazon S3 Transfer Acceleration is designed to speed up file uploads and downloads to and from Amazon S3, not to reduce data transfer costs from CloudFront to end users. C. Caching is not appropriate f

</details>

### 350. q-866

A company is developing a monolithic Microsoft Windows based application that will run on Amazon EC2 instances. The application will run long data-processing jobs that must not be in-terrupted. The company has modeled expected usage growth for the next 3 years. The company wants to optimize costs for the EC2 instances during the 3-year growth period.

<details><summary>Answer</summary>

**A. Purchase a Compute Savings Plan with a 3-year commitment. Adjust the hourly commit-ment based on the plan recommendations.**

The company's goal is to optimize costs over a 3-year period for a workload that cannot be interrupted and has predictable growth. A 3-year Savings Plan provides a significantly higher discount compared to a 1-year plan, making it the best choice for long-term cost optimization. A Compute Savings Plan is the most appropriate type because it offers flexibility. It automatically applies discounts to EC2 usage regardless of instance family, size, region, or operating system. This is ideal for a 3-year commitment, as it allows the company to modernize its instances over time without losing the savings. As usage grows, the company can purchase additional Savings Plans to increase its hourly commitment, guided by AWS Cost Explorer recommendations. Why Incorrect Options are Wrong: B. An EC2 Instance Savings Plan is too restrictive for a 3-year term, as it locks the company into a specific insta

</details>

### 351. q-870

A company runs a Java-based job on an Amazon EC2 instance. The job runs every hour and takes 10 seconds to run. The job runs on a scheduled interval and consumes 1 GB of memory. The CPU utilization of the instance is low except for short surges during which the job uses the maximum CPU available. The company wants to optimize the costs to run the job.

<details><summary>Answer</summary>

**B. Copy the code into an AWS Lambda function that has 1 GB of memory. Create an Amazon EventBridge scheduled rule to run the code each hour.**

The most cost-effective solution for a short-duration, periodic job is to use a serverless compute service like AWS Lambda. The job runs for only 10 seconds every hour, meaning an EC2 instance would be idle for over 99% of the time while still incurring costs. AWS Lambda's pricing model charges only for the execution duration (billed in milliseconds) and the number of requests. By migrating the code to a Lambda function and triggering it with an Amazon EventBridge scheduled rule, the company pays only for the 10 seconds of compute time each hour, drastically reducing costs compared to any server-based or container-based model that has longer minimum billing durations. Why Incorrect Options are Wrong: A. AWS Fargate is more cost-effective than a full-time EC2 instance, but it is not the most optimal choice. Fargate billing is less granular than Lambda's, making it more expensive for a ver

</details>

### 352. q-875 `cost`

A company runs Amazon EC2 instances as web servers. Peak traffic occurs at two predictable times each day. The web servers remain mostly idle during the rest of the day. A solutions architect must manage the web servers while maintaining fault tolerance in the most cost-effective way. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use an EC2 Auto Scaling group to scale the instances based on demand.**

The most suitable solution is to use an Amazon EC2 Auto Scaling group. This service is designed to automatically adjust the number of EC2 instances to match application demand, ensuring performance during peaks and minimizing costs during lulls. For predictable traffic patterns, scheduled scaling actions can be configured to proactively increase capacity before the daily peaks and decrease it afterward. This approach directly addresses the requirements for cost-effectiveness by only running necessary capacity, and it maintains fault tolerance by automatically replacing unhealthy instances and distributing instances across multiple Availability Zones. Why Incorrect Options are Wrong: B. Purchase Reserved Instances to ensure peak capacity at all times. This is not cost-effective because it requires paying for peak capacity continuously, even during long idle periods. C. Use a cron job to s

</details>

### 353. q-876 `cost`

A company runs a custom application on Amazon EC2 On-Demand Instances. The application has frontend nodes that must run 24/7. The backend nodes only need to run for short periods depending on the workload. Frontend nodes accept jobs and place them in queues. Backend nodes asynchronously process jobs from the queues, and jobs can be restarted. The company wants to scale infrastructure based on workload, using the most cost-effective option. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use Reserved Instances for the frontend nodes. Use Spot Instances for the backend nodes.**

This solution is the most cost-effective because it correctly aligns the EC2 pricing models with the specific workload characteristics of each application tier. The frontend nodes run continuously (24/7), which is a predictable, steady-state workload. Reserved Instances (RIs) are designed for this use case, offering significant discounts over On-Demand pricing in exchange for a commitment. The backend nodes process jobs that are asynchronous and can be restarted, indicating they are fault-tolerant and can handle interruptions. Spot Instances are ideal for such workloads, providing the deepest discounts (up to 90% off On-Demand prices) by utilizing spare EC2 capacity. This combination maximizes savings while meeting all technical requirements. Why Incorrect Options are Wrong: A. While AWS Fargate can scale, EC2 Spot Instances generally provide a lower price point for interruptible, statel

</details>

### 354. q-888 `cost`

A company wants to reduce the cost of its existing three-tier web application. The web servers, application servers, and database servers run on Amazon EC2 On-Demand instances in development, test, and production environments. The EC2 instances average 30% CPU utilization during peak hours and 10% CPU utilization during non-peak hours. The production EC2 instances run 24 hours a day all year. The development and test EC2 instances run for at least 8 hours a day all year. The company wants to implement automation to stop the development and test EC2 instances when those EC2 instances are not in use. Which EC2 instance purchasing solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Use Reserved Instances for the production EC2 instances. Use On-Demand Instances for the development and test EC2 instances.**

This solution provides the most cost-effective purchasing strategy by matching the EC2 instance usage pattern with the appropriate pricing model. For the production instances running 24/7, Reserved Instances (RIs) or Savings Plans offer significant discounts (up to 72%) compared to On-Demand pricing in exchange for a 1- or 3-year commitment. For the development and test instances that run for a portion of the day and are then stopped, the On-Demand model is most cost-effective. With On-Demand, you pay only for the hours the instances are running, avoiding payment for idle time, which aligns perfectly with the plan to automate shutdowns. Why Incorrect Options are Wrong: A. Using Reserved Instances for dev/test instances that are stopped daily is not cost-effective, as you pay for the RI commitment 24/7, even when the instance is off. C. Using a Spot Fleet for a production workload is risk

</details>

### 355. q-892

A company runs an application on an Amazon ECS cluster that uses AWS Fargate On-Demand capacity. The application cannot tolerate any sudden interruptions. The company wants to optimize costs for the application and ensure that the application remains operational. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Purchase a Compute Savings Plan.**

A Compute Savings Plan provides the most flexibility and significant cost savings for AWS Fargate without compromising availability. It offers a discount on compute usage in exchange for a commitment to a consistent amount of usage (measured in $/hour) over a 1- or 3-year term. This plan automatically applies to Fargate, EC2, and Lambda usage, reducing costs while using the same reliable On-Demand capacity. The application continues to run without any risk of interruption, meeting all the company's requirements. Why Incorrect Options are Wrong: A. On-Demand Capacity Reservations ensure capacity is available but do not offer the same level of cost savings as a Savings Plan. B. Reserved Instances are a pricing model for Amazon EC2 instances and do not apply to the serverless compute of AWS Fargate. C. Fargate Spot offers large discounts but can be interrupted with a two-minute warning, whi

</details>

### 356. q-896 `cost`

A company processes large amounts of data by using Amazon EC2 instances in an Auto Scaling group. The data processing jobs run for up to 48 hours each week. The data processing jobs can handle interruptions. However, the company wants to minimize the interruptions. The company wants to use the latest generation of Amazon EC2 instances each year. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**D. Purchase Spot Instances with a capacity-optimized allocation strategy. Override instance types in the Auto Scaling group.**

The workload is interruptible and runs for a limited duration (48 hours/week), making Spot Instances the most cost-effective compute choice, offering up to 90% savings over On-Demand prices. The requirement to minimize interruptions is best met by the capacity-optimized allocation strategy, which sources instances from Spot pools with the most available capacity, reducing the likelihood of reclamation. Using instance type overrides in the Auto Scaling group launch template allows for flexibility to use a diverse set of instance types, including the latest generations, which further increases the probability of acquiring Spot capacity and meets the requirement to stay current. Why Incorrect Options are Wrong: A. Reserved Instances are not cost-effective for workloads with low utilization (28% in this case). A 3-year term is also a long commitment. B. Standard RIs are inflexible and cannot

</details>

### 357. q-901

A company has a development account that contains Amazon EC2 instances. The company uses the EC2 instances for testing. A recent audit of the development account showed that some developers occasionally forget to stop instances after the tests are finished, which incurs extra costs. The company wants to optimize costs for the development account. The company wants to use AWS Budgets to implement a budget for the account. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Define an alert in AWS Budgets for when the budget threshold reaches 100% of forecasted costs. Implement an action in the alert to automatically stop the EC2 instances.**

Create an AWS Budget that monitors forecasted cost; set an action of type "Stop EC2" and choose "Auto-apply." When the forecasted spend reaches 100 % of the monthly budget, AWS Budgets triggers an AWS Systems Manager Automation document that stops all running EC2 instances in the account. Using forecasted cost acts proactively to prevent unnecessary spend caused by forgotten instances. Why Incorrect Options are Wrong: A. Manual SNS + Lambda adds complexity; Budgets native actions already provide stop automation. C. EventBridge rule is unrelated; Budgets can trigger instance actions directly. D. Alerting on actual spend reacts only after overrun, not proactively; forecasted cost is required for prevention.

</details>

### 358. q-915

A company runs an application on Amazon EC2 instances. EC2 instance usage is higher during daytime hours than nighttime hours. A solutions architect wants to automatically optimize Amazon EC2 costs based on this usage pattern. Which AWS service or purchasing option will meet this requirement?

<details><summary>Answer</summary>

**D. AWS Auto Scaling**

The scenario describes a predictable, cyclical usage pattern where demand is high during the day and low at night. AWS Auto Scaling is the ideal service to automatically adjust the number of EC2 instances to match this demand. By using scheduled scaling, a solutions architect can configure rules to increase the desired capacity of the Auto Scaling group during daytime hours and decrease it during nighttime hours. This ensures that the application has sufficient capacity to handle the load while minimizing costs by not running unnecessary instances during periods of low traffic. Why Incorrect Options are Wrong: A. Spot Instances offer cost savings but can be interrupted with short notice, which may not be suitable. They don't inherently follow a daily schedule automatically. B. Reserved Instances provide a billing discount for a long-term commitment but do not automatically scale capacity

</details>

### 359. q-919 `cost`

A company needs to design a solution to process videos that users upload to an Amazon S3 bucket. Each video file is approximately 1 GB in size and takes approximately 20 minutes to process. During peak hours, the company expects to process approximately 100 simultaneous uploads. The video file processing is stateless and can run in parallel as soon as the video files arrive in the S3 bucket. Which solution will meet these requirements in the MOST cost-effective way?

<details><summary>Answer</summary>

**D. Use an Amazon ECS cluster with the AWS Fargate launch type. Use Fargate Spot capacity to run one container task for each uploaded video. Configure an Amazon EventBridge rule to invoke the cluster when a user uploads a video.**

The video processing takes 20 minutes, which exceeds the 15-minute maximum execution time for AWS Lambda. Therefore, a container-based solution is required. AWS Fargate is a serverless compute engine for containers that eliminates the need to manage EC2 instances. For stateless, fault-tolerant workloads like this, Fargate Spot capacity offers discounts of up to 70% compared to On-Demand prices, making it the most cost-effective option. Using an Amazon EventBridge rule to trigger an Amazon ECS task on Fargate for each S3 upload provides a scalable, event-driven, and low-cost solution. Why Incorrect Options are Wrong: A. An AWS Lambda function cannot run for 20 minutes, as its maximum timeout is 15 minutes. Orchestrating chunks with Step Functions adds significant complexity. B. Amazon EKS is designed for Kubernetes and generally has more operational overhead and cost than Amazon ECS, maki

</details>

### 360. q-920 `least-ops`

A company runs a web application in an Amazon EC2 Auto Scaling group. The application runs during business hours only. The company cannot allow interruptions to the application during business hours. The company wants to optimize compute costs for the application based on the application's usage pattern. Which solution will meet this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a scheduled scaling policy for the Auto Scaling group. Configure the policy to scale out during business hours and to scale in during non-business hours.**

The requirement is to optimize costs for an application that runs only during business hours, with minimal operational overhead. Scheduled scaling for an Auto Scaling group is the ideal solution. It allows you to define a recurring schedule to automatically increase the number of instances (scale out) at the start of business hours and decrease them (scale in) at the end. This directly matches the predictable usage pattern, optimizes costs by not running instances when they are not needed, and is a fully automated, "set-and-forget" configuration, thus minimizing operational overhead. Why Incorrect Options are Wrong: A. Manually terminating and launching instances incurs the highest possible operational overhead, which contradicts a key requirement of the question. C. Spot Instances can be interrupted, which violates the requirement that the application cannot have interruptions during bu

</details>

### 361. q-924

A company is planning to migrate multiple workloads to Amazon EC2 instances and needs to determine an appropriate AWS account structure. The workloads must be isolated from one another and belong to separate business units. The company needs to be able to perform chargeback to the business units by using a consolidated monthly view. Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**B. Create a single organization in AWS Organizations. Create a member account for each business unit. Use the bill from the organization management account to perform chargeback.**

AWS Organizations is the recommended service for managing multiple AWS accounts. Creating a member account for each business unit provides strong workload isolation. The service's consolidated billing feature centralizes payment for all accounts into the management account. This single bill provides a detailed breakdown of charges per member account, which directly facilitates chargeback to the respective business units. This approach meets all requirements with the least administrative overhead by using a purpose-built AWS service, avoiding custom scripting or complex tagging strategies for isolation and billing. Why Incorrect Options are Wrong: A. Using standalone accounts and custom scripts for billing creates significant administrative overhead compared to the integrated solution provided by AWS Organizations. C. A single account does not provide the required workload isolation betwe

</details>

### 362. q-950 `availability`

A media streaming company is redesigning its infrastructure to accommodate increasing demand for video content that users consume daily. The company needs to process terabyte-sized videos to block some content in the videos. Video processing can take up to 20 minutes. The company needs a solution that is cost-effective, highly available, and scalable. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon Elastic Container Service (Amazon ECS) with the AWS Fargate launch type to implement microservices to process videos. Store video metadata in Amazon Aurora. Store video content in Amazon S3 Intelligent-Tiering.**

This solution meets all requirements. AWS Fargate is a serverless compute engine for containers that can run tasks longer than the 15-minute limit of AWS Lambda, accommodating the 20-minute video processing time. It is highly scalable and cost-effective as it eliminates the need to manage underlying EC2 instances. Amazon Aurora is a relational database service that provides high availability and scalability by replicating data across multiple Availability Zones. Amazon S3 Intelligent-Tiering is a cost-effective storage solution for video content with unpredictable access patterns, automatically moving data to the most cost-effective access tier without performance impact. Why Incorrect Options are Wrong: A. AWS Lambda functions have a maximum execution timeout of 15 minutes, which is insufficient for the required 20-minute video processing task. C. Amazon EMR is designed for large-scale

</details>

### 363. q-964

A company uses on-premises virtual machines VMs to run a Kubernetes cluster. The company must operate network connectivity for the cluster on premises. The company wants to simplify overall management for the Kubernetes cluster while maintaining control over the underlying infrastructure. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy an Amazon EKS Anywhere cluster on the existing VMs.**

Amazon EKS Anywhere is a deployment option for Amazon EKS that allows you to create and operate Kubernetes clusters on your own on-premises infrastructure, including existing virtual machines (VMs). It provides consistent Kubernetes management tooling with EKS in the cloud, which simplifies overall management. This solution meets the requirements of using existing on-premises hardware and network connectivity while maintaining control over the underlying infrastructure and simplifying cluster operations. Why Incorrect Options are Wrong: B. Amazon EKS Hybrid Nodes is not a valid AWS service name. EKS can be extended on-premises via EKS Anywhere or AWS Outposts, but this is not a distinct offering. C. AWS Outposts requires specific AWS-managed hardware, not the company's existing VMs. This also involves self-hosting Kubernetes, which does not simplify management compared to EKS Anywhere. D

</details>

### 364. q-967 `availability`

A company hosts a popular social networking application on premises. Both the web tier and the application tier run on the same server. The company wants to migrate the application to AWS to handle increased user traffic. The solution must minimize migration effort and ongoing operational costs. The solution must reuse the existing application code. The application must scale to handle millions of requests. The application must be highly available. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application on an Amazon ECS cluster. Configure AWS Application Auto Scaling. Create an Application Load Balancer (ALB). Set the ECS cluster as an ALB target. Create an Amazon CloudFront distribution that uses the ALB as an origin.**

This solution effectively meets all requirements. Containerizing the application with Amazon ECS allows the reuse of existing code with minimal changes. Placing the ECS cluster behind an Application Load Balancer (ALB) and configuring Application Auto Scaling enables the application to handle millions of requests and scale dynamically. Deploying ECS tasks across multiple Availability Zones ensures high availability. Using managed services like ECS, ALB, and Auto Scaling minimizes ongoing operational costs compared to self-managed solutions. Finally, adding a CloudFront distribution improves performance for end-users by caching content globally. This approach balances migration effort, cost, scalability, and availability. Why Incorrect Options are Wrong: B. A self-managed Kubernetes cluster incurs significant operational overhead, and deploying it in a single Availability Zone does not pr

</details>

### 365. q-969

A company needs a solution to prevent photos with unwanted content from being uploaded to the company's web application. The solution must not involve training a machine learning (ML) model. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an AWS Lambda function that uses Amazon Rekognition to detect unwanted content. Create a Lambda function URL that the web application invokes when new photos are uploaded.**

The most effective solution is to use Amazon Rekognition, a service that provides pre-trained machine learning capabilities for image and video analysis. The DetectModerationLabels API operation within Amazon Rekognition is specifically designed to identify unsafe or unwanted content in images without requiring the user to train any models, thus satisfying a key constraint. An AWS Lambda function provides a serverless environment to host the code that calls the Rekognition API. By creating a Lambda function URL, the web application gains a dedicated HTTPS endpoint to invoke this function and submit photos for analysis, creating a complete and efficient solution. Why Incorrect Options are Wrong: A. Amazon SageMaker Autopilot is used to automatically build, train, and tune custom machine learning models, which directly violates the requirement not to train a model. C. Amazon Comprehend is

</details>

### 366. q-972 `least-ops`

A company runs its applications on both Amazon EKS clusters and on-premises Kubernetes clusters. The company wants to view all clusters and workloads from a central location. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon EKS Connector to register and connect all Kubernetes clusters.**

Amazon EKS Connector is a purpose-built feature that allows you to register and connect any conformant Kubernetes cluster to AWS and visualize it in the Amazon EKS console. This provides a single, central location to view both Amazon EKS and on-premises Kubernetes clusters and their workloads. This solution directly addresses the requirements with minimal configuration and is designed for this specific use case, thus having the least operational overhead compared to building a custom solution with other monitoring or management tools. Why Incorrect Options are Wrong: A. CloudWatch Container Insights is primarily for collecting, aggregating, and summarizing metrics and logs for monitoring, not for providing a central management view of cluster resources. C. AWS Systems Manager is a management service for EC2 instances and on-premises servers at the OS level, not for providing a consolidat

</details>
