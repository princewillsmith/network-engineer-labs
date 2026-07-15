# DHCP (Dynamic Host Configuration Protocol)

## Purpose

DHCP automatically assigns IP addresses to clients.

---

## DORA Process

1. Discover
2. Offer
3. Request
4. Acknowledge

---

## Information Assigned

- IP Address
- Subnet Mask
- Default Gateway
- DNS Server
- Lease Time

---

## Useful Commands

Linux:

```bash
dhclient
```

Windows:

```cmd
ipconfig /renew
ipconfig /release
```

---

## Troubleshooting

- Verify DHCP server
- Check VLAN configuration
- Verify relay agent
- Check lease availability

---

## Interview Question

What is the DORA process?

Discover → Offer → Request → Acknowledge.
