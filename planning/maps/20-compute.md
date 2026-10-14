# The compute map

> Where every compute question lives, top to bottom: where the code runs, how
> it grows, how you pay.

## zone: Where the code runs. Least to manage at the top; stop at the first that fits | vpc

### row

**Lambda**
match: \bLambda\b
A function on a trigger. *15 minutes, 10 GB*, a zip or a container image.
Nothing to patch.

**Fargate**
Containers with *no servers*. Longer than 15 minutes, or always on. ECS or
EKS on top.

**ECS or EKS on EC2**
match: (ECS|EKS).{0,60}EC2|EC2 launch type
You *choose the hardware*: a GPU, a size. EKS only when Kubernetes is named.

**EC2**
match: -
Anything at all, and *you patch it*. Pick when nothing above fits.

**Batch**
match: AWS Batch
*Many queued jobs*, with an order between them. It runs the instances.

**Elastic Beanstalk**
Hand it the app; it runs the rest. *Rolling, immutable, blue/green, traffic
splitting* deployments.

## end

## arrow

Then how it carries more

## zone: Growing | sub

### row

**Auto Scaling group**
match: Auto Scaling group
*Min, desired, max*, across two zones or more. Replaces what dies. The answer
to "handle more traffic".

**Target tracking**
match: target tracking
*Keep one number* where you want it. Reach for it first.

**Step, scheduled, predictive**
match: step scaling|scheduled (scaling|action)|predictive scaling
Step: sizes of response. *Scheduled*: a rush with a time. *Predictive*: a
weekly pattern.

**Warm pool**
Instances that take too long to *boot*.

**Memory or disk**
match: CloudWatch agent|memory utili[sz]ation
Not there until the *CloudWatch agent* is installed. CPU and network are.

**Bigger, not more**
match: larger instance|instance (size|type)|vertical
One job that cannot be split: a *larger instance*. A stop and a start, still
one machine.

## end

## zone: Lambda, when it is the answer and something is wrong | sub

### row

**Cold starts**
match: provisioned concurrency|SnapStart
*Provisioned concurrency*; schedule it for a known hour. Java: *SnapStart*.

**One function eating all**
match: reserved concurrency
*Reserved concurrency*: a ceiling, and zero turns it off.

**Inside a VPC**
match: Lambda.{0,80}VPC|VPC.{0,80}Lambda
No public address: a *NAT gateway* for the internet, *endpoints* for AWS.

**Big or shared files**
match: Lambda.{0,80}\bEFS\b|\bEFS\b.{0,80}Lambda
*Mount EFS*. The package is 250 MB, /tmp 10 GB.

**Something in front**
match: function URL|API Gateway
*Function URL* for just HTTPS. API Gateway for keys, caching, limits.

**Failed events**
match: dead-letter|on-failure destination
A *dead-letter queue*, or a destination.

## end

## zone: Paying for EC2 | home

### row

**On-Demand**
match: On-Demand
Short, unknown, or being measured.

**Spot**
match: \bSpot\b
Can be *interrupted, two minutes' warning*. Spread across instance types.

**Savings Plan**
match: Savings Plan
Steady, and the *type may change*. Pounds per hour, not a reservation.

**Reserved**
match: Reserved Instance
Steady, *one type*, one to three years.

**Dedicated Host**
A *licence by socket or core*. Dedicated Instance only keeps others' tenants
off.

**Placement groups**
match: placement group
*Cluster*: fast, one zone. *Spread*: 7 a zone, apart. *Partition*: big
distributed systems.

## end

## key

cyan: where it runs · amber: paying. Underlined text is the pick.

## Notes

The ladder in the top box is the thing to memorise: each step down is more to
manage, so the one above is the least-overhead answer.
