# import json
#
# with open('currency/30_05_2024.json', 'r', encoding='utf-8') as file:
#     curr: dict = json.load(file)
#
# # curr <- что это за переменная
# # что там хранится
# # какой тип данных
# # и как этот объект можно проиттерировать?
#

# curr = 'string'
#
# for i in curr.items():
#     print(i)


# with open('test_file.txt', 'w', encoding='utf-8') as file:
#     print(file.read())


import os

if os.path.isfile('currency/091_05_2024.json'):
    print('Такой файл существует')
else:
    print('Такого файла НЕ существует')