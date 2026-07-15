import ipaddress

network = ipaddress.ip_network("192.168.10.0/24")

print("Network Address :", network.network_address)
print("Broadcast Address :", network.broadcast_address)
print("Subnet Mask :", network.netmask)
print("Number of Hosts :", network.num_addresses)
