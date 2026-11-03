# The security map

> Cue on the left, pick on the right. Who may do what, keys and secrets, who
> finds what, the defences, many accounts.

## zone: Who may do what | vpc

### row

**A role**
match: IAM role|\bSTS\b|Security Token Service
*Assumed, credentials expire.* Never an access key on a server. Contractors
for a project: *STS temporary credentials on roles that expire*.

**Instance, task, execution role**
match: instance profile|instance role|task role|execution role
App on an instance: *instance role*. Fargate container reading S3: *task
role*. Lambda decrypting: *execution role*, granted on the KMS key.

**Across accounts**
match: cross-account|trust polic|trust the|Roles Anywhere
*A role in the far account*: trust policy there, permission on the caller.
A vendor's role: *trust the vendor role*. A server outside AWS with
certificates: *IAM Roles Anywhere*.

**Resource policy**
match: resource(-based)? polic|bucket polic|queue polic
*An outsider at one bucket or queue*, written on the thing itself.

**Conditions**
match: aws:SourceIp|aws:RequestedRegion|Condition|CIDR block
Only from the office: *aws:SourceIp*. Only these Regions: *aws:RequestedRegion*.
Only from one VPC: *aws:SourceVpc*. A deny with a condition beats an allow.

**People**
match: IAM group|Identity Center|\bSSO\b|\bSAML\b|identity broker|MFA|root user
Staff with company logins: *Identity Center*. LDAP that is not SAML: *a
custom identity broker with STS*. Permissions by department: *IAM groups*,
never policies on users. Root: *MFA, several devices, no daily use*.

**Users of your own app**
match: Cognito
*Cognito user pool* for the login (AD FS, Google, SAML), identity pool for
AWS credentials. An ALB can demand it.

**A ceiling**
match: service control polic|\bSCP\b|permissions boundar
Nobody in the account may: *service control policy*, limits, never grants,
not the management account. One user: *permissions boundary*.

## end

## arrow

Then what protects the data

## zone: Keys and secrets | sub

### row

**Who holds the key**
match: SSE-S3|SSE-KMS|SSE-C|client-side encryption|customer managed key
Nobody asked: *SSE-S3*. Who may use it, audit: *SSE-KMS, customer managed
key*. AWS never sees it: *SSE-C or client-side*.

**KMS**
match: \bKMS\b|CloudHSM
Encrypts the data key, which encrypts the data. *Automatic rotation* changes
the outer key only. Your own hardware module: *CloudHSM*.

**Secrets Manager**
match: Secrets Manager
A password that must *rotate itself*; built in to RDS, Aurora, Redshift.
Hardcoded credentials in an app: this.

**Parameter Store**
match: Parameter Store
A setting, or a secret with *no rotation*, free. Env vars for a container.

**Certificates**
match: Certificate Manager|\bACM\b|TLS|SSL
In transit: *ACM*, free public certificates, DNS validation; CloudFront needs
us-east-1. At rest: *KMS*. End-to-end ALB to instance: *ACM cert on the
ALB, self-signed on the instances*.

## end

## zone: Who finds what | sub

### row

**GuardDuty**
match: GuardDuty
*Threats*: stolen key, mining, odd login. Acts: *EventBridge rule, Lambda*.

**Macie**
match: Macie
*Personal data in S3.* Only S3.

**Inspector**
match: Inspector
*Software flaws* on instances, containers, Lambda.

**Config**
match: AWS Config|Config rule
*A setting that drifted*, what changed and whether allowed. Custom rule +
Lambda for anything else.

**CloudTrail**
match: CloudTrail
*Who called what, when.* Never flow logs.

**The rest**
match: Access Analyzer|Security Hub|Detective|Trusted Advisor
Outsiders who can reach in: *Access Analyzer*. Every finding in one place:
*Security Hub*. Why it happened: *Detective*. Cost, limits, best practice:
*Trusted Advisor*.

## end

## zone: Defences | home

### row

**WAF**
match: \bWAF\b
*Rules on web requests*: SQL injection, bots (*Bot Control*), rate limits,
IP sets. On CloudFront, ALB, API Gateway.

**Shield**
match: Shield
Standard on and free. *Advanced*: big DDoS, a team, cost protection, an NLB
or Elastic IP.

**Network ACL**
match: network ACL|\bNACL\b
The only one with *deny*. Block an address, or one subnet from another.

**Security group**
match: security group
*Allow only*, stateful, instance level. *From another group by id.*

**Network Firewall**
match: Network Firewall
Filters a *VPC's traffic* by address, port, domain. Not web requests.

**Firewall Manager**
match: Firewall Manager
*The same rules in every account.* Needs Organizations.

## end

## row: hub

**Many accounts**
match: Organizations|Control Tower|tag polic|Resource Access Manager|\bRAM\b|Budgets
One bill, shared discounts, chargeback: *Organizations*. Stop something
everywhere: *SCP on the root OU*. New accounts set up right: *Control Tower*.
Allowed tag values: *tag policy*. Share a subnet: *RAM*. Overspend: *Budgets
actions*.

## key

cyan: who may · amber: defences · magenta: many accounts. Underlined text is
the pick.

## Notes

Reviewed against all 82 reviewed security questions on 2026-10-15. Written as
cue: pick, so each line can be learnt as a pair.
