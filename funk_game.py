import requests
import os

import json
from datetime import datetime

def check_currrency_data(user_date_string: str) -> bool:
    try:
        datetime.strptime(user_date_string, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def getrightpath(foldername: str = 'currency', __file=None) -> str:
    """Функция призвана сформировать абсолютный путь до папки,
    которая указана в качестве аргумента в зависимости от ОС, на которой выполняется запуск"""
    path_to_current_file = os.path.abspath(__file)
    seperator = '/' if os.name == 'posix' else '\\'
    path_list = path_to_current_file.split(seperator)

    path_list[-1] = foldername

    return seperator.join(path_list) + seperator

def save_data_about_currency(user_input: str) -> bool:
    """Выдает курс валют на данное число которое ввел пользователь, если курса на число нет то ничего не произойдет"""
    user_data = datetime.strptime(user_input, "%d.%m.%Y")

    url = f'https://www.cbr-xml-daily.ru/archive/{user_data.strftime("%Y/%m/%d")}/daily_json.js'

    response = requests.get(url)
    status = response.status_code
    if status != 200:
        return False
    else:
        fiile = user_data.strftime(f'%d_%m_%Y')
        with open(f"currency\\{fiile}.json", 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)
    return True





