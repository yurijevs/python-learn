# Импортируем библиотеки

import socket
import netifaces
from tabulate import tabulate

def fn_ipaddresses():
    v4 =[]
    v6 = []
    for i in netifaces.interfaces():
        addresses = netifaces.ifaddresses(i)
        adr = addresses.get(netifaces.AF_INET, [])
        for j in adr:
            netmask = j.get("netmask")
            prefix = sum(bin(int(x)).count('1') for x in netmask.split('.'))
            v4.append((j.get('addr'), prefix))

        adr = addresses.get(netifaces.AF_INET6, [])

        for j in adr:
            netmask = j.get("netmask")
            bitCount = [0, 0x8000, 0xc000, 0xe000, 0xf000, 0xf800, 0xfc00, 0xfe00, 0xff00, 0xff80, 0xffc0, 0xffe0,
                        0xfff0, 0xfff8, 0xfffc, 0xfffe, 0xffff]
            count = 0
            try:
                for w in netmask.split(':'):
                    if not w or int(w, 16) == 0 :
                        break
                    count += bitCount.index(int(w, 16))
            except:
                pass
            v6.append((j.get('addr'), count))
    return {'ipv4': v4, 'ipv6': v6}

def fn_portscan(ips):
    v4 = ips.get('ipv4')
    v6 = ips.get('ipv6')
    data = v4
    rows_open = []
    rows_close = []
    for i in data:
        ip = i[0]
        close_ports = []
        open_ports = []
        for port in range(1, 200):

            sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockt.settimeout(0.001)
            try:
                connect = sockt.connect((ip, port))
                open_ports.append(str(port))
                connect.close()
            except:
                close_ports.append(str(port))
        rows_open.append(f'IP-адрес: {ip}, порты: {",".join(open_ports)}')
        rows_close.append(f'IP-адрес: {ip}, порты: {",".join(close_ports)}')

    data = v6
    for i in data:
        ip = i[0]
        close_ports = []
        open_ports = []
        for port in range(1, 200):
            sockt = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            sockt.settimeout(0.001)
            try:
                connect = sockt.connect((ip, port))
                open_ports.append(str(port))
                connect.close()
            except:
                close_ports.append(str(port))
        rows_open.append(f'IP-адрес: {ip}, порты: {",".join(open_ports)}')
        rows_close.append(f'IP-адрес: {ip}, порты: {",".join(close_ports)}')
    with open('open_ports.txt', 'w') as f:
        f.write('\n'.join(rows_open))
    with open('close_ports.txt', 'w') as f:
        f.write('\n'.join(rows_close))

    return [('open_ports.txt', len(rows_open)), ('close_ports.txt', len(rows_close))]

def fn_ipaccess(ips):
    accessed = []
    not_accessed = []
    for i in ips:
        from subprocess import PIPE, Popen
        res = Popen(f"ping -n 1 {i}", shell=True, stdout=PIPE)
        out = str(res.communicate()[0].decode("CP866"))

        if out.find("100% потерь") == -1:
            accessed.append(i)
        else:
            not_accessed.append(i)

    return accessed, not_accessed

def main():
    ips = fn_ipaddresses()
    print(tabulate(ips, headers="keys", tablefmt='grid', stralign="left"))
    data = fn_portscan(ips)
    print(data)
    temp_list = ips['ipv4']
    temp_list = [item for t in temp_list for item in t]
    ipv4list = []
    for i in temp_list:
        if type(i) is not int:
            ipv4list.append(i)
    data = fn_ipaccess(ipv4list)
    result = {"Доступные": data[0], "Не доступные": data[1]}
    print(tabulate(result, headers="keys", tablefmt='grid', stralign="left"))

if __name__ == '__main__':
    main()