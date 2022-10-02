# Задание 1
# Обработать строку nat таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet
# nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# nat_new = nat.replace("FastEthernet", "GigabitEthernet")
# print(nat_new)

# Задание 2
# Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
# mac = 'AAAA:BBBB:CCCC'
# mac_new = mac.replace(":", ".")
# print(mac_new)

# Задание 3
# Получить из строки config список VLANов вида: ['1','3','10','20','30','100']
# config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# string = config.split()
# vlans = string[-1]
# vlan_list = vlans.split(",")
# print(vlan_list)

# Задание 4
# Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров
# vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# vlans2 = set(vlans)
# vlans2 = list(vlans2)
# vlans2.sort()
# print(vlans2)

# Задание 5
# Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.
# Результатом должен быть список:['1','3','8']
# command1 = "switchport trunk allowed vlan 1,2,3,5,8"
# command2 = "switchport trunk allowed vlan 1,3,8,9"
# string1 = command1.split()
# string2 = command2.split()
# vlans1 = string1[-1]
# vlans2 = string2[-1]
# vlans1 = vlans1.split(",")
# vlans2 = vlans2.split(",")
# print(list(set(vlans1) & set(vlans2)))

# Задание 6
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
# Protocol:               OSPF
# Prefix:                 10.0.24.0/24
# AD/Metric:              110/41
# Next-Hop:               10.0.13.3
# Last update:            3d18h
# Outbound Interface:     FastEthernet0/0
# ospf_route = '10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
# string = ospf_route.split()
# print('Protocol:\t', 'OSPF')
# print('Prefix:\t',string[0])
# print('AD/Metric:\t',string[1])
# print('Next-Hop:\t',string[3][:-1])
# print('Last update:\t',string[4][:-1])
# print('Outbound Interface:\t',string[5])

# Задание 7
# Преобразовать MAC-адрес mac в двоичную строку такого вида:101010101010101010111011101110111100110011001100
# mac = '50ed:3c52:4654'
# hex_string = mac.split(":")
# new_mac = hex_string[0] + hex_string[1] + hex_string[2]
# print(bin(int(new_mac, 16)))

# Задание 8
# Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
# * первой строкой должны идти десятичные значения байтов
# * второй строкой двоичные значения
# Вывод должен быть упорядочен также, как в примере:
# * столбцами
# * ширина столбца 10 символов
# Пример вывода для адреса 10.1.1.1:
# 10        1         1         1
# 00001010  00000001  00000001  00000001
# ip = '192.168.3.1'
# ip_string = ip.split(".")
# template_int = '''{0:<10} {1:<10} {2:<10} {3:<10}'''
# template_bin = '''{0:08b}   {1:08b}   {2:08b}   {3:08b}'''
# print(template_int.format(ip_string[0],ip_string[1],ip_string[2],ip_string[3]))
# print(template_bin.format(int(ip_string[0]), int(ip_string[1]), int(ip_string[2]), int(ip_string[3]),))