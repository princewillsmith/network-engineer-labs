# Linux Networking

Linux provides several commands for configuring and troubleshooting network connectivity.

## Check IP Address

```bash
ip addr
```

Displays all network interfaces and their IP addresses.

---

## Show Routing Table

```bash
ip route
```

Displays the routing table.

---

## Test Connectivity

```bash
ping 8.8.8.8
```

Tests whether a remote host is reachable.

---

## Check DNS Resolution

```bash
nslookup google.com
```

or

```bash
dig google.com
```

Resolves a hostname to an IP address.

---

## View Listening Ports

```bash
ss -tulnp
```

Shows TCP and UDP ports currently listening.

---

## Check Network Interfaces

```bash
ip link show
```

Lists all network interfaces.

---

## Display ARP Table

```bash
ip neigh
```

Shows IP-to-MAC address mappings.

---

## Trace the Network Path

```bash
traceroute google.com
```

Displays the path packets take to reach the destination.
