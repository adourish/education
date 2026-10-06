# Networking — VPC, load balancing, DNS, edge, hybrid

252 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. q-1 `security`

A company's software development team needs an Amazon RDS Multi-AZ cluster. The RDS cluster will serve as a backend for a desktop client that is deployed on premises. The desktop client requires direct connectivity to the RDS cluster. The company must give the development team the ability to connect to the cluster by using the client when the team is in the office. Which solution provides the required connectivity MOST securely?

<details><summary>Answer</summary>

**B. Create a VPC and two private subnets. Create the RDS cluster in the private subnets. Use AWS Site- to-Site VPN with a customer gateway in the company's office.**

This solution provides the highest level of security by implementing a defense-in-depth strategy. Placing the Amazon RDS cluster in private subnets ensures it is not directly accessible from the public internet, which is a fundamental security best practice for databases. An AWS Site-to-Site VPN establishes a secure, encrypted IPsec tunnel between the company's on-premises office and the AWS VPC. This allows the desktop clients to communicate with the RDS cluster over a private, encrypted connection as if it were on the local network, without exposing any resources to the public internet. This combination of network isolation (private subnets) and encrypted transit (VPN) represents the most secure architecture for the given requirements. Why Incorrect Options are Wrong: A. Placing the RDS cluster in public subnets exposes it to the internet, which is a significant and unnecessary securit

</details>

### 2. q-4

An application runs on an Amazon EC2 instance in a VPC. The application processes logs that are stored in an Amazon S3 bucket. The EC2 instance needs to access the S3 bucket without connectivity to the internet. Which solution will provide private network connectivity to Amazon S3?

<details><summary>Answer</summary>

**A. Create a gateway VPC endpoint to the S3 bucket.**

Keywords: - EC2 in VPC - EC2 instance needs to access the S3 bucket without connectivity to the internet VPC endpoint allows you to connect to AWS services using a private network instead of using the public Internet.  With a gateway endpoint, you can access Amazon S3 from your VPC, without requiring an internet gateway or NAT device for your VPC, and with no additional cost. However, gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway.

</details>

### 3. dt-5

You are designing an intrusion detection prevention (IDS/IPS) solution for a customer web application in a single VPC. You are considering the options for implementing IOS IPS protection for traffic coming from the Internet. Which of the following options would you consider? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Implement IDS/IPS agents on each Instance running in VPC.; D. Implement a reverse proxy layer in front of web servers and configure IDS/ IPS agents on each reverse proxy server.**

</details>

### 4. dt-7

How can the domain's zone apex, for example, 'myzoneapexdomain.com', be pointed towards an Elastic Load Balancer?

<details><summary>Answer</summary>

**A. By using an Amazon Route 53 Alias record.**

</details>

### 5. q-9 `least-ops`

A company wants to isolate its workloads by creating an AWS account for each workload. The company needs a solution that centrally manages networking components for the workloads. The solution also must create accounts with automatic security controls (guardrails). Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use AWS Control Tower to deploy accounts. Create a networking account that has a VPC with private subnets and public subnets. Use AWS Resource Access Manager (AWS RAM) to share the subnets with the workload accounts.**

This solution correctly addresses all requirements with the least operational overhead. AWS Control Tower is the designated service for setting up and governing a secure, multi-account AWS environment with pre-configured security controls, known as guardrails. This directly fulfills the need for automated security. Creating a dedicated networking account to host a central VPC and then sharing its subnets with workload accounts using AWS Resource Access Manager (AWS RAM) is a standard and efficient pattern. This centralizes network management, allowing workload accounts to deploy resources into the shared subnets without managing their own VPCs, thus minimizing administrative effort. Why Incorrect Options are Wrong: B. Use AWS Organizations to deploy accounts. Create a networking account that has a VPC with private subnets and public subnets. Use AWS Resource Access Manager (AWS RAM) to s

</details>

### 6. wl-11

Which of the following statements are true with respect to VPC? (choose multiple)

<details><summary>Answer</summary>

**B. A network ACL can be associated with multiple subnets.; D. Subnet’s IP CIDR block can be same as the VPC CIDR block.**

Option A is not correct. A subnet can have only one route table associated with it.
Option B is correct.
Option C is not correct.
Option D is correct.
Aspired to learn AWS? Here we bring the AWS CHEAT SHEET that will take you
through cloud Computing and AWS basics along with AWS products and services!

</details>

### 7. dt-15

After an Amazon VPC instance is launched, can I change the VPC security groups it belongs to?

<details><summary>Answer</summary>

**B. Yes. You can.**

</details>

### 8. q-15

A company recently migrated to AWS and wants to implement a solution to protect the traffic that flows in and out of the production VPC. The company had an inspection server in its on-premises data center. The inspection server performed specific operations such as traffic flow inspection and traffic filtering. The company wants to have the same functionalities in the AWS Cloud. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Network Firewall to create the required rules for traffic inspection and traffic filtering for the production VPC.**

AWS Network Firewall is a managed firewall service that provides filtering for both inbound and outbound network traffic. It allows you to create rules for traffic inspection and filtering, which can help protect your production VPC

</details>

### 9. dt-16

If I want an instance to have a public IP address, which IP address should I use?

<details><summary>Answer</summary>

**A. Elastic IP Address.**

</details>

### 10. wl-17

How many VPCs can an Internet Gateway be attached to at any given time?

<details><summary>Answer</summary>

**C. 1**

https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/amazon-vpc-limits.html
#vpc-limits-gateways
At any given time, an Internet Gateway can be attached to only one VPC. It can be
detached from the VPC and be used for another VPC.

</details>

### 11. wl-18

Your organization was planning to develop a web application on AWS EC2. Application admin was tasked to perform AWS setup required to spin EC2 instance inside an existing private VPC. He/she has created a subnet and wants to ensure no other subnets in the VPC can communicate with your subnet except for the specific IP address. So he/she created a new route table and associated with the new subnet. When he/she was trying to delete the route with the target as local, there is no option to delete the route. What could have caused this behavior?

<details><summary>Answer</summary>

**B. A route with the target as local cannot be deleted.**

https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.htm
l#RouteTa

</details>

### 12. dt-21

How can I change the security group membership for interfaces owned by other AWS, such as Elastic Load Balancing?

<details><summary>Answer</summary>

**A. By using the service specific console or APICLI commands.**

</details>

### 13. dt-22

You have created a Route 53 latency record set from your domain to a machine in Northern Virginia and a similar record to a machine in Sydney. When a user located in US visits your domain he will be routed to

<details><summary>Answer</summary>

**A. Northern Virginia.**

</details>

### 14. wl-22

You had set up an internal HTTP(S) Elastic Load Balancer to route requests to two EC2 instances inside a private VPC. However, one of the target EC2 instance is showing Unhealthy status. Which of the following options could not be a reason for this?

<details><summary>Answer</summary>

**B. An EC2 instance is in different availability zones than load balancer.**

If a target is taking longer than expected to enter the InService state, it might be
failing health checks. Your target is not in service until it passes one health check.
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-tro
ubleshooting.html#target-not-inservice
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-heal
th-checks.html

</details>

### 15. wl-23

Your organization has an existing VPC setup and has a requirement to route any traffic going from VPC to AWS S3 bucket through AWS internal network. So they have created a VPC endpoint for S3 and configured to allow traffic for S3 buckets. The application you are developing involves sending traffic to AWS S3 bucket from VPC for which you planned to use a similar approach. You have created a new route table, added route to VPC endpoint and associated route table with your new subnet. However, when you are trying to send a request from EC2 to S3 bucket using AWS CLI, the request is getting failed with 403 access denied errors. What could be causing the failure?

<details><summary>Answer</summary>

**C. VPC endpoint might have a restrictive policy and does not contain the new S3 bucket.**

The failure is an HTTP 403 AccessDenied, which means the request reached Amazon S3 and was refused on authorization rather than being lost on the network. A VPC endpoint policy narrows what the endpoint is allowed to do, so an existing policy that names only the original buckets will reject calls to the newly added bucket with exactly that error, and the fix is to add the new bucket to the endpoint policy. The other options all produce different symptoms: a security group that does not permit outbound traffic to the S3 prefix list silently drops the packets, so the CLI hangs and then reports a connection timeout rather than a 403, and a bucket in another Region is not served by the gateway endpoint at all, so without a NAT gateway or internet gateway route the request also times out. CORS applies only to browser requests from a web page in another origin and has no bearing on an AWS CLI call.

</details>

### 16. dt-24

Which one of the below doesn't affect Amazon CloudFront billing?

<details><summary>Answer</summary>

**A. Distribution Type.**

</details>

### 17. wl-25

Which of the following is an AWS component which consumes resources from your VPC?

<details><summary>Answer</summary>

**D. NAT Gateway**

Option A is not correct.
An internet gateway is an AWS component which sits outside of your VPC does not
consume any resources from your VPC.
Option B is not correct.
Endpoints are virtual devices. They are horizontally scaled, redundant, and highly
available VPC components that allow communication between instances in your VPC
and services without imposing availability risks or bandwidth constraints on your
network traffic.
Option C is not correct.
An Elastic IP address is a static, public IPv4 address designed for dynamic cloud
computing. You can associate an Elastic IP address with any instance or network
interface for any VPC in your account. With an Elastic IP address, you can mask the
failure of an instance by rapidly remapping the address to another instance in your
VPC.
They do not belong to a single VPC.
Option D is correct.
To create a NAT gateway, you must specify the public subnet in which the NAT
gateway should reside. For more information about public and private subnets, see
Subnet Routing. You must also specify an Elastic IP address to associate with the
NAT gateway when you create it. After you've created a NAT gateway, you must
update the route table associated wi

</details>

### 18. wl-26

You have successfully set up a VPC peering connection in your account between two VPCs – VPC A and VPC B, each in a different region. When you are trying to make a request from VPC A to VPC B, the request fails. Which of the following could be a reason?

<details><summary>Answer</summary>

**C. Routes not configured in route tables for peering connections.**

Option A is not correct. Cross-region VPC peering is supported in AWS.
Option B is not correct.
When the VPC IP CIDR blocks are overlapping, you cannot create a peering
connection. Question states the peering connection was successful.
Option C is correct.
To send private IPv4 traffic from your instance to an instance in a peer VPC, you
must add a route to the route table that's associated with your subnet in which your
instance resides. The route points to the CIDR block (or portion of the CIDR block) of
the peer VPC in the VPC peering connection.
https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-peering-routing.h
tml
Option D is not correct.
A security group’s default outbound rule allows all traffic to go out from the resources
attached to the security group.
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.ht
ml#Defaul

</details>

### 19. wl-27

Which of the following statements are true in terms of allowing/denying traffic from/to VPC assuming the default rules are not in effect? (choose multiple)

<details><summary>Answer</summary>

**B. In a Network ACL, for a successful HTTPS connection, you must add an inbound; C. In a Security Group, for a successful HTTPS connection, add an inbound rule with**

Security groups are stateful — if you send a request from your instance, the response
traffic for that request is allowed to flow in regardless of inbound security group rules.
Responses to allowed inbound traffic are allowed to flow out, regardless of outbound
rules.
Network ACLs are stateless; responses to allowed inbound traffic are subject to the
rules for outbound traffic (and vice versa).

Option A is not correct. NACL must have an outbound rule defined for a
successful connection due to its stateless nature.

Option B is correct.

Option C is correct.

Configuring an inbound rule in a security group is enough for a successful
connection due to its stateful nature.

Option D is not correct.
Configuring an outbound rule for incoming connection is not required in security
groups.

https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html#A
CLs

https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGrou
ps.html#VPCSe
Frequently Asked Questions (FAQs)
How many questions are on AWS exam?
The number of questions in the AWS Architect exam is around 60-70. This number
could be varry.
What is passing score for AWS?
The passing score of the exam is around

</details>

### 20. q-28

An enterprise is implementing a hub-and-spoke VPC architecture with a central security VPC for inspection and a dozen application VPCs. Network traffic from application VPCs must flow through security appliances in the central VPC for inspection before reaching the internet. Which AWS service architecture should be used to enforce this requirement at scale?

<details><summary>Answer</summary>

**B. Use Transit Gateway with Network Firewall attached to the security VPC, configuring rules to inspect all traffic. Create VPC peering between each application VPC and the security VPC, manually managing routes in each VPC.**

To implement a scalable hub-and-spoke architecture with centralized egress inspection, AWS Transit Gateway is the recommended service. It acts as a central cloud router, simplifying network topology. By attaching the application VPCs (spokes) and a central security VPC to the Transit Gateway, you can use Transit Gateway route tables to direct all outbound internet traffic from the application VPCs to the security VPC. Within the security VPC, AWS Network Firewall inspects the traffic before routing it to a NAT Gateway and an Internet Gateway. This architecture scales seamlessly, avoids complex point-to-point peering, and provides centralized security management for enterprise workloads. Why Incorrect Options are Wrong: A. Gateway endpoints are exclusively used to access Amazon S3 and DynamoDB privately; they cannot route general internet traffic through security appliances. C. VPC peerin

</details>

### 21. dt-32

Security groups act like a firewall at the instance level, whereas [...] are an additional layer of security that act at the subnet level.

<details><summary>Answer</summary>

**C. network ACLs.**

</details>

### 22. q-35 `cost` `security`

A solutions architect wants to design a data warehouse by using an Amazon Redshift cluster in the eu-west-1 Region. The data warehouse will initially ingest data from Amazon DynamoDB tables in eu- west-1. The VPC that the Redshift cluster will be deployed in must not connect to the internet. Which solution will securely load data MOST cost-effectively?

<details><summary>Answer</summary>

**A. Create a DynamoDB gateway VPC endpoint within the VPC. Add a route from the VPC subnets to the DynamoDB prefix list by using the gateway endpoint. Add a resource policy to the endpoint to allow the Redshift cluster to access the specific workload tables.**

To allow a resource in a private VPC to securely access AWS services like DynamoDB without traversing the internet, a VPC endpoint is required. DynamoDB supports Gateway VPC endpoints, which are highly available, scalable, and do not incur hourly charges or data processing fees, making them the most cost-effective option. A gateway endpoint adds a route to the VPC's route table for the service's public IP range, directing traffic through the AWS private network. Endpoint policies can be attached to restrict access to specific DynamoDB tables for enhanced security. Why Incorrect Options are Wrong: B. An interface endpoint would work but is not the most cost-effective solution, as it has both hourly and per-GB data processing charges, unlike a gateway endpoint. C. This option describes an interface endpoint, which is more expensive than the available gateway endpoint for DynamoDB. D. Dynam

</details>

### 23. q-38 `cost`

A company is hosting a static website on Amazon S3 and is using Amazon Route 53 for DNS. The website is experiencing increased demand from around the world. The company must decrease latency for users who access the website. Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Add an Amazon CloudFront distribution in front of the S3 bucket. Edit the Route 53 entries to point to the CloudFront distribution.**

Amazon CloudFront is a content delivery network (CDN) service that distributes content globally to reduce latency. By setting up a CloudFront distribution in front of the S3 bucket hosting the static website, you can take advantage of its edge locations around the world to deliver content from the nearest location to the users, reducing the latency they experience.  CloudFront automatically caches and replicates content to its edge locations, resulting in faster delivery and lower latency for users worldwide. This solution is highly effective in optimizing performance while keeping costs under control because CloudFront charges are based on actual data transfer and requests, and the pay-as-you-go pricing model ensures that you only pay for what you use.

</details>

### 24. dt-39

You are configuring a new VPC for one of your clients for a cloud migration project, and only a public VPN will be in place. After you created your VPC, you created a new subnet, a new internet gateway, and attached your internet gateway to your VPC. When you launched your first instance into your VPC, you realized that you aren't able to connect to the instance, even if it is configured with an elastic IP. What should be done to access the instance?

<details><summary>Answer</summary>

**A. A route should be created as 0.0.0.0/0 and your internet gateway as target.**

</details>

### 25. q-40

A company runs an Amazon Redshift cluster in a VPC in an AWS account named Account

<details><summary>Answer</summary>

**A. Create a VPC peering connection between each team's VPC and Account A's VPC.**

VPC peering is the most cost-effective solution for connecting a small number of VPCs (five team VPCs to one central VPC) within the same AWS Region. Unlike AWS Transit Gateway or AWS PrivateLink, VPC peering does not incur any hourly base charges or data processing fees; you only pay standard intra-region data transfer rates. Since the data volume is minimal (1 GB per database nightly) and the number of VPCs is well below the peering limit, establishing a hub-and-spoke VPC peering topology minimizes costs while securely routing traffic between the Aurora databases and the Redshift cluster across different AWS accounts. Why Incorrect Options are Wrong: B. Interface VPC endpoints (AWS PrivateLink) incur hourly endpoint charges and per-GB data processing fees, making it significantly more expensive than VPC peering for this scenario. C. AWS Transit Gateway charges an hourly fee per VPC att

</details>

### 26. q-42

A company is building an application in the AWS Cloud. The application is hosted on Amazon EC2 instances behind an Application Load Balancer (ALB). The company uses Amazon Route 53 for the DNS. The company needs a managed solution with proactive engagement to detect against DDoS attacks. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Subscribe to AWS Shield Advanced. Configure hosted zones in Route 53 Add ALB resources as protected resources.**

AWS Shield Advanced is a managed Distributed Denial of Service (DDoS) protection service that provides enhanced protections for applications running on AWS. A key feature of Shield Advanced is 24x7 access to the AWS Shield Response Team (SRT), which offers expert assistance before, during, and after a DDoS attack. This direct, expert involvement fulfills the requirement for a "managed solution with proactive engagement." The service is designed to protect resources such as Application Load Balancers (ALBs) and Amazon Route 53 hosted zones, which are specified in the scenario. Why Incorrect Options are Wrong: A. AWS Config is a service for assessing, auditing, and evaluating the configurations of AWS resources. It is not a DDoS detection or mitigation service. B. AWS WAF is a web application firewall that helps protect against common web exploits. While it can mitigate Layer 7 DDoS attack

</details>

### 27. q-42 `cost` `availability`

A company runs a highly available image-processing application on Amazon EC2 instances in a single VPC. The EC2 instances run inside several subnets across multiple Availability Zones. The EC2 instances do not communicate with each other. However, the EC2 instances download images from Amazon S3 and upload images to Amazon S3 through a single NAT gateway. The company is concerned about data transfer charges. What is the MOST cost-effective way for the company to avoid Regional data transfer charges?

<details><summary>Answer</summary>

**C. Deploy a gateway VPC endpoint for Amazon S3.**

S3 VPC endpoint provides a way for an S3 request to be routed through to the Amazon S3 service, without having to connect a subnet to an internet gateway. The S3 VPC endpoint is what's known as a gateway endpoint.

</details>

### 28. dt-43

You are in the process of creating a Route 53 DNS failover to direct traffic to two EC2 zones. Obviously, if one fails, you would like Route 53 to direct traffic to the other region. Each region has an ELB with some instances being distributed. What is the best way for you to configure the Route 53 health check?

<details><summary>Answer</summary>

**D. Route 53 natively supports ELB with an internal health check. Turn 'Evaluate target health' on and 'Associate with Health Check' off and R53 will use the ELB's internal health check.**

</details>

### 29. q-47

A company hosts a video streaming web application in a VPC. The company uses a Network Load Balancer (NLB) to handle TCP traffic for real-time data processing. There have been unauthorized attempts to access the application. The company wants to improve application security with minimal architectural change to prevent unauthorized attempts to access the application. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS Shield Advanced to provide enhanced DDoS protection and prevent unauthorized access attempts.**

A Network Load Balancer (NLB) operates at the transport layer (Layer 4) of the OSI model, handling TCP and UDP traffic. The phrase "unauthorized attempts to access the application" in this context often refers to network-level attacks such as Distributed Denial of Service (DDoS). AWS Shield Advanced is a managed threat protection service specifically designed to safeguard applications against DDoS attacks. It can be enabled on resources like an NLB (by protecting its associated Elastic IP address) with no architectural changes. This directly addresses the security requirement while adhering to the constraint of minimal architectural modification. Why Incorrect Options are Wrong: A. AWS WAF is a web application firewall that operates at the application layer (Layer 7) and cannot be directly integrated with a Network Load Balancer, which is a Layer 4 service. B. Security groups cannot be d

</details>

### 30. dt-50

A [...] for a VPC is a collection of subnets (typically private) that you may want to designate for your backend RDS DB Instances.

<details><summary>Answer</summary>

**C. DB Subnet Group.**

</details>

### 31. dt-51

An instance is launched into a VPC subnet with the network ACL configured to allow all inbound traffic and deny all outbound traffic. The instance's security group is configured to allow SSH from any IP address and deny all outbound traffic. What changes need to be made to allow SSH access to the instance?

<details><summary>Answer</summary>

**B. The outbound network ACL needs to be modified to allow outbound traffic.**

</details>

### 32. dt-61

A friend tells you he is being charged $100 a month to host his WordPress website, and you tell him you can move it to AWS for him and he will only pay a fraction of that, which makes him very happy. He then tells you he is being charged $50 a month for the domain, which is registered with the same people that set it up, and he asks if it's possible to move that to AWS as well. You tell him you aren't sure, but will look into it. Which of the following statements is true in regards to transferring domain names to AWS?

<details><summary>Answer</summary>

**B. You can transfer existing domains into Amazon Route 53's management.**

</details>

### 33. dt-72

Any person or application that interacts with AWS requires security credentials. AWS uses these credentials to identify who is making the call and whether to allow the requested access. You have just set up a VPC network for a client and you are now thinking about the best way to secure this network. You set up a security group called vpcsecuritygroup. Which following statement is true in respect to the initial settings that will be applied to this security group if you choose to use the default settings for this group?

<details><summary>Answer</summary>

**B. Allow no inbound traffic and allow all outbound traffic.**

</details>

### 34. dt-73

Which one of the below is not an AWS Storage Service?

<details><summary>Answer</summary>

**C. Amazon CloudFront.**

</details>

### 35. q-75

A company is migrating a new application from an on-premises data center to a new VPC in the AWS Cloud. The company has multiple AWS accounts and VPCs that share many subnets and applications. The company wants to have fine-grained access control for the new application.The company wants to ensure that all network resources across accounts and VPCs that are granted permission to access the new application can access the application. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy a transit gateway in the account that hosts the new application. Share the transit gateway with each account that needs to connect to the application. Update route tables in the VPC that hosts the new application and in the transit gateway to enable connectivity.**

An AWS Transit Gateway acts as a cloud router and a central hub for connecting multiple VPCs and on-premises networks. This hub-and-spoke model significantly simplifies network management and scaling compared to complex VPC peering meshes. The Transit Gateway can be created in one account and shared with other accounts using AWS Resource Access Manager (RAM). This allows resources in VPCs from different accounts to connect to the central gateway. By using Transit Gateway route tables, the company can implement fine-grained routing policies, ensuring that only authorized VPCs can communicate with the new application's VPC, thus meeting the requirements for scalable, cross-account connectivity with fine-grained access control. Why Incorrect Options are Wrong: A. VPC peering creates 1-to-1 connections. In an environment with many VPCs, this results in a complex, hard-to-manage "full mesh" n

</details>

### 36. dt-79 `availability`

You are designing Internet connectivity for your VPC. The Web servers must be available on the Internet. The application must have a highly available architecture. Which alternatives should you consider? (Choose 2 answers)

<details><summary>Answer</summary>

**C. Place all your web servers behind EL8 Configure a Route 53 CNAME to point to the ELB DNS name.; D. Assign EIPs to all web servers. Configure a Route 53 record set with all EIPs. With health checks and DNS failover.**

</details>

### 37. dt-84

You have deployed a web application targeting a global audience across multiple AWS Regions under the domain name.example.com. You decide to use Route 53 Latency-Based Routing to serve web requests to users from the region closest to the user. To provide business continuity in the event of server downtime you configure weighted record sets associated with two web servers in separate Availability Zones per region. During a DR test you notice that when you disable all web servers in one of the regions Route 53 does not automatically direct all users to the other region. What could be happening? (Choose 2 answers)

<details><summary>Answer</summary>

**B. You did not setup an HTTP health check for one or more of the weighted resource record sets associated with the disabled web servers.; E. You did not set 'Evaluate Target Health' to 'Yes' on the latency alias resource record set associated with example com in the region where you disabled the servers.**

</details>

### 38. dt-86

You've been hired to enhance the overall security posture for a very large e-commerce site. They have a well architected multi-tier application running in a VPC that uses ELBs in front of both the web and the app tier with static assets served directly from S3. They are using a combination of RDS and DynamoDB for their dynamic data and then archiving nightly into S3 for further processing with EMR. They are concerned because they found questionable log entries and suspect someone is attempting to gain unauthorized access. Which approach provides a cost effective scalable mitigation to this kind of attack?

<details><summary>Answer</summary>

**C. Add a WAF tier by creating a new ELB and an AutoScaling group of EC2 Instances running a host based WAF. They would redirect Route 53 to resolve to the new WAF tier ELB. The WAF tier would then pass the traffic to the current web tier. The web tier Security Groups would be updated to only allow traffic from the WAF tier Security Group.**

</details>

### 39. dt-87

You are designing the network infrastructure for an application server in Amazon VPC. Users will access all the application instances from the Internet as well as from an on-premises network. The on-premises network is connected to your VPC over an AWS Direct Connect link. How would you design routing to meet the above requirements?

<details><summary>Answer</summary>

**A. Configure a single routing Table with a default route via the Internet gateway. Propagate a default route via BGP on the AWS Direct Connect customer router. Associate the routing table with all VPC subnets.**

</details>

### 40. q-89

A company is launching a new application that will be hosted on Amazon EC2 instances. A solutions architect needs to design a solution that does not allow public IPv4 access that originates from the internet. However, the solution must allow the EC2 instances to make outbound IPv4 internet requests.

<details><summary>Answer</summary>

**A. Deploy a NAT gateway in public subnets in both Availability Zones. Create and configure one route table for each private subnet.**

The requirement is to allow EC2 instances to make outbound IPv4 requests to the internet while preventing inbound connections from the internet. This is the primary use case for a Network Address Translation (NAT) gateway. To ensure high availability and avoid cross-Availability Zone (AZ) data transfer charges, the best practice is to deploy a NAT gateway in a public subnet in each AZ that contains private subnets. Each private subnet should have its own route table configured to direct internet-bound traffic (0.0.0.0/0) to the NAT gateway within the same AZ. This design provides resilience, as an outage in one AZ's NAT gateway will not affect instances in the other AZ. Why Incorrect Options are Wrong: B: An internet gateway allows two-way communication with the internet, which violates the requirement to block inbound traffic. Also, an internet gateway is attached to a VPC, not deployed

</details>

### 41. q-90

A company hosts an application on Amazon EC2 instances that are part of a target group behind an Application Load Balancer (ALB). The company has attached a security group to the ALB. During a recent review of application logs, the company found many unauthorized login attempts from IP addresses that belong to countries outside the company's normal user base. The company wants to allow traffic only from the United States and Australia.

<details><summary>Answer</summary>

**B. Create a geographic match rule in AWS WAF. Attach the rule to the ALB.**

The most effective and scalable solution is to use AWS WAF (Web Application Firewall). AWS WAF is specifically designed to protect web applications by filtering and monitoring HTTP/S traffic. It includes a geographic match rule statement that allows you to control access based on the country of origin. By creating a rule to allow requests only from the United States and Australia and attaching this rule to the Application Load Balancer (ALB), the company can enforce this policy efficiently at the edge of its application. This approach is managed by AWS, eliminating the need for the company to maintain and update vast lists of IP addresses for different countries. Why Incorrect Options are Wrong: A. Network ACLs are not suitable for managing the vast, dynamic IP ranges of entire countries. They have rule limits that would be quickly exhausted, making this approach impractical and unmanage

</details>

### 42. q-104 `security`

A company is creating a low-latency payment processing application that supports TLS connections from IPv4 clients. The application requires outbound access to the public internet. Users must access the application from a single entry point. The bank wants to use Amazon Elastic Container Service (Amazon ECS) tasks to deploy the application. The company wants to enable AWSVPC network mode. Which solution will meet these requirements MOST securely?

<details><summary>Answer</summary>

**A. Create a VPC that has an internet gateway, public subnets, and private subnets. Deploy a Network Load Balancer and a NAT gateway in the public subnets. Deploy the ECS tasks in the private subnets.**

This solution provides the most secure and functional architecture. Placing the Amazon ECS tasks in private subnets is a security best practice, as it prevents them from being directly exposed to the internet. A Network Load Balancer (NLB) is ideal for low-latency, high-throughput TCP-based workloads like payment processing with TLS. It operates at the transport layer (Layer 4) and can handle millions of requests per second while maintaining ultra-low latencies. The NAT gateway, placed in a public subnet, enables the ECS tasks in the private subnets to initiate outbound connections to the public internet for necessary updates or API calls, without allowing inbound connections from the internet to the tasks. Why Incorrect Options are Wrong: B: An outbound-only internet gateway (Egress-Only Internet Gateway) is used for IPv6 traffic, not IPv4 as specified in the requirements. C: Deploying

</details>

### 43. q-120

A company has a multi-tier web application. The application's internal service components are deployed on Amazon EC2 instances. The internal service components need to access third-party software as a service (SaaS) APIs that are hosted on AWS. The company needs to provide secure and private connectivity from the application's internal services to the third-party SaaS application. The company needs to ensure that there is minimal public internet exposure. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use AWS PrivateLink to create a private connection between the application's VPC and the third- party SaaS provider.**

AWS PrivateLink is the purpose-built AWS service for creating secure, private connectivity between a VPC and services hosted on AWS, including third-party SaaS applications. It works by creating an interface VPC endpoint in the consumer's VPC, which acts as a private entry point to the service. This ensures that all traffic between the EC2 instances and the SaaS application remains on the AWS private network, never traversing the public internet. This directly meets the requirements for a secure, private connection with minimal public exposure. Why Incorrect Options are Wrong: A. AWS Site-to-Site VPN is primarily used to connect on-premises networks to a VPC. It is not the standard or most efficient solution for connecting to a SaaS service within AWS. B. AWS Transit Gateway is a network hub for interconnecting multiple VPCs and on-premises networks at scale. It simplifies network routin

</details>

### 44. dt-120

You have launched an Amazon Elastic Compute Cloud (EC2) instance into a public subnet with a primary private I P address assigned, an internet gateway is attached to the VPC, and the public route table is configured to send all Internet-based traffic to the Internet gateway. The instance security group is set to allow all outbound traffic but cannot access the internet. Why is the Internet unreachable from this instance?

<details><summary>Answer</summary>

**A. The instance does not have a public IP address.**

</details>

### 45. q-131

A company wants to deploy an internal web application on AWS. The web application must be accessible only from the company's office. The company needs to download security patches for the web application from the internet. The company has created a VPC and has configured an AWS Site- to-Site VPN connection to the company's office. A solutions architect must design a secure architecture for the web application. Which solution will meet these requirements? Options:

<details><summary>Answer</summary>

**B. Deploy the web application on Amazon EC2 instances in private subnets behind an internal Application Load Balancer (ALB). Deploy NAT gateways in public subnets. Attach an internet gateway to the VPC. Set the inbound source of the ALB's security group to the company's office network CIDR block.**

This solution provides a secure and functional architecture that meets all requirements. Placing the EC2 instances in private subnets prevents them from being directly accessible from the internet, which is crucial for an internal application. An internal Application Load Balancer (ALB) is used, which has a private IP address and is only accessible from within the VPC or from connected networks like the office via the Site-to-Site VPN. To allow the instances to download security patches, NAT gateways are deployed in public subnets. The private subnets' route tables are configured to direct internet-bound traffic (0.0.0.0/0) to the NAT gateways. Finally, the ALB's security group is configured with an inbound rule that allows traffic only from the company's office network CIDR block, enforcing the access restriction. Why Incorrect Options are Wrong: A. Deploying resources in public subnets

</details>

### 46. q-132

A company hosts a public application on AWS. The company uses an Application Load Balancer (ALB) to distribute application traffic to multiple Amazon EC2 instances that are hosted in private subnets. The company wants to authenticate all the requests by using an on-premises Active Directory Federation Service (AD FS). The company uses AWS Direct Connect to connect its on-premises data center to AWS. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Configure an Amazon Cognito user pool. Integrate the user pool with the ALB for AD FS authentication.**

The most effective solution is to use an Application Load Balancer (ALB) integrated with an Amazon Cognito user pool. The ALB can be configured to authenticate users before forwarding requests to the backend EC2 instances. Amazon Cognito user pools support federation with third-party identity providers (IdPs) using SAML 2.0, which includes Active Directory Federation Services (AD FS). In this architecture, the ALB redirects unauthenticated users to Cognito, which in turn federates with the on-premises AD FS for authentication. After successful authentication, Cognito provides tokens that the ALB validates to grant access. Why Incorrect Options are Wrong: B. Configure an AWS Directory Service directory. Integrate the directory with the ALB for AD FS authentication. ALBs do not natively integrate with AWS Directory Service for user authentication. The ALB's authentication feature is design

</details>

### 47. dt-133

In Amazon CloudFront, if you use Amazon EC2 instances and other custom origins with CloudFront, it is recommended to [...].

<details><summary>Answer</summary>

**D. specify the URL of the load balancer for the domain name of your origin server.**

</details>

### 48. dt-134

Which of the following statements is true regarding attaching network interfaces to your instances in your VPC?

<details><summary>Answer</summary>

**C. The number of ENIs you can attach varies by instance type.**

</details>

### 49. q-148

A solutions architect is designing the architecture for a two-tier web application. The web application consists of an internet-facing Application Load Balancer (ALB) that forwards traffic to an Auto Scaling group of Amazon EC2 instances. The EC2 instances must be able to access an Amazon RDS database. The company does not want to rely solely on security groups or network ACLs. Only the minimum resources that are necessary should be routable from the internet. Which network design meets these requirements?

<details><summary>Answer</summary>

**B. Place the ALB in public subnets. Place the EC2 instances and RDS database in private subnets.**

This architecture represents a standard and secure multi-tier design. An internet-facing Application Load Balancer (ALB) must be placed in public subnets (subnets with a route to an Internet Gateway) to be accessible from the internet. The EC2 instances, which form the application tier, do not need direct internet access; they only need to receive traffic from the ALB. Placing them in private subnets minimizes their exposure. Similarly, the RDS database, the data tier, should be isolated from the internet for maximum security and placed in private subnets, accessible only from the application tier (the EC2 instances). This design adheres to the principle of least privilege by exposing only the necessary component (the ALB) to the internet. Why Incorrect Options are Wrong: A. An internet-facing ALB cannot be placed in private subnets, as it would not be able to receive traffic directly fr

</details>

### 50. dt-152

A customer is running a multi-tier web application farm in a virtual private cloud (VPC) that is not connected to their corporate network. They are connecting to the VPC over the Internet to manage all of their Amazon EC2 instances running in both the public and private subnets. They have only authorized the bastion-security-group with Microsoft Remote Desktop Protocol (RDP) access to the application instance security groups, but the company wants to further limit administrative access to all of the instances in the VPC. Which of the following Bastion deployment scenarios will meet this requirement?

<details><summary>Answer</summary>

**C. Deploy a Windows Bastion host with an Elastic IP address in the private subnet, and restrict RDP access to the bastion from only the corporate public IP addresses.**

</details>

### 51. dt-158 `availability`

Your company hosts a social media site supporting users in multiple countries. You have been asked to provide a highly available design for the application that leverages multiple regions for the most recently accessed content and latency sensitive portions of the web site. The most latency sensitive component of the application involves reading user preferences to support web site personalization and ad selection. In addition to running your application in multiple regions, which option will support this application's requirements?

<details><summary>Answer</summary>

**A. Serve user content from S3. CloudFront and use Route 53 latency-based routing between ELBs in each region. Retrieve user preferences from a local DynamoDB table in each region and leverage SQS to capture changes to user preferences with SQS workers for propagating updates to each table.**

</details>

### 52. q-164

A company is designing an IPv6 application that is hosted on Amazon EC2 instances in a private subnet within a VPC. The application will store user-uploaded content in Amazon S3 buckets. The application will save each S3 object's URL link and metadata in Amazon DynamoDB. The company must not use public internet connections to transmit user-uploaded content or metadata. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Implement interface VPC endpoints for both Amazon S3 and Amazon DynamoDB.**

The core requirement is to establish private connectivity for an IPv6 application running on EC2 instances to both Amazon S3 and Amazon DynamoDB. VPC endpoints are the correct mechanism for this. However, there are two types: Gateway and Interface endpoints. Gateway VPC endpoints do not support IPv6 traffic; they are limited to IPv4 only. Since the application is designed for IPv6, using a gateway endpoint for either S3 or DynamoDB would fail to meet the requirements. Interface VPC endpoints, powered by AWS PrivateLink, support IPv6 traffic. By creating interface endpoints for both Amazon S3 and Amazon DynamoDB, the application can privately and securely communicate with both services over IPv6 without traversing the public internet. Why Incorrect Options are Wrong: A. The gateway VPC endpoint for S3 does not support the required IPv6 traffic, making this solution non-functional for the

</details>

### 53. q-165

A solutions architect is configuring a VPC that has public subnets and private subnets. The VPC and subnets use IPv4 CIDR blocks. There is one public subnet and one private subnet in each of three Availability Zones (AZs). An internet gateway is attached to the VPC. The private subnets require access to the internet to allow Amazon EC2 instances to download software updates. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Create a NAT gateway in one of the public subnets. Update the route tables that are attached to the private subnets to forward non-VPC traffic to the NAT gateway.**

To enable instances in a private subnet to initiate outbound internet connections while preventing inbound connections, a Network Address Translation (NAT) device is required. An AWS NAT gateway is a managed service that provides this functionality. The NAT gateway must be placed in a public subnet-a subnet with a route to an Internet Gateway-so it can forward traffic to the internet. The route tables associated with the private subnets must then be configured to direct internet-bound traffic (destination 0.0.0.0/0) to the NAT gateway. This architecture allows instances in the private subnets to access the internet for tasks like software updates. Why Incorrect Options are Wrong: B. A NAT device (NAT instance or gateway) must be placed in a public subnet to have a route to the internet; placing it in a private subnet will not work. C. An egress-only internet gateway is used exclusively f

</details>

### 54. dt-169

An edge location refers to which Amazon Web Service?

<details><summary>Answer</summary>

**C. An edge location is the location of the data center used for Amazon CloudFront.**

</details>

### 55. q-170

A company is planning to connect a remote office to its AWS infrastructure. The office requires permanent and secure connectivity to AWS. The connection must provide secure access to resources in two VPCs. However, the VPCs must not be able to access each other.

<details><summary>Answer</summary>

**B. Set up one AWS Site-to-Site VPN connection from the remote office to each of the VPCs. Update the VPC route tables with static routes to the remote office resources.**

This solution establishes two independent AWS Site-to-Site VPN connections, one from the remote office to each of the two VPCs. Each VPN connection terminates on a separate Virtual Private Gateway (VGW) attached to its respective VPC. This architecture directly meets all requirements: it provides permanent and secure connectivity to both VPCs. Crucially, because there is no network path established between the VPCs (such as VPC peering or a shared Transit Gateway), they remain completely isolated from each other, fulfilling the key constraint of the scenario. This is the most direct and cost-effective design for the stated goals. Why Incorrect Options are Wrong A: This is an overly complex and expensive solution. While it would work, using two separate Transit Gateways for only two VPCs is not a standard or cost-effective architecture. C: This option directly violates the requirement tha

</details>

### 56. q-171

A company has a VPC with multiple private subnets that host multiple applications. The applications must not be accessible to the internet. However, the applications need to access multiple AWS services. The applications must not use public IP addresses to access the AWS services.

<details><summary>Answer</summary>

**A. Configure interface VPC endpoints for the required AWS services. Route traffic from the private subnets through the interface VPC endpoints.**

Interface VPC endpoints, powered by AWS PrivateLink, provide private connectivity to AWS services. An interface endpoint creates an elastic network interface (ENI) with a private IP address from your subnet's IP address range. This ENI serves as an entry point for traffic destined for the supported AWS service. All traffic between your VPC and the service remains on the Amazon network, completely isolated from the public internet. This solution directly meets the requirements of accessing AWS services privately without using public IP addresses and without exposing the applications to the internet. Why Incorrect Options are Wrong: B. A NAT gateway allows instances in a private subnet to connect to the internet or AWS services, but the traffic traverses the public internet, violating the no-public-IP requirement. C. An Internet Gateway is attached to a VPC to enable communication with the

</details>

### 57. q-175 `security`

A company has deployed a multi-tier web application to support a website. The architecture includes an Application Load Balancer (ALB) in public subnets, two Amazon Elastic Container Service (Amazon ECS) tasks in the public subnets, and a PostgreSQL cluster that runs on Amazon EC2 instances in private subnets. The EC2 instances that host the PostgreSQL database run shell scripts that need to access an external API to retrieve product information. A solutions architect must design a solution to allow the EC2 instances to securely communicate with the external API without increasing operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure a NAT gateway in the public subnets. Update the route table for the private subnets to route traffic to the NAT gateway.**

The most secure and operationally efficient solution is to use a NAT gateway. EC2 instances in a private subnet, by design, cannot directly access the internet. A NAT gateway, placed in a public subnet, acts as an intermediary. The private subnet's route table is configured to send all internet-bound traffic (0.0.0.0/0) to the NAT gateway. The NAT gateway then translates the private IP addresses of the EC2 instances to its own public IP address and forwards the traffic to the external API. This allows the instances to initiate outbound connections while remaining completely private and inaccessible from the internet, fulfilling the security requirement. As a managed service, a NAT gateway handles scaling and availability automatically, minimizing operational overhead. Why Incorrect Options are Wrong: A. Assigning public IPs to database instances in a private subnet is a security risk and

</details>

### 58. q-182

A company wants to protect resources that the company hosts on AWS, including Application Load Balancers and Amazon CloudFront distributions. The company wants an AWS service that can provide near real-time visibility into attacks on the company's resources. The service must also have a dedicated AWS team to assist with DDoS attacks. Which AWS service will meet these requirements?

<details><summary>Answer</summary>

**D. AWS Shield Advanced**

AWS Shield Advanced is a managed DDoS protection service that provides enhanced safeguards for applications running on AWS. It offers near real-time visibility into attacks using Amazon CloudWatch metrics and detailed attack diagnostics. A key feature of Shield Advanced is 24x7 access to the AWS DDoS Response Team (DRT), who can assist in mitigating complex DDoS attacks. This service is specifically designed to protect resources like Application Load Balancers and CloudFront distributions, directly meeting all the specified requirements for advanced protection and expert assistance. Why Incorrect Options are Wrong: A. AWS WAF: Protects against common web exploits at the application layer (Layer 7) but does not include a dedicated DDoS response team for assistance during attacks. B. AWS Shield Standard: Provides baseline, automatic DDoS protection but lacks the advanced visibility, detail

</details>

### 59. dt-183

Which of the following statements are true about Amazon Route 53 resource records? (Choose 2 answers)

<details><summary>Answer</summary>

**A. An Alias record can map one DNS name to another Amazon Route 53 DNS name.; C. An Amazon Route 53 CNAME record can point to any DNS record hosted anywhere.**

</details>

### 60. q-184

A company runs an application on Amazon EC2 instances behind an Application Load Balancer (ALB). The company uses Amazon Route 53 to route traffic to the ALB. The ALB is a resource in an AWS Shield Advanced protection group. The company is preparing for a blue/green deployment in which traffic will shift to a new ALB. The company wants to protect against DDoS attacks during the deployment. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Add the new ALB to the Shield Advanced protection group. Select Sum as the aggregation type for the volume of traffic for the whole group.**

During a blue/green deployment, traffic is gradually shifted from the old environment (blue) to the new one (green). For a period, both environments, and thus both Application Load Balancers (ALBs), will be serving production traffic. To protect the entire application from a DDoS attack, AWS Shield Advanced must monitor the total traffic volume across both ALBs. By adding the new ALB to the existing protection group and setting the aggregation type to Sum, Shield Advanced will combine the traffic from both the old and new ALBs. This provides a holistic view of the application's traffic, allowing for accurate baselining and detection of DDoS attacks targeting the application as a whole, regardless of how traffic is distributed between the two ALBs during the transition. Why Incorrect Options are Wrong: B. Using Mean aggregation is incorrect. It would average the traffic, which would not a

</details>

### 61. q-185

A company runs multiple applications on Amazon EC2 instances in a VPC. Application A runs in a private subnet that has a custom route table and network ACL. Application B runs in a second private subnet in the same VPC. The company needs to prevent Application A from sending traffic to Application B. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Add a deny outbound rule to the custom network ACL for the Application A subnet. Configure the rule to prevent Application A from sending traffic to IP addresses that are associated with the Application B subnet.**

The requirement is to prevent traffic originating from Application A from reaching Application B. Network Access Control Lists (NACLs) are the appropriate tool for this scenario as they operate at the subnet level and support explicit deny rules. By adding an outbound deny rule to the NACL associated with Application A's subnet, with the destination being the CIDR block of Application B's subnet, all traffic from A to B is blocked before it leaves the source subnet. NACLs are stateless, so this single rule effectively prevents the communication as requested. Why Incorrect Options are Wrong: A. Security groups do not support explicit deny rules. Furthermore, an outbound rule on Application B's security group would not block inbound traffic. B. Security groups do not have explicit deny rules; they only support allow rules. Any traffic not matching an allow rule is implicitly denied. C. An

</details>

### 62. q-186 `security`

A company uses AWS Lambda functions in a private subnet in a VPC to run application logic. The Lambda functions must not have access to the public internet. Additionally, all data communication must remain within the private network. As part of a new requirement, the application logic needs access to an Amazon DynamoDB table. What is the MOST secure way to meet this new requirement?

<details><summary>Answer</summary>

**B. Create a gateway VPC endpoint for DynamoDB to provide access to the table.**

The most secure method to allow a Lambda function in a private subnet to access Amazon DynamoDB, while ensuring all traffic remains on the private AWS network, is to use a gateway VPC endpoint for DynamoDB. A gateway endpoint creates a private connection by adding a target for a specific route in the VPC's route table for traffic destined for DynamoDB. This ensures that requests from the Lambda function to the DynamoDB service are routed through the AWS private network and do not traverse the public internet, fulfilling the core security and networking requirements of the scenario. Why Incorrect Options are Wrong: A. Amazon DynamoDB is a regional AWS service that operates outside of any customer VPC. It is not possible to provision a DynamoDB table inside a VPC. C. A network ACL is a stateless firewall for subnets. It can permit or deny traffic but cannot create the private network path

</details>

### 63. dt-188

A major client who has been spending a lot of money on his internet service provider asks you to set up an AWS Direct Connection to try and save him some money. You know he needs high-speed connectivity. Which connection port speeds are available on AWS Direct Connect?

<details><summary>Answer</summary>

**B. 1Gbps and 10Gbps.**

</details>

### 64. dt-196

A user has configured ELB with two EBS backed EC2 instances. The user is trying to understand the DNS access and IP support for ELB. Which of the below mentioned statements may not help the user understand the IP mechanism supported by ELB?

<details><summary>Answer</summary>

**D. The ELB supports either IPV4 or IPV6 but not both.**

</details>

### 65. dt-198

You can use [...] to help secure the instances in your VPC.

<details><summary>Answer</summary>

**D. security groups and network ACLs.**

</details>

### 66. q-204

A company is designing a serverless application to process a large number of events within an AWS account. The application saves the events to a data warehouse for further analysis. The application sends incoming events to an Amazon SQS queue. Traffic between the application and the SQS queue must not use public IP addresses.

<details><summary>Answer</summary>

**A. Create a VPC endpoint for Amazon SQS. Set the queue policy to deny all access except from the VPC endpoint.**

The core requirement is to ensure traffic between an application in a VPC and an Amazon SQS queue does not traverse the public internet. The solution is to use an interface VPC endpoint for Amazon SQS. This creates an Elastic Network Interface (ENI) within your VPC, allowing resources to communicate with the SQS API endpoint using private IP addresses. All traffic remains securely on the AWS global network. To enforce this private-only access, an SQS queue policy can be configured to deny any requests that do not originate from the specified VPC endpoint, effectively blocking all public access. Why Incorrect Options are Wrong: B. Configure server-side encryption with SQS-managed keys (SSE-SQS). This encrypts data at rest within the queue. It does not address the requirement for private network connectivity (data in transit). C. Configure AWS Security Token Service (AWS STS) to generate t

</details>

### 67. dt-205

A user has configured a website and launched it using the Apache web server on port 80. The user is using ELB with the EC2 instances for Load Balancing. What should the user do to ensure that the EC2 instances accept requests only from ELB?

<details><summary>Answer</summary>

**A. Configure the security group of EC2, which allows access to the ELB source security group.**

</details>

### 68. dt-206

You're trying to delete an SSL certificate from the IAM certificate store, and you're getting the message 'Certificate: <certificate< span=''>-id> is being used by CloudFront.' Which of the following statements is probably the reason why you are getting this error?

<details><summary>Answer</summary>

**A. Before you can delete an SSL certificate, you need to either rotate SSL certificates or revert from using a custom SSL certificate to using the default CloudFront certificate.**

</details>

### 69. dt-207

A government client needs you to set up secure cryptographic key storage for some of their extremely confidential data. You decide that the AWS CloudHSM is the best service for this. However, there seem to be a few pre-requisites before this can happen, one of those being a security group that has certain ports open. Which of the following is correct in regards to those security groups?

<details><summary>Answer</summary>

**A. A security group that has port 22 (for SSH) or port 3389 (for RDP) open to your network.**

</details>

### 70. dt-208

A web company is looking to implement an intrusion detection and prevention system into their deployed VPC. This platform should have the ability to scale to thousands of instances running inside of the VPC. How should they architect their solution to achieve these goals?

<details><summary>Answer</summary>

**C. Configure servers running in the VPC using the host-based 'route' commands to send all traffic through the platform to a scalable virtualized IDS/IP.**

</details>

### 71. q-208

A company needs to move data from an Amazon EC2 instance to an Amazon S3 bucket. The company must ensure that no API calls and no data are routed through public internet routes. Only the EC2 instance can have access to upload data to the S3 bucket. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an interface VPC endpoint for Amazon S3 in the subnet where the EC2 instance is located. Attach a resource policy to the S3 bucket to only allow the EC2 instance's IAM role for access.**

An interface VPC endpoint for Amazon S3 is backed by AWS PrivateLink: it places an elastic network interface with a private IP in the chosen subnet, so the instance reaches S3 over the AWS network and neither the API calls nor the object data touch the public internet. The bucket policy is what limits who may upload, so restricting it to the EC2 instance's IAM role satisfies the "only the EC2 instance" requirement. The gateway-endpoint option is not just second best, it is not buildable as written, because a gateway endpoint is a route-table target rather than something you place in an Availability Zone, and it accepts no security group. The two remaining options try to discover a private IP for the S3 service endpoint and route to it by hand, which is not how S3 is reached.

</details>

### 72. q-210 `security`

A company operates multiple VPCs in a single AWS account. Account users need temporary access to Amazon S3 buckets. The S3 buckets are private and have no public endpoints. The solution must follow the principle of least privilege for access to each environment and must avoid distributing permanent access keys. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a gateway VPC endpoint for Amazon S3 in each VPC. Attach an endpoint policy that allows only environment-scoped IAM roles to access the S3 buckets.**

This solution correctly addresses all requirements. A gateway VPC endpoint for Amazon S3 establishes a private connection between the VPC and the S3 service, ensuring traffic does not traverse the public internet. Attaching an endpoint policy to the gateway endpoint allows for fine-grained access control, which can be used to enforce the principle of least privilege. By specifying environment-scoped IAM roles in the policy, only users who have assumed the appropriate role can access the designated S3 buckets through the endpoint. This use of IAM roles provides temporary credentials, satisfying the requirement to avoid distributing permanent access keys. Why Incorrect Options are Wrong: B: SSE-S3 is an encryption feature for data at rest and does not control network access. Using VPC CIDR blocks in bucket policies is not the recommended or most secure method for controlling access from a

</details>

### 73. q-213

A company is developing a new mobile app. The company must implement proper traffic filtering to protect its Application Load Balancer (ALB) against common application-level attacks, such as cross-site scripting or SQL injection. The company has minimal infrastructure and operational staff. The company needs to reduce its share of the responsibility in managing, updating, and securing servers for its AWS environment. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Configure AWS WAF rules and associate them with the ALB.**

AWS WAF (Web Application Firewall) is a service that helps protect web applications from common web exploits by allowing you to define customizable web security rules. It can be associated with an Application Load Balancer (ALB) to filter and block malicious traffic before it reaches the application. AWS WAF is a managed service, which means it reduces the operational burden on the company by handling the infrastructure, updates, and security configurations.

</details>

### 74. dt-217

What are the initial settings of an user created security group?

<details><summary>Answer</summary>

**C. Al low no inbound traffic and Al low all outbound traffic.**

</details>

### 75. q-217

A company runs a global web application on Amazon EC2 instances behind an Application Load Balancer. The application stores data in Amazon Aurora. The company needs to create a disaster recovery solution and can tolerate up to 30 minutes of downtime and potential data loss. The solution does not need to handle the load when the primary infrastructure is healthy. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application with the required infrastructure elements in place. Use Amazon Route 53 to configure active-passive failover. Create an Aurora Replica in a second AWS Region.**

</details>

### 76. q-218

A company wants to protect AWS-hosted resources, including Application Load Balancers and CloudFront distributions. They need near real-time visibility into attacks and a dedicated AWS response team for DDoS events. Which AWS service meets these requirements?

<details><summary>Answer</summary>

**D. AWS Shield Advanced**

AWS Shield Advanced is a managed Distributed Denial of Service (DDoS) protection service that provides enhanced safeguards for applications running on AWS. It specifically meets the requirements by offering near real-time visibility into attacks through advanced diagnostics and Amazon CloudWatch metrics. Crucially, Shield Advanced provides subscribers with 24x7 access to the AWS Shield Response Team (SRT). The SRT offers expert assistance in mitigating complex DDoS events, analyzing attacks, and applying custom mitigations, directly fulfilling the need for a dedicated response team. This service is designed to protect resources like Application Load Balancers and Amazon CloudFront distributions. Why Incorrect Options are Wrong: A. AWS WAF protects against common web exploits at the application layer (Layer 7) but does not inherently provide a dedicated DDoS response team. B. AWS Shield S

</details>

### 77. q-218

A company has a web server running on an Amazon EC2 instance in a public subnet with an Elastic IP address. The default security group is assigned to the EC2 instance. The default network ACL has been modified to block all traffic. A solutions architect needs to make the web server accessible from everywhere on port 443. Which combination of steps will accomplish this task? (Choose two.)

<details><summary>Answer</summary>

**A. Create a security group with a rule to allow TCP port 443 from source 0.0.0.0/0.**

E. Update the network ACL to allow inbound TCP port 443 from source 0.0.0.0/0 and outbound TCP port 32768-65535 to destination 0.0.0.0/0.

</details>

### 78. q-223

An insurance company is creating an application to record personal user data. The data includes users' names, ages, and health data. The company wants to run the application in a private subnet on AWS. Because of data security requirements, the company must have access to the operating system of the compute resources that run the application tier. The company must use a low-latency NoSQL database to store the data. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon EC2 instances for the application tier. Use an Amazon DynamoDB table for the database tier. Create a VPC endpoint for DynamoDB. Assign the instances an instance profile that has permission to access DynamoDB.**

This solution meets all the specified requirements. Amazon EC2 instances provide the necessary access to the underlying operating system. Amazon DynamoDB is a fully managed, serverless NoSQL database that delivers single-digit millisecond performance, satisfying the low-latency requirement. To ensure the application in the private subnet can communicate with DynamoDB without traversing the public internet, a VPC gateway endpoint for DynamoDB is the correct mechanism. Finally, assigning an IAM instance profile to the EC2 instances is the secure and standard method for granting permissions to access other AWS services like DynamoDB, without hardcoding credentials. Why Incorrect Options are Wrong: B. AWS Lambda is a serverless compute service and does not provide the required access to the underlying operating system. C. AWS Fargate is a serverless compute engine that abstracts the OS, and

</details>

### 79. dt-224

You are tasked with setting up a Linux bastion host for access to Amazon EC2 instances running in your VPC. Only clients connecting from the corporate external public IP address 72.34.51.100 should have SSH access to the host. Which option will meet the customer requirement?

<details><summary>Answer</summary>

**A. Security Group Inbound Rule: Protocol – TCP. Port Range – 22, Source 72.34.51.100/32**

</details>

### 80. q-231 `security`

An application runs on an Amazon EC2 instance that has an Elastic IP address in VPC A. The application requires access to a database in VPC B. Both VPCs are in the same AWS account. Which solution will provide the required access MOST securely?

<details><summary>Answer</summary>

**B. Configure a VPC peering connection between VPC A and VPC B.**

VPC peering allows direct connectivity between two VPCs. This solution enables communication between instances in VPC A and VPC B using private IP addresses. It does not require public IP addresses or the exposure of databases to the public internet.

</details>

### 81. q-233

A company is building a web application. The company needs a load balancing solution that supports HTTPS header-based routing. The company's security team also requires a rules-based method of blocking specific incoming requests to decrease the effects of malicious activity. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create an Application Load Balancer (ALB). Integrate the ALB with AWS WAF. Configure the security team's required rules.**

The solution requires two key capabilities: Layer 7 (application layer) routing and a web application firewall. An Application Load Balancer (ALB) operates at Layer 7 and supports advanced routing rules based on HTTP/S headers, paths, and methods, fulfilling the first requirement. AWS WAF is a web application firewall that integrates directly with an ALB to protect against common web exploits and allows the creation of custom, rules-based filters. By associating a WAF Web ACL with the ALB, the security team can define rules to block malicious requests based on IP addresses, HTTP headers, or request body content, meeting the second requirement. This combination provides a complete solution. Why Incorrect Options are Wrong: A. Mutual TLS (mTLS) on an ALB is for client authentication (verifying the client's identity via certificates), not for general, rules-based blocking of malicious web t

</details>

### 82. q-237

An application running on an Amazon EC2 instance in VPC-A needs to access files in another EC2 instance in VPC-B. Both VPCs are in separate AWS accounts. The network administrator needs to design a solution to configure secure access to EC2 instance in VPC-B from VPC-A. The connectivity should not have a single point of failure or bandwidth concerns. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Set up a VPC peering connection between VPC-A and VPC-B.**

A VPC peering connection allows secure communication between instances in different VPCs using private IP addresses without the need for internet gateways, VPN connections, or NAT devices. By setting it up, the application running in VPC-A can directly access the EC2 in VPC-B without going through the public internet or any single point of failure.

</details>

### 83. q-245

A company's application uses Network Load Balancers, Auto Scaling groups, Amazon EC2 instances, and databases that are deployed in an Amazon VPC. The company wants to capture information about traffic to and from the network interfaces in near real time in its Amazon VPC. The company wants to send the information to Amazon OpenSearch Service for analysis. Which solution will meet these requirements?

<details><summary>Answer</summary>

**Reduce the maximum number of EC2 instances in the development environment's Auto Scaling group.**

Development and production each have their own Auto Scaling group, and only production sees bursts of traffic. Capping the maximum size of the development group stops it from ever scaling out to a production-sized fleet, so development runs the minimum it needs and nothing more. Taking a target out of the development target group saves nothing, because the instance keeps running and billing - the Auto Scaling group still owns it and will simply register it again - and it also contradicts the requirement that the load balancer serve at least two instances. Shrinking instance sizes in both environments would change production as well, and the load balancing algorithm has no bearing on cost.

</details>

### 84. q-246

A company runs a web application on Amazon EC2 instances in multiple Availability Zones. The EC2 instances are in private subnets. A solutions architect implements an internet-facing Application Load Balancer (ALB) and specifies the EC2 instances as the target group. However, the internet traffic is not reaching the EC2 instances. How should the solutions architect reconfigure the architecture to resolve this issue?

<details><summary>Answer</summary>

**D. Create public subnets in each Availability Zone. Associate the public subnets with the ALB. Update the route tables for the public subnets with a route to the private subnets.**

This option involves creating public subnets for the ALB, allowing it to receive internet traffic. The EC2 instances can remain in private subnets. This approach follows the best practice of using public subnets for internet-facing components like ALBs.

</details>

### 85. dt-250

You have a load balancer configured for VPC, and all back-end Amazon EC2 instances are in service. However, your web browser times out when connecting to the load balancer's DNS name. Which options are probable causes of this behavior? (Choose 2 answers)

<details><summary>Answer</summary>

**A. The load balancer was not configured to use a public subnet with an Internet gateway configured.; C. The security groups or network ACLs are not properly configured for web traffic.**

</details>

### 86. q-251

An Amazon EC2 instance is located in a private subnet in a new VPC. This subnet does not have outbound internet access, but the EC2 instance needs the ability to download monthly security updates from an outside vendor. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create a NAT gateway, and place it in a public subnet. Configure the private subnet route table to use the NAT gateway as the default route.**

NAT gateways are designed to provide outbound internet access for instances in private subnets. Placing a NAT gateway in a public subnet and configuring the private subnet's route table to use the NAT gateway as the default route allows the EC2 instance to download security updates while maintaining security.

</details>

### 87. q-254 `security`

A company is reviewing a recent migration of a three-tier application to a VPC. The security team discovers that the principle of least privilege is not being applied to Amazon EC2 security group ingress and egress rules between the application tiers. What should a solutions architect do to correct this issue?

<details><summary>Answer</summary>

**B. Create security group rules using the security group ID as the source or destination.**

Using security group IDs allows for dynamic and flexible configuration. Referencing security groups directly in rules ensures that instances associated with those security groups, regardless of their individual IDs, are included. This approach aligns with the principle of least privilege and simplifies rule management.

</details>

### 88. q-255 `security`

A company is designing a web application on AWS. The application uses a VPN connection between the company's on-premises data center and the company's VPC. The company uses Amazon Route 53 as its DNS service. The application must use private DNS records to communicate with the on-premises services from a VPC. Which solution will meet these requirements MOST securely?

<details><summary>Answer</summary>

**A. Create a Route 53 Resolver outbound endpoint. Create a Resolver rule. Associate the Resolver rule with the VPC.**

To resolve DNS queries for on-premises domains from within a VPC, you must forward those queries to the on-premises DNS servers. This is achieved using Amazon Route 53 Resolver. The correct configuration involves creating a Resolver outbound endpoint in the VPC, which provides a path for queries to exit the VPC. Then, a Resolver forwarding rule is created to specify which domain names (e.g., the on-premises domain) should be forwarded to the IP addresses of the on-premises DNS servers. Finally, this rule is associated with the VPC. Why Incorrect Options are Wrong: B. A Route 53 Resolver inbound endpoint is used for the opposite traffic flow: resolving VPC DNS names from the on-premises network. C. A private hosted zone is for resolving DNS within AWS VPCs. It cannot be associated with an on-premises network to forward queries. D. A public hosted zone is for public internet DNS resolution

</details>

### 89. dt-256

You have been setting up an Amazon Virtual Private Cloud (Amazon VPC) for your company, including setting up subnets. Security is a concern, and you are not sure which is the best security practice for securing subnets in your VPC. Which statement below is correct in describing the protection of AWS resources in each subnet?

<details><summary>Answer</summary>

**A. You can use multiple layers of security, including security groups and network access control lists (ACL).**

</details>

### 90. q-258

A website runs on Amazon EC2 behind an ALB with Amazon CloudFront in front. The site is receiving a high rate of unwanted requests from specific IP addresses. How should the solutions architect address this problem?

<details><summary>Answer</summary>

**D. Use AWS WAF with a rate-based rule on the CloudFront distribution.**

The most effective and efficient way to mitigate a high rate of unwanted requests from specific IP addresses at the network edge is to use AWS WAF. By associating a WAF Web ACL with the Amazon CloudFront distribution, you can inspect and filter traffic before it reaches your origin (ALB and EC2 instances). A rate-based rule specifically tracks requests from individual IP addresses and can automatically block an IP if its request rate exceeds a defined threshold within a 5-minute period. This directly addresses the problem described, enhancing security and reducing load on the backend infrastructure. Why Incorrect Options are Wrong: A. AWS Shield is a managed DDoS protection service. While it works with WAF, AWS WAF is the service used to configure specific custom rules like rate-based blocking. B. Increasing Auto Scaling capacity would accommodate the unwanted traffic, not block it. This

</details>

### 91. dt-259

After deploying a new website for a client on AWS, he asks if you can set it up so that if it fails it can be automatically redirected to a backup website that he has stored on a dedicated server elsewhere. You are wondering whether Amazon Route 53 can do this. Which statement below is correct in regards to Amazon Route 53?

<details><summary>Answer</summary>

**B. Amazon Route 53 can help detect an outage of your website and redirect your end users to alternate locations.**

</details>

### 92. q-263

A company is creating a payment processing application that supports TLS connections from IPv4 clients. The application requires outbound access to the public internet. The application must allow users to access the application from a single entry point while maintaining the lowest possible attack surface. The company wants to use Amazon ECS tasks to deploy the application. The company wants to enable awsvpc network mode. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a VPC that has an internet gateway, public subnets, and private subnets. Deploy a Network Load Balancer (NLB) and a NAT gateway in the public subnets. Deploy the ECS tasks in the private subnets.**

This solution provides the most secure and functional architecture. Placing ECS tasks in private subnets minimizes the attack surface, as they are not directly accessible from the internet. A Network Load Balancer (NLB) in the public subnets provides a single, high-performance entry point for TLS traffic. A NAT gateway, also in a public subnet, is required to allow the tasks in the private subnets to initiate outbound connections to the public internet for dependencies like payment gateways, which is a stated requirement. This setup adheres to the principle of least privilege and security best practices. Why Incorrect Options are Wrong: B. An egress-only internet gateway is for IPv6 traffic only. The scenario specifies IPv4 clients and requires a NAT gateway for outbound IPv4 access. C. Deploying ECS tasks in public subnets exposes them directly to the internet, which unnecessarily incre

</details>

### 93. q-264

A company has a web application hosted over 10 Amazon EC2 instances with traffic directed by Amazon Route 53. The company occasionally experiences a timeout error when attempting to browse the application. The networking team finds that some DNS queries return IP addresses of unhealthy instances, resulting in the timeout error. What should a solutions architect implement to overcome these timeout errors?

<details><summary>Answer</summary>

**D. Create an Application Load Balancer (ALB) with a health check in front of the EC2 instances. Route to the ALB from Route 53.**

By creating an ALB and configuring health checks, the architect ensures that only healthy instances receive traffic. The ALB periodically checks the health of the EC2 instances based on the configured health check settings.  Routing traffic to the ALB from Route 53 ensures that DNS queries return the IP address of the ALB instead of individual instances. This allows the ALB to distribute traffic only to healthy instances, avoiding timeouts caused by unhealthy instances.

</details>

### 94. q-265 `availability` `security`

A solutions architect needs to design a highly available application consisting of web, application, and database tiers. HTTPS content delivery should be as close to the edge as possible, with the least delivery time. Which solution meets these requirements and is MOST secure?

<details><summary>Answer</summary>

**C. Configure a public Application Load Balancer (ALB) with multiple redundant Amazon EC2 instances in private subnets. Configure Amazon CloudFront to deliver HTTPS content using the public ALB as the origin.**

CloudFront terminates HTTPS at edge locations close to users, which is what the "as close to the edge as possible, least delivery time" requirement asks for, and it needs an origin it can reach, so the ALB has to be internet-facing. Putting the EC2 instances in private subnets behind that ALB is where the security comes from: the instances have no public IPs and no inbound path from the internet, and only the load balancer's security group can reach them. Spreading the ALB and the instances across multiple Availability Zones gives the high availability the question asks for. The options that place the instances in public subnets expose them directly, and the options that use the EC2 instances as the CloudFront origin lose the load balancer, so a single instance becomes the entry point.

</details>

### 95. dt-266

Your company has an on-premises multi-tier PHP web application, which recently experienced downtime due to a large burst in web traffic due to a company announcement. Over the coming days, you are expecting similar announcements to drive similar unpredictable bursts, and are looking to find ways to quickly improve your infrastructure's ability to handle unexpected increases in traffic. The application currently consists of 2 tiers: a web tier which consists of a load balancer and several Linux Apache web servers, as well as a database tier which hosts a Linux server hosting a MySQL database. Which scenario below will provide full site functionality, while helping to improve the ability of your application in the short timeframe required?

<details><summary>Answer</summary>

**C. Offload traffic from on-premises environment: Setup a CloudFront distribution, and configure CloudFront to cache objects from a custom origin. Choose to customize your object cache behavior, and select a TTL that objects should exist in cache.**

</details>

### 96. q-272

A company hosts an application on Amazon EC2 instances behind an Application Load Balancer ALB. The company wants the application to be accessible only from inside the VPC that hosts the ALB. The company creates an alias record of example.com in Amazon Route 53. The DNS record for the application must be resolvable only in the VPC where the application runs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use an internal ALB. Create a Route 53 private hosted zone for the application DNS name.**

To meet the requirements, both network access and DNS resolution must be restricted to the VPC. An internal Application Load Balancer (ALB) has a private IP address and is only accessible from within its VPC, satisfying the network access requirement. An Amazon Route 53 private hosted zone allows you to manage DNS for a domain within one or more VPCs. DNS queries for records in a private hosted zone are only resolved by clients within the associated VPCs. Combining an internal ALB with a private hosted zone ensures the application is both accessible and resolvable exclusively from inside the VPC. Why Incorrect Options are Wrong: A. An internet-facing ALB and a public hosted zone make the application and its DNS record publicly accessible, violating both requirements. B. An internal ALB restricts network access, but a public hosted zone makes the DNS record publicly resolvable, violating

</details>

### 97. q-272

A company serves a dynamic website from a fleet of Amazon EC2 instances behind an Application Load Balancer (ALB). The website needs to support multiple languages to serve customers around the world. The website’s architecture is running in the us-west-1 Region and is exhibiting high request latency for users that are located in other parts of the world. The website needs to serve requests quickly and efficiently regardless of a user’s location. However, the company does not want to recreate the existing architecture across multiple Regions. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Configure an Amazon CloudFront distribution with the ALB as the origin. Set the cache behavior settings to cache based on the Accept- Language request header.**

</details>

### 98. q-282

A company runs a web application that is deployed on Amazon EC2 instances in the private subnet of a VPC. An Application Load Balancer (ALB) that extends across the public subnets directs web traffic to the EC2 instances. The company wants to implement new security measures to restrict inbound traffic from the ALB to the EC2 instances while preventing access from any other source inside or outside the private subnet of the EC2 instances. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure the security group for the EC2 instances to only allow traffic that comes from the security group for the ALB.**

Security groups act as virtual firewalls for EC2 instances. By configuring the security group for the EC2 instances to only allow traffic from the security group associated with the ALB, you can control and restrict inbound traffic effectively.  When you specify a security group as the source in the inbound rules of another security group, you allow traffic only from instances that are members of that source security group. In this case, you can allow traffic only from the ALB, ensuring that traffic is restricted to the necessary source.

</details>

### 99. dt-288

Your company has multiple IT departments, each with their own VPC. Some VPCs are located within the same AWS account, and others in a different AWS account. You want to peer together all VPCs to enable the IT departments to have full access to each others' resources. There are certain limitations placed on VPC peering. Which of the following statements is incorrect in relation to VPC peering?

<details><summary>Answer</summary>

**B. You can have up to 3 VPC peering connections between the same two VPCs at the same time.**

</details>

### 100. dt-290

A/An [...] acts as a firewall that controls the traffic allowed to reach one or more instances.

<details><summary>Answer</summary>

**A. security group.**

</details>

### 101. dt-292

You need to create a management network using network interfaces for a virtual private cloud (VPC) network. Which of the following statements is incorrect pertaining to Best Practices for ConfiguringNetwork Interfaces.

<details><summary>Answer</summary>

**D. Attaching another network interface to an instance is a valid method to increase or double the network bandwidth to or from the dual-homed instance.**

</details>

### 102. q-294

An application that is hosted on Amazon EC2 instances needs to access an Amazon S3 bucket. Traffic must not traverse the internet. How should a solutions architect configure access to meet these requirements?

<details><summary>Answer</summary>

**B. Set up a gateway VPC endpoint for Amazon S3 in the VPC.**

A VPC endpoint for Amazon S3 allows you to connect your VPC directly to S3 without traversing the internet. This ensures that traffic between your EC2 instances and the S3 bucket stays within the AWS network.

</details>

### 103. q-296

A development team has launched a new application that is hosted on Amazon EC2 instances inside a development VPC. A solutions architect needs to create a new VPC in the same account. The new VPC will be peered with the development VPC. The VPC CIDR block for the development VPC is 192.168.0.0/24. The solutions architect needs to create a CIDR block for the new VPC. The CIDR block must be valid for a VPC peering connection to the development VPC. What is the SMALLEST CIDR block that meets these requirements?

<details><summary>Answer</summary>

**D. 10.0.1.0/24**

This is a valid CIDR block that does not overlap with the existing development VPC (192.168.0.0/24).  Therefore, this is the SMALLEST CIDR block that meets the requirements.

</details>

### 104. dt-297

Your manager has asked you to set up a public subnet with instances that can send and receive internet traffic, and a private subnet that can't receive traffic directly from the internet, but can initiate traffic to the internet (and receive responses) through a NAT instance in the public subnet. Hence, the following 3 rules need to be allowed: Inbound SSH traffic. Web servers in the public subnet to read and write to MS SQL servers in the private subnet. Inbound RDP traffic from the Microsoft Terminal Services gateway in the public private subnet. What are the respective ports that need to be opened for this?

<details><summary>Answer</summary>

**A. Ports 22, 1433, 3389.**

</details>

### 105. dt-298

An EC2 instance is connected to an ENI (Elastic Network Interface) in one subnet. What happens to the data on an instance if the instance reboots (intentionally or unintentionally)?

<details><summary>Answer</summary>

**B. Data persists.**

</details>

### 106. dt-301

An EC2 instance is connected to an ENI (Elastic Network Interface) in one subnet. What happens when you attach an ENI of a different subnet to this EC2 instance?

<details><summary>Answer</summary>

**B. The EC2 instance follows the rules of both the subnets.**

</details>

### 107. dt-302

You have deployed a three-tier web application in a VPC with a CIDR block of 10.0.0.0/28. You initially deploy two web servers, two application servers, two database servers and one NAT instance for a total of seven EC2 instances. The web, application and database servers are deployed across two Availability Zones (AZs). You also deploy an ELB in front of the two web servers, and use Route 53 for DNS. Web traffic gradually increases in the first few days following the deployment, so you attempt to double the number of instances in each tier of the application to handle the new load. Unfortunately some of these new instances fail to launch. Which of the following could be the root cause? (Choose 2 answers)

<details><summary>Answer</summary>

**C. The ELB has scaled-up, adding more instances to handle the traffic spike, reducing the number of available private IP addresses for new instance launches.; E. AWS reserves the first four and the last IP address in each subnet's CIDR block so you do not have enough addresses left to launch all of the new EC2 instances.**

</details>

### 108. dt-305

You are tasked with moving a legacy application from a virtual machine running Inside your datacenter to an Amazon VPC Unfortunately this app requires access to a number of on-premises services and no one who configured the app still works for your company. Even worse there's no documentation for it. What will allow the application running inside the VPC to reach back and access its internal dependencies without being reconfigured? (Choose 3 answers)

<details><summary>Answer</summary>

**A. An AWS Direct Connect link between the VPC and the network housing the internal services.; D. An IP address space that does not conflict with the one on-premises.; F. A VM Import of the current virtual machine.**

</details>

### 109. q-310

A company that recently started using AWS establishes an AWS Site-to-Site VPN connection between its on-premises data center and AWS. The company's security mandate states that traffic originating from on premises must stay within the company's private IP address space when communicating with an Amazon ECS cluster that hosts a sample web application. Which solution meets this requirement?

<details><summary>Answer</summary>

**B. Create a Network Load Balancer and an AWS PrivateLink endpoint service in the same VPC that hosts the ECS cluster.**

The core requirement is to provide private connectivity from an on-premises network to an Amazon ECS service, ensuring traffic does not traverse the public internet. AWS PrivateLink is the service designed for this purpose. The correct architecture involves placing the ECS service tasks behind a Network Load Balancer (NLB). Then, an endpoint service is created and configured to point to this NLB. This endpoint service can then be accessed from the on-premises network through the Site-to-Site VPN connection via an interface VPC endpoint. This entire communication path remains within the private network, fulfilling the security mandate. Why Incorrect Options are Wrong: A. Gateway endpoints are only supported for Amazon S3 and DynamoDB, not for Amazon ECS. This option proposes an invalid configuration. C. This architecture is unnecessarily complex and misaligned. AWS PrivateLink is designed

</details>

### 110. q-313 `least-ops`

A solutions architect is creating an AWS Lambda function that needs network access to private resources in a VPC. Which solution will provide this access with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Attach the Lambda function to the VPC through private subnets. Create a security group that allows network access to the private resources. Associate the security group with the Lambda function.**

The standard and most direct method for an AWS Lambda function to access resources within a VPC is to configure it to connect to that VPC. When configured, Lambda creates an Elastic Network Interface (ENI) within the specified private subnets. A security group is then associated with this ENI to control its network traffic. This security group's rules can explicitly allow the Lambda function to communicate with other private resources (like an RDS database) within the VPC. This approach is a native Lambda feature, requiring minimal configuration directly on the function, thereby representing the least operational overhead. Why Incorrect Options are Wrong: B: A VPN connection is designed to connect a VPC to an external network (e.g., on-premises data center), not for a Lambda function to access resources within the same VPC. This adds unnecessary complexity. C: A VPC endpoint is used for

</details>

### 111. dt-313

A company has an AWS account that contains three VPCs (Dev, Test, and Prod) in the same region. Test is peered to both Prod and Dev. All VPCs have non-overlapping CIDR blocks. The company wants to push minor code releases from Dev to Prod to speed up time to market. Which of the following options helps the company accomplish this?

<details><summary>Answer</summary>

**D. The VPCs have non-overlapping Cl DR blocks in the same account. The route tables contain local routes for all VPCs.**

</details>

### 112. q-313

A company is building a mobile app on AWS. The company wants to expand its reach to millions of users. The company needs to build a platform so that authorized users can watch the company’s content on their mobile devices. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon CloudFront. Provide signed URLs to stream content.**

Amazon CloudFront: CloudFront is a content delivery network (CDN) service provided by AWS. It accelerates the delivery of content by caching it at edge locations globally, reducing latency for end-users. Signed URLs: CloudFront supports the generation of signed URLs, which can be used to control access to content. You can create time-limited URLs with specific permissions, allowing only authorized users to access the content.

</details>

### 113. dt-316

You have set up an Elastic Load Balancer (ELB) with the usual default settings, which route each request independently to the application instance with the smallest load. However, someone has asked you to bind a user's session to a specific application instance so as to ensure that all requests coming from the user during the session will be sent to the same application instance. AWS has a feature to do this. What is it called?

<details><summary>Answer</summary>

**D. Sticky session.**

</details>

### 114. dt-333

Can you specify the security group that you created for a VPC when you launch an instance in EC2-Classic?

<details><summary>Answer</summary>

**C. No.**

</details>

### 115. dt-334

Which two methods increases the fault tolerance of the connection to VPC-1? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Establish a hardware VPN over the internet between VPC-1 and the on-premises network.; E. Establish a new AWS Direct Connect connection and private virtual interface in the same AWS region as VPC-1.**

</details>

### 116. dt-340

A US-based company is expanding their web presence into Europe. The company wants to extend their AWS infrastructure from Northern Virginia (us-east-1) into the Dublin (eu-west-1) region. Which of the following options would enable an equivalent experience for users on both continents?

<details><summary>Answer</summary>

**D. Use Amazon Route 53, and apply a weighted routing policy to distribute traffic across both regions.**

</details>

### 117. dt-350

True or False: When you add a rule to a DB security group, you do not need to specify port number or protocol.

<details><summary>Answer</summary>

**B. True.**

</details>

### 118. q-357 `availability`

A gaming company is moving its public scoreboard from a data center to the AWS Cloud. The company uses Amazon EC2 Windows Server instances behind an Application Load Balancer to host its dynamic application. The company needs a highly available storage solution for the application. The application consists of static files and dynamic server-side code. Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Store the static files on Amazon S3. Use Amazon CloudFront to cache objects at the edge.**

D. Store the server-side code on Amazon FSx for Windows File Server. Mount the FSx for Windows File Server volume on each EC2 instance to share the files.  Amazon S3 is a highly scalable and durable object storage service, and it is well-suited for storing static files. Using CloudFront as a content delivery network (CDN) improves the delivery of static content by caching objects at edge locations, reducing latency for end users.  Amazon FSx for Windows File Server provides a fully managed Windows file system that is accessible from Windows-based EC2 instances. This is suitable for storing dynamic server-side code that requires file sharing across multiple instances. It offers high availability and supports Windows-native features.

</details>

### 119. dt-358

Your company previously configured a heavily used, dynamically routed VPN connection between your on-premises data center and AWS. You recently provisioned a DirectConnect connection and would like to start using the new connection. After configuring DirectConnect settings in the AWS Console, which of the following options will provide the most seamless transition for your users?

<details><summary>Answer</summary>

**D. Configure your DirectConnect router. Update your VPC route tables to point to the DirectConnect connection. Configure your VPN connection with a higher BGP priority and verify network traffic is leveraging the DirectConnect connection.**

</details>

### 120. q-358 `least-ops`

A social media company runs its application on Amazon EC2 instances behind an Application Load Balancer (ALB). The ALB is the origin for an Amazon CloudFront distribution. The application has more than a billion images stored in an Amazon S3 bucket and processes thousands of images each second. The company wants to resize the images dynamically and serve appropriate formats to clients. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Use a Lambda@Edge function with an external image management library. Associate the Lambda@Edge function with the CloudFront behaviors that serve the images.**

Lambda@Edge: Allows you to run code in response to CloudFront events without provisioning or managing servers. In this case, a Lambda@Edge function can be used to dynamically resize images based on the request.  External image management library: Since the company wants to minimize operational overhead, using an external image management library within a Lambda@Edge function is a good choice. This eliminates the need to manage EC2 instances or other infrastructure.

</details>

### 121. q-360

A company uses Amazon API Gateway to run a private gateway with two REST APIs in the same VPC. The BuyStock RESTful web service calls the CheckFunds RESTful web service to ensure that enough funds are available before a stock can be purchased. The company has noticed in the VPC flow logs that the BuyStock RESTful web service calls the CheckFunds RESTful web service over the internet instead of through the VPC. A solutions architect must implement a solution so that the APIs communicate through the VPC. Which solution will meet these requirements with the FEWEST changes to the code?

<details><summary>Answer</summary>

**B. Use an interface endpoint.**

Interface Endpoint (VPC Endpoint for API Gateway): An interface endpoint allows private connectivity to API Gateway within your VPC. By creating a VPC endpoint for API Gateway, you can ensure that the communication between the BuyStock and CheckFunds RESTful web services stays within the VPC, eliminating the need for traffic to go over the internet.

</details>

### 122. q-362

A company has a three-tier web application. An Application Load Balancer (ALB) is in front of Amazon EC2 instances that are in the ALB target group. An Amazon S3 bucket stores documents. The company requires the application to meet a recovery time objective (RTO) of 60 seconds. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Replicate S3 objects to a second AWS Region. Create a second ALB and a minimum set of EC2 instances in the second Region. Ensure that the EC2 instances in the second Region are running. Configure Amazon Route 53 to fail over to the secondary Region based on health checks.**

To meet a stringent Recovery Time Objective (RTO) of 60 seconds, a Warm Standby disaster recovery strategy is required. This approach involves maintaining a scaled-down but fully functional version of the application in a secondary AWS Region. Option D correctly describes this strategy. By keeping a minimum set of EC2 instances running behind an Application Load Balancer and replicating S3 data, the environment is ready to handle traffic. Using Amazon Route 53 with health checks provides an automated and rapid failover mechanism. When the primary region's health checks fail, Route 53 automatically reroutes traffic to the healthy secondary region, a process that can complete well within the 60-second RTO. Why Incorrect Options are Wrong: A. Starting shut-down EC2 instances (a Pilot Light strategy) takes several minutes, which would violate the 60-second RTO. IP-based routing is not for he

</details>

### 123. q-365

A company runs a web application in a single AWS Region. A solutions architect wants to ensure that the web application can continue to operate if the application becomes unavailable in the Region. Which solution will meet this requirement?

<details><summary>Answer</summary>

**A. Deploy the application in multiple Regions. Use Amazon Route 53 DNS health checks to route traffic to a healthy Region.**

The core requirement is to ensure the application remains operational even if an entire AWS Region becomes unavailable. This necessitates a multi-Region disaster recovery (DR) strategy. Deploying the application across multiple Regions provides the necessary infrastructure redundancy. Amazon Route 53, configured with a failover routing policy and associated health checks, can monitor the health of the application endpoints in each Region. If the health checks detect that the primary Region is down, Route 53 will automatically stop sending traffic to it and reroute all traffic to the healthy secondary Region, thus meeting the requirement. Why Incorrect Options are Wrong: B. Deploying in multiple Availability Zones protects against failures within a single Region but does not provide resilience against a complete regional outage. C. An Amazon Route 53 simple routing policy does not support

</details>

### 124. dt-365

You are designing an SSUTLS solution that requires HTTPS clients to be authenticated by the Web server using client certificate authentication. The solution must be resilient. Which of the following options would you consider for configuring the web server infrastructure? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Configure ELB with TCP listeners on TCP/4d3. And place the Web servers behind it.; B. Configure your Web servers with EIPS Place the Web servers in a Route 53 Record Set and configure health checks against all Web servers.**

</details>

### 125. gh-366

367] A company is using Amazon Route 53 latency-based routing to route requests to its UDP-based application for users around the world. The application is hosted on redundant servers in the company's on-premises data centers in the United States, Asia, and Europe. The company’s compliance requirements state that the application must be hosted on premises. The company wants to improve the performance and availability of the application.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Configure three Network Load Balancers (NLBs) in the three AWS Regions to address the on-premises endpoints. Create an accelerator by using AWS Global Accelerator, and register the NLBs as its endpoints. Provide access to the application by using a CNAME that points to the accelerator DNS.**

A Network Load Balancer supports UDP listeners and accepts IP addresses as targets, so each Regional NLB can point at the redundant on-premises servers across Direct Connect or a VPN. The application therefore stays hosted on premises, which is what the compliance rule requires, while AWS Global Accelerator puts anycast static IPs at the edge so user traffic enters the AWS backbone close to the user and is carried to the nearest healthy on-premises site. Global Accelerator also health checks each endpoint and reroutes in seconds, which improves availability over the Route 53 latency records the company uses today, because those depend on client DNS caches expiring. The Application Load Balancer and Classic Load Balancer options cannot carry UDP, and the CloudFront option cannot either.

</details>

### 126. q-369

A company needs to run its external website on Amazon EC2 instances and on-premises virtualized servers. The AWS environment has a 1 GB AWS Direct Connect connection to the data center. The application has IP addresses that will not change. The on-premises and AWS servers are able to restart themselves while maintaining the same IP address if a failure occurs. Some website users have to add their vendors to an allow list, so the solution must have a fixed IP address. The company needs a solution with the lowest operational overhead to handle this split traffic. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy a Network Load Balancer on AWS. Create target groups for the on-premises and AWS addresses.**

The solution must load balance traffic to a hybrid environment (AWS and on-premises) and provide a fixed public IP address for client allow lists. A Network Load Balancer (NLB) is the ideal service for this scenario. NLB operates at Layer 4 and is designed for high performance. It supports registering IP addresses as targets, which allows it to route traffic to on-premises servers over an AWS Direct Connect connection. Critically, an internet-facing NLB can be assigned a static Elastic IP address for each Availability Zone, fulfilling the requirement for a fixed IP. This provides a managed, low-overhead solution that meets all the specified needs. Why Incorrect Options are Wrong: An Application Load Balancer (ALB) does not have a static IP address; its IPs are dynamic, which violates a core requirement for user allow lists. Amazon Route 53 Resolver is a recursive DNS service for resolvin

</details>

### 127. q-370

A company runs a public three-tier web application in a VPC. The application runs on Amazon EC2 instances across multiple Availability Zones. The EC2 instances that run in private subnets need to communicate with a license server over the internet. The company needs a managed solution that minimizes operational maintenance. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Provision a NAT gateway in a public subnet. Modify each private subnet's route table with a default route that points to the NAT gateway.**

NAT Gateway: A NAT gateway is a managed service provided by AWS that allows EC2 instances in private subnets to initiate outbound traffic to the internet while preventing unsolicited inbound traffic from reaching those instances. NAT gateways are fully managed, highly available, and require minimal maintenance.  Public Subnet: Placing the NAT gateway in a public subnet allows it to have access to the internet, fulfilling the requirement for private instances to communicate with a license server over the internet.  Default Route: Modifying each private subnet's route table with a default route that points to the NAT gateway ensures that traffic from private instances is directed through the NAT gateway for outbound communication.

</details>

### 128. q-374

A company is running several business applications in three separate VPCs within the us-east-1 Region. The applications must be able to communicate between VPCs. The applications also must be able to consistently send hundreds of gigabytes of data each day to a latency- sensitive application that runs in a single on-premises data center. A solutions architect needs to design a network connectivity solution that maximizes cost-effectiveness. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Set up one AWS Direct Connect connection from the data center to AWS. Create a transit gateway, and attach each VPC to the transit gateway. Establish connectivity between the Direct Connect connection and the transit gateway.**

AWS Direct Connect: Using a single AWS Direct Connect connection from the data center to AWS is more cost-effective than setting up multiple connections. It provides a dedicated and consistent network connection between the on-premises data center and AWS.  Transit Gateway: The use of a transit gateway simplifies network connectivity. It acts as a hub, allowing communication between the VPCs and the on-premises data center without requiring separate connections for each VPC. This reduces complexity and costs associated with managing multiple connections.

</details>

### 129. dt-375

You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) so you decide to use the VPC wizard in the AWS console to help make it easier for you. Which of the following statements is correct regarding instances that you launch into a default subnet via the VPC wizard?

<details><summary>Answer</summary>

**B. Instances that you launch into a default subnet receive both a public IP address and a private IP address.**

</details>

### 130. dt-379

What does Amazon ELB stand for?

<details><summary>Answer</summary>

**D. Elastic Load Balancing.**

</details>

### 131. q-383

A solutions architect is designing a multi-Region disaster recovery (DR) strategy for a company. The company runs an application on Amazon EC2 instances in Auto Scaling groups that are behind an Application Load Balancer (ALB). The company hosts the application in the company's primary and secondary AWS Regions. The application must respond to DNS queries from the secondary Region if the primary Region fails. Only one Region must serve traffic at a time. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create primary and secondary DNS records in Amazon Route 53. Configure health checks and a failover routing policy.**

The scenario requires an active-passive disaster recovery (DR) strategy where traffic is automatically redirected from a failed primary AWS Region to a secondary Region. Amazon Route 53's failover routing policy is designed specifically for this use case. By creating primary and secondary alias records pointing to the Application Load Balancers in each Region and associating them with a Route 53 health check, Route 53 can monitor the health of the primary endpoint. If the health check fails, Route 53 will automatically stop responding to DNS queries with the primary record and start responding with the secondary record, effectively failing over traffic to the DR Region. Why Incorrect Options are Wrong: A. Route 53 Resolver endpoints are for resolving DNS queries between VPCs and on-premises networks (hybrid DNS), not for managing public-facing, multi-Region application failover. C. Geolo

</details>

### 132. q-385

A solutions architect is creating a new VPC design. There are two public subnets for the load balancer, two private subnets for web servers, and two private subnets for MySQL. The web servers use only HTTPS. The solutions architect has already created a security group for the load balancer allowing port 443 from 0.0.0.0/0. Company policy requires that each resource has the least access required to still be able to perform its tasks. Which additional configuration strategy should the solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**C. Create a security group for the web servers and allow port 443 from the load balancer. Create a security group for the MySQL servers and allow port 3306 from the web servers security group.**

</details>

### 133. q-395

An IAM user made several configuration changes to AWS resources in their company's account during a production deployment last week. A solutions architect learned that a couple of security group rules are not configured as desired. The solutions architect wants to confirm which IAM user was responsible for making changes. Which service should the solutions architect use to find the desired information?

<details><summary>Answer</summary>

**C. AWS CloudTrail**

AWS CloudTrail is a service provided by Amazon Web Services (AWS) that allows you to monitor and log AWS account activity. It records API calls made on your AWS account, capturing information such as the identity of the caller, the time of the API call, the source IP address, the request parameters, and the response elements returned by the AWS service.

</details>

### 134. q-396

A company has implemented a self-managed DNS service on AWS. The solution consists of the following: • Amazon EC2 instances in different AWS Regions • Endpoints of a standard accelerator in AWS Global Accelerator The company wants to protect the solution against DDoS attacks. What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Subscribe to AWS Shield Advanced. Add the accelerator as a resource to protect.**

AWS Shield Advanced is a managed Distributed Denial of Service (DDoS) protection service provided by AWS. By subscribing to AWS Shield Advanced, you gain access to enhanced DDoS protection capabilities, including automatic detection and mitigation of DDoS attacks.

</details>

### 135. q-397 `availability`

A company runs an application on Amazon EC2 instances. The application is deployed in private subnets in three Availability Zones of the us-east-1 Region. The instances must be able to connect to the internet to download files. The company wants a design that is highly available across the Region. Which solution should be implemented to ensure that there are no disruptions to internet connectivity?

<details><summary>Answer</summary>

**B. Deploy a NAT gateway in a public subnet of each Availability Zone.**

Instances in private subnets do not have public IP addresses and cannot access the internet directly. To enable outbound internet connectivity, a Network Address Translation (NAT) device is required. An AWS NAT gateway is a managed, highly available service designed for this purpose. For regional high availability, the best practice is to deploy a NAT gateway in a public subnet within each Availability Zone (AZ). The route tables for the private subnets in each AZ are then configured to route internet-bound traffic (0.0.0.0/0) to the NAT gateway in their respective AZ. This design ensures that an outage in one AZ does not affect the internet connectivity of instances in the other AZs. Why Incorrect Options are Wrong: A. A NAT instance is a self-managed EC2 instance, which can be a single point of failure. It must also be placed in a public, not private, subnet. C. An AWS Transit Gateway

</details>

### 136. dt-398

You've been brought in as solutions architect to assist an enterprise customer with their migration of an e-commerce platform to Amazon Virtual Private Cloud (VPC) The previous architect has already deployed a 3-tier VPC, The configuration is as follows. VPC: vpc-2f8bc447. IGW: igw-2d8bc445. NACL: ad-208bc448. 5ubnets and Route Tables: Web servers: subnet-258bc44d. Application servers: subnet-248bc44c. Database servers: subnet-9189c6f9. Route Tables: rrb-218bc449, rtb-238bc44b. Associations: subnet-258bc44d: rtb-218bc449, subnet-248bc44c: rtb-238bc44b, subnet-9189c6f9: rtb-238bc44b. You are now ready to begin deploying EC2 instances into the VPC Web servers must have direct access to the internet Application and database servers cannot have direct access to the internet. Which configuration below will allow you the ability to remotely administer your application and database servers, as well as allow these servers to retrieve updates from the Internet?

<details><summary>Answer</summary>

**A. Create a bastion and NAT instance in subnet-258bc44d, and add a route from rtb- 238bc44b to the NAT instance.**

</details>

### 137. q-399

A finance company hosts a data lake in Amazon S3. The company receives financial data records over SFTP each night from several third parties. The company runs its own SFTP server on an Amazon EC2 instance in a public subnet of a VPC. After the files are uploaded, they are moved to the data lake by a cron job that runs on the same instance. The SFTP server is reachable on DNS sftp.example.com through the use of Amazon Route 53. What should a solutions architect do to improve the reliability and scalability of the SFTP solution?

<details><summary>Answer</summary>

**B. Migrate the SFTP server to AWS Transfer for SFTP. Update the DNS record sftp.example.com in Route 53 to point to the server endpoint hostname.**

The most effective way to improve the reliability and scalability of the SFTP solution is to migrate to AWS Transfer Family. This is a fully managed AWS service designed for file transfers (including SFTP) directly into and out of Amazon S3. As a managed service, it is inherently highly available and automatically scales to meet demand, eliminating the single point of failure and performance bottlenecks of a single EC2 instance. It also simplifies the architecture by removing the need for the cron job, as files are natively written to the S3 bucket, reducing operational overhead and potential points of failure. Why Incorrect Options are Wrong: A. An Application Load Balancer (ALB) operates at the application layer (Layer 7) and does not support the SFTP protocol, which runs over TCP at Layer 4. C. AWS Storage Gateway's File Gateway provides file-based access to S3 using NFS and SMB proto

</details>

### 138. dt-406

What does Amazon Route 53 provide?

<details><summary>Answer</summary>

**C. A scalable Domain Name System.**

</details>

### 139. q-408

A solutions architect is designing a system to be highly resilient. The system uses Amazon Route 53 with health checks and an Application Load Balancer (ALB). The system is critical and must have the highest availability possible.

<details><summary>Answer</summary>

**B. Configure the Route 53 health checks to perform a failover automatically.**

Amazon Route 53 health checks are a fundamental component for building resilient architectures. They monitor the health of specified resources, such as an Application Load Balancer (ALB) endpoint. To achieve high availability, you configure a Route 53 routing policy, such as the "Failover" policy. This policy is associated with the health check. When the health check determines that the primary endpoint is unhealthy, Route 53 automatically stops routing traffic to it and redirects traffic to a pre-configured secondary (standby) resource. This process provides seamless, automatic failover at the DNS level, which is essential for critical systems requiring the highest possible availability. Why Incorrect Options are Wrong: A. This describes the result of a failover configuration, not the configuration action itself. The setup of health checks and a failover policy is what causes the automa

</details>

### 140. q-408

A company runs an application that receives data from thousands of geographically dispersed remote devices that use UDP. The application processes the data immediately and sends a message back to the device if necessary. No data is stored. The company needs a solution that minimizes latency for the data transmission from the devices. The solution also must provide rapid failover to another AWS Region. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Global Accelerator. Create a Network Load Balancer (NLB) in each of the two Regions as an endpoint. Create an Amazon Elastic Container Service (Amazon ECS) cluster with the Fargate launch type. Create an ECS service on the cluster. Set the ECS service as the target for the NLProcess the data in Amazon ECS.**

AWS Global Accelerator: AWS Global Accelerator provides static IP addresses that act as a fixed entry point to your application. It routes traffic over the AWS global network to the optimal AWS endpoint based on health, geography, and routing policies.  Network Load Balancer (NLB): NLB is well-suited for UDP-based traffic, and it's designed for high-performance, low-latency applications. In this case, it can efficiently handle the thousands of geographically dispersed remote devices sending UDP traffic.  Amazon ECS with Fargate Launch Type: Using ECS with Fargate allows you to deploy and run containers without managing the underlying infrastructure. This setup can efficiently handle the immediate processing of data without the need to manage the underlying servers.

</details>

### 141. q-412

The DNS provider that hosts a company's domain name records is experiencing outages that cause service disruption for a website running on AWS. The company needs to migrate to a more resilient managed DNS service and wants the service to run on AWS. What should a solutions architect do to rapidly migrate the DNS hosting service?

<details><summary>Answer</summary>

**A. Create an Amazon Route 53 public hosted zone for the domain name. Import the zone file containing the domain records hosted by the previous provider.**

To rapidly migrate an existing public domain's DNS hosting to AWS, the correct service is Amazon Route 53. The first step is to create a public hosted zone for the domain, as this allows Route 53 to respond to DNS queries for the domain on the public internet. To expedite the migration of existing DNS records, the most efficient method is to obtain a zone file (a standard text file format for DNS records) from the current provider and import it directly into the newly created Route 53 public hosted zone. This avoids the time-consuming and error-prone process of manually recreating each record. Why Incorrect Options are Wrong: B: A private hosted zone is used for resolving domain names within a VPC and is not accessible from the public internet, making it unsuitable for a public website. C: AWS Directory Service is for managing Microsoft Active Directory in the cloud. Its DNS functionalit

</details>

### 142. dt-415

You have just set up your first Elastic Load Balancer (ELB) but it does not seem to be configured properly. You discover that before you start using ELB, you have to configure the listeners for your load balancer. Which protocols does ELB use to support the load balancing of applications?

<details><summary>Answer</summary>

**C. HTTP, HTTPS, TCP, and SSL.**

</details>

### 143. dt-417

A user has created a subnet in VPC and launched an EC2 instance within it. The user has not selected the option to assign the IP address while launching the instance. The user has 3 elastic IPs and is trying to assign one of the Elastic IPs to the VPC instance from the console. The console does not show any instance in the IP assignment screen. What is a possible reason that the instance is unavailable in the assigned IP console?

<details><summary>Answer</summary>

**D. The IP addresses belong to EC2 Classic; so they cannot be assigned to VPC.**

</details>

### 144. dt-427

You need to set up security for your VPC and you know that Amazon VPC provides two features that you can use to increase security for your VPC: security groups and network access control lists (ACLs). You have already looked into security groups and you are now trying to understand ACLs. Which statement below is incorrect in relation to ACLs?

<details><summary>Answer</summary>

**B. Is stateful: Return traffic is automatically allowed, regardless of any rules.**

</details>

### 145. q-434

A company runs an internet-facing web application on AWS and uses Amazon Route 53 with a public hosted zone. The company wants to log DNS response codes to support future root cause analysis. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Route 53 to configure query logging.**

Amazon Route 53 query logging records the DNS queries that Route 53 receives for a specified public hosted zone. This log data is sent to Amazon CloudWatch Logs and includes information such as the domain queried, the time of the query, the query type (e.g., A, AAAA), and the DNS response code (e.g., NOERROR, NXDOMAIN). This detailed information is essential for performing root cause analysis on DNS resolution issues and for security auditing. Configuring query logging is the direct and intended method to meet the requirement. Why Incorrect Options are Wrong: B. AWS CloudTrail logs API calls made to the Route 53 service (management events), not the actual DNS queries processed by it. C. Amazon CloudWatch metrics for Route 53 provide aggregated data on query volume but lack the granular detail of individual queries and response codes. D. AWS Trusted Advisor provides recommendations on cos

</details>

### 146. dt-437

You must assign each server to at least [...] security group.

<details><summary>Answer</summary>

**D. 1.**

</details>

### 147. q-439 `least-ops`

A solutions architect configured a VPC that has a small range of IP addresses. The number of Amazon EC2 instances that are in the VPC is increasing, and there is an insufficient number of IP addresses for future workloads. Which solution resolves this issue with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Add an additional IPv4 CIDR block to increase the number of IP addresses and create additional subnets in the VPC. Create new resources in the new subnets by using the new CIDR.**

By adding an additional IPv4 CIDR block to the existing VPC, you can effectively increase the number of available IP addresses within the same VPC. Creating additional subnets using the new CIDR block allows you to organize your resources and maintain segmentation within the VPC.

</details>

### 148. dt-443

A customer is hosting their company website on a cluster of web servers that are behind a public facing load balancer. The customer also uses Amazon Route 53 to manage their public DNS. How should the customer configure the DNS zone apex record to point to the load balancer?

<details><summary>Answer</summary>

**C. Create a CNAME record aliased to the load balancer DNS name.**

</details>

### 149. q-444

A company hosts an Amazon EC2 instance in a private subnet in a new VPC. The VPC also has a public subnet that has the default route set to an internet gateway. The private subnet does not have outbound internet access. The EC2 instance needs to have the ability to download monthly security updates from an outside vendor. However, the company must block any connections that are initiated from the internet. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a NAT gateway in the public subnet. Configure the private subnet route table to use the NAT gateway as the default route.**

To meet the requirements, the EC2 instance in the private subnet needs a way to initiate outbound connections to the internet without being reachable from the internet. A NAT (Network Address Translation) gateway is the correct AWS managed service for this purpose. The NAT gateway must be deployed in a public subnet so it can route traffic to the internet gateway. The route table associated with the private subnet must then be configured with a default route (0.0.0.0/0) that points to the NAT gateway. This configuration allows instances in the private subnet to send outbound traffic through the NAT gateway, while the NAT gateway itself blocks any unsolicited inbound connections from the internet. Why Incorrect Options are Wrong: A. Configuring the private subnet's route table to use the internet gateway directly would make it a public subnet, allowing inbound connections from the interne

</details>

### 150. q-448

A company has two VPCs named Management and Production. The Management VPC uses VPNs through a customer gateway to connect to a single device in the data center. The Production VPC uses a virtual private gateway with two attached AWS Direct Connect connections. The Management and Production VPCs both use a single VPC peering connection to allow communication between the applications. What should a solutions architect do to mitigate any single point of failure in this architecture?

<details><summary>Answer</summary>

**C. Add a second set of VPNs to the Management VPC from a second customer gateway device.**

Adding a second set of VPN connections from the Management VPC to a second customer gateway device provides redundancy and eliminates this single point of failure.

</details>

### 151. q-450

A company has a three-tier web application that is in a single server. The company wants to migrate the application to the AWS Cloud. The company also wants the application to align with the AWS Well-Architected Framework and to be consistent with AWS recommended best practices for security, scalability, and resiliency. Which combination of solutions will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**C. Create a VPC across two Availability Zones. Refactor the application to host the web tier, application tier, and database tier. Host each tier on its own private subnet with Auto Scaling groups for the web tier and application tier.**

This choice aligns with best practices by using separate subnets for each tier, allowing for better security and scalability. Auto Scaling groups provide elasticity and resiliency.  E. Use Elastic Load Balancers in front of the web tier. Control access by using security groups containing references to each layer's security groups.  This option introduces an Elastic Load Balancer (ELB) for the web tier, which enhances scalability and resiliency. Using security groups to control access adds an additional layer of security.  F. Use an Amazon RDS database Multi-AZ cluster deployment in private subnets. Allow database access only from application tier security groups.  This option leverages Amazon RDS for the database tier, utilizing Multi-AZ for high availability. Placing the RDS database in private subnets and restricting access to the application tier security groups enhances security.

</details>

### 152. dt-452

A customer has established an AWS Direct Connect connection to AWS. The link is up and routes are being advertised from the customer's end, however the customer is unable to connect from EC2 instances inside its VPC to servers residing in its datacenter. Which of the following options provide a viable solution to remedy this situation? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Enable route propagation to the virtual pinnate gateway (VGW).; E. Modify the Instances VPC subnet route table by adding a route back to the customer's on-premises environment.**

</details>

### 153. dt-453

While creating a network in the VPC, which of the following is true of a NAT device?

<details><summary>Answer</summary>

**B. You can choose to use any of the three kinds of NAT devices offered by AWS for special purposes.**

</details>

### 154. dt-454

Which of the following statements is NOT true about using Elastic IP Address (EIP) in EC2-Classic and EC2-VPC platforms?

<details><summary>Answer</summary>

**A. In the EC2-VPC platform, the Elastic IP Address (EIP) does not remain associated with the instance when you stop it.**

</details>

### 155. dt-457

You are in the process of moving your friend's WordPress site onto AWS to try and save him some money, and you have told him that he should probably also move his domain name. He asks why he can't leave his domain name where it is and just have his infrastructure on AWS. What would be an incorrect response to his question?

<details><summary>Answer</summary>

**D. Route 53 supports Domain Name System Security Extensions (DNSSEC).**

</details>

### 156. dt-460

You have an environment that consists of a public subnet using Amazon VPC and 3 instances that are running in this subnet. These three instances can successfully communicate with other hosts on the Internet. You launch a fourth instance in the same subnet, using the same AMI and security group configuration you used for the others, but find that this instance cannot be accessed from the internet. What should you do to enable Internet access?

<details><summary>Answer</summary>

**B. Assign an Elastic IP address to the fourth instance.**

</details>

### 157. dt-465

Doug has created a VPC with CIDR 10.201.0.0/16 in his AWS account. In this VPC he has created a public subnet with CIDR block 10.201.31.0/24. While launching a new EC2 from the console, he is not able to assign the private IP address 10.201.31.6 to this instance. Which is the most likely reason for this issue?

<details><summary>Answer</summary>

**B. Private address IP 10.201.31.6 is currently assigned to another interface.**

</details>

### 158. q-471

A company is creating an application that runs on containers in a VPC. The application stores and accesses data in an Amazon S3 bucket. During the development phase, the application will store and access 1 TB of data in Amazon S3 each day. The company wants to minimize costs and wants to prevent traffic from traversing the internet whenever possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a gateway VPC endpoint for Amazon S3. Associate this endpoint with all route tables in the VPC**

</details>

### 159. q-473

A company hosts a website on Amazon EC2 instances behind an Application Load Balancer (ALB). The website serves static content. Website traffic is increasing, and the company is concerned about a potential increase in cost.

<details><summary>Answer</summary>

**A. Create an Amazon CloudFront distribution to cache state files at edge locations**

By creating a CloudFront distribution and configuring it to cache static files, you can offload the delivery of static content to the CDN, reducing the load on the ALB and potentially lowering data transfer costs. CloudFront helps improve website performance and can be cost-effective due to its caching mechanism.

</details>

### 160. q-474

A company has multiple VPCs across AWS Regions to support and run workloads that are isolated from workloads in other Regions. Because of a recent application launch requirement, the company’s VPCs must communicate with all other VPCs across all Regions. Which solution will meet these requirements with the LEAST amount of administrative effort?

<details><summary>Answer</summary>

**C. Use AWS Transit Gateway to manage VPC communication in a single Region and Transit Gateway peering across Regions to manage VPC communications.**

AWS Transit Gateway is designed for simplifying the connectivity between multiple VPCs and on-premises networks. It allows for hub-and-spoke connectivity patterns, making it easier to manage communication across multiple VPCs. By using AWS Transit Gateway in a single Region to connect VPCs and enabling Transit Gateway peering across Regions, you can efficiently manage communication between VPCs in different Regions with centralized control and minimal administrative effort.

</details>

### 161. dt-476

After launching an instance that you intend to serve as a NAT (Network Address Translation) device in a public subnet you modify your route tables to have the NAT device be the target of internet bound traffic of your private subnet. When you try and make an outbound connection to the internet from an instance in the private subnet, you are not successful. Which of the following steps could resolve the issue?

<details><summary>Answer</summary>

**A. Disabling the Source/Destination Check attribute on the NAT instance.**

</details>

### 162. q-480

A business application is hosted on Amazon EC2 and uses Amazon S3 for encrypted object storage. The chief information security officer has directed that no application traffic between the two services should traverse the public internet. Which capability should the solutions architect use to meet the compliance requirements?

<details><summary>Answer</summary>

**B. VPC endpoint**

AWS provides VPC endpoints that allow you to privately connect your VPC to supported AWS services, including Amazon S3, without needing to use public IP addresses or traverse the public internet. With an S3 VPC endpoint, the traffic between your Amazon EC2 instances and Amazon S3 remains within the AWS network, providing a secure and private connection.

</details>

### 163. dt-481

How many Elastic IP by default in Amazon Account?

<details><summary>Answer</summary>

**D. 0 Elastic IP.**

</details>

### 164. dt-484

You are designing a connectivity solution between on-premises infrastructure and Amazon VPC. Your servers on-premises will be communicating with your VPC instances. You will be establishing IPSec tunnels over the internet. You will be using VPN gateways and terminating the IPsec tunnels on AWS supported customer gateways. Which of the following objectives would you achieve by implementing an IPSec tunnel as outlined above? (Choose 4 answers)

<details><summary>Answer</summary>

**C. Data encryption across the Internet.; D. Protection of data in transit over the Internet.; E. Peer identity authentication between VPN gateway and customer gateway.; F. Data integrity protection across the Internet.**

</details>

### 165. q-487 `availability`

A company seeks a storage solution for its application. The solution must be highly available and scalable. The solution also must function as a file system be mountable by multiple Linux instances in AWS and on premises through native protocols, and have no minimum size requirements. The company has set up a Site-to-Site VPN for access from its on-premises network to its VPC. Which storage solution meets these requirements?

<details><summary>Answer</summary>

**C. Amazon Elastic File System (Amazon EFS) with multiple mount targets**

Amazon EFS is a scalable file storage service that can be mounted by multiple Amazon EC2 instances and on-premises servers. It provides a shared file system with multiple mount targets in different Availability Zones (AZs) for high availability. Multiple mount targets allow you to mount the file system from different subnets, ensuring that instances in different network segments can access the file system.

</details>

### 166. q-493

A news company that has reporters all over the world is hosting its broadcast system on AWS. The reporters send live broadcasts to the broadcast system. The reporters use software on their phones to send live streams through the Real Time Messaging Protocol (RTMP). A solutions architect must design a solution that gives the reporters the ability to send the highest quality streams The solution must provide accelerated TCP connections back to the broadcast system. What should the solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**B. AWS Global Accelerator**

AWS Global Accelerator is a networking service designed to improve the availability and performance of applications for global users. It leverages the AWS global network to route user traffic to the optimal application endpoint, minimizing latency, jitter, and packet loss. By providing static anycast IP addresses as a fixed entry point, it directs the reporters' RTMP traffic over the AWS backbone network instead of the public internet. This directly provides the "accelerated TCP connections" required to send the highest quality, stable live streams from various international locations. Why Incorrect Options are Wrong: A. Amazon CloudFront is a Content Delivery Network (CDN) optimized for accelerating the delivery of cached content to viewers, not for accelerating TCP-based uploads from clients to an origin. C. AWS Client VPN is a service for providing secure, encrypted access to AWS reso

</details>

### 167. q-499

An online gaming company hosts its platform on Amazon EC2 instances behind Network Load Balancers (NLBs) across multiple AWS Regions. The NLBs can route requests to targets overthe internet. The company wants to improve the customer playing experience by reducing end-to-end load time for its global customer base. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Create a standard accelerator in AWS Global Accelerator. Configure the existing NLBs as target endpoints.**

AWS Global Accelerator is a networking service designed to improve the availability and performance of applications for global users. It provides static IP addresses that act as a fixed entry point to your application endpoints, such as Network Load Balancers, in one or more AWS Regions. Global Accelerator uses the AWS global network to route user traffic to the optimal endpoint based on performance, client location, and health checks. This minimizes latency and jitter by routing traffic over the congested public internet for only a short distance to the nearest AWS edge location, and then over the highly reliable AWS backbone network. This directly addresses the requirement to reduce end-to-end load time for a global customer base. Why Incorrect Options are Wrong: A. Replacing NLBs with ALBs changes the load balancer type (Layer 4 to Layer 7) but does not solve the core problem of optim

</details>

### 168. q-499

A company needs to minimize the cost of its 1 Gbps AWS Direct Connect connection. The company's average connection utilization is less than 10%. A solutions architect must recommend a solution that will reduce the cost without compromising security. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Contact an AWS Direct Connect Partner to order a 200 Mbps hosted connection for an existing AWS account.**

</details>

### 169. q-501

A company is implementing a new application on AWS. The company will run the application on multiple Amazon EC2 instances across multiple Availability Zones within multiple AWS Regions. The application will be available through the internet. Users will access the application from around the world. The company wants to ensure that each user who accesses the application is sent to the EC2 instances that are closest to the user's location. Which solution will meet these requirements?

<details><summary>Answer</summary>

**Use Amazon Data Firehose (formerly Amazon Kinesis Data Firehose) to ingest the data. Use Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics) to analyze the data in real time.**

Amazon Data Firehose is a fully managed delivery stream that buffers incoming records and writes them to Amazon S3 with no servers, shards or scaling to manage, which is what makes it the most operationally efficient way to land payment data in the data lake. Amazon Managed Service for Apache Flink reads the same stream and runs continuous queries over it, giving real-time analysis alongside delivery to S3. The alternatives - scheduled batch jobs, or custom consumers running on EC2 or in Lambda - add code and operational work for the same result.

</details>

### 170. dt-503

Does Amazon Route 53 support NS Records?

<details><summary>Answer</summary>

**D. Yes, it supports Name Server records.**

</details>

### 171. q-504

A company needs to connect several VPCs in the us-east-1 Region that span hundreds of AWS accounts. The company's networking team has its own AWS account to manage the cloud network. What is the MOST operationally efficient solution to connect the VPCs?

<details><summary>Answer</summary>

**C. Create an AWS Transit Gateway in the networking team’s AWS account. Configure static routes from each VPC.**

AWS Transit Gateway: It is designed to simplify the connectivity between multiple VPCs. It acts as a central hub that allows you to connect multiple VPCs and on-premises networks. This approach reduces the complexity of managing peering connections individually.

</details>

### 172. q-506

A company is building a new furniture inventory application. The company has deployed the application on a fleet of Amazon EC2 instances across multiple Availability Zones. The EC2 instances run behind an Application Load Balancer (ALB) in their VPC. A solutions architect has observed that incoming traffic seems to favor one EC2 instance, resulting in latency for some requests. What should the solutions architect do to resolve this issue?

<details><summary>Answer</summary>

**A. Disable session affinity (sticky sessions) on the ALB.**

The scenario describes traffic being unevenly distributed to a specific EC2 instance behind an Application Load Balancer (ALB), causing latency. This is a characteristic symptom of session affinity, also known as "sticky sessions." When sticky sessions are enabled on a target group, the ALB binds a user's session to a specific target instance. This ensures all requests from that user during the session are sent to the same instance. If a particular user or a few users generate a high volume of requests, the instance they are "stuck" to can become overloaded, while other instances remain underutilized. Disabling this feature allows the ALB to use its default round-robin algorithm to distribute requests evenly across all healthy instances, resolving the imbalance and associated latency. Why Incorrect Options are Wrong: B. Replacing the ALB with a Network Load Balancer is a significant arch

</details>

### 173. dt-507

Which of the following are characteristics of Amazon VPC subnets? (Choose 2 answers)

<details><summary>Answer</summary>

**B. Each subnet maps to a single Availability Zone.; E. Instances in a private subnet can communicate with the Internet only if they have an Elastic IP.**

</details>

### 174. dt-509

You are designing a data leak prevention solution for your VPC environment. You want your VPC Instances to be able to access software depots and distributions on the Internet for product updates. The depots and distributions are accessible via third party CONs by their URLs. You want to explicitly deny any other outbound connections from your VPC instances to hosts on the internet. Which of the following options would you consider?

<details><summary>Answer</summary>

**A. Configure a web proxy server in your VPC and enforce URL-based ru les for outbound access Remove default routes.**

</details>

### 175. q-509

A company operates a two-tier application for image processing. The application uses two Availability Zones, each with one public subnet and one private subnet. An Application Load Balancer (ALB) for the web tier uses the public subnets. Amazon EC2 instances for the application tier use the private subnets. Users report that the application is running more slowly than expected. A security audit of the web server log files shows that the application is receiving millions of illegitimate requests from a small number of IP addresses. A solutions architect needs to resolve the immediate performance problem while the company investigates a more permanent solution. What should the solutions architect recommend to meet this requirement?

<details><summary>Answer</summary>

**B. Modify the network ACL for the web tier subnets. Add an inbound deny rule for the IP addresses that are consuming resources.**

</details>

### 176. q-510 `security`

A global marketing company has applications that run in the ap-southeast-2 Region and the eu-west-1 Region. Applications that run in a VPC in eu- west-1 need to communicate securely with databases that run in a VPC in ap-southeast-2. Which network design will meet these requirements?

<details><summary>Answer</summary>

**C. Configure a VPC peering connection between the ap-southeast-2 VPC and the eu-west-1 VPUpdate the subnet route tables. Create an inbound rule in the ap-southeast-2 database security group that allows traffic from the eu-west-1 application server IP addresses.**

VPC peering connections can be established between VPCs in different AWS Regions. In this case, a VPC peering connection is set up between the VPC in ap-southeast-2 and the VPC in eu-west-1.

</details>

### 177. dt-513

You would like to create a mirror image of your production environment in another region for disaster recovery purposes. Which of the following AWS resources do not need to be recreated in the second region? (Choose 2 answers)

<details><summary>Answer</summary>

**A. Route 53 Record Sets.; B. IAM Roles.**

</details>

### 178. q-514

A company is running a microservices application on Amazon EC2 instances. The company wants to migrate the application to an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for scalability. The company must configure the Amazon EKS control plane with endpoint private access set to true and endpoint public access set to false to maintain security compliance. The company must also put the data plane in private subnets. However, the company has received error notifications because the node cannot join the cluster. Which solution will allow the node to join the cluster?

<details><summary>Answer</summary>

**B. Create interface VPC endpoints to allow nodes to access the control plane.**

When the Amazon EKS control plane has private access, nodes need to communicate with the control plane through interface VPC endpoints. Creating interface VPC endpoints ensures that the nodes in private subnets can securely communicate with the EKS control plane without the need for public IP addresses.

</details>

### 179. dt-519

You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) network so you decide you should probably use the AWS Management Console and the VPC Wizard. Which of the following is not an option for network architectures after launching the 'Start VPC Wizard' in Amazon VPC page on the AWS Management Console?

<details><summary>Answer</summary>

**B. VPC with a Public Subnet Only and Hardware VPN Access.**

</details>

### 180. q-520

A finance company is migrating its trading platform to AWS. The trading platform processes a high volume of market data and processes stock trades. The company needs to establish a consistent, low- latency network connection from its on-premises data center to AWS. The company will host resources in a VPC. The solution must not use the public internet. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Direct Connect to set up a connection from the on-premises data center to AWS**

The scenario requires a consistent, low-latency network connection that does not use the public internet. AWS Direct Connect is the only service listed that meets all these requirements. It establishes a dedicated, private physical network connection between an on-premises data center and AWS. This bypasses the internet, resulting in more consistent network performance and lower latency compared to internet-based connections, which is critical for a high-volume financial trading platform. Why Incorrect Options are Wrong: A. AWS Client VPN is designed for connecting individual end-users (clients) to AWS or on-premises networks, not for a persistent, high-performance data center connection. C. AWS PrivateLink provides private connectivity from a VPC to specific AWS services or VPC endpoint services, not a general network connection from an on-premises data center. D. AWS Site-to-Site VPN e

</details>

### 181. dt-520

True or False: A VPC contains multiple subnets, where each subnet can span multiple Availability Zones.

<details><summary>Answer</summary>

**B. This is true.**

</details>

### 182. dt-527

When will you incur costs with an Elastic IP address (EIP)?

<details><summary>Answer</summary>

**D. Costs are incurred regardless of whether the ElP is associated with a running instance.**

</details>

### 183. q-530

A company has an online gaming application that has TCP and UDP multiplayer gaming capabilities. The company uses Amazon Route 53 to point the application traffic to multiple Network Load Balancers (NLBs) in different AWS Regions. The company needs to improve application performance and decrease latency for the online game in preparation for user growth. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Add AWS Global Accelerator in front of the NLBs. Configure a Global Accelerator endpoint to use the correct listener ports.**

AWS Global Accelerator is a service that uses anycast IP addresses to route traffic over the AWS global network to optimal endpoints based on health, geography, and routing policies.

</details>

### 184. dt-532

Does Route 53 support MX Records?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 185. q-532

A company has a workload in an AWS Region. Customers connect to and access the workload by using an Amazon API Gateway REST API. The company uses Amazon Route 53 as its DNS provider. The company wants to provide individual and secure URLs for all customers. Which combination of steps will meet these requirements with the MOST operational efficiency? (Choose three.)

<details><summary>Answer</summary>

**A. Register the required domain in a registrar. Create a wildcard custom domain name in a Route 53 hosted zone and record in the zone that points to the API Gateway endpoint.**

D. Request a wildcard certificate that matches the custom domain name in AWS Certificate Manager (ACM) in the same Region.  F. Create a custom domain name in API Gateway for the REST API. Import the certificate from AWS Certificate Manager (ACM).  Registering the domain in a registrar and creating a wildcard custom domain name in Route 53 allows you to manage the DNS records efficiently. The DNS records can point to the API Gateway endpoint.  ACM provides a simple way to request and manage SSL/TLS certificates. Requesting a wildcard certificate for the custom domain ensures that it covers all subdomains, allowing for individual and secure URLs.  API Gateway allows you to create a custom domain name and associate it with your REST API. By importing a wildcard certificate from AWS Certificate Manager (ACM), you can secure the custom domain.

</details>

### 186. q-538

A global video streaming company uses Amazon CloudFront as a content distribution network (CDN). The company wants to roll out content in a phased manner across multiple countries. The company needs to ensure that viewers who are outside the countries to which the company rolls out content are not able to view the content. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Add geographic restrictions to the content in CloudFront by using an allow list. Set up a custom error message.**

CloudFront allows you to set up geographic restrictions by creating an allow list. This allows you to specify the countries from which viewers are allowed to access your content. Viewers from countries not in the allow list will be restricted from accessing the content.

</details>

### 187. q-544

A retail company uses a regional Amazon API Gateway API for its public REST APIs. The API Gateway endpoint is a custom domain name that points to an Amazon Route 53 alias record. A solutions architect needs to create a solution that has minimal effects on customers and minimal data loss to release the new version of APIs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a canary release deployment stage for API Gateway. Deploy the latest API version. Point an appropriate percentage of traffic to the canary stage. After API verification, promote the canary stage to the production stage.**

A canary release deployment is a strategy in software development and release management where a new version of a software application or service is gradually rolled out to a small subset of users before making it available to the entire user base.

</details>

### 188. q-545

A company wants to direct its users to a backup static error page if the company's primary website is unavailable. The primary website's DNS records are hosted in Amazon Route 53. The domain is pointing to an Application Load Balancer (ALB). The company needs a solution that minimizes changes and infrastructure overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up a Route 53 active-passive failover configuration. Direct traffic to a static error page that is hosted in an Amazon S3 bucket when Route 53 health checks determine that the ALB endpoint is unhealthy.**

An active-passive failover configuration in Route 53 involves designating one endpoint (primary, in this case, the ALB) as active and another endpoint (S3 bucket hosting a static error page) as passive. Route 53 health checks can be configured to monitor the health of the ALB endpoint. If the health checks determine that the ALB endpoint is unhealthy (i.e., the primary website is unavailable), Route 53 automatically directs traffic to the passive endpoint (S3 bucket with the static error page).

</details>

### 189. dt-546

True or False: in Amazon Route 53, you can create a hosted zone for a top-level domain (TLD).

<details><summary>Answer</summary>

**A. False.**

</details>

### 190. q-549

A company has created a multi-tier application for its ecommerce website. The website uses an Application Load Balancer that resides in the public subnets, a web tier in the public subnets, and a MySQL cluster hosted on Amazon EC2 instances in the private subnets. The MySQL database needs to retrieve product catalog and pricing information that is hosted on the internet by a third-party provider. A solutions architect must devise a strategy that maximizes security without increasing operational overhead. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy a NAT gateway in the public subnets. Modify the private subnet route table to direct all internet-bound traffic to the NAT gateway.**

A NAT gateway is a fully managed service provided by AWS that allows instances in a private subnet to initiate outbound traffic to the internet while preventing inbound traffic from reaching those instances. It simplifies the process of enabling internet access for instances in private subnets without the need for managing a separate NAT instance.

</details>

### 191. dt-555

You are building a solution for a customer to extend their on-premises data center to AWS. The customer requires a 50-Mbps dedicated and private connection to their VPC. Which AWS product or feature satisfies this requirement?

<details><summary>Answer</summary>

**C. AWS Direct Connect.**

</details>

### 192. q-555

A company runs an application in a VPC with public and private subnets. The VPC extends across multiple Availability Zones. The application runs on Amazon EC2 instances in private subnets. The application uses an Amazon Simple Queue Service (Amazon SQS) queue. A solutions architect needs to design a secure solution to establish a connection between the EC2 instances and the SQS queue. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Implement an interface VPC endpoint for Amazon SQS. Configure the endpoint to use the private subnets. Add to the endpoint a security group that has an inbound access rule that allows traffic from the EC2 instances that are in the private subnets.**

Interface VPC endpoints are used for services that are accessed over the Internet, and in this case, it's Amazon SQS. By implementing an interface VPC endpoint for SQS, you can ensure that the traffic stays within the Amazon network.

</details>

### 193. q-558 `cost`

A company has two VPCs that are located in the us-west-2 Region within the same AWS account. The company needs to allow network traffic between these VPCs. Approximately 500 GB of data transfer will occur between the VPCs each month. What is the MOST cost-effective solution to connect these VPCs?

<details><summary>Answer</summary>

**C. Set up a VPC peering connection between the VPCs. Update the route tables of each VPC to use the VPC peering connection for inter-VPC communication.**

VPC peering allows communication between VPCs within the same AWS account. It is a cost-effective solution, especially when the VPCs are located in the same region. In this case, both VPCs are in the us-west-2 region.

</details>

### 194. dt-561

Is there any way to own a direct connection to Amazon Web Services?

<details><summary>Answer</summary>

**D. Yes, it's called Direct Connect.**

</details>

### 195. dt-577

Select the incorrect statement.

<details><summary>Answer</summary>

**C. In Amazon VPC, an instance does NOT retain its private IP addresses when the instance is stopped.**

</details>

### 196. q-577

A company uses an Amazon CloudFront distribution to serve content pages for its website. The company needs to ensure that clients use a TLS certificate when accessing the company's website. The company wants to automate the creation and renewal of the TLS certificates. Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**C. Use AWS Certificate Manager (ACM) to create a certificate. Use DNS validation for the domain.**

AWS Certificate Manager (ACM): ACM is a fully managed service that allows you to easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources. It is designed for automation and ease of use.  DNS Validation: DNS validation involves adding a DNS record to your domain's DNS configuration. This method is more suitable for automation as it does not require manual intervention, and it can be easily integrated into automated certificate issuance and renewal processes.

</details>

### 197. q-582

An ecommerce company uses Amazon Route 53 as its DNS provider. The company hosts its website on premises and in the AWS Cloud. The company's on-premises data center is near the us-west-1 Region. The company uses the eu-central-1 Region to host the website. The company wants to minimize load time for the website as much as possible. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Set up a geolocation routing policy. Send the traffic that is near us-west-1 to the on-premises data center. Send the traffic that is near eu-central-1 to eu-central-1.**

The website runs in two places, an on-premises data center near us-west-1 and the eu-central-1 Region, so the shortest load time comes from sending each visitor to whichever is nearer. A geolocation routing policy resolves the name differently depending on where the query comes from, so North American users get the on-premises site and European users get eu-central-1. Latency-based routing would normally be the better tool for a pure latency goal, but Route 53 latency records measure latency to an AWS Region you associate with each record, and the latency option here associates only us-west-1, which cannot direct anyone to eu-central-1 and cannot represent an on-premises endpoint properly. A simple policy gives every requester the same answer and a weighted policy splits traffic by percentage, so neither takes location into account.

</details>

### 198. dt-589

Which Amazon service can I use to define a virtual network that closely resembles a traditional data center?

<details><summary>Answer</summary>

**A. Amazon VPC.**

</details>

### 199. dt-590

Select the correct set of options. These are the initial settings for the default security group:

<details><summary>Answer</summary>

**A. Allow no inbound traffic, Allow all outbound traffic and Allow instances associated with this security group to talk to each other.**

</details>

### 200. dt-596

Your team has a tomcat-based Java application you need to deploy into development, test and production environments. After some research, you opt to use Elastic Beanstalk due to its tight integration with your developer tools and RDS due to its ease of management. Your QA team lead points out that you need to roll a sanitized set of production data into your environment on a nightly basis. Similarly, other software teams in your org want access to that same restored data via their EC2 instances in your VPC. The optimal setup for persistence and security that meets the above requirements would be the following:

<details><summary>Answer</summary>

**A. Create your RDS instance as part of your Elastic Beanstalk definition and alter its security group to allow access to it from hosts in your application subnets.**

</details>

### 201. dt-600

You are setting up a VPC and you need to set up a public subnet within that VPC. Which following requirement must be met for this subnet to be considered a public subnet?

<details><summary>Answer</summary>

**B. Subnet's traffic is routed to an internet gateway.**

</details>

### 202. q-600

A company is planning to migrate a TCP-based application into the company's VPC. The application is publicly accessible on a nonstandard TCP port through a hardware appliance in the company's data center. This public endpoint can process up to 3 million requests per second with low latency. The company requires the same level of performance for the new public endpoint in AWS. What should a solutions architect recommend to meet this requirement?

<details><summary>Answer</summary>

**A. Deploy a Network Load Balancer (NLB). Configure the NLB to be publicly accessible over the TCP port that the application requires.**

Network Load Balancer (NLB): It operates at the connection level (Layer 4) and is well-suited for TCP traffic. It can handle millions of requests per second with minimal latency. NLB allows you to configure the listener for the specific TCP port that the application requires, ensuring compatibility with the nonstandard TCP port used by the application.

</details>

### 203. q-609

A company needs to connect its on-premises data center network to a new VPC. The data center network has a 100 Mbps symmetrical internet connection. An application that is running on premises will transfer multiple gigabytes of data each day. The application will use an Amazon Data Firehose delivery stream for processing. What should a solutions architect recommend for maximum performance?

<details><summary>Answer</summary>

**D. Use AWS PrivateLink to create an interface VPC endpoint for Firehose in the VPC. Set up a 1 Gbps AWS Direct Connect connection between the on-premises network and AWS. Use the PrivateLink endpoint to send the data from on premises to Firehose.**

For maximum performance, a dedicated, private connection is superior to one that traverses the public internet. AWS Direct Connect provides a private, dedicated network link from an on-premises data center to AWS, offering consistent low-latency performance and high bandwidth (e.g., 1 Gbps or higher). To send data to Amazon Data Firehose without traversing the public internet, AWS PrivateLink is used to create an interface VPC endpoint for Firehose. This endpoint makes the Firehose service privately accessible from the VPC, and by extension, from the on-premises network via the Direct Connect connection. This combination ensures the highest throughput and most reliable connectivity. Why Incorrect Options are Wrong: A. VPC peering is a networking connection between two VPCs. It cannot be used to connect an on-premises network to a VPC. B. AWS Snowball is designed for offline, large-scale

</details>

### 204. dt-610

A benefits enrollment company is hosting a 3-tier web application running in a VPC on AWS which includes a NAT (Network Address Translation) instance in the public Web tier. There is enough provisioned capacity for the expected workload for the new fiscal year benefit enrollment period plus some extra overhead. Enrollment proceeds nicely for two days and then the web tier becomes unresponsive. Upon investigation using CloudWatch and other monitoring tools it is discovered that there is an extremely large and unanticipated amount of inbound traffic coming from a set of 15 specific IP addresses over port 80 from a country where the benefits company has no customers. The web tier instances are so overloaded that benefit enrollment administrators cannot even SSH into them. Which activity would be useful in defending against this attack?

<details><summary>Answer</summary>

**D. Create an inbound NACL (Network Access control list) associated with the web tier subnet with deny rules to block the attacking IP addresses.**

</details>

### 205. q-610

A company deploys Amazon EC2 instances that run in a VPC. The EC2 instances load source data into Amazon S3 buckets so that the data can be processed in the future. According to compliance laws, the data must not be transmitted over the public internet. Servers in the company's on- premises data center will consume the output from an application that runs on the EC2 instances. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy a gateway VPC endpoint for Amazon S3. Set up an AWS Direct Connect connection between the on-premises network and the VPC.**

A gateway VPC endpoint allows communication between resources in your VPC and Amazon S3 without traversing the public internet. AWS Direct Connect provides a dedicated network connection from the on-premises data center to the VPC. This dedicated connection enhances security and ensures a reliable and consistent connection between on-premises servers and the EC2 instances in the VPC.

</details>

### 206. dt-612

Does AWS Direct Connect allow you access to all Availability Zones within a Region?

<details><summary>Answer</summary>

**A. Depends on the type of connection.**

</details>

### 207. q-612

A company has an application that runs on Amazon EC2 instances in a private subnet. The application needs to process sensitive information from an Amazon S3 bucket. The application must not use the internet to connect to the S3 bucket. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a VPC endpoint. Update the S3 bucket policy to allow access from the VPC endpoint. Update the application to use the new VPC endpoint.**

VPC Endpoint for S3: A VPC endpoint allows you to privately connect your VPC to supported AWS services, including Amazon S3, without traversing the public internet. This ensures secure and direct access to S3 from within your VPC.

</details>

### 208. dt-615

You need to create a load balancer in a VPC network that you are building. You can make your load balancer internal (private) or internet-facing (public). When you make your load balancer internal, a DNS name will be created, and it will contain the private IP address of the load balancer. An internal load balancer is not exposed to the internet. When you make your load balancer internet-facing, a DNS name will be created with the public IP address. If you want the Internet-facing load balancer to be connected to the Internet, where must this load balancer reside?

<details><summary>Answer</summary>

**A. The load balancer must reside in a subnet that is connected to the internet using the internet gateway.**

</details>

### 209. q-620

A company asks a solutions architect to review the architecture for its messaging application. The application uses TCP and UDP traffic. The company is planning to deploy a new VoIP feature, but its 10 test users in other countries are reporting poor call quality. The VoIP application runs on an Amazon EC2 instance with more than enough resources. The HTTP portion of the company's application behind an Application Load Balancer has no issues. What should the solutions architect recommend for the company to do to address the VoIP performance issues?

<details><summary>Answer</summary>

**A. Use AWS Global Accelerator.**

AWS Global Accelerator is the optimal solution because it is designed to improve the performance and availability of applications with a global user base. It uses the vast, congestion-free AWS global network to route user traffic to the application endpoint. For latency-sensitive applications like VoIP, which use TCP and UDP, Global Accelerator significantly reduces latency and jitter by directing traffic to an edge location nearest to the user and then carrying it over the AWS backbone. This bypasses the unpredictable public internet for a large portion of the path, directly addressing the poor call quality experienced by international users. Why Incorrect Options are Wrong: B. Implement Amazon CloudFront into the architecture. CloudFront is a Content Delivery Network (CDN) optimized for caching and delivering web content over HTTP/HTTPS, not for real-time, non-HTTP traffic like VoIP (U

</details>

### 210. dt-622

You manually launch a NAT AMI in a public subnet. The network is properly configured. Security groups and network access control lists are properly configured. Instances in a private subnet can access the NAT. The NAT can access the Internet. However, private instances cannot access the Internet. What additional step is required to allow access from the private instances?

<details><summary>Answer</summary>

**B. Enable Source/Destination Check on the NAT instance.**

</details>

### 211. q-623 `least-ops`

A company has set up hybrid connectivity between an on-premises data center and AWS by using AWS Site-to-Site VPN. The company is migrating a workload to AWS. The company sets up a VPC that has two public subnets and two private subnets. The company wants to monitor the total packet loss and round-trip-time (RTT) between the data center and AWS. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Use Amazon CloudWatch Network Monitor to set up Internet Control Message Protocol (ICMP) probe monitoring from each subnet to the on-premises destination.**

Amazon CloudWatch Network Monitor is a fully managed service designed specifically for monitoring network performance between AWS and on-premises environments. It measures key metrics like packet loss and round-trip time (RTT) without requiring users to deploy or manage any monitoring infrastructure. By creating a monitor and specifying the source subnets and the on-premises destination IP, the service automatically handles the probing and data collection. This approach directly fulfills the requirements with the least possible operational overhead, as it eliminates the need for managing EC2 instances, custom scripts, or complex service configurations. Why Incorrect Options are Wrong: B. This solution incurs high operational overhead due to the need to launch, manage, patch, and secure EC2 instances, in addition to developing and maintaining monitoring scripts. C. Using AWS Lambda requir

</details>

### 212. q-625

A company is hosting a website behind multiple Application Load Balancers. The company has different distribution rights for its content around the world. A solutions architect needs to ensure that users are served the correct content without violating distribution rights. Which configuration should the solutions architect choose to meet these requirements?

<details><summary>Answer</summary>

**C. Configure Amazon Route 53 with a geolocation policy**

Geolocation routing in Amazon Route 53 allows you to route traffic based on the geographic location of the user. You can create different records for your website content and associate them with specific geographic locations. This way, users from different regions will be directed to the appropriate servers or load balancers hosting the content that adheres to the distribution rights for that region.

</details>

### 213. q-627

A company wants to migrate two DNS servers to AWS. The servers host a total of approximately 200 zones and receive 1 million requests each day on average. The company wants to maximize availability while minimizing the operational overhead that is related to the management of the two servers. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Create 200 new hosted zones in the Amazon Route 53 console Import zone files.**

Amazon Route 53 is a highly available and scalable domain name system (DNS) web service provided by AWS. By creating 200 new hosted zones in the Amazon Route 53 console and importing the existing zone files, you can take advantage of the fully managed and highly available nature of Route 53 without the need to manage servers.

</details>

### 214. dt-629

Regarding the attaching of ENI to an instance, what does 'warm attach' refer to?

<details><summary>Answer</summary>

**A. Attaching an ENI to an instance when it is stopped.**

</details>

### 215. q-636

A company runs an application in a VPC on AWS. The company's on-premises data center has a DNS server. The data center is connected to AWS through an AWS Direct Connect connection with a private virtual interface (VIF). The on-premises DNS server needs to resolve the DNS name of the application in the VPC.

<details><summary>Answer</summary>

**D. Create an Amazon Route 53 Resolver inbound endpoint in the VPC. Configure the on-premises DNS server to send requests for the application to the inbound endpoint.**

The scenario requires DNS queries originating from an on-premises network to be resolved for resources within an AWS VPC. Amazon Route 53 Resolver is the service designed for this hybrid cloud DNS integration. An inbound endpoint for Route 53 Resolver provides one or more elastic network interfaces (ENIs) within the VPC. The on-premises DNS server can then be configured to conditionally forward DNS queries for the VPC's domain to the IP addresses of these ENIs. The inbound endpoint allows Route 53 Resolver to receive these queries from the on-premises network over the Direct Connect connection and resolve them using the VPC's DNS. Why Incorrect Options are Wrong: A. AWS Verified Access is a service for providing secure, VPN-less access to corporate applications. It is not a general-purpose DNS resolution service for hybrid networks. B. AWS Direct Connect provides the private network conn

</details>

### 216. dt-636

In Route 53, what does a Hosted Zone refer to?

<details><summary>Answer</summary>

**B. A hosted zone is a collection of resource record sets hosted by Route 53.**

</details>

### 217. q-639

A company wants to use AWS Direct Connect to connect the company's on-premises networks to the AWS Cloud. The company runs several VPCs in a single AWS Region. The company plans to expand its VPC fleet to include hundreds of VPCs. A solutions architect needs to simplify and scale the company's network infrastructure to accommodate future VPCs. Which service or resource will meet these requirements?

<details><summary>Answer</summary>

**B. AWS Transit Gateway**

AWS Transit Gateway acts as a network transit hub, or a cloud router, to simplify network architecture and scale connectivity. By connecting all VPCs and the on-premises network (via a Direct Connect gateway) to a single Transit Gateway, the company can manage routing in one central place. This hub-and-spoke model eliminates the need for complex VPC peering meshes or managing numerous individual connections as the number of VPCs grows to the hundreds. It directly addresses the requirements to simplify and scale the network infrastructure. Why Incorrect Options are Wrong: A. VPC endpoints provide private connectivity from a VPC to AWS services, not for interconnecting multiple VPCs and on-premises networks. C. Amazon Route 53 is a DNS service used for domain name resolution; it does not manage network routing topology or connectivity between VPCs. D. AWS Secrets Manager is a service for m

</details>

### 218. q-640

A company recently migrated its application to a VPC on AWS. An AWS Site-to-Site VPN connection connects the company's on-premises network to the VPC. The application retrieves customer data from another system that resides on premises. The application uses an on-premises DNS server to resolve domain records. After the migration, the application is not able to connect to the customer data because of name resolution errors. Which solution will give the application the ability to resolve the internal domain names?

<details><summary>Answer</summary>

**B. Create an Amazon Route 53 Resolver outbound endpoint. Configure the outbound endpoint to forward DNS queries against the on-premises domain to the on-premises DNS server.**

The most effective and scalable solution is to use Amazon Route 53 Resolver. By creating a Resolver outbound endpoint in the VPC, you establish a path for DNS queries to leave the VPC. You then create a forwarding rule associated with this endpoint. This rule specifies that any DNS queries for the on-premises domain should be forwarded to the IP address of the on-premises DNS server. The query travels securely over the existing Site-to-Site VPN connection. This is the AWS-native, managed service approach for integrating DNS resolution between a VPC and an on-premises network. Why Incorrect Options are Wrong: A. This is a legacy, self-managed approach. It introduces unnecessary operational overhead for managing EC2 instances and DNS software, whereas Route 53 Resolver provides a fully managed solution for this exact use case. C. This option incorrectly conflates network connectivity (AWS

</details>

### 219. dt-653 `availability`

A company has primary and secondary data centers that are 500 miles (804.7 km) apart and interconnected with high-speed fiber-optic cable. The company needs a highly available and secure network connection between its data centers and a VPC on AWS for a mission-critical workload. A solutions architect must choose a connection solution that provides maximum resiliency. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Two AWS Direct Connect connections from each of the primary and secondary data centers terminating at two Direct Connect locations on two separate devices.**

</details>

### 220. dt-655

A solutions architect is creating an application. The application will run on Amazon EC2 instances in private subnets across multiple Availability Zones in a VPC. The EC2 instances will frequently access large files that contain confidential information. These files are stored in Amazon S3 buckets for processing. The solutions architect must optimize the network architecture to minimize data transfer costs. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Create a gateway endpoint for Amazon S3 in the VPC. In the route tables for the private subnets, add an entry for the gateway endpoint.**

</details>

### 221. gh-657 `cost`

A company has multiple AWS accounts in an organization in AWS Organizations that different business units use. The company has multiple
o ces around the world. The company needs to update security group rules to allow new o ce CIDR ranges or to remove old CIDR ranges across
the organization. The company wants to centralize the management of security group rules to minimize the administrative overhead that updating
CIDR ranges requires.
Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**Answer: B) Create a shared prefix list via AWS RAM and reference it in security groups.**

Prefix lists centralize CIDR management. AWS RAM enables cross-account sharing.
Firewall Manager (Option D) is overkill for CIDR updates.

</details>

### 222. dt-662

A company runs a web application on multiple Amazon EC2 instances in a VPC. The application needs to write sensitive data to an Amazon S3 bucket. The data cannot be sent over the public internet. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a gateway VPC endpoint for Amazon S3. Create a route in the VPC route table to the endpoint.**

</details>

### 223. gh-663

A company is developing a new application on AWS. The application consists of an Amazon Elastic Container Service (Amazon ECS) cluster, an
Amazon S3 bucket that contains assets for the application, and an Amazon RDS for MySQL database that contains the dataset for the application.
The dataset contains sensitive information. The company wants to ensure that only the ECS cluster can access the data in the RDS for MySQL
database and the data in the S3 bucket.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: C) Restrict S3/RDS access via VPC endpoints + security groups.**

VPC endpoints keep traffic private. Security groups limit access to ECS subnets.
KMS (Options A/B) doesn’t restrict network access.

</details>

### 224. q-683

A company is deploying an application in three AWS Regions using an Application Load Balancer. Amazon Route 53 will be used to distribute traffic between these Regions. Which Route 53 configuration should a solutions architect use to provide the MOST high-performing experience?

<details><summary>Answer</summary>

**A. Create an A record with a latency policy.**

To provide the most high-performing experience for a multi-region application, the goal is to minimize latency for end-users. Amazon Route 53 latency-based routing directs user traffic to the AWS Region that provides the lowest network latency for that specific user. Route 53 determines the lowest latency endpoint by using a network of real-time latency measurements. An A record, specifically an Alias A record, is used to map the domain name directly to the AWS resource, such as an Application Load Balancer, in each region. This configuration ensures users are automatically routed to the region that will serve them the fastest. Why Incorrect Options are Wrong: B. Geolocation routing directs traffic based on the user's geographic location (e.g., country), not the lowest network latency, which is a more accurate measure of performance. C. Failover routing is for disaster recovery (active-p

</details>

### 225. dt-683 `least-ops`

A company has a three-tier web application that is deployed on AWS. The web servers are deployed in a public subnet in a VPC. The application servers and database servers are deployed in private subnets in the same VPC. The company has deployed a third-party virtual firewall appliance from AWS Marketplace in an inspection VPC. The appliance is configured with an IP interface that can accept IP packets. A solutions architect needs to integrate the web application with the appliance to inspect all traffic to the application before the traffic reaches the web server. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Deploy a Gateway Load Balancer in the inspection VPC. Create a Gateway Load Balancer endpoint to receive the incoming packets and forward the packets to the appliance.**

</details>

### 226. dt-693 `performance`

A company provides a Voice over Internet Protocol (VoIP) service that uses UDP connections. The service consists of Amazon EC2 instances that run in an Auto Scaling group. The company has deployments across multiple AWS Regions. The company needs to route users to the Region with the lowest latency. The company also needs automated failover between Regions. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region.**

</details>

### 227. dt-697

A company is preparing to launch a public-facing web application in the AWS Cloud. The architecture consists of Amazon EC2 instances within a VPC behind an Elastic Load Balancer (ELB). A third-party service is used for the DNS. The company's solutions architect must recommend a solution to detect and protect against large-scale DDoS attacks. Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Enable AWS Shield Advanced and assign the ELB to it.**

</details>

### 228. dt-706

A solutions architect is designing a three-tier web application. The architecture consists of an internet-facing Application Load Balancer (ALB) and a web tier that is hosted on Amazon EC2 instances in private subnets. The application tier with the business logic runs on EC2 instances in private subnets. The database tier consists of Microsoft SQL Server that runs on EC2 instances in private subnets. Security is a high priority for the company. Which combination of security group configurations should the solutions architect use? (Choose three.)

<details><summary>Answer</summary>

**A. Configure the security group for the web tier to allow inbound HTTPS traffic from the security group for the ALB.; C. Configure the security group for the database tier to allow inbound Microsoft SQL Server traffic from the security group for the application tier.; E. Configure the security group for the application tier to allow inbound HTTPS traffic from the security group for the web tier.**

</details>

### 229. q-707

A company wants to use AWS Direct Connect to connect on-premises networks to AWS. The company runs many VPCs in a single Region and plans to scale to hundreds of VPCs. Which service will simplify and scale the network architecture?

<details><summary>Answer</summary>

**B. AWS Transit Gateway**

AWS Transit Gateway is designed to simplify network connectivity at scale. It acts as a cloud router or a central hub, connecting thousands of VPCs and on-premises networks within a single, managed gateway. For a company scaling to hundreds of VPCs, a Transit Gateway avoids the complexity of numerous VPC peering connections or managing a separate Virtual Private Gateway (VGW) for each VPC. By connecting the AWS Direct Connect gateway to the Transit Gateway, the company can establish a hub-and-spoke architecture, providing a single point of management and connectivity for all attached VPCs, which is highly scalable and simplifies the overall network design. Why Incorrect Options are Wrong: A. VPC endpoints provide private connectivity from a VPC to AWS services or endpoint services, not for connecting VPCs to on-premises networks. C. Amazon Route 53 is a scalable Domain Name System (DNS)

</details>

### 230. q-717

A solutions architect runs a web application on multiple Amazon EC2 instances that are in individual target groups behind an Application Load Balancer (ALB). Users can reach the application through a public website. The solutions architect wants to allow engineers to use a development version of the website to access one specific development EC2 instance to test new features for the application. The solutions architect wants to use an Amazon Route 53 hosted zone to give the engineers access to the development instance. The solution must automatically route to the development instance even if the development instance is replaced. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create an A record for the development website that has the value set to the ALB. Create a listener rule on the ALB that forwards requests for the development website to the target group that contains the development instance.**

The most effective solution is to use the Application Load Balancer's (ALB) host-based routing feature. By creating a unique DNS A record (e.g., dev.example.com) pointing to the ALB, a listener rule can be configured on the ALB. This rule inspects the host header of incoming requests. If the host header matches the development website's URL, the ALB forwards the traffic to a dedicated target group containing only the development EC2 instance. This isolates development traffic and automatically handles instance replacements as long as the new instance is registered with the correct target group. Why Incorrect Options are Wrong: B. Using a public IP address bypasses the ALB and requires manual DNS updates if the instance is replaced, failing the automation requirement. C. Redirecting to a public IP is inefficient and also fails the automation requirement, as the IP address would change if

</details>

### 231. dt-721

A company wants to build an immutable infrastructure for its software applications. The company wants to test the software applications before sending traffic to them. The company seeks an efficient solution that limits the effects of application bugs. Which combination of steps should a solutions architect recommend? (Select TWO.)

<details><summary>Answer</summary>

**B. Apply Amazon Route 53 weighted routing to test the staging environment and gradually increase the traffic as the tests pass.; D. Use AWS CloudFormation with a parameter set to the staging value in a separate environment other than the production environment.**

</details>

### 232. dt-723

An application running in a private subnet accesses an Amazon DynamoDB table. The data cannot leave the AWS network to meet security requirements. How should this requirement be met?

<details><summary>Answer</summary>

**D. Create a gateway VPC endpoint for DynamoDB and configure the endpoint policy.**

</details>

### 233. q-729 `performance`

A global company hosts its web application on Amazon EC2 instances behind an Application Load Balancer ALB. The web application has static data and dynamic data. The company stores its static data in an Amazon S3 bucket. The company wants to improve performance and reduce latency for the static data and dynamic data. The company is using its own domain name registered with Amazon Route 53. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon CloudFront distribution that has the S3 bucket and the ALB as origins. Configure Route 53 to route traffic to the CloudFront distribution.**

Amazon CloudFront is designed to accelerate the delivery of both static and dynamic content. By creating a single CloudFront distribution with two origins-the S3 bucket for static assets and the Application Load Balancer (ALB) for dynamic content-the company can leverage AWS's global edge network. Cache behaviors can be configured based on URL path patterns (e.g., /images/ to S3, / to ALB) to route requests to the appropriate origin. This setup caches static content close to users and uses AWS's optimized network to accelerate dynamic requests to the ALB, improving performance and reducing latency for all content through a single domain name configured in Route 53. Why Incorrect Options are Wrong: B. AWS Global Accelerator is not the optimal service for caching static content from S3; CloudFront is. This solution is unnecessarily complex and misuses Global Accelerator. C. This configurat

</details>

### 234. dt-733

A company that recently started using AWS establishes a Site-to-Site VPN between its on-premises datacenter and AWS. The company's security mandate states that traffic originating from on premises should stay within the company's private IP space when communicating with an Amazon Elastic Container Service (Amazon ECS) cluster that is hosting a sample web application. Which solution meets this requirement?

<details><summary>Answer</summary>

**B. Create a Network Load Balancer and AWS PrivateLink endpoint for Amazon ECS in the same VPC that is hosting the ECS cluster.**

</details>

### 235. dt-740

A company has applications hosted on Amazon EC2 instances with IPv6 addresses. The applications must initiate communications with other external applications using the internet. However, the company's security policy states that any external service cannot initiate a connection to the EC2 instances. What should a solutions architect recommend to resolve this issue?

<details><summary>Answer</summary>

**D. Create an egress-only internet gateway and make it the destination of the subnet's route table.**

</details>

### 236. q-749

A company is designing the network for an online multi-player game. The game uses the UDP networking protocol and will be deployed in eight AWS Regions. The network architecture needs to minimize latency and packet loss to give end users a high-quality gaming experience. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up AWS Global Accelerator with UDP listeners and endpoint groups in each Region.**

The key requirements are minimizing latency and packet loss for a global, multi-region UDP-based game. AWS Global Accelerator is a networking service designed for this exact purpose. It uses the highly available and congestion-free AWS global network to direct traffic from users to the nearest application endpoint. It provides static anycast IP addresses as a fixed entry point and optimizes the path, which significantly reduces latency and packet loss for both TCP and UDP traffic. This makes it the ideal solution for improving the performance of a global online game. Why Incorrect Options are Wrong: A. Transit Gateway peering connects VPCs but does not optimize the network path from the end-user to the AWS network, which is critical for latency. C. Amazon CloudFront is a content delivery network (CDN) primarily optimized for caching and delivering HTTP/S web content, not for real-time UD

</details>

### 237. q-750

A company is planning to migrate to AWS. The network layout will include more than 1,000 VPCs in a single AWS Region. The resources in the VPCs need to communicate with each other. What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**D. Create a transit gateway, and place attachments in subnets of all the VPCs. Configure a transit gateway route table with the new routes.**

AWS Transit Gateway is designed to simplify network connectivity at scale. It acts as a central hub or a cloud router to interconnect thousands of VPCs and on-premises networks without requiring complex peering connections. By creating a transit gateway and attaching all 1,000+ VPCs to it, you establish a hub-and-spoke topology. This drastically simplifies route management and scales effectively to meet the requirement of connecting a large number of VPCs. Why Incorrect Options are Wrong: A. Creating a full mesh of VPN tunnels between 1,000+ VPCs is operationally unmanageable and does not scale. B. AWS Direct Connect is used for connecting on-premises data centers to AWS, not for inter-VPC communication within an AWS Region. C. VPC peering does not support a transitive relationship and would require a full mesh of connections. Managing peering for over 1,000 VPCs is not feasible due to c

</details>

### 238. dt-758

A company previously migrated its data warehouse solution to AWS. The company also has an AWS Direct Connect connection. Corporate office users query the data warehouse using a visualization tool. The average size of a query returned by the data warehouse is 50 MB and each webpage sent by the visualization tool is approximately 500 KB. Result sets returned by the data warehouse are not cached. Which solution provides the LOWEST data transfer egress cost for the company?

<details><summary>Answer</summary>

**D. Host the visualization tool in the same AWS Region as the data warehouse and access it over a Direct Connect connection at a location in the same Region.**

</details>

### 239. dt-760

A company has an application that runs on Amazon EC2 instances within a private subnet in a VPC. The instances access data in an Amazon S3 bucket in the same AWS Region. The VPC contains a NAT gateway in a public subnet to access the S3 bucket. The company wants to reduce costs by replacing the NAT gateway without compromising security or redundancy. Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Replace the NAT gateway with a gateway VPC endpoint.**

</details>

### 240. dt-761

A company hosts a website on premises and wants to migrate it to the AWS Cloud. The website exposes a single hostname to the internet but it routes its functions to different on-premises server groups based on the path of the URL. The server groups are scaled independently depending on the needs of the functions they support. The company has an AWS Direct Connect connection configured to its on-premises network. What should a solutions architect do to provide path-based routing to send the traffic to the correct group of servers?

<details><summary>Answer</summary>

**C. Route all traffic to an Application Load Balancer (ALB). Configure path-based routing at the ALB to route traffic to the correct target group for the servers supporting that path.**

</details>

### 241. q-768

A company hosts an application on an Amazon EC2 instance in a single AWS Region. The application requires support for non-HTTP TCP traffic and HTTP traffic. The company wants to deliver content with low latency by using the AWS network. The company also wants to implement an Auto Scaling group with an Elastic Load Balancing (ELB) load balancer. How should a solutions architect meet these requirements?

<details><summary>Answer</summary>

**D. Create an Auto Scaling group with a Network Load Balancer (NLB). Add an accelerator with AWS Global Accelerator with the NLB as an endpoint.**

The requirement to support both non-HTTP TCP and HTTP traffic necessitates a load balancer that operates at the transport layer (Layer 4). A Network Load Balancer (NLB) is designed for this purpose, handling TCP, UDP, and TLS traffic. An Application Load Balancer (ALB) operates at the application layer (Layer 7) and is limited to HTTP, HTTPS, and gRPC protocols. To achieve low latency using the AWS global network for TCP-based applications, AWS Global Accelerator is the appropriate service. It directs user traffic over the optimized AWS global network to the application endpoint, reducing latency and jitter. Amazon CloudFront is a CDN primarily for caching and accelerating HTTP/S web content, not generic TCP traffic. Therefore, combining an NLB with an Auto Scaling group and placing it behind a Global Accelerator accelerator meets all requirements. Why Incorrect Options are Wrong: A. App

</details>

### 242. dt-768

A company has an application hosted on Amazon EC2 instances in two VPCs across different AWS Regions. To communicate with each other, the instances use the internet for connectivity. The security team wants to ensure that no communication between the instances happens over the internet. What should a solutions architect do to accomplish this?

<details><summary>Answer</summary>

**D. Create a VPC peering connection and update the route table of the EC2 instances' subnet.**

</details>

### 243. dt-771

A company is designing a web application with an internet-facing Application Load Balancer (ALB). The company needs the ALB to receive HTTPS web traffic from the public internet. The ALB must send only HTTPS traffic to the web application servers hosted on the Amazon EC2 instances on port 443. The ALB must perform a health check of the web application servers over HTTPS on port 8443. Which combination of configurations of the security group that is associated with the ALB will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**A. Allow HTTPS inbound traffic from 0.0.0.0/0 for port 443.; C. Allow HTTPS outbound traffic to the web application instances for port 443.; E. Allow HTTPS outbound traffic to the web application instances for the health check on port 8443.**

</details>

### 244. q-801

A company recently migrated a data warehouse to AWS. The company has an AWS Direct Connect connection to AWS. Company users query the data warehouse by using a visualization tool. The average size of the queries that the data warehouse returns is 50 MB. The average visualization that the visualization tool produces is 500 KB in size. The result sets that the data warehouse returns are not cached. The company wants to optimize costs for data transfers between the data warehouse and the company. Which solution will meet this requirement?

<details><summary>Answer</summary>

**D. Host the visualization tool in the same AWS Region as the data warehouse. Access the visualization tool through the Direct Connect connection.**

The primary goal is to minimize data transfer costs, which are mainly incurred for data egress from an AWS Region. The query returns a large 50 MB dataset, while the final visualization is only 500 KB. The most cost-effective strategy is to perform the data processing (generating the visualization from the query result) within AWS. By hosting the visualization tool in the same AWS Region as the data warehouse, the large 50 MB data transfer occurs within the region, which is either free or significantly cheaper than egress traffic. Consequently, only the small 500 KB visualization needs to be transferred out to the users. Using the existing AWS Direct Connect connection for this egress is more cost-effective than transferring data over the public internet. Why Incorrect Options are Wrong: A. This option transfers the large 50 MB dataset out of AWS over the internet, which is the most expe

</details>

### 245. q-809 `cost`

A company hosts its applications in multiple private and public subnets in a VPC. The applications in the private subnets need to access an API. The API is available on the internet and is hosted in the company's on-premises data center. A solutions architect needs to establish connectivity for applications in the private subnets. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**D. Implement an AWS Site-to-Site VPN connection between the VPC and the on-premises data center. Use the VPN connection to make API calls from the private subnets to the on-premises data center.**

The most cost-effective solution to establish secure, private connectivity between a VPC and an on-premises data center is an AWS Site-to-Site VPN. This service creates an encrypted tunnel over the internet, allowing applications in the private subnets to securely access the on-premises API without traversing the public internet unprotected. Compared to other hybrid connectivity options like AWS Direct Connect or AWS Transit Gateway, a Site-to-Site VPN offers the lowest entry cost, making it ideal for scenarios with moderate bandwidth requirements. It directly fulfills the need for connecting the private subnets to the on-premises network. Why Incorrect Options are Wrong: A. A transit gateway is designed to simplify network management for connecting multiple VPCs and on-premises networks. For a single VPC-to-on-premises connection, it introduces unnecessary complexity and higher costs th

</details>

### 246. q-837

A company hosts a website on Amazon EC2 instances behind an Application Load Balancer (ALB). The website serves static content. Website traffic is increasing. The company wants to minimize the website hosting costs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Move the website to an Amazon S3 bucket. Configure an Amazon CloudFront distribution for the S3 bucket.**

The most cost-effective and scalable solution for hosting a static website on AWS is to use Amazon S3 for storage and Amazon CloudFront as a Content Delivery Network (CDN). The current architecture using EC2 instances and an Application Load Balancer is designed for dynamic applications and is inefficient for serving static content, leading to higher costs. By moving the static files to an S3 bucket configured for website hosting, the company leverages a low-cost, durable storage service. Adding a CloudFront distribution in front of the S3 bucket caches the content at edge locations globally. This significantly improves performance for users, reduces latency, and minimizes data transfer costs from S3, directly addressing the requirements of handling increasing traffic while reducing expenses. Why Incorrect Options are Wrong: B: Amazon ElastiCache is an in-memory caching service for datab

</details>

### 247. q-839 `availability`

A company runs multiple workloads in separate AWS environments. The company wants to optimize its AWS costs but must maintain the same level of performance for the environments. The company's production environment requires resources to be highly available. The other environments do not require highly available resources. Each environment has the same set of networking components, including the following: • 1 VPC • 1 Application Load Balancer • 4 subnets distributed across 2 Availability Zones (2 public subnets and 2 private subnets) • 2 NAT gateways (1 in each public subnet) • 1 internet gateway Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Do not change the production environment workload. For each non-production workload, remove one NAT gateway and update the route tables for private subnets to target the remaining NAT gateway for the destination 0.0.0.0/0.**

The goal is to optimize costs for non-production environments while maintaining high availability (HA) for the production environment. NAT Gateways incur a fixed hourly charge. The described setup with two NAT Gateways, one in each Availability Zone (AZ), is a standard high-availability pattern. Since non-production environments do not require HA, one of the two NAT Gateways can be eliminated to save on hourly costs. The route tables for private subnets in both AZs can be updated to point to the single remaining NAT Gateway. This meets the cost optimization goal for non-production environments without impacting the performance or availability of the production environment. Why Incorrect Options are Wrong: B: Reducing the number of Availability Zones for all environments would violate the high availability requirement for the production environment. C: Replacing managed NAT gateways with

</details>

### 248. q-893

A company is running a web-based game in two Availability Zones in the us-west-2 Region. The web servers use an Application Load Balancer (ALB) in public subnets. The ALB has an SSL certificate from AWS Certificate Manager (ACM) with a custom domain name. The game is written in JavaScript and runs entirely in a user's web browser. The game is increasing in popularity in many countries around the world. The company wants to update the application architecture and optimize costs without compromising performance. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon S3 and create an S3 bucket in us-west-2. Deploy the HTML and JavaScript files to the S3 bucket. Use Amazon CloudFront and create a global distribution with the S3 bucket as the origin. Use ACM to create a new certificate for the distribution. Use Amazon Route 53 to update the application alias to point to the distribution.**

The game consists of static JavaScript and HTML files, which are ideal for hosting in Amazon S3. To provide low-latency access to a global audience, Amazon CloudFront should be used as a Content Delivery Network (CDN). A CloudFront distribution is created with the S3 bucket as its origin. CloudFront caches the game's files at edge locations around the world, closer to the users. This significantly improves performance and is more cost-effective than running web servers on EC2 instances for static content. A new ACM certificate is needed for the CloudFront distribution's custom domain name. Why Incorrect Options are Wrong: A. Using CloudFront with the ALB is a valid pattern but is not cost-optimal for purely static content, as it retains the cost of the EC2 instances and ALB. B. Deploying the entire application stack to multiple regions is the most complex and expensive option, representi

</details>

### 249. q-946

A company manages separate AWS environments for multiple customers. Each customer has its own dedicated VPC, internet gateway, NAT gateway, network infrastructure, and some common management services. The company wants to avoid increasing infrastructure costs as the company onboards new customers. The company wants to optimize network architecture costs while maintaining strict customer data isolation requirements. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a shared-services VPC that contains a transit gateway. Configure each customer VPC to use its own transit gateway route table. Enable routing only to the shared-services VPC.**

This solution describes a scalable and cost-effective hub-and-spoke network architecture using AWS Transit Gateway. A central shared-services VPC (the hub) is created to host common resources like NAT gateways and management services, which eliminates the need to provision these for every customer. This directly addresses the cost optimization requirement. By attaching each customer VPC (the spokes) to the Transit Gateway and assigning each attachment its own unique route table, strict isolation is enforced. Configuring these route tables to only allow traffic to and from the shared-services VPC prevents any inter-customer VPC communication, thus meeting the strict data isolation requirement. Why Incorrect Options are Wrong: A: Using a single, default Transit Gateway route table for all customers would allow all connected VPCs to route traffic to each other by default, which violates the

</details>

### 250. q-949

A company is designing an advertisement distribution application to run on AWS. The company wants to deploy the application as a container to Amazon Elastic Container Service (Amazon ECS). Advertisements must be displayed to users around the world with low latency. The company needs to optimize data transfer costs. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application in a single AWS Region. Use an Application Load Balancer (ALB) to distribute traffic. Create an Amazon CloudFront distribution, and set the ALB as the origin.**

This solution correctly uses Amazon CloudFront, a Content Delivery Network (CDN), to meet the requirements. By deploying the application in a single AWS Region and placing a CloudFront distribution in front of the Application Load Balancer (ALB), the company can cache advertisement content at edge locations worldwide. This significantly reduces latency for global users as they are served from a nearby edge location. This architecture also optimizes data transfer costs because many requests are served from the CloudFront cache, reducing the amount of data transferred out from the origin (the ALB and ECS application), which is typically more expensive. This is a standard, cost-effective pattern for global content delivery. Why Incorrect Options are Wrong: B: A multi-region deployment with Route 53 latency routing is more complex and expensive to operate than a single-region deployment with

</details>

### 251. q-956 `availability`

An ecommerce company hosts an application on AWS across multiple Availability Zones. The application experiences uniform load throughout most days. The company hosts some components of the application in private subnets. The components need to access the internet to install and update patches. A solutions architect needs to design a cost-effective solution that provides secure outbound internet connectivity for private subnets across multiple Availability Zones. The solution must maintain high availability.

<details><summary>Answer</summary>

**A. Deploy one NAT gateway in each Availability Zone. Configure the route table for each pri-vate subnet within an Availability Zone to route outbound traffic through the NAT gateway in the same Availability Zone.**

The most effective solution to provide highly available and secure outbound internet connectivity for private subnets across multiple Availability Zones (AZs) is to deploy a NAT gateway in each AZ. Each private subnet's route table should be configured to direct internet-bound traffic to the NAT gateway within its own AZ. This architecture ensures that an outage in one AZ does not affect the internet connectivity of resources in other AZs, thus meeting the high availability requirement. This design also avoids inter-AZ data transfer costs for this traffic, making it cost-effective at scale, which aligns with AWS best practices for reliability and cost optimization. Why Incorrect Options are Wrong: B. Placing a single NAT gateway in one AZ creates a single point of failure. If that specific AZ experiences an outage, all private subnets lose internet access, violating the high availability

</details>

### 252. q-957 `cost`

A company needs to create an AWS Lambda function that will run in a VPC in the company's primary AWS account. The Lambda function needs to access files that the company stores in an Amazon Elastic File System (Amazon EFS) file system. The EFS file system is located in a secondary AWS account. As the company adds files to the file system, the solution must scale to meet the demand. Which solution will meet these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**B. Create a VPC peering connection between the VPCs that are in the primary account and the secondary account.**

The most direct, scalable, and cost-effective method to allow a VPC-enabled Lambda function in one account to access an EFS file system in another account is by establishing a network path between their respective VPCs. A VPC peering connection provides private, direct network connectivity between two VPCs, even across different AWS accounts. Once the peering connection is established, and the associated route tables and security groups are configured to allow traffic, the Lambda function can mount the EFS file system as if it were in the same VPC. This solution avoids costly data duplication and the architectural complexity of alternative approaches. Why Incorrect Options are Wrong: A. Duplicating the EFS file system with AWS DataSync doubles storage costs and introduces synchronization latency, making it expensive and not suitable for real-time access. C. Chaining Lambda functions is i

</details>
