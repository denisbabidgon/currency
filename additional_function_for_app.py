import requests

import os
import json
from datetime import datetime


def get_right_path(folder_name: str = 'currency') -> str:
    """Функция призвана сформировать абсолютный путь до папки,
    которая указана в качестве аргумента в зависимости от ОС, на которой выполняется запуск"""
    path_to_current_file = os.path.abspath(__file__)
    seperator = '/' if os.name == 'posix' else '\\'
    path_list = path_to_current_file.split(seperator)

    path_list[-1] = folder_name

    return seperator.join(path_list) + seperator


def check_correctly_date(user_date_string: str) -> bool:
    try:
        datetime.strptime(user_date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def save_data_about_currency(user_data: datetime) -> bool:
    """Документ строка"""
    # вставить в нужные места дату которые ввел пользователь.(что бы это работало)
    url = f'https://www.cbr-xml-daily.ru/archive/{user_data.strftime("%Y/%m/%d")}/daily_json.js'

    response = requests.get(url)
    status = response.status_code

    if status != 200:
        return False
    else:
        file_name = user_data.strftime(f'%d_%m_%Y')
        with open(f"{get_right_path()}{file_name}.json", 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)
    return True


# 1) пользователь может ввести не правильную дату
# 1.1) несуществующий фактически в календаре день
# 1.2) некорректный вид день.месяц.год -> месяц.день.год
# 2) пользователь может постоянно спрашивать одну и ту же дату
# - запросы которые мы прошли успешно ()
# - запросы, которые возвращают код 4.. - их было неплохо где-то сохранять


# 0) где и как хранить успешные и неуспешные запросы?

# 14.05.2024 -> 14_05_2024.json
# 1) принять от пользователя строку и перевести её в более удобный для себя формат
# 2) заглянуть в папку

# files = os.listdir('currency')
# print(files)

# json_object = {
#     '14_05_2024': True,
#     '15_05_2024': True,
#     '17_05_2024': True,
# }
#
# # text = 'h\\w'             # набор символов
# # print((len(text)))
# # print(text)
#
#
# def func(a, b, c, d):
#     return 'hello'
#
#
# lst = [1, 2, 3, 4]
# a = lst[-1]
# print(a)
