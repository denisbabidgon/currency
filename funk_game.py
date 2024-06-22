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



def get_right_path(folder_name: str = 'currency') -> str:
    """Функция призвана сформировать абсолютный путь до папки,
        которая указана в качестве аргумента в зависимости от ОС, на которой выполняется запуск"""
    path_to_current_file = os.path.abspath(__file__)
    seperator = '/' if os.name == 'posix' else '\\'
    path_list = path_to_current_file.split(seperator)

    path_list[-1] = folder_name

    return seperator.join(path_list) + seperator

def get_answer_about_next_response(user_date: datetime, key: str) -> str:
    info_response: dict = get_info_about_response(key)
    completed_response: dict = info_response['all_data']

    if info_response['flag'] == 'Требуется выполнить запрос!':
        flag_response: bool = save_data_about_currency(user_date)
        completed_response[key] = flag_response

        save_all_responses(completed_response)

    return info_response['flag']

def get_info_about_response(data_key: str) -> dict:
    with open(f'{get_right_path()}completed_response.json', 'r', encoding='utf-8') as file:
        completed_response: dict = json.load(file)

    result_dict: dict = {
        'flag': '',
        'all_data': completed_response,
    }

    if data_key in completed_response:
        flag = completed_response[data_key]
        if flag:
            result_dict['flag'] = 'Данные найдены!'
        else:
            result_dict['flag'] = 'По дате на бирже нету данных!'
    else:
        result_dict['flag'] = 'Требуется выполнить запрос!'

    return result_dict


def save_all_responses(all_data: dict) -> None:
    with open(f'{get_right_path()}completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)
