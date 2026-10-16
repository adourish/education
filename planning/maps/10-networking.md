# The networking map

> Cue on the left, pick on the right. The user at the edge, your VPC, the ways
> out.

## row: edge

**Route 53**
match: Route ?53|latency(-based)? (routing )?polic|geolocation|failover (routing )?polic|weighted|multivalue
Fastest Region for each user: *latency*. By country: *geolocation*. A
standby: *failover + health check*. Several healthy servers, no load
balancer: *multivalue*. A share: *weighted*.

**CloudFront**
match: CloudFront
Users everywhere, content cacheable: *one Region + CloudFront*, not many
Regions. Only files: *S3 + CloudFront*. ALB origin too.

**Global Accelerator**
match: Global Accelerator
*UDP or TCP, gaming, VoIP, live video, fixed IPs, many Regions*: Global
Accelerator. Caches nothing; NLBs or ALBs as endpoints.

**WAF**
match: WAF
*Rules on web requests*: SQL injection, bots, rate limits, IP sets. On
CloudFront, ALB, API Gateway. *Never an NLB.*

**Shield Advanced**
match: Shield
DDoS on an *NLB, Elastic IP*, CloudFront, ALB, Route 53. Team to call, bill
refunded. "Attacks on an NLB, minimal change": *Shield Advanced*.

## end

## arrow

In through the VPC's one door

## zone: Your VPC | vpc

### row

**Internet gateway**
match: internet gateway(?! .{0,10}egress)|(?<!egress-only )Internet Gateway
*One per VPC, no zone, in and out.* A subnet is public only if its route
table points here. One per zone or per subnet: wrong.

**Load balancer**
match: Application Load Balancer|\bALB\b|Network Load Balancer|\bNLB\b
Paths, headers, cookies, WAF, *Cognito login*: *ALB*. Fixed IP, TCP or UDP,
PrivateLink, on-premises IP targets: *NLB*. Both sit in *public subnets*;
servers and database in private.

**NAT gateway**
match: NAT gateway|NAT instance
Private out, never in. Production: *one per zone*. Test: *one shared*. IPv6:
*egress-only internet gateway* instead.

**Route tables**
match: route table
*One per private subnet*, each to its own zone's NAT. One shared table sends
every zone through one gateway. Public subnet: a route to the internet
gateway.

**Security group vs network ACL**
match: security group|network ACL|\bNACL\b
Allow only, stateful, per instance, *from another group by id*: *security
group*. *Deny*, stateless, per subnet, *block one subnet or address*:
*network ACL*.

## end

### arrow

Private things reaching out, privately

### row

**Gateway endpoint**
match: gateway (VPC )?endpoint|VPC gateway endpoint|endpoint polic
*S3 and DynamoDB only*, free, a route. "Private bucket, no public endpoint,
least privilege": *gateway endpoint + endpoint policy* naming the roles. Cuts
the NAT bill.

**Interface endpoint (PrivateLink)**
match: interface (VPC )?endpoint|VPC interface endpoint|PrivateLink|VPC endpoint for (Amazon )?(SQS|SNS|Kinesis|Secrets|KMS)
*Any other AWS service* (SQS, Kinesis, Secrets Manager): interface endpoint,
a private address, by the hour. *Another company's service on AWS*:
PrivateLink. *Offer yours*: NLB + endpoint service. "Stay within the
company's private IP space" over a VPN: this.

**Lambda in a VPC**
match: Lambda.{0,60}(VPC|private subnet)|(VPC|private subnet).{0,60}Lambda
Needs something private: *attach the function to the subnets* with a
security group. Not a VPN, not an endpoint. Then it has no internet: NAT
gateway or endpoints.

**IPv4 or IPv6**
match: IPv6|IPv4|egress-only|dual-stack|NAT64|DNS64
Every IPv6 address is public: private-but-outbound is the *egress-only
internet gateway*. NAT gateway: IPv4 (NAT64 for IPv6-only hosts). Gateway
endpoint, Elastic IP: IPv4 only. Everything else: both. Rules per family:
*::/0 is not 0.0.0.0/0*.

**Seeing the traffic**
match: Flow Logs|Network Monitor|Reachability Analyzer
Which traffic was allowed or rejected: *VPC Flow Logs*, to CloudWatch Logs,
then *Firehose to OpenSearch*. Is the path to on premises up: *CloudWatch
Network Monitor*. Why a packet cannot get there: *Reachability Analyzer*.

## end

## arrow

Out to other networks

## row: hub

**Transit gateway**
match: Transit Gateway
*Hundreds of VPCs, many accounts, many sites*: transit gateway. Keep spokes
apart: *a route table per attachment*. Share across accounts: RAM.

**VPC peering**
match: VPC peering|peering connection|[Pp]eer (each|the|all|every)
*Exactly two VPCs*, even across accounts (a Lambda reaching another
account's EFS). Not transitive, stops at 125.

**Many accounts, one network**
match: Control Tower|Resource Access Manager|\bRAM\b|shared subnet|share the subnet
Account per workload with *guardrails*: *Control Tower*. One networking
account, *subnets shared with RAM*. Transit gateway + inspection VPC: more
to run.

## zone: Your own building | home

### row

**Direct Connect**
match: Direct Connect(?! gateway)
*Private line, steady, never the internet.* Weeks to set up.

**Site-to-Site VPN**
match: Site-to-Site VPN|customer gateway|virtual private gateway
*Encrypted over the internet, this week, cheap.* A customer gateway at the
office, a virtual private gateway on the VPC. Private RDS for an office
client: this.

**Both**
match: Direct Connect.{0,120}VPN|VPN.{0,120}Direct Connect
Link must not fail: *Direct Connect with the VPN as backup*.

**One line, many VPCs**
match: Direct Connect gateway
*Direct Connect gateway*, usually into a transit gateway.

**One person's laptop**
match: Client VPN
*Client VPN.* Not for a whole building.

**Names across the link**
match: Resolver|forwarding rule
*Route 53 Resolver*: outbound endpoint + *forwarding rule* + *associate the
rule with the VPC* that has the VPN. On premises resolving your names:
inbound endpoint.

## end

## key

cyan: the edge · magenta: joining networks · amber: your building. Underlined
text is the pick.

## Notes

Reviewed against all 71 reviewed networking questions on 2026-10-15. Written
as cue: pick, so each line can be learnt as a pair.
