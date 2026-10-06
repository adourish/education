# Flagged questions to adjudicate: security

6 questions. For each: establish the truth, then decide keep / fix / drop.


---

## gh-232  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: B. Configure the EC2 instances with an IAM instance profile that has an IAM role with the AmazonSSMManagedInstanceCore policy attached. Should be: C. Publish VPC flow logs to Amazon CloudWatch Logs. Create the required metric filters. Create a CloudWatch metric alarm with a notification action for when the alarm is in the ALARM state. Why: Attaching an SSM instance profile only enab

**Question:**

A company runs demonstration environments for its customers on Amazon EC2 instances. Each environment is isolated in its own VPC. The company’s operations team needs to be notified when RDP or SSH access to an environment has been established.

**Stated answer:** B. Configure the EC2 instances with an IAM instance profile that has an IAM role with the AmazonSSMManagedInstanceCore policy attached.

**Stated explanation:** The correct option for notifying the operations team when RDP or SSH access to an environment has been established is:

C. Publish VPC flow logs to Amazon CloudWatch Logs. Create required metric filters. Create an Amazon CloudWatch metric alarm with a notification action for when the alarm is in the ALARM state.

Here's why:

VPC Flow Logs:** VPC flow logs capture information about the IP traffic going to and from network interfaces in your VPC. This includes information about accepted and rejected connections. To monitor RDP or SSH access, you can analyze these logs.

CloudWatch Logs:** By publishing VPC flow logs to CloudWatch Logs, you can analyze the logs using metric filters to extract relevant information.

Metric Filters:** Create metric filters to match the patterns corresponding to RDP or SSH access in the CloudWatch Logs. For example, you can create metric filters that look for


---

## gh-28  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory. Now: The substance is still correct — IAM Identity Center does require a two-way forest trust to AWS Managed Microsoft AD so it can read users and groups from

**Question:**

A company is migrating applications to AWS. The applications are deployed in different accounts. The company manages the accounts centrally by using AWS Organizations. The company's security team needs a single sign-on (SSO) solution across all the company's accounts. The company must continue managing the users and groups in its on-premises self-managed Microsoft Active Directory.
Which solution will meet these requirements?

**Stated answer:** B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the company's self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.

**Stated explanation:** Explanation:
AWS Single Sign-On (AWS SSO), now called AWS IAM Identity Center, provides centralized SSO access across multiple AWS accounts in AWS Organizations. To continue managing users and groups in the company's on-premises self-managed Microsoft Active Directory, the company can connect the directory to AWS Managed Microsoft AD by using a two-way forest trust. The two-way trust is required so IAM Identity Center can authenticate users and read users and groups from the self-managed Active Directory.

Option A is incorrect because a one-way trust is not enough for IAM Identity Center in this scenario. Option C is incomplete because it creates the trust but does not configure AWS SSO/IAM Identity Center for SSO across accounts. Option D adds unnecessary operational overhead by deploying a separate on-premises identity provider.


---

## gh-418  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation says the approach is least privilege because users "access only the specific resources (S3 bucket) defined in the trust policy of the IAM role." A trust policy defines *who may assume* the role (its Principal); it never defines resources or actions. The resource restriction comes from the permissions policy attached to the role. The stated answer (add the development account

**Question:**

A solutions architect needs to allow team members to access Amazon S3 buckets in two different AWS accounts: a development account and a production account. The team currently has access to S3 buckets in the development account by using unique IAM users that are assigned to an IAM group that has appropriate permissions in the account.
The solutions architect has created an IAM role in the production account. The role has a policy that grants access to an S3 bucket in the production account.
Which solution will meet these requirements while complying with the principle of least privilege?

**Stated answer:** B. Add the development account as a principal in the trust policy of the role in the production account.

**Stated explanation:** By adding the development account as a principal in the trust policy of the IAM role in the production account, you enable IAM users in the development account to assume the role and gain temporary permissions to access the S3 bucket in the production account.

This approach follows the principle of least privilege because it allows users in the development account to access only the specific resources (S3 bucket) defined in the trust policy of the IAM role.


---

## gh-492  (reviewer says: explanation)

**Reviewer's complaint:** Issue: This explanation — and the near-identical wording reused in gh-412, gh-433, gh-488, gh-548 and gh-619 — describes SCPs as policies that "set fine-grained permissions on AWS accounts." SCPs never grant any permission; they only set the maximum permissions an account's principals can have, and a principal still needs an identity-based or resource-based policy that allows the action. Two furth

**Question:**

A company has multiple AWS accounts for development work. Some staff consistently use oversized Amazon EC2 instances, which causes the company to exceed the yearly budget for the development accounts. The company wants to centrally restrict the creation of AWS resources in these accounts.
Which solution will meet these requirements with the LEAST development effort?

**Stated answer:** B. Use AWS Organizations to organize the accounts into organizational units (OUs). Define and attach a service control policy (SCP) to control the usage of EC2 instance types.

**Stated explanation:** AWS Organizations allows you to consolidate multiple AWS accounts into an organization that you create and centrally manage.
Organizational Units (OUs) can be used to group accounts based on different criteria, such as development, production, etc.
Service Control Policies (SCPs) are used to set fine-grained permissions on AWS accounts within an organization.
By defining an SCP and attaching it to the OUs containing the development accounts, you can restrict the EC2 instance types that can be launched.


---

## gh-644  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation states "For wildcard certificates, DNS validation is necessary." ACM supports both DNS validation and email validation for wildcard domain names; DNS validation is merely recommended because it can renew the certificate automatically. The answer (request a certificate covering the apex plus `*.example.com`, then validate ownership via DNS records) is correct, but the "necess

**Question:**

An international company has a subdomain for each country that the company operates in. The subdomains are formatted as example.com, country1.example.com, and country2.example.com. The company's workloads are behind an Application Load Balancer. The company wants to encrypt the website data that is in transit.
Which combination of steps will meet these requirements? (Choose two.)

**Stated answer:** A. Use the AWS Certificate Manager (ACM) console to request a public certificate for the apex top domain example com and a wildcard certificate for *.example.com.

**Stated explanation:** E. Validate domain ownership for the domain by adding the required DNS records to the DNS provider.

AWS Certificate Manager (ACM) is a service provided by Amazon Web Services (AWS) that simplifies the process of managing and provisioning SSL/TLS (Secure Sockets Layer/Transport Layer Security) certificates for your applications and websites. SSL/TLS certificates are essential for encrypting data in transit and securing communication between clients and servers.

 ACM requires domain ownership validation before issuing certificates. For wildcard certificates, DNS validation is necessary.


---

## gh-668  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation claims "IAM policies (Option A) cannot validate tag values." That is factually wrong. IAM policies can and routinely do validate tag values using the `aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys — for example, denying resource creation unless `aws:RequestTag/application` matches an approved value. The tag policy answer is still the better fit for an Organizati

**Question:**

A company created a new organization in AWS Organizations. The organization has multiple accounts for the company's development teams. The
development team members use AWS IAM Identity Center (AWS Single Sign-On) to access the accounts. For each of the company's applications,
the development teams must use a prede ned application name to tag resources that are created.
A solutions architect needs to design a solution that gives the development team the ability to create resources only if the application name tag
has an approved value.
Which solution will meet these requirements?

**Stated answer:** Answer: D) Create a tag policy in Organizations with allowed application names.

**Stated explanation:** Tag policies enforce standardized tagging across accounts.
IAM policies (Option A) cannot validate tag values.
