# GlobalProtect VPN

## What is GlobalProtect?

GlobalProtect is Palo Alto Networks' VPN solution that provides secure remote access to corporate resources.

---

## Components

- GlobalProtect Portal
- GlobalProtect Gateway
- GlobalProtect Agent

### Portal
- Authenticates users
- Provides gateway information

### Gateway
- Establishes VPN tunnels
- Enforces security policies

### Agent
- Installed on the user's device
- Connects to the portal and gateway

---

## Connection Process

1. User launches GlobalProtect.
2. Agent connects to the Portal.
3. User authenticates.
4. Portal sends Gateway information.
5. Agent connects to the Gateway.
6. VPN tunnel is established.

---

## Common Issues

### VPN Connection Failed

Possible causes:

- Incorrect credentials
- Certificate issues
- Gateway unavailable
- Internet connectivity problems
- Firewall policy blocking traffic

---

### User Cannot Connect

Checklist:

- Verify internet connectivity
- Verify portal is reachable
- Check gateway status
- Review authentication logs
- Review GlobalProtect logs
- Verify certificates
- Compare with a working user

---

## Useful CLI Commands

```bash
show global-protect-gateway current-user
show global-protect-gateway statistics
```

---

## Interview Question

What is the difference between the Portal and Gateway?

The Portal authenticates users and tells the agent which Gateway to use. The Gateway establishes the VPN tunnel and provides secure access to resources.
