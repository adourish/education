# Compute — question review

Reviewed 92 questions. Found 12 problems.

## Confirmed wrong

### gh-245
**Stated answer:** A. Reconfigure the target group in the development environment to have only one EC2 instance as a target.
**Should be:** D. Reduce the maximum number of EC2 instances in the development environment's Auto Scaling group.
**Why:** The question states the application uses the ALB to direct traffic to *at least two* EC2 instances in a single target group, so dropping the development environment to one target breaks a requirement the question itself sets. Lowering the maximum size of the development Auto Scaling group cuts cost (the development environment never needs production's peak headroom) without violating that requirement.

### gh-523
**Stated answer:** B. Amazon CloudFront with Lambda@Edge functions.
**Should be:** A. AWS AppSync pipeline resolvers.
**Why:** AppSync pipeline resolvers chain several data-source calls — here several DynamoDB tables — inside a single GraphQL request, which is exactly "retrieve data from multiple DynamoDB tables" with no change to baseline performance and nothing to operate. Lambda@Edge is for rewriting requests and responses at CloudFront edge locations; using it to fan out to DynamoDB adds latency, code and operational work rather than removing it.

### gh-584
**Stated answer:** A. Run the EC2 instances in a spread placement group.
**Should be:** The partition placement group option.
**Why:** AWS defines a partition placement group as one where "groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions" — the question's wording about preventing *groups of nodes* from sharing hardware, and about the architecture being *configurable*, is that definition. Partition groups are the documented fit for large distributed parallel workloads (Hadoop, Cassandra, Kafka). A spread placement group isolates individual instances and is limited to 7 running instances per Availability Zone per group, which does not suit a workload "processing large quantities of data in parallel".

### gh-677
**Stated answer:** B. Use mixed On-Demand and Spot Instances in managed node groups.
**Should be:** A. Use Spot Instances in managed node groups (all Spot).
**Why:** The qualifier is MOST cost-effective, and the cluster is a development cluster used infrequently whose stated purpose is testing the application's resiliency — Spot interruptions are tolerable there, and are arguably the point. Managed node groups already satisfy "the EKS cluster must manage all the nodes". Holding On-Demand capacity in that cluster adds cost for a reliability guarantee the scenario does not ask for.

## Out of date

### wl-10
**Stated answer:** D. AWS Lambda (as the option that is *not* a CloudFront origin), with the explanation "AWS Lambda is not supported directly as the CloudFront origin".
**Now:** A Lambda function URL is a supported CloudFront origin type and is listed as such in the CloudFront console. CloudFront added Origin Access Control for Lambda function URL origins on 11 April 2024, so you can both point a distribution at a function URL and lock the function URL down to that distribution. The stated answer and its explanation no longer hold, so the question has no correct answer as written.

### gh-320
**Stated answer:** A. Publish data to Amazon Kinesis Data Streams, use Kinesis Data Analytics to query the data.
**Now:** The service was renamed Amazon Managed Service for Apache Flink in August 2023. The SQL variant the explanation actually describes ("provides an SQL-like language for querying") — Kinesis Data Analytics for SQL Applications — is gone: no new applications could be created after 15 October 2025, and existing applications were deleted and support ended on 27 January 2026. The architecture (a stream plus managed stream processing) is still right, but both the service name and the SQL capability cited are retired.

## Explanation problems

### gh-51
**Issue:** The answer block is corrupted. After the two correct choices (the EventBridge/Lambda query and Amazon SES for the email) it continues with the full text and answers of three unrelated source questions — numbered 52, 53 and 54, covering EFS storage, S3 Object Lock and Windows file shares — and the last one is cut off mid-sentence. Anyone opening the toggle gets three other questions' answers spoiled and no explanation for this one.

### gh-422
**Issue:** The explanation does not describe the stated answer. The answer is SQS plus ECS services scaled on queue depth, but the explanation discusses an Application Load Balancer "to direct requests from the API to the ECS services" and claims "AWS App Mesh can be used to scale the instances of the ECS cluster based on the SQS queue size". App Mesh is a service mesh for service-to-service traffic and performs no scaling at all; scaling here comes from Application Auto Scaling on a CloudWatch queue-depth metric. The ALB sentence belongs to a different option.

### gh-531
**Issue:** The explanation opens with "AWS Lambda supports API Gateway integration, which allows you to create an HTTP endpoint (URL) for your Lambda function," which describes the wrong mechanism. The stated answer is a Lambda function URL — a built-in Lambda feature that gives the function its own dedicated HTTPS endpoint with no API Gateway in the path. The later sentences about avoiding extra services contradict that opening line.

### gh-563
**Issue:** The explanation says Amazon EKS Connector is for centralizing "multiple Amazon EKS clusters" and for "register and connect multiple EKS clusters". EKS Connector exists to register Kubernetes clusters that are *not* EKS — on-premises, self-managed on EC2, or on another cloud — so they show up alongside EKS clusters in the EKS console. EKS clusters in the account already appear there and need no connector. Separately, the question stem is truncated: the first sentence is missing, so the scenario (clusters running outside AWS) is not actually stated.

### gh-576
**Issue:** The explanation says edge-optimized API Gateway endpoints "leverage the AWS Global Accelerator and CloudFront". Global Accelerator is not involved in any way. An edge-optimized endpoint is fronted by an API Gateway-managed CloudFront distribution, and that is the whole mechanism.

### gh-671
**Issue:** The explanation justifies the answer with "CloudWatch (Option D) lacks built-in anomaly detection", which is false — CloudWatch has had metric anomaly detection (machine-learning bands on any metric, usable as an alarm) since 2019. The correct reason to choose AWS Cost Anomaly Detection is that it is purpose-built for cost and usage data, segments spend by service, account and tag, and notifies stakeholders directly, whereas a CloudWatch alarm on the billing metric would need building and tuning by hand.

Checked 92 questions: 4 answers are wrong, 2 are out of date, and 6 explanations are broken or materially incorrect — the answer keys are mostly sound (about 96% defensible) but the explanations are unreliable, with several showing copy-paste damage from the community sources they came from.
