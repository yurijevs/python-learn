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
# ===========================================

# f1 <-- '255.255.255.0' --> 24
def cidr(netmask):
	return (sum([bin(int(bits)).count("1") for bits in netmask.split(".")]))
# net = input("Введите маску подсети: ")
# print(cidr(net))

# f2 <-- {ip1: '192.169.12.1, 255.255.255.0', ip2: '192.168.12.2', '255.255.255.0'} --> {ip1:'192.168.11.11\24'}
# ips = {"ip1": '192.169.12.1, 255.255.255.0', "ip2": '192.168.12.2, 255.255.255.0'}
# iplist = []
# for k, i in ips.items():
# 	iplist=i.split(',')
# 	si=cidr(iplist[1])
# 	ips[k]=iplist[0]+'\u005C'+str(si)
# print(ips)
# ============================================

# Задания на практику
# 1. Напишите программу, вычисляющую НОД последовательности чисел до 0. Новое число вводится в новой строке. Программа должна использовать функцию gcd.
def gcd(a,b):
	while b != 0:
		a, b = b, a%b
	return a
# x, y = int(input('Введите число x: ')), int(input('Введите число y: '))
# print('Наибольший общий делитель =', gcd(x,y))

# 2. Программа «площадь треугольника»
# a) Напишите функцию Len, вычисляющую длину отрезка по координатам его концов. В эту функцию передается 4 целых числа – координаты точек.
# b) Вторая функция данной программы – square. Она вычисляет площадь треугольника по формуле Герона. В эту функцию передаются 6 целых чисел – координатx x1, y1, x2, y2, x3, y3 вершин треугольника. Она должна использовать функцию Len.
# c) Все данные вводятся в основной программе. Вызовите в ней функцию square. Ответ выведите с точностью до 6 знаков после десятичной точки, отведя под него 10 позиций.
def len(x1,y1,x2,y2):
	lenght = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
	return lenght
def square(x1,y1,x2,y2,x3,y3):
	a = len(x1,y1,x2,y2)
	b = len(x2,y2,x3,y3)
	c = len(x3,y3,x1,y1)
	p = 0.5*(a+b+c)
	s = round((p*(p-a)*(p-b)*(p-c))**0.5, 2)
	if a + b > c and b + c > a and c + a > b: # проверка на существование треугольника
		p = 0.5*(a+b+c)
		s = round((p*(p-a)*(p-b)*(p-c))**0.5, 2)
		return print(f'Площадь треугольника = {s}')
	else:
		return print('Треугольник не существует')

# x1 = float(input('Введите координату x1: '))
# y1 = float(input('Введите координату y1: '))
# x2 = float(input('Введите координату x2: '))
# y2 = float(input('Введите координату y2: '))
# x3 = float(input('Введите координату x3: '))
# y3 = float(input('Введите координату y3: '))
# square(x1,y1,x2,y2,x3,y3)

# 3. С помощью функций напечатайте таблицу умножения
def table(x,y):
    for i in range(1,11):
        for j in range(x,y+1):
            print(f'\t{j} * {i} = {i * j}', end='')
        print()
# x = int(input('Начало таблицы '))
# y = int(input('Конец таблицы '))
# table(x,y)

# ======================================
# Анонимные функции
# Задание на практику
# 1. Написать функцию, которая возвращает минимум и максимум из вводимой до нуля последовательности. Число 0 не учитывать, последовательность вводить внутри функции.
def minmax (*args):
	args = []
	number = None
	while number != 0:
		number = int(input('Введите число, для завершения введите 0: '))
		args.append(number)
	args = args[:-1]
	return print('Минимум последовательности =', min(args), 'Максимум последовательности =', max(args))

# minmax()

# 2. Написать функцию, которая получает произвольное число параметров целых чисел и возвращает их среднее арифметическое.
def sredarif(*args):
	args = list((int(i) for i in args))
	return sum(args)/len(args)

# print(sredarif(1,'2',3))

# 3. Написать функцию Калькулятор: получает на вход 2 числа и символ операции и возвращает результат. Реализовать простые арифметические операции. Воспользоваться lambda-функциями
def calc(x,char,y):
	if char == '+':
		summa = lambda x,y: x+y
		return summa(x,y)
	if char == '-':
		raznost = lambda x,y: x-y
		return raznost(x,y)
	if char == '*':
		proiz = lambda x,y: x*y
		return proiz(x,y)
	if char == '/':
		delen = lambda x,y: x/y
		return delen(x,y)

# x = int(input('x = '))
# y = int(input('y = '))
# char = input('Введите действие (+, -, *, /): ')
# print(x, char, y, '=', calc(x,char,y))