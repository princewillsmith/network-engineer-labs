# Network Address Translation (NAT)

## What is NAT?

NAT translates one IP address into another.

It allows private IP addresses to communicate with public networks.

---

## Types of NAT

### Source NAT

Changes the source IP address.

Example:

```
192.168.1.10
↓

203.0.113.5
```

---

### Destination NAT

Changes the destination IP address.

Example:

```
Public IP

↓

Internal Server
```

---

## NAT Rule Components

- Original Source
- Original Destination
- Service
- Translated Source
- Translated Destination

---

## NAT Processing

1. Packet arrives.
2. Security policy lookup.
3. NAT rule matched.
4. Address translation.
5. Packet forwarded.

---

## Troubleshooting

- Verify NAT rule order.
- Verify zones.
- Verify interfaces.
- Check translated address.
- Review traffic logs.
- Use packet capture if necessary.

---

## Useful CLI Commands

```bash
show running nat-policy
show session all
```

---

## Interview Question

Difference between Source NAT and Destination NAT?

Source NAT changes the source IP. Destination NAT changes the destination IP.
