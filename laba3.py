# Задание на самостоятельную работу
# 1. Напишите функцию, в которую поступает число N и которая возвращает количество цифр в этом числе
def numberlen(num):
	if num.isdigit() == True:
		return len(num)
	else:
		return 0
# n = numberlen(input())
# print(n)
# 2. Вводятся натуральные числа N и K. Напишите функцию, которая возвращает количество цифр K в числе N.
def finddigit(n,k):
	if n.isdigit() == True and k.isdigit() == True and len(k) == 1:
		count = n.count(k)
		return count
	else:
		return 0
# n = input('Введите число n: ')
# k = input('Введите число k: ')
# print(finddigit(n,k))
# 3. Дана строка, содержащая буквы и цифры. Подсчитайте количество цифр в данной строке (*количество уникальных цифр).
def countnum(string):
	countnum = []
	countstr = []
	countset = []
	for c in string:
		if c.isdigit():
			countnum.append(c)
		else:
			countstr.append(c)
	countset = len(set(countnum))
	countnum = len(countnum)
	countstr = len(countstr)
	return f'Количество цифр: {countnum}, количество нецифр: {countstr}, количество уникальных цифр: {countset}'
# string = input("Введите строку: ")
# print(countnum(string))

# f1 <-- '255.255.255.0' --> 24
def cidr(netmask):
	return (sum([bin(int(bits)).count("1") for bits in netmask.split(".")]))
# net = input("Введите маску подсети: ")
# print(cidr(net))

# f2 <-- {ip1: '192.169.12.1, 255.255.255.0', ip2: '192.168.12.2', '255.255.255.0'} --> {ip1:'192.168.11.11/24'}

# 2. Написать функцию, которая получает произвольное число параметров целых чисел и возвращает их среднее арифметическое.
def sredarif(*args):
	args = list((int(i) for i in args))
	return sum(args)/len(args)

# print(sredarif(1,'2',3))




