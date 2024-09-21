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
# import json
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
#
#
# user_date_string = input('Введи дату: ')
#
# if check_currrency_data(user_date_string)
# надо продолжить и понять 
#     user_date: datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
#     key: str = user_date.strftime('%d_%m_%Y')
#
#     result = get_answer_about_next_response(user_date, key)
#     if result == 'Данные найдены!':
#         with open(f"{get_right_path()}{key}.json", "r", encoding="utf-8") as file:
#             data = json.load(file)
#             print(data)
#
#     print(result)
#
# else:
#     print('Ты ввел что-то не похожее на дату')



import os
from flask import Flask, render_template, request, redirect, url_for
import json
from funk_game import (get_right_path, check_currrency_data, save_data_about_currency, get_info_about_response, add_new_key_value, left_and_right_dates)

app = Flask(__name__)

@app.route('/')
def index():
    with open(f'{get_right_path()}15_05_2024.json', 'r', encoding='utf-8') as f:
        currency_data = json.load(f)
    data = {
        'title': 'Это моя первая страница',
        'header': 'тут ты узнаешь курс валют любой интересующий тебя день!',
        'currency': currency_data["Valute"],
        "zagolovok": 'Курс валют'
    }
    return render_template('index.html',  **data)

@app.route('/asd')
def asd():
    with open(f'{get_right_path()}15_05_2024.json', 'r', encoding='utf-8') as f:
        currency_data = json.load(f)
    data = {
        'title': 'А это моя вторая страница',
        'header': 'тут ты узнаешь курс валют любой интересующий тебя день!',
        'currency': currency_data["Valute"]
    }

    # не доделано
    return render_template('index.html', **data)

@app.route('/current_day')
def current_day():
    data = {
        'title': 'Курс валют',
        'first_header': 'Курс валют на 15 мая 2024 года',
    }
    with open('currency/30_05_2024.json', 'r', encoding='utf-8') as file:
        curr: dict = json.load(file)

    data['currency'] = curr['Valute']

    return render_template('current_day.html', **data)

@app.route('/submit', methods=['POST'])
def submit():
    day = request.form.get('day')
    month = request.form.get('month')
    year = request.form.get('year')
    date = request.form.get('date')


    if date is not None:
        return redirect(url_for('success', data=f'{date}'))
    if check_currrency_data(f'{day}.{month}.{year}'):
        # переадресовать пользователя на нормальную страницу
        return redirect(url_for('success', data=f'{day}.{month}.{year}'))

    else:
        print('я тут')
        return redirect(url_for('error'))

@app.route('/error')
def error():
    data = {
        'title': 'Курс валют',
        'first_header': 'Ошибка'
    }
    return render_template('error.html', **data)

@app.route('/success')
def success():
    data = {
    'title': 'Курс валют',
    'first_header': 'Успешно!',
    'left_and_right':  None
    }

    string_from_index = request.args.get('data').replace('.', '_')
    string_from_index = datetime.strptime(string_from_index, '%d_%m_%Y').strftime('%d_%m_%Y')

    flag = get_info_about_response(string_from_index)

    # print(flag['flag'])

    if flag['flag'] == 'Данные найдены!':
        # print('ты тут')
        with open(f'currency/{string_from_index}.json', 'r', encoding='utf-8') as file:
            data['currency'] = json.load(file)['Valute']

        return render_template('success.html', **data)

    else:
        result_response = None
        if flag['flag'] == 'Требуется выполнить запрос!':
            dt_obj = datetime.strptime(string_from_index, '%d_%m_%Y')
            dt_obj1 = dt_obj.strftime("%d.%m.%Y")
            result_response = save_data_about_currency(dt_obj1)

            # добавляем новую пару
            add_new_key_value(string_from_index, result_response)

            if result_response:
                with open(f'currency/{string_from_index}.json', 'r', encoding='utf-8') as file:
                    data['currency'] = json.load(file)['Valute']

                return render_template('success.html', **data)

        if result_response is None or result_response is False:
            # предоставить пользователю выбор ближайшей даты слева и даты справа
            left_and_right = left_and_right_dates(string_from_index)

            data['left_and_right'] = left_and_right
            count = 0
            if left_and_right['left'] is not None:
                count += 1
            if left_and_right['right'] is not None:
                count += 1

            data['count'] = count

            return render_template('selecting_the_nearest_page.html', **data)

# не рабочий метод !!!!!!!!!!!!!!!!!!!!!!!
# @app.route('/selecting_the_nearest_page')
# def selecting_the_nearest_page():
#     data = {
#         'title': 'Курс валют',
#         'first_header': 'На данную дату нет данных нажми на одну из кнопок с другими датами!'
#     }
#     return render_template('selecting_the_nearest_page.html', **data)

if __name__ == '__main__':
    app.run(debug=True)















