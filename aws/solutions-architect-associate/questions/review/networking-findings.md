# Networking — question review

Reviewed 77 questions. Found 8 problems.

## Confirmed wrong

### gh-208
**Stated answer:** B. Create a gateway VPC endpoint for Amazon S3 in the Availability Zone where the EC2 instance is located. Attach appropriate security groups to the endpoint. Attach a resource policy to the S3 bucket to only allow the EC2 instance's IAM role for access.
**Should be:** A. Create an interface VPC endpoint for Amazon S3 in the subnet where the EC2 instance is located. Attach a resource policy to the S3 bucket to only allow the EC2 instance's IAM role for access.
**Why:** A gateway endpoint is a route-table target — it is not placed in an Availability Zone or a subnet and it cannot have a security group attached, so the stated option describes something AWS does not let you build. Only an interface endpoint (PrivateLink) lives in a subnet and takes security groups. The explanation printed under the answer actually argues for the interface endpoint, so the answer line and the reasoning disagree.

## Out of date

### gh-676
**Stated answer:** B. Use VPC Flow Logs to CloudWatch Logs, then Kinesis Data Firehose to OpenSearch Service.
**Now:** The answer is still correct, but the service name is stale. Amazon Kinesis Data Firehose was renamed **Amazon Data Firehose** in February 2024. The option text in the current exam pool and in AWS documentation uses the new name; the delivery path itself is unchanged.

## Explanation problems

### wl-23
**Issue:** The rationale for ruling out the security-group option says "when the security group does not allow traffic, the failure cause will be 403 access denied." That is backwards, and it contradicts the sentence it opens with ("Same as above"). A security group that drops traffic produces a connection timeout, not an HTTP 403 — which is precisely why the security-group option can be eliminated. As written the explanation argues *for* the option it is dismissing.

### gh-29
**Issue:** The explanation is unfinished author commentary rather than a justification: "Answer A does not mention service Global Accelerator, it mentions the NLB would act like one. Not sure if the wording is wrong or not." The option plainly does name AWS Global Accelerator, and Global Accelerator is the reason the answer works (anycast static IPs, UDP listeners, latency-based routing, automatic cross-Region failover on endpoint health). The explanation needs replacing; the answer is fine.

### gh-240
**Issue:** The explanation gives the wrong reason. It claims the saving comes from the data warehouse and the visualization tool being in the same Region so "the data transfer between them doesn't incur the usual costs associated with data leaving the AWS network." The actual reason the answer wins is payload size: moving the tool next to the warehouse means only the ~500 KB rendered webpage egresses to the office instead of the 50 MB result set — roughly a 100x reduction in billable egress — and Direct Connect egress rates are lower than internet egress rates. Same-Region traffic is not uniformly free either (cross-AZ transfer is billed).

### gh-265
**Issue:** The explanation states "Deploy a public Application Load Balancer (ALB) in private subnets. This ensures that the ALB is not directly accessible from the internet." Both halves are wrong. An internet-facing ALB must have at least two public subnets with a route to an internet gateway, and it is by definition reachable from the internet. The answer is defensible (EC2 instances in private subnets, CloudFront in front of a public ALB), but the stated mechanism is not how ALB subnet placement works. It also says the EC2 instances "host the application and database tiers," which does not match the three-tier design the question asks for.

### gh-366
**Issue:** The explanation ends by rejecting the answer it just selected: "This does not meet the requirement of hosting the application on premises." It does meet it — Global Accelerator fronts Network Load Balancers that use IP targets pointing at the on-premises servers over Direct Connect or VPN, so the application stays on premises while gaining anycast entry points and UDP support. This looks like a distractor rationale pasted under the correct option.

### gh-582
**Issue:** Same pattern — the explanation undercuts the stated answer: "While this approach considers geographic location, it might not always result in the lowest latency." The question's qualifier is "minimize load time as much as possible," and geolocation is the right pick here because the only latency-routing option on offer associates a single Region, which cannot steer traffic to both the on-premises site and eu-central-1. The explanation should say why geolocation beats the alternatives given, not cast doubt on it.

Checked 77 questions: 1 factually wrong answer, 1 stale service name, and 6 explanations that are wrong or contradict their own answer — overall a usable set whose answer keys are largely sound, but whose explanations are unreliable and in several places appear to be rationales copied from the wrong option.
