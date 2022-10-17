import socket, netifaces, ipaddress, tabulate
from socket import AddressFamily
def fn_ipaddresses():
    v4 = []
    v6 = []
    for i in socket.getaddrinfo(socket.gethostname(), None):
        cur_ip = i[4][0]
        a = ipaddress.ip_network(cur_ip)
        net_prefix = a.prefixlen
        if i[0] == AddressFamily.AF_INET:
            v4.append((cur_ip, net_prefix))
        else:
            v6.append((cur_ip, net_prefix))
    return {'ipv4': v4, 'ipv6': v6}

ips = fn_ipaddresses()
print(ips)







# def fn_ipaddresses(interface):
# 	adresses = netifaces.ifaddresses(interface)
# 	addr_4 = adresses[netifaces.AF_INET][0]['addr']
# 	mask_4 = adresses[netifaces.AF_INET][0]['netmask']
# 	cidr4 = (sum([bin(int(bits)).count("1") for bits in mask_4.split(".")]))
# 	addr_6 = adresses[netifaces.AF_INET6][0]['addr']
# 	pref_6 = adresses[netifaces.AF_INET6][0]['netmask']
# 	adresses_6 = adresses[netifaces.AF_INET6][0]
# 	print(addr_4, cidr4)
# 	print(addr_6, pref_6)
# 	# print(adresses)
#
# interfaces = netifaces.interfaces()
# print('Доступные сетевые интерфейсы:', *interfaces)
# interface = input('Выберете интерфейс: ')
# if interface in interfaces:
# 	fn_ipaddresses(interface)
# else:
# 	print("Неправильный интерфейс")

# def fn_ipaddresses():
#     interfaces = netifaces.interfaces()
#     for interface in interfaces:
#         adresses = netifaces.ifaddresses(interface)
#     print(adresses)
# fn_ipaddresses()
# def get_interfaces():
#
#     interfaces = netifaces.interfaces()
#     interfaces.remove('lo0')
#
#     out_interfaces = dict()
#
#     for interface in interfaces:
#         addrs = netifaces.ifaddresses(interface)
#         out_addrs = dict()
#         if netifaces.AF_INET in addrs.keys():
#             out_addrs["ipv4"] = addrs[netifaces.AF_INET]
#         if netifaces.AF_INET6 in addrs.keys():
#             out_addrs["ipv6"] = addrs[netifaces.AF_INET6]
#         out_interfaces[interface] = out_addrs
#
#     print(out_interfaces)
# get_interfaces()