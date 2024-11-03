from engine import get_data_from_data_base, connect_to_sqlite


# SQLite

text = """

CREATE TABLE Books
(
    id          INT,
    title       VARCHAR(40),
    author      VARCHAR(40),
    price       INT
);

"""

text_to_drop = """

DROP TABLE

"""


# print(get_data_from_data_base(text))
# print(connect_to_sqlite(text, True))


# ==        ->          =
# !=        ->          !=
# >         ->          >
# <         ->          <
# >=        ->          >=
# <=        ->          <=

# AND / OR / IN / NOT IN

# lst = [1, 2, 3, 4, 5]
#
# if 6 in lst:
#     print('ok')

# Метасимволы и оператор LIKE

# a = 'tead'
# b = 'asd'
#
# print(a + ' ' + b + '!')
# print(f'{a} {b}!')

# lst = ['asd', 'bcd', 'ad']
# a = ' * '.join(lst)
# print(a)
#
# b = 'asd * bcd * ad'
# print([i.lstrip() for i in b.split('*')])

# print(23 / 0)


# text = 'hello world'
# # # print(text[::-1])
# #
# # text = text.lstrip()
# # print(f'|{text}|')
#
# try:
#     print(text.index('L'))
# except:
#     print('такого в строке нету')
#
# if 'L' in text:
#     print(text.index('L'))
# else:
#     print('такого в строке нету')
#
# print(text.find('L'))



# text = 'hello world'            # --->> llo world
# print(text[::2])

# СРЕЗЫ



# text.replace('l', '')

# print(list( range(100, 10, -1) ))

# a = 10 + 2




# a = 13
# b = 3
#
# # a целочисленно поделить на b
#
# c = a % b
# print(c)

# print(round(2.655, 1))
# print(round(3.465, 1))
# print(round(4.5))
# print(round(5.5))
# print(round(6.5))
# print(round(7.5))


# import math
#
# math.
#
# print(math.sqrt(42875))

# print(math.pow(35, 3))
# print(35 ** 3)

# import random
#
# random.


# a = [1, 2, 3, 4, 5, 6, 4, 3, 2, 4, 5, 6, 7]
#
# b = []
# for i in a:
#     #   True.
#     # if i == 4 or i == 3:
#     if i in [3, 4]:
#         b.append(i)
#
# print(b)







# 1. afafd
# 2. skjlkvd
# 3. serslb

# lst = [[1, 'afafd'], [2, 'skjlkvd'], [3, 'serslb']]
#
# for i in lst:
#     print(str(i[0]) + '. ' + i[1])

# a = 'hello'
# b = 'world'
# print(a + ' ' + b)


# b = 'hello'
a = [7.99, 9.99, 3.49, 15.99, 7.99, 19.99, 12.99, 11.99, 13.99, 9.99]
print(sum(a))
minimum = 100
maximum = 0

for num in a:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print(f'{maximum = }')
print(f'{minimum = }')
#
# # 1) кол-во элементов
# print(len(a))
#
# print(a.count(3))
# print(b.count('l'))

# g = 0
# d = len(a)
# for i in a:
#     g += i


# print(g / d)


# 11.440000

















