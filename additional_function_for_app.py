from textwrap import indent

import requests

import os
import json
from datetime import datetime, timedelta


def get_right_path(folder_name: str = 'currency') -> str:
    """Функция призвана сформировать абсолютный путь до папки,
    которая указана в качестве аргумента в зависимости от ОС, на которой выполняется запуск"""
    path_to_current_file = os.path.abspath(__file__)
    seperator = '/' if os.name == 'posix' else r'\\'
    path_list = path_to_current_file.split(seperator)

    path_list[-1] = folder_name

    return seperator.join(path_list) + seperator


def check_correctly_date(user_date_string: str) -> bool:
    try:
        dt_obj = datetime.strptime(user_date_string, '%d.%m.%Y')
        if dt_obj >= datetime.today():
            return False
        return True
    except ValueError:
        return False


def save_data_about_currency(user_data: datetime) -> bool:
    """
    1) Отправляется запрос и если запрос был НЕ успешен - то возвращается False
    а иначе:
        сохраняем полученные данные И возвращаем True
    """
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


def get_info_about_response(data_key: str) -> dict:
    """
    на вход мы получаем строку в формате %d_%m_%Y и эта строка - гарантированно валидная
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


def save_all_responses(all_data: dict) -> None:
    """
    completed_response.json нужен для того, чтобы хранить результаты по запросам пользователей.
    данные храняться парами: str: bool
    если bool = True - запрос уже был когда-то выполнен, и прошел успешно
    если bool = False - запрос уже был когда-то выполнен, по данной дате не было получено никаких данных
    """
    with open(f'{get_right_path()}completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)


def get_answer_about_next_response(user_date: datetime, key: str) -> str:
    """
    1) вызываем функцию, которая открывает completed_response.json и
    """
    info_response: dict = get_info_about_response(key)
    completed_response: dict = info_response['all_data']

    if info_response['flag'] == 'Требуется выполнить запрос!':
        flag_response: bool = save_data_about_currency(user_date)
        completed_response[key] = flag_response

        save_all_responses(completed_response)

    return info_response['flag']


def add_new_key_value(key: str, value: bool) -> None:
    # добавляем новую пару
    with open('currency/completed_response.json', 'r', encoding='utf-8') as file:
        all_data = json.load(file)

    all_data[key] = value

    with open('currency/completed_response.json', 'w', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)


def get_left_and_right_dates(data: str) -> dict:
    # data - это строка типа %d_%m_%Y
    start_dt_obj = datetime.strptime(data, '%d_%m_%Y')

    final_dict = {
        'left': None,
        'right': None,
    }

    count = 15
    for j in ['left', 'right']:
        for i in range(1, count + 1):
            if j == 'left':
                new_date = start_dt_obj - timedelta(days=i)
            else:
                new_date = start_dt_obj + timedelta(days=i)

            flag = save_data_about_currency(new_date)
            if flag:
                final_dict[j] = new_date.strftime('%d.%m.%Y')
                break

    return final_dict


# print(get_left_and_right_dates('31_08_2024'))


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
