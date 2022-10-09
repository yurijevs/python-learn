import os
from pickle import REDUCE

from laba3 import numberlen

# Самостоятельная работа
# Создайте функцию, которая на вход получает имя файла - f
def filetolist(f):
	nums = []
	with open(f, "rt") as file:
		for i in file:
			nums.append(i.strip())
	return nums
def filetodict(f):
	slov = {}
	key = 1
	with open(f, "rt") as file:
		for i in file:
			slov[key] = i.strip()
			key += 1
	return slov

# f = "file.txt"
# print(filetolist(f))
# print(filetodict(f))
# =================================
# функция получает имя файла и строку пишет строку в конец файла и закрывает файл
def writetofile(filename,string):
	with open(filename, "at") as file:
 		file.write(string + "\n")
# filename = input('введите имя файла: ')
# string = input('введите строку: ')
# writetofile(filename,string)
# print(filetodict(filename))
def writetofilebylines(filename, string):
	with open(filename, "wt") as file:
		file.seek(0,2)
		file.writelines(string)

# filename = input('введите имя файла: ')
# string = []
# userinput = None
# while userinput != "0":
# 	userinput = input('введите ip адрес и маску, для окончания введите 0: ')
# 	if userinput != "0":
# 		string.append(userinput + "\n")
# writetofilebylines(filename,string)
# print(filetolist(filename))

# Задание на практику
# Скачайте с сайта lib.ru любой текстовый документ и сохраните его под именем doc.txt.
# - Проверьте кодировку.
# - Напишите программу, которая сделает копию данного файла и сохранит ее в файл doc1.txt
# - Посчитайте сколько слов содержит сохраненный файл.
def showenc(filename):
	with open(filename, "rt") as file:
		enc = file.encoding
	return enc

# filename = input('Введите имя файла: ')
# print('Кодировка файла', '-', showenc(filename))

def copyfile(filename, copy):
	f = open(filename, "rt")
	copy = open(copy, "wt")
	f_content = f.read()
	print(f_content, file=copy)
	f.close()
	copy.close()

# filename = input('Введите имя файла: ')
# copy = input('Введите имя нового файла: ')
# copyfile(filename, copy)

def word_count(filename):
	with open(filename, "rt") as file:
		f_content = file.read()
		words = f_content.split()
		count_words = len(words)
	return count_words

# filename = input('Введите имя файла: ')
# print('Количество слов:', word_count(filename))

# В файле input.txt в разнобой записаны целые числа. Напишите программу, которая создаст файл output.txt и запишет в него сумму этих чисел.
def sum_files(filename):
	number_list = []
	with open(filename, "rt") as file:
		number_list = file.read().split()
		number_list = list(map(int, number_list))
	return sum(number_list)

# filename = 'input.txt'
# with open('output.txt', "wt") as file:
# 	print(sum_files(filename), file=file)	
# =============================================

# Задачи дополнительно

# С клавиатуры через пробел вводится список целых чисел. Запишите его в файл с именем list1.txt. Затем перенесите из этого файла в файл list2.txt все числа, которые стоят на четных местах. Позиции нумеровать с единицы


# Создайте текстовый файл с произвольным наполнением. Узнайте, сколько символов в нем содержится. Символы перевода строки ‘\n’ учитывать не надо


# Напишите программу, которая копирует данные из одного файла в другой, но в обратном порядке. То есть в новом файле сначала идет последняя строка из старого
def reversefile(inputfile, outputfile):
	with open(inputfile, "rt") as infile:
		string = infile.readlines()
		string = reversed(string)
		with open(outputfile, "wt") as outfile:
			for i in string:
				outfile.write(i)
# inputfile = input("Введите имя файла1: ")
# outputfile = input("Введите имя файла2: ")
# reversefile(inputfile, outputfile)


# Напишите функцию delete_file(f), удаляющую из файла f все символы ‘+’ и ‘-’
def delete_file(f):
	with open(f, "rt") as file:
		f_content = file.read()
		f_content = f_content.replace("+", "")
		f_content = f_content.replace("-", "")
	with open(f, "wt") as file:
		file.write(f_content)

# f = input("Введите имя файла: ")
# delete_file(f)
