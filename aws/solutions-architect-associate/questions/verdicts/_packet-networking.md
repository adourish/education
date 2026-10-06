# Flagged questions to adjudicate: networking

8 questions. For each: establish the truth, then decide keep / fix / drop.


---

## gh-208  (reviewer says: wrong)

**Reviewer's complaint:** Stated answer: B. Create a gateway VPC endpoint for Amazon S3 in the Availability Zone where the EC2 instance is located. Attach appropriate security groups to the endpoint. Attach a resource policy to the S3 bucket to only allow the EC2 instance's IAM role for access. Should be: A. Create an interface VPC endpoint for Amazon S3 in the subnet where the EC2 instance is located. Attach a resource po

**Question:**

A company needs to move data from an Amazon EC2 instance to an Amazon S3 bucket. The company must ensure that no API calls and no data are routed through public internet routes. Only the EC2 instance can have access to upload data to the S3 bucket.
Which solution will meet these requirements?

**Stated answer:** B. Create a gateway VPC endpoint for Amazon S3 in the Availability Zone where the EC2 instance is located. Attach appropriate security

**Stated explanation:** groups to the endpoint. Attach a resource policy to the S3 bucket to only allow the EC2 instance’s IAM role for access.

Interface VPC endpoints for Amazon S3 (powered by AWS PrivateLink) allow communication between resources in your VPC and Amazon S3 without relying on public internet routes. It provides a secure and private connection.
By creating an interface VPC endpoint for Amazon S3 in the subnet where the EC2 instance is located, you ensure that the data doesn't travel over the public internet.
Attaching a resource policy to the S3 bucket allows you to control access and restrict it to the IAM role associated with the EC2 instance, ensuring only authorized entities can upload data to the bucket.


---

## gh-240  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation gives the wrong reason. It claims the saving comes from the data warehouse and the visualization tool being in the same Region so "the data transfer between them doesn't incur the usual costs associated with data leaving the AWS network." The actual reason the answer wins is payload size: moving the tool next to the warehouse means only the ~500 KB rendered webpage egresses

**Question:**

A company previously migrated its data warehouse solution to AWS. The company also has an AWS Direct Connect connection. Corporate office users query the data warehouse using a visualization tool. The average size of a query returned by the data warehouse is 50 MB and each webpage sent by the visualization tool is approximately 500 KB. Result sets returned by the data warehouse are not cached.
Which solution provides the LOWEST data transfer egress cost for the company?

**Stated answer:** D. Host the visualization tool in the same AWS Region as the data warehouse and access it over a Direct Connect connection at a location in the same Region.

**Stated explanation:** Hosting the visualization tool in the same AWS Region as the data warehouse and accessing it over a Direct Connect connection within the same Region minimizes data transfer costs. Since the data warehouse and the visualization tool are in the same Region, the data transfer between them doesn't incur the usual costs associated with data leaving the AWS network.


---

## gh-265  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation states "Deploy a public Application Load Balancer (ALB) in private subnets. This ensures that the ALB is not directly accessible from the internet." Both halves are wrong. An internet-facing ALB must have at least two public subnets with a route to an internet gateway, and it is by definition reachable from the internet. The answer is defensible (EC2 instances in private sub

**Question:**

A solutions architect needs to design a highly available application consisting of web, application, and database tiers. HTTPS content delivery should be as close to the edge as possible, with the least delivery time.
Which solution meets these requirements and is MOST secure?

**Stated answer:** C. Configure a public Application Load Balancer (ALB) with multiple redundant Amazon EC2 instances in private subnets. Configure Amazon CloudFront to deliver HTTPS content using the public ALB as the origin.

**Stated explanation:** Public ALB in Private Subnets:

Deploy a public Application Load Balancer (ALB) in private subnets. This ensures that the ALB is not directly accessible from the internet, providing an additional layer of security.

Deploy multiple redundant Amazon EC2 instances in private subnets behind the ALB. The instances host the application and database tiers.

Configure Amazon CloudFront to deliver HTTPS content using the public ALB as the origin. CloudFront provides content delivery close to the edge, reducing latency and improving the delivery time for end-users.


---

## gh-29  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation is unfinished author commentary rather than a justification: "Answer A does not mention service Global Accelerator, it mentions the NLB would act like one. Not sure if the wording is wrong or not." The option plainly does name AWS Global Accelerator, and Global Accelerator is the reason the answer works (anycast static IPs, UDP listeners, latency-based routing, automatic cro

**Question:**

A company provides a Voice over Internet Protocol (VoIP) service that uses UDP connections. The service consists of Amazon EC2 instances that run in an Auto Scaling group. The company has deployments across multiple AWS Regions.
The company needs to route users to the Region with the lowest latency. The company also needs automated failover between Regions.
Which solution will meet these requirements?

**Stated answer:** A. Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region.

**Stated explanation:** Answer A does not mention service Global Accelerator, it mentions the NLB would act like one. Not sure if the wording is wrong or not.
' Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region.


---

## gh-366  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The explanation ends by rejecting the answer it just selected: "This does not meet the requirement of hosting the application on premises." It does meet it — Global Accelerator fronts Network Load Balancers that use IP targets pointing at the on-premises servers over Direct Connect or VPN, so the application stays on premises while gaining anycast entry points and UDP support. This looks li

**Question:**

367] A company is using Amazon Route 53 latency-based routing to route requests to its UDP-based application for users around the world. The application is hosted on redundant servers in the company's on-premises data centers in the United States, Asia, and Europe. The company’s compliance requirements state that the application must be hosted on premises. The company wants to improve the performance and availability of the application.
What should a solutions architect do to meet these requirements?

**Stated answer:** A. Configure three Network Load Balancers (NLBs) in the three AWS Regions to address the on-premises endpoints. Create an accelerator by using AWS Global Accelerator, and register the NLBs as its endpoints. Provide access to the application by using a CNAME that points to the accelerator DNS.

**Stated explanation:** This option suggests configuring three Network Load Balancers (NLBs) in the three AWS Regions to address on-premises endpoints. While AWS Global Accelerator is used, the NLBs are registered as its endpoints. This does not meet the requirement of hosting the application on premises.


---

## gh-582  (reviewer says: explanation)

**Reviewer's complaint:** Issue: Same pattern — the explanation undercuts the stated answer: "While this approach considers geographic location, it might not always result in the lowest latency." The question's qualifier is "minimize load time as much as possible," and geolocation is the right pick here because the only latency-routing option on offer associates a single Region, which cannot steer traffic to both the on-pr

**Question:**

An ecommerce company uses Amazon Route 53 as its DNS provider. The company hosts its website on premises and in the AWS Cloud. The company's on-premises data center is near the us-west-1 Region. The company uses the eu-central-1 Region to host the website. The company wants to minimize load time for the website as much as possible.
Which solution will meet these requirements?

**Stated answer:** A. Set up a geolocation routing policy. Send the traffic that is near us-west-1 to the on-premises data center. Send the traffic that is near eu-central-1 to eu-central-1.

**Stated explanation:** Geolocation routing directs traffic based on the geographic location of the user. This option would send users near us-west-1 to the on-premises data center and users near eu-central-1 to eu-central-1. While this approach considers geographic location, it might not always result in the lowest latency.


---

## gh-676  (reviewer says: stale)

**Reviewer's complaint:** Stated answer: B. Use VPC Flow Logs to CloudWatch Logs, then Kinesis Data Firehose to OpenSearch Service. Now: The answer is still correct, but the service name is stale. Amazon Kinesis Data Firehose was renamed **Amazon Data Firehose** in February 2024. The option text in the current exam pool and in AWS documentation uses the new name; the delivery path itself is unchanged.

**Question:**

A company's application uses Network Load Balancers, Auto Scaling groups, Amazon EC2 instances, and databases that are deployed in an
Amazon VPC. The company wants to capture information about tra c to and from the network interfaces in near real time in its Amazon VPC. The
company wants to send the information to Amazon OpenSearch Service for analysis.
Which solution will meet these requirements?

**Stated answer:** Answer: B) Use VPC Flow Logs → CloudWatch → Kinesis Firehose → OpenSearch.

**Stated explanation:** Flow Logs capture traffic; Firehose streams to OpenSearch.
CloudTrail (Options C/D) logs API calls, not network traffic.


---

## wl-23  (reviewer says: explanation)

**Reviewer's complaint:** Issue: The rationale for ruling out the security-group option says "when the security group does not allow traffic, the failure cause will be 403 access denied." That is backwards, and it contradicts the sentence it opens with ("Same as above"). A security group that drops traffic produces a connection timeout, not an HTTP 403 — which is precisely why the security-group option can be eliminated. A

**Question:**

Your organization has an existing VPC setup and has a requirement to route any traffic going from VPC to AWS S3 bucket through AWS internal network. So they have created a VPC endpoint for S3 and configured to allow traffic for S3 buckets. The application you are developing involves sending traffic to AWS S3 bucket from VPC for which you planned to use a similar approach. You have created a new route table, added route to VPC endpoint and associated route table with your new subnet. However, when you are trying to send a request from EC2 to S3 bucket using AWS CLI, the request is getting failed with 403 access denied errors. What could be causing the failure?

**Options given by the source:**

- A. AWS S3 bucket is in a different region than your VPC.
- B. EC2 security group outbound rules not allowing traffic to S3 prefix list.
- C. VPC endpoint might have a restrictive policy and does not contain the new S3
- D. S3 bucket CORS configuration does not have EC2 instances as the origin.

**Stated answer:** C. VPC endpoint might have a restrictive policy and does not contain the new S3

**Stated explanation:** Option A is not correct. The question states “403 access denied”. If the S3 bucket is in
a different region than VPC, the request looks for a route with NAT Gateway or
Internet Gateway. If it exists, the request goes through the internet to S3. If it does not
exist, the request gets failed with connection refused or connection timed out. Not
with an error “403 access denied”.
Option B is not correct. Same as above, when the security group does not allow traffic,
the failure cause will be 403 access denied.
Option C is correct.
Option D is not correct.
Cross-origin resource sharing (CORS) defines a way for client web applications that
are loaded in one domain to interact with resources in a different domain. With CORS
support, you can build rich client-side web applications with Amazon S3 and
selectively allow cross-origin access to your Amazon S3 resources.
In this case, the request is n
