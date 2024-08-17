import requests

import json
from datetime import datetime

from additional_function_for_app import check_correctly_date
from additional_function_for_app import get_right_path
#
# user_date_string = input('Введи дату: ')
#
# if check_correctly_date(user_date_string):
#     user_date: datetime = datetime.strptime(user_date_string, '%d.%m.%Y')
#     key: str = user_date.strftime('%d_%m_%Y')
#
#     result = get_answer_about_next_response(user_date, key)
#     if result == 'Данные найдены!':
#         with open(f'{get_right_path()}{key}.json', 'r', encoding='utf-8') as file:
#             data = json.load(file)
#             print(data)
#
#     print(result)
#
# else:
#     print('Ты ввел что-то не похожее на дату')


# библиотека для "объединения" бэка и фронта
# flask, fastapi, django

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'title': 'Курс валют',
        'first_header': 'Курс валют',
        'second_header': 'Тут ты узнаешь курс валют на сегодня',
    }

    return render_template('index.html', **data)


@app.route('/submit', methods=['POST'])
def submit():
    day = request.form.get('day')
    month = request.form.get('month')
    year = request.form.get('year')

    result = check_correctly_date(date_string := f'{day}.{month}.{year}')

    if result['flag'] == 'Данные найдены!':
        return redirect(url_for('success', data=result['response']))

    elif result['flag'] == 'Ты пытаешься ввести несуществующую дату':
        print('Ты пытаешься ввести несуществующую дату')
        return redirect(url_for('error'))

    elif result['flag'] == 'Ты пытаешься получить данные по дате в будущем!':
        print('Ты пытаешься получить данные по дате в будущем!')
        return redirect(url_for('error'))

    elif result['flag'] == 'По дате на бирже нету данных!':
        print('По дате на бирже нету данных!')
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
        'currency': json.loads(request.args.get('data').replace('+', '')),
    }



    return render_template('success.html', **data)


@app.route('/current_day')
def current_day():
    data = {
        'title': 'Курс валют',
        'first_header': 'Курс валют на 30 мая 2024 года',
    }
    with open('currency/30_05_2024.json', 'r', encoding='utf-8') as file:
        curr: dict = json.load(file)

    data['currency'] = curr['Valute']

    return render_template('current_day.html', **data)


if __name__ == '__main__':
    app.run(debug=True)

















