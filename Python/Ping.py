"""
Ping a list of devices to check if they are reachable.
"""

import subprocess

devices = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

for device in devices:
    print(f"Pinging {device}...")

    result = subprocess.run(
        ["ping", "-c", "2", device],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode == 0:
        print(f"{device} is reachable\n")
    else:
        print(f"{device} is NOT reachable\n")
