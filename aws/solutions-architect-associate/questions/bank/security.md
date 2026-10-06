# Security and identity — IAM, encryption, protection, governance

192 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. ce-3

A company is running a highly sensitive application on Amazon EC2 backed by an Amazon RDS database Compliance regulations mandate that all personally identifiable information (Pll) be encrypted at rest. Which solution should a solutions architect recommend to meet this requirement with the LEAST amount of changes to the infrastructure?

<details><summary>Answer</summary>

**D. Configure Amazon Elastic Block Store (Amazon EBS) encryption and Amazon RDS encryption with AWS Key Management Service (AWS KMS) keys to encrypt instance and database volumes.**

The requirement is to encrypt personally identifiable information (PII) at rest for an application running on Amazon EC2 and its Amazon RDS database, with minimal infrastructure changes. Amazon EBS encryption is a native feature that encrypts data at rest for volumes attached to EC2 instances. Similarly, Amazon RDS encryption encrypts the underlying database storage, automated backups, read replicas, and snapshots. Both services seamlessly integrate with AWS Key Management Service (KMS) to manage the encryption keys. Enabling these features is a straightforward configuration change, directly addressing the compliance requirement for both tiers of the application with the least operational overhead. Why Incorrect Options are Wrong: A. AWS Certificate Manager (ACM) provides and manages SSL/TLS certificates for securing network communications (data in transit), not for encrypting data at re

</details>

### 2. ce-4

A company is preparing to store confidential data in Amazon S3. For compliance reasons, the data must be encrypted at rest. Encryption key usage must be logged for auditing purposes. Keys must be rotated every year. Which solution meets these requirements and is the MOST operationally efficient?

<details><summary>Answer</summary>

**D. Server-side encryption with AWS KMS keys (SSE-KMS) with automatic rotation**

The solution requires encryption at rest, logging of key usage for auditing, annual key rotation, and maximum operational efficiency. Server-side encryption with AWS Key Management Service (SSE-KMS) is the only option that meets all criteria. AWS KMS integrates with AWS CloudTrail to log every use of the encryption key, satisfying the audit requirement. Furthermore, KMS supports automatic annual rotation of the backing key material for customer managed keys. This automated process is the most operationally efficient method, as it requires no manual intervention after initial setup, unlike manual rotation or managing customer-provided keys. Why Incorrect Options are Wrong: A. Server-side encryption with customer-provided keys (SSE-C): AWS does not store or manage these keys, so it cannot log their usage or rotate them. This fails the logging, rotation, and operational efficiency requireme

</details>

### 3. dt-11

In regards to IAM you can edit user properties later, but you cannot use the console to change the [...].

<details><summary>Answer</summary>

**A. user name.**

</details>

### 4. ce-14 `least-ops`

A company has separate AWS accounts for its finance, data analytics, and development departments. Because of costs and security concerns, the company wants to control which services each AWS account can use Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create organization units (OUs) for each department in AWS Organizations. Attach service control policies (SCPs) to the OUs.**

AWS Organizations is designed for centrally governing and managing multiple AWS accounts. By grouping accounts into Organizational Units (OUs) based on department, you can apply policies to all accounts within that OU simultaneously. Service Control Policies (SCPs) are a feature of AWS Organizations that act as guardrails, allowing you to specify the maximum permissions for member accounts. You can attach an SCP to an OU to either deny access to specific services or allow access to only an explicit list of services, thereby controlling usage for security and cost reasons with minimal administrative effort. Why Incorrect Options are Wrong: A. AWS Systems Manager is for operational management, automation, and configuration of resources like EC2 instances, not for enforcing permissions or restricting access to AWS services at the account level. C. AWS CloudFormation is an Infrastructure as

</details>

### 5. wl-16

Your organization has an AWS setup and planning to build Single Sign-On for users to authenticate with on-premise Microsoft Active Directory Federation Services (ADFS) and let users log in to the AWS console using AWS STS Enterprise Identity Federation. Which of the following services do you need to call from AWS STS service after you authenticate with your on-premise?

<details><summary>Answer</summary>

**A. AssumeRoleWithSAML**

https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.
html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html

</details>

### 6. dt-33

You have been asked to tighten up the password policies in your organization after a serious security breach, so you need to consider every possible security measure. Which of the following is not an account password policy for IAM Users that can be set?

<details><summary>Answer</summary>

**C. Force IAM users to contact an account administrator when the user has entered his password incorrectly.**

</details>

### 7. ce-36 `least-ops`

A financial services company plans to launch a new application on AWS to handle sensitive financial transactions. The company will deploy the application on Amazon EC2 instances. The company will use Amazon RDS for MySQL as the database. The company's security policies mandate that data must be encrypted at rest and in transit. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure encryption at rest for Amazon RDS for MySQL by using AWS KMS managed keys. Configure AWS Certificate Manager (ACM) SSL/TLS certificates for encryption in transit.**

This solution meets the requirements with the least operational overhead by leveraging managed AWS services. Amazon RDS provides a built-in feature for encryption at rest that integrates with AWS Key Management Service (KMS). This allows data on the underlying storage, automated backups, read replicas, and snapshots to be encrypted with a simple configuration setting. For encryption in transit, Amazon RDS supports SSL/TLS connections between the application on EC2 and the database. This is the standard, low-overhead method for securing data in motion without requiring complex network configurations like VPNs or IPsec tunnels. Using these native, managed features minimizes the operational burden on the company. Why Incorrect Options are Wrong: B. Configuring IPsec tunnels between EC2 instances and the RDS database adds significant complexity and management overhead compared to using the n

</details>

### 8. ce-43 `least-ops`

A company is designing an application on AWS that processes sensitive dat a. The application stores and processes financial data for multiple customers. To meet compliance requirements, the data for each customer must be encrypted separately at rest by using a secure, centralized key management solution. The company wants to use AWS Key Management Service (AWS KMS) to implement encryption. Which solution will meet these requirements with the LEAST operational overhead'?

<details><summary>Answer</summary>

**D. Create separate AWS KMS keys for each customer's data that have granular access control and logging enabled.**

The core requirement is to encrypt each customer's data separately using a centralized, low-overhead solution. Creating a distinct AWS KMS customer-managed key (CMK) for each customer directly fulfills this mandate. This approach provides cryptographic isolation, as each customer's data is protected by a unique key. It also enables granular, customer-specific access controls through key policies and detailed audit trails via AWS CloudTrail, which are essential for compliance. As AWS KMS is a fully managed service, this solution has the least operational overhead compared to managing keys or hardware manually. Why Incorrect Options are Wrong: A. Storing raw encryption keys in an S3 bucket is a significant security anti-pattern and creates high operational overhead for key management. B. Deploying and managing a hardware security appliance introduces substantial operational complexity, vio

</details>

### 9. ce-44 `least-ops` `security`

A company is building a cloud-based application on AWS that will handle sensitive customer dat a. The application uses Amazon RDS for the database. Amazon S3 for object storage, and S3 Event Notifications that invoke AWS Lambda for serverless processing. The company uses AWS IAM Identity Center to manage user credentials. The development, testing, and operations teams need secure access to Amazon RDS and Amazon S3 while ensuring the confidentiality of sensitive customer data. The solution must comply with the principle of least privilege. Which solution meets these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Enable IAM Identity Center with an Identity Center directory. Create and configure permission sets with granular access to Amazon RDS and Amazon S3. Assign all the teams to groups that have specific access with the permission sets.**

The company already uses AWS IAM Identity Center, which is the recommended service for centrally managing workforce access to AWS accounts and applications. The most efficient and scalable solution is to leverage this existing system. By creating groups for each team (development, testing, operations) and attaching granular permission sets, the company can manage access based on job functions. This approach adheres to the principle of least privilege by defining specific permissions for Amazon RDS and Amazon S3 in the permission sets. It also minimizes operational overhead, as administrators only need to manage group memberships and permission sets, rather than individual user policies. Why Incorrect Options are Wrong: A. This describes using standard IAM roles, which is less efficient than using IAM Identity Center's permission sets and group management, especially since Identity Center

</details>

### 10. ce-45 `security`

A company has applications that run in an organization in AWS Organizations. The company outsources operational support of the applications. The company needs to provide access for the external support engineers without compromising security. The external support engineers need access to the AWS Management Console. The external support engineers also need operating system access to the company's fleet of Amazon EC2 instances that run Amazon Linux in private subnets. Which solution will meet these requirements MOST securely?

<details><summary>Answer</summary>

**A. Confirm that AWS Systems Manager Agent (SSM Agent) is installed on all instances. Assign an instance profile with the necessary policy to connect to Systems Manager. Use AWS IAM IdentityCenter to provide the external support engineers console access. Use Systems Manager Session Manager to assign the required permissions.**

This solution provides the most secure and manageable access. AWS IAM Identity Center (formerly AWS SSO) is the recommended best practice for centrally managing user access to multiple AWS accounts within an AWS Organization, eliminating the need for insecure, long-term local IAM users in each account. For OS-level access, AWS Systems Manager Session Manager provides secure, auditable shell access to instances in private subnets without requiring bastion hosts, SSH keys, or opening inbound ports (like SSH port 22) in security groups. Access is controlled through fine-grained IAM policies, and all session activity can be logged to Amazon S3 or CloudWatch Logs for auditing, fulfilling the requirement for maximum security. Why Incorrect Options are Wrong: B: Providing local IAM user credentials in each account is not a secure or scalable practice. It creates credential sprawl and makes cent

</details>

### 11. ce-46 `least-ops` `security`

A company is designing a new internal web application in the AWS Cloud. The new application must securely retrieve and store multiple employee usernames and passwords from an AWS managed service. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Store the employee credentials in AWS Secrets Manager. Use AWS Cloud Formation and the BatchGetSecretValue API to retrieve the usernames and passwords from Secrets Manager.**

AWS Secrets Manager is the purpose-built service for securely storing, managing, and retrieving secrets such as usernames and passwords. It offers features like automatic secret rotation, which significantly reduces operational overhead compared to manual management. The BatchGetSecretValue API call is a specific function within the Secrets Manager service designed to efficiently retrieve multiple secret values in a single request. Using AWS CloudFormation to provision the secrets as part of the infrastructure deployment is a standard Infrastructure as Code (IaC) best practice. This combination provides a secure, scalable, and low-overhead solution that directly meets all the stated requirements. Why Incorrect Options are Wrong: A. The BatchGetSecretValue API is part of AWS Secrets Manager, not AWS Systems Manager Parameter Store. This option incorrectly pairs an API with the wrong servi

</details>

### 12. ce-57

A company needs a solution to enforce data encryption at rest on Amazon EC2 instances. The solution must automatically identify noncompliant resources and enforce compliance policies on findings. Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**A. Use an IAM policy that allows users to create only encrypted Amazon Elastic Block Store (Amazon EBS) volumes. Use AWS Config and AWS Systems Manager to automate the detection and remediation of unencrypted EBS volumes.**

This solution provides a comprehensive, multi-layered approach with minimal administrative effort. An IAM policy proactively prevents the creation of unencrypted Amazon Elastic Block Store (EBS) volumes, which is the most efficient first line of defense. For any existing or mistakenly created non-compliant resources, AWS Config is the designated service for continuously monitoring and assessing resource configurations against desired policies. It has a managed rule (encrypted-volumes) specifically for this purpose. Upon detecting a non-compliant volume, AWS Config can automatically trigger a remediation action using an AWS Systems Manager Automation document to enforce encryption, fulfilling all requirements in a highly automated and integrated fashion. Why Incorrect Options are Wrong: B: This is a custom solution requiring development and maintenance of Lambda functions, which incurs hi

</details>

### 13. ce-60

A company wants to restrict access to the content of its web application. The company needs to protect the content by using authorization techniques that are available on AWS. The company also wants to implement a serverless architecture for authorization and authentication that has low login latency. The solution must integrate with the web application and serve web content globally. The application currently has a small user base, but the company expects the application's user base to increase Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure Amazon Cognito for authentication. Implement Lambda@Edge for authorization. Configure Amazon CloudFront to serve the web application globally**

This solution meets all requirements by using a combination of serverless, globally distributed AWS services. Amazon Cognito provides a scalable, serverless user directory for authentication. Amazon CloudFront is the AWS Content Delivery Network (CDN) that serves the web application globally from edge locations, ensuring low latency for users worldwide. Lambda@Edge integrates with CloudFront to run authorization logic at the edge locations, closest to the user. This significantly reduces latency for authorization checks, as the request is validated before being forwarded to the origin, fulfilling the low login latency requirement. This architecture is fully serverless and scales automatically with user growth. Why Incorrect Options are Wrong: B: An Application Load Balancer (ALB) is a regional service and cannot serve content globally with low latency like a CDN. AWS Directory Service is

</details>

### 14. ce-63

A company is migrating applications from an on-premises Microsoft Active Directory that the company manages to AWS. The company deploys the applications in multiple AWS accounts. The company uses AWS Organizations to manage the accounts centrally. The company's security team needs a single sign-on solution across all the company's AWS accounts. The company must continue to manage users and groups that are in the on-premises Active Directory Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Enable AWS IAM Identity Center. Configure a two-way forest trust relationship to connect the company's self-managed Active Directory with IAM Identity Center by using AWS Directory Service for Microsoft Active Directory.**

AWS IAM Identity Center (formerly AWS SSO) is the recommended service for centrally managing single sign-on (SSO) access to multiple AWS accounts within an AWS Organization. To meet the requirement of using the existing on-premises Active Directory as the identity source, the standard and recommended architecture is to deploy AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). A trust relationship is then established between the AWS Managed Microsoft AD and the on-premises AD. This configuration allows IAM Identity Center to use the on-premises directory for user authentication, enabling employees to use their existing corporate credentials to access AWS accounts without migrating user identities. Why Incorrect Options are Wrong: A. This option proposes creating a new directory in AWS, which contradicts the requirement to continue managing users and groups in

</details>

### 15. ce-64 `security`

A company is designing a microservice-based architecture tor a new application on AWS. Each microservice will run on its own set of Amazon EC2 instances. Each microservice will need to interact with multiple AWS services such as Amazon S3 and Amazon Simple Queue Service (Amazon SQS). The company wants to manage permissions for each EC2 instance based on the principle of least privilege. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Create individual IAM roles based on the specific needs of each microservice. Associate the IAM roles with the appropriate EC2 instances.**

This solution directly implements the principle of least privilege. By creating a unique IAM role for each microservice with a policy that grants only the specific permissions required for its tasks (e.g., access to a particular S3 bucket or SQS queue), you ensure that each component has the minimum necessary access. Associating these tailored roles with the corresponding EC2 instances is the secure, recommended AWS best practice. This method uses temporary credentials that are automatically rotated, eliminating the security risks associated with managing and embedding long-term access keys within applications. Why Incorrect Options are Wrong: A. Storing IAM user access keys in application code is a significant security anti-pattern. It exposes long-term credentials that are difficult to rotate and manage securely. B. A single, overly permissive role for all microservices directly violat

</details>

### 16. ce-69

A company runs an application on EC2 instances that need access to RDS credentials stored in AWS Secrets Manager. Which solution meets this requirement?

<details><summary>Answer</summary>

**A. Create an IAM role, and attach the role to each EC2 instance profile. Use an identity-based policy to grant the role access to the secret.**

The most secure and standard AWS method for granting permissions to applications running on EC2 instances is to use an IAM role. An IAM role is associated with the EC2 instance via an instance profile. This provides the application with temporary, automatically rotated security credentials, eliminating the need to store long-term keys on the instance. An identity-based policy is then attached to this role, granting it the specific permissions (e.g., secretsmanager:GetSecretValue) required to access the designated secret in AWS Secrets Manager. This approach adheres to the principle of least privilege and is an AWS best practice. Why Incorrect Options are Wrong: B. You cannot attach an IAM user to an EC2 instance profile. Instance profiles are containers for IAM roles, not users. Using users would require managing static credentials. C. EC2 Instance Connect is a service for establishing S

</details>

### 17. ce-72

How can a company detect and notify security teams about PII in S3 buckets?

<details><summary>Answer</summary>

**A. Use Amazon Macie. Create an EventBridge rule for SensitiveData findings and send an SNS notification.**

Amazon Macie is the designated AWS service for discovering and protecting sensitive data, such as Personally Identifiable Information (PII), within Amazon S3 buckets. When Macie identifies sensitive data, it generates a "finding." These findings are automatically published as events to Amazon EventBridge. To meet the requirement, an EventBridge rule can be configured to filter for Macie's SensitiveData findings. The target for this rule should be an Amazon Simple Notification Service (SNS) topic. The security team can subscribe to this SNS topic to receive immediate notifications via email, SMS, or other configured endpoints, enabling a prompt response. Why Incorrect Options are Wrong: B. Amazon GuardDuty is a threat detection service that monitors for malicious activity and unauthorized behavior, not for discovering sensitive data content like PII within S3 objects. C. While Amazon Maci

</details>

### 18. ce-74

A company wants to provide a third-party system that runs in a private data center with access to its AWS account. The company wants to call AWS APIs directly from the third-party system. The company has an existing process for managing digital certificates. The company does not want to use SAML or OpenID Connect (OIDC) capabilities and does not want to store long-term AWS credentials. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure AWS Identity and Access Management (IAM) Roles Anywhere to exchange X.509 certificates for AWS credentials to interact with AWS APIs.**

AWS Identity and Access Management (IAM) Roles Anywhere is designed for this exact scenario. It allows workloads, such as servers running in a private data center, to use X.509 digital certificates to obtain temporary AWS credentials. This solution enables the third-party system to assume an IAM role and make secure API calls without needing to store long-term AWS access keys. It directly leverages the company's existing certificate management infrastructure and avoids SAML/OIDC federation, meeting all stated requirements. The temporary credentials are then used to sign API requests with Signature Version 4. Why Incorrect Options are Wrong: A. Mutual TLS (mTLS) authenticates the client and server at the transport layer but does not, by itself, provide the IAM credentials required to authorize AWS API requests. B. AWS Signature Version 4 is the protocol for signing and authenticating API

</details>

### 19. dt-75

A company is building software on AWS that requires access to various AWS services. Which configuration should be used to ensure that AWS credentials (i.e., Access Key ID/Secret Access Key combination) are not compromised?

<details><summary>Answer</summary>

**B. Assign an IAM role to the Amazon EC2 instance.**

</details>

### 20. ce-82

A company runs an application on Amazon EC2 instances. The instances need to access an Amazon RDS database by using specific credentials. The company uses AWS Secrets Manager to contain the credentials the EC2 instances must use. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Create an IAM role, and attach the role to each EC2 instance profile. Use an identity-based policy to grant the new IAM role access to the secret that contains the database credentials.**

The most secure and standard method for an AWS service, like an EC2 instance, to access another AWS service is by using an IAM role. An IAM role is attached to the EC2 instance via an instance profile, which provides temporary security credentials to the application running on the instance. An identity-based policy is then attached to this role, granting it the specific permissions (e.g., secretsmanager:GetSecretValue) required to retrieve the designated secret from AWS Secrets Manager. This approach avoids hardcoding long-term credentials and adheres to the principle of least privilege. Why Incorrect Options are Wrong: B. You attach IAM roles, not IAM users, to EC2 instance profiles. Using long-term IAM user credentials on an EC2 instance is a significant security anti-pattern. C. EC2 Instance Connect is a service for establishing SSH or RDP connections to an instance; it is not used by

</details>

### 21. dt-82 `availability`

You are developing a new mobile application and are considering storing user preferences in AWS. This would provide a more uniform cross-device experience to users using multiple mobile devices to access the application. The preference data for each user is estimated to be 50KB in size. Additionally, 5 million customers are expected to use the application on a regular basis. The solution needs to be cost-effective, highly available, scalable and secure. How would you design a solution to meet the above requirements?

<details><summary>Answer</summary>

**B. Setup a DynamoDB table with an item for each user having the necessary attributes to hold the user preferences. The mobile application will query the user preferences directly from the DynamoDB table. Utilize STS, Web Identity Federation, and DynamoDB Fine Grained Access Control to authenticate and authorize access.**

</details>

### 22. ce-84

A company stores data in Amazon S3. According to regulations, the data must not contain personally identifiable information (PII). The company recently discovered that S3 buckets have some objects that contain PII. The company needs to automatically detect PII in S3 buckets and to notify the company's security team. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Macie. Create an Amazon EventBridge rule to filter the SensitiveData event type from Macie findings and to send an Amazon Simple Notification Service (Amazon SNS) notification to the security team.**

Amazon Macie is the designated AWS service for discovering and protecting sensitive data, such as personally identifiable information (PII), within Amazon S3. Macie automatically generates findings when it detects potential PII. These findings are published as events to Amazon EventBridge. To meet the notification requirement, an EventBridge rule can be created to filter for these specific findings (e.g., by the SensitiveData event type). This rule can then invoke a target, such as an Amazon Simple Notification Service (SNS) topic, which is designed to send notifications directly to subscribers, like the security team, via email or SMS. This solution provides an automated, end-to-end workflow for PII detection and notification. Why Incorrect Options are Wrong: B. Amazon GuardDuty is a threat detection service that monitors for malicious activity and unauthorized behavior, not for scannin

</details>

### 23. ce-91

A company is developing a new application that will run on Amazon EC2 instances. The application needs to access multiple AWS services. The company needs to ensure that the application will not use long-term access keys to access AWS services.

<details><summary>Answer</summary>

**D. Create an IAM role that has permissions to access the required AWS services. Associate the IAM role with each EC2 instance profile.**

The most secure and recommended method for applications running on Amazon EC2 instances to access other AWS services is by using an IAM role associated with an EC2 instance profile. This approach provides temporary, automatically rotated credentials to the instance via its metadata service. The AWS SDK or CLI running on the instance can then use these credentials to make signed API calls. This completely eliminates the need to create, manage, or store long-term IAM user access keys, directly fulfilling the requirement to avoid them and adhering to AWS security best practices. Why Incorrect Options are Wrong: A. This method uses long-term access keys and embeds them in code, which is a severe security risk and directly contradicts the requirement. B. This option still relies on long-term IAM user access keys. While storing them in Secrets Manager is more secure than embedding them, it doe

</details>

### 24. ce-95

A company is developing a public web application that needs to access multiple AWS services. The application will have hundreds of users who must log in to the application first before using the services. The company needs to implement a secure and scalable method to grant the web application temporary access to the AWS resources. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an IAM role that has the access permissions the web application requires. Configure the web application to use AWS Security Token Service (AWS STS) to assume the IAM role. Use STS tokens to access the required AWS services.**

The most secure and scalable method for an application to access AWS resources is by using an IAM role with temporary credentials. The application, after authenticating its own users, uses the AWS Security Token Service (STS) AssumeRole API action to obtain short-lived credentials. These temporary credentials (access key ID, secret access key, and session token) are then used to make signed API calls to other AWS services. This approach avoids embedding long-lived IAM user access keys in the application, adhering to security best practices by providing automatically rotated, temporary access. Why Incorrect Options are Wrong: A: Creating a separate IAM role for each service is inefficient. A single role with a policy granting all necessary permissions is the standard and more manageable approach. C: AWS IAM Identity Center is for managing human workforce access to AWS accounts and cloud a

</details>

### 25. ce-102

A company is implementing a new policy to enhance the security of its AWS environment. The policy requires all administrative actions that users perform on the AWS Management Console to be secured by multi-factor authentication (MFA). Which solution will allow the company to enforce this policy in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create an IAM policy that requires MFA to be enabled for the IAM roles that administrators assume to perform administrative actions.**

The most operationally efficient and secure method to enforce Multi-Factor Authentication (MFA) for administrative actions is by using an IAM policy. This policy can be attached to the IAM roles that administrators assume. The policy should include a condition element with the aws:MultiFactorAuthPresent key set to true. This proactively denies any API calls for administrative actions if the user's session was not authenticated using MFA, directly enforcing the security requirement without manual intervention or delay. This is a preventative control that aligns with AWS security best practices. Why Incorrect Options are Wrong: A. Using the root account for routine administrative tasks is a significant security risk and violates the principle of least privilege. It should only be used for specific account management tasks. C. This is a detective control, not a preventative one. It only sen

</details>

### 26. ce-106

A global company is migrating its workloads from an on-premises data center to AWS. The AWS environment includes multiple AWS accounts. IAM roles. AWS Config rules, and a VPC. The company wants an automated process to provision new accounts on demand when the company's business units require new accounts. Which solution will meet these requirements with LEAST effort?

<details><summary>Answer</summary>

**A. Use AWS Control Tower to set up an organization in AWS Organizations. Use AWS Control Tower Account Factory for Terraform (AFT) to provision new AWS accounts.**

AWS Control Tower is a managed service designed to set up and govern a secure, multi-account AWS environment with the least effort. It automates the creation of a landing zone, which includes AWS Organizations, identity management, and preventative and detective guardrails. A core feature, Account Factory, provides a standardized, automated workflow for provisioning new AWS accounts that automatically conform to the organization's baseline policies, including VPCs, IAM roles, and AWS Config rules. Using Account Factory (or its Terraform extension, AFT) is the most direct and lowest-effort solution to meet the company's requirement for on-demand, standardized account provisioning. Why Incorrect Options are Wrong: B. This approach requires significant manual effort. While the AWS CLI can create an account, it does not automatically configure the necessary baseline resources like VPCs, IAM

</details>

### 27. ce-107 `least-ops`

An international company needs to share data from an Amazon S3 bucket to employees who are located around the world. The company needs a secure solution to provide employees with access to the S3 bucket. The employees are already enrolled in AWS IAM Identity Center. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a group for Amazon S3 access in IAM Identity Center. Add the employees who require access to the S3 bucket to the group. Create an IAM policy to allow Amazon S3 access from the group. Instruct employees to use the AWS access portal to access the AWS Management Console and navigate to the S3 bucket.**

The most efficient solution with the least operational overhead is to leverage the existing AWS IAM Identity Center infrastructure. By creating a group for S3 access within IAM Identity Center, administrators can centrally manage permissions. A single IAM policy (as part of a permission set) can be created and assigned to this group, granting the necessary S3 bucket access. Employees can then use their existing corporate credentials to sign in to the AWS access portal and navigate to the S3 console, inheriting the permissions granted to their group. This approach avoids custom application development, manual processes, and the management of separate infrastructure or credentials. Why Incorrect Options are Wrong: A. This creates significant operational overhead by requiring a custom application and manual intervention from a help desk for every access request, which is inefficient and doe

</details>

### 28. dt-108

After creating a new IAM user which of the following must be done before they can successfully make API calls?

<details><summary>Answer</summary>

**D. Create a set of Access Keys for the user.**

</details>

### 29. ce-109

A company stores sensitive customer data in an Amazon DynamoDB table. The company frequently updates the dat a. The company wants to use the data to personalize offers for customers. The company's analytics team has its own AWS account. The analytics team runs an application on Amazon EC2 instances that needs to process data from the DynamoDB tables. The company needs to follow security best practices to create a process to regularly share data from DynamoDB to the analytics team. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a cross-account IAM role. Create an IAM policy that allows the AWS account ID of the analytics team to access the DynamoDB table. Attach the IAM policy to the IAM role. Establish a trust relationship between accounts.**

The most secure and appropriate method for granting programmatic, cross-account access to AWS resources is by using an IAM role. This solution follows the principle of least privilege and the best practice of using temporary credentials. By creating a role in the source account with a trust policy that allows the analytics account to assume it, the company avoids sharing long-term credentials like IAM user access keys. The EC2 instances in the analytics account can assume this role to get temporary security credentials, enabling them to directly and securely access the frequently updated data in the DynamoDB table as needed. Why Incorrect Options are Wrong: A. Exporting data to S3 introduces latency, meaning the analytics team would be working with stale data, which is not ideal for a frequently updated source. B. Allowing public access to a table containing sensitive customer data is a

</details>

### 30. dt-110

IAM's Policy Evaluation Logic always starts with a default [...] for every request, except for those that use the AWS account's root security credentials?

<details><summary>Answer</summary>

**B. Deny.**

</details>

### 31. ce-113 `least-ops`

A company has an e-commerce site. The site is designed as a distributed web application hosted in multiple AWS accounts under one AWS Organizations organization. The web application is comprised of multiple microservices. All microservices expose their AWS services either through Amazon CloudFront distributions or public Application Load Balancers (ALBs). The company wants to protect public endpoints from malicious attacks and monitor security configurations. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS WAF to protect the public endpoints. Use AWS Firewall Manager from a dedicated security account to manage rules in AWS WAF. Use AWS Config rules to monitor the Regional and global WAF configurations.**

The solution requires protecting public endpoints (ALBs, CloudFront) across multiple accounts within an AWS Organization with minimal operational overhead. AWS WAF is the appropriate service for protecting against common web exploits. To manage WAF rules centrally across all accounts, AWS Firewall Manager is the ideal choice, as it is designed for this purpose within AWS Organizations, thus minimizing operational overhead. For monitoring, AWS Config is the correct service to assess and audit the configurations of AWS resources, including AWS WAF WebACLs, ensuring they comply with security policies. This combination provides a complete, centrally managed, and auditable security solution. Why Incorrect Options are Wrong: B: Applying WAF rules in each account individually creates high operational overhead, directly contradicting a key requirement of the question. Centralized management is n

</details>

### 32. dt-114

A corporate web application is deployed within an Amazon Virtual Private Cloud (VPC) and is connected to the corporate data center via an IPsec VPN. The application must authenticate against the on-premises LDAP server. After authentication, each logged-in user can only access an Amazon Simple Storage Space (S3) keyspace specific to that user. Which two approaches can satisfy these objectives? (Choose 2 answers)

<details><summary>Answer</summary>

**B. The application authenticates against LDAP and retrieves the name of an IAM role associated with the user. The application then calls the IAM Security Token Service to assume that IAM role. The application can use the temporary credentials to access the appropriate S3 bucket.; C. Develop an identity broker that authenticates against LDAP and then calls IAM Security Token Service to get IAM federated user credentials. The application calls the identity broker to get IAM federated user credentials with access to the appropriate S3 bucket.**

</details>

### 33. ce-118

A company manages multiple AWS accounts in an organization in AWS Organizations. The company's applications run on Amazon EC2 instances in multiple AWS Regions. The company needs a solution to simplify the management of security rules across the accounts in its organization. The solution must apply shared security group rules, audit security groups, and detect unused and redundant rules in VPC security groups across all AWS environments. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**A. Use AWS Firewall Manager to create a set of rules based on the security requirements. Replicate the rules to all the AWS accounts and Regions.**

AWS Firewall Manager is a security management service designed to centrally configure and manage firewall rules across multiple accounts and applications within an AWS Organization. It directly addresses all the requirements with the highest operational efficiency. A Firewall Manager security group policy can be used to establish a baseline set of common security group rules and apply them consistently across all accounts. Furthermore, Firewall Manager includes specific policy types for auditing existing security groups, identifying non-compliant rules, and detecting unused or redundant security groups, which simplifies cleanup and improves security posture. This managed service approach eliminates the need for custom scripts or complex deployments, making it the most efficient solution. Why Incorrect Options are Wrong: B: AWS Network Firewall is a VPC-level firewall for filtering traffi

</details>

### 34. ce-125

A company uses AWS to run its e-commerce platform, which is critical to its operations and experiences a high volume of traffic and transactions. The company has configured a multi-factor authentication (MFA) device to secure its AWS account root user credentials. The company wants to ensure that it will not lose access to the root user account if the MFA device is lost. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Add multiple MFA devices for the root user account to handle the disaster scenario.**

AWS Identity and Access Management (IAM) supports the assignment of multiple Multi-Factor Authentication (MFA) devices to a single AWS account root user or IAM user. By registering more than one MFA device, such as a hardware security key and a virtual authenticator app on a phone, the company creates a resilient authentication mechanism. If the primary MFA device is lost, stolen, or becomes unavailable, the company can use one of the other registered backup MFA devices to sign in to the root user account, thereby preventing a lockout scenario and ensuring business continuity. Why Incorrect Options are Wrong: A. A backup administrator account cannot perform certain tasks reserved only for the root user, so this does not fully restore access or control. C. It is not possible to create a new administrator account if you are locked out of the root account and have no other administrative ac

</details>

### 35. ce-127

A company is planning to migrate customer records to an Amazon S3 bucket. The company needs to ensure that customer records are protected against unauthorized access and are encrypted in transit and at rest. The company must monitor all access to the S3 bucket.

<details><summary>Answer</summary>

**A. Use AWS Key Management Service (AWS KMS) to encrypt customer records at rest. Create an S3 bucket policy that includes the aws:SecureTransport condition. Use an IAM policy to control access to the records. Use AWS CloudTrail to monitor access to the records.**

This option provides a comprehensive and correct security strategy for Amazon S3. Using AWS Key Management Service (SSE-KMS) for encryption at rest offers centralized key management and audit capabilities. Enforcing encryption in transit is correctly achieved by using the aws:SecureTransport condition in an S3 bucket policy, which denies any non-HTTPS requests. Access control is fundamentally managed through IAM policies, which provide granular permissions. Finally, AWS CloudTrail is the designated service for logging API calls (including S3 object-level access when data events are enabled), which directly fulfills the requirement to monitor all access to the records. This combination represents a robust, multi-layered security approach that meets all the specified requirements. Why Incorrect Options are Wrong: B: AWS Nitro Enclaves are isolated compute environments for EC2, not a storag

</details>

### 36. ce-129

A company uses AWS Organizations to manage multiple AWS accounts. Each department in the company has its own AWS account. A security team needs to implement centralized governance and control to enforce security best practices across all accounts. The team wants to have control over which AWS services each account can use. The team needs to restrict access to sensitive resources based on IP addresses or geographic regions. The root user must be protected with multi-factor authentication (MFA) across all accounts. Options:

<details><summary>Answer</summary>

**B. Use AWS Control Tower to establish a multi-account environment. Use service control policies (SCPs) to enforce service restrictions in AWS Organizations. Configure MFA for the root user across all accounts.**

AWS Control Tower is designed to set up and govern a secure, multi-account AWS environment based on best practices. It automates the creation of a "landing zone" using AWS Organizations. A core feature of AWS Organizations is Service Control Policies (SCPs), which provide centralized control over the maximum available permissions for all accounts. SCPs are the ideal mechanism to enforce which AWS services can be used. They can also enforce security controls, such as requiring multi-factor authentication (MFA) for the root user or restricting actions based on IP address or geographic region using condition keys. This combination directly addresses all the requirements for centralized governance and enforcement. Why Incorrect Options are Wrong: A. AWS managed prefix lists are for controlling traffic in security groups and route tables, not for restricting access to AWS services. Managing I

</details>

### 37. dt-129 `security`

An enterprise wants to use a third-party SaaS application. The SaaS application needs to have access to issue several API commands to discover Amazon EC2 resources running within the enterprise's account The enterprise has internal security policies that require any outside access to their environment must conform to the principles of least privilege and there must be controls in place to ensure that the credentials used by the 5aa5 vendor cannot be used by any other third party. Which of the following would meet all of these conditions?

<details><summary>Answer</summary>

**C. Create an IAM role for cross-account access allows the SaaS provider's account to assume the role and assign it a policy that allows only the actions required by the SaaS application.**

</details>

### 38. ce-137

A company needs to grant a team of developers access to the company's AWS resources. The company must maintain a high level of security for the resources. The company requires an access control solution that will prevent unauthorized access to the sensitive data. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Define IAM roles that have fine-grained permissions based on the principle of least privilege. Assign an IAM role to each developer.**

The most secure and scalable solution is to use IAM roles with permissions defined by the principle of least privilege. IAM roles provide temporary security credentials, which is an AWS security best practice that reduces the risk of compromised long-term keys. By creating roles with fine-grained permissions tailored to specific job functions (e.g., a 'developer' role), the company ensures that team members have only the access they need to perform their duties. This method directly prevents unauthorized access to sensitive data and aligns with maintaining a high level of security. Developers would assume these roles from their IAM user or federated identity. Why Incorrect Options are Wrong: A. Sharing credentials is a critical security anti-pattern. It eliminates individual accountability and makes it impossible to trace actions to a specific person, violating security and compliance pr

</details>

### 39. ce-138 `security`

A company is setting up a development environment on AWS for a team of developers. The team needs to access multiple Amazon S3 buckets to store project dat a. The team also needs to use Amazon EC2 to run development instances. The company needs to ensure that the developers have access only to specific Amazon S3 buckets and EC2 instances. Access permissions must be assigned according to each developer's role on the team. The company wants to minimize the use of permanent credentials and to ensure access is securely managed according to the principle of least privilege. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create IAM roles that have fine-grained permissions for Amazon S3 and Amazon EC2. Configure AWS IAM Identity Center to manage credentials for the developers.**

This solution directly addresses all requirements. AWS IAM Identity Center (formerly AWS SSO) is the recommended service for centrally managing workforce access to AWS accounts and applications. It integrates with identity providers and allows you to assign users to groups, which are then mapped to permission sets. These permission sets use IAM roles with fine-grained policies to enforce the principle of least privilege. This approach provides users with temporary credentials for accessing resources like EC2 and S3, which minimizes the security risks associated with permanent access keys. Why Incorrect Options are Wrong: A. Granting "administrative-level permissions" directly violates the principle of least privilege, which is a core requirement of the question. C. Creating IAM users with individual access keys results in long-lived, permanent credentials, which contradicts the requireme

</details>

### 40. dt-148

Which of the below mentioned options is a possible solution to avoid any security threat?

<details><summary>Answer</summary>

**B. Use the IAM role and assign it to the instance.**

</details>

### 41. dt-150

You are looking to migrate your Development (Dev) and Test environments to AWS. You have decided to use separate AWS accounts to host each environment. You plan to link each accounts bill to a Master AWS account using Consolidated Billing. To make sure you Keep within budget you would like to implement a way for administrators in the Master account to have access to stop, delete and/or terminate resources in both the Dev and Test accounts. Identify which option will allow you to achieve this goal.

<details><summary>Answer</summary>

**C. Create IAM users in the Master account Create cross-account roles in the Dev and Test accounts that have full Admin permissions and grant the Master.**

</details>

### 42. dt-154

A company is building a voting system for a popular TV show. Viewers will watch the performances then visit the show's website to vote for their favorite performer. It is expected that in a short period of time after the show has finished the site will receive millions of visitors. The visitors will first login to the site using their Amazon.com credentials and then submit their vote. After the voting is completed the page will display the vote totals. The company needs to build the site such that can handle the rapid influx of traffic while maintaining good performance but also wants to keep costs to a minimum. Which of the design patterns below should they use?

<details><summary>Answer</summary>

**D. Use CloudFront and an Elastic Load Balancer in front of an auto-scaled set of web servers. The web servers will first call the Login with Amazon service to authenticate the user. The web servers will process the user's vote and store the result into an SQS queue using IAM Roles for EC2 Instances to gain permissions to the SQS queue. A set of application servers will then retrieve the items from the queue and store the result into a DynamoDB table.**

</details>

### 43. ce-155 `security`

A company runs an application on Amazon EC2 instances. The application needs to access an Amazon RDS database. The company wants to grant the EC2 instances access permissions to the RDS database while following the principle of least privilege. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an IAM role that has a policy that grants the minimum required permissions to access the RDS database. Attach the IAM role to an EC2 instance profile. Associate the instance profile with the instances.**

The most secure and scalable method to grant permissions from an EC2 instance to another AWS service is by using an IAM role. An IAM role associated with an EC2 instance profile provides temporary security credentials to the application running on the instance. This avoids the security risk of storing long-term IAM user access keys on the instance itself. The policy attached to the role should be crafted to grant only the minimum permissions required for the application to access the RDS database (e.g., using IAM database authentication), thereby adhering to the principle of least privilege. Why Incorrect Options are Wrong: A. This solution violates the principle of least privilege by granting administrative permissions and uses insecure, hardcoded IAM user access keys. B. While this option applies least privilege to the policy, it relies on embedding insecure, long-term access keys on t

</details>

### 44. dt-155 `security`

You are designing a photo sharing mobile app. The application will store all pictures in a single Amazon S3 bucket. Users will upload pictures from their mobile device directly to Amazon S3 and will be able to view and download their own pictures directly from Amazon S3. You want to configure security to handle potentially millions of users in the most secure manner possible. What should your server-side application do when a new user registers on the photo sharing mobile application?

<details><summary>Answer</summary>

**D. Record the user's information in Amazon RDS and create a role in IAM with appropriate permissions. When the user uses their mobile app, create temporary credentials using the AWS Security Token Service `AssumeRole` function. Store these credentials in the mobile app's memory and use them to access Amazon S3. Generate new credentials the next time the user runs the mobile app.**

</details>

### 45. ce-159

A company is using AWS Identity and Access Management (IAM) Access Analyzer to refine IAM permissions for employee users. The company uses an organization in AWS Organizations and AWS Control Tower to manage its AWS accounts. The company has designated a specific member account as an audit account. A solutions architect needs to set up IAM Access Analyzer to aggregate findings from all member accounts in the audit account. What is the first step the solutions architect should take?

<details><summary>Answer</summary>

**B. Configure a delegated administrator account for IAM Access Analyzer in the AWS Control Tower management account. In the delegated administrator account for IAM Access Analyzer, specify the AWS account ID of the audit account.**

To centralize IAM Access Analyzer findings across an AWS Organization, the first and mandatory step is to designate a member account as the delegated administrator for the service. This action is performed from the organization's management account. Designating the audit account as the delegated administrator grants it the permissions to create and manage analyzers that collect findings from all other accounts in the organization. This establishes the central aggregation point before any analyzers can be configured or findings can be reviewed. Why Incorrect Options are Wrong: A. IAM Access Analyzer functions by analyzing resource-based policies, not by processing AWS CloudTrail logs. This describes setting up centralized logging, which is a different security function. C. IAM Access Analyzer does not require a manually created Amazon S3 bucket for its findings, nor does it require a cust

</details>

### 46. dt-159

A [...] is a document that provides a formal statement of one or more permissions.

<details><summary>Answer</summary>

**A. policy.**

</details>

### 47. ce-161

A company has AWS Lambda functions that use environment variables. The company does not want its developers to see environment variables in plaintext. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create an AWS Key Management Service (AWS KMS) key. Enable encryption helpers on the Lambda functions to use the KMS key to store and encrypt the environment variables.**

AWS Lambda provides built-in integration with AWS Key Management Service (KMS) to secure environment variables. By enabling encryption helpers in the Lambda console or API, you can encrypt environment variables at rest. Using a customer-managed KMS key allows for granular control over who can decrypt these variables. You can configure IAM policies to grant the Lambda function's execution role permission to decrypt the variables at runtime, while denying developers the kms:Decrypt permission on that specific key. This ensures that developers cannot view the sensitive information in plaintext, meeting the company's requirements directly and securely. Why Incorrect Options are Wrong: A: Migrating to EC2 is a drastic architectural change that avoids the problem rather than solving it within the existing serverless architecture. B: SSL/TLS encryption is for securing data in transit, not for e

</details>

### 48. ce-172

A company stores sensitive financial reports in an Amazon S3 bucket. To comply with auditing requirements, the company must encrypt the data at rest. Users must not have the ability to change the encryption method or remove encryption when the users upload dat a. The company must be able to audit all encryption and storage actions. Which solution will meet these requirements and provide the MOST granular control?

<details><summary>Answer</summary>

**B. Configure server-side encryption with AWS KMS (SSE-KMS) keys. Use an S3 bucket policy to reject any data that is not encrypted by the designated key.**

This solution meets all requirements by leveraging server-side encryption with AWS Key Management Service (SSE-KMS). Using SSE-KMS provides a centralized and auditable encryption mechanism. AWS KMS integrates with AWS CloudTrail to log every use of the encryption key, fulfilling the audit requirement. A bucket policy can enforce that all uploaded objects are encrypted with a specific KMS key by evaluating the s3:x-amz-server-side-encryption-aws-kms-key-id condition. This prevents users from changing or removing encryption. KMS key policies offer fine-grained permissions, providing the most granular control over who can use the key and for what purpose. Why Incorrect Options are Wrong: A. SSE-S3 does not provide an audit trail of key usage or the granular control over key policies that AWS KMS offers, failing the audit and granular control requirements. C. Client-side encryption cannot be

</details>

### 49. ce-177

A solutions architect is storing sensitive data generated by an application in Amazon S3. The solutions architect wants to encrypt the data at rest. A company policy requires an audit trail of when the AWS KMS key was used and by whom. Which encryption option will meet these requirements?

<details><summary>Answer</summary>

**B. Server-side encryption with AWS KMS managed keys (SSE-KMS)**

The core requirements are encryption at rest and a detailed audit trail of encryption key usage, including who used the key and when. Server-Side Encryption with AWS Key Management Service (SSE-KMS) is the only option that meets both criteria. AWS KMS is specifically designed to create and manage cryptographic keys and is integrated with AWS CloudTrail. This integration provides detailed logs of every API call made to KMS, including requests from Amazon S3 for encryption or decryption. These CloudTrail logs serve as the required audit trail, capturing the user identity, time of use, and the specific key involved. Why Incorrect Options are Wrong: A. Server-side encryption with Amazon S3 managed keys (SSE-S3): While this provides encryption, you do not have control over the keys or access to a detailed audit trail of their specific usage, as S3 manages the entire lifecycle. C. Server-side

</details>

### 50. ce-181

A multinational company operates in multiple AWS Regions. The company must ensure that its developers and administrators have secure, role-based access to AWS resources. The roles must be specific to each user's geographic location and job responsibilities. The company wants to implement a solution to ensure that each team can access only resources within the team's Region. The company wants to use its existing directory service to manage user access. The existing directory service organizes users into roles based on location. The system must be capable of integrating seamlessly with multi-factor authentication (MFA). Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure AWS IAM Identity Center with federated access. Integrate IAM Identity Center with the directory service to set up Region-specific IAM roles.**

AWS IAM Identity Center (formerly AWS SSO) is the recommended service for centrally managing access to multiple AWS accounts and applications. It integrates directly with existing directory services (like Active Directory or other SAML 2.0 identity providers), fulfilling the requirement to use the company's identity source. Using IAM Identity Center, administrators can map groups from the external directory to permission sets in AWS. These permission sets use IAM roles and can have policies attached that restrict access to specific AWS Regions using condition keys like aws:RequestedRegion. This directly addresses the need for role-based, geographically-specific access. IAM Identity Center also seamlessly supports multi-factor authentication (MFA), which can be enforced either within the service or at the identity provider level. Why Incorrect Options are Wrong: A. This is too low-level.

</details>

### 51. ce-183 `least-ops`

A company needs to provide a team of contractors with temporary access to the company's AWS resources for a short-term project. The contractors need different levels of access to AWS services. The company needs to revoke permissions for all the contractors when the project is finished. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS Security Token Service (AWS STS) to generate temporary credentials for the contractors. Provide the contractors access based on predefined roles. Set the access to automatically expire when the project is finished.**

The most efficient and secure method to provide temporary access is by using AWS Security Token Service (STS) in conjunction with IAM roles. This approach allows you to create distinct IAM roles with specific, least-privilege permissions tailored to different contractor needs. Contractors can then assume a role to receive temporary security credentials with a predefined expiration time. This automates the access revocation process, as the credentials automatically become invalid upon expiration, directly fulfilling the requirement to revoke permissions with the least operational overhead. This method avoids the security risks and manual effort associated with long-lived IAM user credentials. Why Incorrect Options are Wrong: A. Creating IAM users generates long-term credentials and requires manual deactivation, which increases operational overhead and the risk of forgotten, active account

</details>

### 52. dt-187

True or False: Amazon EC2 has no Amazon Resource Names (ARNs) because you can't specify a particular Amazon EC2 resource in an IAM policy.

<details><summary>Answer</summary>

**A. True.**

</details>

### 53. ce-188

A company plans to store sensitive user data on Amazon S3. Internal security compliance requirements mandate encryption of data before sending it to Amazon S3. What should a solutions architect recommend to satisfy these requirements?

<details><summary>Answer</summary>

**D. Client-side encryption with a key stored in AWS Key Management Service (AWS KMS)**

The core requirement is to encrypt data before sending it to Amazon S3. This process is known as client-side encryption. The client application encrypts the data objects first and then uploads the encrypted objects to Amazon S3. In this model, Amazon S3 receives already encrypted data and does not play a role in the encryption or decryption process. Using AWS Key Management Service (AWS KMS) provides a secure and managed way to handle the encryption keys (specifically, the customer master key used to encrypt the data keys) required for this client-side encryption process, aligning with best practices for key management. Why Incorrect Options are Wrong: A. Server-side encryption with customer-provided encryption keys: This is server-side encryption (SSE-C). Encryption occurs after the data is received by Amazon S3, not before, which violates the stated requirement. B. Client-side encrypti

</details>

### 54. ce-193

A company has established a new AWS account. The account is newly provisioned and no changes have been made to the default settings. The company is concerned about the security of the AWS account root user. What should be done to secure the root user?

<details><summary>Answer</summary>

**B. Create IAM users for daily administrative tasks. Enable multi-factor authentication on the root user.**

AWS security best practices strongly recommend securing the AWS account root user by enabling Multi-Factor Authentication (MFA). The root user has unrestricted access to all resources in the account and should not be used for daily administrative tasks. Instead, individual IAM users with the minimum necessary permissions (the principle of least privilege) should be created for all human and programmatic access. This dual approach of locking down the root user with MFA and delegating daily tasks to IAM users is a foundational security measure for any AWS account. Why Incorrect Options are Wrong: A. The AWS account root user cannot be disabled. It is required for a small number of specific account and service management tasks. C. Creating and using root user access keys is strongly discouraged. If compromised, these keys provide unrestricted programmatic access to the entire account. D. Us

</details>

### 55. ce-194 `least-ops`

A company runs an application on premises. The application needs to periodically upload large files to an Amazon S3 bucket. A solutions architect needs a solution to provide the application with short- lived authenticated access to the S3 bucket. The solution must not use long-term credentials. The solution needs to be secure and scalable. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Configure a trust relationship between the on-premises server and AWS Security Token Service (AWS STS). Generate credentials by assuming an IAM role for each upload operation.**

The most secure and efficient solution is to use AWS Security Token Service (STS) to generate temporary, short-lived credentials. An on-premises application can be configured to call the sts:AssumeRole API action. This action returns a set of temporary credentials (an access key ID, a secret access key, and a session token) that the application can use to make authenticated requests to the S3 bucket. This method directly fulfills the requirements by avoiding the use of static, long-term credentials, enhancing security by limiting the credential lifetime, and representing the lowest operational overhead compared to infrastructure-heavy solutions. Why Incorrect Options are Wrong: A. This solution uses long-term credentials (IAM user access keys), which violates a key requirement and is an AWS security anti-pattern. B. This approach is overly complex and introduces significant operational o

</details>

### 56. ce-200

A company runs several custom applications on Amazon EC2 instances. Each team within the company manages its own set of applications and backups. To comply with regulations, the company must be able to report on the status of backups and ensure that backups are encrypted. Which solution will meet these requirements with the LEAST effort?

<details><summary>Answer</summary>

**D. Use AWS Config and AWS Backup Audit Manager to ensure compliance. Review generated reports daily.**

AWS Backup Audit Manager is a purpose-built feature within AWS Backup designed to help you audit and report on the compliance of your data protection policies. It allows you to define controls (e.g., backups must be encrypted, backups must occur with a certain frequency) and automatically generates reports to demonstrate compliance with regulatory requirements. This managed service directly addresses the need to report on backup status and ensure encryption with minimal operational overhead, making it the "least effort" solution compared to building custom scripts or performing manual checks. Why Incorrect Options are Wrong: A. Creating a custom Lambda function requires significant development, testing, and maintenance effort, which is not the path of "least effort" compared to a managed service. B. Manual daily checks are operationally intensive, prone to human error, and do not scale e

</details>

### 57. ce-201

A healthcare company stores personally identifiable information (PII) data in an Amazon RDS for Oracle database. The company must encrypt the PII data at rest. The company must use dedicated hardware modules to store and manage the encryption keys.

<details><summary>Answer</summary>

**B. Use AWS CloudHSM backed AWS KMS keys to configure transparent encryption for the RDS database.**

The requirement is to encrypt an Amazon RDS for Oracle database at rest, with encryption keys managed in dedicated hardware modules. Amazon RDS integrates with AWS Key Management Service (KMS) to encrypt databases. To satisfy the requirement for dedicated hardware, AWS KMS can be configured to use a custom key store backed by an AWS CloudHSM cluster. This ensures that the KMS keys used for RDS encryption are generated, stored, and used exclusively within your single-tenant Hardware Security Modules (HSMs). RDS for Oracle uses Transparent Data Encryption (TDE), and this integrated solution transparently encrypts the data while meeting the stringent key management requirements. Why Incorrect Options are Wrong: A: This option is less precise. You cannot directly configure RDS to store and manage keys in CloudHSM. The correct and required integration path is through an AWS KMS custom key sto

</details>

### 58. dt-203

Which service enables AWS customers to manage users and permissions in AWS?

<details><summary>Answer</summary>

**B. AWS Identity and Access Management (IAM).**

</details>

### 59. ce-206

A company uses Amazon EC2 instances to host its internal systems. As part of a deployment operation, an administrator tries to use the AWS CLI to terminate an EC2 instance. However, the administrator receives a 403 (Access Denied) error message. The administrator is using an IAM role that has the following IAM policy attached: What is the cause of the unsuccessful request?

<details><summary>Answer</summary>

**D. The request to terminate the EC2 instance does not originate from the CIDR blocks 192.0.2.0/24 or 203.0.113.0/24.**

The IAM policy includes a Condition element that restricts access based on the source IP address. The Allow effect for the ec2:TerminateInstances action is only granted if the API request originates from an IP address within the 192.0.2.0/24 or 203.0.113.0/24 ranges. Since the administrator received an "Access Denied" error, the condition was not met. This means the AWS CLI command was executed from a machine with an IP address outside of the specified CIDR blocks, leading to the request being denied. Why Incorrect Options are Wrong: A. Amazon EC2 instances do not support resource-based policies. Permissions for EC2 actions are managed through identity-based policies like the one shown. B. The Principal element is not specified in identity-based policies because the principal is implicitly the user, group, or role to which the policy is attached. C. The policy explicitly includes "Action

</details>

### 60. dt-213

You log in to IAM on your AWS console and notice the following message. 'Delete your root access keys.' Why do you think IAM is requesting this?

<details><summary>Answer</summary>

**D. Because they provide unrestricted access to your AWS resources.**

</details>

### 61. ce-221 `least-ops`

A home security company is expanding globally and needs to encrypt customer data. The company does not want to manage encryption keys. The keys must be usable in multiple AWS Regions, and access to the keys must be controlled. Which solution meets these requirements with the least operational overhead?

<details><summary>Answer</summary>

**A. Use AWS KMS multi-Region keys. Apply tags and use ABAC condition keys for access control.**

The solution requires a managed encryption service that minimizes operational overhead, supports keys across multiple AWS Regions, and provides granular access control. AWS Key Management Service (KMS) multi-Region keys are designed for this exact scenario. They are AWS-managed keys that share the same key ID and key material across specified Regions, simplifying cross-Region data encryption and decryption. This eliminates the need for the company to manage key material or synchronization. Access control can be effectively implemented using Attribute-Based Access Control (ABAC) by applying tags to the keys and using condition keys in IAM and key policies, which meets the access control requirement with minimal management effort. Why Incorrect Options are Wrong: B. Use AWS KMS imported key material in multiple Regions with ABAC-based policies. This option requires the company to generate

</details>

### 62. et-222

A company has hired an external vendor to perform work in the company’s AWS account. The vendor uses an automated tool that is hosted in an AWS account that the vendor owns. The vendor does not have IAM access to the company’s AWS account. How should a solutions architect grant this access to the vendor?

<details><summary>Answer</summary>

**A. Create an IAM role in the company’s account to delegate access to the vendor’s IAM role. Attach the appropriate IAM policies to the role for the permissions that the vendor requires.**

IAM roles allow you to delegate access to resources in your AWS account to another AWS account. In this case, you can create a role in your account and grant the vendor's IAM role permission to assume that role.  By doing this, the vendor can use temporary security credentials obtained by assuming the role to access resources in your account. This ensures that the vendor doesn't need IAM credentials from your account.

</details>

### 63. et-223

A company has deployed a Java Spring Boot application as a pod that runs on Amazon Elastic Kubernetes Service (Amazon EKS) in private subnets. The application needs to write data to an Amazon DynamoDB table. A solutions architect must ensure that the application can interact with the DynamoDB table without exposing traffic to the internet. Which combination of steps should the solutions architect take to accomplish this goal? (Choose two.)

<details><summary>Answer</summary>

**A. Attach an IAM role that has sufficient privileges to the EKS pod.**

D. Create a VPC endpoint for DynamoDB. Most Voted  This IAM role should have the necessary permissions to interact with DynamoDB. You can attach the IAM role to the pod using Kubernetes service account annotations or other mechanisms.  By creating a VPC endpoint for DynamoDB, you allow your EKS pods to access DynamoDB directly within the AWS network without traversing the public internet. This enhances security and reduces the risk of exposure.

</details>

### 64. ce-225 `least-ops`

A home security company is expanding its business globally. The company needs to encrypt customer data. The company does not want to manage its own keys. The company needs the keys to be usable in multiple AWS Regions and needs to control access to the keys. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Key Management Service (AWS KMS) to create multi-Region keys. Apply tags to identify each key. Use attribute-based access control (ABAC) condition keys to control access to the keys.**

The solution requires a low-overhead, multi-region encryption key strategy where the company does not manage the key material. AWS Key Management Service (KMS) is a managed service that abstracts away the complexity of operating a key management infrastructure. KMS multi-Region keys are specifically designed to simplify encrypting data in one AWS Region and decrypting it in another, meeting the global business requirement with minimal operational effort. Using attribute-based access control (ABAC) with tags on these keys provides a scalable and flexible method for controlling access, fulfilling the final requirement. This combination directly addresses all constraints with the least operational burden. Why Incorrect Options are Wrong: B: Importing key material (BYOK) requires the company to generate, secure, and manage its own keys, which directly contradicts the requirement to not manag

</details>

### 65. dt-226

Is there a method in the IAM system to allow or deny access to a specific instance?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 66. dt-227

Using Amazon IAM, can I give permission based on organizational groups?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 67. et-232

A company runs demonstration environments for its customers on Amazon EC2 instances. Each environment is isolated in its own VPC. The company’s operations team needs to be notified when RDP or SSH access to an environment has been established.

<details><summary>Answer</summary>

**C. Publish VPC flow logs to Amazon CloudWatch Logs. Create the required metric filters. Create a CloudWatch metric alarm with a notification action for when the alarm is in the ALARM state.**

VPC flow logs record every accepted and rejected connection on the network interfaces in each VPC, including the destination port, so SSH (port 22) and RDP (port 3389) connections show up in the log records. Sending those logs to CloudWatch Logs lets you attach a metric filter that increments a custom metric whenever a record matches one of those ports, and a CloudWatch alarm on that metric can publish to an SNS topic to notify the operations team. The instance-profile option is wrong because AmazonSSMManagedInstanceCore just grants the instance permission to talk to Systems Manager; it produces no alert. Note the honest limit of this design: flow logs show that a connection on those ports was accepted, not that a user successfully authenticated, which is all the question asks for.

</details>

### 68. ce-234 `security`

A company is designing a microservice-based architecture for a new application on AWS. Each microservice will run on its own set of Amazon EC2 instances. Each microservice will need to interact with multiple AWS services. The company wants to manage permissions for each EC2 instance according to the principle of least privilege. Which solution will meet this requirement with the LEAST administrative overhead?

<details><summary>Answer</summary>

**D. Create individual IAM roles based on the specific needs of each microservice. Add each IAM role to an instance profile that is associated with the appropriate EC2 instance.**

An IAM role can be scoped to exactly the API actions that a given microservice needs. Attaching that role to the EC2 instances through an instance profile lets the Amazon EC2 Instance Metadata Service deliver short-lived, automaticallyrotated credentials to the workload, eliminating hard-coded keys. Creating one role per microservice satisfies the principle of least privilege, while administration is minimal because no keys need rotation and roles are attached only once at launch or by a simple API call. This provides the tightest permission boundaries with the least ongoing effort compared with user keys, an overly broad shared role, or multiple AWS accounts. Why Incorrect Options are Wrong: A. Hard-coded access keys violate security best practices, require manual rotation, and grant static, long-lived credentials-high overhead and risk. B. One broad role grants every microservice more

</details>

### 69. et-234

A company is building a new web-based customer relationship management application. The application will use several Amazon EC2 instances that are backed by Amazon Elastic Block Store (Amazon EBS) volumes behind an Application Load Balancer (ALB). The application will also use an Amazon Aurora database. All data for the application must be encrypted at rest and in transit. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Key Management Service (AWS KMS) to encrypt the EBS volumes and Aurora database storage at rest. Attach an AWS Certificate Manager (ACM) certificate to the ALB to encrypt data in transit.**

Using AWS KMS to encrypt EBS volumes and Aurora database storage at rest is a good practice. You can specify a KMS key when creating these resources to ensure data encryption.  Attaching an ACM certificate to the ALB allows you to use HTTPS, which encrypts data in transit between clients and the ALB. This ensures secure communication over the network.

</details>

### 70. ce-235 `least-ops`

A company is developing a new application that uses Amazon EC2, Amazon S3, and AWS Lambda resources. The company wants to allow employees to access the AWS Management Console by using existing credentials that the company stores and manages in an on-premises Microsoft Active Directory. Each employee must have a specific level of access to the AWS resources that is based on the employee's role. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure AWS Directory Service to create an Active Directory in AWS Managed Microsoft AD. Establish a trust relationship with the on-premises Active Directory. Configure IAM roles and trust policies to give the employees access to the AWS resources.**

The requirement is to integrate an on-premises Microsoft Active Directory with AWS for console access with minimal operational overhead. The most direct and lowest-overhead solution is to use AWS Directory Service to create an AWS Managed Microsoft AD and establish a forest trust relationship with the on-premises directory. This allows users to authenticate with their existing corporate credentials. IAM roles can then be mapped to AD groups to enforce role-based access control. This approach uses fully managed AWS services, significantly reducing the administrative burden compared to building a custom solution or using less direct integration methods. Why Incorrect Options are Wrong: B. IAM does not offer direct LDAP integration for federating users for console access. This would require a custom-built or third-party solution, increasing overhead. C. Implementing a custom identity broker

</details>

### 71. ce-236

A company hosts an end-user application on Amazon EC2 instances behind an Application Load Balancer (ALB). The company needs to configure end-to-end encryption between the ALB and the EC2 instances. Which solution will meet this requirement with the LEAST operational effort?

<details><summary>Answer</summary>

**B. Import a third-party certificate bundle into AWS Certificate Manager (ACM). Generate a self- signed certificate on the EC2 instances. Associate the ACM imported third-party certificate with the ALB.**

For end-to-end encryption with minimal operational effort, you need certificates on both the ALB and EC2 instances. Option B correctly implements this by using ACM to manage the ALB certificate (reducing operational overhead) and self-signed certificates on EC2 instances for backend encryption. Self-signed certificates are acceptable for ALB-to-EC2 communication since the ALB doesn't validate backend certificates by default. This approach minimizes certificate management complexity while meeting the encryption requirement. Why Incorrect Options are Wrong: A: CloudHSM adds unnecessary complexity and cost for a simple TLS requirement. C: Installing third-party certificates on EC2 instances requires manual management and renewal, increasing operational effort. D: ACM certificates cannot be installed directly on EC2 instances; they only work with AWS-managed services.

</details>

### 72. ce-238

A company is building an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for its workloads. All secrets that are stored in Amazon EKS must be encrypted in the Kubernetes etcd key-value store. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a new AWS Key Management Service (AWS KMS) key. Enable Amazon EKS KMS secrets encryption on the Amazon EKS cluster.**

Amazon Elastic Kubernetes Service (Amazon EKS) provides a native feature to encrypt Kubernetes secrets at rest within the underlying etcd key-value store. This is achieved by enabling envelope encryption using a customer-managed AWS Key Management Service (KMS) key. When this feature is enabled on the EKS cluster, Kubernetes secrets are encrypted by EKS using a data key, and that data key is itself encrypted by the specified KMS key. This directly fulfills the requirement to encrypt all secrets stored in etcd. Why Incorrect Options are Wrong: A. AWS Secrets Manager stores secrets outside of the Kubernetes secrets object model and etcd. The requirement is to encrypt secrets within etcd. C. The Amazon EBS Container Storage Interface (CSI) driver is used for managing persistent storage volumes for pods, not for encrypting Kubernetes secrets in etcd. D. Enabling default EBS encryption encryp

</details>

### 73. ce-239

A company uses AWS WAF to protect its web applications. A solutions architect configures a web ACL that uses several rules, including a rule that inspects the HTTP request body for malicious content. The solutions architect notices that the web ACL is not inspecting large HTTP POST requests properly. As a result, suspicious activities are not being detected. Some large HTTP POST requests are more than 8 MB in size. The solutions architect must ensure that the web ACL inspects the large HTTP POST requests properly. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Create two custom AWS WAF rules. Configure one rule to block all oversized requests. Configure the second rule with a higher priority to allow large requests from legitimate hosts.**

AWS WAF has a default size limit of 8 KB for inspecting the body of an HTTP/S request. For requests with bodies larger than this limit, WAF's behavior is determined by the "oversize handling" setting in the rule. The proper way to manage this is to create a rule that specifically handles oversized components, typically by blocking them. To allow legitimate large requests, a separate, higher-priority rule can be configured to allow traffic from trusted sources (e.g., by IP address), bypassing the blocking rule. Why Incorrect Options are Wrong: B. AWS Shield Advanced is a managed DDoS protection service. It does not change the fundamental request body inspection size limits of AWS WAF. C. The Content-Type header informs WAF how to parse the body (e.g., as JSON), but it does not affect or override the size limitation for inspection. D. An AWS Lambda function (e.g., Lambda@Edge) cannot prepr

</details>

### 74. et-239

A solutions architect needs to design a new microservice for a company’s application. Clients must be able to call an HTTPS endpoint to reach the microservice. The microservice also must use AWS Identity and Access Management (IAM) to authenticate calls. The solutions architect will write the logic for this microservice by using a single AWS Lambda function that is written in Go 1.x. Which solution will deploy the function in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create a Lambda function URL for the function. Specify AWS_IAM as the authentication type.**

Explanation: A Lambda function URL gives the function its own HTTPS endpoint directly, with no separate API Gateway resource to create or manage. Setting the auth type to AWS_IAM satisfies the IAM-authentication requirement, making this the more operationally efficient option compared to fronting the function with a full API Gateway REST API.

</details>

### 75. ce-242

A solutions architect has created an AWS Lambda function that is written in Java. A company will use the Lambda function as a new microservice for its application. The company's customers must be able to call an HTTPS endpoint to reach the microservice. The microservice must use AWS Identity and Access Management (IAM) to authenticate calls. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an AWS Lambda function URL for the Lambda function. Specify AWSIAM as the authentication type.**

AWS Lambda Function URLs are a built-in feature that provides a dedicated HTTPS endpoint for a Lambda function. This directly meets the requirement for an HTTPS endpoint without needing an additional service like API Gateway or CloudFront. When creating a function URL, you can configure the authentication type. Specifying AWSIAM enforces that all incoming requests must be signed with valid AWS credentials, fulfilling the IAM authentication requirement. This is the simplest, most direct, and most cost-effective solution for this specific use case. Why Incorrect Options are Wrong: A. A Lambda authorizer is for custom authorization logic. For standard IAM authentication with API Gateway, you would configure the method's authorization type, not use a separate authorizer function. C. Lambda@Edge is designed for running code at edge locations to customize content delivered by CloudFront, not f

</details>

### 76. ce-247

A company uses AWS CloudFormation to deploy IAM resources within accounts that AWS Control Tower governs. The security team wants to prevent the deployment of IAM roles that include inline policies with the following statements: "Effect": "Allow", "Action": "*", "Resource": "*" Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Use AWS Control Tower proactive controls to block CloudFormation stacks that match these inline policy statements.**

The requirement is to prevent the deployment of non-compliant IAM resources. AWS Control Tower proactive controls are designed for this exact purpose. They are implemented using AWS CloudFormation hooks, which run checks on resources before they are provisioned by CloudFormation. If a resource, such as an IAM role with an overly permissive inline policy, violates a proactive control, CloudFormation will fail the deployment, thereby preventing the non-compliant resource from ever being created. This directly meets the requirement. Why Incorrect Options are Wrong: B. Detective controls operate after a resource has been deployed. They can detect non-compliance but cannot prevent the initial deployment, which is the core requirement. C. AWS Config with auto-remediation is a reactive mechanism. It detects a non-compliant resource after it has been created and then attempts to fix it, rather t

</details>

### 77. ce-248

A company wants DevOps teams to create IAM roles, but no role may have administrative permissions. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use SCPs to require a permissions boundary when creating IAM roles.**

To allow IAM role creation while preventing administrative permissions, the best practice is to use a Service Control Policy (SCP) within AWS Organizations. An SCP can enforce a rule that requires any newly created IAM role to have a specific permissions boundary attached. This boundary acts as a ceiling, defining the maximum permissions the role can ever have, regardless of the identity-based policies attached to it. This is a preventative control that ensures no role can be created with permissions exceeding those defined in the boundary, effectively blocking the creation of administrative roles. Why Incorrect Options are Wrong: A. Denying a specific policy like AdministratorAccess is insufficient, as users could create a custom policy with equivalent : permissions. C. A reactive "detect and delete" approach is insecure as it leaves a window of opportunity for misuse before the noncomp

</details>

### 78. ce-249 `least-ops`

A company requires centralized auditing for all AWS accounts and compliance monitoring against AWS Foundational Security Best Practices (FSBP) with minimal operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy AWS Control Tower in the management account. Enable AWS Security Hub and Account Factory.**

AWS Control Tower provides the most streamlined way to set up and govern a secure, multi-account AWS environment with minimal operational overhead. By deploying it in the management account, it establishes a landing zone with best-practice blueprints, mandatory guardrails for security, and centralized logging. It automates the provisioning of new accounts using Account Factory. Critically, Control Tower integrates with AWS Security Hub, which can be enabled to continuously monitor compliance against security standards like the AWS Foundational Security Best Practices (FSBP) across all accounts in the organization, providing a centralized view. Why Incorrect Options are Wrong: B. AWS Control Tower must be deployed in the management account of an AWS Organization to govern member accounts; it cannot operate from a member account. C. This is an incomplete solution. AWS Managed Services (AMS

</details>

### 79. ce-250

A company has an application that runs on Amazon EC2 instances and uses an Amazon Aurora database. The EC2 instances connect to the Aurora database by using user names and passwords that the company stores locally in a file. The company changes the user names and passwords every month. The company wants to minimize the operational overhead of credential management. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Store the credentials as a secret within AWS Secrets Manager. Assign IAM permissions to the secret. Reconfigure the application to call the secret. Enable rotation on the secret and configure rotation to occur on a monthly schedule.**

AWS Secrets Manager is the ideal service for managing database credentials. It securely stores secrets and, crucially, offers automated rotation capabilities that integrate directly with services like Amazon Aurora. By configuring the application to retrieve credentials from Secrets Manager and enabling automatic monthly rotation, the company completely offloads the operational overhead of manual credential management. This solution is secure, automated, and specifically designed for this use case, directly meeting all requirements. Why Incorrect Options are Wrong: B. AWS Systems Manager Parameter Store can store secrets, but its automated rotation is less straightforward and integrated than Secrets Manager for databases. C. Storing a credentials file in an S3 bucket is not a recommended security practice for active database credentials and adds retrieval overhead. D. Using an encrypted

</details>

### 80. ce-251

A company has deployed a non-production Amazon EC2 instance by using an Amazon Linux AMI in a private subnet. The company wants to allow a group of developers to connect to the EC2 instance remotely by using SSH without exposing the EC2 instance to the internet. The developers must be able to connect to the EC2 instance through the AWS Management Console. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an EC2 Instance Connect Endpoint in the same subnet as the EC2 instance. Attach a security group to the endpoint that allows inbound connections on port 443. Assign the AmazonEC2InstanceConnect IAM managed policy to the group of developers.**

EC2 Instance Connect Endpoint enables console-initiated SSH to instances located in private subnets without requiring a public IP or bastion. Traffic from the developer's browser is tunneled over TLS (TCP 443) to the endpoint, which then makes an internal TCP-22 connection to the instance. The endpoint's security group therefore needs port 443 open, not 22. Developers require the AmazonEC2InstanceConnect managed policy to push temporary SSH keys. Why Incorrect Options are Wrong: A. SSM Session Manager provides command-line sessions, not native SSH, and port 22 isn't used. C. Endpoint listens on 443; authorizing 22 prevents the TLS handshake, blocking connections. D. AmazonSSMReadOnlyAccess does not allow an instance to register with SSM, and Session Manager still is not SSH.

</details>

### 81. dt-253

In AWS, which security aspects are the customer's responsibility? (Choose 4 answers)

<details><summary>Answer</summary>

**A. Security Group and ACL (Access Control List) settings.; C. Patch management on the EC2 instance's operating system.; D. Life-cycle management of IAM credentials.; F. Encryption of EBS (Elastic Block Storage) volumes.**

</details>

### 82. ce-254

A company needs to allow a vendor to access CloudWatch Logs in the company's AWS account by using IAM roles for cross-account access. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a role in the company account with permissions and trust the vendor role.**

To establish cross-account access, the account containing the resources (the company) must create an IAM role. This role needs two policies: 1) a permissions policy that grants the necessary permissions (e.g., read access to CloudWatch Logs), and 2) a trust policy that specifies the external principal (the vendor's AWS account or a specific role within it) that is allowed to assume the role. The vendor's IAM user/role would then use the AWS STS AssumeRole API action to obtain temporary credentials for the company's role. Why Incorrect Options are Wrong: A. The trust relationship is one-way; the company's role must trust the vendor's account, not another role in the company's own account. B. The role with permissions to access resources must be created in the account that owns those resources (the company account), not the vendor's account. C. Trusting a role in the same account does not

</details>

### 83. ce-259 `security`

A company has hired an external vendor to work in the company's AWS account. The vendor uses an automated tool that the vendor hosts in its own AWS account. The vendor does not have IAM access to the company's AWS account. A solutions architect needs to grant access to the vendor. Which solution will meet these requirements MOST securely?

<details><summary>Answer</summary>

**A. Create an IAM role in the company's account to delegate access to the vendor's IAM role. Attach the appropriate IAM policies to the new IAM role to grant the permissions that the vendor requires.**

The most secure method for granting cross-account access to an automated tool is by using an IAM role. The company (the trusting account) creates an IAM role with a trust policy that specifies the vendor's AWS account (the trusted account) as the principal. The role is also attached a permissions policy defining exactly what actions the vendor's tool can perform. The vendor's tool can then programmatically call the AssumeRole API action to obtain temporary security credentials. This approach adheres to the principle of least privilege and avoids the use of long-term credentials like access keys, which is a security best practice. Why Incorrect Options are Wrong: B. Creating an IAM user with a password or access keys involves sharing long-term credentials, which is less secure than using temporary credentials obtained by assuming a role. C. It is not possible to add an IAM user from one A

</details>

### 84. ce-262

A global company operates in multiple AWS Regions to meet data residency requirements. The company uses AWS Organizations to manage its accounts. The company wants to restrict IAM roles and access to specific Regions to prevent accidental data operations across geographic boundaries. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure IAM policies by using the aws:RequestedRegion condition.**

The most direct and effective method to restrict IAM actions to specific AWS Regions is by using the aws:RequestedRegion global condition key in IAM policies. This key allows you to create policy statements that explicitly deny any action not performed in an approved list of Regions. This is a preventative control that can be attached to IAM users, groups, or roles to enforce data residency and prevent accidental cross-region operations, directly meeting the company's requirements for regional access restriction. Why Incorrect Options are Wrong: A. This is too specific. While an SCP is a valid tool for this, restricting only ec2:RunInstances does not meet the broader requirement of restricting all access and operations. C. The aws:SourceIp condition key restricts access based on the caller's IP address, not the AWS Region where the API call is targeted. It is used for network-based contr

</details>

### 85. ce-264

A company needs to save confidential medical results in an Amazon S3 bucket. The repository must allow a few approved users to add new files. The repository must restrict all other users to read-only access by using a write once, read many (WORM) approach. The company must keep every file in the repository for a minimum of 1 year after its creation date. Which solution will meet these requirements with the LEAST implementation effort?

<details><summary>Answer</summary>

**B. Use S3 Object Lock in compliance mode with a retention period of 1 year. Use an IAM policy that restricts file access to specified approved users.**

S3 Object Lock is the purpose-built AWS feature for implementing a write-once-read-many (WORM) model. Using Object Lock in compliance mode with a 1-year retention period directly meets the requirements to prevent file modification or deletion for a minimum duration, even by the root account. This is the most direct and secure way to enforce the retention policy. An IAM policy can then be layered on top to grant a few approved users s3:PutObject permissions while restricting all others to read-only access, fulfilling all requirements with the least implementation effort. Why Incorrect Options are Wrong: A. MFA delete protects against accidental deletion but does not enforce a WORM model or a minimum retention period, nor does it prevent overwrites. C. An IAM role can restrict deletion but is a less robust WORM implementation than Object Lock and does not inherently enforce a time-based re

</details>

### 86. ce-268

A company needs to use its on-premises LDAP directory service to authenticate its users to the AWS Management Console. The directory service is not compatible with Security Assertion Markup Language (SAML). Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Develop an on-premises custom identity broker application or process that uses AWS STS to get short-lived credentials.**

Since the on-premises LDAP directory is not compatible with SAML, standard federation methods like using AWS IAM Identity Center with a SAML 2.0 identity provider are not possible. The correct pattern for this scenario is to create a custom identity broker. This on-premises application authenticates users against the LDAP directory. Upon successful authentication, the broker application calls the AWS Security Token Service (STS) AssumeRole API action to trade the application's credentials for temporary, short-lived AWS credentials scoped for the authenticated user. The user can then use these temporary credentials to access the AWS Management Console. Why Incorrect Options are Wrong: A. AWS IAM Identity Center typically requires a SAML 2.0-compatible identity provider or Active Directory for federation, which is not available in this scenario. B. This is not a valid or secure integration

</details>

### 87. ce-274

A company uses an organization in AWS Organizations to manage multiple AWS accounts. The company is migrating users from IAM to AWS IAM Identity Center. The company wants to ensure that no new IAM users can be created in any of the member accounts. The company wants to allow only existing IAM users to have access to the accounts. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a service control policy SCP that denies the iam:CreateUser action. Apply the SCP to all the member accounts in the organization.**

Service Control Policies (SCPs) are a feature of AWS Organizations used to manage permissions and enforce governance guardrails across multiple accounts. By creating an SCP with a "Deny" effect for the iam:CreateUser action and applying it to the organizational unit (OU) or root containing the member accounts, the company can centrally prevent the creation of any new IAM users in those accounts. This policy does not affect existing IAM users or their permissions, thus meeting all stated requirements effectively and scalably. Why Incorrect Options are Wrong: B. Attaching a policy to all users is difficult to manage and would not prevent a root user in a member account from creating new users. C. This only prevents the creation of access keys, not the creation of users. It also requires manual configuration in each account. D. A permissions boundary only sets the maximum permissions for an

</details>

### 88. dt-277

A company is preparing to give AWS Management Console access to developers. Company policy mandates identity federation and role-based access control. Roles are currently assigned using groups in the corporate Active Directory. What combination of the following will give developers access to the AWS console? (Choose 2 answers)

<details><summary>Answer</summary>

**A. AWS Directory Service AD Connector.; D. AWS identity and Access Management roles.**

</details>

### 89. ce-279

A solutions architect is using Amazon EC2 instances to host an application. The solutions architect needs to grant permissions for the application to access an Amazon DynamoDB table. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Create an IAM role to access the DynamoDB table. Assign the IAM role to the EC2 instance profile.**

The standard and most secure method for an application on an Amazon EC2 instance to access other AWS services is by using an IAM role. An IAM role is created with the necessary permissions (in this case, to access the DynamoDB table). This role is then attached to the EC2 instance via an instance profile. The application running on the instance can then retrieve temporary security credentials from the instance metadata service, eliminating the need to hardcode or manage long-term credentials within the application or on the instance itself. Why Incorrect Options are Wrong: A. Instance profiles are associated with IAM roles, not directly with access keys. Storing keys on the instance is not a best practice. B. EC2 key pairs are used for authenticating SSH access to the instance, not for granting permissions to AWS services. C. Instance profiles are associated with IAM roles, not IAM users

</details>

### 90. ce-280

A company has an AWS Lambda function and an Amazon S3 bucket. A solutions architect creates an IAM role that has S3:GetObject and S3:ListBucket permissions and configures it as the Lambda function execution role. The function must write logs to an Amazon CloudWatch Logs log group when the function is invoked. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Update the IAM policy that is attached to the existing IAM role to include the logs:CreateLogGroup, logs:CreateLogStream, and logs:PutLogEvents permissions.**

The AWS Lambda function's permissions are defined by its execution role. To allow the function to write logs, its execution role must have the necessary permissions to interact with Amazon CloudWatch Logs. The standard permissions required are logs:CreateLogGroup, logs:CreateLogStream, and logs:PutLogEvents. The correct solution is to add these permissions to the policy attached to the existing Lambda execution role. This grants the function the ability to create and write to log streams without granting excessive permissions. Why Incorrect Options are Wrong: A. IAM roles are attached to principals (like a Lambda function), not resources (like an S3 bucket). The function needs the permissions. C. An S3 bucket policy controls access to the S3 bucket; it cannot grant permissions for a Lambda function to write to CloudWatch Logs. D. The logs:GetLogEvents permission allows for reading logs,

</details>

### 91. ce-282

A company uses an organization in AWS Organizations to manage multiple AWS accounts. Multiple teams access each AWS account by assuming IAM roles. Each team has a unique IAM role. Each IAM role has a unique set of permissions. A security team wants to automate some security tasks by deploying AWS Lambda functions within each AWS account. The security team wants to ensure that only members of the security team can modify the Lambda functions directly. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a service control policy SCP that prevents any entity from making changes to Lambda functions except for the IAM role of the security team that is specified in the Condition clause. Attach the SCP to the root of the organization.**

Service Control Policies (SCPs) are the correct mechanism to enforce organization-wide permissions guardrails. To create an exception for a specific IAM role, a Condition element must be used in the SCP's Deny statement. The condition would check if the ARN of the principal making the request does not match the security team's role ARN (e.g., using the aws:PrincipalArn condition key with the StringNotEquals operator). This policy, attached to the organization's root, prevents all other principals in all member accounts from modifying the specified Lambda functions while allowing the designated security team role to perform its duties. Why Incorrect Options are Wrong: A. The Principal element is not supported in SCPs. Exceptions in SCPs must be configured using the Condition element. B. An IAM policy attached to the root user is ineffective, as the root user should not be used for routine

</details>

### 92. ce-283

A company hosts customer data in an Amazon S3 bucket. The company wants to ensure that only specific applications that run on Amazon EC2 instances in a private subnet have access to the S3 bucket. The applications must not require long-term AWS access keys. The company needs to log all access to S3 objects for auditing purposes. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an IAM role that has access to the S3 bucket. Attach the IAM role to the EC2 instances. Update the bucket policy to allow access only for the role. Use AWS CloudTrail to log data events for the bucket.**

This solution meets all requirements securely and efficiently. Using an IAM role attached to the EC2 instances leverages temporary credentials, eliminating the need for long-term access keys, which is a security best practice. The S3 bucket policy can be configured to grant access exclusively to this IAM role, ensuring only the authorized applications can access the data. AWS CloudTrail data events provide detailed, object-level API activity logging (e.g., GetObject, PutObject) for the S3 bucket, which is essential for auditing purposes. This combination provides a secure, auditable, and manageable access control mechanism. Why Incorrect Options are Wrong: A. Storing access keys, even in Parameter Store, violates the requirement to avoid long-term credentials. IAM roles are the correct mechanism. C. This uses a long-term IAM user access key. CloudTrail management events do not log object

</details>

### 93. ce-286 `security`

A company performs a security review of its AWS workloads and finds that all the company's IAM users have the AdministratorAccess IAM managed policy directly attached. The company's IAM users belong to either an engineering department or an operations department. Engineering users require full read and write access to all resources. Operations users require only read access to all resources. The company must apply the principle of least privilege to user access. Which solution will meet this requirement in the MOST operationally efficient way?

<details><summary>Answer</summary>

**A. Create an IAM group for each department. Add either the AdministratorAccess or ReadOnlyAccess IAM managed policy to each group as appropriate. Add each department user to the appropriate IAM group. Remove existing IAM permissions from the users.**

This solution is the most operationally efficient and aligns with AWS IAM best practices. Creating IAM groups for each department (Engineering, Operations) allows for centralized management of permissions. By attaching the appropriate managed policy (AdministratorAccess or ReadOnlyAccess) to each group, permissions are consistently applied to all users within that department. Adding or removing users from a group is a single, simple action, which is far more efficient than managing policies for each user individually, especially as the organization grows. This approach correctly implements the principle of least privilege. Why Incorrect Options are Wrong: B. Applying both policies to a single group would grant all users administrator access, violating the principle of least privilege for the operations team. C. Attaching policies directly to users is less efficient to manage than using g

</details>

### 94. ce-287

A company wants to share data between applications that run in separate AWS accounts. The company wants to use Amazon API Gateway REST APIs to expose private APIs. The company wants to ensure that only authorized accounts can invoke the private APIs. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Use an API Gateway resource policy to grant access to specific accounts.**

The standard and most direct method to control cross-account access to a private Amazon API Gateway REST API is by using a resource policy. A resource policy is a JSON policy document that you attach to a resource, in this case, the API itself. Within this policy, you can specify which AWS principals (such as other AWS accounts, users, or roles) are allowed or denied actions on your API. This allows the company to explicitly grant invocation permissions to specific, authorized AWS accounts while denying all others, meeting the security requirement. Why Incorrect Options are Wrong: A. An interface endpoint policy controls access to the VPC endpoint from within the VPC, not which external accounts can invoke the API through it. C. While the calling account will use IAM permissions, the API Gateway itself must have a resource policy to grant access to that external principal. D. Lambda auth

</details>

### 95. ce-288

A company uses an organization in AWS Organizations to manage five AWS accounts. The company requires a centralized solution to prevent anyone from creating IAM users or access keys in any account. Which solution will meet this requirement with the LEAST administrative overhead?

<details><summary>Answer</summary>

**A. Attach a service control policy SCP to the organization root that denies the creation of IAM users and access keys.**

The goal is to centrally prevent the creation of IAM users and access keys across all accounts in an AWS Organization with minimal effort. Service Control Policies (SCPs) are the ideal tool for this. By attaching an SCP with an explicit Deny statement for iam:CreateUser and iam:CreateAccessKey actions to the organization's root, these permissions are denied for all IAM principals in all member accounts. This is a proactive, preventative control that is managed from a single location (the management account) and applies universally, thus meeting the requirements with the least administrative overhead. Why Incorrect Options are Wrong: B. Applying IAM policies to every user individually is the opposite of a centralized solution and creates maximum administrative overhead. C. Amazon GuardDuty is a threat detection service; it can detect these actions after they occur but cannot prevent them.

</details>

### 96. et-289 `security`

A company has an AWS Lambda function that needs read access to an Amazon S3 bucket that is located in the same AWS account. Which solution will meet these requirements in the MOST secure manner?

<details><summary>Answer</summary>

**B. Apply an IAM role to the Lambda function. Apply an IAM policy to the role to grant read access to the S3 bucket.**

An IAM role provides temporary credentials to the Lambda function to access AWS resources. The function does not have persistent credentials. The IAM policy grants least privilege access by specifying read access only to the specific S3 bucket needed. Access is not granted to all S3 buckets. If the Lambda function is compromised, the attacker would only gain access to the one specified S3 bucket. They would not receive broad access to resources.

</details>

### 97. ce-296 `security`

A company uses an organization in AWS Organizations to manage multiple AWS accounts. The company is building a product that spans multiple accounts. Developers at the company who work in multiple accounts need to give AWS Lambda functions access to write logs to an Amazon S3 bucket that is in a central logging account. Which solution will meet this requirement in the MOST secure way?

<details><summary>Answer</summary>

**A. Create an IAM role in the central logging account that has write access to the S3 bucket. Create a trust policy that allows AWS Lambda functions in accounts within the organization to assume the IAM role.**

The most secure and standard method for granting cross-account access is to use an IAM role. An IAM role is created in the central logging account with a permissions policy granting write access to the S3 bucket. A trust policy is attached to the role, specifying which principals (in this case, Lambda execution roles from other accounts within the organization) are allowed to assume it. This approach uses temporary security credentials, avoiding the use of long-lived access keys, and adheres to the principle of least privilege. The trust policy can use the aws:PrincipalOrgID condition key to restrict access only to principals from within the AWS Organization. Why Incorrect Options are Wrong: B. Using an IAM user with long-lived access keys is a significant security risk and goes against AWS best practices for programmatic access. C. A bucket policy allowing full access for "AWS Lambda" i

</details>

### 98. ce-298

A company is building an application on an Amazon ECS cluster that uses the AWS Fargate launch type. The application must read files from a private Amazon S3 bucket. The company needs to design a security solution to allow ECS tasks to retrieve data from the S3 bucket. Which solution will meet these requirements with the LEAST administrative effort?

<details><summary>Answer</summary>

**A. Assign an inline IAM policy to the task role that is configured in the ECS task definition. Configure the policy to grant access to the S3 bucket.**

The most secure and efficient method to grant AWS permissions to applications running in Amazon ECS is by using an IAM role for tasks. By creating an IAM task role with a policy that grants read access to the specific S3 bucket and associating it with the ECS task definition, the ECS agent automatically provides temporary, short-lived credentials to the containers. This eliminates the need to manage long-lived credentials like IAM user access keys, thus minimizing administrative effort and adhering to security best practices. Why Incorrect Options are Wrong: B. Using an IAM user and Parameter Store requires manual management of long-lived credentials, which is less secure and more administrative effort. C. The task execution role grants permissions to the ECS agent for actions like pulling images, not to the application container itself. D. Using an IAM user and Secrets Manager still inv

</details>

### 99. ce-299

A company runs a web application on Amazon EC2 instances behind an Application Load Balancer ALB. The application experiences periodic spikes in malicious traffic attempts from attackers. The application receives mostly SQL injection and cross-site scripting XSS attacks from external sources. The company requires a solution to protect the application from the attacks. The solution must have minimal effect on application performance. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy AWS WAF on the ALB. Configure rules to block malicious traffic activity. Enable AWS Shield Advanced.**

The requirement is to protect a web application from common layer 7 attacks like SQL injection and cross-site scripting (XSS) with minimal performance impact. AWS WAF (Web Application Firewall) is a service designed specifically for this purpose. By deploying AWS WAF on the Application Load Balancer (ALB), all incoming traffic is inspected at the edge before it reaches the EC2 instances. You can configure managed or custom rules to identify and block malicious requests, such as those containing SQL injection or XSS patterns. This approach is highly effective and has a negligible impact on application performance. Why Incorrect Options are Wrong: B. AWS CloudTrail is an audit tool for API calls, not a real-time traffic inspection or blocking service. This method would be slow and ineffective. C. Host-based intrusion detection systems (IDS) consume instance resources, potentially impacting

</details>

### 100. ce-300 `security`

The company must encrypt finance reports that are stored in an Amazon S3 bucket. An AWS Lambda function must be able to decrypt the reports dynamically. An IAM group that the company's security administrators use must manage the encryption keys. The IAM group must manage key rotation, deletion, and creation. The company must grant access to the keys according to the principle of least privilege. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use customer managed AWS KMS keys to encrypt the reports in the S3 bucket. Use IAM policies to grant the Lambda function execution role permissions to decrypt the files. Use IAM policies to grant the security administrator IAM group permissions to perform only kms:CreateKey, kms:DeleteKey, and kms:RotateKey actions on KMS keys.**

The requirements necessitate granular control over key management and adherence to the principle of least privilege. Using customer-managed AWS KMS keys (CMKs) allows the security administrators' IAM group to manage the key lifecycle (creation, rotation, deletion). An IAM policy attached to this group can grant only the specific permissions required (kms:CreateKey, kms:DeleteKey, etc.). A separate IAM policy for the Lambda function's execution role can grant it only the kms:Decrypt permission needed to read the reports. This configuration meets all requirements, including least privilege, by separating duties and providing minimal necessary permissions. Why Incorrect Options are Wrong: A. With SSE-S3, AWS manages the encryption keys, so the company's security administrators cannot manage their lifecycle as required. C. This option is less specific than B. It only mentions granting permis

</details>

### 101. dt-300

Without [...] you must either create multiple AWS accounts-each with its own billing and subscriptions to AWS products-or your employees must share the security credentials of a single AWS account.

<details><summary>Answer</summary>

**D. Amazon IAM.**

</details>

### 102. ce-306 `least-ops`

A company uses an Amazon Aurora PostgreSQL DB cluster to store structured sensitive data about its customers. To meet compliance requirements, the company introduced a policy that all the customer-related data must be encrypted at rest. Which solution will ensure that the company is compliant with the policy with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create a snapshot of the existing Aurora PostgreSQL DB cluster. Enable encryption by using an AWS KMS key. Restore the snapshot to a new Aurora PostgreSQL DB cluster.**

You cannot enable encryption on an existing, unencrypted Amazon Aurora DB cluster. The standard and most operationally efficient method to encrypt the data is to first take a snapshot of the unencrypted cluster. Then, you create an encrypted copy of that snapshot, specifying an AWS KMS key. Finally, you restore a new, encrypted Aurora DB cluster from the encrypted snapshot. This process is managed by AWS and is less error-prone and operationally intensive than a manual data migration. Why Incorrect Options are Wrong: A. Modifying an existing unencrypted Aurora DB cluster to enable encryption is not a supported operation in AWS. B. Manually migrating data involves complex export/import processes (e.g., using pgdump and pgrestore), which incurs significant operational overhead and potential for error. C. Server-side encryption (SSE) is a general term; for Aurora, encryption is specifically

</details>

### 103. dt-306

A company needs to deploy services to an AWS region which they have not previously used. The company currently has an AWS identity and Access Management (IAM) role for the Amazon EC2 instances, which permits the instance to have access to Amazon DynamoDB. The company wants their EC2 instances in the new region to have the same privileges. How should the company achieve this?

<details><summary>Answer</summary>

**B. Assign the existing IAM role to the Amazon EC2 instances in the new region.**

</details>

### 104. ce-309

A company's cloud operations team uses the AWS Management Console to administer AWS resources from remote locations, including employees' home offices. The cloud operations team logs in by using individual IAM user accounts. The IAM users belong to an IAM user group that has the PowerUserAccess AWS managed policy attached. A solutions architect needs to recommend a solution to improve security for the cloud operations team's AWS account. The solution must not increase operational overhead for the cloud operations team. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Enable AWS IAM Identity Center. Configure IAM Identity Center to always require users to use multi-factor authentication (MFA) to log in.**

Enforcing multi-factor authentication (MFA) is a fundamental security best practice that adds a critical layer of protection for user sign-ins. AWS IAM Identity Center (formerly AWS Single Sign-On) centralizes access management across multiple AWS accounts and applications. By configuring IAM Identity Center to require MFA, the company can significantly enhance security for all users. This approach meets the requirement of not increasing operational overhead because it simplifies user access management and the end-user experience of using MFA is minimal after a one-time setup. Why Incorrect Options are Wrong: B. Forcing a complete shift from the AWS Management Console to the CLI and CloudFormation represents a drastic change in workflow, which would substantially increase operational overhead for training and daily tasks. C. While using least-privilege policies is a best practice, creati

</details>

### 105. ce-311

A large company requires a data backup strategy. The solution must replicate long-term backups from a source AWS account to a dedicated backup AWS account. All backups must be encrypted. The encryption keys must be available for encryption and decryption operations in both the source account and the backup account. Only specific AWS accounts, resources, and users must have access permissions for the encryption keys. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use customer-managed AWS KMS keys that have appropriate policies attached in both the source account and the backup account. Configure AWS Backup to automate the backup and replication process.**

This solution correctly addresses all requirements using the most appropriate AWS services. Customer-managed AWS Key Management Service (KMS) keys are essential because their key policies can be explicitly configured to grant permissions to other AWS accounts, specific IAM roles, and users. This fulfills the requirement for controlled, cross-account key access. AWS Backup is the native, managed service designed to automate backup schedules and replicate backup copies to different accounts and regions. It integrates seamlessly with customer-managed KMS keys to ensure that backups are encrypted at rest and that the destination account has the necessary decryption permissions, providing a secure and automated solution. Why Incorrect Options are Wrong: A. A third-party solution and a custom Lambda function add unnecessary operational overhead and complexity when a fully managed, integrated A

</details>

### 106. dt-319

A user has created an application which will be hosted on EC2. The application makes calls to DynamoDB to fetch certain data. The application is using the DynamoDB SDK to connect with from theEC2 instance. Which of the below mentioned statements is true with respect to the best practice for security in this scenario?

<details><summary>Answer</summary>

**B. The user should attach an IAM role with DynamoDB access to the EC2 instance.**

</details>

### 107. et-325

A company is hosting a web application from an Amazon S3 bucket. The application uses Amazon Cognito as an identity provider to authenticate users and return a JSON Web Token (JWT) that provides access to protected resources that are stored in another S3 bucket. Upon deployment of the application, users report errors and are unable to access the protected content. A solutions architect must resolve this issue by providing proper permissions so that users can access the protected content. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Update the Amazon Cognito identity pool to assume the proper IAM role for access to the protected content.**

Amazon Cognito Identity Pool: When users authenticate through Amazon Cognito, they assume roles that determine their access to AWS resources. By updating the Cognito identity pool, you can configure it to assume the proper IAM role that has the necessary permissions to access the protected content stored in the S3 bucket.  IAM Role Permissions: The IAM role associated with the identity pool should have the required permissions (e.g., S3 getObject permissions) to access the protected content in the S3 bucket.

</details>

### 108. et-330

A company is planning to store data on Amazon RDS DB instances. The company must encrypt the data at rest. What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Create a key in AWS Key Management Service (AWS KMS). Enable encryption for the DB instances.**

By creating a key in AWS KMS and enabling encryption for the RDS DB instances, you ensure that the data at rest is encrypted using the specified key.  AWS RDS supports encryption at rest, and you can use AWS KMS to manage the encryption keys. When you enable encryption for an RDS DB instance, you can specify a KMS key to use for encryption.

</details>

### 109. et-336

A company hosts a multi-tier web application that uses an Amazon Aurora MySQL DB cluster for storage. The application tier is hosted on Amazon EC2 instances. The company’s IT security guidelines mandate that the database credentials be encrypted and rotated every 14 days. What should a solutions architect do to meet this requirement with the LEAST operational effort?

<details><summary>Answer</summary>

**A. Create a new AWS Key Management Service (AWS KMS) encryption key. Use AWS Secrets Manager to create a new secret that uses the KMS key with the appropriate credentials. Associate the secret with the Aurora DB cluster. Configure a custom rotation period of 14 days.**

A proposes to create a new AWS KMS encryption key and use AWS Secrets Manager to create a new secret that uses the KMS key with the appropriate credentials. Then, the secret will be associated with the Aurora DB cluster, and a custom rotation period of 14 days will be configured. AWS Secrets Manager will automate the process of rotating the database credentials, which will reduce the operational effort required to meet the IT security guidelines.

</details>

### 110. dt-337

Through which of the following interfaces is AWS Identity and Access Management available? A. AWS Management Console. B. Command line interface (CLI). C. IAM Query API. D. Existing libraries.

<details><summary>Answer</summary>

**D. All of the above.**

</details>

### 111. et-345 `cost`

A company wants to restrict access to the content of one of its main web applications and to protect the content by using authorization techniques available on AWS. The company wants to implement a serverless architecture and an authentication solution for fewer than 100 users. The solution needs to integrate with the main web application and serve web content globally. The solution must also scale as the company's user base grows while providing the lowest login latency possible. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Use Amazon Cognito for authentication. Use Lambda@Edge for authorization. Use Amazon CloudFront to serve the web application globally.**

Amazon Cognito for Authentication: Amazon Cognito is a fully managed service for user identity and access control. It provides easy integration for authentication with a serverless architecture and supports a user pool for fewer than 100 users.  Lambda@Edge for Authorization: Lambda@Edge allows you to run custom code in response to CloudFront events, including authorization. You can implement authorization logic at the edge locations closest to the end-users, providing low-latency access.  Amazon CloudFront for Content Delivery: Amazon CloudFront is a global content delivery network (CDN) that integrates seamlessly with Lambda@Edge. CloudFront can serve the web application globally, distributing content from edge locations for low-latency access.

</details>

### 112. et-359

A hospital needs to store patient records in an Amazon S3 bucket. The hospital’s compliance team must ensure that all protected health information (PHI) is encrypted in transit and at rest. The compliance team must administer the encryption key for data at rest. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use the aws:SecureTransport condition on S3 bucket policies to allow only encrypted connections over HTTPS (TLS). Configure default encryption for each S3 bucket to use server-side encryption with AWS KMS keys (SSE-KMS). Assign the compliance team to manage the KMS keys.**

it allows the compliance team to manage the KMS keys used for server-side encryption, thereby providing the necessary control over the encryption keys. Additionally, the use of the "aws:SecureTransport" condition on the bucket policy ensures that all connections to the S3 bucket are encrypted in transit.

</details>

### 113. dt-363

Every user you create in the IAM system starts with [...].

<details><summary>Answer</summary>

**C. no permissions.**

</details>

### 114. et-364

A hospital is designing a new application that gathers symptoms from patients. The hospital has decided to use Amazon Simple Queue Service (Amazon SQS) and Amazon Simple Notification Service (Amazon SNS) in the architecture. A solutions architect is reviewing the infrastructure design. Data must be encrypted at rest and in transit. Only authorized personnel of the hospital should be able to access the data. Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Turn on server-side encryption on the SNS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply a key policy to restrict key usage to a set of authorized principals.**

D. Turn on server-side encryption on the SQS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply a key policy to restrict key usage to a set of authorized principals. Set a condition in the queue policy to allow only encrypted connections over TLS.  This option ensures that data at rest in the SNS components is encrypted using an AWS KMS customer managed key. The key policy restricts key usage to authorized personnel.  This option ensures that data at rest in the SQS components is encrypted using an AWS KMS customer managed key. The key policy restricts key usage to authorized personnel, and the queue policy ensures that only encrypted connections over TLS are allowed.

</details>

### 115. et-368

A solutions architect wants all new users to have specific complexity requirements and mandatory rotation periods for IAM user passwords. What should the solutions architect do to accomplish this?

<details><summary>Answer</summary>

**A. Set an overall password policy for the entire AWS account.**

Amazon Web Services (AWS) allows you to set an account-wide password policy using AWS Identity and Access Management (IAM). This policy defines the rules and requirements for all IAM users in the AWS account. It's a centralized approach to enforce security measures consistently across all users. In this case, the solutions architect can set the specific complexity requirements and mandatory rotation periods by configuring the password policy at the AWS account level.

</details>

### 116. dt-378

True or False: Without IAM, you cannot control the tasks a particular user or system can do and what AWS resources they might use.

<details><summary>Answer</summary>

**A. True.**

</details>

### 117. dt-384

In AWS CloudHSM, in addition to the AWS recommendation that you use two or more HSM appliances in a high-availability configuration to prevent the loss of keys and data, you can also perform a remote backup/restore of a Luna SA partition if you have purchased a:

<details><summary>Answer</summary>

**B. Luna Backup HS.**

</details>

### 118. et-387 `security`

A new employee has joined a company as a deployment engineer. The deployment engineer will be using AWS CloudFormation templates to create multiple AWS resources. A solutions architect wants the deployment engineer to perform job activities while following the principle of least privilege. Which combination of actions should the solutions architect take to accomplish this goal? (Choose two.)

<details><summary>Answer</summary>

**D. Create a new IAM user for the deployment engineer and add the IAM user to a group that has an IAM policy that allows AWS CloudFormation actions only.**

E. Create an IAM role for the deployment engineer to explicitly define the permissions specific to the AWS CloudFormation stack and launch stacks using that IAM role.  This ensures that the IAM user has the necessary permissions for AWS CloudFormation but not unnecessary permissions for other AWS services.  IAM roles are more suitable for temporary elevated permissions needed during AWS CloudFormation stack operations. The deployment engineer can assume the role when required, limiting their permissions to only what is needed for those specific actions.

</details>

### 119. dt-391

After a major security breach your manager has requested a report of all users and their credentials in AWS. You discover that in IAM you can generate and download a credential report that lists all users in your account and the status of their various credentials, including passwords, access keys, MFA devices, and signing certificates. Which following statement is incorrect in regards to the use of credential reports?

<details><summary>Answer</summary>

**A. Credential reports are downloaded XML files.**

</details>

### 120. et-399 `least-ops`

A financial company hosts a web application on AWS. The application uses an Amazon API Gateway Regional API endpoint to give users the ability to retrieve current stock prices. The company’s security team has noticed an increase in the number of API requests. The security team is concerned that HTTP flood attacks might take the application offline. A solutions architect must design a solution to protect the application from this type of attack. Which solution meets these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a Regional AWS WAF web ACL with a rate-based rule. Associate the web ACL with the API Gateway stage.**

Rate-based Rule with AWS WAF: AWS WAF provides protection against various web application attacks, including HTTP flood attacks. By using a rate-based rule, you can set thresholds for the number of requests from a client IP within a specified time period. This helps in detecting and mitigating HTTP flood attacks effectively.

</details>

### 121. dt-400

A/An [...] is the concept of allowing (or disallowing) an entity such as a user, group, or role some type of access to one or more resources.

<details><summary>Answer</summary>

**B. AWS Account.**

</details>

### 122. et-403

A developer has an application that uses an AWS Lambda function to upload files to Amazon S3 and needs the required permissions to perform the task. The developer already has an IAM user with valid IAM credentials required for Amazon S3. What should a solutions architect do to grant the permissions?

<details><summary>Answer</summary>

**D. Create an IAM execution role with the required permissions and attach the IAM role to the Lambda function.**

o grant the necessary permissions to an AWS Lambda function to upload files to Amazon S3, a solutions architect should create an IAM execution role with the required permissions and attach the IAM role to the Lambda function. This approach follows the principle of least privilege and ensures that the Lambda function can only access the resources it needs to perform its specific task.

</details>

### 123. dt-407

The AWS CloudHSM service defines a resource known as a high-availability (HA) [...], which is a virtual partition that represents a group of partitions, typically distributed between several physical HSMs for high-availability.

<details><summary>Answer</summary>

**B. partition group.**

</details>

### 124. et-412

An image-hosting company stores its objects in Amazon S3 buckets. The company wants to avoid accidental exposure of the objects in the S3 buckets to the public. All S3 objects in the entire AWS account need to remain private. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use the S3 Block Public Access feature on the account level. Use AWS Organizations to create a service control policy (SCP) that prevents IAM users from changing the setting. Apply the SCP to the account.**

AWS Organizations allows you to create service control policies (SCPs) that set fine-grained permissions for member accounts. In this case, you can create an SCP that prevents IAM users from changing the S3 Block Public Access settings. Applying this SCP to the account ensures that the configured public access settings remain in place and cannot be altered by IAM users.

</details>

### 125. dt-414

Your company has recently extended its datacenter into a VPC on AWS to add burst computing capacity as needed Members of your Network Operations Center need to be able to go to the AWSManagement Console and administer Amazon EC2 instances as necessary You don't want to create new IAM users for each NOC member and make those users sign in again to the AWS Management Console Which option below will meet the needs for your NOC members?

<details><summary>Answer</summary>

**D. Use your on-premises SAML2.0-compliam identity provider (IOP) to retrieve temporary security credentials to enable NOC members to sign in to the AWS Management Console.**

</details>

### 126. et-418 `security`

A solutions architect needs to allow team members to access Amazon S3 buckets in two different AWS accounts: a development account and a production account. The team currently has access to S3 buckets in the development account by using unique IAM users that are assigned to an IAM group that has appropriate permissions in the account. The solutions architect has created an IAM role in the production account. The role has a policy that grants access to an S3 bucket in the production account. Which solution will meet these requirements while complying with the principle of least privilege?

<details><summary>Answer</summary>

**B. Add the development account as a principal in the trust policy of the role in the production account.**

A role has two separate policies: the trust policy, which lists the principals allowed to call sts:AssumeRole on it, and the permissions policy, which lists what the role may do once assumed. Naming the development account as a principal in the trust policy lets the existing development IAM users assume the production role and receive short-lived credentials, with no second set of users or long-term access keys in the production account. Least privilege holds because the role's permissions policy already grants access to just the one production S3 bucket and nothing else, so that is the ceiling on what an assuming user can do. The development users also need sts:AssumeRole for that role ARN allowed on their own side, since both accounts must agree before a cross-account assume succeeds.

</details>

### 127. et-419

A company uses AWS Organizations with all features enabled and runs multiple Amazon EC2 workloads in the ap-southeast-2 Region. The company has a service control policy (SCP) that prevents any resources from being created in any other Region. A security policy requires the company to encrypt all data at rest. An audit discovers that employees have created Amazon Elastic Block Store (Amazon EBS) volumes for EC2 instances without encrypting the volumes. The company wants any new EC2 instances that any IAM user or root user launches in ap-southeast-2 to use encrypted EBS volumes. The company wants a solution that will have minimal effect on employees who create EBS volumes. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**E. In the Organizations management account, specify the Default EBS volume encryption setting.**

C. Create an SCP. Attach the SCP to the root organizational unit (OU). Define the SCP to deny the ec2:CreateVolume action whenthe ec2:Encrypted condition equals false.  Explanation: "Default EBS encryption" is a per-account, per-Region setting — it cannot be configured centrally from the Organizations management account (ruling out the old option E). It has to be set in each member account instead, paired with the SCP (C) as a guardrail that blocks anyone who creates a volume without encryption regardless.

</details>

### 128. et-428 `security`

A serverless application uses Amazon API Gateway, AWS Lambda, and Amazon DynamoDB. The Lambda function needs permissions to read and write to the DynamoDB table. Which solution will give the Lambda function access to the DynamoDB table MOST securely?

<details><summary>Answer</summary>

**B. Create an IAM role that includes Lambda as a trusted service. Attach a policy to the role that allows read and write access to the DynamoDB table. Update the configuration of the Lambda function to use the new role as the execution role.**

IAM Role with Lambda as a Trusted Service: This approach follows the principle of least privilege. You create an IAM role that specifically grants the required permissions to access DynamoDB and makes Lambda a trusted service. This ensures that only Lambda functions associated with this role can assume it.

</details>

### 129. dt-429

True or False: When you use the AWS Management Console to delete an IAM user, IAM also deletes any signing certificates and any access keys belonging to the user.

<details><summary>Answer</summary>

**C. True.**

</details>

### 130. et-433

A company is running its production and nonproduction environment workloads in multiple AWS accounts. The accounts are in an organization in AWS Organizations. The company needs to design a solution that will prevent the modification of cost usage tags. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a service control policy (SCP) to prevent tag modification except by authorized principals.**

SCPs in AWS Organizations are used to set fine-grained permissions on what actions AWS accounts within the organization can perform. You can create a custom SCP to specifically control access to tag modification.

</details>

### 131. et-438 `security`

A company wants to share accounting data with an external auditor. The data is stored in an Amazon RDS DB instance that resides in a private subnet. The auditor has its own AWS account and requires its own copy of the database. What is the MOST secure way for the company to share the database with the auditor?

<details><summary>Answer</summary>

**D. Create an encrypted snapshot of the database. Share the snapshot with the auditor. Allow access to the AWS Key Management Service (AWS KMS) encryption key.**

Creating an encrypted snapshot ensures that the database data is protected during the transfer and storage process. Sharing the encrypted snapshot with the auditor allows them to create their own copy of the database securely. By allowing access to the AWS KMS encryption key, the auditor can decrypt the snapshot and restore it to their own environment.

</details>

### 132. dt-459

A user has defined an AutoScaling termination policy to first delete the instance with the nearest billing hour. AutoScaling has launched 3 instances in the US-East-1A region and 2 instances in the US-East-1B region. One of the instances in the US-East-1B region is running nearest to the billing hour. Which instance will AutoScaling terminate first while executing the termination action?

<details><summary>Answer</summary>

**C. Instance with the nearest billing hour in US-East-1A.**

</details>

### 133. et-459

A company uses AWS Organizations to run workloads within multiple AWS accounts. A tagging policy adds department tags to AWS resources when the company creates tags. An accounting team needs to determine spending on Amazon EC2 consumption. The accounting team must determine which departments are responsible for the costs regardless ofAWS account. The accounting team has access to AWS Cost Explorer for all AWS accounts within the organization and needs to access all reports from Cost Explorer. Which solution meets these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**A. From the Organizations management account billing console, activate a user-defined cost allocation tag named department. Create one cost report in Cost Explorer grouping by tag name, and filter by EC2.**

While AWS provides AWS-defined tags, the use of a user-defined tag provides flexibility in terms of naming and tagging conventions. Activating the tag at the Organizations management account level ensures that the tag is applied to resources across all member accounts.

</details>

### 134. et-460 `security`

A company wants to securely exchange data between its software as a service (SaaS) application Salesforce account and Amazon S3. The company must encrypt the data at rest by using AWS Key Management Service (AWS KMS) customer managed keys (CMKs). The company must also encrypt the data in transit. The company has enabled API access for the Salesforce account.

<details><summary>Answer</summary>

**C. Create Amazon AppFlow flows to transfer the data securely from Salesforce to Amazon S3.**

Amazon AppFlow is a fully managed integration service that allows you to securely transfer data between AWS services and SaaS applications like Salesforce. It supports data encryption both in transit and at rest. With AppFlow, you can configure the integration flow, including source (Salesforce) and destination (Amazon S3), and set up encryption options. It simplifies the data transfer process and can handle the encryption requirements without the need for custom development.

</details>

### 135. ce-463

A company has an organization in AWS Organizations that has all features enabled. The company has multiple Amazon S3 buckets in multiple AWS Regions around the world. The S3 buckets contain sensitive data. The company needs to ensure that no personally identifiable information (PII) is stored in the S3 buckets. The company also needs a scalable solution to identify PII. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. For each Region in the Organizations management account, designate a delegated Amazon Macie administrator account. In the Macie administrator account, add all accounts in the organization. Use the Macie administrator account to enable Macie. Configure automated sensitive data discovery for all accounts in the organization.**

Amazon Macie is the AWS managed service designed for discovering sensitive data, such as personally identifiable information (PII), within Amazon S3 buckets. To manage Macie across a multi-account environment like AWS Organizations, the recommended and most scalable approach is to designate a specific member account as the delegated Macie administrator. This allows for centralized management without using the organization's management account for operational tasks. Because Macie is a regional service, the delegated administrator must be configured in each AWS Region where S3 buckets need to be monitored. The delegated administrator can then enable Macie and configure automated sensitive data discovery for all member accounts, providing a continuous and scalable solution. Why Incorrect Options are Wrong: A. Delegated administration in AWS Organizations is assigned to an AWS account, not a

</details>

### 136. dt-464

Within the IAM service a GROUP is regarded as a:

<details><summary>Answer</summary>

**D. A collection of users.**

</details>

### 137. et-476 `security`

A company is expecting rapid growth in the near future. A solutions architect needs to configure existing users and grant permissions to new users on AWS. The solutions architect has decided to create IAM groups. The solutions architect will add the new users to IAM groups based on department. Which additional action is the MOST secure way to grant permissions to the new users?

<details><summary>Answer</summary>

**C. Create an IAM policy that grants least privilege permission. Attach the policy to the IAM groups**

Creating an IAM policy that grants the least privilege required for the users' tasks is a security best practice. By attaching this policy to IAM groups, you ensure that new users added to these groups inherit the specific permissions defined in the policy.

</details>

### 138. ce-483

A company uses AWS to run its ecommerce platform. The platform is critical to the company's operations and has a high volume of traffic and transactions. The company configures a multi-factor authentication (MFA) device to secure its AWS account root user credentials. The company wants to ensure that it will not lose access to the root user account if the MFA device is lost. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Add multiple MFA devices for the root user account to handle the disaster scenario.**

To prevent losing access to the AWS account root user if a single Multi-Factor Authentication (MFA) device is lost, the best practice is to register multiple MFA devices. AWS Identity and Access Management (IAM) allows registering up to eight MFA devices for the root user. This provides redundancy; if one device is lost, stolen, or unavailable, another registered device can be used to sign in, ensuring continued access to the account without going through a lengthy recovery process. Why Incorrect Options are Wrong: A. A backup administrator IAM account is a best practice but does not help regain access to the root user account itself if it is locked out. C. Creating a new administrator account is not possible if you are locked out of the account, as you cannot sign in to perform this action. D. Attaching an administrator policy to another user is not possible if you cannot sign in to the

</details>

### 139. et-484

A company wants to move from many standalone AWS accounts to a consolidated, multi-account architecture. The company plans to create many new AWS accounts for different business units. The company needs to authenticate access to these AWS accounts by using a centralized corporate directory service. Which combination of actions should a solutions architect recommend to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Create a new organization in AWS Organizations with all features turned on. Create the new AWS accounts in the organization.**

E. Set up AWS IAM Identity Center (AWS Single Sign-On) in the organization. Configure IAM Identity Center, and integrate it with the company's corporate directory service.  Create a new organization in AWS Organizations with all features turned on. Create the new AWS accounts in the organization. This is a foundational step for managing multiple AWS accounts in a consolidated manner. Option E: Set up AWS IAM Identity Center (AWS Single Sign-On) in the organization. Configure IAM Identity Center, and integrate it with the company's corporate directory service. AWS Single Sign-On (SSO) is designed to simplify and centralize authentication across multiple AWS accounts.

</details>

### 140. et-488

A 4-year-old media company is using the AWS Organizations all features feature set to organize its AWS accounts. According to the company's finance team, the billing information on the member accounts must not be accessible to anyone, including the root user of the member accounts. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a service control policy (SCP) to deny access to the billing information. Attach the SCP to the root organizational unit (OU).**

SCPs in AWS Organizations allow you to set fine-grained permissions and controls over what actions can be performed in member accounts. By creating an SCP, you can explicitly deny access to billing information for all users, including the root user, under the specified organizational unit (OU).

</details>

### 141. et-492

A company has multiple AWS accounts for development work. Some staff consistently use oversized Amazon EC2 instances, which causes the company to exceed the yearly budget for the development accounts. The company wants to centrally restrict the creation of AWS resources in these accounts. Which solution will meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**B. Use AWS Organizations to organize the accounts into organizational units (OUs). Define and attach a service control policy (SCP) to control the usage of EC2 instance types.**

An SCP is a guardrail, not a grant: it sets the maximum permissions available to principals in the accounts it applies to, and a user still needs an IAM identity-based policy that allows the action before anything works. Writing one SCP that denies ec2:RunInstances unless the ec2:InstanceType condition matches an approved list, then attaching it to the OUs holding the development accounts, stops oversized launches everywhere in those accounts at once, including by account administrators. That is far less work than maintaining IAM policies account by account or building a detection-and-remediation pipeline. Two limits to remember: an SCP never restricts the organization's management account, so keep workloads out of it, and SCPs have no effect unless all features are enabled in the organization.

</details>

### 142. dt-500

Are you able to integrate a multi-factor token service with the AWS Platform?

<details><summary>Answer</summary>

**C. Yes, using the AWS multi-factor token devices to authenticate users on the AWS platform.**

</details>

### 143. dt-501

What is the default maximum number of MFA devices in use per AWS account (at the root account level)?

<details><summary>Answer</summary>

**A. 1.**

</details>

### 144. et-503 `security`

A company runs an infrastructure monitoring service. The company is building a new feature that will enable the service to monitor data in customer AWS accounts. The new feature will call AWS APIs in customer accounts to describe Amazon EC2 instances and read Amazon CloudWatch metrics. What should the company do to obtain access to customer accounts in the MOST secure way?

<details><summary>Answer</summary>

**A. Ensure that the customers create an IAM role in their account with read-only EC2 and CloudWatch permissions and a trust policy to the company’s account.**

</details>

### 145. dt-511

A user is sending bulk emails using AWS SES. The emails are not reaching some of the targeted audience because they are not authorized by the ISPs. How can the user ensure that the emails are all delivered?

<details><summary>Answer</summary>

**A. Send an email using DKIM with SE.**

</details>

### 146. dt-516

You are setting up some IAM user policies and have also become aware that some services support resource-based permissions, which let you attach policies to the service's resources instead of to IAM users or groups. Which of the below statements is true in regards to resource-level permissions?

<details><summary>Answer</summary>

**D. Some services support resource-level permissions only for some actions.**

</details>

### 147. et-521 `security`

A retail company has several businesses. The IT team for each business manages its own AWS account. Each team account is part of an organization in AWS Organizations. Each team monitors its product inventory levels in an Amazon DynamoDB table in the team's own AWS account. The company is deploying a central inventory reporting application into a shared AWS account. The application must be able to read items from all the teams' DynamoDB tables. Which authentication option will meet these requirements MOST securely?

<details><summary>Answer</summary>

**C. In every business account, create an IAM role named BU_ROLE with a policy that gives the role access to the DynamoDB table and a trust policy to trust a specific role in the inventory application account. In the inventory account, create a role named APP_ROLE that allows access to the STS AssumeRole API operation. Configure the application to use APP_ROLE and assume the crossaccount role BU_ROLE to read the DynamoDB table.**

</details>

### 148. dt-524

Can I encrypt connections between my application and my DB Instance using SSL?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 149. et-524

A company wants to analyze and troubleshoot Access Denied errors and Unauthorized errors that are related to IAM permissions. The company has AWS CloudTrail turned on. Which solution will meet these requirements with the LEAST effort?

<details><summary>Answer</summary>

**C. Search CloudTrail logs with Amazon Athena queries to identify the errors.**

Amazon Athena allows you to query data directly from S3 using standard SQL queries. CloudTrail logs can be stored in Amazon S3, and Athena makes it easy to analyze the logs using SQL queries.

</details>

### 150. dt-528

IAM provides several policy templates you can use to automatically assign permissions to the groups you create. The [...] policy template gives the Admins group permission to access all account resources, except your AWS account information.

<details><summary>Answer</summary>

**D. Administrator Access.**

</details>

### 151. dt-536

Which IAM role do you use to grant AWS Lambda permission to access a DynamoDB Stream?

<details><summary>Answer</summary>

**C. Execution role.**

</details>

### 152. dt-550

Can you create IAM security credentials for existing users?

<details><summary>Answer</summary>

**A. Yes, existing users can have security credentials associated with their account.**

</details>

### 153. et-550

A company is using AWS Key Management Service (AWS KMS) keys to encrypt AWS Lambda environment variables. A solutions architect needs to ensure that the required permissions are in place to decrypt and use the environment variables. Which steps must the solutions architect take to implement the correct permissions? (Choose two.)

<details><summary>Answer</summary>

**B. Add AWS KMS permissions in the Lambda execution role.**

D. Allow the Lambda execution role in the AWS KMS key policy.  The Lambda execution role is the role assumed by the Lambda function when it runs. It needs permissions to use the KMS key to decrypt the environment variables. Grant the kms:Decrypt permission on the specific KMS key used for encryption to the Lambda execution role.  The AWS KMS key policy controls who can use the KMS key. To grant the Lambda execution role permission to decrypt using the KMS key, modify the key policy to include a statement allowing the Lambda execution role to perform kms:Decrypt on the key.

</details>

### 154. et-553 `least-ops`

A solutions architect needs to review a company's Amazon S3 buckets to discover personally identifiable information (PII). The company stores the PII data in the us-east-1 Region and us-west-2 Region. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure Amazon Macie in each Region. Create a job to analyze the data that is in Amazon S3.**

Amazon Macie is a managed data security and data privacy service that uses machine learning to automatically discover, classify, and protect sensitive data, including personally identifiable information (PII). By configuring Amazon Macie in each region where the company stores PII data, you can create jobs to analyze the data in Amazon S3 and identify any PII.

</details>

### 155. dt-554

Which technique can be used to integrate AWS IAM (Identity and Access Management) with an on-premise LDAP (Lightweight Directory Access Protocol) directory service?

<details><summary>Answer</summary>

**B. Use SAML (Security Assertion Markup Language) to enable single sign-on between AWS and LDAP.**

</details>

### 156. et-556

A solutions architect is using an AWS CloudFormation template to deploy a three-tier web application. The web application consists of a web tier and an application tier that stores and retrieves user data in Amazon DynamoDB tables. The web and application tiers are hosted on Amazon EC2 instances, and the database tier is not publicly accessible. The application EC2 instances need to access the DynamoDB tables without exposing API credentials in the template. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create an IAM role that has the required permissions to read and write from the DynamoDB tables. Add the role to the EC2 instance profile, and associate the instance profile with the application instances.**

Option B is the correct choice because it leverages IAM roles and instance profiles for EC2 instances. By creating an IAM role with the necessary permissions to access DynamoDB and associating it with the EC2 instance profile, you can securely grant permissions to the EC2 instances without exposing API credentials in the CloudFormation template.

</details>

### 157. et-560 `least-ops`

A company's solutions architect is designing an AWS multi-account solution that uses AWS Organizations. The solutions architect has organized the company's accounts into organizational units (OUs). The solutions architect needs a solution that will identify any changes to the OU hierarchy. The solution also needs to notify the company's operations team of any changes. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Provision the AWS accounts by using AWS Control Tower. Use account drift notifications to identify the changes to the OU hierarchy.**

AWS Control Tower is a service that simplifies the process of setting up and governing a secure, multi-account AWS environment based on AWS best practices. It provides a pre-defined landing zone with an organizational structure, OUs, and guardrails to enforce security and compliance.  the organizational units (OUs) are established as part of the AWS Control Tower landing zone. If there are any changes to the OU hierarchy (such as moving accounts between OUs), these changes are considered drift, and AWS Control Tower can generate account drift notifications.

</details>

### 158. et-571

A company is creating a REST API. The company has strict requirements for the use of TLS. The company requires TLSv1.3 on the API endpoints. The company also requires a specific public third-party certificate authority (CA) to sign the TLS certificate. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use a local machine to create a certificate that is signed by the third-party CImport the certificate into AWS Certificate Manager (ACM). Create an HTTP API in Amazon API Gateway with a custom domain. Configure the custom domain to use the certificate.**

</details>

### 159. dt-574

A company needs to deploy virtual desktops to its customers in a virtual private cloud, leveraging existing security controls. Which set of AWS services and features will meet the company's requirements?

<details><summary>Answer</summary>

**C. AWS Directory Service, Amazon Workspaces, and AWS Identity and Access Management.**

</details>

### 160. et-586

A company has five organizational units (OUs) as part of its organization in AWS Organizations. Each OU correlates to the five businesses that the company owns. The company's research and development (R&D) business is separating from the company and will need its own organization. A solutions architect creates a separate new management account for this purpose. What should the solutions architect do next in the new management account?

<details><summary>Answer</summary>

**B. Invite the R&D AWS account to be part of the new organization after the R&D AWS account has left the prior organization.**

</details>

### 161. dt-599 `security`

How should the application use AWS credentials to access the S3 bucket securely?

<details><summary>Answer</summary>

**C. Create an IAM role for EC2 that allows list access to objects in the S3 bucket. Launch the instance with the role, and retrieve the role's credentials from the EC2 Instance metadata.**

</details>

### 162. dt-609

An organization has three separate AWS accounts, one each for development, testing, and production. The organization wants the testing team to have access to certain AWS resources in the production account. How can the organization achieve this?

<details><summary>Answer</summary>

**B. Create the IAM roles with cross account access.**

</details>

### 163. dt-611

You launch an Amazon EC2 instance without an assigned AWS identity and Access Management (IAM) role. Later, you decide that the instance should be running with an IAM role. Which action must you take in order to have a running Amazon EC2 instance with an IAM role assigned to it?

<details><summary>Answer</summary>

**D. Create an image of the instance, and use this image to launch a new instance with the desired IAM role assigned.**

</details>

### 164. et-613 `least-ops`

A company uses Amazon Elastic Kubernetes Service (Amazon EKS) to run a container application. The EKS cluster stores sensitive information in the Kubernetes secrets object. The company wants to ensure that the information is encrypted. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Enable secrets encryption in the EKS cluster by using AWS Key Management Service (AWS KMS).**

Amazon EKS provides built-in support for encrypting Kubernetes secrets using AWS Key Management Service (AWS KMS). You can enable this feature at the EKS cluster level.

</details>

### 165. et-619

A solutions architect is designing a security solution for a company that wants to provide developers with individual AWS accounts through AWS Organizations, while also maintaining standard security controls. Because the individual developers will have AWS account root user-level access to their own accounts, the solutions architect wants to ensure that the mandatory AWS CloudTrail configuration that is applied to new developer accounts is not modified. Which action meets these requirements?

<details><summary>Answer</summary>

**C. Create a service control policy (SCP) that prohibits changes to CloudTrail, and attach it the developer accounts.**

SCPs are used in AWS Organizations to set fine-grained permissions and restrictions on AWS accounts within the organization. By creating an SCP that explicitly prohibits changes to CloudTrail settings, you can enforce this restriction across all developer accounts.

</details>

### 166. et-628 `least-ops`

A global company runs its applications in multiple AWS accounts in AWS Organizations. The company's applications use multipart uploads to upload data to multiple Amazon S3 buckets across AWS Regions. The company wants to report on incomplete multipart uploads for cost compliance purposes. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Configure S3 Storage Lens to report the incomplete multipart upload object count.**

S3 Storage Lens is a feature in Amazon S3 that provides a comprehensive view of your storage usage and activity across multiple accounts. It helps you understand, analyze, and optimize your storage usage. You can use S3 Storage Lens to generate reports on various metrics, including the incomplete multipart upload object count.

</details>

### 167. dt-630

Can I attach more than one policy to a particular entity?

<details><summary>Answer</summary>

**A. Yes always.**

</details>

### 168. et-640

A company has an application workflow that uses an AWS Lambda function to download and decrypt files from Amazon S3. These files are encrypted using AWS Key Management Service (AWS KMS) keys. A solutions architect needs to design a solution that will ensure the required permissions are set correctly. Which combination of actions accomplish this? (Choose two.)

<details><summary>Answer</summary>

**B. Grant the decrypt permission for the Lambda IAM role in the KMS key's policy**

E. Create a new IAM role with the kms:decrypt permission and attach the execution role to the Lambda function.

</details>

### 169. et-644

An international company has a subdomain for each country that the company operates in. The subdomains are formatted as example.com, country1.example.com, and country2.example.com. The company's workloads are behind an Application Load Balancer. The company wants to encrypt the website data that is in transit. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use the AWS Certificate Manager (ACM) console to request a public certificate for the apex top domain example.com and a wildcard certificate for *.example.com. AND E. Validate domain ownership for the domain by adding the required DNS records to the DNS provider.**

*.example.com matches one label to the left of example.com, so it covers country1.example.com and country2.example.com but not the bare apex example.com, which is why both names are needed. ACM issues public certificates free of charge and they attach directly to the Application Load Balancer's HTTPS listener, which terminates TLS and gives encryption in transit. Before ACM issues anything it has to confirm you control the domain, and you do that by adding the CNAME records ACM supplies to the DNS zone. DNS validation is the right choice here, not because wildcards require it, but because ACM re-checks those records and renews the certificate on its own, whereas email validation needs a human to click a link every renewal.

</details>

### 170. et-645 `least-ops`

A company is required to use cryptographic keys in its on-premises key manager. The key manager is outside of the AWS Cloud because of regulatory and compliance requirements. The company wants to manage encryption and decryption by using cryptographic keys that are retained outside of the AWS Cloud and that support a variety of external key managers from different vendors. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use an AWS Key Management Service (AWS KMS) external key store backed by an external key manager.**

</details>

### 171. dt-649

A company is planning to run a group of Amazon EC2 instances that connect to an Amazon Aurora database. The company has built an AWS CloudFormation template to deploy the EC2 instances and the Aurora DB cluster. The company wants to allow the instances to authenticate to the database in a secure way. The company does not want to maintain static database credentials. Which solution meets these requirements with the LEAST operational effort?

<details><summary>Answer</summary>

**C. Configure the DB cluster to use IAM database authentication. Create a database user to use with IAM authentication. Associate a role with the EC2 instances to allow applications on the instances to access the database.**

</details>

### 172. dt-650

A company wants to configure its Amazon CloudFront distribution to use SSL/TLS certificates. The company does not want to use the default domain name for the distribution. Instead, the company wants to use a different domain name for the distribution. Which solution will deploy the certificate without incurring any additional costs?

<details><summary>Answer</summary>

**C. Request an Amazon issued public certificate from AWS Certificate Manager (ACM) in the us-east-1 Region.**

</details>

### 173. dt-666

A company has two AWS accounts: Production and Development. There are code changes ready in the Development account to push to the Production account. In the alpha phase, only two senior developers on the development team need access to the Production account. In the beta phase, more developers might need access to perform testing as well. What should a solutions architect recommend?

<details><summary>Answer</summary>

**C. Create an IAM role in the Production account with the trust policy that specifies the Development account. Allow developers to assume the role.**

</details>

### 174. dt-668 `least-ops`

A development team uses multiple AWS accounts for its development, Staging, and production environments Team members have been launching large Amazon EC2 instances that are underutilized. A solutions architect must prevent large instances from being launched in all accounts. How can the solutions architect meet this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an orgainization in AWS Organizations in the managment account with the default policy. Create a Service control prolicy that denies the launch of large  EC2 instances and apply to all aws accounts.**

</details>

### 175. et-668

A company created a new organization in AWS Organizations. The organization has multiple accounts for the company's development teams. The development team members use AWS IAM Identity Center (AWS Single Sign-On) to access the accounts. For each of the company's applications, the development teams must use a predefined application name to tag resources that are created. A solutions architect needs to design a solution that gives the development team the ability to create resources only if the application name tag has an approved value. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a tag policy in AWS Organizations that defines the list of allowed application names.**

A tag policy is defined once in the Organizations management account and attached to the root, an OU or an account; it declares the approved values for a tag key, and with enforcement turned on for the supported resource types it blocks tagging operations that would set a value outside that list. That gives one central list to maintain as teams and accounts come and go, which is why it beats the alternatives here. The rejection of the IAM option needs care: an IAM policy or an SCP can check tag values, for example denying a create action unless aws:RequestTag/application equals an approved name, so it is not that IAM cannot do this. It is that you would have to write and keep in sync a condition for every service and action the teams use, which is far more work than one tag policy.

</details>

### 176. ce-670

A global media streaming company is migrating its user authentication and content delivery services to AWS. The company wants to use Amazon API Gateway for user authentication and authorization. The company needs a solution that restricts API access to AWS Regions in the United States and ensures minimal latency. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an API Gateway REST API. Configure an AWS WAF firewall in the same Region. Implement AWS WAF rules to deny requests that originate from Regions outside the United States. Associate the AWS WAF firewall with the API Gateway REST API.**

The solution requires an API that supports robust user authentication and authorization, geographic access restriction, and minimal latency for users in the United States. Amazon API Gateway REST APIs are better suited for this scenario than HTTP APIs because they offer more comprehensive, built-in features for authentication and authorization, such as IAM permissions, Cognito user pools, and Lambda authorizers. To restrict access based on geography, AWS WAF is the appropriate service. A WAF geographic match rule can be configured to allow requests only from the United States. For a regional API Gateway endpoint, the AWS WAF web ACL must be deployed in the same AWS Region as the API. Deploying this regional API in a US region ensures minimal latency for the target user base. Why Incorrect Options are Wrong: B. This is incorrect. For a regional resource like an API Gateway HTTP API, the A

</details>

### 177. dt-674

A company uses AWS Organizations to create dedicated AWS accounts for each business unit to manage each business unit's account independently upon request. The root email recipient missed a notification that was sent to the root user email address of one account. The company wants to ensure that all future notifications are not missed. Future notifications must be limited to account administrators. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure all AWS account root user email addresses as distribution lists that go to a few administrators who can respond to alerts. Configure AWS account alternate contacts in the AWS Organizations console or programmatically.**

</details>

### 178. gh-678

A company stores sensitive data in Amazon S3. A solutions architect needs to create an encryption solution. The company needs to fully control
the ability of users to create, rotate, and disable encryption keys with minimal effort for any data that must be encrypted.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use customer-managed KMS keys (SSE-KMS).**

Grants full control over key rotation/access. SSE-S3 (Option A) lacks key management.
Client-side encryption (Option D) is complex.

</details>

### 179. dt-692

A company is migrating applications to AWS. The applications are deployed in different accounts. The company manages the accounts centrally by using AWS Organizations. The company's security team needs a single sign-on (SSO) solution across all the company's accounts. The company must continue managing the users and groups in its on-premises self-managed Microsoft Active Directory. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.**

</details>

### 180. dt-699 `least-ops` `security`

A company recently launched a variety of new workloads on Amazon EC2 instances in its AWS account. The company needs to create a strategy to access and administer the instances remotely and securely. The company needs to implement a repeatable process that works with native AWS services and follows the AWS Well-Architected Framework. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Attach the appropriate IAM role to each existing instance and new instance. Use AWS Systems Manager Session Manager to establish a remote SSH session.**

</details>

### 181. dt-704 `least-ops`

A company has deployed a multi-account strategy on AWS by using AWS Control Tower. The company has provided individual AWS accounts to each of its developers. The company wants to implement controls to limit AWS resource costs that the developers incur. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS Budgets to establish budgets for each developer account. Set up budget alerts for actual and forecast values to notify developers when they exceed or expect to exceed their assigned budget. Use AWS Budgets actions to apply a DenyAll policy to the developer's IAM role to prevent additional resources from being launched when the assigned budget is reached.**

</details>

### 182. dt-720 `least-ops`

A company's cloud operations team wants to standardize resource remediation. The company wants to provide a standard set of governance evaluations and remediations to all member accounts in its organization in AWS Organizations. Which self-managed AWS service can the company use to meet these requirements with the LEAST amount of operational effort?

<details><summary>Answer</summary>

**B. AWS Config conformance packs**

</details>

### 183. dt-722

A company designs a mobile app for its customers to upload photos to a website. The app needs a secure login with multi-factor authentication (MFA). The company wants to limit the initial build time and the maintenance of the solution. Which solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Cognito user pools with SMS-based MFA.**

</details>

### 184. dt-724

A company is planning to use Amazon S3 to store images uploaded by its users. The images must be encrypted at rest in Amazon S3. The company does not want to spend time managing and rotating the keys, but it does want to control who can access those keys. What should a solutions architect use to accomplish this?

<details><summary>Answer</summary>

**D. Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)**

</details>

### 185. dt-727

An ecommerce company runs several internal applications in multiple AWS accounts. The company uses AWS Organizations to manage its AWS accounts. A security appliance in the company's networking account must inspect interactions between applications across AWS accounts. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Deploy a Gateway Load Balancer (GWLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the GWLB by using an interface GWLB endpoint in the application accounts.**

</details>

### 186. dt-729

A company wants to automate the security assessment of its Amazon EC2 instances. The company needs to validate and demonstrate that security and compliance standards are being followed throughout the development process. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon Inspector with Amazon CloudWatch to publish Amazon Simple Notification Service (Amazon SNS) notifications.**

</details>

### 187. dt-739

An administrator of a large company wants to monitor for and prevent any cryptocurrency-related attacks on the company's AWS accounts. Which AWS service can the administrator use to protect the company against attacks?

<details><summary>Answer</summary>

**B. Amazon GuardDuty**

</details>

### 188. dt-756

A company is preparing to deploy a data lake on AWS. A solutions architect must define the encryption strategy for data at rest in Amazon S3. The company's security policy states: Keys must be rotated every 90 days. Strict separation of duties between key users and key administrators must be implemented. Auditing key usage must be possible. What should the solutions architect recommend?

<details><summary>Answer</summary>

**A. Server-side encryption with AWS KMS managed keys (SSE-KMS) with customer managed customer master keys (CMKs)**

</details>

### 189. dt-767

A company has a dynamic web application hosted on two Amazon EC2 instances. The company has its own SSL certificate, which is on each instance to perform SSL termination. There has been an increase in traffic recently, and the operations team determined that SSL encryption and decryption is causing the compute capacity of the web servers to reach their maximum limit. What should a solutions architect do to increase the application's performance?

<details><summary>Answer</summary>

**D. Import the SSL certificate into AWS Certificate Manager (ACM). Create an Application Load Balancer with an HTTPS listener that uses the SSL certificate from ACM.**

</details>

### 190. ce-900

A company has offices in multiple countries. The company has a separate AWS account for each office. The company uses an organization in AWS Organizations to manage all the accounts. Each office has an allocated budget that is set by company leadership. The company needs a solution to monitor account costs and automatically review service consumption when an account reaches a spending threshold. The solution must not immediately disable resources when an account reaches a spending threshold. The solution must detect budget overruns as soon as possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Budgets to set budget thresholds. Use AWS Budgets actions to define a workflow to manually review accounts that overspend.**

AWS Budgets allows setting cost or usage thresholds and can trigger alerts or actions. The requirement is to review consumption, not immediately disable resources. AWS Budgets actions can be configured to send notifications via Amazon SNS or trigger a workflow, such as starting an AWS Systems Manager Automation runbook, to facilitate a manual review process. This approach meets the need to detect overruns quickly through alerts and initiates a review workflow without being destructive, satisfying all requirements of the scenario. Why Incorrect Options are Wrong: A. Service Control Policies (SCPs) are for permission guardrails and cannot be used to define or react to budget thresholds. They are used for prevention, not monitoring and alerting. C. This option violates the requirement to not immediately disable resources. While Budgets actions can restrict accounts, the question explicitly

</details>

### 191. ce-918

An application team uses an organization in AWS Organizations to manage multiple AWS accounts in a dedicated organizational unit OU. The accounts do not host production workloads. The application team is implementing an ecommerce solution by using Amazon EC2 instances. A solutions architect needs to implement controls to prevent the application team from exceeding the project budget for the application. Which solution will meet this requirement?

<details><summary>Answer</summary>

**B. Create a fixed monthly budget in AWS Budgets. Create a budget action to apply a service control policy SCP to the OU to deny additional usage when the application team reaches the monthly budget. Configure a budget action to send a notification to an Amazon SNS topic that invokes an AWS Lambda function to stop all running EC2 instances.**

The most effective solution to proactively prevent budget overruns is to use AWS Budgets with budget actions. This service allows setting a budget and configuring automated actions when a threshold is reached. The actions can include applying a Service Control Policy (SCP) to the Organizational Unit (OU) to deny new resource creation and invoking an AWS Lambda function via an Amazon SNS topic to stop existing EC2 instances. This combination provides a preventative control mechanism that directly addresses the requirement to stop spending once the budget is exceeded. Why Incorrect Options are Wrong: A. AWS Cost Explorer provides reports and alerts but does not take automated preventative action. The team must manually intervene, which does not meet the requirement. C. While a CloudWatch alarm can trigger a Lambda function to stop instances, AWS Budgets is the purpose-built service for cos

</details>

### 192. ce-968 `cost`

A solutions architect is designing an asynchronous application to process credit card data validation requests for a bank. The application must be secure and be able to process each request at least once. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Use AWS Lambda event source mapping. Set Amazon SQS standard queues as the event source. Use AWS KMS SSE-KMS for encryption. Add the kms:Decrypt permission for the Lambda execution role.**

The solution requires asynchronous, at-least-once processing in a cost-effective and secure manner. Amazon SQS standard queues provide at-least-once delivery and are more cost-effective than FIFO queues, which are designed for exactly-once processing and ordering. For securing sensitive credit card data, server-side encryption (SSE) using AWS KMS (SSE-KMS) is appropriate, providing auditable, centrally managed keys. When an AWS Lambda function processes messages from this queue, its execution role must have the kms:Decrypt permission to read the encrypted message content. This combination meets all requirements most cost-effectively. Why Incorrect Options are Wrong: B. SQS FIFO queues provide exactly-once processing, which is not required and is more expensive than standard queues. SSE-SQS offers less control than SSE-KMS. C. SQS FIFO queues are not the most cost-effective choice for an

</details>
