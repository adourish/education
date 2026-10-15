# The networking map

> Where every networking question lives, top to bottom: the user, your VPC,
> the ways out.

## row: edge

**Route 53**
Which Region answers. *Latency*: fastest. *Geolocation*: by country. *Failover*
and a health check: a standby. *Weighted*: a share.

**CloudFront**
Caches near the user. *One Region behind CloudFront*, not many Regions. Only
files? S3 behind it.

**WAF and Shield**
match: \bWAF\b|Shield
Rules on web requests: CloudFront, ALB or API, *never an NLB*. Big attack, team
to call: Shield Advanced.

## arrow

**Internet gateway**: one per VPC, in no zone

## zone: Your VPC | vpc

### zone: Public subnets, one per zone | sub

#### row

**Load balancer**
match: Application Load Balancer|\bALB\b|Network Load Balancer|\bNLB\b
*ALB* reads the request: paths, headers, logins, WAF. *NLB*: fixed address or
raw TCP.

**NAT gateway**
match: NAT gateway|NAT instance
Private subnets out, never in. *One per zone* in production; one shared for
test.

### end

### arrow

**A route table per private subnet**, to its own zone's NAT gateway. A shared
table sends every zone through one.

### zone: Private subnets, one per zone | sub

#### row

**Servers, containers, Lambda, database**
match: -
No public address. Lambda joins by being *attached to the VPC*, not by VPN or
endpoint. The database opens by security group to the servers only.

### end

### row

**Gateway endpoint**
match: gateway (VPC )?endpoint|VPC gateway endpoint|endpoint polic
A private door to *S3 and DynamoDB* only. Free, one line in the route
table. Cuts the NAT bill. "Private bucket, no public endpoint, least
privilege": gateway endpoint plus an *endpoint policy* that allows only
the right roles. Not a bucket policy by address, not a NAT gateway.

**Interface endpoint (PrivateLink)**
match: interface (VPC )?endpoint|VPC interface endpoint|PrivateLink
A private door to *any other AWS service*, or to *another company's service
hosted on AWS*. No internet, costs by the hour. To let others reach your
service the same way: an NLB in front, published with PrivateLink.

### row

**IPv4 or IPv6**
match: IPv6|IPv4|egress-only|dual-stack|NAT64|DNS64
Every IPv6 address is public, so "private but outbound" means an
*egress-only internet gateway*: IPv6 only, out and never in. *NAT gateway*:
IPv4 (NAT64 lets IPv6-only hosts reach IPv4 services). *Gateway endpoint*
and *Elastic IP*: IPv4 only. Internet gateway, both load balancers, peering,
transit gateway, Direct Connect: both. Security group rules are per family:
::/0 is not 0.0.0.0/0.

## end

## arrow

Out to other networks

## row: hub

**Transit gateway**
Hub for *hundreds of VPCs*, accounts, sites. A route table each keeps VPCs
apart. Two VPCs only: *peering*.

## zone: Your own building | home

### row

**Direct Connect**
match: Direct Connect(?! gateway)
Private line. Steady, never the internet. Weeks to set up.

**Site-to-Site VPN**
Encrypted over the internet. This week, costs little.

**Both**
match: Direct Connect.{0,120}VPN|VPN.{0,120}Direct Connect
*Direct Connect, VPN as backup*, when the link must not fail.

**One line, many VPCs**
match: Direct Connect gateway
*Direct Connect gateway*, usually into a transit gateway.

**One person's laptop**
match: Client VPN
*Client VPN*. Not for a whole building.

**Names across the link**
match: Resolver
*Route 53 Resolver*: outbound asks your DNS, inbound lets it ask yours.

## end

## key

cyan: the edge · magenta: joining networks · amber: your building. Underlined text is the pick.

## Notes

How to write one of these: see the top of app/maps.py. Headings the parser
knows are row, arrow, zone, end and key; a heading it does not know, like this
one, is left out of the picture.

From the 2026-10-13 review of missed networking questions: ce-75, ce-946,
ce-639, ce-750 (transit gateway); ce-839, ce-397, ce-89, ce-104 (NAT gateway);
ce-683, ce-362, ce-893, ce-949 (Route 53 and CloudFront); ce-310, ce-120,
ce-313, ce-809 (PrivateLink, VPN, Lambda in a VPC); ce-132, ce-148, ce-369,
ce-245, ce-640, ce-233, ce-184.

Left out on purpose: security groups against network ACLs, placement groups,
Global Accelerator. Each has its own term or diagram.
