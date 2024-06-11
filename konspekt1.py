# # ФУНКЦИИ, методы, АРГУМЕНТЫ
# # ТИПЫ ДАННЫХ / СТРОКИ / ЧИСЛА
# # ОБЯЗАТЕЛЬНЫЕ АРГУМЕНТЫ / НЕОБЯЗАТЕЛЬНЫЕ АРГУМЕНТЫ / АГРУМЕНТЫ ПО УМОЛЧАНИЮ
#
# # print('Hello world', 32, "32")
# # print("Hello world")
#
#
#
# # print(32)
# # print()
#
# print(3, 4, 5, 6, sep='                ', end=' ')
# print(sep=' ', end='')
# print('asdf' + '4')


# print('Как тебя зовут? ')
# name = input()
# print('Привет', name)


# Желательно давать переменным осмысленные имена
# имя переменной должно начинаться с латинского символа (используем только латиницу + цифры)


# переменные let name = 'Sergey'
# константы const name = 'Sergey'


# МАТЕМАТИЧЕСКИЕ ОПЕРАЦИИ
# + сложение
# - вычитание
# * умножение
# / деление
# // целочисленное делениестаток от деления
# % о
# ** возведение в степень


# ТИПЫ ДАННЫХ

# price = 10
# num = input('сколько билетов ты хочешь купить? ')            # все то что мы вводим в программу через функцию input() сохраняется как строка
#
# print('Общяя стоимость:', price * int(num))

# Строка -> str - string (строка) ->            функция str()
# Число (целое) -> int -> integer (целый) ->    функция int()
# Число (дробное) -> float -> (плавающий) ->    функция float()


# type() - функция которая возвращает текущий тип объекта

# a = '10'
# b = 10
# c = 10.99
#
# print(type(a))
# print(type(b))
# print(type(c))


# ОПЕРАЦИИ СО СТРОКАМИ

#
# email = 'mail@mail.RU'
# word1 = 'hello world'
# word2 = 'HELLO WORLD'


# print(email.lower()) # переводит в нижний регистр
# print(email.upper()) # переводит в ВЕРХНИЙ регистр
# print(word.capitalize()) # первая буква сторки - заглавная - остальные строчные
# print(word.title()) # каждую первую букву заглавной
# print(word.swapcase()) # меняет регистр

# print(word1.islower())
# print(word2.isupper())


# a = '12345'
# b = 'dsfhja12'
#
# print(a.isdigit())
# print(b.isalpha())
#
# c = '12ab.'
# print(c.isalnum())


# ЛОГИЧЕСКИЙ ТИП bool True (правда) / False (ложь)

# print(10 > 5)
# print(3 * 2 == 8)
#
# print(type(True))


# СТРОКОВЫЕ МЕТОДЫ

# СТРОКА ЭТО НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ!!!
# count() - возвращает количество подстрок в строке
# replace() - меняем что-то на что-то (создаем новый объект потому что строки это неизменяемыый тип данных)
# len() - возращает длину нашего объекта

# index             ищет индекс искомого элемента слева направо и падает в ошибку если не находит
# rindex            ищет индекс искомого элемента справа налево и падает в ошибку если не находит
# find              ищет индекс искомого элемента слева направо и возвращает -1 если не находит
# rfind             ищет индекс искомого элемента справа налево и возвращает -1 если не находит


# text = 'hello world'
#
# index = text.index('L')


# word1 = 'hello world'
#
# # print(word1.count('world'))
#
# lastIndex = len(word1) - 1
#
# print(word1[lastIndex])


# СРЕЗЫ

# word1 = 'hello world'
#
# print(word1[::-1])

# [start:stop]
# [start:stop:step]
#
# a = 'сосна'
# print(a == a[::-1])


# str
# float
# int
# bool / True / False


# if ... если

# else... иначе


# если число четное и двузначное то мы будем
# во всех остальных случаях будем говорить что число не подходит под наши критерии

# number = int(input())
#
# if number % 2 == 0 or 10 <= number < 100:
#     print('четное ИЛИ двузначное')
# else:
#     print('число не подходит под наши критерии')


# == проверка на равенство
# != проверка на неравенство
# > проверка на больше
# < проверка на меньше
# >= проверка на больше или равно
# <= проверка на меньше или равно

# print(20 == 20)
# print(21 == 19)
#
# print(5 != 10)
# print('s' != 'S')
#
# print(25 > 25)
#
# print('a' > 'A')
#
# print(ord('a'))
# print(ord('A'))


# if / else / elif - иначе если

# цель: перевести оценку со стобальной шкалы в пятибольную
#
# grage = int(input())
#
# if grage >= 90:
#     print(5)
# elif grage >= 80:
#     print(4)
# elif grage >= 70:
#     print(3)
# elif grage >= 60:
#     print(2)
# else:
#     print(1)


# and и
# or или


# a = int(input())
#
# if a == 2:
#     print(28)
# elif a == 4 or a == 6 or a == 9 or a == 11:
#     print(30)
# else:
#     print(31)
#


# ЦИКЛЫ

# цикл который повторяется определенное количество раз (счетные циклы, couting loops)                   for
# цикл который повторяется до наступления определенного события (условные циклы, conditional loops)     while


# for i in range(1000):
#     print('hello world', i)

# while True:
#     print('hello world')


# while - пока

# while УСЛОВИЕ КОТОРЕ ВЕРНЕТ ИЛИ True or False:
#     блок кода с отступом


# print('Введи число, квадрат которого ты хочешь посчитать или не вводи ничего если хочешь закончить!')
# number = input()
#
# while number != '':
#
#     print(f'Квадрат числа {number} равен {int(number) ** 2}')
#     number = input()

# flag = True
# g = 0
#
# while flag:
#     a = int(input())
#     if a < 0:
#         flag = False
#     else:
#         g += a
#
# print('сумма:', g)


# break - экстренно завершает цикл!
# continue - переход на новую иттерацию минуя код ниже!


# index = 0
# while True:
#     if index == 3:
#         index += 1
#         continue
#
#     print(index)
#     index += 1
#
#     if index == 5:
#         break


#

# import random
#
# number = random.randint(0, 10_000_000_000)
#
# print("Попробуй угадать число от 0 до 5!")
#
# # attempts = 0
#
# flag = True
#
# while flag:
#     user_number = int(input("Введи число: "))
#     if user_number == number:
#         print(f"Это верно, я загадал число {user_number}")
#         flag = False
#     else:
#         # attempts += 1
#         print("Не угадал")
#         # if attempts == 3:
#         #     print('Извини, но попытки закончились!')
#         #     flag = False


# ЦИКЛ for

# range() - диапазон
# range(stop)                   получаем диапазон от 0 до stop (не включая его)
# range(start, stop)            получаем диапазон от start до stop (не включая его)
# range(start, stop, step)      получаем диапазон от start до stop (не включая его) c шагом в step

# print(list(range(10)))


# firstString = 'hello world'   # len(object)
# secondString = 'HeLLo worlD'


# print(len(newString))
# print(newString[len(newString) - 1])
# print(newString[-1])


# for i in range(len(firstString)):
#     if firstString[i] != secondString[i]:
#         print(i)

# for i in firstString:
#     print(i)


# count = 0
# while count < 10:
#     print('hello')
#     count += 1


#
# import turtle
# import random
#
# turtle.setup(500, 500)
#
# for i in range(6):
#     turtle.forward(50)
#     turtle.left(60)
# turtle.left(90)
#
# turtle.mainloop()


# import turtle
#
# turtle.setup(500, 500)
#
# turtle.color('red')
# turtle.pensize(3)
# turtle.forward(100)
# turtle.up()
# turtle.goto(-125, 125)
# turtle.down()
# turtle.forward(100)
#
# turtle.mainloop()


# СПИСКИ - ИЗМЕНЯЕМАЯ СТРУКТУРА
# list - список / list() - функция по переводу какого-то объекта в список

# newList = [12, 23, 12, 3.4, 'text', True, [34, 45, 56]]

# print(newList)

# print(len(newList))                 # длина объекта
# print(len('text'))

# print(newList.count(99))            # количество чего-то в нашем списке
#
# print(99 in newList)                # оператор in возвращает логический тип данных или True или False | есть ли что-то где-то?

# lst1 = []
# lst2 = list('helloworld')

# append() - добавляет элемент в конец списка
# extend() - расширяет список другим иттерируемым объектом (чаще всего другим списком)
# pop() - удаляем и возвращаем последний элемент списка
# pop(INDEX) - удаляем и возвращаем последний элемент списка
# del object[index] - удалить элемент из списка
# clear() - отчищает наш список
# copy() - создает поверхностную копию списка
# index() - возвращает индекс элемента который мы ищем
# sort() - сортировка списка / reverse=False
# reverse() - переворачиваем список
# insert(INDEX, obj) - вставить объект на какую-то позицию (остальное двигается вправо)


# ФУНКЦИИ!!!
# newObj = sorted(lst) - сортировка списка / создаем новый объект / reverse=True - обратный порядок
# newObj = reversed(lst) - развернуть список (при этом создается итератор, который по хорошему нужно пропустить через list())


# lst1.append(12)
# lst1.append(23)
#
# lst1.extend('text')
#
# print(lst1)


# lst3 = [34, 5, 67, 112, 99, 9]

# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]


# print(lst3)
# print(lst3)


# a = lst1.pop(0)
# del lst1[-1]

# print(lst1)
# print(a)
#
# print(lst1)


# my_favorite_product = ['бананы', 'ананасы']
# you_favorite_product = my_favorite_product.copy()
#
# my_favorite_product.append('абрикосы')
#
# print(my_favorite_product)
# print(you_favorite_product)


# КОРТЕЖИ       tuple - это тоже самое что и списки, только они НЕИЗМЕНЯЕМЫЕ!

# tpl1 = 1, 2, 3, 4, 5, 1, 1
# tpl2 = (1, 2, 3, 4, 5)
#
# tpl3 = tpl1[:]
# print(type(tpl))
# print(tpl3)


# Нам нужно написать программу, которая будет запрашивать у пользователя цвет на английском
# до тех пор пока пользователь не введет слово exit
# И все эти цветa мы должны где-то хранить для дальнейшего использования


#
# flag = True
# newList = []
#
# while flag:
#     a = input()
#     if a == 'exit':
#         flag = False
#     else:
#         newList.append(a)
#
# print(newList)


# import random
#
# print(random.randint(0, 10))
# import turtle
#
# turtle.setup(500, 500)
#
#
# turtle.color('blue')
# for i in range(4):
#     turtle.forward(30)
#     turtle.left(90)
#
#
# turtle.mainloop()


# import turtle
# turtle.speed(1000)
# turtle.setup()
#
# for i in range(4):
#     turtle.forward(50)
#     turtle.left(90)
#
# x, y = 0, 0
#
# for j in range(50):
#     turtle.goto(x, y)
#     for i in range(25):
#         turtle.forward(1)
#         turtle.left(90)
#         turtle.forward(1)
#         turtle.right(90)
#         turtle.forward(1)
#         turtle.right(90)
#         turtle.forward(1)
#         turtle.left(90)
#     y += 1
#
# turtle.mainloop()

import turtle

# import random
#
#
# flag = True
# colorsList = []
#
# while flag:
#     color = input()
#     if color == 'exit':
#         flag = False
#     else:
#         colorsList.append(color)
#
#
# turtle.setup(500, 500)

# turtle.forward(100)
#
# x, y = -200, -200
#
# for i in range(10):
#     turtle.up()
#     turtle.goto(x, y)
#     turtle.down()
#
#     randomIndex = random.randint(0, len(colorsList) - 1)
#     randomColor = colorsList[randomIndex]
#
#     turtle.dot(20, randomColor)
#
#     x += 25
#     y += 20
#
# turtle.mainloop()


# распаковка / упаковка

# colorList = ('red', 'green', 'blue')

# a, b, c = colorList

# print(a)
# print(b)
# print(c)
#
# pointList = [[2, 5], [6, 7], [12, 34], [-65, 45]]
#
# for x, y in pointList:
#     print((x + y) ** 0.5)
#     print(f'Точка с координатами x = {x}, y = {y}')


# int           целые числа
# float         дробные числа
# str           строки
# bool          логический тип
# list          списки
# tuple         кортежи


# a1 = '12'                   # str         коллекция - иттерируемый объект
# a2 = 23                     # int         НЕ иттерируемый объект
# a3 = 34.45                  # float       НЕ иттерируемый объект
# a4 = 'True'                 # str         коллекция - иттерируемый объект
# a5 = [1, 2, 3, 4, 5]        # list        коллекция - иттерируемый объект
# a6 = 5, 6, 7, 8             # tuple       коллекция - иттерируемый объект
# a7 = False                  # bool        НЕ иттерируемый объект
# a8 = ['22', '4', '6', '8', '33']   # list

# len()                       # возвращает длину объекта
# max()                       # максимальный элемент коллекции
# min()                       # минимальный элемент коллекции
# sum()                       # сумма элементов последовательности


# СЛОВАРИ                   ТИП ДАННЫХ
# словарь это изменяемая структура


# newList = [1, 2, 3, 4, 5, 6, 7, 8]

# newDict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# print(len(newDict))

# dct1 = {}
# dct2 = dict()
# print(dct1)
# print(dct2)

# dct = dict(name='Sergey', age=34, city='Kemerovo')
# dct2 = dict([('name', 'Sergey'), ('age', 34), ('city', 'Kemerovo')])
#
# print(dct2)
#
# dct3 = {'name': 'Sergey',
#         'age': 34,
#         'city': 'Kemerovo',
#         1: 'ok',
#         2.3: 'ok',
#         True: 'ok',
#         (1, 2, 3): 'no'}

# ключи словаря могут быть только неизменяемыми типами данных!!!

# print(dct3)
#


# import math
#
#
# book_phones = {
#   'Квам-Дамн': '-79899899889',
#   'Лук Скамворкер': '112',
#   'Петард Вейпер': '1',
#   'Лия Моргала': '+09998765432',
#   'Эдуард Скамворкер': '0'
# }
# # Напиши код тут
#
# action = input('1 — Показать, 2 — Добавить, 3 — Изменить, 4 — Удалить, 5 — Показать все имена в книге, 6 — Показать все номера в книге. ')
#
# if action == '1':
#     name = input('Введи имя: ')
#     if name in book_phones:
#         print(book_phones[name])
#     else:
#         print('Нет в телефонной книге')
#
# elif action == '2' or action == '3':
#     name = input('Введи имя: ')
#     phone = input('Введи номер: ')
#     book_phones[name] = phone
#
#     for name, phone in book_phones.items():
#         print(f'{name}: {phone}')
#
# elif action == '4':
#     name = input('Введи имя: ')
#     if name in book_phones:
#         del book_phones[name]
#         for name, phone in book_phones.items():
#             print(f'{name}: {phone}')
#     else:
#         print('Нет в телефонной книге')
#
# elif action == '5':
#     print(*[key for key in book_phones.keys()], sep='\n')
#
# elif action == '6':
#     print(*[key for key in book_phones.values()], sep='\n')
#
# else:
#     print('Такого действия нет')
#


# спрашиваем у пользователя строку на русском языке
# наша задача вывести на экран ту же самую строку, но написанную английскими символами

# привет! как дела?
# privet! kak dela?

# dct = {'а': '',
#        'б': '',
#        'в': '',
#        'г': '',
#        'д': '',
#        '': '',
#        '': '',
#        '': '',
#        '': '',
#        '': '',
#        '': '',
#        '': '',
#        '': '',
#        '': '',}

# 0) нужно составить ТАБЛИЦУ
# 1) спросить строку
# 2) создать место где мы будем сохранять нашу новую строку
# 3) перебирая каждый символ из исходной русской строки найти заменитель и подставить в новую строку
# 4) вывести итог на экран





# newDict = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
#            'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
#            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'iu',
#            'я': 'ia'}
#
#
# print("Enter text: ")
# st = input()
# result = str()
#
# len_str = len(st)
#
# for i in range(0, len_str):
#     if st[i].lower() in newDict:
#         if st[i].isupper():
#             simb = newDict[st[i].lower()].upper()
#         else:
#             simb = newDict[st[i].lower()]
#     else:
#         simb = st[i]
#     result = result + simb
#
# print(result)

# print(len(dic))



# МНОЖЕСТВА                 /           ЗАМОРОЖЕННОЕ МНОЖЕСТВО

# НЕУПОРЯДЕЧЕННАЯ, изменяемая коллекция, в которой могу находиться только уникальные элементы,
# set                       /           frozenset() - неизменяемая коллекция

# newSet = set('text')
# one_more_set = {'h', 'e', 'l', 'o', 'w', 'o', 'r', 'l', 'd'}

# print(type(one_more_set))
# print(one_more_set)

# методы множеств
# len()         +
# in            +
# add()         добавить
# copy()        поверхностаня копия множества
# pop()         удаляет и возвращает случайный элемент
# remove()      удаляет элемент из множества (вызывает исключение если удаляемого элемента нет в множестве)
# discard('h')  удаляет и не вызывает исключение в случае если элемент отсутствует
# clear()       отчищает множество

# newSet.add('h')
# # rSet = newSet.copy()
# print(newSet)

# fSet = frozenset('hello world')
#
# print(fSet)
# print(type(fSet))


# newList = [1, 1, 2, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4]
#
# a = newList.pop()
# print(a)
# print(newList)

#
# print(set(newList))

# lst = []
# for num in newList:
#     if num not in lst:
#         lst.append(num)
# print(lst)


# union()                               объединение множеств            ВОЗВРАЩАЕТ НОВОЕ МНОЖЕСТВО          оператор |
# intersection()                        пересечение множеств            ВОЗВРАЩАЕТ НОВОЕ МНОЖЕСТВО          оператор &
# difference()                          разность множеств               ВОЗВРАЩАЕТ НОВОЕ МНОЖЕСТВО          оператор -
# symmetric_difference()                симметричная разность множеств  ВОЗВРАЩАЕТ НОВОЕ МНОЖЕСТВО          оператор ^


# update()                              объединение множеств            ИЗМЕНЯЕТ МНОЖЕСТВО, к которому применяется операция          оператор |=
# intersection_update()                 пересечение множеств            ИЗМЕНЯЕТ МНОЖЕСТВО, к которому применяется операция          оператор &=
# difference_update()                   разность множеств               ИЗМЕНЯЕТ МНОЖЕСТВО, к которому применяется операция          оператор -=
# symmetric_difference_update()         симметричная разность множеств  ИЗМЕНЯЕТ МНОЖЕСТВО, к которому применяется операция          оператор ^=


# firstSet = {1, 2, 3, 4, 5}
# secondSet = {3, 4, 5, 6, 7}

# print(firstSet)

# print(firstSet.intersection(secondSet))
# print(firstSet.difference())
# print(firstSet.symmetric_difference())



# text = 'text ! on text ...! text !,!!!! word word text'
#
#
# newtext = text.lower()
#
# punctuation = [".", ",", "!", "?"]
# for i in punctuation:
#     newtext = newtext.replace(i, "")
#
#
# words = newtext.split()
# print(words)
#
#
# punctuation = [".", ",", "!", "?"]
# for i in punctuation:
#     newtext = newtext.replace(i, "")
#
# words = newtext.split()
#
# print(set(words))
#
#
# clovar = {}
# for g in words:
#     if g in clovar:
#         clovar[g] += 1
#     else:
#         clovar[g] = 1






# ФУНКЦИИ

# 1) функции, которые что-то возвращают
# 2) функции, которые ничего не возвращают

# print()
# len()


# text = 'hello world'
#
# a = len(text)
#
# # b = print(text)
#
# print(a)

# None - ничего


# *******





# def draw_box():
#     result = ''
#     for i in range(num):
#         result += '*' * 10 + '\n'
#
#     return result





# def draw_box(heigth, width):
#     for i in range(heigth):
#         print('*' * width)
#
#
#
# draw_box(3, 15)
# print()
# draw_box(5, 5)




# создать функцию которая будет называться digit_sum()
# функция должна принимать целое число и возвращать сумму всех цифр этого числа

# 245 -> 11


# def digit_sum(num):
#     pass
#
#
# digit_sum(245)
# digit_sum(5673)




#!!! ЗАБЫЛИ ПРО ФУНКЦИИ

# наша задача:
# 1) принять от пользователя (через input) целое число
# 2) посчитать и распечатать сумму всех цифр этого числа

# num = int(input())
#
# # блок кода
#
# print(...)




# def digit_sum(num):
#     res = 0
#
#     while num > 0:
#         dig = num % 10
#         res += dig
#         num //= 10
#
#     return res
#
# print(digit_sum(35))


# def calc(a, b, operator):
#     if operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     elif operator == '*':
#         return a * b
#     elif operator == '/':
#         return a / b
#     else:
#         return 'нет такого действия'
#
#
# print(calc(10, 23, '+'))
# print(calc(10, 2, '*'))
#
#
# for i in range(10):
#     if i == 2:
#         break
#     else:
#         print(i)


# документ строка и аннотации типов


# def digit_sum(num):
#     """Функция принимает целое число и возвращает сумму всех цифр этого числа"""
#     res = 0
#
#     while num > 0:
#         dig = num % 10
#         res += dig
#         num //= 10
#
#     return res



# def upper_func(s: str, a: list) -> list:
#
#     return 23
#
#
# print(upper_func())


# напишем функцию, которая принимает строку, в которой записаны фалмилия имя и отчество
# и возвращает инициалы
# пушкин александр сергеевич -> П.А.С

# print(list(range(10)))
#
# for i in 'text':
#     print('hello')


# поговорим про for ан примере разных типов данных








# a1 = 'text'                                # str          коллекция
# a2 = 123                                   # int          НЕ коллекция
# a3 = 234.30                                # float        НЕ коллекция
# a4 = [12, 23, 34, 45]                      # list         коллекция
# a5 = {'a': 12, 'b': 34}                    # dict         коллекция
# a6 = 14, 56, 78                            # tuple        коллекция
# a7 = {76, 45, 23}                          # set          коллекция
# a8 = frozenset([56, 7, 89])                # frozenset    коллекция


# for i in range(10, 50, 10):
#     print(i)





# # 2 * 3 * 4 * 5 = 120
#
# def multiply_range(start, end):
#     """Принимает два числа и возвращает произведение всех чисел от [start до end]
#     То если на вход передать числа 2 и 5, то мы должны перемножить 2 * 3 * 4 * 5"""
#     if start > end:
#         start, end = end, start
#     result = 1
#     for i in range(start, end + 1):
#         result *= i
#
#     return result
#
#
#
# print(multiply_range(5, 2))
# print(multiply_range(2, 5))

#
# def fio(w: str):
#     w_up_split = w.upper().split()
#
#     acronym = ""
#
#     for i in w_up_split:
#         acronym += i[0] + '.'
#
#     return acronym
#
#
# name = input()
# res = fio(name)
# print(res)
#
# name = input()
# s = fio(name)
# print(s)






# функция проверки логина на правильность:
#     какой-то код
#     да если всё хорошо и нет если все плохо
#
#
#
# функция проверки пароля на правильность:
#     какой-то код
#     да если всё хорошо и нет если все плохо
#
#
# функция проверки почты на правильность:
#     какой-то код
#     да если всё хорошо и нет если все плохо
#
#
#
# функция в которой все собирается в одно целое:
#     логин = введи логин
#     пароль = введи пароль
#     почта = введи почту
#
#     если функция логина(ЛОГИН) == да И функция пароля(ПАРОЛЬ) == да И функция почты(ПОЧТА) == да:
#         выполняем какие-то действия
#         и сообщаем что все окей
#     иначе:
#





# try / except



# try:
#     print('text')
#     print(10 / 0)
#
# except ZeroDivisionError:
#     print('ты пытаешься поделить на ноль')
# except IndexError:
#     print('ты пытаешься обратиться к несуществующему индексу')
#
# except:
#     print('я не знаю что именно не так, но что-то не так')
#
# finally:
#     print('сработает в любом случае вне зависимости от того, произошла ошибка или нет')




# # глобальная
# num = 10
#
#
# def newFunc():
#     # локальная область видимости
#     num = 20
#     print(num)
#
#
# newFunc()
# print(num)







# def sum_nums(num1, num2):
#     result = 0
#     try:
#         result = float(num1) + float(num2)
#     except:
#         pass
#     finally:
#         return result
#
#
# print(sum_nums(10, 15))
# print(sum_nums(10.5, '15'))
# print(sum_nums('10', 'text'))




# lambda-функция - это анонимная функция


#
# def get_sqare_seconde_num(lst: list) -> int:
#     '''Принимаем список целых чисел и возвращаем квадрат второго числа'''
#     return lst[1] ** 2



# filter, map


# matrix = [[69, 11, 37, 45, 94], [99, 11, 3, 87, 57], [10, 24, 98, 1], [32, 11, 5, 8, 90]]
#
# matrix.sort(key=lambda lst: (lst[1], -lst[-1]))
# print(*matrix, sep='\n')



# step1 = []
# for i in range(len(matrix)):
#     step1.append(matrix[i][1] ** 2)
#
# print(step1)
#
# step2 = [matrix[j][1] ** 2 for j in range(len(matrix))]
# print(step2)
#
#
# step3 = list(map(lambda lst: lst[1] ** 2, matrix))
# print(step3)


# print(get_sqare_seconde_num([1, 3, 9]))
# print(anonym_func([1, 4, 9]))







# text = 'шайллаш'
#
# left = 0
# right = len(text) - 1
#
# while left < right:
#     if text[left] == text[right]:
#         left += 1
#         right -= 1
#     else:
#         print('Это не палиндром!')
#         break
# else:
#     print('Это палиндром!')
#
#
# start = 0
# while start < 10:
#     if start == 5:
#         break
#     start += 1
#
# else:
#     start += 1
#
# print(start)


#
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'),
#         (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'),
#         (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#





# def generate_math_questions() -> str:
#     '''Наша функция генерирует математический пример по случайным числам от 1 до 10'''

# num1, num2, symb = 2, 3, "+"
#
# # print(str(num1) + symb + str(num2))
#
# print(f"{num1} {symb} {num2} = ")

# print('text' + 'HELLO')





# q = '3 * 6 ='
#
# print(int(q))




# 2.7
# 3.10
# 3.11
# 3.12



# 'FizZ', 'buZZ' -> 'zzUB@@@zZIffIZz'
# второе слово переворачиваю и меняю регистр zzUB
# первое слово меняем регистр и переворачиваем zZIf fIZz


# String Reversing, Changing Case
# ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING
# ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING
#


# def reverse_and_mirror(s1: str, s2: str):
#     reversed2 = s2[:: -1]
#     reversed2 = reversed2.swapcase()
#     reversed1 = s1[:: -1]
#     reversed1 = reversed1.swapcase()
#     reversed1 = reversed1 + reversed1[:: -1]
#     obsreversed = reversed2 + "@@@" + reversed1
#     return obsreversed
#
# print(reverse_and_mirror('FizZ', 'buZZ'))