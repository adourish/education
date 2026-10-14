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
Rules on web requests: CloudFront, ALB or API, *never an NLB*. Big attack, team
to call: Shield Advanced.

## arrow

**Internet gateway**: one per VPC, in no zone

## zone: Your VPC | vpc

### zone: Public subnets, one per zone | sub

#### row

**Load balancer**
*ALB* reads the request: paths, headers, logins, WAF. *NLB*: fixed address or
raw TCP.

**NAT gateway**
Private subnets out, never in. *One per zone* in production; one shared for
test.

### end

### arrow

**A route table per private subnet**, to its own zone's NAT gateway. A shared
table sends every zone through one.

### zone: Private subnets, one per zone | sub

#### row

**Servers, containers, Lambda, database**
No public address. Lambda joins by being *attached to the VPC*, not by VPN or
endpoint. The database opens by security group to the servers only.

### end

### row

**Gateway endpoint**
*S3 and DynamoDB* only. Free. Cuts the NAT bill.

**Interface endpoint, PrivateLink**
Any other AWS service, or *another company's service on AWS*, no internet. To
offer yours: NLB with PrivateLink in front.

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
Private line. Steady, never the internet. Weeks to set up.

**Site-to-Site VPN**
Encrypted over the internet. This week, costs little.

**Both**
*Direct Connect, VPN as backup*, when the link must not fail.

**One line, many VPCs**
*Direct Connect gateway*, usually into a transit gateway.

**One person's laptop**
*Client VPN*. Not for a whole building.

**Names across the link**
*Route 53 Resolver*: outbound asks your DNS, inbound lets it ask yours.

## end

## key

cyan: the edge · magenta: joining networks · amber: your building. Magenta text
is the pick.

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
