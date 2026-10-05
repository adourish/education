# Monitoring and management — observability, IaC, operations

8 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. wl-13

Which of the following is not a category in AWS Trusted Advisor service checks?

<details><summary>Answer</summary>

**D. Network Optimization**

https://aws.amazon.com/premiumsupport/trustedadvisor/

</details>

### 2. gh-27 `security`

A company is launching a new application and will display application metrics on an Amazon CloudWatch dashboard. The company's product manager needs to access this dashboard periodically. The product manager does not have an AWS account. A solutions architect must provide access to the product manager by following the principle of least privilege.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Share the dashboard from the CloudWatch console. Enter the product manager's email address, and complete the sharing steps. Provide a shareable link for the dashboard to the product manage.**

Share a single dashboard and designate specific email addresses of the people who can view the dashboard. Each of these users creates their own password that they must enter to view the dashboard.

</details>

### 3. gh-34

A company hosts its multi-tier applications on AWS. For compliance, governance, auditing, and security, the company must track configuration changes on its AWS resources and record a history of API calls made to these resources.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Config to track configuration changes and AWS CloudTrail to record API calls.**

AWS Config for Configuration Changes: AWS Config is a service that tracks changes to resource configurations over time. It provides a history of configuration changes to your AWS resources and helps with compliance and auditing by allowing you to assess how resource configurations have changed over time.

AWS CloudTrail for API Calls: AWS CloudTrail is designed specifically for recording API calls made to AWS resources. It captures detailed information about who made each API call, the actions taken, and the resources affected. This is essential for auditing and security purposes.

</details>

### 4. gh-50

A company has a production workload that runs on 1,000 Amazon EC2 Linux instances. The workload is powered by third-party software. The company needs to patch the third-party software on all EC2 instances as quickly as possible to remediate a critical security vulnerability.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Systems Manager Run Command to run a custom command that applies the patch to all EC2 instances.**

AWS Systems Manager Run Command allows the company to run commands or scripts on multiple EC2 instances. By using Run Command, the company can quickly and easily apply the patch to all 1,000 EC2 instances to remediate the security vulnerability.

Creating an AWS Lambda function to apply the patch to all EC2 instances would not be a suitable solution, as Lambda functions are not designed to run on EC2 instances. Configuring AWS Systems Manager Patch Manager to apply the patch to all EC2 instances would not be a suitable solution, as Patch Manager is not designed to apply third-party software patches. Scheduling an AWS Systems Manager maintenance window to apply the patch to all EC2 instances would not be a suitable solution, as maintenance windows are not designed to apply patches to third-party software.

</details>

### 5. gh-319

A company has hundreds of Amazon EC2 Linux-based instances in the AWS Cloud. Systems administrators have used shared SSH keys to manage the instances. After a recent audit, the company’s security team is mandating the removal of all shared keys. A solutions architect must design a solution that provides secure access to the EC2 instances.
Which solution will meet this requirement with the LEAST amount of administrative overhead?

<details><summary>Answer</summary>

**A. Use AWS Systems Manager Session Manager to connect to the EC2 instances.**

AWS Systems Manager Session Manager: AWS Systems Manager provides a service called Session Manager that allows you to securely connect to your EC2 instances without the need for an external bastion host or direct access to the instances. Session Manager uses IAM roles for authentication and provides an auditable and controlled way to access instances.

</details>

### 6. gh-329

A security audit reveals that Amazon EC2 instances are not being patched regularly. A solutions architect needs to provide a solution that will run regular security scans across a large fleet of EC2 instances. The solution should also patch the EC2 instances on a regular schedule and provide a report of each instance’s patch status.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Turn on Amazon Inspector in the account. Configure Amazon Inspector to scan the EC2 instances for software vulnerabilities. Set up AWS Systems Manager Patch Manager to patch the EC2 instances on a regular schedule.**

</details>

### 7. gh-519

A consulting company provides professional services to customers worldwide. The company provides solutions and tools for customers to expedite gathering and analyzing data on AWS. The company needs to centrally manage and deploy a common set of solutions and tools for customers to use for self-service purposes.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create AWS Service Catalog products for the customers.**

AWS Service Catalog allows you to create and manage catalogs of IT services that are approved for use on AWS. It enables you to centrally manage and distribute standardized product portfolios.

</details>

### 8. gh-665

A company has customers located across the world. The company wants to use automation to secure its systems and network infrastructure. The
company's security team must be able to track and audit all incremental changes to the infrastructure.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use AWS CloudFormation + AWS Config.**

CloudFormation automates infrastructure; Config tracks changes for auditing.
Service Catalog (Options C/D) is for governance, not change tracking.

</details>
