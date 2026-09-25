# Networking Interview Notes

Short, practical answers to questions that come up in network engineer interviews.

---

## OSI and TCP/IP

**Walk through what happens when you open https://example.com.**
1. The browser checks its cache, then asks the OS resolver, which queries DNS (UDP/53, or TCP for large responses) for the A/AAAA record.
2. The host ARPs for the default gateway MAC if it is not already cached.
3. A TCP three-way handshake runs to port 443 (SYN → SYN-ACK → ACK).
4. TLS handshake: ClientHello (with SNI), ServerHello, certificate validation, then key exchange.
5. The HTTP request is sent over the encrypted session and the response is rendered.

**TCP vs UDP?**
TCP is connection-oriented, with sequencing, acknowledgements, retransmission and flow control. UDP is connectionless and lower-overhead, used for DNS, DHCP, VoIP, streaming and QUIC.

**What is MTU and why do MTU problems look "random"?**
MTU is the largest L3 packet an interface will send (1500 bytes on standard Ethernet). Tunnels such as IPsec and GRE add overhead, so large packets fail while small ones (pings, the TCP handshake) succeed. You fix it with TCP MSS clamping or a lower MTU, and test with `ping -M do -s 1472` (Linux) or `ping -D -s 1472` (macOS).

---

## Switching

**Access vs trunk port?**
An access port carries one untagged VLAN. A trunk carries multiple VLANs tagged with 802.1Q, plus an untagged native VLAN.

**Why does STP exist?**
Layer 2 has no TTL, so a loop causes broadcast storms and MAC table instability. STP elects a root bridge and blocks redundant paths. RSTP (802.1w) converges in seconds instead of 30–50 s.

**How do hosts in different VLANs talk?**
Through a Layer 3 device: a router-on-a-stick with subinterfaces, or SVIs on a Layer 3 switch.

---

## Routing

**Administrative distance vs metric?**
AD chooses between routing sources (Connected 0, Static 1, eBGP 20, OSPF 110, iBGP 200). The metric chooses between paths from the same protocol. The longest prefix match always wins first.

**OSPF neighbours stuck in EXSTART/EXCHANGE?**
Almost always an MTU mismatch. Stuck in INIT or 2-WAY? Check hello/dead timers, area ID, subnet/mask, authentication, and network type. (2-WAY is normal between DROTHERs.)

**iBGP vs eBGP?**
eBGP peers between different ASes (AD 20, TTL 1 by default). iBGP peers within an AS (AD 200) and does not re-advertise iBGP-learned routes to other iBGP peers, so it needs a full mesh or route reflectors.

**BGP best path selection (Cisco order)?**
Weight → Local Preference → locally originated → AS-path length → Origin → MED → eBGP over iBGP → lowest IGP metric to next hop → oldest route → lowest router ID.

---

## Services

**DHCP process?**
DORA: Discover (broadcast) → Offer → Request → Acknowledge. Across subnets a relay (`ip helper-address`) forwards the broadcast as unicast to the server.

**DNS record types you use daily?**
A, AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), PTR (reverse), NS, SOA, SRV.

**What does NAT break, and how do you work around it?**
End-to-end addressing. It complicates IPsec (solved by NAT-T on UDP/4500) and protocols that embed IPs in the payload (FTP, SIP), which need ALGs. Inbound access needs a destination NAT or a static mapping.

---

## Security

**Stateful firewall vs ACL?**
An ACL checks every packet against static rules. A stateful firewall tracks sessions, so return traffic is allowed automatically and out-of-state packets are dropped.

**IPsec phases?**
IKE Phase 1 builds a secure management channel (IKE SA): authentication, encryption, DH group and lifetime. Phase 2 negotiates the IPsec SAs (ESP) that carry the data, including proxy IDs or traffic selectors. Most failures are Phase 1 parameter mismatches, wrong pre-shared keys, or Phase 2 proxy-ID mismatches.

---

## Troubleshooting Method

1. Define the problem: who, what, since when, what changed.
2. Work bottom-up through the OSI model: link → IP/ARP → routing → firewall/NAT → application.
3. Reproduce the issue and capture evidence (logs, `show` output, packet captures).
4. Change one thing at a time, verify the fix, then document the root cause.
