# Networking — VPC, load balancing, DNS, edge, hybrid

77 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. gh-4

An application runs on an Amazon EC2 instance in a VPC. The application processes logs that are stored in an Amazon S3 bucket. The EC2 instance needs to access the S3 bucket without connectivity to the internet.
Which solution will provide private network connectivity to Amazon S3?

<details><summary>Answer</summary>

**A. Create a gateway VPC endpoint to the S3 bucket.**

Keywords:
- EC2 in VPC
- EC2 instance needs to access the S3 bucket without connectivity to the internet
VPC endpoint allows you to connect to AWS services using a private network instead of using the public Internet.

With a gateway endpoint, you can access Amazon S3 from your VPC, without requiring an internet gateway or NAT device for your VPC, and with no additional cost. However, gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway.

</details>

### 2. wl-11

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

### 3. gh-12 `performance`

A global company hosts its web application on Amazon EC2 instances behind an Application Load Balancer (ALB). The web application has static data and dynamic data. The company stores its static data in an Amazon S3 bucket. The company wants to improve performance and reduce latency for the static data and dynamic data. The company is using its own domain name registered with Amazon Route 53.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Create an Amazon CloudFront distribution that has the S3 bucket and the ALB as origins. Configure Route 53 to route traffic to the CloudFront distribution.**

CloudFront with Multiple Origins: CloudFront allows you to set up multiple origins for your distribution, so you can use both the ALB (for dynamic content) and the S3 bucket (for static content) as origins. This means that both your dynamic and static content can be served through CloudFront, which will cache content at edge locations to reduce latency.
Route 53 Integration with CloudFront: Amazon Route 53 can be easily configured to route traffic for your domain to a CloudFront distribution. Users will access your domain, and Route 53 will direct them to the nearest CloudFront edge location.

</details>

### 4. gh-15

A company recently migrated to AWS and wants to implement a solution to protect the traffic that flows in and out of the production VPC. The company had an inspection server in its on-premises data center. The inspection server performed specific operations such as traffic flow inspection and traffic filtering. The company wants to have the same functionalities in the AWS Cloud.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Use AWS Network Firewall to create the required rules for traffic inspection and traffic filtering for the production VPC.**

AWS Network Firewall is a managed firewall service that provides filtering for both inbound and outbound network traffic. It allows you to create rules for traffic inspection and filtering, which can help protect your production VPC

</details>

### 5. wl-17

How many VPCs can an Internet Gateway be attached to at any given time?

<details><summary>Answer</summary>

**C. 1**

https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/amazon-vpc-limits.html
#vpc-limits-gateways
At any given time, an Internet Gateway can be attached to only one VPC. It can be
detached from the VPC and be used for another VPC.

</details>

### 6. wl-18

Your organization was planning to develop a web application on AWS EC2. Application admin was tasked to perform AWS setup required to spin EC2 instance inside an existing private VPC. He/she has created a subnet and wants to ensure no other subnets in the VPC can communicate with your subnet except for the specific IP address. So he/she created a new route table and associated with the new subnet. When he/she was trying to delete the route with the target as local, there is no option to delete the route. What could have caused this behavior?

<details><summary>Answer</summary>

**B. A route with the target as local cannot be deleted.**

https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.htm
l#RouteTa

</details>

### 7. gh-19 `least-ops`

A company has a three-tier web application that is deployed on AWS. The web servers are deployed in a public subnet in a VPC. The application servers and database servers are deployed in private subnets in the same VPC. The company has deployed a third-party virtual firewall appliance from AWS Marketplace in an inspection VPC. The appliance is configured with an IP interface that can accept IP packets.
A solutions architect needs to integrate the web application with the appliance to inspect all traffic to the application before the traffic reaches the web server.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Deploy a Gateway Load Balancer in the inspection VPC. Create a Gateway Load Balancer endpoint to receive the incoming packets and forward the packets to the appliance.**

Gateway Load Balancer is a new type of load balancer that operates at layer 3 of the OSI model and is built on Hyperplane, which is capable of handling several thousands of connections per second. Gateway Load Balancer endpoints are configured in spoke VPCs originating or receiving traffic from the Internet. This architecture allows you to perform inline inspection of traffic from multiple spoke VPCs in a simplified and scalable fashion while still centralizing your virtual appliances.

</details>

### 8. wl-22

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

### 9. wl-23

Your organization has an existing VPC setup and has a requirement to route any traffic going from VPC to AWS S3 bucket through AWS internal network. So they have created a VPC endpoint for S3 and configured to allow traffic for S3 buckets. The application you are developing involves sending traffic to AWS S3 bucket from VPC for which you planned to use a similar approach. You have created a new route table, added route to VPC endpoint and associated route table with your new subnet. However, when you are trying to send a request from EC2 to S3 bucket using AWS CLI, the request is getting failed with 403 access denied errors. What could be causing the failure?

<details><summary>Answer</summary>

**C. VPC endpoint might have a restrictive policy and does not contain the new S3**

Option A is not correct. The question states “403 access denied”. If the S3 bucket is in
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
In this case, the request is not coming from a web client.

</details>

### 10. wl-25

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

### 11. wl-26

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

### 12. wl-27

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

### 13. gh-29 `performance`

A company provides a Voice over Internet Protocol (VoIP) service that uses UDP connections. The service consists of Amazon EC2 instances that run in an Auto Scaling group. The company has deployments across multiple AWS Regions.
The company needs to route users to the Region with the lowest latency. The company also needs automated failover between Regions.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region.**

Answer A does not mention service Global Accelerator, it mentions the NLB would act like one. Not sure if the wording is wrong or not.
' Deploy a Network Load Balancer (NLB) and an associated target group. Associate the target group with the Auto Scaling group. Use the NLB as an AWS Global Accelerator endpoint in each Region.

</details>

### 14. gh-35

A company is preparing to launch a public-facing web application in the AWS Cloud. The architecture consists of Amazon EC2 instances within a VPC behind an Elastic Load Balancer (ELB). A third-party service is used for the DNS. The company's solutions architect must recommend a solution to detect and protect against large-scale DDoS attacks.
Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Enable AWS Shield Advanced and assign the ELB to it.**

AWS Shield Advanced provides expanded DDoS attack protection for your Amazon EC2 instances, Elastic Load Balancing load balancers, CloudFront distributions, Route 53 hosted zones, and AWS Global Accelerator standard accelerators.

</details>

### 15. gh-38 `cost`

A company is hosting a static website on Amazon S3 and is using Amazon Route 53 for DNS. The website is experiencing increased demand from around the world. The company must decrease latency for users who access the website.
Which solution meets these requirements MOST cost-effectively?

<details><summary>Answer</summary>

**C. Add an Amazon CloudFront distribution in front of the S3 bucket. Edit the Route 53 entries to point to the CloudFront distribution**

Amazon CloudFront is a content delivery network (CDN) service that distributes content globally to reduce latency. By setting up a CloudFront distribution in front of the S3 bucket hosting the static website, you can take advantage of its edge locations around the world to deliver content from the nearest location to the users, reducing the latency they experience.

CloudFront automatically caches and replicates content to its edge locations, resulting in faster delivery and lower latency for users worldwide. This solution is highly effective in optimizing performance while keeping costs under control because CloudFront charges are based on actual data transfer and requests, and the pay-as-you-go pricing model ensures that you only pay for what you use.

</details>

### 16. gh-42 `cost` `availability`

A company runs a highly available image-processing application on Amazon EC2 instances in a single VPC. The EC2 instances run inside several subnets across multiple Availability Zones. The EC2 instances do not communicate with each other. However, the EC2 instances download images from Amazon S3 and upload images to Amazon S3 through a single NAT gateway. The company is concerned about data transfer charges.
What is the MOST cost-effective way for the company to avoid Regional data transfer charges?

<details><summary>Answer</summary>

**C. Deploy a gateway VPC endpoint for Amazon S3.**

S3 VPC endpoint provides a way for an S3 request to be routed through to the Amazon S3 service, without having to connect a subnet to an internet gateway. The S3 VPC endpoint is what's known as a gateway endpoint.

</details>

### 17. gh-208

A company needs to move data from an Amazon EC2 instance to an Amazon S3 bucket. The company must ensure that no API calls and no data are routed through public internet routes. Only the EC2 instance can have access to upload data to the S3 bucket.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Create a gateway VPC endpoint for Amazon S3 in the Availability Zone where the EC2 instance is located. Attach appropriate security**

groups to the endpoint. Attach a resource policy to the S3 bucket to only allow the EC2 instance’s IAM role for access.

Interface VPC endpoints for Amazon S3 (powered by AWS PrivateLink) allow communication between resources in your VPC and Amazon S3 without relying on public internet routes. It provides a secure and private connection.
By creating an interface VPC endpoint for Amazon S3 in the subnet where the EC2 instance is located, you ensure that the data doesn't travel over the public internet.
Attaching a resource policy to the S3 bucket allows you to control access and restrict it to the IAM role associated with the EC2 instance, ensuring only authorized entities can upload data to the bucket.

</details>

### 18. gh-213

A company is developing a new mobile app. The company must implement proper traffic filtering to protect its Application Load Balancer (ALB) against common application-level attacks, such as cross-site scripting or SQL injection. The company has minimal infrastructure and operational staff. The company needs to reduce its share of the responsibility in managing, updating, and securing servers for its AWS environment.
What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Configure AWS WAF rules and associate them with the ALB.**

AWS WAF (Web Application Firewall) is a service that helps protect web applications from common web exploits by allowing you to define customizable web security rules. It can be associated with an Application Load Balancer (ALB) to filter and block malicious traffic before it reaches the application.
AWS WAF is a managed service, which means it reduces the operational burden on the company by handling the infrastructure, updates, and security configurations.

</details>

### 19. gh-217

A company runs a global web application on Amazon EC2 instances behind an Application Load Balancer. The application stores data in Amazon Aurora. The company needs to create a disaster recovery solution and can tolerate up to 30 minutes of downtime and potential data loss. The solution does not need to handle the load when the primary infrastructure is healthy.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Deploy the application with the required infrastructure elements in place. Use Amazon Route 53 to configure active-passive failover. Create an Aurora Replica in a second AWS Region.**

</details>

### 20. gh-218

A company has a web server running on an Amazon EC2 instance in a public subnet with an Elastic IP address. The default security group is assigned to the EC2 instance. The default network ACL has been modified to block all traffic. A solutions architect needs to make the web server accessible from everywhere on port 443.
Which combination of steps will accomplish this task? (Choose two.)

<details><summary>Answer</summary>

**A. Create a security group with a rule to allow TCP port 443 from source 0.0.0.0/0.**

E. Update the network ACL to allow inbound TCP port 443 from source 0.0.0.0/0 and outbound TCP port 32768-65535 to destination 0.0.0.0/0.

</details>

### 21. gh-231 `security`

An application runs on an Amazon EC2 instance that has an Elastic IP address in VPC A. The application requires access to a database in VPC B. Both VPCs are in the same AWS account.
Which solution will provide the required access MOST securely?

<details><summary>Answer</summary>

**B. Configure a VPC peering connection between VPC A and VPC B.**

VPC peering allows direct connectivity between two VPCs. This solution enables communication between instances in VPC A and VPC B using private IP addresses. It does not require public IP addresses or the exposure of databases to the public internet.

</details>

### 22. gh-237

An application running on an Amazon EC2 instance in VPC-A needs to access files in another EC2 instance in VPC-B. Both VPCs are in separate AWS accounts. The network administrator needs to design a solution to configure secure access to EC2 instance in VPC-B from VPC-A. The connectivity should not have a single point of failure or bandwidth concerns.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Set up a VPC peering connection between VPC-A and VPC-B.**

A VPC peering connection allows secure communication between instances in different VPCs using private IP addresses without the need for internet gateways, VPN connections, or NAT devices. By setting it up, the application running in VPC-A can directly access the EC2 in VPC-B without going through the public internet or any single point of failure.

</details>

### 23. gh-240

A company previously migrated its data warehouse solution to AWS. The company also has an AWS Direct Connect connection. Corporate office users query the data warehouse using a visualization tool. The average size of a query returned by the data warehouse is 50 MB and each webpage sent by the visualization tool is approximately 500 KB. Result sets returned by the data warehouse are not cached.
Which solution provides the LOWEST data transfer egress cost for the company?

<details><summary>Answer</summary>

**D. Host the visualization tool in the same AWS Region as the data warehouse and access it over a Direct Connect connection at a location in the same Region.**

Hosting the visualization tool in the same AWS Region as the data warehouse and accessing it over a Direct Connect connection within the same Region minimizes data transfer costs. Since the data warehouse and the visualization tool are in the same Region, the data transfer between them doesn't incur the usual costs associated with data leaving the AWS network.

</details>

### 24. gh-246

A company runs a web application on Amazon EC2 instances in multiple Availability Zones. The EC2 instances are in private subnets. A solutions architect implements an internet-facing Application Load Balancer (ALB) and specifies the EC2 instances as the target group. However, the internet traffic is not reaching the EC2 instances.
How should the solutions architect reconfigure the architecture to resolve this issue?

<details><summary>Answer</summary>

**D. Create public subnets in each Availability Zone. Associate the public subnets with the ALB. Update the route tables for the public subnets with a route to the private subnets.**

This option involves creating public subnets for the ALB, allowing it to receive internet traffic. The EC2 instances can remain in private subnets. This approach follows the best practice of using public subnets for internet-facing components like ALBs.

</details>

### 25. gh-251

An Amazon EC2 instance is located in a private subnet in a new VPC. This subnet does not have outbound internet access, but the EC2 instance needs the ability to download monthly security updates from an outside vendor.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Create a NAT gateway, and place it in a public subnet. Configure the private subnet route table to use the NAT gateway as the default route.**

NAT gateways are designed to provide outbound internet access for instances in private subnets. Placing a NAT gateway in a public subnet and configuring the private subnet's route table to use the NAT gateway as the default route allows the EC2 instance to download security updates while maintaining security.

</details>

### 26. gh-254 `security`

A company is reviewing a recent migration of a three-tier application to a VPC. The security team discovers that the principle of least privilege is not being applied to Amazon EC2 security group ingress and egress rules between the application tiers.
What should a solutions architect do to correct this issue?

<details><summary>Answer</summary>

**B. Create security group rules using the security group ID as the source or destination.**

Using security group IDs allows for dynamic and flexible configuration. Referencing security groups directly in rules ensures that instances associated with those security groups, regardless of their individual IDs, are included. This approach aligns with the principle of least privilege and simplifies rule management.

</details>

### 27. gh-264

A company has a web application hosted over 10 Amazon EC2 instances with traffic directed by Amazon Route 53. The company occasionally experiences a timeout error when attempting to browse the application. The networking team finds that some DNS queries return IP addresses of unhealthy instances, resulting in the timeout error.
What should a solutions architect implement to overcome these timeout errors?

<details><summary>Answer</summary>

**D. Create an Application Load Balancer (ALB) with a health check in front of the EC2 instances. Route to the ALB from Route 53.**

By creating an ALB and configuring health checks, the architect ensures that only healthy instances receive traffic. The ALB periodically checks the health of the EC2 instances based on the configured health check settings.

Routing traffic to the ALB from Route 53 ensures that DNS queries return the IP address of the ALB instead of individual instances. This allows the ALB to distribute traffic only to healthy instances, avoiding timeouts caused by unhealthy instances.

</details>

### 28. gh-265 `availability` `security`

A solutions architect needs to design a highly available application consisting of web, application, and database tiers. HTTPS content delivery should be as close to the edge as possible, with the least delivery time.
Which solution meets these requirements and is MOST secure?

<details><summary>Answer</summary>

**C. Configure a public Application Load Balancer (ALB) with multiple redundant Amazon EC2 instances in private subnets. Configure Amazon CloudFront to deliver HTTPS content using the public ALB as the origin.**

Public ALB in Private Subnets:

Deploy a public Application Load Balancer (ALB) in private subnets. This ensures that the ALB is not directly accessible from the internet, providing an additional layer of security.

Deploy multiple redundant Amazon EC2 instances in private subnets behind the ALB. The instances host the application and database tiers.

Configure Amazon CloudFront to deliver HTTPS content using the public ALB as the origin. CloudFront provides content delivery close to the edge, reducing latency and improving the delivery time for end-users.

</details>

### 29. gh-272

A company serves a dynamic website from a fleet of Amazon EC2 instances behind an Application Load Balancer (ALB). The website needs to support multiple languages to serve customers around the world. The website’s architecture is running in the us-west-1 Region and is exhibiting high request latency for users that are located in other parts of the world.
The website needs to serve requests quickly and efficiently regardless of a user’s location. However, the company does not want to recreate the existing architecture across multiple Regions.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Configure an Amazon CloudFront distribution with the ALB as the origin. Set the cache behavior settings to cache based on the Accept-Language request header.**

</details>

### 30. gh-282

A company runs a web application that is deployed on Amazon EC2 instances in the private subnet of a VPC. An Application Load Balancer (ALB) that extends across the public subnets directs web traffic to the EC2 instances. The company wants to implement new security measures to restrict inbound traffic from the ALB to the EC2 instances while preventing access from any other source inside or outside the private subnet of the EC2 instances.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Configure the security group for the EC2 instances to only allow traffic that comes from the security group for the ALB.**

Security groups act as virtual firewalls for EC2 instances. By configuring the security group for the EC2 instances to only allow traffic from the security group associated with the ALB, you can control and restrict inbound traffic effectively.

When you specify a security group as the source in the inbound rules of another security group, you allow traffic only from instances that are members of that source security group. In this case, you can allow traffic only from the ALB, ensuring that traffic is restricted to the necessary source.

</details>

### 31. gh-294

An application that is hosted on Amazon EC2 instances needs to access an Amazon S3 bucket. Traffic must not traverse the internet.
How should a solutions architect configure access to meet these requirements?

<details><summary>Answer</summary>

**B. Set up a gateway VPC endpoint for Amazon S3 in the VPC.**

A VPC endpoint for Amazon S3 allows you to connect your VPC directly to S3 without traversing the internet. This ensures that traffic between your EC2 instances and the S3 bucket stays within the AWS network.

</details>

### 32. gh-296

A development team has launched a new application that is hosted on Amazon EC2 instances inside a development VPC. A solutions architect needs to create a new VPC in the same account. The new VPC will be peered with the development VPC. The VPC CIDR block for the development VPC is 192.168.0.0/24. The solutions architect needs to create a CIDR block for the new VPC. The CIDR block must be valid for a VPC peering connection to the development VPC.
What is the SMALLEST CIDR block that meets these requirements?

<details><summary>Answer</summary>

**D. 10.0.1.0/24**

This is a valid CIDR block that does not overlap with the existing development VPC (192.168.0.0/24).

Therefore, this is the SMALLEST CIDR block that meets the requirements.

</details>

### 33. gh-313

A company is building a mobile app on AWS. The company wants to expand its reach to millions of users. The company needs to build a platform so that authorized users can watch the company’s content on their mobile devices.
What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**C. Use Amazon CloudFront. Provide signed URLs to stream content.**

Amazon CloudFront: CloudFront is a content delivery network (CDN) service provided by AWS. It accelerates the delivery of content by caching it at edge locations globally, reducing latency for end-users.
Signed URLs: CloudFront supports the generation of signed URLs, which can be used to control access to content. You can create time-limited URLs with specific permissions, allowing only authorized users to access the content.

</details>

### 34. gh-352

A company is designing the network for an online multi-player game. The game uses the UDP networking protocol and will be deployed in eight AWS Regions. The network architecture needs to minimize latency and packet loss to give end users a high-quality gaming experience.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up AWS Global Accelerator with UDP listeners and endpoint groups in each Region.**

AWS Global Accelerator is designed to improve the availability and performance of applications by using static IP addresses (Anycast) and directing traffic over the AWS global network. It provides low-latency and high-performance routing, making it well-suited for applications with a global user base, such as multi-player games.

By setting up UDP listeners and endpoint groups in each Region with AWS Global Accelerator, you can efficiently route traffic to the nearest game servers, reducing latency and improving the overall gaming experience.

</details>

### 35. gh-357 `availability`

A gaming company is moving its public scoreboard from a data center to the AWS Cloud. The company uses Amazon EC2 Windows Server instances behind an Application Load Balancer to host its dynamic application. The company needs a highly available storage solution for the application. The application consists of static files and dynamic server-side code.
Which combination of steps should a solutions architect take to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Store the static files on Amazon S3. Use Amazon CloudFront to cache objects at the edge.**

D. Store the server-side code on Amazon FSx for Windows File Server. Mount the FSx for Windows File Server volume on each EC2 instance to share the files.

Amazon S3 is a highly scalable and durable object storage service, and it is well-suited for storing static files. Using CloudFront as a content delivery network (CDN) improves the delivery of static content by caching objects at edge locations, reducing latency for end users.

Amazon FSx for Windows File Server provides a fully managed Windows file system that is accessible from Windows-based EC2 instances. This is suitable for storing dynamic server-side code that requires file sharing across multiple instances. It offers high availability and supports Windows-native features.

</details>

### 36. gh-358 `least-ops`

A social media company runs its application on Amazon EC2 instances behind an Application Load Balancer (ALB). The ALB is the origin for an Amazon CloudFront distribution. The application has more than a billion images stored in an Amazon S3 bucket and processes thousands of images each second. The company wants to resize the images dynamically and serve appropriate formats to clients.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**C. Use a Lambda@Edge function with an external image management library. Associate the Lambda@Edge function with the CloudFront behaviors that serve the images.**

Lambda@Edge: Allows you to run code in response to CloudFront events without provisioning or managing servers. In this case, a Lambda@Edge function can be used to dynamically resize images based on the request.

External image management library: Since the company wants to minimize operational overhead, using an external image management library within a Lambda@Edge function is a good choice. This eliminates the need to manage EC2 instances or other infrastructure.

</details>

### 37. gh-360

A company uses Amazon API Gateway to run a private gateway with two REST APIs in the same VPC. The BuyStock RESTful web service calls the CheckFunds RESTful web service to ensure that enough funds are available before a stock can be purchased. The company has noticed in the VPC flow logs that the BuyStock RESTful web service calls the CheckFunds RESTful web service over the internet instead of through the VPC. A solutions architect must implement a solution so that the APIs communicate through the VPC.
Which solution will meet these requirements with the FEWEST changes to the code?

<details><summary>Answer</summary>

**B. Use an interface endpoint.**

Interface Endpoint (VPC Endpoint for API Gateway): An interface endpoint allows private connectivity to API Gateway within your VPC. By creating a VPC endpoint for API Gateway, you can ensure that the communication between the BuyStock and CheckFunds RESTful web services stays within the VPC, eliminating the need for traffic to go over the internet.

</details>

### 38. gh-366

367] A company is using Amazon Route 53 latency-based routing to route requests to its UDP-based application for users around the world. The application is hosted on redundant servers in the company's on-premises data centers in the United States, Asia, and Europe. The company’s compliance requirements state that the application must be hosted on premises. The company wants to improve the performance and availability of the application.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Configure three Network Load Balancers (NLBs) in the three AWS Regions to address the on-premises endpoints. Create an accelerator by using AWS Global Accelerator, and register the NLBs as its endpoints. Provide access to the application by using a CNAME that points to the accelerator DNS.**

This option suggests configuring three Network Load Balancers (NLBs) in the three AWS Regions to address on-premises endpoints. While AWS Global Accelerator is used, the NLBs are registered as its endpoints. This does not meet the requirement of hosting the application on premises.

</details>

### 39. gh-370

A company runs a public three-tier web application in a VPC. The application runs on Amazon EC2 instances across multiple Availability Zones. The EC2 instances that run in private subnets need to communicate with a license server over the internet. The company needs a managed solution that minimizes operational maintenance.
Which solution meets these requirements?

<details><summary>Answer</summary>

**C. Provision a NAT gateway in a public subnet. Modify each private subnet's route table with a default route that points to the NAT gateway.**

NAT Gateway: A NAT gateway is a managed service provided by AWS that allows EC2 instances in private subnets to initiate outbound traffic to the internet while preventing unsolicited inbound traffic from reaching those instances. NAT gateways are fully managed, highly available, and require minimal maintenance.

Public Subnet: Placing the NAT gateway in a public subnet allows it to have access to the internet, fulfilling the requirement for private instances to communicate with a license server over the internet.

Default Route: Modifying each private subnet's route table with a default route that points to the NAT gateway ensures that traffic from private instances is directed through the NAT gateway for outbound communication.

</details>

### 40. gh-374

A company is running several business applications in three separate VPCs within the us-east-1 Region. The applications must be able to communicate between VPCs. The applications also must be able to consistently send hundreds of gigabytes of data each day to a latency-sensitive application that runs in a single on-premises data center.
A solutions architect needs to design a network connectivity solution that maximizes cost-effectiveness.
Which solution meets these requirements?

<details><summary>Answer</summary>

**D. Set up one AWS Direct Connect connection from the data center to AWS. Create a transit gateway, and attach each VPC to the transit gateway. Establish connectivity between the Direct Connect connection and the transit gateway.**

AWS Direct Connect: Using a single AWS Direct Connect connection from the data center to AWS is more cost-effective than setting up multiple connections. It provides a dedicated and consistent network connection between the on-premises data center and AWS.

Transit Gateway: The use of a transit gateway simplifies network connectivity. It acts as a hub, allowing communication between the VPCs and the on-premises data center without requiring separate connections for each VPC. This reduces complexity and costs associated with managing multiple connections.

</details>

### 41. gh-385

A solutions architect is creating a new VPC design. There are two public subnets for the load balancer, two private subnets for web servers, and two private subnets for MySQL. The web servers use only HTTPS. The solutions architect has already created a security group for the load balancer allowing port 443 from 0.0.0.0/0. Company policy requires that each resource has the least access required to still be able to perform its tasks.
Which additional configuration strategy should the solutions architect use to meet these requirements?

<details><summary>Answer</summary>

**C. Create a security group for the web servers and allow port 443 from the load balancer. Create a security group for the MySQL servers and allow port 3306 from the web servers security group.**

</details>

### 42. gh-395

An IAM user made several configuration changes to AWS resources in their company's account during a production deployment last week. A solutions architect learned that a couple of security group rules are not configured as desired. The solutions architect wants to confirm which IAM user was responsible for making changes.
Which service should the solutions architect use to find the desired information?

<details><summary>Answer</summary>

**C. AWS CloudTrail**

AWS CloudTrail is a service provided by Amazon Web Services (AWS) that allows you to monitor and log AWS account activity. It records API calls made on your AWS account, capturing information such as the identity of the caller, the time of the API call, the source IP address, the request parameters, and the response elements returned by the AWS service.

</details>

### 43. gh-396

A company has implemented a self-managed DNS service on AWS. The solution consists of the following:
• Amazon EC2 instances in different AWS Regions
• Endpoints of a standard accelerator in AWS Global Accelerator
The company wants to protect the solution against DDoS attacks.
What should a solutions architect do to meet this requirement?

<details><summary>Answer</summary>

**A. Subscribe to AWS Shield Advanced. Add the accelerator as a resource to protect.**

AWS Shield Advanced is a managed Distributed Denial of Service (DDoS) protection service provided by AWS.
By subscribing to AWS Shield Advanced, you gain access to enhanced DDoS protection capabilities, including automatic detection and mitigation of DDoS attacks.

</details>

### 44. gh-408

A company runs an application that receives data from thousands of geographically dispersed remote devices that use UDP. The application processes the data immediately and sends a message back to the device if necessary. No data is stored.
The company needs a solution that minimizes latency for the data transmission from the devices. The solution also must provide rapid failover to another AWS Region.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use AWS Global Accelerator. Create a Network Load Balancer (NLB) in each of the two Regions as an endpoint. Create an Amazon Elastic Container Service (Amazon ECS) cluster with the Fargate launch type. Create an ECS service on the cluster. Set the ECS service as the target for the NLProcess the data in Amazon ECS.**

AWS Global Accelerator: AWS Global Accelerator provides static IP addresses that act as a fixed entry point to your application. It routes traffic over the AWS global network to the optimal AWS endpoint based on health, geography, and routing policies.

Network Load Balancer (NLB): NLB is well-suited for UDP-based traffic, and it's designed for high-performance, low-latency applications. In this case, it can efficiently handle the thousands of geographically dispersed remote devices sending UDP traffic.

Amazon ECS with Fargate Launch Type: Using ECS with Fargate allows you to deploy and run containers without managing the underlying infrastructure. This setup can efficiently handle the immediate processing of data without the need to manage the underlying servers.

</details>

### 45. gh-439 `least-ops`

A solutions architect configured a VPC that has a small range of IP addresses. The number of Amazon EC2 instances that are in the VPC is increasing, and there is an insufficient number of IP addresses for future workloads.
Which solution resolves this issue with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Add an additional IPv4 CIDR block to increase the number of IP addresses and create additional subnets in the VPC. Create new resources in the new subnets by using the new CIDR.**

By adding an additional IPv4 CIDR block to the existing VPC, you can effectively increase the number of available IP addresses within the same VPC.
Creating additional subnets using the new CIDR block allows you to organize your resources and maintain segmentation within the VPC.

</details>

### 46. gh-448

A company has two VPCs named Management and Production. The Management VPC uses VPNs through a customer gateway to connect to a single device in the data center. The Production VPC uses a virtual private gateway with two attached AWS Direct Connect connections. The Management and Production VPCs both use a single VPC peering connection to allow communication between the applications.
What should a solutions architect do to mitigate any single point of failure in this architecture?

<details><summary>Answer</summary>

**C. Add a second set of VPNs to the Management VPC from a second customer gateway device.**

Adding a second set of VPN connections from the Management VPC to a second customer gateway device provides redundancy and eliminates this single point of failure.

</details>

### 47. gh-450

A company has a three-tier web application that is in a single server. The company wants to migrate the application to the AWS Cloud. The company also wants the application to align with the AWS Well-Architected Framework and to be consistent with AWS recommended best practices for security, scalability, and resiliency.
Which combination of solutions will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**C. Create a VPC across two Availability Zones. Refactor the application to host the web tier, application tier, and database tier. Host each tier on its own private subnet with Auto Scaling groups for the web tier and application tier.**

This choice aligns with best practices by using separate subnets for each tier, allowing for better security and scalability. Auto Scaling groups provide elasticity and resiliency.

E. Use Elastic Load Balancers in front of the web tier. Control access by using security groups containing references to each layer's security groups.

This option introduces an Elastic Load Balancer (ELB) for the web tier, which enhances scalability and resiliency. Using security groups to control access adds an additional layer of security.

F. Use an Amazon RDS database Multi-AZ cluster deployment in private subnets. Allow database access only from application tier security groups.

This option leverages Amazon RDS for the database tier, utilizing Multi-AZ for high availability. Placing the RDS database in private subnets and restricting access to the application tier security groups enhances security.

</details>

### 48. gh-470

A company has applications hosted on Amazon EC2 instances with IPv6 addresses. The applications must initiate communications with other external applications using the internet. However the company’s security policy states that any external service cannot initiate a connection to the EC2 instances.
What should a solutions architect recommend to resolve this issue?

<details><summary>Answer</summary>

**D. Create an egress-only internet gateway and make it the destination of the subnet's route table.**

An egress-only internet gateway is used for IPv6 traffic leaving the VPC to reach the internet. It allows outbound communication initiated by resources inside the VPC but prevents incoming traffic initiated from the internet.
Configuring the subnet's route table to use the egress-only internet gateway as the destination ensures that IPv6 traffic initiated from EC2 instances can reach external services while blocking unsolicited incoming traffic.

</details>

### 49. gh-471

A company is creating an application that runs on containers in a VPC. The application stores and accesses data in an Amazon S3 bucket. During the development phase, the application will store and access 1 TB of data in Amazon S3 each day. The company wants to minimize costs and wants to prevent traffic from traversing the internet whenever possible.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a gateway VPC endpoint for Amazon S3. Associate this endpoint with all route tables in the VPC.**

</details>

### 50. gh-473

A company hosts a website on Amazon EC2 instances behind an Application Load Balancer (ALB). The website serves static content. Website traffic is increasing, and the company is concerned about a potential increase in cost.

<details><summary>Answer</summary>

**A. Create an Amazon CloudFront distribution to cache state files at edge locations**

By creating a CloudFront distribution and configuring it to cache static files, you can offload the delivery of static content to the CDN, reducing the load on the ALB and potentially lowering data transfer costs.
CloudFront helps improve website performance and can be cost-effective due to its caching mechanism.

</details>

### 51. gh-474

A company has multiple VPCs across AWS Regions to support and run workloads that are isolated from workloads in other Regions. Because of a recent application launch requirement, the company’s VPCs must communicate with all other VPCs across all Regions.
Which solution will meet these requirements with the LEAST amount of administrative effort?

<details><summary>Answer</summary>

**C. Use AWS Transit Gateway to manage VPC communication in a single Region and Transit Gateway peering across Regions to manage VPC communications.**

AWS Transit Gateway is designed for simplifying the connectivity between multiple VPCs and on-premises networks. It allows for hub-and-spoke connectivity patterns, making it easier to manage communication across multiple VPCs.
By using AWS Transit Gateway in a single Region to connect VPCs and enabling Transit Gateway peering across Regions, you can efficiently manage communication between VPCs in different Regions with centralized control and minimal administrative effort.

</details>

### 52. gh-480

A business application is hosted on Amazon EC2 and uses Amazon S3 for encrypted object storage. The chief information security officer has directed that no application traffic between the two services should traverse the public internet.
Which capability should the solutions architect use to meet the compliance requirements?

<details><summary>Answer</summary>

**B. VPC endpoint**

AWS provides VPC endpoints that allow you to privately connect your VPC to supported AWS services, including Amazon S3, without needing to use public IP addresses or traverse the public internet.
With an S3 VPC endpoint, the traffic between your Amazon EC2 instances and Amazon S3 remains within the AWS network, providing a secure and private connection.

</details>

### 53. gh-487 `availability`

A company seeks a storage solution for its application. The solution must be highly available and scalable. The solution also must function as a file system be mountable by multiple Linux instances in AWS and on premises through native protocols, and have no minimum size requirements. The company has set up a Site-to-Site VPN for access from its on-premises network to its VPC.
Which storage solution meets these requirements?

<details><summary>Answer</summary>

**C. Amazon Elastic File System (Amazon EFS) with multiple mount targets**

Amazon EFS is a scalable file storage service that can be mounted by multiple Amazon EC2 instances and on-premises servers.
It provides a shared file system with multiple mount targets in different Availability Zones (AZs) for high availability.
Multiple mount targets allow you to mount the file system from different subnets, ensuring that instances in different network segments can access the file system.

</details>

### 54. gh-499

A company needs to minimize the cost of its 1 Gbps AWS Direct Connect connection. The company's average connection utilization is less than 10%. A solutions architect must recommend a solution that will reduce the cost without compromising security.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Contact an AWS Direct Connect Partner to order a 200 Mbps hosted connection for an existing AWS account.**

</details>

### 55. gh-504

A company needs to connect several VPCs in the us-east-1 Region that span hundreds of AWS accounts. The company's networking team has its own AWS account to manage the cloud network.
What is the MOST operationally efficient solution to connect the VPCs?

<details><summary>Answer</summary>

**C. Create an AWS Transit Gateway in the networking team’s AWS account. Configure static routes from each VPC.**

AWS Transit Gateway: It is designed to simplify the connectivity between multiple VPCs. It acts as a central hub that allows you to connect multiple VPCs and on-premises networks. This approach reduces the complexity of managing peering connections individually.

</details>

### 56. gh-509

A company operates a two-tier application for image processing. The application uses two Availability Zones, each with one public subnet and one private subnet. An Application Load Balancer (ALB) for the web tier uses the public subnets. Amazon EC2 instances for the application tier use the private subnets.
Users report that the application is running more slowly than expected. A security audit of the web server log files shows that the application is receiving millions of illegitimate requests from a small number of IP addresses. A solutions architect needs to resolve the immediate performance problem while the company investigates a more permanent solution.
What should the solutions architect recommend to meet this requirement?

<details><summary>Answer</summary>

**B. Modify the network ACL for the web tier subnets. Add an inbound deny rule for the IP addresses that are consuming resources.**

</details>

### 57. gh-510 `security`

A global marketing company has applications that run in the ap-southeast-2 Region and the eu-west-1 Region. Applications that run in a VPC in eu-west-1 need to communicate securely with databases that run in a VPC in ap-southeast-2.
Which network design will meet these requirements?

<details><summary>Answer</summary>

**C. Configure a VPC peering connection between the ap-southeast-2 VPC and the eu-west-1 VPUpdate the subnet route tables. Create an inbound rule in the ap-southeast-2 database security group that allows traffic from the eu-west-1 application server IP addresses.**

VPC peering connections can be established between VPCs in different AWS Regions.
In this case, a VPC peering connection is set up between the VPC in ap-southeast-2 and the VPC in eu-west-1.

</details>

### 58. gh-514

A company is running a microservices application on Amazon EC2 instances. The company wants to migrate the application to an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for scalability. The company must configure the Amazon EKS control plane with endpoint private access set to true and endpoint public access set to false to maintain security compliance. The company must also put the data plane in private subnets. However, the company has received error notifications because the node cannot join the cluster.
Which solution will allow the node to join the cluster?

<details><summary>Answer</summary>

**B. Create interface VPC endpoints to allow nodes to access the control plane.**

When the Amazon EKS control plane has private access, nodes need to communicate with the control plane through interface VPC endpoints.
Creating interface VPC endpoints ensures that the nodes in private subnets can securely communicate with the EKS control plane without the need for public IP addresses.

</details>

### 59. gh-530

A company has an online gaming application that has TCP and UDP multiplayer gaming capabilities. The company uses Amazon Route 53 to point the application traffic to multiple Network Load Balancers (NLBs) in different AWS Regions. The company needs to improve application performance and decrease latency for the online game in preparation for user growth.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Add AWS Global Accelerator in front of the NLBs. Configure a Global Accelerator endpoint to use the correct listener ports.**

AWS Global Accelerator is a service that uses anycast IP addresses to route traffic over the AWS global network to optimal endpoints based on health, geography, and routing policies.

</details>

### 60. gh-532

A company has a workload in an AWS Region. Customers connect to and access the workload by using an Amazon API Gateway REST API. The company uses Amazon Route 53 as its DNS provider. The company wants to provide individual and secure URLs for all customers.
Which combination of steps will meet these requirements with the MOST operational efficiency? (Choose three.)

<details><summary>Answer</summary>

**A. Register the required domain in a registrar. Create a wildcard custom domain name in a Route 53 hosted zone and record in the zone that points to the API Gateway endpoint.**

D. Request a wildcard certificate that matches the custom domain name in AWS Certificate Manager (ACM) in the same Region.

F. Create a custom domain name in API Gateway for the REST API. Import the certificate from AWS Certificate Manager (ACM).

Registering the domain in a registrar and creating a wildcard custom domain name in Route 53 allows you to manage the DNS records efficiently. The DNS records can point to the API Gateway endpoint.

ACM provides a simple way to request and manage SSL/TLS certificates. Requesting a wildcard certificate for the custom domain ensures that it covers all subdomains, allowing for individual and secure URLs.

API Gateway allows you to create a custom domain name and associate it with your REST API. By importing a wildcard certificate from AWS Certificate Manager (ACM), you can secure the custom domain.

</details>

### 61. gh-538

A global video streaming company uses Amazon CloudFront as a content distribution network (CDN). The company wants to roll out content in a phased manner across multiple countries. The company needs to ensure that viewers who are outside the countries to which the company rolls out content are not able to view the content.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Add geographic restrictions to the content in CloudFront by using an allow list. Set up a custom error message.**

CloudFront allows you to set up geographic restrictions by creating an allow list. This allows you to specify the countries from which viewers are allowed to access your content. Viewers from countries not in the allow list will be restricted from accessing the content.

</details>

### 62. gh-544

A retail company uses a regional Amazon API Gateway API for its public REST APIs. The API Gateway endpoint is a custom domain name that points to an Amazon Route 53 alias record. A solutions architect needs to create a solution that has minimal effects on customers and minimal data loss to release the new version of APIs.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Create a canary release deployment stage for API Gateway. Deploy the latest API version. Point an appropriate percentage of traffic to the canary stage. After API verification, promote the canary stage to the production stage.**

A canary release deployment is a strategy in software development and release management where a new version of a software application or service is gradually rolled out to a small subset of users before making it available to the entire user base.

</details>

### 63. gh-545

A company wants to direct its users to a backup static error page if the company's primary website is unavailable. The primary website's DNS records are hosted in Amazon Route 53. The domain is pointing to an Application Load Balancer (ALB). The company needs a solution that minimizes changes and infrastructure overhead.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Set up a Route 53 active-passive failover configuration. Direct traffic to a static error page that is hosted in an Amazon S3 bucket when Route 53 health checks determine that the ALB endpoint is unhealthy.**

An active-passive failover configuration in Route 53 involves designating one endpoint (primary, in this case, the ALB) as active and another endpoint (S3 bucket hosting a static error page) as passive.
Route 53 health checks can be configured to monitor the health of the ALB endpoint. If the health checks determine that the ALB endpoint is unhealthy (i.e., the primary website is unavailable), Route 53 automatically directs traffic to the passive endpoint (S3 bucket with the static error page).

</details>

### 64. gh-549

A company has created a multi-tier application for its ecommerce website. The website uses an Application Load Balancer that resides in the public subnets, a web tier in the public subnets, and a MySQL cluster hosted on Amazon EC2 instances in the private subnets. The MySQL database needs to retrieve product catalog and pricing information that is hosted on the internet by a third-party provider. A solutions architect must devise a strategy that maximizes security without increasing operational overhead.
What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**B. Deploy a NAT gateway in the public subnets. Modify the private subnet route table to direct all internet-bound traffic to the NAT gateway.**

A NAT gateway is a fully managed service provided by AWS that allows instances in a private subnet to initiate outbound traffic to the internet while preventing inbound traffic from reaching those instances. It simplifies the process of enabling internet access for instances in private subnets without the need for managing a separate NAT instance.

</details>

### 65. gh-555

A company runs an application in a VPC with public and private subnets. The VPC extends across multiple Availability Zones. The application runs on Amazon EC2 instances in private subnets. The application uses an Amazon Simple Queue Service (Amazon SQS) queue.
A solutions architect needs to design a secure solution to establish a connection between the EC2 instances and the SQS queue.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Implement an interface VPC endpoint for Amazon SQS. Configure the endpoint to use the private subnets. Add to the endpoint a security group that has an inbound access rule that allows traffic from the EC2 instances that are in the private subnets.**

Interface VPC endpoints are used for services that are accessed over the Internet, and in this case, it's Amazon SQS. By implementing an interface VPC endpoint for SQS, you can ensure that the traffic stays within the Amazon network.

</details>

### 66. gh-558 `cost`

A company has two VPCs that are located in the us-west-2 Region within the same AWS account. The company needs to allow network traffic between these VPCs. Approximately 500 GB of data transfer will occur between the VPCs each month.
What is the MOST cost-effective solution to connect these VPCs?

<details><summary>Answer</summary>

**C. Set up a VPC peering connection between the VPCs. Update the route tables of each VPC to use the VPC peering connection for inter-VPC communication.**

VPC peering allows communication between VPCs within the same AWS account. It is a cost-effective solution, especially when the VPCs are located in the same region. In this case, both VPCs are in the us-west-2 region.

</details>

### 67. gh-577

A company uses an Amazon CloudFront distribution to serve content pages for its website. The company needs to ensure that clients use a TLS certificate when accessing the company's website. The company wants to automate the creation and renewal of the TLS certificates.
Which solution will meet these requirements with the MOST operational efficiency?

<details><summary>Answer</summary>

**C. Use AWS Certificate Manager (ACM) to create a certificate. Use DNS validation for the domain.**

AWS Certificate Manager (ACM): ACM is a fully managed service that allows you to easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources. It is designed for automation and ease of use.

DNS Validation: DNS validation involves adding a DNS record to your domain's DNS configuration. This method is more suitable for automation as it does not require manual intervention, and it can be easily integrated into automated certificate issuance and renewal processes.

</details>

### 68. gh-582

An ecommerce company uses Amazon Route 53 as its DNS provider. The company hosts its website on premises and in the AWS Cloud. The company's on-premises data center is near the us-west-1 Region. The company uses the eu-central-1 Region to host the website. The company wants to minimize load time for the website as much as possible.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Set up a geolocation routing policy. Send the traffic that is near us-west-1 to the on-premises data center. Send the traffic that is near eu-central-1 to eu-central-1.**

Geolocation routing directs traffic based on the geographic location of the user. This option would send users near us-west-1 to the on-premises data center and users near eu-central-1 to eu-central-1. While this approach considers geographic location, it might not always result in the lowest latency.

</details>

### 69. gh-600

A company is planning to migrate a TCP-based application into the company's VPC. The application is publicly accessible on a nonstandard TCP port through a hardware appliance in the company's data center. This public endpoint can process up to 3 million requests per second with low latency. The company requires the same level of performance for the new public endpoint in AWS.
What should a solutions architect recommend to meet this requirement?

<details><summary>Answer</summary>

**A. Deploy a Network Load Balancer (NLB). Configure the NLB to be publicly accessible over the TCP port that the application requires.**

Network Load Balancer (NLB): It operates at the connection level (Layer 4) and is well-suited for TCP traffic. It can handle millions of requests per second with minimal latency.
NLB allows you to configure the listener for the specific TCP port that the application requires, ensuring compatibility with the nonstandard TCP port used by the application.

</details>

### 70. gh-610

A company deploys Amazon EC2 instances that run in a VPC. The EC2 instances load source data into Amazon S3 buckets so that the data can be processed in the future. According to compliance laws, the data must not be transmitted over the public internet. Servers in the company's on-premises data center will consume the output from an application that runs on the EC2 instances.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Deploy a gateway VPC endpoint for Amazon S3. Set up an AWS Direct Connect connection between the on-premises network and the VPC.**

A gateway VPC endpoint allows communication between resources in your VPC and Amazon S3 without traversing the public internet.
AWS Direct Connect provides a dedicated network connection from the on-premises data center to the VPC. This dedicated connection enhances security and ensures a reliable and consistent connection between on-premises servers and the EC2 instances in the VPC.

</details>

### 71. gh-612

A company has an application that runs on Amazon EC2 instances in a private subnet. The application needs to process sensitive information from an Amazon S3 bucket. The application must not use the internet to connect to the S3 bucket.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Configure a VPC endpoint. Update the S3 bucket policy to allow access from the VPC endpoint. Update the application to use the new VPC endpoint.**

VPC Endpoint for S3: A VPC endpoint allows you to privately connect your VPC to supported AWS services, including Amazon S3, without traversing the public internet. This ensures secure and direct access to S3 from within your VPC.

</details>

### 72. gh-625

A company is hosting a website behind multiple Application Load Balancers. The company has different distribution rights for its content around the world. A solutions architect needs to ensure that users are served the correct content without violating distribution rights.
Which configuration should the solutions architect choose to meet these requirements?

<details><summary>Answer</summary>

**C. Configure Amazon Route 53 with a geolocation policy**

Geolocation routing in Amazon Route 53 allows you to route traffic based on the geographic location of the user.
You can create different records for your website content and associate them with specific geographic locations. This way, users from different regions will be directed to the appropriate servers or load balancers hosting the content that adheres to the distribution rights for that region.

</details>

### 73. gh-627

A company wants to migrate two DNS servers to AWS. The servers host a total of approximately 200 zones and receive 1 million requests each day on average. The company wants to maximize availability while minimizing the operational overhead that is related to the management of the two servers.
What should a solutions architect recommend to meet these requirements?

<details><summary>Answer</summary>

**A. Create 200 new hosted zones in the Amazon Route 53 console Import zone files.**

Amazon Route 53 is a highly available and scalable domain name system (DNS) web service provided by AWS.
By creating 200 new hosted zones in the Amazon Route 53 console and importing the existing zone files, you can take advantage of the fully managed and highly available nature of Route 53 without the need to manage servers.

</details>

### 74. gh-639

A company is building a new furniture inventory application. The company has deployed the application on a fleet ofAmazon EC2 instances across multiple Availability Zones. The EC2 instances run behind an Application Load Balancer (ALB) in their VPC.
A solutions architect has observed that incoming traffic seems to favor one EC2 instance, resulting in latency for some requests.
What should the solutions architect do to resolve this issue?

<details><summary>Answer</summary>

**A. Disable session affinity (sticky sessions) on the ALB**

Session affinity, also known as sticky sessions, directs a client's requests to the same EC2 instance, based on the client's session information. While sticky sessions can be useful in some scenarios, they can lead to uneven distribution of traffic, causing latency for some requests if one EC2 instance is overloaded.

</details>

### 75. gh-657 `cost`

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

### 76. gh-663

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

### 77. gh-676

A company's application uses Network Load Balancers, Auto Scaling groups, Amazon EC2 instances, and databases that are deployed in an
Amazon VPC. The company wants to capture information about tra c to and from the network interfaces in near real time in its Amazon VPC. The
company wants to send the information to Amazon OpenSearch Service for analysis.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Use VPC Flow Logs → CloudWatch → Kinesis Firehose → OpenSearch.**

Flow Logs capture traffic; Firehose streams to OpenSearch.
CloudTrail (Options C/D) logs API calls, not network traffic.

</details>
