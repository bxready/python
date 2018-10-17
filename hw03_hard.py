# -*- coding: utf-8 -*-

__author__ = 'Алексей Коваленко'

import fractions
import random
import re
import os

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def fract(equation):
    pattern = '[-+]?(\d+)\/(\d+)\s*([-+])\s*(\d+)\/(\d+)'
    if re.fullmatch(pattern, equation):
        match = re.findall(pattern, equation)[0]
        a1 = int(match[0])
        b1 = int(match[1])
        a2 = int(match[3])
        b2 = int(match[4]) * (-1 if match[2] == '-' else 1)
        y = fractions.Fraction(a1, b1) + fractions.Fraction(a2, b2)

        result = {
            'numerator': y.numerator,
            'denominator': y.denominator,
            'int': y.numerator // y.denominator
        }
        if result.get('int') > 0:
            result['numerator'] = result['numerator'] - result['int'] * result['denominator']

        return result.get('int'), result.get('numerator'), result.get('denominator')
    else:
        return False


# для удосбтва напишем алгоритм генерации  и проверки примеров
print('Задание 1')
for i in range(10):
    equation = str('-' if random.randint(1, 10) % 5 == 0 else '') + str(random.randint(1, 20)) + '/' + str(random.randint(1, 10))
    equation += str(' - ' if random.randint(1, 10) % 2 == 0 else ' + ') + str(random.randint(1, 20)) + '/' + str(random.randint(1, 10))
    print('Пример {}: {}'.format(i, equation))
    f = fract(equation)
    if type(f) != bool:
        print('Ответ: {} {}/{}'.format(*fract(equation)))
    else:
        print('Выражение не корректно')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def buh():

    # заведем словарь для расчета длин строк (потом будем пользоваться им при выводе)
    max_len = {
        'Name': 0,
        'Surname': 0,
        'Sal': 0,
        'State': 0,
        'Plan': 0,
        'Percent': 0,
        'Fact': 0,
        'Sum': 0,
    }

    # Разберем список сотрулников
    workers = {}
    with open("data/workers", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        lines.pop(0)
        pattern = '^([\w\S]+)\s+([\w\S]+)\s+(\d+)\s+([\w\S]+)\s+(\d+)'
        for i in lines:
            if re.fullmatch(pattern, i):
                match = re.findall(pattern, i)[0]
                workers['{} {}'.format(match[1], match[0])] = {
                    'Name': match[0],
                    'Surname': match[1],
                    'Sal': int(match[2]),
                    'State': match[3],
                    'Plan': int(match[4]),
                    'Percent': 0,
                    'Fact': 0,
                    'Sum': 0,
                }
    # загрузим в словарь информацию по отработанному времени
    with open("data/hours_of", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        lines.pop(0)
        pattern = '^([\w\S]+)\s+([\w\S]+)\s+(\d+)'
        for i in lines:
            if re.fullmatch(pattern, i):
                match = re.findall(pattern, i)[0]
                person = '{} {}'.format(match[1], match[0])
                if person in workers:
                    workers[person]['Fact'] = int(match[2])
                    workers[person]['Percent'] = round(workers[person]['Fact'] / workers[person]['Plan'] * 100, 1)
                    workers[person]['Sum'] = round(workers[person]['Fact'] / workers[person]['Plan'] * workers[person]['Sal'], 2)
    # выгрузим рассчитанную зарплату в файл
    with open("data/vedomost.txt", "w", encoding="utf-8") as f:
        pattern = '{:<15} {:<15} {:<6} {:<6} {:<10} %{:<10} {}\n'
        line = ('Фамилия', 'Имя', 'Зарплата', 'План', 'Факт', '%от плана', 'Начислено')
        f.write(pattern.format(*line))
        for i in workers:
            line = (workers[i]['Surname'], workers[i]['Name'], workers[i]['Sal'], workers[i]['Plan'], workers[i]['Fact'], workers[i]['Percent'], workers[i]['Sum'])
            f.write(pattern.format(*line))


buh()
print('\nРезультат выполнения Задания 2 выведен в ведомость "data/vedomost.txt"')

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


def fruits():
    # на всякий случай почистим ранее созданные файлы
    abc = list(map(chr, range(ord('А'), ord('Я')+1)))
    for i in abc:
        file = "data/fruits_{}.txt".format(i)
        if os.path.exists(file):
            os.remove(file)
    # Основной блок. Разбираем фрукты
    with open("data/fruits.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = list(filter(lambda x: len(x) > 0, [line.rstrip() for line in lines]))
        for i in lines:
            with open("data/fruits_{}.txt".format(i[0]), "a", encoding="utf-8") as fi:
                fi.write('{}\n'.format(i))


fruits()
print('\nРезультат выполнения Задания 3 находится в папке "data"')
