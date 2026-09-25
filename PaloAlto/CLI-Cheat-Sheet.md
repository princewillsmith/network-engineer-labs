# Palo Alto Networks CLI Cheat Sheet

Commands I used daily on PAN-OS firewalls in TAC and operations work.

---

## Sessions and Policy

```bash
show session all filter source 10.1.1.10 destination 8.8.8.8
show session id <id>                      # rule, NAT, zones, app, state
test security-policy-match from trust to untrust source 10.1.1.10 destination 8.8.8.8 protocol 6 destination-port 443
test nat-policy-match from trust to untrust source 10.1.1.10 destination 8.8.8.8 protocol 6 destination-port 443
show running security-policy
```

## Drops and Counters

```bash
show counter global filter delta yes severity drop
show counter global filter delta yes packet-filter yes   # after setting a packet filter
```

## Packet Capture (packet-diag)

```bash
debug dataplane packet-diag set filter match source 10.1.1.10 destination 8.8.8.8
debug dataplane packet-diag set filter on
debug dataplane packet-diag set capture stage receive file rx.pcap
debug dataplane packet-diag set capture stage firewall file fw.pcap
debug dataplane packet-diag set capture stage transmit file tx.pcap
debug dataplane packet-diag set capture stage drop file drop.pcap
debug dataplane packet-diag set capture on
# ... reproduce the issue ...
debug dataplane packet-diag set capture off
debug dataplane packet-diag clear all
```

## Routing and Interfaces

```bash
show routing route destination 8.8.8.8
show routing fib
test routing fib-lookup virtual-router default ip 8.8.8.8
show interface ethernet1/1
show arp all
```

## IPsec VPN

```bash
show vpn ike-sa gateway <gw-name>
show vpn ipsec-sa tunnel <tunnel-name>
test vpn ike-sa gateway <gw-name>
test vpn ipsec-sa tunnel <tunnel-name>
less mp-log ikemgr.log
```

## GlobalProtect

```bash
show global-protect-gateway current-user
show global-protect-gateway statistics
less mp-log gpsvc.log
less mp-log rasmgr.log
```

## System Health

```bash
show system info
show system resources follow
show running resource-monitor
show high-availability state
show jobs all
less mp-log ms.log
```

---

## Packet Flow (Simplified)

1. Ingress: L2/L3 parsing, zone and session lookup
2. **New session:** DoS/zone protection → forwarding lookup → NAT policy lookup (the translated address is determined here) → security policy lookup (pre-NAT IPs, post-NAT zone) → session installed
3. **Existing session:** fast path, with App-ID and Content-ID inspection
4. Egress: NAT applied, forwarded out
