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


# import json
# from datetime import datetime
# from funk_game import save_data_about_currency
#
#
# user_obj = input('Введи дату: ')
# user_datetime = datetime.strptime(user_obj, "%d.%m.%Y")
#
# with open(f"currency\\completed_queries.json", "r", encoding="utf-8") as file:
#     load_file = json.load(file)
#     key = user_datetime.strftime("%d_%m_%Y")
#     if key in load_file:
#         pass
#     else:
#         result = save_data_about_currency(user_obj)
#         load_file[key] = result
#
# with open(f"currency\\completed_queries.json", "w", encoding="utf-8") as completed:
#     json.dump(load_file, completed, indent=4, ensure_ascii=False)






import json
from datetime import datetime

from funk_game import save_data_about_currency, check_currrency_data, getrightpath


user_date_string = input('Введи дату: ')
if check_currrency_data(user_date_string):
    user_date_datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
    with open(f'{getrightpath()}completed_response.json', 'r', encoding='utf-8') as file:
        completed_response: dict = json.load(file)
        key = user_date_datetime.strftime('%d%m_%Y')
        if key in completed_response:
            print('ничего никуда не отправляется!')
        else:
            response_result = save_data_about_currency(user_date_datetime)
            completed_response[key] = response_result

    with open(f'{getrightpath()}completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(completed_response, file, indent=4, ensure_ascii=False)
else:
    print('Ты ввел что-то не похожее на дату')


















