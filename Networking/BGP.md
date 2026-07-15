# BGP (Border Gateway Protocol)

## What is BGP?

BGP is the routing protocol used between autonomous systems on the Internet.

---

## Types

- eBGP
- iBGP

---

## Path Selection (Simplified)

1. Highest Weight
2. Highest Local Preference
3. Shortest AS Path
4. Lowest MED

---

## Uses

- Internet routing
- Multi-homing
- ISP connectivity

---

## Useful Commands

Cisco:

```bash
show ip bgp
show ip bgp summary
show ip route bgp
```

---

## Interview Question

Difference between OSPF and BGP?

OSPF is an Interior Gateway Protocol (IGP) used within an organization. BGP is an Exterior Gateway Protocol (EGP) used between autonomous systems.
