# def digit_sum(number):
#     sum = 0
#
#     while number > 0:
#         dig = number % 10
#         sum += dig
#         number //= 10
#
#     return sum







# def top_bread():
#     print('/￣￣￣\\')
#
# def pomidorka():
#     print("◯◯◯◯")
#
# def sirok():
#     print("⋁ΞΞΞΞΞ⋁ ")
#
# def bottom_bread():
#     print('\_____/')
#
#
# top_bread()
# sirok()
# pomidorka()
#





# bottom_bread()
# def schochik():
#     sum = 10 + 20
#     print(sum)
#
#
#
# schochik()




# def calc(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
#
# calc(10, 5)



# warrior = {'здоровье': 100, 'атака': 30, 'защита': 25, 'навыки': {'щит': 10 }}
# archer = {'здоровье': 50, 'атака': 40, 'защита': 20, 'навыки': {'убежать': 10}, 'инвентарь': ['стрелы', 'меч', 'еда']}
# wizard = {'здоровье': 30, 'атака': 50, 'защита': 15, 'навыки': {'магический щит': 10, 'лечение': 5}}
#
# def print_dict(slowar):
#     for key, val in slowar.items():
#         print(f"{key}: {val}")
#
#
# for item in [warrior, archer, wizard]:
#     print_dict(item)



# def sum_numbers(a, b):
#     result = a +b
#     return result
#     print(sum_numbers(10, 5))
#
#
# sum_numbers(10, 5)


# def multiply_range(start, end):
#     if start > end:
#         start, end = end, start
#     result = 1
#     for i in range(start, end + 1):
#             result *= i
#
#
#     return result
#
# print(multiply_range(2, ))



# def fio(op: str) -> str:
#     ty = op.split(input(""))
#     for i in range():
#         acrony = (i)
#     print(acrony)
#
#
#
# ty = op.split(input("Введи свое ФИО: "))
#
# print(fio("Бебих Денис Владимерович"))




# def fio(w: str):
#     w_up_split= w.upper().split()
#     acronym = ""
#
#     for i in w_up_split:
#         acronym += i[0] + "."
#     return acronym
#
#
#
# res = fio("александр сергеевич пушкин")
# print(res)

# print(list(acronym))
#
#
#
#
# if round(answer, 2) == round(fifa, 2):
#     print("fifa ne pravelna!")

#первая и вторая домашка снизу

# def sub_nums(one_numder, two_number):
#     summer = one_numder - two_number
#
#     print(summer)
#
#
#
#
# sub_nums(50, 30)







# def multiply_nums(a, b):
#     summer = a * b
#     if a != float:
#         print("Функция вычитания работает только с числами")
#         print(0)
#     elif b != float:
#         print("Функция вычитания работает только с числами")
#         print(0)
#
#
# multiply_nums(50,20)










# def sum_nums(num1, num2):
#     if num1!= float:
#         print(0)
#     elif num2 != float:
#         print(0)
#     return float(num1) + float(num2)
#






import random


def generate_math_question(dif=10, symvvols=['+', '-', '*', '/']) -> str:
    num1 = random.randint(1, dif)
    num2 = random.randint(1, dif)
    symvol = random.choice(symvvols)

    if symvol == '//':
        while num1 % num2 != 0:
            num1 = random.randint(1, dif)
            num2 = random.randint(1, dif)

    return f"{num1} {symvol} {num2} = "



# 5 + 8 =
def find_right_answer(math_question: str) -> int | float: #закончить функцию
    lst = math_question.split()
    if lst[1] == "+":
        return int(lst[0]) + int(lst[2])
    elif lst[1] == "-":
        return int(lst[0]) - int(lst[2])
    elif lst[1] == "*":
        return int(lst[0]) * int(lst[2])
    elif lst[1] == "/":
        return int(lst[0]) / int(lst[2])


# print(find_right_answer("55 / 8 ="))




def check_answer(user_answer: str, right_answer: int | float) -> bool :
    try:
        user_answer = float(user_answer)
        return right_answer == user_answer
    except:
        return False


# print(check_answer("13", 13))

def matimatic_test():
    points = 0


    for i in range(10):
        primer = generate_math_question()
        user_ansfer = input(primer)
        right_answer = find_right_answer(primer)
        check = check_answer(user_ansfer, right_answer)

        if check:
            points += 1

    print(f"Ты ответил на {points} из 10")






matimatic_test()














