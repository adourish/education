# Unclassified — review and tag by hand

63 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-36

You need to quickly set up an email-sending service because a client needs to start using it in the next hour. Amazon Simple Email Service (Amazon SES) seems to be the logical choice but there are several options available to set it up. Which of the following options to set up SES would best meet the needs of the client?

<details><summary>Answer</summary>

**A. Amazon SES console.**

</details>

### 2. dt-44

For each DB Instance class, what is the maximum size of associated storage capacity?

<details><summary>Answer</summary>

**B. 1TB.**

</details>

### 3. dt-46

What does specifying the mapping /dev/sdc=none when launching an instance do?

<details><summary>Answer</summary>

**D. Prevents /dev/sdc from attaching to the instance.**

</details>

### 4. dt-60

HTTP Query-based requests are HTTP requests that use the HTTP verb GET or POST and a Query parameter named [...].

<details><summary>Answer</summary>

**A. Action.**

</details>

### 5. dt-68

You are using Amazon SES as an email solution but are unsure of what its limitations are. Which statement below is correct in regards to that?

<details><summary>Answer</summary>

**D. Every Amazon SES sender has a unique set of sending limits.**

</details>

### 6. dt-70

What does a 'Domain' refer to in Amazon SWF?

<details><summary>Answer</summary>

**C. A collection of related Workflows.**

</details>

### 7. dt-88

You have multiple VPN connections and want to provide secure communication between sites using the AWS VPN CloudHub. Which statement is the most accurate in describing what you must do to set this up correctly?

<details><summary>Answer</summary>

**A. Create a virtual private gateway with multiple customer gateways, each with unique Border Gateway Protocol (BGP) Autonomous System Numbers (ASNs).**

</details>

### 8. dt-96

If I want my instance to run on a single-tenant hardware, which value do I have to set the instance's tenancy attribute to?

<details><summary>Answer</summary>

**A. Dedicated.**

</details>

### 9. dt-97

Can the string value of 'Key' be prefixed with :aws:'?

<details><summary>Answer</summary>

**D. No.**

</details>

### 10. dt-101

What is the maximum write throughput I can provision for a single Dynamic DB table?

<details><summary>Answer</summary>

**C. Dynamic DB is designed to scale without limits, but if you go beyond 10,000 you have to contact AWS first.**

</details>

### 11. dt-115

A group can contain many users. Can a user belong to multiple groups?

<details><summary>Answer</summary>

**A. Yes always.**

</details>

### 12. dt-116

Does Dynamo DB support in-place atomic updates?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 13. dt-118

You want to establish a dedicated network connection from your premises to AWS in order to save money by transferring data directly to AWS rather than through your internet service provider. You are sure there must be some other benefits beyond cost savings. Which of the following statements would be the best choice to put your client's mind at rest?

<details><summary>Answer</summary>

**C. Different instances running on the same physical machine are isolated from each other via the Xen hypervisor.**

</details>

### 14. dt-119

Can I detach the primary (ethO) network interface when the instance is running or stopped?

<details><summary>Answer</summary>

**B. No. You cannot.**

</details>

### 15. dt-126

If I modify a DB Instance or the DB parameter group associated with the instance, should I reboot the instance for the changes to take effect?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 16. dt-135

What is the reason for this?

<details><summary>Answer</summary>

**C. Public (IPV4) internet addresses are a scarce resource.**

</details>

### 17. dt-136

Can a 'user' be associated with multiple AWS accounts?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 18. q-144

A company wants to provide users with access to AWS resources. The company has 1,500 users and manages their access to on-premises resources through Active Directory user groups on the corporate network. However, the company does not want users to have to maintain another identity to access the resources. A solutions architect must manage user access to the AWS resources while preserving access to the on-premises resources. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Configure Security Assertion Markup Language (SAML) 2.0-based federation. Create roles with the appropriate policies attached. Map the roles to the Active Directory groups.**

The most appropriate solution is to configure SAML 2.0-based federation. This allows the company to use its existing on-premises Active Directory as an Identity Provider (IdP) to grant users access to AWS, which acts as the Service Provider (SP). Users authenticate with their corporate credentials, and the IdP sends a SAML assertion to AWS. AWS then provides temporary security credentials, allowing the user to assume an IAM role. By mapping Active Directory groups to specific IAM roles, the company can centrally manage permissions using their existing group structures, fulfilling the requirement to avoid creating and managing separate identities for each user in AWS. Why Incorrect Options are Wrong: A. Creating an IAM user for each of the 1,500 users directly contradicts the requirement that users should not have to maintain another identity. It also creates significant administrative ov

</details>

### 19. dt-153

True or False: Common points of failures like generators and cooling equipment are shared across Availability Zones.

<details><summary>Answer</summary>

**B. False.**

</details>

### 20. dt-156

Is there a limit to how many groups a user can be in?

<details><summary>Answer</summary>

**A. Yes for all users.**

</details>

### 21. dt-157

Which is the default region in AWS?

<details><summary>Answer</summary>

**B. us-east-1.**

</details>

### 22. dt-161

Is there a limit to the number of groups you can have?

<details><summary>Answer</summary>

**D. Yes for all users.**

</details>

### 23. dt-162

True or False: Automated backups are enabled by default for a new DB Instance

<details><summary>Answer</summary>

**A. True.**

</details>

### 24. dt-167

True or False: Provisioned IOPS Costs - you are charged for the IOPS and storage whether or not you use them in a given month.

<details><summary>Answer</summary>

**A. True.**

</details>

### 25. dt-176

What is the maximum key length of a tag?

<details><summary>Answer</summary>

**D. 128 Unicode characters.**

</details>

### 26. dt-179

Are penetration tests allowed as long as they are limited to the customer's instances?

<details><summary>Answer</summary>

**D. Yes, they are allowed but only with approval.**

</details>

### 27. dt-191

What are the four levels of AWS Premium Support?

<details><summary>Answer</summary>

**A. Basic, Developer, Business, Enterprise.**

</details>

### 28. dt-192

What is the default maximum number of Access Keys per user?

<details><summary>Answer</summary>

**C. 2.**

</details>

### 29. dt-193

In the most recent company meeting, your CEO focused on the fact that everyone in the organization needs to make sure that all of the infrastructure that is built is truly scalable. Which of the following statements is incorrect in reference to scalable architecture?

<details><summary>Answer</summary>

**C. A scalable architecture won't be cost effective as it grows.**

</details>

### 30. dt-212

Location of Instances are [...].

<details><summary>Answer</summary>

**B. based on Availability Zone.**

</details>

### 31. q-233

A solutions architect has created a new AWS account and must secure AWS account root user access. Which combination of actions will accomplish this? (Choose two.)

<details><summary>Answer</summary>

**A. Ensure the root user uses a strong password.**

B. Enable multi-factor authentication to the root user.  Using a strong, complex password for the root user is a fundamental security practice. This helps protect the account from unauthorized access. Enabling MFA adds an additional layer of security. Even if someone manages to obtain the root user's password, they would still need the second factor (e.g., a mobile device or hardware token) to successfully authenticate.

</details>

### 32. dt-237

Which of the below statements would be an incorrect response to your customers enquiry?

<details><summary>Answer</summary>

**C. Every packet sent in the AWS network uses Internet Protocol Security (IPsec).**

</details>

### 33. dt-242

Your supervisor has asked you to build a simple file synchronization service for your department. He doesn't want to spend too much money and he wants to be notified of any changes to files by email. What do you think would be the best Amazon service to use for the email solution?

<details><summary>Answer</summary>

**A. Amazon SES.**

</details>

### 34. dt-247

What is the command line instruction for running the remote desktop client in Windows?

<details><summary>Answer</summary>

**B. mstsc.**

</details>

### 35. dt-249

What is the charge for the data transfer incurred in replicating data between your primary and standby?

<details><summary>Answer</summary>

**C. No charge. It is free.**

</details>

### 36. dt-251

Resources that are created in AWS are identified by a unique identifier called an

<details><summary>Answer</summary>

**C. Amazon Resource Name.**

</details>

### 37. dt-263

Can I test my DB Instance against a new version before upgrading?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 38. dt-270

The base URI for all requests for instance metadata is [...].

<details><summary>Answer</summary>

**D. <http://169.254.169.254/latest/>.**

</details>

### 39. dt-272

A user is planning to launch a scalable web application. Which of the below mentioned options will not affect the latency of the application?

<details><summary>Answer</summary>

**B. Provisioned IOPS.**

</details>

### 40. dt-279

A, [...] is an individual, system, or application that interacts with AWS programmatically.

<details><summary>Answer</summary>

**A. user.**

</details>

### 41. dt-303

Which of the following will cause an immediate DB instance reboot to occur?

<details><summary>Answer</summary>

**A. You change storage type from standard to PIOPS, and Apply Immediately is set to true.**

</details>

### 42. dt-332

What does Amazon SWF stand for?

<details><summary>Answer</summary>

**B. Simple Work Flow.**

</details>

### 43. dt-338

A [...] is a storage device that moves data in sequences of bytes or bits (blocks).

<details><summary>Answer</summary>

**D. block device.**

</details>

### 44. dt-356

Can the string value of 'Key' be prefixed with laws?

<details><summary>Answer</summary>

**A. No.**

</details>

### 45. dt-370

You must increase storage size in increments of at least [...].

<details><summary>Answer</summary>

**D. 10.**

</details>

### 46. dt-371

You need to set up a security certificate for a client's e-commerce website as it will use the HTTPS protocol. Which of the below AWS services do you need to access to manage your SSL server certificate?

<details><summary>Answer</summary>

**B. AWS Identity & Access Management.**

</details>

### 47. dt-383

What are the two permission types used by AWS?

<details><summary>Answer</summary>

**D. User-based and Resource-based.**

</details>

### 48. dt-392

What is the maximum response time for a Business level Premium Support case?

<details><summary>Answer</summary>

**B. 1 hour.**

</details>

### 49. dt-395

True or False: If you add a tag that has the same key as an existing tag on a DB Instance, the new value overwrites the old value.

<details><summary>Answer</summary>

**A. True.**

</details>

### 50. dt-418

Will I be alerted when automatic fail over occurs?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 51. dt-435

Is decreasing the storage size of a DB Instance permitted?

<details><summary>Answer</summary>

**B. Yes.**

</details>

### 52. dt-444

True or False: REST or Query requests are HTTP or HTTPS requests that use an HTTP verb (such as GET or POST) and a parameter named Action or Operation that specifies the API you are calling.

<details><summary>Answer</summary>

**B. False.**

</details>

### 53. q-454

A company has resources across multiple AWS Regions and accounts. A newly hired solutions architect discovers a previous employee did not provide details about the resources inventory. The solutions architect needs to build and map the relationship details of the various workloads across all accounts. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**C. Use Workload Discovery on AWS to generate architecture diagrams of the workloads.**

Workload Discovery on AWS is a prebuilt solution you deploy from the AWS Solutions Library using a CloudFormation template; once running it inventories resources across the accounts and Regions you point it at and draws the relationships between them as architecture diagrams you can browse and export. That is exactly the gap here, which is an unknown estate with no documentation, and it needs no custom code, so it is the most operationally efficient choice. The AWS Well-Architected Tool is a different thing entirely: it records your answers to a review questionnaire and reports risks against the Well-Architected pillars, and it neither discovers resources nor draws diagrams. AWS Config is the complementary piece worth knowing, since it records resource configuration and relationships, but it does not produce the diagrams the question asks for.

</details>

### 54. dt-492

What does Amazon Cloud Formation provide?

<details><summary>Answer</summary>

**D. A template to map network resources for Amazon Web Services.**

</details>

### 55. q-493

A company wants to use artificial intelligence (AI) to determine the quality of its customer service calls. The company currently manages calls in four different languages, including English. The company will offer new languages in the future. The company does not have the resources to regularly maintain machine learning (ML) models. The company needs to create written sentiment analysis reports from the customer service call recordings. The customer service call recording text must be translated into English. Which combination of steps will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**D. Use Amazon Transcribe to convert the audio recordings in any language into text.**

E. Use Amazon Translate to translate text in any language to English. F. Use Amazon Comprehend to create the sentiment analysis reports.  Use Amazon Transcribe to Convert Audio Recordings into Text:  Amazon Transcribe is a service that converts speech into text. Use it to transcribe the customer service call recordings into text. Use Amazon Translate to Translate Text into English:  Amazon Translate is a service that provides language translation. After transcribing the call recordings into text, use Amazon Translate to translate the text into English. Use Amazon Comprehend to Create Sentiment Analysis Reports:  Amazon Comprehend can be used for sentiment analysis, which involves determining the sentiment or emotion expressed in the text. After translating the text into English, use Amazon Comprehend to analyze the sentiment and create sentiment analysis reports.

</details>

### 56. dt-495

What does Amazon SES stand for?

<details><summary>Answer</summary>

**B. Simple Email Service.**

</details>

### 57. dt-497

Disabling automated backups [...] disable the point-in-time recovery.

<details><summary>Answer</summary>

**C. will.**

</details>

### 58. dt-506

Once again your customers are concerned about the security of their sensitive data and with their latest enquiry ask about what happens to old storage devices on AWS. What would be the best answer to this question?

<details><summary>Answer</summary>

**B. AWS uses the techniques detailed in DoD 5220.22-M to destroy data as part of the decommissioning process.**

</details>

### 59. dt-522

While signing in REST/ Query requests, for additional security, you should transmit your requests using Secure Sockets Layer (SSL) by using [...].

<details><summary>Answer</summary>

**D. HTTPS.**

</details>

### 60. dt-537

Can resource record sets in a hosted zone have a different domain suffix (for example, <www.blog>. acme.com and <www.acme.ca>)?

<details><summary>Answer</summary>

**C. Yes, it can have depending on the TL.**

</details>

### 61. dt-541

Will I be charged if the DB instance is idle?

<details><summary>Answer</summary>

**A. Yes.**

</details>

### 62. dt-639

Select the correct statement.

<details><summary>Answer</summary>

**C. You can't terminate, stop, or delete a resource based solely on its tags.**

</details>

### 63. gh-684

A company wants to migrate its web applications from on premises to AWS. The company is located close to the eu-central-1 Region. Because of
regulations, the company cannot launch some of its applications in eu-central-1. The company wants to achieve single-digit millisecond latency.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Deploy in AWS Local Zones.**

Local Zones provide single-digit latency near eu-central-1 while complying with regulations.
CloudFront (Option A) is for caching, not app hosting.

</details>
