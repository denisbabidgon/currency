import requests

import json
from datetime import datetime

from additional_function_for_app import check_correctly_date, get_answer_about_next_response


user_date_string = input('Введи дату: ')

if check_correctly_date(user_date_string):
    user_date: datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
    key: str = user_date.strftime('%d_%m_%Y')

    result = get_answer_about_next_response(user_date, key)

    print(result)

else:
    print('Ты ввел что-то не похожее на дату')



























