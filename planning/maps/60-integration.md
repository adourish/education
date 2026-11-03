# The integration map

> Cue on the left, pick on the right. What goes in between, what the queue
> needs set, the front door, events.

## zone: What goes in between | vpc

### row

**SQS**
match: \bSQS\b
*One sender, one worker, nothing lost*, at-least-once. Surge at 8 AM Monday:
*API, SQS, Lambda with provisioned concurrency*. Email results in bulk:
*API, SQS, Lambda*.

**SQS FIFO**
match: \bFIFO\b|MessageDeduplicationId|NumberOfDeduplicatedSentMessages
*Order, no duplicates*: FIFO with a *MessageDeduplicationId*. 300 a second,
3,000 in batches. Are duplicates being dropped: *NumberOfDeduplicatedSentMessages*.

**SNS**
match: \bSNS\b
*One message, many places at once*: email, SMS, Lambda, queues. A contact
form: *API, Lambda, SNS*.

**SNS in front of SQS**
match: SNS.{0,80}SQS|SQS.{0,80}SNS
*Both*: a copy to every subscriber, each queue holds its own work. Containers
consuming messages: *SNS topic, SQS queue, Fargate*.

**EventBridge**
match: EventBridge
*Route on what is inside the event*, schedules, other companies' products.
A custom bus with a Lambda target writing to DynamoDB.

**Kinesis and MSK**
match: Kinesis Data Streams|Apache Flink|\bMSK\b|Kafka
*A stream several readers can replay*: Kinesis Data Streams. Transform on the
way: *Managed Service for Apache Flink*. Kafka named, real-time dashboards
from many schemas: *MSK*.

**Data Firehose**
match: Firehose
*Straight into S3, Redshift, OpenSearch*, no code, no replay. A Lambda can
transform on the way (mask PII).

**Step Functions**
match: Step Functions|state machine|log level
*Steps, retries, waiting for a person*, jobs of many tasks up to a day.
Thousands in parallel: *Map, distributed*. Debug a task: *log level ALL*.

**Amazon MQ**
match: Amazon MQ|ActiveMQ|RabbitMQ
An *existing ActiveMQ or RabbitMQ* app, moved as it is.

## end

## arrow

Then what the queue needs set

## zone: SQS details | sub

### row

**Visibility timeout**
match: visibility timeout
How long a taken message *stays hidden*. Longer than the work, or it is done
twice.

**Dead-letter queue**
match: dead-letter
After *too many failed tries*, here, to be looked at.

**Long polling**
match: long polling|ReceiveMessageWaitTime
*Wait up to 20 seconds* for a message: fewer empty answers, less cost.

**Size and age**
match: 256 KB|Extended Client|retention period
*256 KB* a message; bigger goes to S3 with a pointer. Kept 4 days, up to 14.

**Scaling the workers**
match: queue.{0,80}(Auto Scaling|scal)|ApproximateNumberOfMessages
ASG *target tracking on ApproximateNumberOfMessages* per instance.

**Delay**
match: delay queue|delay seconds|DelaySeconds
Hide a new message for up to *15 minutes*.

## end

## zone: The front door | home

### row

**API Gateway REST**
match: REST API
*Caching, usage plans, API keys, request validation, WAF.* Front for a queue:
*REST API to SQS, Fargate reads*. Writes straight to DynamoDB: *AWS
integration, PutItem*.

**API Gateway HTTP**
match: HTTP API
*Cheaper and faster*, JWT authorizer built in. None of the above.

**Protecting an API**
match: resource polic|\bWAF\b.{0,60}API|API.{0,60}\bWAF\b
SQL injection on a REST API: *WAF*. Only these addresses: *a resource policy*
that denies the rest.

**Lambda function URL**
match: function URL
*One function, one address*, nothing in between. Callers with AWS
credentials: *auth type AWS_IAM*.

**WebSocket, AppSync**
match: WebSocket|AppSync
*Two-way, live*: WebSocket API. *GraphQL*, offline sync: AppSync.

## end

## row: hub

**Lambda and events**
match: S3 event|EventBridge rule|event source mapping|destination
*S3 event, EventBridge schedule, SQS or stream* as the trigger. Async calls
fail into a *dead-letter queue* or a destination.

**Email**
match: \bSES\b|Simple Email
*SES* to send at volume or receive and parse attachments. SNS email is for
alerts.

## key

cyan: what goes in between · amber: the front door · magenta: events. Underlined
text is the pick.

## Notes

Reviewed against all 50 reviewed integration questions on 2026-10-15. Written
as cue: pick, so each line can be learnt as a pair.
