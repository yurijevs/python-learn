import socket, netifaces
from socket import AddressFamily
v4 = []
v6 = []
for i in netifaces.interfaces():
	cur_ip = i[netifaces.AF_INET][0]['addr']
	net_prefix = i[netifaces.AF_INET][0]['netmask']
	if i[0] == AddressFamily.AF_INET:
		v4.append((cur_ip))
	else:
		v6.append((cur_ip))
print(v4, v6)
