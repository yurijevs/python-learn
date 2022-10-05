import os

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

