# The compute map

> Cue on the left, pick on the right. Where the code runs, how it grows, Lambda
> fixes, how you pay.

## zone: Where the code runs. Stop at the first that fits | vpc

### row

**Lambda**
match: \bLambda\b
*Under 15 minutes, on a trigger*, a zip or a *container image* up to 10 GB.
Nothing to patch. Event in, Lambda out.

**Fargate**
match: Fargate
*Containers, no servers*, longer than 15 minutes or always on. Nightly job,
can be interrupted: *Fargate Spot*.

**ECS or EKS on EC2**
match: (ECS|EKS).{0,80}EC2|EC2 launch type|GPU instance|EKS Anywhere|EKS Connector|Amazon ECS cluster|ECS containers
*A GPU, or you choose the hardware.* Kubernetes named: EKS; else ECS.
Kubernetes on your own servers: *EKS Anywhere*. See every cluster in one
place: *EKS Connector*.

**EC2**
match: -
Anything at all, *you patch it*. Last resort.

**Batch**
match: AWS Batch
*Many jobs, hours or days, with an order.* Simulations that run for days.

**Elastic Beanstalk**
match: Elastic Beanstalk
Hand it the app. New version on a slice of real traffic: *traffic splitting*.
Safest, undoable: *immutable*. Quick rollback: *blue/green*.

## end

## arrow

Then how it carries more

## zone: Growing | sub

### row

**Auto Scaling group**
match: Auto Scaling group|launch template|AWS Auto Scaling|Application Auto Scaling
*Min, desired, max, across zones*, replaces what dies. "Single instance,
growing": *ASG min 3 across zones + ALB*. Queue-fed workers: *scale on queue
length*.

**Which policy**
match: target tracking|step scaling|scheduled (scaling|action)|predictive scaling
Keep one number: *target tracking*, first choice. A time you can name:
*scheduled*. Weekly pattern: *predictive*. Sizes of response: *step*.

**Slow to start**
match: warm pool|fast snapshot restore
Instances boot slowly, peak known: *max at peak + warm pool*. Large AMI:
*fast snapshot restore* on the snapshot, then a new AMI.

**Memory or disk**
match: CloudWatch agent|memory utili[sz]ation|Container Insights
Not there until the *CloudWatch agent* is installed. EKS pods and nodes:
*Container Insights*.

**Bigger, not more**
match: larger instance|instance (size|type)|vertical
One job that cannot be split: *a larger instance*. A stop and a start, still
one machine.

**Containers scaling**
match: Service Auto Scaling|Cluster Autoscaler|Horizontal Pod|task placement
ECS tasks across zones: *Service Auto Scaling, min 3, placement spread by
zone*. EKS pods grow but nodes do not: *Cluster Autoscaler*.

**Images and config**
match: Image Builder|Service Catalog|ECR.{0,40}scan|scan on push|Parameter Store
Patched AMIs on a schedule: *EC2 Image Builder*. Only approved AMIs: *Service
Catalog*. Scan images for CVEs: *ECR scan on push*. Secrets into a container:
*Parameter Store + task execution role*.

## end

## zone: Lambda, when something is wrong | sub

### row

**Cold starts**
match: provisioned concurrency|SnapStart
Peak season, latency: *provisioned concurrency*, scheduled for the hour.
Java: *SnapStart*.

**One function eating all**
match: reserved concurrency
*Reserved concurrency*: a ceiling; zero turns it off.

**Something in front**
match: function URL|API Gateway|edge-optimized|HTTP API
One function, one HTTPS address, a webhook, a mainframe calling REST:
*function URL*. Keys, caching, limits: *API Gateway*. Users worldwide:
*edge-optimized + caching*. JWT: *HTTP API*.

**Big or shared files**
match: Lambda.{0,80}\bEFS\b|\bEFS\b.{0,80}Lambda
Dependencies too big for a layer: *mount EFS*.

**Reacting to things**
match: EventBridge rule.{0,80}Lambda|Lambda.{0,80}EventBridge|Config custom rule|GuardDuty.{0,80}Lambda
Start and stop by schedule: *EventBridge rule, Lambda*. A finding needs
action (GuardDuty mining, a bad Redshift setting): *EventBridge or Config
custom rule, Lambda*.

**Failed events**
match: dead-letter|on-failure destination
*A dead-letter queue*, or a destination.

## end

## zone: Paying for EC2 | home

### row

**On-Demand**
match: On-Demand
Short, unknown, dev and test, being measured.

**Spot**
match: \bSpot\b|allocation strategy
Can be interrupted, two minutes' warning: *Spot*. Capacity keeps failing:
*capacity-optimized allocation + more instance types*. Stateless web on one
instance: *AMI, launch template, Spot Fleet*.

**Reserved or Savings Plan**
match: Reserved Instance|Savings Plan
Steady baseline, cannot be interrupted: *Reserved for the ASG minimum*,
Spot or On-Demand above it. Production reserved, *dev and test On-Demand*.
Type may change: *Savings Plan*.

**Dedicated Host**
match: Dedicated Host|Dedicated Instance
*Licence by socket or core*: Dedicated Host. Only off others' hardware:
Dedicated Instance.

**Placement groups**
match: placement group|Elastic Fabric Adapter|\bEFA\b
Tightly coupled HPC, node to node: *cluster placement group + EFA*. Few
critical instances apart: *spread*. Big distributed system: *partition*.

**Spending guard**
match: Budgets|Instance Scheduler
Developers leave instances on: *Budgets alert at forecast, action stops
them*. Office hours only: *Instance Scheduler* or EventBridge + Lambda.

## end

## key

cyan: where it runs · amber: paying. Underlined text is the pick.

## Notes

Reviewed against all 111 reviewed compute questions on 2026-10-15. Written as
cue: pick, so each line can be learnt as a pair.
