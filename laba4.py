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

f = "file.txt"
print(filetolist(f))
print(filetodict(f))