# Security and identity — question review

Reviewed 54 questions. Found 6 problems.

## Confirmed wrong

### gh-232
**Stated answer:** B. Configure the EC2 instances with an IAM instance profile that has an IAM role with the AmazonSSMManagedInstanceCore policy attached.
**Should be:** C. Publish VPC flow logs to Amazon CloudWatch Logs. Create the required metric filters. Create a CloudWatch metric alarm with a notification action for when the alarm is in the ALARM state.
**Why:** Attaching an SSM instance profile only enables Systems Manager management — it sends no notification to anyone, so it cannot meet the stated requirement. VPC flow logs record accepted connections on ports 3389 (RDP) and 22 (SSH); a metric filter plus a CloudWatch alarm with an SNS action is the native way to alert the operations team. The question's own explanation says the answer is C, so the bolded letter is simply the wrong one.

## Out of date

### gh-28
**Stated answer:** B. Enable AWS Single Sign-On (AWS SSO) from the AWS SSO console. Create a two-way forest trust to connect the self-managed Microsoft Active Directory with AWS SSO by using AWS Directory Service for Microsoft Active Directory.
**Now:** The substance is still correct — IAM Identity Center does require a two-way forest trust to AWS Managed Microsoft AD so it can read users and groups from the self-managed directory, so a one-way trust is not enough. Only the naming is stale: AWS Single Sign-On was renamed AWS IAM Identity Center in 2022 and there is no "AWS SSO console" any more. The explanation already notes the rename, but the answer text should be reworded; the current exam guide uses the IAM Identity Center name throughout.

## Explanation problems

### gh-418
**Issue:** The explanation says the approach is least privilege because users "access only the specific resources (S3 bucket) defined in the trust policy of the IAM role." A trust policy defines *who may assume* the role (its Principal); it never defines resources or actions. The resource restriction comes from the permissions policy attached to the role. The stated answer (add the development account as a principal in the role's trust policy) is defensible, but the reasoning teaches the wrong model of how roles work — and the explanation omits that the development-side group still needs an `sts:AssumeRole` permission for the role's ARN.

### gh-668
**Issue:** The explanation claims "IAM policies (Option A) cannot validate tag values." That is factually wrong. IAM policies can and routinely do validate tag values using the `aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys — for example, denying resource creation unless `aws:RequestTag/application` matches an approved value. The tag policy answer is still the better fit for an Organizations-wide, centrally managed standard, but the stated reason for rejecting the IAM option is not true.

### gh-644
**Issue:** The explanation states "For wildcard certificates, DNS validation is necessary." ACM supports both DNS validation and email validation for wildcard domain names; DNS validation is merely recommended because it can renew the certificate automatically. The answer (request a certificate covering the apex plus `*.example.com`, then validate ownership via DNS records) is correct, but the "necessary" claim is a false fact to memorise.

### gh-492
**Issue:** This explanation — and the near-identical wording reused in gh-412, gh-433, gh-488, gh-548 and gh-619 — describes SCPs as policies that "set fine-grained permissions on AWS accounts." SCPs never grant any permission; they only set the maximum permissions an account's principals can have, and a principal still needs an identity-based or resource-based policy that allows the action. Two further points these explanations should state, because they are common exam traps: an SCP never restricts the organization's management account (so attaching one to the root OU leaves the management account untouched), and an SCP *does* restrict the root user of a member account, which is exactly why gh-488 and gh-619 work.

Checked 54 questions: 1 answer is outright wrong, 1 is stale on service naming, and 4 explanations contain misleading or false reasoning — so roughly 89% of the set is sound, with the IAM, encryption and Organizations answers mostly matching current AWS behaviour but the explanations needing a careful rewrite.
