# 06 — Networking and Content Delivery

## VPC fundamentals

| Cue | Answer |
|---|---|
| Scope of a VPC | **one region**, spanning all its Availability Zones |
| Scope of a subnet | **one Availability Zone** — a subnet never spans AZs |
| CIDR block size range | **/16 down to /28** |
| Reserved addresses per subnet | **5** — the first four and the last |
| Can you change a VPC's primary CIDR | **no**, but you can **add secondary CIDR blocks** |
| What makes a subnet public | a **route to an internet gateway** in its route table. Nothing else. |
| What an instance in a public subnet also needs | a **public IP or Elastic IP** |
| Internet gateways per VPC | **1** |
| What lets private instances reach out to the internet | a **NAT gateway** (or legacy NAT instance) in a **public** subnet |
| Can anything on the internet start a connection through a NAT gateway | **no** — outbound only |
| NAT gateway availability | **AZ-scoped** — deploy one per AZ for resilience, and route each private subnet to the one in its own AZ |
| NAT gateway versus NAT instance | **Gateway** is managed, scales to 100 Gbps, highly available in its AZ. **Instance** is an EC2 you patch, and you must **disable the source/destination check**. |
| Egress-only internet gateway | the **IPv6** equivalent of a NAT gateway |
| Default VPC subnets | one **public** subnet per AZ, auto-assigning public IPv4 |

### The five things a default VPC comes with

1. An **internet gateway** attached.
2. A **main route table** with `0.0.0.0/0` pointing at that internet gateway.
3. A **default security group**, allowing all outbound and allowing inbound from itself.
4. A **default network ACL**, allowing all inbound and all outbound.
5. The account's **default DHCP option set**, associated.

## Security groups versus NACLs

| | Security group | Network ACL |
|---|---|---|
| Level | **Instance / network interface** | **Subnet** |
| State | **Stateful** — return traffic allowed automatically | **Stateless** — you must allow return traffic yourself |
| Rules | **Allow only** | **Allow and Deny** |
| Evaluation | All rules together | **In rule-number order, lowest first, first match wins** |
| Default behaviour | Deny all inbound, allow all outbound | Default NACL allows everything; a **custom** NACL denies everything |
| Can reference another security group | **Yes** | No — IP ranges only |
| Changes take effect | **Immediately** | Immediately |
| Filters traffic between instances in the same subnet | Yes, if they are in different security groups | **No** |
| How many apply | **up to 5 per interface**, all combined | **exactly 1 per subnet** |

> **The ephemeral port trap.** Because NACLs are stateless, an inbound rule for port 443 is not enough — you also need an **outbound** rule for the ephemeral port range (**1024 to 65535**) so the response can get out. SSH through a NACL needs **both** an inbound and an outbound rule.
>
> **The blocking trap.** To block a single malicious IP address, you must use a **NACL deny rule**. A security group cannot deny anything.
>
> **One-line summary for the exam:** security groups usually control **which ports** are open on your instances; NACLs usually control **which networks or IP ranges** can reach a subnet.

## Connecting VPCs and networks

| Cue | Answer |
|---|---|
| Connect two VPCs privately | **VPC peering** |
| Is peering transitive | **No** — if A peers B and B peers C, A cannot reach C |
| Can peered VPCs have overlapping CIDRs | **No** |
| Does peering cross regions and accounts | **Yes, both** |
| Connect hundreds of VPCs and on-premises networks | **Transit Gateway** — a hub-and-spoke router, and it **is** transitive |
| Share one VPC's subnets with other accounts | **VPC sharing via AWS Resource Access Manager (RAM)** |
| Expose your own service to other VPCs without peering | **AWS PrivateLink** / **VPC endpoint services** with an **NLB** |
| Encrypted tunnel from your datacentre over the internet | **Site-to-Site VPN** — 2 tunnels, about 1.25 Gbps each, set up in hours |
| Private, dedicated, consistent-bandwidth link to AWS | **Direct Connect** — 1, 10, or 100 Gbps, **takes weeks to months** |
| Highest-resilience hybrid design | **Direct Connect with a Site-to-Site VPN as backup**, or two Direct Connect links at different locations |
| Encrypt a Direct Connect link | run a **VPN over the Direct Connect public virtual interface**, or use **MACsec** |
| Connect individual users or laptops | **AWS Client VPN** |
| Component on the AWS side of a VPN | a **virtual private gateway** attached to the VPC |
| Component on your side of a VPN | a **customer gateway** |

> **The hybrid question's decision line:** if the question says **"urgent", "within days", "temporary"** → **Site-to-Site VPN**. If it says **"consistent bandwidth", "low jitter", "large steady transfers", "private, not over the internet"** → **Direct Connect**. If it says **both resilience and private bandwidth** → Direct Connect **with VPN failover**.

## VPC endpoints

| Type | Works with | How it works |
|---|---|---|
| **Gateway endpoint** | **S3 and DynamoDB only** | A **route in your route table**. Free. |
| **Interface endpoint (PrivateLink)** | Almost every other AWS service, plus partner and your own services | An **elastic network interface with a private IP** in your subnet, protected by a **security group**. Charged per hour and per GB. |

| Cue | Answer |
|---|---|
| Why use an endpoint at all | traffic to the AWS service **never leaves the AWS network** — no internet gateway, NAT, VPN, or Direct Connect needed |
| Are endpoints highly available | **yes** — horizontally scaled, redundant, no bandwidth bottleneck |
| To restrict which buckets can be reached through an endpoint | a **VPC endpoint policy** |
| Private subnet needs S3 but has no NAT gateway | **gateway endpoint for S3** — and this is also the cost-saving answer, because it removes NAT data processing charges |

## Route 53

| Cue | Answer |
|---|---|
| What it is | a **highly available authoritative DNS** service, plus domain registration and health checks |
| Hosted zone types | **public** (internet-resolvable) and **private** (resolvable only inside associated VPCs) |
| Alias record versus CNAME | **Alias** works at the **zone apex** (example.com), is **free**, and points at AWS resources. **CNAME** cannot be used at the apex and is charged per query. |
| What an Alias can point at | **ELB, CloudFront, API Gateway, S3 static website, Global Accelerator, another Route 53 record, Elastic Beanstalk, VPC endpoint** |
| What an Alias cannot point at | an **EC2 instance DNS name** — use an A record to its IP |
| TTL on an Alias to an ELB | **you do not set it** — Route 53 uses the target's |
| Record types you should recognize | **A, AAAA, CNAME, MX, TXT, NS, SOA, SRV, PTR, CAA, Alias** |
| Health checks can watch | an **endpoint**, **other health checks (calculated)**, or a **CloudWatch alarm** |
| Default health check failure threshold | **3 consecutive failures** |
| Resolve on-premises DNS names from a VPC and vice versa | **Route 53 Resolver inbound and outbound endpoints** |
| To block DNS queries to malicious domains | **Route 53 Resolver DNS Firewall** |

### Routing policies — the trigger table

| The question says | Policy |
|---|---|
| One resource, nothing clever | **Simple** |
| "Send 10% to the new version", "A/B test", "gradual migration" | **Weighted** |
| "Active-passive", "disaster recovery site", "fail over to a static S3 page" | **Failover** |
| "Users in Germany must see the German site", "content licensing by country", "block a country" | **Geolocation** |
| "Shift traffic from one region to another with a bias" | **Geoproximity** (needs traffic flow) |
| "Serve users from the fastest region" | **Latency** |
| "Return several healthy IPs and let the client choose", "basic load balancing in DNS" | **Multivalue answer** |
| "Route based on the user's ISP CIDR block" | **IP-based** |

> **Geolocation versus Latency:** geolocation is about **compliance and content**, latency is about **speed**. If the question says "lowest latency," never pick geolocation.

## CloudFront

| Cue | Answer |
|---|---|
| What it is | a **content delivery network** of edge locations that caches and accelerates content |
| What it accelerates besides static files | **dynamic content, APIs, and whole websites**, via persistent connections over the AWS backbone |
| Origins it supports | **S3, ALB, EC2, API Gateway, MediaStore, or any custom HTTP origin** |
| Default TTL and max TTL | **24 hours** and **1 year** |
| To control caching per request | **cache policies** and **origin request policies** (the legacy name is "cache behaviours with forwarded values") |
| To remove an object from the cache now | an **invalidation** — but **versioned file names** are the cheaper and recommended approach |
| To keep a private S3 bucket private while CloudFront serves it | **Origin Access Control (OAC)** |
| To restrict content to paying users | **signed URLs** (one file) and **signed cookies** (many files) |
| To block or allow whole countries | **geo-restriction** |
| To run code at the edge | **CloudFront Functions** (lightweight, sub-millisecond, header and URL work) and **Lambda@Edge** (heavier, can call other services) |
| To reduce cost by shrinking the footprint | a lower **price class** — All, 200, or 100 |
| To add a WAF | attach a **web ACL** to the distribution |
| To use your own domain with HTTPS | an **ACM certificate in us-east-1** — this region requirement is tested |
| The four viewer-facing layers that need us-east-1 ACM | CloudFront, and that is the one to remember |

### CloudFront versus Global Accelerator

| | CloudFront | Global Accelerator |
|---|---|---|
| Caches content | **Yes** | **No** |
| Protocols | HTTP and HTTPS | **TCP and UDP**, any protocol |
| Gives you | a distribution domain name | **two static anycast IP addresses** |
| Pick it for | static and dynamic **web content** | **non-HTTP** traffic, gaming, VoIP, IoT, or when you need **static IPs** and fast regional failover |

## Elastic IPs and ENIs

| Cue | Answer |
|---|---|
| Elastic IP | a **static public IPv4** you own in a region, remappable between instances |
| When you are charged for an Elastic IP | when it is **not associated with a running instance** — and, since 2024, **all public IPv4 addresses carry an hourly charge** |
| Default Elastic IPs per region | **5** |
| Elastic network interface (ENI) | a virtual network card; it keeps its **private IP, MAC address, and security groups** when you move it |
| Use for a secondary ENI | a **fixed management IP**, a **low-budget high-availability failover**, or separating networks |
| ENI scope | **one Availability Zone** |

## VPC Flow Logs

| Cue | Answer |
|---|---|
| What they capture | **metadata about IP traffic** to and from network interfaces — source, destination, ports, protocol, bytes, and **ACCEPT or REJECT** |
| What they do **not** capture | the **packet contents** — for that you need **VPC Traffic Mirroring** |
| Levels you can enable them at | **VPC, subnet, or network interface** |
| Where they can go | **CloudWatch Logs, S3, or Kinesis Data Firehose** |
| Classic use | diagnosing why traffic is blocked — a **REJECT** tells you a security group or NACL is in the way |
| Traffic flow logs never capture | Amazon DNS server queries, Windows licence activation, instance metadata at 169.254.169.254, DHCP traffic |

## Bastion hosts and Systems Manager

| Cue | Answer |
|---|---|
| Traditional way to reach a private instance | a **bastion host** in a public subnet, with a security group allowing SSH only from your office CIDR |
| Modern way with no bastion, no open ports, no keys | **AWS Systems Manager Session Manager** |
| Why Session Manager is usually the better answer | no inbound ports, no SSH keys to manage, **all sessions logged to CloudTrail and CloudWatch** |
| What a private instance needs for Session Manager | the **SSM Agent** and an **instance profile** with the SSM policy, plus either a NAT gateway or **VPC interface endpoints for SSM** |
