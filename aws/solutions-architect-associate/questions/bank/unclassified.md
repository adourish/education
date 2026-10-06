# Unclassified — review and tag by hand

5 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. q-233

A solutions architect has created a new AWS account and must secure AWS account root user access. Which combination of actions will accomplish this? (Choose two.)

<details><summary>Answer</summary>

**A. Ensure the root user uses a strong password.**

B. Enable multi-factor authentication to the root user.  Using a strong, complex password for the root user is a fundamental security practice. This helps protect the account from unauthorized access. Enabling MFA adds an additional layer of security. Even if someone manages to obtain the root user's password, they would still need the second factor (e.g., a mobile device or hardware token) to successfully authenticate.

</details>

### 2. q-454

A company has resources across multiple AWS Regions and accounts. A newly hired solutions architect discovers a previous employee did not provide details about the resources inventory. The solutions architect needs to build and map the relationship details of the various workloads across all accounts. Which solution will meet these requirements in the MOST operationally efficient way?

<details><summary>Answer</summary>

**C. Use Workload Discovery on AWS to generate architecture diagrams of the workloads.**

Workload Discovery on AWS is a prebuilt solution you deploy from the AWS Solutions Library using a CloudFormation template; once running it inventories resources across the accounts and Regions you point it at and draws the relationships between them as architecture diagrams you can browse and export. That is exactly the gap here, which is an unknown estate with no documentation, and it needs no custom code, so it is the most operationally efficient choice. The AWS Well-Architected Tool is a different thing entirely: it records your answers to a review questionnaire and reports risks against the Well-Architected pillars, and it neither discovers resources nor draws diagrams. AWS Config is the complementary piece worth knowing, since it records resource configuration and relationships, but it does not produce the diagrams the question asks for.

</details>

### 3. q-493

A company wants to use artificial intelligence (AI) to determine the quality of its customer service calls. The company currently manages calls in four different languages, including English. The company will offer new languages in the future. The company does not have the resources to regularly maintain machine learning (ML) models. The company needs to create written sentiment analysis reports from the customer service call recordings. The customer service call recording text must be translated into English. Which combination of steps will meet these requirements? (Choose three.)

<details><summary>Answer</summary>

**D. Use Amazon Transcribe to convert the audio recordings in any language into text.**

E. Use Amazon Translate to translate text in any language to English. F. Use Amazon Comprehend to create the sentiment analysis reports.  Use Amazon Transcribe to Convert Audio Recordings into Text:  Amazon Transcribe is a service that converts speech into text. Use it to transcribe the customer service call recordings into text. Use Amazon Translate to Translate Text into English:  Amazon Translate is a service that provides language translation. After transcribing the call recordings into text, use Amazon Translate to translate the text into English. Use Amazon Comprehend to Create Sentiment Analysis Reports:  Amazon Comprehend can be used for sentiment analysis, which involves determining the sentiment or emotion expressed in the text. After translating the text into English, use Amazon Comprehend to analyze the sentiment and create sentiment analysis reports.

</details>

### 4. q-624

A company wants to provide users with access to AWS resources. The company has 1,500 users and manages their access to on-premises resources through Active Directory user groups on the corporate network. However, the company does not want users to have to maintain another identity to access the resources. A solutions architect must manage user access to the AWS resources while preserving access to the on- premises resources. What should the solutions architect do to meet these requirements?

<details><summary>Answer</summary>

**D. Configure Security Assertion Markup Language (SAML) 2 0-based federation. Create roles with the appropriate policies attached Map the roles to the Active Directory groups.**

using SAML 2.0-based federation, which allows you to integrate AWS with your existing Active Directory infrastructure. This approach enables single sign-on (SSO) for users, meaning they can use their existing corporate credentials to access both on-premises and AWS resources without maintaining separate identities.

</details>

### 5. gh-684

A company wants to migrate its web applications from on premises to AWS. The company is located close to the eu-central-1 Region. Because of
regulations, the company cannot launch some of its applications in eu-central-1. The company wants to achieve single-digit millisecond latency.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**Answer: B) Deploy in AWS Local Zones.**

Local Zones provide single-digit latency near eu-central-1 while complying with regulations.
CloudFront (Option A) is for caching, not app hosting.

</details>
