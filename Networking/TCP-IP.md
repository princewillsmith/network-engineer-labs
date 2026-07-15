# TCP/IP

## What is TCP/IP?

TCP/IP (Transmission Control Protocol/Internet Protocol) is the standard suite of communication protocols used for networking and the Internet.

---

## TCP/IP Layers

| Layer | Function |
|--------|----------|
| Application | HTTP, HTTPS, DNS, FTP, SSH |
| Transport | TCP, UDP |
| Internet | IP, ICMP |
| Network Access | Ethernet, Wi-Fi |

---

## TCP vs UDP

| TCP | UDP |
|-----|-----|
| Connection-oriented | Connectionless |
| Reliable | Faster but no guarantee |
| Uses acknowledgements | No acknowledgements |
| Ordered delivery | No ordering |
| Examples: HTTP, HTTPS, SSH | Examples: DNS, VoIP, DHCP |

---

## TCP Three-Way Handshake

1. SYN
2. SYN-ACK
3. ACK

This establishes a reliable connection before data is transmitted.

---

## Common Ports

| Protocol | Port |
|----------|------|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| FTP | 21 |
| DNS | 53 |
| DHCP | 67/68 |
| SMTP | 25 |

---

## Useful Commands

```bash
netstat -tulnp
ss -tulnp
ip addr
ip route
```

---

## Interview Questions

### What is the difference between TCP and UDP?

TCP is reliable and connection-oriented. UDP is faster but connectionless and does not guarantee delivery.

### What is the TCP three-way handshake?

SYN → SYN-ACK → ACK.
