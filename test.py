# import json
#
# with open('currency/30_05_2024.json', 'r', encoding='utf-8') as file:
#     curr: dict = json.load(file)
#
# # curr <- что это за переменная
# # что там хранится
# # какой тип данных
# # и как этот объект можно проиттерировать?
#
# for i in curr.items():
#     print(i)
import asyncio
from datetime import datetime, timedelta

# with open('test_file.txt', 'w', encoding='utf-8') as file:
#     print(file.read())


# import time
from time import perf_counter
# import asyncio
#
#
# def req(timer: int):
#     print('Начинаем выполнять функцию req', timer)
#     time.sleep(timer)
#     print('Закончили работу с функцией req', timer)
#
#
# def main():
#     for i in range(10):
#         req(i)
#
#
# start = perf_counter()
# main()
# print('время выполнения синхронного кода: ', perf_counter() - start)
# print('\n\n\nНачинаем ассинхронный цикл')
#
#
# # 9
#
# async def as_req(timer: int):
#     print('Начинаем выполнять функцию req', timer)
#     await asyncio.sleep(timer)
#     print('Закончили работу с функцией req', timer)
#
#
# async def main(lst: list):
#     tasks = []
#     for i in lst:
#         task = asyncio.create_task(   as_req(i)  )
#         tasks.append(task)
#
#     await asyncio.gather(*tasks)
#     print('все задачи завершены')
#
#
# start = perf_counter()
# asyncio.run(main([5, 6, 4, 3, 7, 6, 8, 5]))
# print('время выполнения асинхронного кода: ', perf_counter() - start)


import aiohttp
from aiohttp import ClientSession


async def fetch(session: ClientSession, url, date: datetime):
    async with session.get(url, ssl=True) as response:
        text = await response.text()
        if response.status == 200:
            print(f'Запрос был успешно выполнен за {date.strftime("%d - %m - %Y")}')
        else:
            print(f'Запрос был НЕ выполнен! Дата - {date.strftime("%d - %m - %Y")}')


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        start_date = datetime.strptime('01.01.2024', '%d.%m.%Y')
        for i in range(300):

            url = f'https://www.cbr-xml-daily.ru/archive/{start_date.strftime("%Y/%m/%d")}/daily_json.js'
            task = asyncio.create_task(fetch(session, url, start_date))
            tasks.append(task)
            start_date += timedelta(days=1)

        await asyncio.gather(*tasks)


start = perf_counter()
asyncio.run(main())
print('время выполнения синхронного кода: ', perf_counter() - start)






# file = open('test_file.txt', 'r', encoding='utf-8')
#
# file.close()

# file = open('test_file.txt', 'r', encoding='utf-8')
# try:
#     pass
# except:
#     pass
# finally:
#     file.close()









# def func(obj: list) -> int:
#     result = 0
#     for i in obj:
#         result += i
#     return result
#
#
# def func2(*args, **kwargs) -> int:
#     print(kwargs)
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# print(func2(2, 2, 2, 4, 5, 6, name='asd', number=324, adsf=[1, 2, 3, ]))
#
#
# Task1 = 'asdf'
# Task2 = 'asdf'
# Task3 = 'asdf'
# Task4 = 'asdf'
# t = [Task1, Task2, Task3, Task4]
#
#
# asyncio.gather(Task1, Task2, Task3, Task4)
