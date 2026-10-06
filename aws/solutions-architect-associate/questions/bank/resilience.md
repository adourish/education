# Resilience and disaster recovery

20 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-28

In the Launch Db Instance Wizard, where can I select the backup and maintenance options?

<details><summary>Answer</summary>

**C. Under MANAGEMENT OPTIONS.**

</details>

### 2. dt-52

You can modify the backup retention period; valid values are 0 (for no backup retention) to a maximum of [...] days.

<details><summary>Answer</summary>

**B. 35.**

</details>

### 3. dt-81

A major customer has asked you to set up his AWS infrastructure so that it will be easy to recover in the case of a disaster of some sort. Which of the following is important when thinking about being able to quickly launch resources in AWS to ensure business continuity in case of a disaster?

<details><summary>Answer</summary>

**C. All items listed here are important when thinking about disaster recovery.**

</details>

### 4. dt-211

Changes to the backup window take effect [...].

<details><summary>Answer</summary>

**C. immediately.**

</details>

### 5. dt-230

You are responsible for a legacy web application whose server environment is approaching end of life. You would like to migrate this application to AWS as quickly as possible, since the application environment currently has the following limitations. The VM's single 10GB VMDK is almost full. The virtual network interface still uses the 10Mbps driver, which leaves your 100Mbps WAN connection completely underutilized. It is currently running on a highly customized Windows VM within a VMware environment. You do not have the installation media. This is a mission critical application with an RTO (Recovery Time Objective) of 8 hours and RPO (Recovery Point Objective) of 1 hour. How could you best migrate this application to AWS while meeting your business continuity requirements?

<details><summary>Answer</summary>

**A. Use the EC2 VM Import Connector for vCenter to import the VM into EC2.**

</details>

### 6. q-230 `availability`

A company is concerned that two NAT instances in use will no longer be able to support the traffic needed for the company’s application. A solutions architect wants to implement a solution that is highly available, fault tolerant, and automatically scalable. What should the solutions architect recommend?

<details><summary>Answer</summary>

**C. Remove the two NAT instances and replace them with two NAT gateways in different Availability Zones.**

NAT Gateway: NAT Gateways are managed, highly available, and scalable components provided by AWS. They are designed to handle the network address translation for instances in private subnets. By deploying NAT gateways in different Availability Zones, you ensure high availability.  Benefits of NAT Gateway: Managed Service: NAT Gateway is a fully managed service, reducing operational overhead. High Availability: Deploying NAT gateways in different Availability Zones ensures fault tolerance and high availability. Automatically Scalable: NAT Gateways automatically scale based on the traffic volume, eliminating the need for manual adjustments.

</details>

### 7. dt-234

To ensure failover capabilities, consider using a [...] for incoming traffic on a network interface.

<details><summary>Answer</summary>

**B. secondary private IP.**

</details>

### 8. dt-255

An ERP application is deployed across multiple AZs in a single region. In the event of failure, the Recovery Time Objective (RTO) must be less than 3 hours, and the Recovery Point Objective (RPO) must be 15 minutes. The customer realizes that data corruption occurred roughly 1.5 hours ago. What DR strategy could be used to achieve this RTO and RPO in the event of this kind of failure?

<details><summary>Answer</summary>

**A. Take hourly DB backups to S3, with transaction logs stored in S3 every 5 minutes.**

</details>

### 9. q-274

A company runs an application on Amazon EC2 instances. The company needs to implement a disaster recovery (DR) solution for the application. The DR solution needs to have a recovery time objective (RTO) of less than 4 hours. The DR solution also needs to use the fewest possible AWS resources during normal operations. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**B. Create Amazon Machine Images (AMIs) to back up the EC2 instances. Copy the AMIs to a secondary AWS Region. Automate infrastructure deployment in the secondary Region by using AWS CloudFormation.**

By creating Amazon Machine Images (AMIs) to back up the EC2 instances and copying them to a secondary AWS Region, the company can ensure that they have a reliable backup in the event of a disaster. By using AWS CloudFormation to automate infrastructure deployment in the secondary Region, the company can minimize the amount of time and effort required to set up the DR solution.

</details>

### 10. dt-291

Your manager has just given you access to multiple VPN connections that someone else has recently set up between all your company's offices. She needs you to make sure that the communication between the VPNs is secure. Which of the following services would be best for providing a low-cost hub-and-spoke model for primary or backup connectivity between these remote offices?

<details><summary>Answer</summary>

**D. AWS VPN CloudHub.**

</details>

### 11. q-326 `availability`

An image hosting company uploads its large assets to Amazon S3 Standard buckets. The company uses multipart upload in parallel by using S3 APIs and overwrites if the same object is uploaded again. For the first 30 days after upload, the objects will be accessed frequently. The objects will be used less frequently after 30 days, but the access patterns for each object will be inconsistent. The company must optimize its S3 storage costs while maintaining high availability and resiliency of stored assets. Which combination of actions should a solutions architect recommend to meet these requirements? (Choose two.)

<details><summary>Answer</summary>

**A. Move assets to S3 Intelligent-Tiering after 30 days.**

B. Configure an S3 Lifecycle policy to clean up incomplete multipart uploads.  Move assets to S3 Intelligent-Tiering after 30 days: This option is suitable for objects with unknown or changing access patterns. S3 Intelligent-Tiering automatically moves objects between two access tiers (frequent and infrequent access) based on changing access patterns. It helps optimize costs by automatically selecting the most cost-effective tier for each object.  Configure an S3 Lifecycle policy to clean up incomplete multipart uploads: This is a good practice to clean up any incomplete multipart uploads, which can consume additional storage space without contributing to the actual objects. Cleaning up incomplete uploads helps manage storage costs efficiently.

</details>

### 12. dt-353

Your company currently has a 2-tier web application running in an on-premises data center. You have experienced several infrastructure failures in the past two months resulting in significant financial losses. Your CIO is strongly agreeing to move the application to AWS. While working on achieving buy-in from the other company executives, he asks you to develop a disaster recovery plan to help improve Business continuity in the short term. He specifies a target Recovery Time Objective (RTO) of 4 hours and a Recovery Point Objective (RPO) of 1 hour or less. He also asks you to implement the solution within 2 weeks. Your database is 200GB in size and you have a 20Mbps Internet connection. How would you do this while minimizing costs?

<details><summary>Answer</summary>

**A. Create an EBS backed private AMI which includes a fresh install of your application. Develop a CloudFormation template which includes your AMI and the required EC2, AutoScaling, and ELB resources to support deploying the application across Multiple Availability Zones. Asynchronously replicate transactions from your on-premises database to a database instance in AWS across a secure VPN connection.**

</details>

### 13. q-356 `availability`

A company stores its data objects in Amazon S3 Standard storage. A solutions architect has found that 75% of the data is rarely accessed after 30 days. The company needs all the data to remain immediately accessible with the same high availability and resiliency, but the company wants to minimize storage costs. Which storage solution will meet these requirements?

<details><summary>Answer</summary>

**B. Move the data objects to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 days.**

S3 Standard-Infrequent Access (S3 Standard-IA): This storage class is designed for infrequently accessed data but still provides low-latency and high-throughput performance. It maintains the same high availability and durability as S3 Standard, making it suitable for data that is accessed less frequently.

</details>

### 14. dt-433

Having set up a website to automatically be redirected to a backup website if it fails, you realize that there are different types of failovers that are possible. You need all your resources to be available the majority of the time. Using Amazon Route 53 which configuration would best suit this requirement?

<details><summary>Answer</summary>

**A. Active-active failover.**

</details>

### 15. q-447

A company has a stateless web application that runs on AWS Lambda functions that are invoked by Amazon API Gateway. The company wants to deploy the application across multiple AWS Regions to provide Regional failover capabilities. What should a solutions architect do to route traffic to multiple Regions?

<details><summary>Answer</summary>

**A. Create Amazon Route 53 health checks for each Region. Use an active-active failover configuration.**

By creating Amazon Route 53 health checks for each Region and configuring an active-active failover configuration, Route 53 can monitor the health of the endpoints in each Region and route traffic to healthy endpoints. In the event of a failure in one Region, Route 53 automatically routes traffic to the healthy endpoints in other Regions.

</details>

### 16. dt-552 `availability`

A user has created an ELB with the Availability Zone US-East-1A. The user wants to add more zones to ELB to achieve High Availability. How can the user add more zones to the existing ELB?

<details><summary>Answer</summary>

**D. The user can add zones on the fly from the AWS console.**

</details>

### 17. dt-553

Amazon SWF is designed to help users …

<details><summary>Answer</summary>

**D. Coordinate synchronous and asynchronous tasks which are distributed and fault tolerant.**

</details>

### 18. dt-582

Prior to the introduction of this function, the HA feature provided redundancy and performance, but required that a failed/lost group member be [...] reinstated.

<details><summary>Answer</summary>

**C. manually.**

</details>

### 19. q-585

A solutions architect is designing a disaster recovery (DR) strategy to provide Amazon EC2 capacity in a failover AWS Region. Business requirements state that the DR strategy must meet capacity in the failover Region. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Purchase a Capacity Reservation in the failover Region.**

An On-Demand Capacity Reservation holds EC2 capacity for your account in one Availability Zone for a stated instance type, platform and tenancy, and that capacity stays held whether or not you have instances running in it, so it is there when you declare a disaster and fail over. Because it is pinned that tightly, you must create the reservation for the exact instance types and the exact AZ your DR plan will launch into, and you pay the On-Demand rate for the reserved capacity for as long as it exists. The key distinction the question is testing: Savings Plans and regional Reserved Instances are billing discounts and reserve no capacity at all, so they cannot guarantee a failover launch will succeed. If you want the discount as well, a Capacity Reservation can be combined with a Savings Plan or a Reserved Instance, which then applies to the reserved capacity's charges.

</details>

### 20. q-647 `availability`

A gaming company is building an application with Voice over IP capabilities. The application will serve traffic to users across the world. The application needs to be highly available with an automated failover across AWS Regions. The company wants to minimize the latency of users without relying on IP address caching on user devices. What should a solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**A. Use AWS Global Accelerator with health checks.**

AWS Global Accelerator is a service that provides static IP addresses (Anycast) to route traffic over the AWS global network. It routes traffic over the optimal path to the AWS endpoint, improving availability and performance.

</details>
