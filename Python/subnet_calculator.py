import ipaddress

network = ipaddress.ip_network("192.168.10.0/24")

print("Network Address :", network.network_address)
print("Broadcast Address :", network.broadcast_address)
print("Subnet Mask :", network.netmask)
print("Number of Hosts :", network.num_addresses)


# sample output
Network Address : 192.168.10.0
Broadcast Address : 192.168.10.255
Subnet Mask : 255.255.255.0
Number of Hosts : 256
