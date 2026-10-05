# Resilience and disaster recovery

7 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. gh-230 `availability`

A company is concerned that two NAT instances in use will no longer be able to support the traffic needed for the company’s application. A solutions architect wants to implement a solution that is highly available, fault tolerant, and automatically scalable.
What should the solutions architect recommend?

<details><summary>Answer</summary>

**C. Remove the two NAT instances and replace them with two NAT gateways in different Availability Zones.**

NAT Gateway: NAT Gateways are managed, highly available, and scalable components provided by AWS. They are designed to handle the network address translation for instances in private subnets. By deploying NAT gateways in different Availability Zones, you ensure high availability.

Benefits of NAT Gateway:
Managed Service: NAT Gateway is a fully managed service, reducing operational overhead.
High Availability: Deploying NAT gateways in different Availability Zones ensures fault tolerance and high availability.
Automatically Scalable: NAT Gateways automatically scale based on the traffic volume, eliminating the need for manual adjustments.

</details>

### 2. gh-274

A company runs an application on Amazon EC2 instances. The company needs to implement a disaster recovery (DR) solution for the application. The DR solution needs to have a recovery time objective (RTO) of less than 4 hours. The DR solution also needs to use the fewest possible AWS resources during normal operations.
Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create Amazon Machine Images (AMIs) to back up the EC2 instances. Copy the AMIs to a secondary AWS Region. Automate infrastructure deployment in the secondary Region by using AWS CloudFormation.**

By creating Amazon Machine Images (AMIs) to back up the EC2 instances and copying them to a secondary AWS Region, the company can ensure that they have a reliable backup in the event of a disaster. By using AWS CloudFormation to automate infrastructure deployment in the secondary Region, the company can minimize the amount of time and effort required to set up the DR solution.

</details>

### 3. gh-326 `availability`

An image hosting company uploads its large assets to Amazon S3 Standard buckets. The company uses multipart upload in parallel by using S3 APIs and overwrites if the same object is uploaded again. For the first 30 days after upload, the objects will be accessed frequently. The objects will be used less frequently after 30 days, but the access patterns for each object will be inconsistent. The company must optimize its S3 storage costs while maintaining high availability and resiliency of stored assets.
Which combination of actions should a solutions architect recommend to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Move assets to S3 Intelligent-Tiering after 30 days.**

B. Configure an S3 Lifecycle policy to clean up incomplete multipart uploads.

Move assets to S3 Intelligent-Tiering after 30 days: This option is suitable for objects with unknown or changing access patterns. S3 Intelligent-Tiering automatically moves objects between two access tiers (frequent and infrequent access) based on changing access patterns. It helps optimize costs by automatically selecting the most cost-effective tier for each object.

Configure an S3 Lifecycle policy to clean up incomplete multipart uploads: This is a good practice to clean up any incomplete multipart uploads, which can consume additional storage space without contributing to the actual objects. Cleaning up incomplete uploads helps manage storage costs efficiently.

</details>

### 4. gh-356 `availability`

A company stores its data objects in Amazon S3 Standard storage. A solutions architect has found that 75% of the data is rarely accessed after 30 days. The company needs all the data to remain immediately accessible with the same high availability and resiliency, but the company wants to minimize storage costs.
Which storage solution will meet these requirements?

<details><summary>Answer</summary>

**B. Move the data objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.**

S3 Standard-Infrequent Access (S3 Standard-IA): This storage class is designed for infrequently accessed data but still provides low-latency and high-throughput performance. It maintains the same high availability and durability as S3 Standard, making it suitable for data that is accessed less frequently.

</details>

### 5. gh-447

A company has a stateless web application that runs on AWS Lambda functions that are invoked by Amazon API Gateway. The company wants to deploy the application across multiple AWS Regions to provide Regional failover capabilities.
What should a solutions architect do to route traffic to multiple Regions?

<details><summary>Answer</summary>

**A. Create Amazon Route 53 health checks for each Region. Use an active-active failover configuration.**

By creating Amazon Route 53 health checks for each Region and configuring an active-active failover configuration, Route 53 can monitor the health of the endpoints in each Region and route traffic to healthy endpoints. In the event of a failure in one Region, Route 53 automatically routes traffic to the healthy endpoints in other Regions.

</details>

### 6. gh-585

A solutions architect is designing a disaster recovery (DR) strategy to provide Amazon EC2 capacity in a failover AWS Region. Business requirements state that the DR strategy must meet capacity in the failover Region.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Purchase a Capacity Reservation in the failover Region.**

A Capacity Reservation allows you to reserve a specific amount of EC2 instance capacity in a given region without purchasing specific instances. This reserved capacity is dedicated to your account and can be utilized for launching instances when needed. Capacity Reservations offer flexibility, allowing you to launch different instance types and sizes within the reserved capacity.

</details>

### 7. gh-647 `availability`

A gaming company is building an application with Voice over IP capabilities. The application will serve traffic to users across the world. The application needs to be highly available with an automated failover across AWS Regions. The company wants to minimize the latency of users without relying on IP address caching on user devices.
What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Global Accelerator with health checks.**

AWS Global Accelerator is a service that provides static IP addresses (Anycast) to route traffic over the AWS global network. It routes traffic over the optimal path to the AWS endpoint, improving availability and performance.

</details>
