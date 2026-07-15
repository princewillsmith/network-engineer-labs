"""
Simple network configuration backup example.
"""

devices = [
    "Switch-1",
    "Router-1",
    "Firewall-1"
]

for device in devices:
    print(f"Backing up configuration from {device}...")
    print("Backup completed.\n")
