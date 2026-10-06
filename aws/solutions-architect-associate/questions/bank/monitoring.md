# Monitoring and management — observability, IaC, operations

38 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-2

What is the minimum time interval for the data that Amazon CloudWatch receives and aggregates?

<details><summary>Answer</summary>

**C. One minute.**

</details>

### 2. wl-13

Which of the following is not a category in AWS Trusted Advisor service checks?

<details><summary>Answer</summary>

**D. Network Optimization**

https://aws.amazon.com/premiumsupport/trustedadvisor/

</details>

### 3. q-34

A company hosts its multi-tier applications on AWS. For compliance, governance, auditing, and security, the company must track configuration changes on its AWS resources and record a history of API calls made to these resources. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Config to track configuration changes and AWS CloudTrail to record API calls.**

AWS Config for Configuration Changes: AWS Config is a service that tracks changes to resource configurations over time. It provides a history of configuration changes to your AWS resources and helps with compliance and auditing by allowing you to assess how resource configurations have changed over time.  AWS CloudTrail for API Calls: AWS CloudTrail is designed specifically for recording API calls made to AWS resources. It captures detailed information about who made each API call, the actions taken, and the resources affected. This is essential for auditing and security purposes.

</details>

### 4. dt-37

A user is observing the EC2 CPU utilization metric on CloudWatch. The user has observed some interesting patterns while filtering over the 1 week period for a particular hour. The user wants to zoom that data point to a more granular period. How can the user do that easily with CloudWatch?

<details><summary>Answer</summary>

**A. The user can zoom a particular period by selecting that period with the mouse and then releasing the mouse.**

</details>

### 5. q-55 `least-ops`

A company needs to set up a centralized solution to audit API calls to AWS for workloads that run on AWS services and non AWS services. The company must store logs of the audits for 7 years. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Configure custom integrations for AWS CloudTrail Lake to collect and store CloudTrail events from AWS services and non AWS services. Use CloudTrail to store the logs for 7 years.**

AWS CloudTrail Lake is a managed data lake specifically designed to aggregate, immutably store, and query audit and security logs. It directly supports ingesting events from both AWS services and non-AWS sources through partner or custom integrations. This creates the required centralized solution. CloudTrail Lake allows for a configurable retention period of up to 10 years (3653 days), easily meeting the 7-year requirement. As a fully managed service, it handles the underlying infrastructure for data ingestion, storage, and optimization, representing the solution with the least operational overhead compared to building a custom data lake. Why Incorrect Options are Wrong: A. Building a data lake in Amazon S3 requires significant operational overhead for creating ingestion pipelines, managing partitioning, and setting up query services, which contradicts the requirement for the least over

</details>

### 6. q-62

A company has customers located across the world. The company wants to use automation to secure its systems and network infrastructure The company's security team must be able to track and audit all incremental changes to the infrastructure. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Cloud Formation to set up the infrastructure. Use AWS Config to track changes.**

This solution correctly pairs two services to meet the distinct requirements of the question. AWS CloudFormation is the primary Infrastructure as Code (IaC) service on AWS, enabling the company to automate the provisioning and management of its infrastructure through code templates. This directly addresses the need for automation. AWS Config is a service designed to assess, audit, and evaluate the configurations of AWS resources. It continuously monitors and records resource configuration changes, providing a complete audit trail for the security team to track all incremental modifications. Why Incorrect Options are Wrong: A. AWS Organizations is used for central governance and management of multiple AWS accounts, not for provisioning infrastructure resources via code. C. AWS Organizations is for account governance. AWS Service Catalog provides a curated list of deployable IT services, n

</details>

### 7. dt-94

A customer needs to capture all client connection information from their load balancer every five minutes. The company wants to use this data for analyzing traffic patterns and troubleshooting their applications. Which of the following options meets the customer requirements?

<details><summary>Answer</summary>

**A. Enable AWS CloudTrail for the load balancer.**

</details>

### 8. dt-100

You have been asked to set up monitoring of your network and you have decided that Cloudwatch would be the best service to use. Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real-time. You can use CloudWatch to collect and track metrics, which are the variables you want to measure for your resources and applications. Which of the following items listed can AWS Cloudwatch monitor?

<details><summary>Answer</summary>

**B. All of the items listed on this page.**

</details>

### 9. dt-106

You are looking at ways to improve some existing infrastructure as it seems a lot of engineering resources are being taken up with basic management and monitoring tasks and the costs seem to be excessive. You are thinking of deploying Amazon ElasticCache to help. Which of the following statements is true in regards to ElasticCache?

<details><summary>Answer</summary>

**D. You can improve load and response times to user actions and queries and also reduce the cost associated with scaling web applications.**

</details>

### 10. dt-107

A customer needs corporate IT governance and cost oversight of all AWS resources consumed by its divisions. The divisions want to maintain administrative control of the discrete AWS resources they consume and keep those resources separate from the resources of other divisions. Which of the following options, when used together will support the autonomy/control of divisions while enabling corporate IT to maintain governance and cost oversight? (Choose 2 answers)

<details><summary>Answer</summary>

**D. Use AWS Consolidated Billing to link the divisions' accounts to a parent corporate account.; E. Write all child AWS CloudTrail and Amazon CloudWatch logs to each child account's Amazon S3 'Log' bucket.**

</details>

### 11. dt-122

It is advised that you watch the Amazon CloudWatch [...] metric (available via the AWS Management Console or Amazon Cloud Watch APIs) carefully and recreate the Read Replica should it fall behind due to replication errors.

<details><summary>Answer</summary>

**C. Replica Lag.**

</details>

### 12. q-153

A company runs production workloads in its AWS account. Multiple teams create and maintain the workloads. The company needs to be able to detect changes in resource configurations. The company needs to capture changes as configuration items without changing or modifying the existing resources. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Config. Start the configuration recorder for AWS resources to detect changes in resource configurations.**

AWS Config is the designated service for assessing, auditing, and evaluating the configurations of AWS resources. It continuously monitors and records resource configurations, capturing them as "configuration items." By enabling the configuration recorder, AWS Config can detect any changes made to the resources and maintain a detailed history. This process is non-intrusive and provides the exact functionality required: detecting and capturing configuration changes without modifying the resources themselves. The term "configuration items" is specific terminology for the data objects that AWS Config creates. Why Incorrect Options are Wrong: B. AWS CloudFormation drift detection is limited to resources managed within a CloudFormation stack and compares the current state only to the template-defined state. C. Amazon Detective is a security service for investigating potential security issues

</details>

### 13. dt-189

What will be the state of the alarm at the end of 90 minutes, if the CPU utilization is constant at 80%?

<details><summary>Answer</summary>

**B. ALARM.**

</details>

### 14. dt-200

A user comes to you and wants access to Amazon CloudWatch but only wants to monitor a specific LoadBalancer. Is it possible to give him access to a specific set of instances or a specific LoadBalancer?

<details><summary>Answer</summary>

**A. No because you can't use IAM to control access to CloudWatch data for specific resources.**

</details>

### 15. dt-218

Which one of the following answers is not a possible state of Amazon CloudWatch Alarm?

<details><summary>Answer</summary>

**D. STATUS_CHECK_FAILED.**

</details>

### 16. dt-240

The Trusted Advisor service provides insight regarding which four categories of an AWS account?

<details><summary>Answer</summary>

**C. Performance, cost optimization, security, and fault tolerance.**

</details>

### 17. q-241

A security audit reveals that Amazon EC2 instances are not being patched regularly. A solutions architect needs to provide a solution that will run regular security scans across a large fleet of EC2 instances. The solution should also patch the EC2 instances on a regular schedule and provide a report of each instance's patch status. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Turn on Amazon Inspector in the account. Configure Amazon Inspector to scan the EC2 instances for software vulnerabilities. Set up AWS Systems Manager Patch Manager to patch the EC2 instances on a regular schedule.**

This solution correctly pairs AWS services to meet all requirements. Amazon Inspector is a vulnerability management service that continuously scans AWS workloads, including EC2 instances, for software vulnerabilities. It provides detailed findings reports. AWS Systems Manager Patch Manager automates the process of patching managed nodes, including EC2 instances, on a schedule. It also provides detailed compliance reporting on the patch status of each instance. This combination provides a comprehensive, automated solution for scanning, patching, and reporting across a large fleet of instances. Why Incorrect Options are Wrong: A. Amazon Macie is a data security service for Amazon S3, not for scanning EC2 instance vulnerabilities. A cron job is not a scalable fleet management solution. B. Amazon GuardDuty is a threat detection service that monitors for malicious activity, not a vulnerabilit

</details>

### 18. dt-245

You are architecting a highly-scalable and reliable web application which will have a huge amount of content. You have decided to use Cloudfront as you know it will speed up distribution of your static and dynamic web content and know that Amazon CloudFront integrates with Amazon CloudWatch metrics so that you can monitor your web application. Because you live in Sydney you have chosen the the Asia Pacific (Sydney) region in the AWS console. However you have set up this up but no CloudFront metrics seem to be appearing in the CloudWatch console. What is the most likely reason from the possible choices below for this?

<details><summary>Answer</summary>

**C. Metrics for CloudWatch are available only when you choose the US East (Virginia).**

</details>

### 19. q-277

An image-hosting company stores images as objects in Amazon S3 buckets. The company must prevent accidental exposure of the objects to the public. All S3 objects in the company's entire AWS account must remain private. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use the S3 Block Public Access feature at the account level. Deploy the AWS Config s3-account- level-public-access-blocks rule and an AWS Systems Manager document to take automatic remediation actions when the rule is in the non-compliant state.**

The requirement is to enforce a private-only policy for all S3 objects across an entire AWS account. The S3 Block Public Access feature, when enabled at the account level, provides a centralized, preventative control that overrides any bucket-level policies that might otherwise allow public access. This is the most direct and effective way to meet the primary requirement. To ensure this setting is never disabled, deploying the AWS Config managed rule s3-account-level-public-access-blocks will continuously monitor the configuration. Pairing this with an AWS Systems Manager automation document provides an automated remediation mechanism to re-enable the block if it's ever found to be non-compliant. Why Incorrect Options are Wrong: A. Amazon GuardDuty is a threat detection service; it is not the primary tool for enforcing preventative configuration policies like blocking public access. B. A

</details>

### 20. q-319

A company has hundreds of Amazon EC2 Linux-based instances in the AWS Cloud. Systems administrators have used shared SSH keys to manage the instances. After a recent audit, the company’s security team is mandating the removal of all shared keys. A solutions architect must design a solution that provides secure access to the EC2 instances. Which solution will meet this requirement with the LEAST amount of administrative overhead?

<details><summary>Answer</summary>

**A. Use AWS Systems Manager Session Manager to connect to the EC2 instances.**

AWS Systems Manager Session Manager: AWS Systems Manager provides a service called Session Manager that allows you to securely connect to your EC2 instances without the need for an external bastion host or direct access to the instances. Session Manager uses IAM roles for authentication and provides an auditable and controlled way to access instances.

</details>

### 21. dt-362

You are very concerned about security on your network because you have multiple programmers testing APIs and SDKs and you have no idea what is happening. You think CloudTrail may help but are not sure what it does. Which of the following statements best describes the AWS service CloudTrail?

<details><summary>Answer</summary>

**A. With AWS CloudTrail you can get a history of AWS API calls and related events for your account.**

</details>

### 22. dt-411

You need to create a JSON-formatted text file for AWS CloudFormation. This is your first template and the only thing you know is that the templates include several major sections but there is only one that is required for it to work. What is the only section required?

<details><summary>Answer</summary>

**C. Resources.**

</details>

### 23. dt-430

You are working with a customer who is using Chef configuration management in their data center. Which service is designed to let the customer leverage existing Chef recipes in AWS?

<details><summary>Answer</summary>

**D. AWS OpsWorks.**

</details>

### 24. q-473 `least-ops`

A company runs a non-production application on an Amazon EC2 instance that has the Amazon CloudWatch agent installed. The CloudWatch agent monitors application processes and sends custom metrics to CloudWatch. The application has a critical bug that causes crashes that require an instance reboot. The company does not currently have the resources to address the bug, but the server needs to remain as operational as possible. The company manually reboots the instance several times each day. The company needs a solution to automate the instance reboots until the company can address the root cause of the bug. Which solution will meet this requirement with the LEAST amount of operational overhead?

<details><summary>Answer</summary>

**A. Use a CloudWatch alarm state change event to invoke Amazon EventBridge to run AWS Systems Manager Run Command to restart the instance.**

The goal is to automate instance reboots with the least operational overhead. A CloudWatch alarm can be configured to monitor a custom metric (e.g., application process count). When the alarm enters the ALARM state, it can send an event to Amazon EventBridge. An EventBridge rule can then be configured to trigger an AWS Systems Manager Run Command as its target, which executes the reboot on the specified instance. This approach is fully automated and serverless, avoiding the need to write, manage, and maintain custom code in an AWS Lambda function, thereby minimizing operational overhead. Why Incorrect Options are Wrong: B. This solution works but involves creating and managing a Lambda function, which adds more operational overhead than using a direct EventBridge rule. C. This solution is not automated. It notifies a team via an SNS topic, requiring manual intervention to restart the ins

</details>

### 25. dt-491

You are playing around with setting up stacks using JSON templates in CloudFormation to try and understand them a little better. You have set up about 5 or 6 but now start to wonder if you are being charged for these stacks. What is AWS's billing policy regarding stack resources?

<details><summary>Answer</summary>

**B. You are charged for the stack resources for the time they were operating (even if you deleted the stack right away).**

</details>

### 26. dt-567

Using Amazon CloudWatch's Free Tier, what is the frequency of metric updates which you receive?

<details><summary>Answer</summary>

**A. 5 minutes.**

</details>

### 27. dt-584

Which statement below best describes what thresholds you can set to trigger a CloudWatch Alarm?

<details><summary>Answer</summary>

**A. Set a target value and choose whether the alarm will trigger when the value is greater than (>), greater than or equal to (>=), less than (<), or less than or equal to (<=) that value.**

</details>

### 28. dt-598

You need to set up a complex network infrastructure for your organization that will be reasonably easy to deploy, replicate, control, and track changes on. Which AWS service would be best to use to help you accomplish this?

<details><summary>Answer</summary>

**B. AWS CloudFormation.**

</details>

### 29. q-613

A solutions architect creates an Auto Scaling group for a memory-intensive application. The solutions architect wants to scale up and scale down based on memory usage. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Install and configure the Amazon CloudWatch agent. Create a target tracking policy to scale based on the memusedpercent CloudWatch metric.**

To scale an Auto Scaling group based on memory usage, two components are required. First, since memory utilization is a custom metric not natively published by EC2 instances to CloudWatch, the Amazon CloudWatch agent must be installed and configured on the instances to collect and send this data. The agent can be configured to report metrics like memusedpercent. Second, a target tracking scaling policy is the most suitable and recommended approach. This policy type automatically adjusts the number of instances in the Auto Scaling group to keep the average memusedpercent metric at, or close to, a specified target value, simplifying the scaling configuration. Why Incorrect Options are Wrong: A. The AWS Systems Manager (SSM) Agent is used for management and configuration, not for collecting and publishing custom CloudWatch metrics like memory usage. C. The AWS Systems Manager (SSM) Agent do

</details>

### 30. dt-616

In the Amazon CloudWatch, which metric should I be checking to ensure that your DB Instance has enough free storage space?

<details><summary>Answer</summary>

**B. Free Storage Space.**

</details>

### 31. dt-635

What can I access by visiting the URL: http://status.aws.amazon.com/?

<details><summary>Answer</summary>

**C. AWS Service Health Dashboard.**

</details>

### 32. dt-640

What is the time period with which metric data is sent to CloudWatch when detailed monitoring is enabled on an Amazon EC2 instance?

<details><summary>Answer</summary>

**C. 1 minute.**

</details>

### 33. dt-669

A company has migrated a fleet of hundreds of on-premises virtual machines (VMs) to Amazon EC2 instances. The instances run a diverse fleet of Windows Server versions along with several Linux distributions. The company wants a solution that will automate inventory and updates of the operating systems. The company also needs a summary of common vulnerabilities of each instance for regular monthly reviews. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**B. Set up AWS Systems Manager Patch Manager to manage all the EC2 instances. Deploy Amazon Inspector, and configure monthly reports.**

</details>

### 34. q-679

A company is using a loosely coupled serverless architecture on AWS. The architecture consists of multiple web applications and APIs distributed across multiple teams. The company uses AWS Control Tower to provision AWS accounts. The company's development teams use AWS CloudFormation. The company wants to improve trace monitoring and gain insight into how individual services in application stacks are performing. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Enable AWS X-Ray in the CloudFormation templates.**

The core requirement is to implement "trace monitoring" for a distributed, serverless architecture to understand the performance of individual services. AWS X-Ray is the service designed specifically for this purpose. It analyzes and debugs distributed applications by tracing requests as they travel through various services. Since the company uses AWS CloudFormation for infrastructure deployment, the correct and standard practice is to enable X-Ray tracing for the relevant resources (e.g., AWS Lambda functions, Amazon API Gateway stages) directly within the CloudFormation templates. This approach integrates performance tracing into their existing infrastructure-as-code workflow, ensuring consistency and scalability across all application stacks. Why Incorrect Options are Wrong: A. AWS CloudTrail is a service for logging, monitoring, and retaining account activity related to actions acros

</details>

### 35. dt-691 `security`

A company is launching a new application and will display application metrics on an Amazon CloudWatch dashboard. The company's product manager needs to access this dashboard periodically. The product manager does not have an AWS account. A solutions architect must provide access to the product manager by following the principle of least privilege. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Share the dashboard from the CloudWatch console. Enter the product manager's email address, and complete the sharing steps. Provide a shareable link for the dashboard to the product manager.**

</details>

### 36. dt-701

A company has a production workload that runs on 1,000 Amazon EC2 Linux instances. The workload is powered by third-party software. The company needs to patch the third-party software on all EC2 instances as quickly as possible to remediate a critical security vulnerability. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Systems Manager Run Command to run a custom command that applies the patch to all EC2 instances.**

</details>

### 37. q-879 `cost`

A company hosts a web application on Amazon EC2 instances that are part of an Auto Scaling group behind an Application Load Balancer (ALB). The application experiences spikes in requests that come through the ALB throughout each day. The traffic spikes last between 15 and 20 minutes. The company needs a solution that uses a standard or custom metric to scale the EC2 instances based on the number of requests that come from the ALB. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Configure an Amazon CloudWatch alarm to monitor the ALB RequestCount metric. Configure a simple scaling policy to scale the EC2 instances in response to the metric.**

The ALB RequestCount metric is a standard CloudWatch metric that directly measures the number of requests processed by the load balancer. A simple scaling policy with this metric provides immediate response to traffic spikes. This is the most cost-effective approach as it uses built-in metrics without additional complexity, scales only when needed during the 15-20 minute spikes, and avoids over-provisioning that could occur with predictive scaling. Why Incorrect Options are Wrong: B: Predictive scaling would pre-provision instances based on patterns, causing unnecessary costs outside actual spike periods. C: UnhealthyHostCount measures instance health, not request volume, making it inappropriate for traffic-based scaling. D: Creating custom metrics for GET requests adds unnecessary complexity and cost when RequestCount already provides this functionality.

</details>

### 38. q-955

A consulting company provides professional services to customers worldwide. The company provides solutions and tools for customers to expedite gathering and analyzing data on AWS. The company needs to centrally manage and deploy a common set of solutions and tools for customers to use for self-service purposes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create AWS Service Catalog products for the customers.**

AWS Service Catalog is designed specifically for this use case. It enables organizations to create and manage a curated catalog of IT services (called products) that are approved for use on AWS. These products are typically based on AWS CloudFormation templates. This allows the consulting company to centrally manage a common set of solutions, enforce governance and best practices through constraints, and provide a simple self-service portal for customers to discover and deploy these pre-approved solutions without needing direct access to the underlying AWS services. Why Incorrect Options are Wrong: A. AWS CloudFormation templates are the building blocks for defining infrastructure but do not provide a central catalog, governance, or a self-service portal for end-users. C. AWS Systems Manager is used for operational management, automation, and patching of existing resources, not for provi

</details>
