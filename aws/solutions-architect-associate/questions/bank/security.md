# Security and identity — IAM, encryption, protection, governance

116 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-11

In regards to IAM you can edit user properties later, but you cannot use the console to change the [...].

<details><summary>Answer</summary>

**A. user name.**

</details>

### 2. wl-16

Your organization has an AWS setup and planning to build Single Sign-On for users to authenticate with on-premise Microsoft Active Directory Federation Services (ADFS) and let users log in to the AWS console using AWS STS Enterprise Identity Federation. Which of the following services do you need to call from AWS STS service after you authenticate with your on-premise?

<details><summary>Answer</summary>

**A. AssumeRoleWithSAML**

https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.
html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html

</details>

### 3. dt-33

You have been asked to tighten up the password policies in your organization after a serious security breach, so you need to consider every possible security measure. Which of the following is not an account password policy for IAM Users that can be set?

<details><summary>Answer</summary>

**C. Force IAM users to contact an account administrator when the user has entered his password incorrectly.**

</details>

### 4. dt-75

A company is building software on AWS that requires access to various AWS services. Which configuration should be used to ensure that AWS credentials (i.e., Access Key ID/Secret Access Key combination) are not compromised?

<details><summary>Answer</summary>

**B. Assign an IAM role to the Amazon EC2 instance.**

</details>

### 5. dt-82 `availability`

You are developing a new mobile application and are considering storing user preferences in AWS. This would provide a more uniform cross-device experience to users using multiple mobile devices to access the application. The preference data for each user is estimated to be 50KB in size. Additionally, 5 million customers are expected to use the application on a regular basis. The solution needs to be cost-effective, highly available, scalable and secure. How would you design a solution to meet the above requirements?

<details><summary>Answer</summary>

**B. Setup a DynamoDB table with an item for each user having the necessary attributes to hold the user preferences. The mobile application will query the user preferences directly from the DynamoDB table. Utilize STS, Web Identity Federation, and DynamoDB Fine Grained Access Control to authenticate and authorize access.**

</details>

### 6. dt-108

After creating a new IAM user which of the following must be done before they can successfully make API calls?

<details><summary>Answer</summary>

**D. Create a set of Access Keys for the user.**

</details>

### 7. dt-110

IAM's Policy Evaluation Logic always starts with a default [...] for every request, except for those that use the AWS account's root security credentials?

<details><summary>Answer</summary>

**B. Deny.**

</details>

### 8. dt-114

A corporate web application is deployed within an Amazon Virtual Private Cloud (VPC) and is connected to the corporate data center via an IPsec VPN. The application must authenticate against the on-premises LDAP server. After authentication, each logged-in user can only access an Amazon Simple Storage Space (S3) keyspace specific to that user. Which two approaches can satisfy these objectives? (Choose 2 answers)

<details><summary>Answer</summary>

**B. The application authenticates against LDAP and retrieves the name of an IAM role associated with the user. The application then calls the IAM Security Token Service to assume that IAM role. The application can use the temporary credentials to access the appropriate S3 bucket.; C. Develop an identity broker that authenticates against LDAP and then calls IAM Security Token Service to get IAM federated user credentials. The application calls the identity broker to get IAM federated user credentials with access to the appropriate S3 bucket.**

</details>

### 9. dt-129 `security`

An enterprise wants to use a third-party SaaS application. The SaaS application needs to have access to issue several API commands to discover Amazon EC2 resources running within the enterprise's account The enterprise has internal security policies that require any outside access to their environment must conform to the principles of least privilege and there must be controls in place to ensure that the credentials used by the 5aa5 vendor cannot be used by any other third party. Which of the following would meet all of these conditions?

<details><summary>Answer</summary>

**C. Create an IAM role for cross-account access allows the SaaS provider's account to assume the role and assign it a policy that allows only the actions required by the SaaS application.**

</details>

### 10. dt-148

Which of the below mentioned options is a possible solution to avoid any security threat?

<details><summary>Answer</summary>

**B. Use the IAM role and assign it to the instance.**

</details>

### 11. dt-150

You are looking to migrate your Development (Dev) and Test environments to AWS. You have decided to use separate AWS accounts to host each environment. You plan to link each accounts bill to a Master AWS account using Consolidated Billing. To make sure you Keep within budget you would like to implement a way for administrators in the Master account to have access to stop, delete and/or terminate resources in both the Dev and Test accounts. Identify which option will allow you to achieve this goal.

<details><summary>Answer</summary>

**C. Create IAM users in the Master account Create cross-account roles in the Dev and Test accounts that have full Admin permissions and grant the Master.**

</details>

### 12. dt-154

A company is building a voting system for a popular TV show. Viewers will watch the performances then visit the show's website to vote for their favorite performer. It is expected that in a short period of time after the show has finished the site will receive millions of visitors. The visitors will first login to the site using their Amazon.com credentials and then submit their vote. After the voting is completed the page will display the vote totals. The company needs to build the site such that can handle the rapid influx of traffic while maintaining good performance but also wants to keep costs to a minimum. Which of the design patterns below should they use?

<details><summary>Answer</summary>

**D. Use CloudFront and an Elastic Load Balancer in front of an auto-scaled set of web servers. The web servers will first call the Login with Amazon service to authenticate the user. The web servers will process the user's vote and store the result into an SQS queue using IAM Roles for EC2 Instances to gain permissions to the SQS queue. A set of application servers will then retrieve the items from the queue and store the result into a DynamoDB table.**

</details>

### 13. dt-155 `security`

You are designing a photo sharing mobile app. The application will store all pictures in a single Amazon S3 bucket. Users will upload pictures from their mobile device directly to Amazon S3 and will be able to view and download their own pictures directly from Amazon S3. You want to configure security to handle potentially millions of users in the most secure manner possible. What should your server-side application do when a new user registers on the photo sharing mobile application?

<details><summary>Answer</summary>

**D. Record the user's information in Amazon RDS and create a role in IAM with appropriate permissions. When the user uses their mobile app, create temporary credentials using the AWS Security Token Service `AssumeRole` function. Store these credentials in the mobile app's memory and use them to access Amazon S3. Generate new credentials the next time the user runs the mobile app.**

</details>

### 14. dt-159

A [...] is a document that provides a formal statement of one or more permissions.

<details><summary>Answer</summary>

**A. policy.**

</details>

### 15. dt-187

True or False: Amazon EC2 has no Amazon Resource Names (ARNs) because you can't specify a particular Amazon EC2 resource in an IAM policy.

<details><summary>Answer</summary>

**A. True.**

</details>

### 16. dt-203

Which service enables AWS customers to manage users and permissions in AWS?

<details><summary>Answer</summary>

**B. AWS Identity and Access Management (IAM).**

</details>

### 17. dt-213

You log in to IAM on your AWS console and notice the following message. 'Delete your root access keys.' Why do you think IAM is requesting this?

<details><summary>Answer</summary>

**D. Because they provide unrestricted access to your AWS resources.**

</details>

### 18. q-222

A company has hired an external vendor to perform work in the company’s AWS account. The vendor uses an automated tool that is hosted in an AWS account that the vendor owns. The vendor does not have IAM access to the company’s AWS account. How should a solutions architect grant this access to the vendor?

<details><summary>Answer</summary>

**A. Create an IAM role in the company’s account to delegate access to the vendor’s IAM role. Attach the appropriate IAM policies to the role for the permissions that the vendor requires.**

IAM roles allow you to delegate access to resources in your AWS account to another AWS account. In this case, you can create a role in your account and grant the vendor's IAM role permission to assume that role.  By doing this, the vendor can use temporary security credentials obtained by assuming the role to access resources in your account. This ensures that the vendor doesn't need IAM credentials from your account.

</details>

### 19. q-223

A company has deployed a Java Spring Boot application as a pod that runs on Amazon Elastic Kubernetes Service (Amazon EKS) in private subnets. The application needs to write data to an Amazon DynamoDB table. A solutions architect must ensure that the application can interact with the DynamoDB table without exposing traffic to the internet. Which combination of steps should the solutions architect take to accomplish this goal? (Choose two.)

<details><summary>Answer</summary>

**A. Attach an IAM role that has sufficient privileges to the EKS pod.**

D. Create a VPC endpoint for DynamoDB. Most Voted  This IAM role should have the necessary permissions to interact with DynamoDB. You can attach the IAM role to the pod using Kubernetes service account annotations or other mechanisms.  By creating a VPC endpoint for DynamoDB, you allow your EKS pods to access DynamoDB directly within the AWS network without traversing the public internet. This enhances security and reduces the risk of exposure.

</details>

### 20. dt-226

Is there a method in the IAM system to allow or deny access to a specific instance?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 21. dt-227

Using Amazon IAM, can I give permission based on organizational groups?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 22. q-232

A company runs demonstration environments for its customers on Amazon EC2 instances. Each environment is isolated in its own VPC. The company’s operations team needs to be notified when RDP or SSH access to an environment has been established.

<details><summary>Answer</summary>

**C. Publish VPC flow logs to Amazon CloudWatch Logs. Create the required metric filters. Create a CloudWatch metric alarm with a notification action for when the alarm is in the ALARM state.**

VPC flow logs record every accepted and rejected connection on the network interfaces in each VPC, including the destination port, so SSH (port 22) and RDP (port 3389) connections show up in the log records. Sending those logs to CloudWatch Logs lets you attach a metric filter that increments a custom metric whenever a record matches one of those ports, and a CloudWatch alarm on that metric can publish to an SNS topic to notify the operations team. The instance-profile option is wrong because AmazonSSMManagedInstanceCore just grants the instance permission to talk to Systems Manager; it produces no alert. Note the honest limit of this design: flow logs show that a connection on those ports was accepted, not that a user successfully authenticated, which is all the question asks for.

</details>

### 23. q-234

A company is building a new web-based customer relationship management application. The application will use several Amazon EC2 instances that are backed by Amazon Elastic Block Store (Amazon EBS) volumes behind an Application Load Balancer (ALB). The application will also use an Amazon Aurora database. All data for the application must be encrypted at rest and in transit. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Key Management Service (AWS KMS) to encrypt the EBS volumes and Aurora database storage at rest. Attach an AWS Certificate Manager (ACM) certificate to the ALB to encrypt data in transit.**

Using AWS KMS to encrypt EBS volumes and Aurora database storage at rest is a good practice. You can specify a KMS key when creating these resources to ensure data encryption.  Attaching an ACM certificate to the ALB allows you to use HTTPS, which encrypts data in transit between clients and the ALB. This ensures secure communication over the network.

</details>

### 24. q-239

A solutions architect needs to design a new microservice for a company’s application. Clients must be able to call an HTTPS endpoint to reach the microservice. The microservice also must use AWS Identity and Access Management (IAM) to authenticate calls. The solutions architect will write the logic for this microservice by using a single AWS Lambda function that is written in Go 1.x. Which solution will deploy the function in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create a Lambda function URL for the function. Specify AWS_IAM as the authentication type.**

Explanation: A Lambda function URL gives the function its own HTTPS endpoint directly, with no separate API Gateway resource to create or manage. Setting the auth type to AWS_IAM satisfies the IAM-authentication requirement, making this the more operationally efficient option compared to fronting the function with a full API Gateway REST API.

</details>

### 25. dt-253

In AWS, which security aspects are the customer's responsibility? (Choose 4 answers)

<details><summary>Answer</summary>

**A. Security Group and ACL (Access Control List) settings.; C. Patch management on the EC2 instance's operating system.; D. Life-cycle management of IAM credentials.; F. Encryption of EBS (Elastic Block Storage) volumes.**

</details>

### 26. dt-277

A company is preparing to give AWS Management Console access to developers. Company policy mandates identity federation and role-based access control. Roles are currently assigned using groups in the corporate Active Directory. What combination of the following will give developers access to the AWS console? (Choose 2 answers)

<details><summary>Answer</summary>

**A. AWS Directory Service AD Connector.; D. AWS identity and Access Management roles.**

</details>

### 27. q-289 `security`

A company has an AWS Lambda function that needs read access to an Amazon S3 bucket that is located in the same AWS account. Which solution will meet these requirements in the MOST secure manner?

<details><summary>Answer</summary>

**B. Apply an IAM role to the Lambda function. Apply an IAM policy to the role to grant read access to the S3 bucket.**

An IAM role provides temporary credentials to the Lambda function to access AWS resources. The function does not have persistent credentials. The IAM policy grants least privilege access by specifying read access only to the specific S3 bucket needed. Access is not granted to all S3 buckets. If the Lambda function is compromised, the attacker would only gain access to the one specified S3 bucket. They would not receive broad access to resources.

</details>

### 28. dt-300

Without [...] you must either create multiple AWS accounts-each with its own billing and subscriptions to AWS products-or your employees must share the security credentials of a single AWS account.

<details><summary>Answer</summary>

**D. Amazon IAM.**

</details>

### 29. dt-306

A company needs to deploy services to an AWS region which they have not previously used. The company currently has an AWS identity and Access Management (IAM) role for the Amazon EC2 instances, which permits the instance to have access to Amazon DynamoDB. The company wants their EC2 instances in the new region to have the same privileges. How should the company achieve this?

<details><summary>Answer</summary>

**B. Assign the existing IAM role to the Amazon EC2 instances in the new region.**

</details>

### 30. dt-319

A user has created an application which will be hosted on EC2. The application makes calls to DynamoDB to fetch certain data. The application is using the DynamoDB SDK to connect with from theEC2 instance. Which of the below mentioned statements is true with respect to the best practice for security in this scenario?

<details><summary>Answer</summary>

**B. The user should attach an IAM role with DynamoDB access to the EC2 instance.**

</details>

### 31. q-325

A company is hosting a web application from an Amazon S3 bucket. The application uses Amazon Cognito as an identity provider to authenticate users and return a JSON Web Token (JWT) that provides access to protected resources that are stored in another S3 bucket. Upon deployment of the application, users report errors and are unable to access the protected content. A solutions architect must resolve this issue by providing proper permissions so that users can access the protected content. Which solution meets these requirements?

<details><summary>Answer</summary>

**A. Update the Amazon Cognito identity pool to assume the proper IAM role for access to the protected content.**

Amazon Cognito Identity Pool: When users authenticate through Amazon Cognito, they assume roles that determine their access to AWS resources. By updating the Cognito identity pool, you can configure it to assume the proper IAM role that has the necessary permissions to access the protected content stored in the S3 bucket.  IAM Role Permissions: The IAM role associated with the identity pool should have the required permissions (e.g., S3 getObject permissions) to access the protected content in the S3 bucket.

</details>

### 32. q-330

A company is planning to store data on Amazon RDS DB instances. The company must encrypt the data at rest. What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Create a key in AWS Key Management Service (AWS KMS). Enable encryption for the DB instances.**

By creating a key in AWS KMS and enabling encryption for the RDS DB instances, you ensure that the data at rest is encrypted using the specified key.  AWS RDS supports encryption at rest, and you can use AWS KMS to manage the encryption keys. When you enable encryption for an RDS DB instance, you can specify a KMS key to use for encryption.

</details>

### 33. q-336

A company hosts a multi-tier web application that uses an Amazon Aurora MySQL DB cluster for storage. The application tier is hosted on Amazon EC2 instances. The company’s IT security guidelines mandate that the database credentials be encrypted and rotated every 14 days. What should a solutions architect do to meet this requirement with the LEAST operational effort?

<details><summary>Answer</summary>

**A. Create a new AWS Key Management Service (AWS KMS) encryption key. Use AWS Secrets Manager to create a new secret that uses the KMS key with the appropriate credentials. Associate the secret with the Aurora DB cluster. Configure a custom rotation period of 14 days.**

A proposes to create a new AWS KMS encryption key and use AWS Secrets Manager to create a new secret that uses the KMS key with the appropriate credentials. Then, the secret will be associated with the Aurora DB cluster, and a custom rotation period of 14 days will be configured. AWS Secrets Manager will automate the process of rotating the database credentials, which will reduce the operational effort required to meet the IT security guidelines.

</details>

### 34. dt-337

Through which of the following interfaces is AWS Identity and Access Management available? A. AWS Management Console. B. Command line interface (CLI). C. IAM Query API. D. Existing libraries.

<details><summary>Answer</summary>

**D. All of the above.**

</details>

### 35. q-345 `cost`

A company wants to restrict access to the content of one of its main web applications and to protect the content by using authorization techniques available on AWS. The company wants to implement a serverless architecture and an authentication solution for fewer than 100 users. The solution needs to integrate with the main web application and serve web content globally. The solution must also scale as the company's user base grows while providing the lowest login latency possible. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**A. Use Amazon Cognito for authentication. Use Lambda@Edge for authorization. Use Amazon CloudFront to serve the web application globally.**

Amazon Cognito for Authentication: Amazon Cognito is a fully managed service for user identity and access control. It provides easy integration for authentication with a serverless architecture and supports a user pool for fewer than 100 users.  Lambda@Edge for Authorization: Lambda@Edge allows you to run custom code in response to CloudFront events, including authorization. You can implement authorization logic at the edge locations closest to the end-users, providing low-latency access.  Amazon CloudFront for Content Delivery: Amazon CloudFront is a global content delivery network (CDN) that integrates seamlessly with Lambda@Edge. CloudFront can serve the web application globally, distributing content from edge locations for low-latency access.

</details>

### 36. q-359

A hospital needs to store patient records in an Amazon S3 bucket. The hospital’s compliance team must ensure that all protected health information (PHI) is encrypted in transit and at rest. The compliance team must administer the encryption key for data at rest. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use the aws:SecureTransport condition on S3 bucket policies to allow only encrypted connections over HTTPS (TLS). Configure default encryption for each S3 bucket to use server-side encryption with AWS KMS keys (SSE-KMS). Assign the compliance team to manage the KMS keys.**

it allows the compliance team to manage the KMS keys used for server-side encryption, thereby providing the necessary control over the encryption keys. Additionally, the use of the "aws:SecureTransport" condition on the bucket policy ensures that all connections to the S3 bucket are encrypted in transit.

</details>

### 37. dt-363

Every user you create in the IAM system starts with [...].

<details><summary>Answer</summary>

**C. no permissions.**

</details>

### 38. q-364

A hospital is designing a new application that gathers symptoms from patients. The hospital has decided to use Amazon Simple Queue Service (Amazon SQS) and Amazon Simple Notification Service (Amazon SNS) in the architecture. A solutions architect is reviewing the infrastructure design. Data must be encrypted at rest and in transit. Only authorized personnel of the hospital should be able to access the data. Which combination of steps should the solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**B. Turn on server-side encryption on the SNS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply a key policy to restrict key usage to a set of authorized principals.**

D. Turn on server-side encryption on the SQS components by using an AWS Key Management Service (AWS KMS) customer managed key. Apply a key policy to restrict key usage to a set of authorized principals. Set a condition in the queue policy to allow only encrypted connections over TLS.  This option ensures that data at rest in the SNS components is encrypted using an AWS KMS customer managed key. The key policy restricts key usage to authorized personnel.  This option ensures that data at rest in the SQS components is encrypted using an AWS KMS customer managed key. The key policy restricts key usage to authorized personnel, and the queue policy ensures that only encrypted connections over TLS are allowed.

</details>

### 39. q-368

A solutions architect wants all new users to have specific complexity requirements and mandatory rotation periods for IAM user passwords. What should the solutions architect do to accomplish this?

<details><summary>Answer</summary>

**A. Set an overall password policy for the entire AWS account.**

Amazon Web Services (AWS) allows you to set an account-wide password policy using AWS Identity and Access Management (IAM). This policy defines the rules and requirements for all IAM users in the AWS account. It's a centralized approach to enforce security measures consistently across all users. In this case, the solutions architect can set the specific complexity requirements and mandatory rotation periods by configuring the password policy at the AWS account level.

</details>

### 40. dt-378

True or False: Without IAM, you cannot control the tasks a particular user or system can do and what AWS resources they might use.

<details><summary>Answer</summary>

**A. True.**

</details>

### 41. dt-384

In AWS CloudHSM, in addition to the AWS recommendation that you use two or more HSM appliances in a high-availability configuration to prevent the loss of keys and data, you can also perform a remote backup/restore of a Luna SA partition if you have purchased a:

<details><summary>Answer</summary>

**B. Luna Backup HS.**

</details>

### 42. q-387 `security`

A new employee has joined a company as a deployment engineer. The deployment engineer will be using AWS CloudFormation templates to create multiple AWS resources. A solutions architect wants the deployment engineer to perform job activities while following the principle of least privilege. Which combination of actions should the solutions architect take to accomplish this goal? (Choose two.)

<details><summary>Answer</summary>

**D. Create a new IAM user for the deployment engineer and add the IAM user to a group that has an IAM policy that allows AWS CloudFormation actions only.**

E. Create an IAM role for the deployment engineer to explicitly define the permissions specific to the AWS CloudFormation stack and launch stacks using that IAM role.  This ensures that the IAM user has the necessary permissions for AWS CloudFormation but not unnecessary permissions for other AWS services.  IAM roles are more suitable for temporary elevated permissions needed during AWS CloudFormation stack operations. The deployment engineer can assume the role when required, limiting their permissions to only what is needed for those specific actions.

</details>

### 43. dt-391

After a major security breach your manager has requested a report of all users and their credentials in AWS. You discover that in IAM you can generate and download a credential report that lists all users in your account and the status of their various credentials, including passwords, access keys, MFA devices, and signing certificates. Which following statement is incorrect in regards to the use of credential reports?

<details><summary>Answer</summary>

**A. Credential reports are downloaded XML files.**

</details>

### 44. q-399 `least-ops`

A financial company hosts a web application on AWS. The application uses an Amazon API Gateway Regional API endpoint to give users the ability to retrieve current stock prices. The company’s security team has noticed an increase in the number of API requests. The security team is concerned that HTTP flood attacks might take the application offline. A solutions architect must design a solution to protect the application from this type of attack. Which solution meets these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create a Regional AWS WAF web ACL with a rate-based rule. Associate the web ACL with the API Gateway stage.**

Rate-based Rule with AWS WAF: AWS WAF provides protection against various web application attacks, including HTTP flood attacks. By using a rate-based rule, you can set thresholds for the number of requests from a client IP within a specified time period. This helps in detecting and mitigating HTTP flood attacks effectively.

</details>

### 45. dt-400

A/An [...] is the concept of allowing (or disallowing) an entity such as a user, group, or role some type of access to one or more resources.

<details><summary>Answer</summary>

**B. AWS Account.**

</details>

### 46. q-403

A developer has an application that uses an AWS Lambda function to upload files to Amazon S3 and needs the required permissions to perform the task. The developer already has an IAM user with valid IAM credentials required for Amazon S3. What should a solutions architect do to grant the permissions?

<details><summary>Answer</summary>

**D. Create an IAM execution role with the required permissions and attach the IAM role to the Lambda function.**

o grant the necessary permissions to an AWS Lambda function to upload files to Amazon S3, a solutions architect should create an IAM execution role with the required permissions and attach the IAM role to the Lambda function. This approach follows the principle of least privilege and ensures that the Lambda function can only access the resources it needs to perform its specific task.

</details>

### 47. dt-407

The AWS CloudHSM service defines a resource known as a high-availability (HA) [...], which is a virtual partition that represents a group of partitions, typically distributed between several physical HSMs for high-availability.

<details><summary>Answer</summary>

**B. partition group.**

</details>

### 48. q-412

An image-hosting company stores its objects in Amazon S3 buckets. The company wants to avoid accidental exposure of the objects in the S3 buckets to the public. All S3 objects in the entire AWS account need to remain private. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use the S3 Block Public Access feature on the account level. Use AWS Organizations to create a service control policy (SCP) that prevents IAM users from changing the setting. Apply the SCP to the account.**

AWS Organizations allows you to create service control policies (SCPs) that set fine-grained permissions for member accounts. In this case, you can create an SCP that prevents IAM users from changing the S3 Block Public Access settings. Applying this SCP to the account ensures that the configured public access settings remain in place and cannot be altered by IAM users.

</details>

### 49. dt-414

Your company has recently extended its datacenter into a VPC on AWS to add burst computing capacity as needed Members of your Network Operations Center need to be able to go to the AWSManagement Console and administer Amazon EC2 instances as necessary You don't want to create new IAM users for each NOC member and make those users sign in again to the AWS Management Console Which option below will meet the needs for your NOC members?

<details><summary>Answer</summary>

**D. Use your on-premises SAML2.0-compliam identity provider (IOP) to retrieve temporary security credentials to enable NOC members to sign in to the AWS Management Console.**

</details>

### 50. q-418 `security`

A solutions architect needs to allow team members to access Amazon S3 buckets in two different AWS accounts: a development account and a production account. The team currently has access to S3 buckets in the development account by using unique IAM users that are assigned to an IAM group that has appropriate permissions in the account. The solutions architect has created an IAM role in the production account. The role has a policy that grants access to an S3 bucket in the production account. Which solution will meet these requirements while complying with the principle of least privilege?

<details><summary>Answer</summary>

**B. Add the development account as a principal in the trust policy of the role in the production account.**

A role has two separate policies: the trust policy, which lists the principals allowed to call sts:AssumeRole on it, and the permissions policy, which lists what the role may do once assumed. Naming the development account as a principal in the trust policy lets the existing development IAM users assume the production role and receive short-lived credentials, with no second set of users or long-term access keys in the production account. Least privilege holds because the role's permissions policy already grants access to just the one production S3 bucket and nothing else, so that is the ceiling on what an assuming user can do. The development users also need sts:AssumeRole for that role ARN allowed on their own side, since both accounts must agree before a cross-account assume succeeds.

</details>

### 51. q-419

A company uses AWS Organizations with all features enabled and runs multiple Amazon EC2 workloads in the ap-southeast-2 Region. The company has a service control policy (SCP) that prevents any resources from being created in any other Region. A security policy requires the company to encrypt all data at rest. An audit discovers that employees have created Amazon Elastic Block Store (Amazon EBS) volumes for EC2 instances without encrypting the volumes. The company wants any new EC2 instances that any IAM user or root user launches in ap-southeast-2 to use encrypted EBS volumes. The company wants a solution that will have minimal effect on employees who create EBS volumes. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**E. In the Organizations management account, specify the Default EBS volume encryption setting.**

C. Create an SCP. Attach the SCP to the root organizational unit (OU). Define the SCP to deny the ec2:CreateVolume action whenthe ec2:Encrypted condition equals false.  Explanation: "Default EBS encryption" is a per-account, per-Region setting — it cannot be configured centrally from the Organizations management account (ruling out the old option E). It has to be set in each member account instead, paired with the SCP (C) as a guardrail that blocks anyone who creates a volume without encryption regardless.

</details>

### 52. q-428 `security`

A serverless application uses Amazon API Gateway, AWS Lambda, and Amazon DynamoDB. The Lambda function needs permissions to read and write to the DynamoDB table. Which solution will give the Lambda function access to the DynamoDB table MOST securely?

<details><summary>Answer</summary>

**B. Create an IAM role that includes Lambda as a trusted service. Attach a policy to the role that allows read and write access to the DynamoDB table. Update the configuration of the Lambda function to use the new role as the execution role.**

IAM Role with Lambda as a Trusted Service: This approach follows the principle of least privilege. You create an IAM role that specifically grants the required permissions to access DynamoDB and makes Lambda a trusted service. This ensures that only Lambda functions associated with this role can assume it.

</details>

### 53. dt-429

True or False: When you use the AWS Management Console to delete an IAM user, IAM also deletes any signing certificates and any access keys belonging to the user.

<details><summary>Answer</summary>

**C. True.**

</details>

### 54. q-433

A company is running its production and nonproduction environment workloads in multiple AWS accounts. The accounts are in an organization in AWS Organizations. The company needs to design a solution that will prevent the modification of cost usage tags. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a service control policy (SCP) to prevent tag modification except by authorized principals.**

SCPs in AWS Organizations are used to set fine-grained permissions on what actions AWS accounts within the organization can perform. You can create a custom SCP to specifically control access to tag modification.

</details>

### 55. q-438 `security`

A company wants to share accounting data with an external auditor. The data is stored in an Amazon RDS DB instance that resides in a private subnet. The auditor has its own AWS account and requires its own copy of the database. What is the MOST secure way for the company to share the database with the auditor?

<details><summary>Answer</summary>

**D. Create an encrypted snapshot of the database. Share the snapshot with the auditor. Allow access to the AWS Key Management Service (AWS KMS) encryption key.**

Creating an encrypted snapshot ensures that the database data is protected during the transfer and storage process. Sharing the encrypted snapshot with the auditor allows them to create their own copy of the database securely. By allowing access to the AWS KMS encryption key, the auditor can decrypt the snapshot and restore it to their own environment.

</details>

### 56. dt-459

A user has defined an AutoScaling termination policy to first delete the instance with the nearest billing hour. AutoScaling has launched 3 instances in the US-East-1A region and 2 instances in the US-East-1B region. One of the instances in the US-East-1B region is running nearest to the billing hour. Which instance will AutoScaling terminate first while executing the termination action?

<details><summary>Answer</summary>

**C. Instance with the nearest billing hour in US-East-1A.**

</details>

### 57. q-459

A company uses AWS Organizations to run workloads within multiple AWS accounts. A tagging policy adds department tags to AWS resources when the company creates tags. An accounting team needs to determine spending on Amazon EC2 consumption. The accounting team must determine which departments are responsible for the costs regardless ofAWS account. The accounting team has access to AWS Cost Explorer for all AWS accounts within the organization and needs to access all reports from Cost Explorer. Which solution meets these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**A. From the Organizations management account billing console, activate a user-defined cost allocation tag named department. Create one cost report in Cost Explorer grouping by tag name, and filter by EC2.**

While AWS provides AWS-defined tags, the use of a user-defined tag provides flexibility in terms of naming and tagging conventions. Activating the tag at the Organizations management account level ensures that the tag is applied to resources across all member accounts.

</details>

### 58. q-460 `security`

A company wants to securely exchange data between its software as a service (SaaS) application Salesforce account and Amazon S3. The company must encrypt the data at rest by using AWS Key Management Service (AWS KMS) customer managed keys (CMKs). The company must also encrypt the data in transit. The company has enabled API access for the Salesforce account.

<details><summary>Answer</summary>

**C. Create Amazon AppFlow flows to transfer the data securely from Salesforce to Amazon S3.**

Amazon AppFlow is a fully managed integration service that allows you to securely transfer data between AWS services and SaaS applications like Salesforce. It supports data encryption both in transit and at rest. With AppFlow, you can configure the integration flow, including source (Salesforce) and destination (Amazon S3), and set up encryption options. It simplifies the data transfer process and can handle the encryption requirements without the need for custom development.

</details>

### 59. dt-464

Within the IAM service a GROUP is regarded as a:

<details><summary>Answer</summary>

**D. A collection of users.**

</details>

### 60. q-476 `security`

A company is expecting rapid growth in the near future. A solutions architect needs to configure existing users and grant permissions to new users on AWS. The solutions architect has decided to create IAM groups. The solutions architect will add the new users to IAM groups based on department. Which additional action is the MOST secure way to grant permissions to the new users?

<details><summary>Answer</summary>

**C. Create an IAM policy that grants least privilege permission. Attach the policy to the IAM groups**

Creating an IAM policy that grants the least privilege required for the users' tasks is a security best practice. By attaching this policy to IAM groups, you ensure that new users added to these groups inherit the specific permissions defined in the policy.

</details>

### 61. q-484

A company wants to move from many standalone AWS accounts to a consolidated, multi-account architecture. The company plans to create many new AWS accounts for different business units. The company needs to authenticate access to these AWS accounts by using a centralized corporate directory service. Which combination of actions should a solutions architect recommend to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Create a new organization in AWS Organizations with all features turned on. Create the new AWS accounts in the organization.**

E. Set up AWS IAM Identity Center (AWS Single Sign-On) in the organization. Configure IAM Identity Center, and integrate it with the company's corporate directory service.  Create a new organization in AWS Organizations with all features turned on. Create the new AWS accounts in the organization. This is a foundational step for managing multiple AWS accounts in a consolidated manner. Option E: Set up AWS IAM Identity Center (AWS Single Sign-On) in the organization. Configure IAM Identity Center, and integrate it with the company's corporate directory service. AWS Single Sign-On (SSO) is designed to simplify and centralize authentication across multiple AWS accounts.

</details>

### 62. q-488

A 4-year-old media company is using the AWS Organizations all features feature set to organize its AWS accounts. According to the company's finance team, the billing information on the member accounts must not be accessible to anyone, including the root user of the member accounts. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a service control policy (SCP) to deny access to the billing information. Attach the SCP to the root organizational unit (OU).**

SCPs in AWS Organizations allow you to set fine-grained permissions and controls over what actions can be performed in member accounts. By creating an SCP, you can explicitly deny access to billing information for all users, including the root user, under the specified organizational unit (OU).

</details>

### 63. q-492

A company has multiple AWS accounts for development work. Some staff consistently use oversized Amazon EC2 instances, which causes the company to exceed the yearly budget for the development accounts. The company wants to centrally restrict the creation of AWS resources in these accounts. Which solution will meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**B. Use AWS Organizations to organize the accounts into organizational units (OUs). Define and attach a service control policy (SCP) to control the usage of EC2 instance types.**

An SCP is a guardrail, not a grant: it sets the maximum permissions available to principals in the accounts it applies to, and a user still needs an IAM identity-based policy that allows the action before anything works. Writing one SCP that denies ec2:RunInstances unless the ec2:InstanceType condition matches an approved list, then attaching it to the OUs holding the development accounts, stops oversized launches everywhere in those accounts at once, including by account administrators. That is far less work than maintaining IAM policies account by account or building a detection-and-remediation pipeline. Two limits to remember: an SCP never restricts the organization's management account, so keep workloads out of it, and SCPs have no effect unless all features are enabled in the organization.

</details>

### 64. dt-500

Are you able to integrate a multi-factor token service with the AWS Platform?

<details><summary>Answer</summary>

**C. Yes, using the AWS multi-factor token devices to authenticate users on the AWS platform.**

</details>

### 65. dt-501

What is the default maximum number of MFA devices in use per AWS account (at the root account level)?

<details><summary>Answer</summary>

**A. 1.**

</details>

### 66. q-503 `security`

A company runs an infrastructure monitoring service. The company is building a new feature that will enable the service to monitor data in customer AWS accounts. The new feature will call AWS APIs in customer accounts to describe Amazon EC2 instances and read Amazon CloudWatch metrics. What should the company do to obtain access to customer accounts in the MOST secure way?

<details><summary>Answer</summary>

**A. Ensure that the customers create an IAM role in their account with read-only EC2 and CloudWatch permissions and a trust policy to the company’s account.**

</details>

### 67. dt-511

A user is sending bulk emails using AWS SES. The emails are not reaching some of the targeted audience because they are not authorized by the ISPs. How can the user ensure that the emails are all delivered?

<details><summary>Answer</summary>

**A. Send an email using DKIM with SE.**

</details>

### 68. dt-516

You are setting up some IAM user policies and have also become aware that some services support resource-based permissions, which let you attach policies to the service's resources instead of to IAM users or groups. Which of the below statements is true in regards to resource-level permissions?

<details><summary>Answer</summary>

**D. Some services support resource-level permissions only for some actions.**

</details>

### 69. q-521 `security`

A retail company has several businesses. The IT team for each business manages its own AWS account. Each team account is part of an organization in AWS Organizations. Each team monitors its product inventory levels in an Amazon DynamoDB table in the team's own AWS account. The company is deploying a central inventory reporting application into a shared AWS account. The application must be able to read items from all the teams' DynamoDB tables. Which authentication option will meet these requirements MOST securely?

<details><summary>Answer</summary>

**C. In every business account, create an IAM role named BU_ROLE with a policy that gives the role access to the DynamoDB table and a trust policy to trust a specific role in the inventory application account. In the inventory account, create a role named APP_ROLE that allows access to the STS AssumeRole API operation. Configure the application to use APP_ROLE and assume the crossaccount role BU_ROLE to read the DynamoDB table.**

</details>

### 70. dt-524

Can I encrypt connections between my application and my DB Instance using SSL?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 71. q-524

A company wants to analyze and troubleshoot Access Denied errors and Unauthorized errors that are related to IAM permissions. The company has AWS CloudTrail turned on. Which solution will meet these requirements with the LEAST effort?

<details><summary>Answer</summary>

**C. Search CloudTrail logs with Amazon Athena queries to identify the errors.**

Amazon Athena allows you to query data directly from S3 using standard SQL queries. CloudTrail logs can be stored in Amazon S3, and Athena makes it easy to analyze the logs using SQL queries.

</details>

### 72. dt-528

IAM provides several policy templates you can use to automatically assign permissions to the groups you create. The [...] policy template gives the Admins group permission to access all account resources, except your AWS account information.

<details><summary>Answer</summary>

**D. Administrator Access.**

</details>

### 73. q-533

A company stores data in Amazon S3. According to regulations, the data must not contain personally identifiable information (PII). The company recently discovered that S3 buckets have some objects that contain PII. The company needs to automatically detect PII in S3 buckets and to notify the company’s security team. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Macie. Create an Amazon EventBridge rule to filter the SensitiveData event type from Macie findings and to send an Amazon Simple Notification Service (Amazon SNS) notification to the security team.**

Amazon Macie is a service designed for data discovery and classification. It can identify sensitive data, including personally identifiable information (PII). By creating an EventBridge rule to filter the SensitiveData event type, you can specifically target PII-related findings and notify the security team using Amazon SNS.

</details>

### 74. q-535

A company is building an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for its workloads. All secrets that are stored in Amazon EKS must be encrypted in the Kubernetes etcd key-value store. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a new AWS Key Management Service (AWS KMS) key. Enable Amazon EKS KMS secrets encryption on the Amazon EKS cluster.**

B. This option is the most appropriate for encrypting secrets stored in the Kubernetes etcd key-value store within Amazon EKS. Amazon EKS KMS secrets encryption allows you to encrypt secrets in etcd using an AWS Key Management Service (KMS) key. This enhances security by ensuring that the secrets are encrypted at rest.

</details>

### 75. dt-536

Which IAM role do you use to grant AWS Lambda permission to access a DynamoDB Stream?

<details><summary>Answer</summary>

**C. Execution role.**

</details>

### 76. q-548 `least-ops`

A company has separate AWS accounts for its finance, data analytics, and development departments. Because of costs and security concerns, the company wants to control which services each AWS account can use. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create organization units (OUs) for each department in AWS Organizations. Attach service control policies (SCPs) to the OUs.**

AWS Organizations and Service Control Policies (SCPs): AWS Organizations provides a way to centrally manage and organize multiple AWS accounts. By creating separate organizational units (OUs) for each department, you can apply Service Control Policies (SCPs) to control which AWS services each department's accounts can access.

</details>

### 77. dt-550

Can you create IAM security credentials for existing users?

<details><summary>Answer</summary>

**A. Yes, existing users can have security credentials associated with their account.**

</details>

### 78. q-550

A company is using AWS Key Management Service (AWS KMS) keys to encrypt AWS Lambda environment variables. A solutions architect needs to ensure that the required permissions are in place to decrypt and use the environment variables. Which steps must the solutions architect take to implement the correct permissions? (Choose two.)

<details><summary>Answer</summary>

**B. Add AWS KMS permissions in the Lambda execution role.**

D. Allow the Lambda execution role in the AWS KMS key policy.  The Lambda execution role is the role assumed by the Lambda function when it runs. It needs permissions to use the KMS key to decrypt the environment variables. Grant the kms:Decrypt permission on the specific KMS key used for encryption to the Lambda execution role.  The AWS KMS key policy controls who can use the KMS key. To grant the Lambda execution role permission to decrypt using the KMS key, modify the key policy to include a statement allowing the Lambda execution role to perform kms:Decrypt on the key.

</details>

### 79. q-553 `least-ops`

A solutions architect needs to review a company's Amazon S3 buckets to discover personally identifiable information (PII). The company stores the PII data in the us-east-1 Region and us-west-2 Region. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Configure Amazon Macie in each Region. Create a job to analyze the data that is in Amazon S3.**

Amazon Macie is a managed data security and data privacy service that uses machine learning to automatically discover, classify, and protect sensitive data, including personally identifiable information (PII). By configuring Amazon Macie in each region where the company stores PII data, you can create jobs to analyze the data in Amazon S3 and identify any PII.

</details>

### 80. dt-554

Which technique can be used to integrate AWS IAM (Identity and Access Management) with an on-premise LDAP (Lightweight Directory Access Protocol) directory service?

<details><summary>Answer</summary>

**B. Use SAML (Security Assertion Markup Language) to enable single sign-on between AWS and LDAP.**

</details>

### 81. q-556

A solutions architect is using an AWS CloudFormation template to deploy a three-tier web application. The web application consists of a web tier and an application tier that stores and retrieves user data in Amazon DynamoDB tables. The web and application tiers are hosted on Amazon EC2 instances, and the database tier is not publicly accessible. The application EC2 instances need to access the DynamoDB tables without exposing API credentials in the template. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create an IAM role that has the required permissions to read and write from the DynamoDB tables. Add the role to the EC2 instance profile, and associate the instance profile with the application instances.**

Option B is the correct choice because it leverages IAM roles and instance profiles for EC2 instances. By creating an IAM role with the necessary permissions to access DynamoDB and associating it with the EC2 instance profile, you can securely grant permissions to the EC2 instances without exposing API credentials in the CloudFormation template.

</details>

### 82. q-560 `least-ops`

A company's solutions architect is designing an AWS multi-account solution that uses AWS Organizations. The solutions architect has organized the company's accounts into organizational units (OUs). The solutions architect needs a solution that will identify any changes to the OU hierarchy. The solution also needs to notify the company's operations team of any changes. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Provision the AWS accounts by using AWS Control Tower. Use account drift notifications to identify the changes to the OU hierarchy.**

AWS Control Tower is a service that simplifies the process of setting up and governing a secure, multi-account AWS environment based on AWS best practices. It provides a pre-defined landing zone with an organizational structure, OUs, and guardrails to enforce security and compliance.  the organizational units (OUs) are established as part of the AWS Control Tower landing zone. If there are any changes to the OU hierarchy (such as moving accounts between OUs), these changes are considered drift, and AWS Control Tower can generate account drift notifications.

</details>

### 83. q-571

A company is creating a REST API. The company has strict requirements for the use of TLS. The company requires TLSv1.3 on the API endpoints. The company also requires a specific public third-party certificate authority (CA) to sign the TLS certificate. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use a local machine to create a certificate that is signed by the third-party CImport the certificate into AWS Certificate Manager (ACM). Create an HTTP API in Amazon API Gateway with a custom domain. Configure the custom domain to use the certificate.**

</details>

### 84. dt-574

A company needs to deploy virtual desktops to its customers in a virtual private cloud, leveraging existing security controls. Which set of AWS services and features will meet the company's requirements?

<details><summary>Answer</summary>

**C. AWS Directory Service, Amazon Workspaces, and AWS Identity and Access Management.**

</details>

### 85. q-586

A company has five organizational units (OUs) as part of its organization in AWS Organizations. Each OU correlates to the five businesses that the company owns. The company's research and development (R&D) business is separating from the company and will need its own organization. A solutions architect creates a separate new management account for this purpose. What should the solutions architect do next in the new management account?

<details><summary>Answer</summary>

**B. Invite the R&D AWS account to be part of the new organization after the R&D AWS account has left the prior organization.**

</details>

### 86. dt-599 `security`

How should the application use AWS credentials to access the S3 bucket securely?

<details><summary>Answer</summary>

**C. Create an IAM role for EC2 that allows list access to objects in the S3 bucket. Launch the instance with the role, and retrieve the role's credentials from the EC2 Instance metadata.**

</details>

### 87. dt-609

An organization has three separate AWS accounts, one each for development, testing, and production. The organization wants the testing team to have access to certain AWS resources in the production account. How can the organization achieve this?

<details><summary>Answer</summary>

**B. Create the IAM roles with cross account access.**

</details>

### 88. dt-611

You launch an Amazon EC2 instance without an assigned AWS identity and Access Management (IAM) role. Later, you decide that the instance should be running with an IAM role. Which action must you take in order to have a running Amazon EC2 instance with an IAM role assigned to it?

<details><summary>Answer</summary>

**D. Create an image of the instance, and use this image to launch a new instance with the desired IAM role assigned.**

</details>

### 89. q-613 `least-ops`

A company uses Amazon Elastic Kubernetes Service (Amazon EKS) to run a container application. The EKS cluster stores sensitive information in the Kubernetes secrets object. The company wants to ensure that the information is encrypted. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Enable secrets encryption in the EKS cluster by using AWS Key Management Service (AWS KMS).**

Amazon EKS provides built-in support for encrypting Kubernetes secrets using AWS Key Management Service (AWS KMS). You can enable this feature at the EKS cluster level.

</details>

### 90. q-619

A solutions architect is designing a security solution for a company that wants to provide developers with individual AWS accounts through AWS Organizations, while also maintaining standard security controls. Because the individual developers will have AWS account root user-level access to their own accounts, the solutions architect wants to ensure that the mandatory AWS CloudTrail configuration that is applied to new developer accounts is not modified. Which action meets these requirements?

<details><summary>Answer</summary>

**C. Create a service control policy (SCP) that prohibits changes to CloudTrail, and attach it the developer accounts.**

SCPs are used in AWS Organizations to set fine-grained permissions and restrictions on AWS accounts within the organization. By creating an SCP that explicitly prohibits changes to CloudTrail settings, you can enforce this restriction across all developer accounts.

</details>

### 91. q-623

A company uses Amazon API Gateway to manage its REST APIs that third-party service providers access. The company must protect the REST APIs from SQL injection and cross-site scripting attacks. What is the MOST operationally efficient solution that meets these requirements?

<details><summary>Answer</summary>

**B. Configure AWS WAF.**

AWS WAF (Web Application Firewall) is specifically designed to protect web applications from common web exploits like SQL injection and cross-site scripting (XSS) attacks. By configuring AWS WAF with API Gateway, you can create rules to filter and allow or block requests based on defined conditions, providing protection against various types of attacks.

</details>

### 92. q-628 `least-ops`

A global company runs its applications in multiple AWS accounts in AWS Organizations. The company's applications use multipart uploads to upload data to multiple Amazon S3 buckets across AWS Regions. The company wants to report on incomplete multipart uploads for cost compliance purposes. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Configure S3 Storage Lens to report the incomplete multipart upload object count.**

S3 Storage Lens is a feature in Amazon S3 that provides a comprehensive view of your storage usage and activity across multiple accounts. It helps you understand, analyze, and optimize your storage usage. You can use S3 Storage Lens to generate reports on various metrics, including the incomplete multipart upload object count.

</details>

### 93. dt-630

Can I attach more than one policy to a particular entity?

<details><summary>Answer</summary>

**A. Yes always.**

</details>

### 94. q-640

A company has an application workflow that uses an AWS Lambda function to download and decrypt files from Amazon S3. These files are encrypted using AWS Key Management Service (AWS KMS) keys. A solutions architect needs to design a solution that will ensure the required permissions are set correctly. Which combination of actions accomplish this? (Choose two.)

<details><summary>Answer</summary>

**B. Grant the decrypt permission for the Lambda IAM role in the KMS key's policy**

E. Create a new IAM role with the kms:decrypt permission and attach the execution role to the Lambda function.

</details>

### 95. q-644

An international company has a subdomain for each country that the company operates in. The subdomains are formatted as example.com, country1.example.com, and country2.example.com. The company's workloads are behind an Application Load Balancer. The company wants to encrypt the website data that is in transit. Which combination of steps will meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Use the AWS Certificate Manager (ACM) console to request a public certificate for the apex top domain example.com and a wildcard certificate for *.example.com. AND E. Validate domain ownership for the domain by adding the required DNS records to the DNS provider.**

*.example.com matches one label to the left of example.com, so it covers country1.example.com and country2.example.com but not the bare apex example.com, which is why both names are needed. ACM issues public certificates free of charge and they attach directly to the Application Load Balancer's HTTPS listener, which terminates TLS and gives encryption in transit. Before ACM issues anything it has to confirm you control the domain, and you do that by adding the CNAME records ACM supplies to the DNS zone. DNS validation is the right choice here, not because wildcards require it, but because ACM re-checks those records and renews the certificate on its own, whereas email validation needs a human to click a link every renewal.

</details>

### 96. q-645 `least-ops`

A company is required to use cryptographic keys in its on-premises key manager. The key manager is outside of the AWS Cloud because of regulatory and compliance requirements. The company wants to manage encryption and decryption by using cryptographic keys that are retained outside of the AWS Cloud and that support a variety of external key managers from different vendors. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use an AWS Key Management Service (AWS KMS) external key store backed by an external key manager.**

</details>

### 97. dt-649

A company is planning to run a group of Amazon EC2 instances that connect to an Amazon Aurora database. The company has built an AWS CloudFormation template to deploy the EC2 instances and the Aurora DB cluster. The company wants to allow the instances to authenticate to the database in a secure way. The company does not want to maintain static database credentials. Which solution meets these requirements with the LEAST operational effort?

<details><summary>Answer</summary>

**C. Configure the DB cluster to use IAM database authentication. Create a database user to use with IAM authentication. Associate a role with the EC2 instances to allow applications on the instances to access the database.**

</details>

### 98. dt-650

A company wants to configure its Amazon CloudFront distribution to use SSL/TLS certificates. The company does not want to use the default domain name for the distribution. Instead, the company wants to use a different domain name for the distribution. Which solution will deploy the certificate without incurring any additional costs?

<details><summary>Answer</summary>

**C. Request an Amazon issued public certificate from AWS Certificate Manager (ACM) in the us-east-1 Region.**

</details>

### 99. dt-666

A company has two AWS accounts: Production and Development. There are code changes ready in the Development account to push to the Production account. In the alpha phase, only two senior developers on the development team need access to the Production account. In the beta phase, more developers might need access to perform testing as well. What should a solutions architect recommend?

<details><summary>Answer</summary>

**C. Create an IAM role in the Production account with the trust policy that specifies the Development account. Allow developers to assume the role.**

</details>

### 100. dt-667

A company wants to restrict access to the content of its web application. The company needs to protect the content by using authorization techniques that are available on AWS. The company also wants to implement a serverless architecture for authorization and authentication that has low login latency. The solution must integrate with the web application and serve web content globally. The application currently has a small user base, but the company expects the application's user base to increase. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure Amazon Cognito for authentication. Implement Lambda@Edge for authorization. Configure Amazon CloudFront to serve the web application globally.**

</details>

### 101. dt-668 `least-ops`

A development team uses multiple AWS accounts for its development, Staging, and production environments Team members have been launching large Amazon EC2 instances that are underutilized. A solutions architect must prevent large instances from being launched in all accounts. How can the solutions architect meet this requirement with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an orgainization in AWS Organizations in the managment account with the default policy. Create a Service control prolicy that denies the launch of large  EC2 instances and apply to all aws accounts.**

</details>

### 102. q-668

A company created a new organization in AWS Organizations. The organization has multiple accounts for the company's development teams. The development team members use AWS IAM Identity Center (AWS Single Sign-On) to access the accounts. For each of the company's applications, the development teams must use a predefined application name to tag resources that are created. A solutions architect needs to design a solution that gives the development team the ability to create resources only if the application name tag has an approved value. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a tag policy in AWS Organizations that defines the list of allowed application names.**

A tag policy is defined once in the Organizations management account and attached to the root, an OU or an account; it declares the approved values for a tag key, and with enforcement turned on for the supported resource types it blocks tagging operations that would set a value outside that list. That gives one central list to maintain as teams and accounts come and go, which is why it beats the alternatives here. The rejection of the IAM option needs care: an IAM policy or an SCP can check tag values, for example denying a create action unless aws:RequestTag/application equals an approved name, so it is not that IAM cannot do this. It is that you would have to write and keep in sync a condition for every service and action the teams use, which is far more work than one tag policy.

</details>

### 103. dt-674

A company uses AWS Organizations to create dedicated AWS accounts for each business unit to manage each business unit's account independently upon request. The root email recipient missed a notification that was sent to the root user email address of one account. The company wants to ensure that all future notifications are not missed. Future notifications must be limited to account administrators. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure all AWS account root user email addresses as distribution lists that go to a few administrators who can respond to alerts. Configure AWS account alternate contacts in the AWS Organizations console or programmatically.**

</details>

### 104. gh-678

A company stores sensitive data in Amazon S3. A solutions architect needs to create an encryption solution. The company needs to fully control
the ability of users to create, rotate, and disable encryption keys with minimal effort for any data that must be encrypted.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use customer-managed KMS keys (SSE-KMS).**

Grants full control over key rotation/access. SSE-S3 (Option A) lacks key management.
Client-side encryption (Option D) is complex.

</details>

### 105. gh-682

A company needs a solution to enforce data encryption at rest on Amazon EC2 instances. The solution must automatically identify noncompliant
resources and enforce compliance policies on ndings.
Which solution will meet these requirements with the LEAST administrative overhead?

<details><summary>Answer</summary>

**Answer: A) Use IAM + AWS Config + Systems Manager for enforcement.**

Config detects noncompliant volumes; Systems Manager automates remediation.
Macie (Option C) is for data classification, not encryption.

</details>

### 106. dt-692

A company is migrating applications to AWS. The applications are deployed in different accounts. The company manages the accounts centrally by using AWS Organizations. The company's security team needs a single sign-on (SSO) solution across all the company's accounts. The company must continue managing the users and groups in its on-premises self-managed Microsoft Active Directory. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.**

</details>

### 107. dt-699 `least-ops` `security`

A company recently launched a variety of new workloads on Amazon EC2 instances in its AWS account. The company needs to create a strategy to access and administer the instances remotely and securely. The company needs to implement a repeatable process that works with native AWS services and follows the AWS Well-Architected Framework. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Attach the appropriate IAM role to each existing instance and new instance. Use AWS Systems Manager Session Manager to establish a remote SSH session.**

</details>

### 108. dt-704 `least-ops`

A company has deployed a multi-account strategy on AWS by using AWS Control Tower. The company has provided individual AWS accounts to each of its developers. The company wants to implement controls to limit AWS resource costs that the developers incur. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use AWS Budgets to establish budgets for each developer account. Set up budget alerts for actual and forecast values to notify developers when they exceed or expect to exceed their assigned budget. Use AWS Budgets actions to apply a DenyAll policy to the developer's IAM role to prevent additional resources from being launched when the assigned budget is reached.**

</details>

### 109. dt-720 `least-ops`

A company's cloud operations team wants to standardize resource remediation. The company wants to provide a standard set of governance evaluations and remediations to all member accounts in its organization in AWS Organizations. Which self-managed AWS service can the company use to meet these requirements with the LEAST amount of operational effort?

<details><summary>Answer</summary>

**B. AWS Config conformance packs**

</details>

### 110. dt-722

A company designs a mobile app for its customers to upload photos to a website. The app needs a secure login with multi-factor authentication (MFA). The company wants to limit the initial build time and the maintenance of the solution. Which solution should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Cognito user pools with SMS-based MFA.**

</details>

### 111. dt-724

A company is planning to use Amazon S3 to store images uploaded by its users. The images must be encrypted at rest in Amazon S3. The company does not want to spend time managing and rotating the keys, but it does want to control who can access those keys. What should a solutions architect use to accomplish this?

<details><summary>Answer</summary>

**D. Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS)**

</details>

### 112. dt-727

An ecommerce company runs several internal applications in multiple AWS accounts. The company uses AWS Organizations to manage its AWS accounts. A security appliance in the company's networking account must inspect interactions between applications across AWS accounts. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Deploy a Gateway Load Balancer (GWLB) in the networking account to send traffic to the security appliance. Configure the application accounts to send traffic to the GWLB by using an interface GWLB endpoint in the application accounts.**

</details>

### 113. dt-729

A company wants to automate the security assessment of its Amazon EC2 instances. The company needs to validate and demonstrate that security and compliance standards are being followed throughout the development process. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon Inspector with Amazon CloudWatch to publish Amazon Simple Notification Service (Amazon SNS) notifications.**

</details>

### 114. dt-739

An administrator of a large company wants to monitor for and prevent any cryptocurrency-related attacks on the company's AWS accounts. Which AWS service can the administrator use to protect the company against attacks?

<details><summary>Answer</summary>

**B. Amazon GuardDuty**

</details>

### 115. dt-756

A company is preparing to deploy a data lake on AWS. A solutions architect must define the encryption strategy for data at rest in Amazon S3. The company's security policy states: Keys must be rotated every 90 days. Strict separation of duties between key users and key administrators must be implemented. Auditing key usage must be possible. What should the solutions architect recommend?

<details><summary>Answer</summary>

**A. Server-side encryption with AWS KMS managed keys (SSE-KMS) with customer managed customer master keys (CMKs)**

</details>

### 116. dt-767

A company has a dynamic web application hosted on two Amazon EC2 instances. The company has its own SSL certificate, which is on each instance to perform SSL termination. There has been an increase in traffic recently, and the operations team determined that SSL encryption and decryption is causing the compute capacity of the web servers to reach their maximum limit. What should a solutions architect do to increase the application's performance?

<details><summary>Answer</summary>

**D. Import the SSL certificate into AWS Certificate Manager (ACM). Create an Application Load Balancer with an HTTPS listener that uses the SSL certificate from ACM.**

</details>
