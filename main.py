import requests

import json
from datetime import datetime
#
# from additional_function_for_app import check_correctly_date, get_answer_about_next_response
# from additional_function_for_app import get_right_path
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

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'title': 'Это моя первая страница',
        'header': 'тут ты узнаешь курс валют на сегодня'
    }
    return render_template('index.html', **data)

@app.route('/asd')
def asd():
    data = {
        'title': 'А это моя вторая страница',
        'header': 'тут ты узнаешь курс валют любой интересующий тебя день!'
    }
    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run(debug=True)

















