import requests

import os
import json
from datetime import datetime


def get_right_path(folder_name: str = 'currency') -> str:
    """Функция призвана сформировать абсолютный путь до папки,
    которая указана в качестве аргумента в зависимости от ОС, на которой выполняется запуск"""
    path_to_current_file = os.path.abspath(__file__)
    seperator = '/' if os.name == 'posix' else r'\\'
    path_list = path_to_current_file.split(seperator)

    path_list[-1] = folder_name

    return seperator.join(path_list) + seperator


def check_correctly_date(user_date_string: str) -> dict:
    result = {
        'user_date_string': user_date_string,
        'flag': None,
        'response': None,
    }

    try:
        date_time_obj = datetime.strptime(user_date_string, '%d.%m.%Y')
        if date_time_obj > datetime.now():
            result['flag'] = 'Ты пытаешься получить данные по дате в будущем!'
            return result

    except ValueError:
        result['flag'] = 'Ты пытаешься ввести несуществующую дату'
        return result

    info_abot_all_resp = get_info_about_response(file_name := date_time_obj.strftime('%d_%m_%Y'))
    if info_abot_all_resp['flag'] == 'Данные найдены!':
        with open(f'{get_right_path()}{file_name}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            result['flag'] = 'Данные найдены!'
            result['response'] = data

        # открыть файл
    elif info_abot_all_resp['flag'] == 'По дате на бирже нету данных!':
        result['flag'] = 'По дате на бирже нету данных!'
    else:
        resp_flag, resp_result = save_data_about_currency(date_time_obj)
        if resp_flag is False:
            result['flag'] = 'По дате на бирже нету данных!'
        else:
            result['flag'] = 'Данные найдены!'
            result['response'] = resp_result

    return result


def save_data_about_currency(user_data: datetime) -> tuple:
    """Документ строка"""
    # вставить в нужные места дату которые ввел пользователь.(что бы это работало)
    url = f'https://www.cbr-xml-daily.ru/archive/{user_data.strftime("%Y/%m/%d")}/daily_json.js'

    response = requests.get(url)
    status = response.status_code

    if status != 200:
        return False, None
    else:
        file_name = user_data.strftime(f'%d_%m_%Y')
        with open(f"{get_right_path()}{file_name}.json", 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)
    return True, response.json()


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


# def get_answer_about_next_response(user_date: datetime, key: str) -> str:
#     info_response: dict = get_info_about_response(key)
#     completed_response: dict = info_response['all_data']
#
#     if info_response['flag'] == 'Требуется выполнить запрос!':
#         flag_response: bool = save_data_about_currency(user_date)
#         completed_response[key] = flag_response
#
#         save_all_responses(completed_response)
#
#     return info_response['flag']


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
