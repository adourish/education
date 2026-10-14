# The networking map

One picture of where every networking question lives. It sits on the Poster
under "Compare the choices", as its own fold called "The networking map",
closed until opened; the Poster remembers whether you left it open. This file
is the source: change the words here and the picture is rebuilt from it
(the shape lives in one small script that holds the same words).

## How it reads

Top to bottom: the user, then your VPC, then the ways out to other networks.
Each box has a name and a line or two saying when it is the answer. Words in
magenta are the pick a question is after. Boxes sit two across, on a phone and
on a desk alike.

Colours (never red or green):

- cyan stripe: the edge, before your VPC
- magenta stripe: joining networks
- amber dashed box: your own building, with its ways in side by side
- the VPC is a pale cyan dashed box; the subnets inside are plain boxes

## Lede

Where every networking question lives, top to bottom: the user, your VPC, the
ways out.

## Row 1: the edge (cyan)

**Route 53**
Which Region answers. *Latency*: fastest. *Geolocation*: by country. *Failover*
and a health check: a standby. *Weighted*: a share.

**CloudFront**
Caches near the user. *One Region behind CloudFront*, not many Regions. Only
files? S3 behind it.

**WAF and Shield**
Rules on web requests: CloudFront, ALB or API, *never an NLB*. Big attack, team
to call: Shield Advanced.

## Arrow

**Internet gateway**: one per VPC, in no zone

## The VPC (pale cyan dashed box)

### Public subnets, one per zone

**Load balancer**
*ALB* reads the request: paths, headers, logins, WAF. *NLB*: fixed address or
raw TCP.

**NAT gateway**
Private subnets out, never in. *One per zone* in production; one shared for
test.

### Arrow

**A route table per private subnet**, to its own zone's NAT gateway. A shared
table sends every zone through one.

### Private subnets, one per zone

**Servers, containers, Lambda, database**
No public address. Lambda joins by being *attached to the VPC*, not by VPN or
endpoint. The database opens by security group to the servers only.

### Endpoints (still inside the VPC)

**Gateway endpoint**
*S3 and DynamoDB* only. Free. Cuts the NAT bill.

**Interface endpoint, PrivateLink**
Any other AWS service, or *another company's service on AWS*, no internet. To
offer yours: NLB with PrivateLink in front.

## Arrow

Out to other networks

## Row 3: joining networks (magenta)

**Transit gateway**
Hub for *hundreds of VPCs*, accounts, sites. A route table each keeps VPCs
apart. Two VPCs only: *peering*.

## Row 4: your own building (amber dashed box, boxes two across)

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

## Key (grey strip at the bottom)

cyan: the edge · magenta: joining networks · amber: your building. Magenta
text is the pick.

## Questions this picture answers

From the 2026-10-13 review of missed networking questions: ce-75, ce-946,
ce-639, ce-750 (transit gateway); ce-839, ce-397, ce-89, ce-104 (NAT gateway);
ce-683, ce-362, ce-893, ce-949 (Route 53 and CloudFront); ce-310, ce-120,
ce-313, ce-809 (PrivateLink, VPN, Lambda in a VPC); ce-132, ce-148, ce-369,
ce-245, ce-640, ce-233, ce-184.

## Not in the picture, on purpose

Security groups against network ACLs, placement groups, Global Accelerator,
and the detail of Direct Connect gateways. Each has its own term or diagram.
Adding them would make this a wall, and the point of one picture is that it
fits on a phone.
