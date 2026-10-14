# The security map

> Where every security question lives, top to bottom: who may do what, keys and
> secrets, who finds what, the defences, many accounts.

## zone: Who may do what | vpc

### row

**A role**
*Assumed, credentials expire*. Never an access key on a server.

**Instance role, execution role**
An app on an instance; a function. The role *is* the identity.

**Across accounts**
*A role in the far account*: a trust policy there, permission on the caller.

**Resource policy**
*An outsider at one bucket or queue*. Written on the thing itself.

**Staff with company logins**
*IAM Identity Center*, federated with their directory.

**Users of your own app**
*Cognito user pool* for the login, identity pool for AWS credentials.

**A ceiling**
*Service control policy*: limits, never grants, not the management account.
Permissions boundary: the same for one user.

## end

## arrow

Then what protects the data

## zone: Keys and secrets | sub

### row

**Who holds the key**
*SSE-S3*: nobody asked. *SSE-KMS, customer managed*: say who may use it,
audit every use. *SSE-C or client-side*: AWS never sees it.

**KMS**
Encrypts the data key; the data key encrypts the data. *Rotation changes the
outer key* only. CloudHSM: a module you control.

**Secrets Manager**
A password that must *rotate itself*. Built in to RDS, Aurora, Redshift.

**Parameter Store**
A setting, or a secret with *no rotation*, free.

**Certificates**
*ACM*, free and public, DNS validation. For CloudFront, in us-east-1.

## end

## zone: Who finds what | sub

### row

**GuardDuty**
*Threats*: a stolen key, mining, an odd login. Reads the logs itself.

**Macie**
*Personal data in S3*. Only S3.

**Inspector**
*Software flaws* on instances, containers, Lambda.

**Config**
*A setting that drifted*. What changed, and whether it is allowed.

**CloudTrail**
*Who called what, when*. Never flow logs.

**Access Analyzer, Security Hub, Detective**
*Outsiders who can reach in*; *every finding in one place*; *why it
happened*.

## end

## zone: Defences | home

### row

**WAF**
*Rules on web requests*: on CloudFront, ALB, API Gateway. Rate-based rule, IP
set, managed rules.

**Shield**
Standard is on and free. *Advanced*: big DDoS, a team, cost protection, an
NLB or Elastic IP.

**Network ACL**
The only one with *deny*. Block an address at the subnet.

**Security group**
*Allow only*, stateful, instance level. From another group by id.

**Network Firewall**
Filters a *VPC's traffic* by address, port, domain. Not web requests.

**Firewall Manager**
*The same rules in every account*. Needs Organizations.

## end

## row: hub

**Many accounts**
*Organizations* for one bill and shared discounts. *SCP on the root OU* to
stop something everywhere. *Control Tower* for new accounts set up right.
Tag policies for allowed values. *Resource Access Manager* to share a subnet
or a transit gateway.

## key

cyan: who may · amber: defences · magenta: many accounts. Underlined text is the pick.

## Notes

Config says what changed and whether it is allowed; CloudTrail says who did
it. A question asking both wants both.
