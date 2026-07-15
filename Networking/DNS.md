# DNS (Domain Name System)

## What is DNS?

DNS translates domain names into IP addresses.

Example:

google.com → 142.x.x.x

---

## Common DNS Records

| Record | Purpose |
|---------|----------|
| A | IPv4 Address |
| AAAA | IPv6 Address |
| CNAME | Alias |
| MX | Mail Server |
| TXT | Verification/SPF |
| NS | Name Server |

---

## DNS Resolution Process

1. Client checks cache
2. Recursive DNS server
3. Root server
4. TLD server
5. Authoritative DNS server
6. IP returned to client

---

## Useful Commands

```bash
nslookup google.com
dig google.com
host google.com
```

---

## Troubleshooting

- Flush DNS cache
- Verify DNS server
- Test another DNS server (8.8.8.8)
- Check firewall rules

---

## Interview Question

What is the difference between recursive and iterative DNS queries?

Recursive queries require the DNS server to return the final answer. Iterative queries return the best information available and refer the client to another server.
