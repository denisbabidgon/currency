import requests

import json
from datetime import datetime

from additional_function_for_app import check_correctly_date, get_info_about_response, add_new_key_value
from additional_function_for_app import get_right_path, get_left_and_right_dates
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

from ind_lesson.denis.currency.additional_function_for_app import save_data_about_currency

app = Flask(__name__)

import time

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
    date = request.form.get('date')
    print('date', date)

    if date is not None:
        print('редирект сразу на success')
        return redirect(url_for('success', data=f'{date}'))

    day = request.form.get('day')
    month = request.form.get('month')
    year = request.form.get('year')

    if check_correctly_date(f'{day}.{month}.{year}'):
        # переадресовать пользователя на нормальную страницу

        return redirect(url_for('success', data=f'{day}.{month}.{year}'))

    else:

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
        'left_and_right': None
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
            result_response = save_data_about_currency(dt_obj)

            # добавляем новую пару
            add_new_key_value(string_from_index, result_response)

            if result_response:
                with open(f'currency/{string_from_index}.json', 'r', encoding='utf-8') as file:
                    data['currency'] = json.load(file)['Valute']

                return render_template('success.html', **data)

        if result_response is None or result_response is False:
            # предоставить пользователю выбор ближайшей даты слева и даты справа
            left_and_right = get_left_and_right_dates(string_from_index)

            data['left_and_right'] = left_and_right
            count = 0
            if left_and_right['left'] is not None:
                count += 1
            if left_and_right['right'] is not None:
                count += 1

            data['count'] = count

            return render_template('two_dates.html', **data)




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





# https://www.google.com/search?q=
# sca_esv=e7553f361a6275f8 &
# sca_upv=1
# source=hp
# ei=pgDKZpPYHfSOwPAPqoS9WQ&iflsig=AL9hbdgAAAAAZsoOtpTcoxZkubnWtKpG8zNQPofkKSIO&ved=0ahUKEwiTw7GD_Y2IAxV0BxAIHSpCLwsQ4dUDCBY&uact=5&oq=%D0%9A%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D0%B3%D0%B0&gs_lp=Egdnd3Mtd2l6IhfQmtGD0YDRgSDQtNC-0LvQu9Cw0LPQsDIVEAAYgAQYsQMYgwEYyQMYChhGGIICMg0QABiABBixAxiDARgKMgoQABiABBiSAxgKMgcQABiABBgKMgoQABiABBixAxgKMgcQABiABBgKMgYQABgDGAoyBxAAGIAEGAoyBhAAGAMYCjIKEAAYgAQYsQMYCkjpP1C0G1iqPHAGeACQAQCYAbEBoAGMD6oBBDIuMTW4AQPIAQD4AQGYAhegArYPqAIKwgIQEC4YAxjlAhjqAhiMAxiPAcICEBAAGAMY5QIY6gIYjAMYjwHCAhEQLhiABBixAxjRAxiDARjHAcICCxAuGIAEGLEDGIMBwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAcICDhAAGIAEGLEDGIMBGIoFwgIOEC4YgAQYsQMY0QMYxwHCAgUQABiABMICDxAAGIAEGAEYsQMYgwEYCsICCxAuGIAEGLEDGNQCwgIOEAAYgAQYARjJAxgKGCrCAgkQABiABBgBGArCAgkQLhiABBgBGArCAhEQLhiABBjHARiYBRiZBRivAcICCxAAGIAEGJIDGIoFwgIPEC4YgAQYsQMYgwEYChgqwgIQEAAYgAQYsQMYgwEYyQMYCsICFxAAGIAEGLEDGIMBGMkDGAoYKhhGGIICwgIFEC4YgATCAg4QABiABBixAxiDARjJA8ICCBAAGIAEGJIDwgITEAAYgAQYsQMYgwEYyQMYRhiCAsICBBAAGAOYAwWSBwQ4LjE1oAfRvwE&sclient=gws-wiz











