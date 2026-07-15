# Palo Alto Troubleshooting

## Step 1 - Define the Problem

- What is failing?
- One user or multiple users?
- Internal or external?
- Since when?

---

## Step 2 - Verify Connectivity

- Ping
- Traceroute
- DNS resolution
- Gateway reachability

---

## Step 3 - Review Logs

Check:

- Traffic Logs
- Threat Logs
- System Logs
- GlobalProtect Logs

---

## Step 4 - Verify Policies

- Security Policy
- NAT Policy
- Decryption Policy

---

## Step 5 - Session Information

Useful CLI:

```bash
show session all
show session id
```

---

## Step 6 - Packet Capture

Capture traffic at:

- Receive
- Firewall
- Transmit
- Drop

---

## Common Issues

### VPN Not Connecting

- Verify portal
- Verify gateway
- Verify certificates
- Check authentication
- Review GP logs

---

### Traffic Denied

- Review Traffic Logs
- Check Security Policy
- Verify NAT
- Verify routing

---

### Slow Internet

- Check interface utilization
- Check CPU
- Check session count
- Review QoS

---

## Troubleshooting Method

1. Gather information.
2. Reproduce the issue.
3. Analyze logs.
4. Identify root cause.
5. Apply fix.
6. Verify the solution.
7. Document the incident.
