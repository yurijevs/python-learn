import socket, netifaces, ipaddress, tabulate
from socket import AddressFamily
def fn_ipaddresses():
    v4 = []
    v6 = []
    for i in netifaces.interfaces():
        cur_ip = i[netifaces.AF_INET][0]['addr']
        # a = ipaddress.ip_address(cur_ip)
        net_prefix = i[netifaces.AF_INET][0]['netmask']
        cidr = (sum([bin(int(bits)).count("1") for bits in mask_4.split(".")]))
        if i[0] == AddressFamily.AF_INET:
            v4.append((cur_ip, cidr))
        else:
            v6.append((cur_ip, net_prefix))
    return {'ipv4': v4, 'ipv6': v6}

ips = fn_ipaddresses()
print(ips)