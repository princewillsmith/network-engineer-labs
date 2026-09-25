# Cloud Networking Interview Notes

Focused on AWS networking, with Kubernetes networking at the end.

---

## VPC Fundamentals

**What makes a subnet "public"?**
Its route table has `0.0.0.0/0` pointing to an **Internet Gateway**, and instances have a public or Elastic IP. A private subnet's default route goes to a **NAT Gateway** in a public subnet, or has no default route at all.

**Security Group vs Network ACL?**

| | Security Group | Network ACL |
|---|---|---|
| Level | ENI / instance | Subnet |
| State | Stateful | Stateless (open ephemeral ports 1024–65535 for return traffic) |
| Rules | Allow only | Allow and deny, evaluated by rule number |
| Default | Deny inbound, allow outbound | Default NACL allows all |

**How many IPs does AWS reserve per subnet?**
Five: network address, VPC router (+1), DNS (+2), future use (+3), and broadcast (last).

---

## Connectivity

**VPC Peering vs Transit Gateway?**
Peering is 1:1 and non-transitive, with no overlapping CIDRs, so it gets hard to manage beyond a few VPCs. Transit Gateway is a regional hub-and-spoke router with route tables for segmentation. It supports VPN and Direct Connect attachments and inter-region peering.

**Site-to-Site VPN vs Direct Connect?**
Site-to-Site VPN is IPsec over the internet: two tunnels per connection, quick to set up, variable latency. Direct Connect is a dedicated private circuit with consistent latency and higher bandwidth, and is often backed up by a VPN.

**How do you reach S3 privately from a private subnet?**
Use a **Gateway VPC Endpoint** for S3 or DynamoDB: a route-table entry with no extra cost. Most other services use **Interface Endpoints** (PrivateLink ENIs with private DNS).

---

## Troubleshooting

**An EC2 instance in a private subnet can't reach the internet. What do you check?**
1. The route table has `0.0.0.0/0 → nat-gw`.
2. The NAT Gateway is in a *public* subnet whose route table points to the IGW.
3. Security Group outbound rules.
4. NACL inbound and outbound rules, including the ephemeral return ports.
5. DNS resolution (`enableDnsSupport`).
6. **VPC Flow Logs**: `REJECT` entries show which layer is dropping traffic.

**What does VPC Reachability Analyzer do?**
It statically analyses the path between two resources (routes, SGs, NACLs, gateways) and tells you exactly which component blocks traffic, without sending packets.

---

## Kubernetes Networking

**How do Pods communicate?**
Every Pod gets its own IP, and all Pods can reach each other without NAT. The CNI plugin (Calico, Cilium, AWS VPC CNI) implements this.

**Service types?**
ClusterIP (internal virtual IP), NodePort (port on every node), LoadBalancer (cloud load balancer), ExternalName (DNS CNAME). kube-proxy (iptables/IPVS) or eBPF programs the forwarding.

**How do you restrict Pod-to-Pod traffic?**
With **NetworkPolicies**: start with default-deny, then allow specific ingress and egress by label, namespace and port. They need a CNI that enforces policy, such as Calico or Cilium.
