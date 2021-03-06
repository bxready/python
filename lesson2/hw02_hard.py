__author__ = 'Коваленко Алексей Иванович'


import re

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y


def linear(equation, x):
    y = None
    pattern = '[yY]\s*\=\s*([-+]?\d+\.?\d*)[xX]\s*([-+])\s*(\d+\.?\d*)?'
    if re.fullmatch(pattern, equation):
        match = re.findall(pattern, equation)[0]
        a = float(match[0])
        b = float(match[2])
        if match[1] == '-':
            b *= -1
        y = a * x + b
    return y


equation = 'y = -12x + 11111140.2121'
# equation = 'y = -3x + 2'
# equation = 'y = 3.5x - 1'
# equation = 'y=3.5x-1'
x = 2.5
print('*** координата y функции  *** ', equation, ' при x =', x)
print('y =', linear(equation, x))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)


def verify_date(string):
    pattern = '(?<!-)(0\d|1\d|2\d|30|31)\.([0-1][0-2])\.(\d{1,4})'
    calendar = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 30,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }
    state = False
    if re.fullmatch(pattern, string):
        match = re.findall(pattern, string)[0]
        if (int(match[0]) <= calendar.get(match[1])) and (int(match[2]) <= 9999) and (int(match[2]) > 0):
            state = True
    return 'Дата корректна' if state else 'Дата некорректна'


# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'
date = '28.02.1985'

print('\n*** Задание 3 ***')
print('Проверка даты ', date)
print(verify_date(date))


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


def vav(app):
    d = 0
    floor = 0
    f = 0
    while f < app:
        d += 1
        floor += d
        f += d ** 2
    # нашли сектор в который попала квартира, определяем его границы
    floor1 = floor - d  # Этаж, предшествующий нашему сектору
    app_delta = app - f + d ** 2
    # определяем этаж и выход обычным делением на этажи
    floor_exit = app_delta // d + floor1
    gate = app_delta % d
    if gate > 0:    # если будет ноль, значит квартира последняя на этаже, иначе же будет на сл. этаже
        floor_exit += 1
    else:
        gate = d

    return floor_exit, gate


print('\n*** Задание 3 ***')
app = input('*** Введите номер квартиры ***: ')
floor, gate = vav(int(app))
print('*** Координаты квартиры (этаж / выход) ***')
print(floor, ' ', gate)
