from engine import get_data_from_data_base



text = """

SELECT id, CONCAT(title, ' - ', director, ' (', running_time, ')') AS abc
FROM Films_2;


"""
# <         >       >=      <=      IS NOT NULL     BETWEEN

print(get_data_from_data_base(text))


a = 'hello'
b = 'world'

print(a + ' - ' + b)
print(f'{a} - {b}')


# ORDER BY
# WHERE

# DDL
# DML Data Manipulation Language
# DCL
# TCL
