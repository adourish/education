# The compute map

> Where every compute question lives, top to bottom: where the code runs, how
> it grows, how you pay.

## zone: Where the code runs. Least to manage at the top; stop at the first that fits | vpc

### row

**Lambda**
A function on a trigger. *15 minutes, 10 GB*, a zip or a container image.
Nothing to patch.

**Fargate**
Containers with *no servers*. Longer than 15 minutes, or always on. ECS or
EKS on top.

**ECS or EKS on EC2**
You *choose the hardware*: a GPU, a size. EKS only when Kubernetes is named.

**EC2**
Anything at all, and *you patch it*. Pick when nothing above fits.

**Batch**
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
*Min, desired, max*, across two zones or more. Replaces what dies. The answer
to "handle more traffic".

**Target tracking**
*Keep one number* where you want it. Reach for it first.

**Step, scheduled, predictive**
Step: sizes of response. *Scheduled*: a rush with a time. *Predictive*: a
weekly pattern.

**Warm pool**
Instances that take too long to *boot*.

**Memory or disk**
Not there until the *CloudWatch agent* is installed. CPU and network are.

**Bigger, not more**
One job that cannot be split: a *larger instance*. A stop and a start, still
one machine.

## end

## zone: Lambda, when it is the answer and something is wrong | sub

### row

**Cold starts**
*Provisioned concurrency*; schedule it for a known hour. Java: *SnapStart*.

**One function eating all**
*Reserved concurrency*: a ceiling, and zero turns it off.

**Inside a VPC**
No public address: a *NAT gateway* for the internet, *endpoints* for AWS.

**Big or shared files**
*Mount EFS*. The package is 250 MB, /tmp 10 GB.

**Something in front**
*Function URL* for just HTTPS. API Gateway for keys, caching, limits.

**Failed events**
A *dead-letter queue*, or a destination.

## end

## zone: Paying for EC2 | home

### row

**On-Demand**
Short, unknown, or being measured.

**Spot**
Can be *interrupted, two minutes' warning*. Spread across instance types.

**Savings Plan**
Steady, and the *type may change*. Pounds per hour, not a reservation.

**Reserved**
Steady, *one type*, one to three years.

**Dedicated Host**
A *licence by socket or core*. Dedicated Instance only keeps others' tenants
off.

**Placement groups**
*Cluster*: fast, one zone. *Spread*: 7 a zone, apart. *Partition*: big
distributed systems.

## end

## key

cyan: where it runs · amber: paying. Underlined text is the pick.

## Notes

The ladder in the top box is the thing to memorise: each step down is more to
manage, so the one above is the least-overhead answer.
