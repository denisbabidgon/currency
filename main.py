# import requests
#
#
# url = f'https://www.cbr-xml-daily.ru/archive/2024/05/14/daily_json.js'
#
#
# response = requests.get(url)
#
# a = response.json()
#
# b = a['Valute']['AUD']['Name']
#
# print(b)










# 1. мы получали ответ в формате json
# 2. проверяли корректность полученных данных
# 3. либо вывели сообщение об ошибке
# 4. чтобы мы сохранили это в "условной базе данных"

# создал папку - и сохранил там полученный json


import json
from datetime import datetime
from funk_game import save_data_about_currency

user_obj = input('Введи дату: ')
user_datetime = datetime.strptime(user_obj, "%d.%m.%Y")

with open(f"currency\\completed_queries.json", "r", encoding="utf-8") as file:
    load_file = json.load(file)
    key = user_datetime.strftime("%d_%m_%Y")
    if key in load_file:
        pass
    else:
        result = save_data_about_currency(user_obj)
        load_file[key] = result

with open(f"currency\\completed_queries.json", "w", encoding="utf-8") as completed:
    json.dump(load_file, completed, indent=4, ensure_ascii=False)

























