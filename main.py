import requests

import json
from datetime import datetime

from additional_function_for_app import save_data_about_currency, check_correctly_date, get_right_path
from additional_function_for_app import get_info_about_response, save_all_responses

user_date_string = input('Введи дату: ')

if check_correctly_date(user_date_string):
    user_date_datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
    key = user_date_datetime.strftime('%d_%m_%Y')

    info_response = get_info_about_response(key)
    completed_response = info_response['all_data']

    print(info_response['flag'])

    if info_response['flag'] == 'Требуется выполнить запрос!':
        flag_response = save_data_about_currency(user_date_datetime)
        completed_response[key] = flag_response

    save_all_responses(completed_response)

else:
    print('Ты ввел что-то не похожее на дату')



























