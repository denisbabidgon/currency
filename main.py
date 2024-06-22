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
import json
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



from datetime import datetime

from funk_game import check_currrency_data, get_answer_about_next_response,get_right_path


user_date_string = input('Введи дату: ')

if check_currrency_data(user_date_string):
    user_date: datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
    key: str = user_date.strftime('%d_%m_%Y')

    result = get_answer_about_next_response(user_date, key)
    if result == 'Данные найдены!':
        with open(f"{get_right_path()}{key}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            print(data)

    print(result)

else:
    print('Ты ввел что-то не похожее на дату')





















