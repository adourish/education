# The integration map

> Where every integration question lives, top to bottom: what goes in between,
> what the queue can do, the front door, and events.

## zone: What goes in between | vpc

### row

**SQS**
*One sender, one worker, nothing lost*. At-least-once, so work must be safe
to repeat.

**SQS FIFO**
*Order, no duplicates*. 300 a second, 3,000 in batches.

**SNS**
*One message, many places at once*. Email, SMS, Lambda, queues.

**SNS in front of SQS**
*Both*: a copy to every subscriber, each queue holds its own work.

**EventBridge**
*Route on what is inside the event*. Schedules. Events from other companies'
products.

**Kinesis Data Streams**
*A stream several readers can replay*. Order inside a shard.

**Data Firehose**
*Straight into S3, Redshift, OpenSearch*, no code. Nothing kept, no replay.

**Step Functions**
*Steps, retries, waiting for a person*. Map state for thousands in parallel.

**Amazon MQ**
An *existing ActiveMQ or RabbitMQ* app, moved as it is.

## end

## arrow

Then what the queue needs set

## zone: SQS details | sub

### row

**Visibility timeout**
How long a taken message *stays hidden*. Longer than the work, or it is
done twice.

**Dead-letter queue**
After *too many failed tries*, the message goes here to be looked at.

**Long polling**
*Wait up to 20 seconds* for a message. Fewer empty answers, less cost.

**Size and age**
*256 KB* a message; bigger goes to S3 with a pointer. Kept 4 days, up to 14.

**Scaling the workers**
An Auto Scaling group on *queue length per instance*.

**Delay**
Hide a new message for up to *15 minutes*.

## end

## zone: The front door | home

### row

**API Gateway REST**
*Caching, usage plans, API keys, request validation, WAF*. More features,
more cost.

**API Gateway HTTP**
*Cheaper and faster*, a JWT authorizer built in. None of the above.

**Lambda function URL**
*One function, one address*, nothing in between.

**WebSocket, AppSync**
*Two-way, live*: WebSocket API. *GraphQL*, offline sync: AppSync.

## end

## row: hub

**Lambda and events**
*S3 event, EventBridge schedule, SQS or stream* as the trigger. Async calls
fail into a *dead-letter queue* or a destination.

**Email**
*SES* to send at volume. SNS email is for alerts, not newsletters.

## key

cyan: what goes in between · amber: the front door · magenta: events. Magenta
text is the pick.

## Notes

A queue holds work for one worker to take; a topic hands a copy to every
subscriber. Firehose keeps nothing, which is what separates it from Data
Streams.
