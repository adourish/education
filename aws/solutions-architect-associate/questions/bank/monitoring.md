# Monitoring and management — observability, IaC, operations

31 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

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

### 5. dt-94

A customer needs to capture all client connection information from their load balancer every five minutes. The company wants to use this data for analyzing traffic patterns and troubleshooting their applications. Which of the following options meets the customer requirements?

<details><summary>Answer</summary>

**A. Enable AWS CloudTrail for the load balancer.**

</details>

### 6. dt-100

You have been asked to set up monitoring of your network and you have decided that Cloudwatch would be the best service to use. Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real-time. You can use CloudWatch to collect and track metrics, which are the variables you want to measure for your resources and applications. Which of the following items listed can AWS Cloudwatch monitor?

<details><summary>Answer</summary>

**B. All of the items listed on this page.**

</details>

### 7. dt-106

You are looking at ways to improve some existing infrastructure as it seems a lot of engineering resources are being taken up with basic management and monitoring tasks and the costs seem to be excessive. You are thinking of deploying Amazon ElasticCache to help. Which of the following statements is true in regards to ElasticCache?

<details><summary>Answer</summary>

**D. You can improve load and response times to user actions and queries and also reduce the cost associated with scaling web applications.**

</details>

### 8. dt-107

A customer needs corporate IT governance and cost oversight of all AWS resources consumed by its divisions. The divisions want to maintain administrative control of the discrete AWS resources they consume and keep those resources separate from the resources of other divisions. Which of the following options, when used together will support the autonomy/control of divisions while enabling corporate IT to maintain governance and cost oversight? (Choose 2 answers)

<details><summary>Answer</summary>

**D. Use AWS Consolidated Billing to link the divisions' accounts to a parent corporate account.; E. Write all child AWS CloudTrail and Amazon CloudWatch logs to each child account's Amazon S3 'Log' bucket.**

</details>

### 9. dt-122

It is advised that you watch the Amazon CloudWatch [...] metric (available via the AWS Management Console or Amazon Cloud Watch APIs) carefully and recreate the Read Replica should it fall behind due to replication errors.

<details><summary>Answer</summary>

**C. Replica Lag.**

</details>

### 10. dt-189

What will be the state of the alarm at the end of 90 minutes, if the CPU utilization is constant at 80%?

<details><summary>Answer</summary>

**B. ALARM.**

</details>

### 11. dt-200

A user comes to you and wants access to Amazon CloudWatch but only wants to monitor a specific LoadBalancer. Is it possible to give him access to a specific set of instances or a specific LoadBalancer?

<details><summary>Answer</summary>

**A. No because you can't use IAM to control access to CloudWatch data for specific resources.**

</details>

### 12. dt-218

Which one of the following answers is not a possible state of Amazon CloudWatch Alarm?

<details><summary>Answer</summary>

**D. STATUS_CHECK_FAILED.**

</details>

### 13. dt-240

The Trusted Advisor service provides insight regarding which four categories of an AWS account?

<details><summary>Answer</summary>

**C. Performance, cost optimization, security, and fault tolerance.**

</details>

### 14. dt-245

You are architecting a highly-scalable and reliable web application which will have a huge amount of content. You have decided to use Cloudfront as you know it will speed up distribution of your static and dynamic web content and know that Amazon CloudFront integrates with Amazon CloudWatch metrics so that you can monitor your web application. Because you live in Sydney you have chosen the the Asia Pacific (Sydney) region in the AWS console. However you have set up this up but no CloudFront metrics seem to be appearing in the CloudWatch console. What is the most likely reason from the possible choices below for this?

<details><summary>Answer</summary>

**C. Metrics for CloudWatch are available only when you choose the US East (Virginia).**

</details>

### 15. q-319

A company has hundreds of Amazon EC2 Linux-based instances in the AWS Cloud. Systems administrators have used shared SSH keys to manage the instances. After a recent audit, the company’s security team is mandating the removal of all shared keys. A solutions architect must design a solution that provides secure access to the EC2 instances. Which solution will meet this requirement with the LEAST amount of administrative overhead?

<details><summary>Answer</summary>

**A. Use AWS Systems Manager Session Manager to connect to the EC2 instances.**

AWS Systems Manager Session Manager: AWS Systems Manager provides a service called Session Manager that allows you to securely connect to your EC2 instances without the need for an external bastion host or direct access to the instances. Session Manager uses IAM roles for authentication and provides an auditable and controlled way to access instances.

</details>

### 16. q-329

A security audit reveals that Amazon EC2 instances are not being patched regularly. A solutions architect needs to provide a solution that will run regular security scans across a large fleet of EC2 instances. The solution should also patch the EC2 instances on a regular schedule and provide a report of each instance’s patch status. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Turn on Amazon Inspector in the account. Configure Amazon Inspector to scan the EC2 instances for software vulnerabilities. Set up AWS Systems Manager Patch Manager to patch the EC2 instances on a regular schedule.**

</details>

### 17. dt-362

You are very concerned about security on your network because you have multiple programmers testing APIs and SDKs and you have no idea what is happening. You think CloudTrail may help but are not sure what it does. Which of the following statements best describes the AWS service CloudTrail?

<details><summary>Answer</summary>

**A. With AWS CloudTrail you can get a history of AWS API calls and related events for your account.**

</details>

### 18. dt-411

You need to create a JSON-formatted text file for AWS CloudFormation. This is your first template and the only thing you know is that the templates include several major sections but there is only one that is required for it to work. What is the only section required?

<details><summary>Answer</summary>

**C. Resources.**

</details>

### 19. dt-430

You are working with a customer who is using Chef configuration management in their data center. Which service is designed to let the customer leverage existing Chef recipes in AWS?

<details><summary>Answer</summary>

**D. AWS OpsWorks.**

</details>

### 20. dt-491

You are playing around with setting up stacks using JSON templates in CloudFormation to try and understand them a little better. You have set up about 5 or 6 but now start to wonder if you are being charged for these stacks. What is AWS's billing policy regarding stack resources?

<details><summary>Answer</summary>

**B. You are charged for the stack resources for the time they were operating (even if you deleted the stack right away).**

</details>

### 21. q-519

A consulting company provides professional services to customers worldwide. The company provides solutions and tools for customers to expedite gathering and analyzing data on AWS. The company needs to centrally manage and deploy a common set of solutions and tools for customers to use for self-service purposes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create AWS Service Catalog products for the customers.**

AWS Service Catalog allows you to create and manage catalogs of IT services that are approved for use on AWS. It enables you to centrally manage and distribute standardized product portfolios.

</details>

### 22. dt-567

Using Amazon CloudWatch's Free Tier, what is the frequency of metric updates which you receive?

<details><summary>Answer</summary>

**A. 5 minutes.**

</details>

### 23. dt-584

Which statement below best describes what thresholds you can set to trigger a CloudWatch Alarm?

<details><summary>Answer</summary>

**A. Set a target value and choose whether the alarm will trigger when the value is greater than (>), greater than or equal to (>=), less than (<), or less than or equal to (<=) that value.**

</details>

### 24. dt-598

You need to set up a complex network infrastructure for your organization that will be reasonably easy to deploy, replicate, control, and track changes on. Which AWS service would be best to use to help you accomplish this?

<details><summary>Answer</summary>

**B. AWS CloudFormation.**

</details>

### 25. dt-616

In the Amazon CloudWatch, which metric should I be checking to ensure that your DB Instance has enough free storage space?

<details><summary>Answer</summary>

**B. Free Storage Space.**

</details>

### 26. dt-635

What can I access by visiting the URL: http://status.aws.amazon.com/?

<details><summary>Answer</summary>

**C. AWS Service Health Dashboard.**

</details>

### 27. dt-640

What is the time period with which metric data is sent to CloudWatch when detailed monitoring is enabled on an Amazon EC2 instance?

<details><summary>Answer</summary>

**C. 1 minute.**

</details>

### 28. gh-665

A company has customers located across the world. The company wants to use automation to secure its systems and network infrastructure. The
company's security team must be able to track and audit all incremental changes to the infrastructure.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use AWS CloudFormation + AWS Config.**

CloudFormation automates infrastructure; Config tracks changes for auditing.
Service Catalog (Options C/D) is for governance, not change tracking.

</details>

### 29. dt-669

A company has migrated a fleet of hundreds of on-premises virtual machines (VMs) to Amazon EC2 instances. The instances run a diverse fleet of Windows Server versions along with several Linux distributions. The company wants a solution that will automate inventory and updates of the operating systems. The company also needs a summary of common vulnerabilities of each instance for regular monthly reviews. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**B. Set up AWS Systems Manager Patch Manager to manage all the EC2 instances. Deploy Amazon Inspector, and configure monthly reports.**

</details>

### 30. dt-691 `security`

A company is launching a new application and will display application metrics on an Amazon CloudWatch dashboard. The company's product manager needs to access this dashboard periodically. The product manager does not have an AWS account. A solutions architect must provide access to the product manager by following the principle of least privilege. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Share the dashboard from the CloudWatch console. Enter the product manager's email address, and complete the sharing steps. Provide a shareable link for the dashboard to the product manager.**

</details>

### 31. dt-701

A company has a production workload that runs on 1,000 Amazon EC2 Linux instances. The workload is powered by third-party software. The company needs to patch the third-party software on all EC2 instances as quickly as possible to remediate a critical security vulnerability. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Systems Manager Run Command to run a custom command that applies the patch to all EC2 instances.**

</details>
