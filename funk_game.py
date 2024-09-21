import requests
from textwrap import indent
import os

import json
from datetime import datetime, timedelta

def check_currrency_data(user_date_string: str) -> bool:
    """Функция принимает в качестве входных данных строку, представляющую дату,
     и проверяет, является ли она допустимой. Если это так, функция возвращает
     значение True;
     в противном случае она возвращает значение False."""
    try:
        dt_obj = datetime.strptime(user_date_string, '%d.%m.%Y')
        if dt_obj >= datetime.today():
            return False
        return True
    except ValueError:
        return False


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
    """Эта функция проверяет, является ли строка допустимой строкой даты в формате "дд.мм.ГГГГ". Если это так,
     функция возвращает значение True. В противном случае она возвращает значение False."""
    info_response: dict = get_info_about_response(key)
    completed_response: dict = info_response['all_data']
    datetime_str = user_date.strftime("%d.%m.%Y")

    if info_response['flag'] == 'Требуется выполнить запрос!':
        flag_response: bool = save_data_about_currency(datetime_str)
        completed_response[key] = flag_response

        save_all_responses(completed_response)

    return info_response['flag']

def get_info_about_response(data_key: str) -> dict:
    """Эта функция проверяет, является ли данная строка user_date_string допустимой датой в формате дд.мм.ГГГГ.
"""
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


def add_new_key_value(key, value):
    with open('currency\\completed_response.json', 'r', encoding='utf-8') as file:
        all_data = json.load(file)

    all_data[key] = value

    with open('currency\\completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)
def save_all_responses(all_data: dict) -> None:
    with open(f'{get_right_path()}completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)





def left_and_right_dates(date: str) -> dict:
    start_obj = datetime.strptime(date, "%d_%m_%Y")

    final_dict = {
        'left': None,
        'right': None
    }

    count = 15
    for j in ["left", "right"]:
        for i in range(1, count + 1):
            if j == "left":
                new_date = start_obj - timedelta(days=i)
            else:
                new_date = start_obj + timedelta(days=i)
            str_obj = new_date.strftime("%d.%m.%Y")
            flag = save_data_about_currency(str_obj)
            if flag:
                final_dict[j] = new_date.strftime("%d.%m.%Y")
                break

    return final_dict




























