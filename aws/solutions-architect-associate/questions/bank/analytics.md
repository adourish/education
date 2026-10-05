# Analytics — query, ETL, big data, search, BI

7 questions. Answers are hidden behind a toggle — read the question, commit to an answer out loud, then open it.

---

### 1. gh-204

An online retail company has more than 50 million active customers and receives more than 25,000 orders each day. The company collects purchase data for customers and stores this data in Amazon S3. Additional customer data is stored in Amazon RDS.
The company wants to make all the data available to various teams so that the teams can perform analytics. The solution must provide the ability to manage fine-grained permissions for the data and must minimize operational overhead.
Which solution will meet these requirements?

<details><summary>Answer</summary>

**C. Create a data lake by using AWS Lake Formation. Create an AWS Glue JDBC connection to Amazon RDS. Register the S3 bucket in Lake Formation. Use Lake Formation access controls to limit access.**

AWS Lake Formation is designed to create a secure and scalable data lake in Amazon S3. By creating a data lake with Lake Formation, you can centrally manage access controls, fine-grained permissions, and define granular data access policies. This simplifies the process of granting and managing permissions for various teams.

In this scenario, you can use AWS Glue to create a JDBC connection to Amazon RDS for accessing the additional customer data. The S3 bucket, where the purchase data is stored, can be registered in Lake Formation. Lake Formation allows you to set up fine-grained access controls and permissions, providing the ability to manage who can access specific data within the data lake.

</details>

### 2. gh-214

A company’s reporting system delivers hundreds of .csv files to an Amazon S3 bucket each day. The company must convert these files to Apache Parquet format and must store the files in a transformed data bucket.
Which solution will meet these requirements with the LEAST development effort?

<details><summary>Answer</summary>

**B. Create an AWS Glue crawler to discover the data. Create an AWS Glue extract, transform, and load (ETL) job to transform the data. Specify the transformed data bucket in the output step.**

AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load data for analysis. In this scenario:
The AWS Glue crawler can automatically discover the schema of your data stored in Amazon S3, including the .csv files.
The AWS Glue ETL job allows you to define the transformation logic easily. You can create a job using a visual interface or script in Python/Spark.
You can specify the transformed data bucket as the output location for the ETL job.

</details>

### 3. gh-258 `least-ops`

A company has an application that places hundreds of .csv files into an Amazon S3 bucket every hour. The files are 1 GB in size. Each time a file is uploaded, the company needs to convert the file to Apache Parquet format and place the output file into an S3 bucket.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Create an AWS Glue extract, transform, and load (ETL) job to convert the .csv files to Parquet format and place the output files into an S3 bucket. Create an AWS Lambda function for each S3 PUT event to invoke the ETL job.**

AWS Glue ETL Job:

AWS Glue is a fully managed extract, transform, and load (ETL) service that can be used to convert data formats.
By creating an AWS Glue ETL job, you can offload the conversion process to a fully managed service, reducing operational overhead.
AWS Lambda for S3 PUT Events:
AWS Lambda can be configured to trigger on S3 PUT events. This ensures that the ETL job is invoked automatically each time a new .csv file is uploaded to the S3 bucket.
The Lambda function acts as a glue between the S3 events and the Glue ETL job.

</details>

### 4. gh-317 `least-ops`

A company uses a legacy application to produce data in CSV format. The legacy application stores the output data in Amazon S3. The company is deploying a new commercial off-the-shelf (COTS) application that can perform complex SQL queries to analyze data that is stored in Amazon Redshift and Amazon S3 only. However, the COTS application cannot process the .csv files that the legacy application produces.
The company cannot update the legacy application to produce data in another format. The company needs to implement a solution so that the COTS application can use the data that the legacy application produces.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**A. Create an AWS Glue extract, transform, and load (ETL) job that runs on a schedule. Configure the ETL job to process the .csv files and store the processed data in Amazon Redshift.**

</details>

### 5. gh-432 `least-ops`

An ecommerce company wants to use machine learning (ML) algorithms to build and train models. The company will use the models to visualize complex scenarios and to detect trends in customer data. The architecture team wants to integrate its ML models with a reporting platform to analyze the augmented data and use the data directly in its business intelligence dashboards.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**B. Use Amazon SageMaker to build and train models. Use Amazon QuickSight to visualize the data.**

Amazon SageMaker: It is a fully managed service for building, training, and deploying machine learning models. SageMaker simplifies the ML workflow and reduces operational overhead. It provides a fully managed Jupyter Notebook instance for model development and training, and it can seamlessly integrate with other AWS services.
QuickSight can directly connect to Amazon SageMaker models and use the results for visualization without the need for extensive data movement or transformation.

</details>

### 6. gh-442 `least-ops` `security`

A company stores several petabytes of data across multiple AWS accounts. The company uses AWS Lake Formation to manage its data lake. The company's data science team wants to securely share selective data from its accounts with the company's engineering team for analytical purposes.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**D. Use Lake Formation tag-based access control to authorize and grant cross-account permissions for the required data to the engineering team accounts.**

Lake Formation allows you to use tag-based access control to authorize and grant permissions for data in the data lake. You can apply tags to databases and tables, and then use those tags to control access to the data.

By applying tags to the relevant data and using tag-based access control, you can easily manage access to specific data sets without having to create additional IAM roles or copy data to a common account.

</details>

### 7. gh-672 `least-ops`

A marketing company receives a large amount of new clickstream data in Amazon S3 from a marketing campaign. The company needs to analyze
the clickstream data in Amazon S3 quickly. Then the company needs to determine whether to process the data further in the data pipeline.
Which solution will meet these requirements with the LEAST operational overhead?

<details><summary>Answer</summary>

**Answer: B) Use AWS Glue crawler + Athena for ad-hoc queries.**

Glue catalogs data; Athena provides serverless SQL queries.
EMR (Option C) adds operational overhead.

</details>
