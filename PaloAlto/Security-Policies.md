# Palo Alto Security Policies

## What is a Security Policy?

A Security Policy determines whether traffic is allowed or denied.

---

## Policy Match Criteria

- Source Zone
- Destination Zone
- Source Address
- Destination Address
- Application
- Service
- User

---

## Rule Order

Policies are evaluated from the top down.

The first matching rule is applied.

---

## Best Practices

- Use Applications instead of ports.
- Keep rules specific.
- Remove unused rules.
- Log important traffic.
- Follow the principle of least privilege.

---

## Troubleshooting

If traffic is denied:

- Verify rule order.
- Verify zones.
- Verify application.
- Verify service.
- Check security logs.
- Verify User-ID if used.

---

## Useful CLI Commands

```bash
show running security-policy
show log traffic
```

---

## Interview Question

How are Security Policies evaluated?

Policies are processed from top to bottom. The first matching rule is applied.
