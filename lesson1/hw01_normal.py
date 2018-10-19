
__author__ = 'Коваленко Алексей Иванович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

import random
import math


def max_number0(numb):   # только арифметическими операциями
    a = int(numb)
    maximum = 0
    while a > 0:
        b = a % 10
        a //= 10
        if b > maximum:
            maximum = b
    return maximum


def max_number(numb):   # первый вариант решения
    a = list(str(numb))
    maximum = 0
    while len(a) > 0:
        b = int(a.pop())
        if b > maximum:
            maximum = b
    return maximum


def max_number2(numb):   # второй вариант решения
    a = str(numb)
    maximum = 0
    for i in a:
        b = int(i)
        if b > maximum:
            maximum = b
    return maximum


def max_number3(numb):   # третий вариант решения, тупое
    a = list(str(numb))
    return max(a)


numb = random.randint(100, 99999)
print("*** число ***")
print(numb)
print(("*** 0 вариант решения (только арифметические операции). Самая большая цифра ***: ", max_number0(numb)))
print(("*** 1 вариант решения. Самая большая цифра ***: ", max_number(numb)))
print("*** 2 вариант решения. Самая большая цифра ***: ", max_number2(numb))
print("*** 3 вариант решения. Просто проверить поведение питонв :) ***: ", max_number3(numb))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

def exchange():
    a = input('Введите первое число a: ')
    b = input('Введите второе число b: ')
    (a, b) = (b, a)
    print("Замена произведена")
    print("Теперь первое число a: ", a)
    print("ыторое число b: ", b)


print('*** выполнение второго задания ***')
exchange()


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


def qvur():
    a = float(input('Введите коэффициент a: '))
    b = float(input('Введите коэффициент b: '))
    c = float(input('Введите коэффициент c: '))
    Discr = b * b - 4 * a * c
    if Discr >= 0:
        x1 = (-b + math.sqrt(Discr)) / (2 * a)
        x2 = (-b - math.sqrt(Discr)) / (2 * a)
        print('Дискриминант равен: ', Discr)
        print('x1 равен: ', x1)
        print('x2 равен: ', x2)
    else:
        print("Дискриминант отрицателен, корней нет")


qvur()