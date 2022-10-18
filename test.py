import zachet
from tabulate import tabulate

print('test')
data = (zachet.fn_ipaccess(['127.0.0.1', '192.168.67.1']))
result = {"Доступные": data[0], "Не доступные": data[1]}
print(tabulate(result, headers="keys", tablefmt='grid', stralign="left"))