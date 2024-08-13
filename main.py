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
# if check_currrency_data(user_date_string):
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




from flask import Flask, render_template, request, redirect, url_for
import json
from funk_game import get_right_path

app = Flask(__name__)

@app.route('/')
def index():
    with open(f'{get_right_path()}15_05_2024.json', 'r', encoding='utf-8') as f:
        currency_data = json.load(f)
    data = {
        'title': 'Это моя первая страница',
        'header': 'тут ты узнаешь курс валют любой интересующий тебя день!',
        'currency': currency_data["Valute"]
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
    print(day, month, year)
    if check_currrency_data(f'{day}.{month}.{year}'):
        # переадресовать пользователя на нормальную страницу
        print('а теперь я тут')
        return redirect(url_for('success', day=day, month=month, year=year))

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
        'first_header': 'Успешно!'
    }

    day= request.args.get('day')
    month= request.args.get('month')
    year= request.args.get('year')
    print(day, month, year)
    # print(type(day))
    #     # print(type(month))
    #     # print(type(year))
    with open(f'currency/{day}_{month}_{year}.json', 'r', encoding='utf-8') as file:
        soul = json.load(file)

    return render_template('success.html', **data)

if __name__ == '__main__':
    app.run(debug=True)

















