# 08 — Application Integration and Analytics

## Pick the integration service

| Shape of the need | Service |
|---|---|
| One producer, one consumer, work queued up, **decoupling** | **SQS** |
| One message, **many** subscribers, fan-out | **SNS** |
| Event-driven routing with filtering on content, plus third-party SaaS events | **EventBridge** |
| Multi-step workflow with branching, retries, and waiting | **Step Functions** |
| Managed RabbitMQ or ActiveMQ because the app already speaks **AMQP, MQTT, STOMP, or JMS** | **Amazon MQ** |
| Streaming data, many consumers, replayable, ordered per shard | **Kinesis Data Streams** |
| Managed Kafka | **Amazon MSK** |

## SQS — Simple Queue Service

| Cue | Answer |
|---|---|
| What it buys you | **loose coupling and elasticity** — the producer and consumer never need to be up at the same time |
| Message size | **256 KB**, or up to 2 GB with the Extended Client Library plus S3 |
| Standard queue guarantees | **at-least-once delivery**, **best-effort ordering**, nearly unlimited throughput |
| What that means for your code | **design for duplicates and out-of-order messages** — make processing safe to repeat |
| FIFO queue guarantees | **exactly-once processing** and **strict order**, 300 messages/s (3,000 batched, far more in high-throughput mode) |
| FIFO queue name must end in | **`.fifo`** |
| FIFO ordering key | the **message group ID** |
| FIFO deduplication | the **message deduplication ID**, or content-based deduplication, over a **5-minute** window |
| Visibility timeout | how long a message is hidden after a receive. Default **30 seconds**, max **12 hours**. |
| Symptom: a message is processed twice | the **visibility timeout is shorter than the processing time** — raise it, or call `ChangeMessageVisibility` while working |
| Short polling versus long polling | **Long polling** waits up to **20 seconds** for a message. It reduces empty responses and cost. **Always prefer long polling.** |
| Dead-letter queue | where messages go after `maxReceiveCount` failed attempts — use it to isolate poison messages |
| Delay queue | delays **every** message up to **15 minutes**; `DelaySeconds` delays an individual message |
| To scale consumers on queue depth | an **Auto Scaling target tracking policy on `ApproximateNumberOfMessagesVisible`**, or the backlog-per-instance metric |
| Encryption | **SSE with KMS**, plus TLS in transit |
| Access control | an **SQS queue policy** (resource-based) |

> **The single most common SQS exam scenario:** traffic spikes overwhelm the processing tier. Answer: **put an SQS queue between the front end and the workers, and auto-scale the workers on queue depth.**

## SNS — Simple Notification Service

| Cue | Answer |
|---|---|
| Model | **publish/subscribe** — one message to many subscribers |
| Subscriber (endpoint) types | **HTTP/HTTPS, Email, Email-JSON, SQS, Lambda, SMS, mobile push, Kinesis Data Firehose** |
| Topic types | **standard** and **FIFO** (FIFO topics can only deliver to SQS FIFO queues) |
| To send one message to several queues at once | **fan-out** — SNS topic with multiple SQS subscriptions |
| To have each subscriber receive only the messages it cares about | a **subscription filter policy** on message attributes |
| To capture messages a subscriber failed to receive | a **redrive policy to a dead-letter queue** |
| Message size | **256 KB** |
| Why fan-out beats having the producer write to each queue | the producer stays unaware of consumers, and you add subscribers without changing code |

## EventBridge

| Cue | Answer |
|---|---|
| What it is | a **serverless event bus** that routes events by **rules matching the event content** |
| Event sources | **AWS services**, your own applications (custom bus), and **SaaS partners** (Zendesk, Datadog, Shopify) |
| Why pick it over SNS | **content-based filtering on the whole event body**, a **schema registry**, **event replay and archive**, and **SaaS integration** |
| Scheduled jobs | **EventBridge Scheduler** — cron or rate expressions, replacing CloudWatch Events rules |
| To react to an AWS API call | a rule matching a **CloudTrail event** |
| EventBridge Pipes | point-to-point: a source, optional filter and enrichment, a target — replaces a lot of glue Lambda code |

> **SNS versus EventBridge in one line:** SNS is for **high-throughput notification fan-out to known subscribers**. EventBridge is for **routing and filtering events across services and SaaS**, with replay.

## Step Functions and SWF

| Cue | Answer |
|---|---|
| **Step Functions** | Visual **state machine** that orchestrates Lambda, ECS, Batch, SNS, SQS, and over 200 services. Handles **retries, error handling, parallel branches, choices, and waits**. |
| Workflow types | **Standard** (up to 1 year, exactly-once, auditable) and **Express** (up to 5 minutes, very high volume, at-least-once) |
| When Step Functions is the answer | "**coordinate multiple Lambda functions**", "a long-running process with human approval", "we need retry and error handling without writing it ourselves", "the workflow takes longer than 15 minutes" |
| **SWF** | The **legacy** workflow service. Only pick it if the question mentions **external signals from humans or on-premises workers** and explicitly rules out Step Functions. For new work, Step Functions. |

## API Gateway

| Cue | Answer |
|---|---|
| What it fronts | **Lambda, HTTP endpoints, any AWS service**, or a VPC resource through a **private integration** |
| API types | **REST** (full features), **HTTP** (cheaper, faster, fewer features), **WebSocket** (two-way) |
| Endpoint types | **Edge-optimized**, **Regional**, **Private** (accessible only through a VPC interface endpoint) |
| To control who calls it | **IAM authorization**, **Lambda authorizers**, **Cognito user pools**, or **resource policies** |
| What an **API key plus usage plan** is for | **throttling and metering per client** — it is **not** authentication |
| To reduce backend load for repeated reads | **API Gateway caching** on a stage |
| To protect the backend from spikes | **throttling** — a steady-state rate and a burst limit |
| To return a 429 | the client exceeded the **throttle limit** |
| To put a WAF in front | attach a **web ACL** to the regional stage |

## Amazon MQ

Pick it when the question says the application **already uses an industry-standard broker protocol** — **AMQP, MQTT, STOMP, OpenWire, or JMS** — and they want a lift-and-shift. For anything new and cloud-native, **SQS and SNS**.

## Kinesis family

| Service | What it does | Trigger |
|---|---|---|
| **Data Streams** | Ingests and retains a stream you write your own consumers for | "**real time**", "**replay**", "multiple applications read the same stream", "ordered per key", "clickstream", "IoT telemetry", "financial transactions", "log and location-tracking events" |
| **Data Firehose** | Delivers a stream into a destination with **no code** | "**load into S3 / Redshift / OpenSearch / Splunk**", "near real time is fine", "no servers to manage", "transform with Lambda on the way" |
| **Managed Service for Apache Flink** | SQL or Flink over a live stream | "**analyse the stream with SQL**", "windowed aggregation in real time", "anomaly detection on the stream" |
| **Video Streams** | Ingest and index video | "camera feeds", "video for ML" |

| Cue | Answer |
|---|---|
| Unit of scale in Data Streams | the **shard** |
| Shard write and read capacity | **1 MB/s or 1,000 records/s in; 2 MB/s out** (shared) |
| To give each consumer its own 2 MB/s | **enhanced fan-out** |
| Record retention | **24 hours** default, up to **365 days** |
| Capacity modes | **provisioned** (you set shards) and **on-demand** (AWS scales it) |
| Symptom: `ProvisionedThroughputExceededException` | too few shards, or a **hot partition key** — use a higher-cardinality partition key, or add shards |
| Kinesis versus SQS | **Kinesis** keeps the data for replay and lets **many consumers read the same records in order**. **SQS** deletes a message once it is processed, and each message goes to one consumer. |
| Firehose latency floor | about **60 seconds** — so Firehose is **not** the answer to "true real time" |

## Analytics

| Service | One-line trigger |
|---|---|
| **Athena** | "**SQL directly on S3**", "no infrastructure", "pay per query, per TB scanned", "ad-hoc analysis of logs in S3" |
| **Glue** | "**serverless ETL**", "**Data Catalog**", "crawl S3 and infer the schema", "prepare data for Athena or Redshift" |
| **EMR** | "**Hadoop, Spark, Hive, HBase, Presto**", "I need access to the cluster and the file system", "customize the framework". EMR launches **EC2 instances you can see and administer**. |
| **Redshift** | "**data warehouse**", "petabyte scale", "complex joins and high-concurrency BI" |
| **OpenSearch Service** | "**full-text search**", "log analytics dashboards", "search an index" |
| **QuickSight** | "**BI dashboards**", "visualize for business users", "embedded analytics" |
| **Lake Formation** | "**build a data lake** with fine-grained, column-level permissions in one place" |
| **Data Pipeline** | legacy scheduled data movement — prefer **Glue** or **Step Functions** for new work |
| **DataZone** | data catalog and governance for sharing data across teams |

### Cost-saving tricks for Athena the exam likes

- Store data in a **columnar format — Parquet or ORC** rather than CSV or JSON.
- **Compress** the files.
- **Partition** by the columns you filter on, such as year and month.
- Use **fewer, larger files** instead of many tiny ones.

All four reduce **bytes scanned**, which is exactly what Athena charges for.

## SES — Simple Email Service

| Cue | Answer |
|---|---|
| What it is for | **sending and receiving bulk or transactional email** |
| SES versus SNS for email | **SES** for real email with templates, attachments, and deliverability reporting. **SNS** email subscriptions for simple notifications. |
| Before you can send at volume | verify your **domain or email address** and request removal from the **sandbox** |
| Deliverability features | **DKIM, SPF, dedicated IPs, configuration sets, reputation dashboard** |

## Media, machine learning, and the rest you should recognize

| Service | One-line trigger |
|---|---|
| **AppSync** | managed **GraphQL** API, with offline sync for mobile |
| **Cognito user pools** | **sign-up and sign-in** for your app's users |
| **Cognito identity pools** | exchange a login for **temporary AWS credentials** |
| **Amplify** | full-stack hosting and backend for web and mobile front ends |
| **Elastic Transcoder / MediaConvert** | convert video formats |
| **Rekognition** | images and video — faces, objects, moderation |
| **Comprehend** | natural language — sentiment, entities, PII detection in text |
| **Textract** | extract text, forms, and tables from scanned documents |
| **Transcribe** | speech to text |
| **Polly** | text to speech |
| **Translate** | language translation |
| **Forecast** | time-series forecasting |
| **Personalize** | recommendations |
| **Fraud Detector** | online fraud detection |
| **SageMaker** | build, train, and deploy your own models |
| **Bedrock** | managed access to foundation models |
| **IoT Core** | connect and manage devices at scale, **MQTT** |
| **Device Farm** | test apps on real phones |
| **WorkSpaces** | managed virtual desktops |
| **AppStream 2.0** | stream a single application to a browser |
