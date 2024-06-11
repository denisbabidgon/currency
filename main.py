import requests

import json
from datetime import datetime

from additional_function_for_app import save_data_about_currency, check_correctly_date


user_date_string = input('Введи дату: ')
if check_correctly_date(user_date_string):
    user_date_datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
    with open('currency/completed_response.json', 'r', encoding='utf-8') as file:
        completed_response: dict = json.load(file)
        # key - это строка, которую мы будем искать в нашем json и строка по которой будем записывать результат запроса
        key = user_date_datetime.strftime('%d_%m_%Y')
        if key in completed_response:
            # мы сюда провалимся только в том случае, если запрос уже проходил!
            print('ничего никуда не отправляется!')

        else:
            response_result = save_data_about_currency(user_date_datetime)
            completed_response[key] = response_result

    with open('currency/completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(completed_response, file, indent=4, ensure_ascii=False)
else:
    print('Ты ввел что-то не похожее на дату')



























