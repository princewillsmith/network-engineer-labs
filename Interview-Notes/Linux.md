# Linux Interview Notes

Commands and answers I use when troubleshooting servers and network appliances.

---

## Networking Commands

| Task | Command |
|---|---|
| Show IP addresses | `ip addr` / `ip -br a` |
| Show routes | `ip route` / `ip route get 8.8.8.8` |
| Listening ports + process | `ss -tulpn` |
| Established connections | `ss -tn state established` |
| ARP / neighbour table | `ip neigh` |
| DNS lookup | `dig example.com +short`, `dig @8.8.8.8 example.com` |
| Path tracing | `traceroute`, `mtr -rw example.com` |
| Packet capture | `tcpdump -i eth0 -nn host 10.0.0.5 and port 443 -w cap.pcap` |
| Test a TCP port | `nc -vz host 443` |
| Firewall rules | `iptables -L -n -v`, `nft list ruleset` |

---

## Common Questions

**A service isn't reachable on port 8080. How do you troubleshoot?**
1. Is it running? `systemctl status app`, `journalctl -u app -e`.
2. Is it listening, and on which address? `ss -tlnp | grep 8080`. `127.0.0.1:8080` is local only, `0.0.0.0:8080` is all interfaces.
3. Is the host firewall blocking it? `iptables`/`nft`/`firewalld`.
4. Is it reachable from the client? `nc -vz`, then `tcpdump` on the server to see whether the SYNs arrive.
5. Check network devices in the path (security groups, firewalls, NAT).

**Disk is full, but `du` doesn't add up. Why?**
A process still holds a deleted file open. Find it with `lsof +L1` and restart the process or truncate the file.

**What does load average mean?**
The average number of processes running or waiting (including uninterruptible I/O wait) over 1, 5 and 15 minutes. Compare it with the CPU count (`nproc`).

**File permissions: what is 750?**
Owner rwx (7), group r-x (5), others none (0). Special bits: SUID (4xxx), SGID (2xxx), sticky (1xxx, as on `/tmp`).

**How do you find which process uses the most memory?**
`ps aux --sort=-%mem | head`, or `top` then `Shift+M`.

**Where are logs?**
`journalctl` (systemd), `/var/log/syslog` or `/var/log/messages`, `/var/log/auth.log` or `/var/log/secure` (SSH/sudo, which are key for security investigations).

---

## Security-Focused

**How do you check for suspicious logins?**
`last`, `lastb`, `journalctl -u sshd`, and `grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn`.

**How do you harden SSH?**
Key-based auth only (`PasswordAuthentication no`), `PermitRootLogin no`, restrict `AllowUsers`/`AllowGroups`, add fail2ban, and limit access by source IP.
