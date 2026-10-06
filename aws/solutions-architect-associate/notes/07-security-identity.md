# 07 — Security and Identity

> This is the **30% domain** — the largest on the exam. When two answers both work, the one with less standing privilege usually wins.

## IAM

| Cue | Answer |
|---|---|
| **User** | A person or a service with **long-term credentials** |
| **Group** | A collection of users. **Groups cannot contain other groups, and a group is not a principal** — you cannot grant a group a role. |
| **Role** | An identity with **no long-term credentials**, assumed temporarily for a set of permissions |
| **Policy** | A JSON document stating what is allowed or denied |
| Scope of IAM | **global** — not regional |
| Best practice for the root user | **enable MFA, create an admin IAM user or an Identity Center user, then never use root again**. Delete root access keys. |
| Things only the root user can do | close the account, change the support plan, change the account name or email, restore IAM user permissions, enable **MFA Delete** on S3, register as a seller in the Reserved Instance Marketplace |
| How an EC2 instance should get credentials | an **instance profile with an IAM role** — **never** hard-coded access keys |
| How a Lambda function gets credentials | its **execution role** |
| How an application on-premises gets temporary credentials | **IAM Roles Anywhere** or **STS with an identity provider** |
| How to give a mobile app access | **Cognito identity pools**, which exchange a social or user-pool login for temporary credentials |
| How to let another AWS account's users in | a **role with a trust policy naming that account**, which they assume with **sts:AssumeRole** |
| How to centrally manage workforce sign-in across many accounts | **IAM Identity Center** (the successor to AWS SSO) |
| Policy evaluation order | **explicit Deny wins → explicit Allow grants → otherwise implicit deny** |
| What never grants permission, only limits it | **SCPs, permission boundaries, session policies** |
| To find unused permissions and over-broad policies | **IAM Access Analyzer** and the **last-accessed** data in the credential report |
| To audit all credentials in the account | the **credential report** |

### The policy elements you must recognize

| Element | Meaning |
|---|---|
| `Version` | Always `"2012-10-17"` |
| `Effect` | `Allow` or `Deny` |
| `Action` | `s3:GetObject`, `ec2:*` |
| `Resource` | The ARN the action applies to |
| `Principal` | **Only in resource-based policies** — who is being granted access |
| `Condition` | `aws:SourceIp`, `aws:MultiFactorAuthPresent`, `aws:PrincipalOrgID`, `s3:prefix`, `aws:RequestedRegion` |

> **Identity-based versus resource-based.** Identity-based policies attach to a user, group, or role and have **no Principal**. Resource-based policies attach to the resource — an **S3 bucket policy, SQS queue policy, SNS topic policy, KMS key policy, Lambda resource policy** — and **must** have a Principal. Cross-account access usually needs both sides to agree.

### ARN shape — recognize it on sight

```
arn:aws:service:region:account-id:resource
arn:aws:s3:::my-bucket/my-key          <- S3 has no region or account
arn:aws:iam::123456789012:role/MyRole  <- IAM is global, so no region
```

## STS — Security Token Service

| Cue | Answer |
|---|---|
| What it issues | **temporary credentials** — an access key, a secret key, and a **session token** |
| Main API calls | **AssumeRole**, **AssumeRoleWithWebIdentity**, **AssumeRoleWithSAML**, **GetSessionToken**, **GetFederationToken** |
| Session duration | **15 minutes to 12 hours** (1 hour default for most) |
| Use it for | cross-account access, federation, temporary elevated access, identity federation for mobile and web apps |

## KMS, CloudHSM, and encryption

| Cue | Answer |
|---|---|
| **KMS** | Managed key service, integrated with nearly every AWS service. **Multi-tenant, FIPS 140-2 Level 3 validated HSMs.** |
| **CloudHSM** | A **single-tenant, dedicated hardware security module** you control. You manage the keys and AWS cannot see them. |
| When CloudHSM is the required answer | "**FIPS 140-2 Level 3 single-tenant**", "we must be the only ones with key access", "we need to run our own PKCS#11 / JCE / CNG", "SQL Server or Oracle TDE with our own HSM" |
| KMS key types | **AWS managed** (free, rotated yearly, you cannot change the policy), **customer managed** (you control the policy and rotation), **AWS owned** |
| Max data you can encrypt directly with KMS | **4 KB** |
| For anything bigger | **envelope encryption** — KMS gives you a data key, you encrypt the data with it, and store the encrypted data key alongside |
| API call that does that | **GenerateDataKey** |
| Key rotation | **automatic yearly** for AWS managed keys; **optional, configurable** for customer managed keys. The old key material is kept so old ciphertext still decrypts. |
| Scope of a KMS key | **regional** — to use encrypted snapshots in another region you must re-encrypt with a key in that region (or use a **multi-Region key**) |
| Who controls access to a KMS key | the **key policy**, plus IAM policies and grants. **A key policy is required** — IAM alone is not enough. |
| To delete a key | schedule deletion with a **7 to 30 day waiting period** |
| To store passwords and database credentials with automatic rotation | **Secrets Manager** |
| To store configuration and plain parameters for free | **Systems Manager Parameter Store** (SecureString for encrypted values) |
| Secrets Manager versus Parameter Store | Secrets Manager costs money but gives **built-in rotation with Lambda** and **cross-account access**. Parameter Store is free up to the standard tier but has **no automatic rotation**. |
| To issue and renew TLS certificates for free | **ACM** — public certificates auto-renew |
| Where an ACM certificate must live for CloudFront | **us-east-1** |

## The protection services

| Service | What it does | Trigger phrase |
|---|---|---|
| **AWS WAF** | Layer 7 web firewall on CloudFront, ALB, API Gateway, AppSync, Cognito | "**SQL injection**", "**cross-site scripting**", "block by **rate** per IP", "block by country at layer 7", "block a specific URI pattern" |
| **AWS Shield Standard** | Free, automatic layer 3 and 4 DDoS protection for everyone | "DDoS", no cost mentioned |
| **AWS Shield Advanced** | Paid, 24/7 DDoS response team, cost protection, visibility | "**DDoS Response Team**", "**reimbursement for scaling costs during an attack**", "advanced DDoS" |
| **GuardDuty** | **Threat detection** from CloudTrail, VPC Flow Logs, and DNS logs, using machine learning | "detect **unusual API calls**", "crypto-mining", "compromised instance", "no agents to install" |
| **Inspector** | **Vulnerability scanning** of EC2, ECR images, and Lambda | "scan for **CVEs**", "software vulnerabilities", "unintended network exposure" |
| **Macie** | Finds **sensitive data** in S3 using machine learning | "**PII**", "credit card numbers in S3", "data classification" |
| **Detective** | Investigates the root cause of a finding | "**investigate**", "analyse the cause of a security finding" |
| **Security Hub** | **Aggregates findings** from GuardDuty, Inspector, Macie, Config, and partners, and runs standards checks | "**single pane of glass**", "CIS benchmark compliance score" |
| **Audit Manager** | Collects evidence for audits continuously | "audit evidence", "SOC 2 / PCI / HIPAA report preparation" |
| **Artifact** | Downloads **AWS's own** compliance reports and agreements | "I need AWS's SOC report", "sign a BAA" |
| **Firewall Manager** | Centrally applies WAF, Shield, security group, and Network Firewall policies **across the organization** | "apply the same rules to **all accounts**" |
| **Network Firewall** | Managed stateful firewall at the **VPC** level, with intrusion prevention | "deep packet inspection", "domain filtering for outbound VPC traffic" |

> **The four that get confused.** GuardDuty **detects** threats from logs. Inspector **scans** for vulnerabilities in software. Macie **classifies** sensitive data in S3. Detective **investigates** after the fact. Security Hub **collects** all of their findings.

## Shared Responsibility Model

| AWS is responsible for | You are responsible for |
|---|---|
| Security **of** the cloud | Security **in** the cloud |
| Hardware, the global infrastructure, regions, AZs, edge locations | Your data, its classification and encryption |
| The hypervisor and the managed service software | Guest OS patching **on EC2**, application code |
| Physical and environmental controls | IAM users, roles, and policies |
| Decommissioning storage media | Security group and NACL configuration |
| Managed service patching (RDS, Lambda, DynamoDB) | Network traffic protection, client-side encryption |

> **The line moves with the service.** On **EC2** you patch the OS. On **RDS** AWS patches it. On **Lambda** and **S3** there is no OS to think about. Encryption and access control are **always** yours.

## Organizations and multi-account

| Cue | Answer |
|---|---|
| What Organizations gives you | **consolidated billing**, **volume discounts pooled across accounts**, **SCPs**, and account automation |
| **Service Control Policy (SCP)** | A guard rail that sets the **maximum** permissions for accounts in an OU. It **never grants** anything. |
| Does an SCP affect the management account | **No** — never. This is tested. |
| How to deny use of a region organization-wide | an **SCP with a `aws:RequestedRegion` condition** |
| Organizational unit (OU) | A folder of accounts you attach SCPs to |
| To spin up new accounts with guard rails already applied | **AWS Control Tower** |
| To deploy a stack to many accounts and regions at once | **CloudFormation StackSets** |
| To share a resource like a subnet or a Transit Gateway across accounts | **AWS Resource Access Manager (RAM)** |
| To stop spend surprises | **AWS Budgets** with alerts, plus **Cost Anomaly Detection** |
| To see cost by team | **cost allocation tags** plus **Cost Explorer** |

## Tagging

The four tag categories to name: **Technical, Automation, Business, and Security**.

| Category | Examples |
|---|---|
| Technical | `Name`, `Application`, `Version`, `Cluster` |
| Automation | `Shutdown=22:00`, `Backup=daily`, `OptIn` |
| Business | `CostCenter`, `Owner`, `Project`, `BusinessUnit` |
| Security | `Confidentiality`, `Compliance`, `DataClass` |

| Cue | Answer |
|---|---|
| To require tags on new resources | an **IAM or SCP condition** on `aws:RequestTag`, or **Tag Policies** in Organizations |
| To grant access based on tags | **attribute-based access control (ABAC)**, using `aws:ResourceTag` conditions |
| Why ABAC scales better than one policy per team | you add resources and people without writing new policies |

## Trusted Advisor

Five categories — **"CPFSS"**: **Cost Optimization, Performance, Fault Tolerance, Security, Service Limits**.

| Cue | Answer |
|---|---|
| Which checks are free on Basic and Developer support | the **core security checks and service limits** |
| Which plans unlock all checks | **Business, Enterprise On-Ramp, and Enterprise** |
| Classic findings | **idle load balancers, underutilized EC2 instances, unassociated Elastic IPs, S3 buckets open to the world, root account without MFA, exposed access keys, approaching a service limit** |
