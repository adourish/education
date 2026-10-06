# Analytics — query, ETL, big data, search, BI

26 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. dt-9

Your department creates regular analytics reports from your company's log files All log data is collected in Amazon S3 and processed by daily Amazon Elastic MapReduce (EMR) jobs that generate daily PDF reports and aggregated tables in CSV format for an Amazon Redshift data warehouse. Which of the following alternatives will lower costs without compromising average performance of the system or data integrity for the raw data?

<details><summary>Answer</summary>

**C. Use reduced redundancy storage (RRS) for PDF and .csv data in Amazon S3. Add Spot Instances to Amazon EMR jobs. Use Reserved Instances for Amazon Redshift.**

</details>

### 2. ce-134

A healthcare company uses an Amazon EMR cluster to process patient dat a. The data must be encrypted in transit and at rest. Local volumes in the cluster also need to be encrypted. Which solution will meet these requirements? Options:

<details><summary>Answer</summary>

**B. Create an EMR security configuration that encrypts the data and the volumes as required.**

An Amazon EMR security configuration is a reusable set of options that simplifies the setup of security settings for a cluster. It is the designated AWS mechanism for configuring encryption for data both at rest and in transit. This single configuration can specify settings for Amazon S3 encryption (for EMRFS), local disk encryption (which includes attached EBS volumes), and in-transit encryption between cluster nodes using TLS. This directly and comprehensively addresses all the requirements stated in the question. Why Incorrect Options are Wrong: A. Manually creating and attaching encrypted EBS volumes is an incomplete solution. It fails to address the requirements for in-transit encryption between nodes or at-rest encryption for data in Amazon S3. C. An EC2 instance profile is an IAM role that grants permissions to the EMR cluster's instances. It does not configure the cluster's inter

</details>

### 3. et-204

An online retail company has more than 50 million active customers and receives more than 25,000 orders each day. The company collects purchase data for customers and stores this data in Amazon S3. Additional customer data is stored in Amazon RDS. The company wants to make all the data available to various teams so that the teams can perform analytics. The solution must provide the ability to manage fine-grained permissions for the data and must minimize operational overhead. Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a data lake by using AWS Lake Formation. Create an AWS Glue JDBC connection to Amazon RDS. Register the S3 bucket in Lake Formation. Use Lake Formation access controls to limit access.**

AWS Lake Formation is designed to create a secure and scalable data lake in Amazon S3. By creating a data lake with Lake Formation, you can centrally manage access controls, fine-grained permissions, and define granular data access policies. This simplifies the process of granting and managing permissions for various teams.  In this scenario, you can use AWS Glue to create a JDBC connection to Amazon RDS for accessing the additional customer data. The S3 bucket, where the purchase data is stored, can be registered in Lake Formation. Lake Formation allows you to set up fine-grained access controls and permissions, providing the ability to manage who can access specific data within the data lake.

</details>

### 4. ce-220 `least-ops`

A company uses AWS Lake Formation to govern its S3 data lake. It wants to visualize data in QuickSight by joining S3 data with Aurora MySQL operational data. The marketing team must see only specific columns. Which solution provides column-level authorization with the least operational overhead?

<details><summary>Answer</summary>

**D. Use a Lake Formation blueprint to ingest database data to S3. Use Lake Formation for column- level access control. Use Athena as the QuickSight data source.**

This solution leverages AWS Lake Formation, which the company already uses, for both data ingestion and governance. Lake Formation blueprints provide a simplified, template-based method to ingest data from sources like Aurora MySQL into the S3 data lake, minimizing operational overhead. Once the data is in the data lake and cataloged, Lake Formation's core feature of fine-grained access control can be used to grant the marketing team permissions to only specific columns. Amazon Athena can then query this governed data, and since it integrates with Lake Formation, it will enforce these column-level permissions. Amazon QuickSight uses Athena as a data source, ensuring that visualizations for the marketing team are built only from the columns they are authorized to see. Why Incorrect Options are Wrong: A. Using EMR involves managing clusters and custom jobs, which represents a significantly

</details>

### 5. ce-226 `least-ops`

A company has an Amazon S3 data lake that is governed by AWS Lake Formation. The company wants to create a visualization in Amazon QuickSight by joining the data in the data lake with operational data that is stored in an Amazon Aurora MySQL database. The company wants to enforce column-level authorization so that the company's marketing team can access only a subset of columns in the database. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use a Lake Formation blueprint to ingest the data from the database to the S3 data lake. Use Lake Formation to enforce column-level access control for the QuickSight users. Use Amazon Athena as the data source in QuickSight.**

This solution leverages AWS Lake Formation, which is already in use for governing the S3 data lake. A Lake Formation blueprint automates the creation of an AWS Glue workflow to ingest data from the Aurora MySQL database into the S3 data lake. Once the new data is registered in the AWS Glue Data Catalog, Lake Formation's centralized, fine-grained access controls can be used to grant the marketing team permissions to only specific columns. Amazon QuickSight can then use Amazon Athena as a data source to query the data lake, and Athena will enforce the column-level permissions defined in Lake Formation. This approach extends the existing governance model with minimal operational overhead using serverless, managed services. Why Incorrect Options are Wrong: A. Using Amazon EMR introduces significant operational overhead for managing clusters and jobs. It also doesn't provide a dynamic column-

</details>

### 6. et-258 `least-ops`

A company has an application that places hundreds of .csv files into an Amazon S3 bucket every hour. The files are 1 GB in size. Each time a file is uploaded, the company needs to convert the file to Apache Parquet format and place the output file into an S3 bucket. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an AWS Glue extract, transform, and load (ETL) job to convert the .csv files to Parquet format and place the output files into an S3 bucket. Create an AWS Lambda function for each S3 PUT event to invoke the ETL job.**

AWS Glue ETL Job:  AWS Glue is a fully managed extract, transform, and load (ETL) service that can be used to convert data formats. By creating an AWS Glue ETL job, you can offload the conversion process to a fully managed service, reducing operational overhead. AWS Lambda for S3 PUT Events: AWS Lambda can be configured to trigger on S3 PUT events. This ensures that the ETL job is invoked automatically each time a new .csv file is uploaded to the S3 bucket. The Lambda function acts as a glue between the S3 events and the Glue ETL job.

</details>

### 7. et-317 `least-ops`

A company uses a legacy application to produce data in CSV format. The legacy application stores the output data in Amazon S3. The company is deploying a new commercial off-the-shelf (COTS) application that can perform complex SQL queries to analyze data that is stored in Amazon Redshift and Amazon S3 only. However, the COTS application cannot process the .csv files that the legacy application produces. The company cannot update the legacy application to produce data in another format. The company needs to implement a solution so that the COTS application can use the data that the legacy application produces. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create an AWS Glue extract, transform, and load (ETL) job that runs on a schedule. Configure the ETL job to process the .csv files and store the processed data in Amazon Redshift.**

</details>

### 8. dt-339

You have just finished setting up an advertisement server in which one of the obvious choices for a service was Amazon Elastic MapReduce( EMR) and are now troubleshooting some weird cluster states that you are seeing. Which of the below is not an Amazon EMR cluster state?

<details><summary>Answer</summary>

**B. STOPPED.**

</details>

### 9. et-432 `least-ops`

An ecommerce company wants to use machine learning (ML) algorithms to build and train models. The company will use the models to visualize complex scenarios and to detect trends in customer data. The architecture team wants to integrate its ML models with a reporting platform to analyze the augmented data and use the data directly in its business intelligence dashboards. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon SageMaker to build and train models. Use Amazon QuickSight to visualize the data.**

Amazon SageMaker: It is a fully managed service for building, training, and deploying machine learning models. SageMaker simplifies the ML workflow and reduces operational overhead. It provides a fully managed Jupyter Notebook instance for model development and training, and it can seamlessly integrate with other AWS services. QuickSight can directly connect to Amazon SageMaker models and use the results for visualization without the need for extensive data movement or transformation.

</details>

### 10. et-442 `least-ops` `security`

A company stores several petabytes of data across multiple AWS accounts. The company uses AWS Lake Formation to manage its data lake. The company's data science team wants to securely share selective data from its accounts with the company's engineering team for analytical purposes. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use Lake Formation tag-based access control to authorize and grant cross-account permissions for the required data to the engineering team accounts.**

Lake Formation allows you to use tag-based access control to authorize and grant permissions for data in the data lake. You can apply tags to databases and tables, and then use those tags to control access to the data.  By applying tags to the relevant data and using tag-based access control, you can easily manage access to specific data sets without having to create additional IAM roles or copy data to a common account.

</details>

### 11. dt-451

A major finance organisation has engaged your company to set up a large data mining application. Using AWS you decide the best service for this is Amazon Elastic MapReduce (EMR) which you know uses Hadoop. Which of the following statements best describes Hadoop?

<details><summary>Answer</summary>

**C. Hadoop is an open source Java software framework.**

</details>

### 12. ce-488 `least-ops`

A marketing company receives a large amount of new clickstream data in Amazon S3 from a marketing campaign The company needs to analyze the clickstream data in Amazon S3 quickly. Then the company needs to determine whether to process the data further in the data pipeline. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Configure an AWS Glue crawler to crawl the data. Configure Amazon Athena to query the data.**

This solution provides the quickest analysis with the least operational overhead by using two serverless AWS services. An AWS Glue crawler automatically discovers the schema of the clickstream data in Amazon S3 and populates the AWS Glue Data Catalog with the metadata. This eliminates the manual effort of defining tables. Amazon Athena, a serverless interactive query service, can then use this catalog to run standard SQL queries directly on the data in S3. This combination allows for immediate, ad-hoc analysis without the need to provision or manage any infrastructure, perfectly matching the requirements for speed and minimal operational overhead. Why Incorrect Options are Wrong: A. AWS Glue jobs are designed for batch ETL (Extract, Transform, Load) processes, not for quick, interactive, ad-hoc querying, making them less suitable and more operationally complex for this use case. C. Amazo

</details>

### 13. ce-551

A company's reporting system delivers hundreds of .csv files to an Amazon S3 bucket each day. The company must convert these files to Apache Parquet format and must store the files in a transformed data bucket. Which solution will meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**B. Create an AWS Glue crawler to discover the data. Create an AWS Glue extract, transform, and load (ETL) job to transform the data. Specify the transformed data bucket in the output step.**

AWS Glue is a fully managed extract, transform, and load (ETL) service designed to simplify data preparation for analytics. For this scenario, an AWS Glue crawler can automatically scan the source S3 bucket to infer the schema of the CSV files and populate the AWS Glue Data Catalog. Subsequently, an AWS Glue ETL job can be created to read the source data, convert it from CSV to Apache Parquet format, and write the results to the destination S3 bucket. This approach minimizes development effort by leveraging managed, purpose-built components and auto-generated transformation scripts, abstracting away the underlying compute infrastructure. Why Incorrect Options are Wrong: A. Amazon EMR requires provisioning and managing a cluster and writing a custom Spark application, which constitutes significantly more development and operational effort than using a managed service like AWS Glue. C. AWS

</details>

### 14. ce-577

A telemarketing company is designing its customer call center functionality on AWS. The company needs a solution that provides multiple speaker recognition and generates transcript files. The company wants to query the transcript files to analyze the business patterns. Which solution will meet these requirements?

<details><summary>Answer</summary>

**B. Use Amazon Transcribe for multiple speaker recognition. Use Amazon Athena to analyze the transcript files.**

Amazon Transcribe is the appropriate AWS service for converting speech to text and includes a feature called speaker diarization, which fulfills the requirement for multiple speaker recognition by identifying and labeling different speakers in the audio. Amazon Transcribe can save the output transcript files (typically in JSON format) to an Amazon S3 bucket. Amazon Athena is a serverless query service that can directly query data stored in Amazon S3 using standard SQL. This combination provides a fully managed, serverless solution to generate, store, and analyze the call center transcripts as required. Why Incorrect Options are Wrong: A. Amazon Rekognition is used for image and video analysis, not for audio transcription or speaker recognition. C. Amazon Translate is a language translation service; it does not perform speech-to-text transcription or identify speakers. D. Amazon Rekogniti

</details>

### 15. ce-590 `least-ops`

An ecommerce company wants to use machine learning (ML) algorithms to build and train models. The company will use the models to visualize complex scenarios and detect trends in customer data. The architecture team wants to integrate its ML models with a reporting platform to analyze the augmented data and use the data directly in its business intelligence dashboards. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon SageMaker AI to build and train models. Use Amazon QuickSight to visualize the data.**

Amazon SageMaker is a fully managed service specifically designed to build, train, and deploy machine learning (ML) models, which directly addresses the company's need to create models for trend detection. Amazon QuickSight is a serverless business intelligence (BI) service built for cloud-scale data visualization and dashboarding. QuickSight can natively integrate with Amazon SageMaker, allowing the company to use the output from its trained models as a data source for its BI dashboards. This combination provides a powerful, integrated solution with the least operational overhead, as both services are fully managed by AWS. Why Incorrect Options are Wrong: A. AWS Glue ML Transforms are for specific data preparation tasks like record deduplication, not for building and training general-purpose ML models for trend analysis. C. Using an AMI from AWS Marketplace requires managing the underly

</details>

### 16. ce-594

A finance company collects streaming data for a real-time search and visualization system. They want to migrate to AWS using a native solution for ingest, search, and visualization. Options:

<details><summary>Answer</summary>

**D. Use Kinesis Data Streams Amazon OpenSearch Service Amazon QuickSight**

This architecture provides a fully managed, native AWS solution for the entire data pipeline. Amazon Kinesis Data Streams is the purpose-built service for ingesting real-time streaming data at scale. Amazon OpenSearch Service is designed for indexing, full-text search, and near-real-time analysis of streaming data, directly addressing the "real-time search" requirement. Finally, Amazon QuickSight is a business intelligence (BI) service that can connect to Amazon OpenSearch Service as a data source to create the required visualizations and dashboards. This combination of services creates a cohesive and efficient serverless pipeline for the specified use case. Why Incorrect Options are Wrong: A. Amazon Athena is an interactive query service for data in S3, which is not suitable for the low-latency, continuous query needs of a real-time search system. B. Amazon Redshift is a data warehouse

</details>

### 17. dt-595

You are in the process of building an online gaming site for a client and one of the requirements is that it must be able to process vast amounts of data easily. Which AWS Service would be very helpful in processing all this data?

<details><summary>Answer</summary>

**D. Amazon EMR.**

</details>

### 18. ce-634

A finance company uses an on-premises search application to collect streaming data from various producers. The application provides real-time updates to search and visualization features. The company is planning to migrate to AWS and wants to use an AWS native solution. Which solution will meet these requirements?

<details><summary>Answer</summary>

**D. Use Amazon Kinesis Data Streams to ingest and process the data streams to Amazon OpenSearch Service. Use OpenSearch Service to search the data. Use Amazon QuickSight to create visualizations.**

This solution correctly maps the requirements to the most suitable AWS native services. Amazon Kinesis Data Streams is designed for ingesting and processing large-scale streaming data in real time. Amazon OpenSearch Service is a managed service built for indexing, searching, and analyzing data in near real-time, making it the ideal replacement for an on-premises search application. The data ingested via Kinesis can be directly streamed into an OpenSearch Service domain for immediate indexing and searching. Amazon QuickSight can then connect to OpenSearch Service to create the required visualizations and dashboards. This architecture provides a fully managed, scalable, and real-time solution. Why Incorrect Options are Wrong: A. Amazon Athena is an interactive query service for data in S3, not a real-time search engine. It is not suitable for applications requiring low-latency, real-time s

</details>

### 19. ce-637

A mining company is using Amazon S3 as its data lake. The company wants to analyze the data collected by the sensors in its mines. A data pipeline is being built to capture data from the sensors, ingest the data into an S3 bucket, and convert the data to Apache Parquet format. The data pipeline must be processed in near-real time. The data will be used for on-demand queries with Amazon Athena. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Data Firehose to invoke an AWS Lambda function that converts the data to Parquet format and stores the data in Amazon S3.**

Amazon Data Firehose is a fully managed service designed to capture, transform, and load streaming data into data stores like Amazon S3. It directly supports the requirements by ingesting near-real-time sensor data. A key feature of Firehose is its built-in capability for data format conversion, which can convert incoming data (e.g., JSON) into columnar formats like Apache Parquet before storing it in S3. This is highly efficient and requires no custom code. If more complex transformations are needed, Firehose can invoke an AWS Lambda function. This creates a serverless, scalable, and low-latency pipeline optimized for subsequent analysis with Amazon Athena. Why Incorrect Options are Wrong: B. Use Amazon Kinesis Data Streams to invoke an AWS Lambda function that converts the data to Parquet format and stores the data in Amazon S3. This is a viable but less optimal solution. It requires m

</details>

### 20. ce-638

A company uses Amazon Redshift to store structured data and Amazon S3 to store unstructured dat a. The company wants to analyze the stored data and create business intelligence reports. The company needs a data visualization solution that is compatible with Amazon Redshift and Amazon S3. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Redshift query editor v2 to analyze data stored in Amazon Redshift. Use Amazon Athena to analyze data stored in Amazon S3. Use Amazon QuickSight to access Amazon Redshift and Athena, visualize the data analyses, and create business intelligence reports.**

This solution presents a standard and effective AWS architecture for business intelligence. Amazon Athena is the designated serverless query service for analyzing data directly in Amazon S3 using standard SQL. The Amazon Redshift query editor v2 is a web-based tool for querying data within an Amazon Redshift data warehouse. Amazon QuickSight is a cloud-native, serverless business intelligence (BI) service that can natively connect to both Amazon Redshift and Amazon Athena as data sources. This allows for the creation of unified dashboards and reports that visualize data from both the S3 data lake and the Redshift data warehouse, directly meeting all the company's requirements. Why Incorrect Options are Wrong: B. Amazon S3 Object Lambda is used to modify data as it is being retrieved from S3; it is not a query or analysis engine like Athena. C. Amazon Redshift Spectrum is used to query da

</details>

### 21. ce-649

A company operates a data lake in Amazon S3 that stores large datasets in multiple formats. The company has an application that retrieves and processes subsets of data from multiple objects in the data lake based on filtering criteri a. For each data query, the application currently downloads the entire S3 object and performs transformations. The current process requires a large amount of transformation time. The company wants a solution that will give the application the ability to query and filter directly on S3 objects without downloading the objects. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Athena to query and filter the objects in Amazon S3.**

Amazon Athena is an interactive, serverless query service designed to analyze data directly in Amazon S3 using standard SQL. It allows the application to query and filter data in-place without the need to download entire objects or manage any infrastructure. By defining a schema for the data in S3 and running SQL queries, Athena processes the query and returns only the requested subset of data. This directly addresses the requirement to query and filter on S3 objects, significantly reducing data transfer and processing time compared to the current method of downloading and transforming entire objects. Why Incorrect Options are Wrong: B. Use Amazon EMR to process and filter the objects. Amazon EMR is a big data platform for large-scale data processing jobs, which is overly complex and costly for interactive querying. It requires managing a cluster. C. Use Amazon API Gateway to create an A

</details>

### 22. ce-654 `least-ops`

A company is developing a platform to process large volumes of data for complex analytics and machine learning (ML) tasks. The platform must handle compute-intensive workloads. The workloads currently require 20 to 30 minutes for each data processing step. The company wants a solution to accelerate data processing. Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Create an Amazon EMR cluster. Use managed scaling. Install Apache Spark to assist with data processing.**

Amazon EMR (Elastic MapReduce) is a managed cloud big data platform designed for processing vast amounts of data using open-source tools like Apache Spark. Apache Spark is a unified analytics engine for large-scale data processing that excels at compute-intensive and iterative ML tasks. Using an EMR cluster with Spark provides a distributed, parallel processing environment that can significantly accelerate the 20-30 minute data processing steps. EMR's managed scaling feature automatically resizes the cluster based on workload, which fulfills the requirement for the least operational overhead by removing the need for manual cluster management. Why Incorrect Options are Wrong: A. Manually deploying and managing EC2 instances for batch processing incurs significant operational overhead for setup, software installation, scaling, and fault tolerance, contradicting a key requirement. C. AWS La

</details>

### 23. ce-695

A company operates a data lake in Amazon S3. The company wants to query and filter data directly in S3 without downloading objects. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Use Amazon Athena to query and filter the objects in Amazon S3.**

Amazon Athena is a serverless, interactive query service designed to analyze data directly in Amazon S3 using standard SQL. It allows users to query large datasets without the need to set up complex infrastructure or move the data. Athena works by pointing to your data in S3, defining a schema, and using its built-in query editor to run queries. This directly meets the requirement to query and filter data in S3 without downloading it, making it the most efficient and appropriate solution for this use case. Why Incorrect Options are Wrong: B. Amazon EMR is a big data processing framework, which is more complex and costly than necessary for simple querying and filtering. C. Amazon API Gateway is used to create and manage APIs; it does not have native capabilities to query data within S3 objects. D. Amazon ElastiCache is an in-memory caching service used to improve application performance,

</details>

### 24. dt-730 `cost`

A company stores 200 GB of data each month in Amazon S3. The company needs to perform analytics on this data at the end of each month to determine the number of items sold in each sales region for the previous month. Which analytics strategy is MOST cost-effective for the company to use?

<details><summary>Answer</summary>

**B. Create a table in the AWS Glue Data Catalog. Query the data in Amazon S3 by using Amazon Athena. Visualize the data in Amazon QuickSight.**

</details>

### 25. ce-823

A company wants to visualize its AWS spend and resource usage. The company wants to use an AWS managed service to provide visual dashboards. Which solution will meet these requirements?

<details><summary>Answer</summary>

**A. Configure an export in AWS Data Exports. Use Amazon QuickSight to create a cost and usage dashboard. View the data in QuickSight.**

The most effective solution is to use AWS Data Exports to create a detailed Cost and Usage Report (CUR) and deliver it to an Amazon S3 bucket. This report contains the most comprehensive set of AWS cost and usage data available. Amazon QuickSight, an AWS managed business intelligence (BI) service, can then connect to this data in S3 (often queried via Amazon Athena for performance) to build powerful, interactive, and customizable visual dashboards. This approach directly meets the company's requirements for visualizing spend and usage using AWS managed services. Why Incorrect Options are Wrong: B: AWS Budgets is primarily for monitoring costs against a set threshold and triggering alerts. It is not a tool for creating detailed, interactive visualization dashboards for in-depth analysis. C: AWS Cost Explorer provides pre-built visualizations and reports, but it offers less customization f

</details>

### 26. ce-952 `least-ops`

A company wants to use automatic machine learning (ML) to create and visualize forecasts of complex scenarios and trends. Which solution will meet these requirements with the LEAST management overhead?

<details><summary>Answer</summary>

**B. Use Amazon QuickSight to visualize the data. Use ML-powered forecasting in QuickSight to create forecasts.**

Amazon QuickSight is a fully managed business intelligence (BI) service that includes built-in, machine learning-powered capabilities for forecasting. Users can add forecasts to time-series visuals with a few clicks, without needing to manage any underlying infrastructure or build complex ML models manually. This integrated approach directly addresses the requirements to create and visualize forecasts with the absolute least management overhead. The ML algorithms are managed by AWS within the QuickSight service, making it the most efficient solution for this scenario. Why Incorrect Options are Wrong: A. AWS Glue ML Transforms are designed for data preparation tasks like finding matching records (record linkage), not for time-series forecasting. This is an incorrect application of the service. C. Using a prebuilt ML AMI requires provisioning and managing an EC2 instance, including OS patc

</details>
