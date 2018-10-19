__author__ = 'Коваленко Алексей Иванович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

import random


def print_number(numb):   # первый вариант решения
    a = list(str(numb))
    while len(a) > 0:
        print(a.pop())


def print_number2(numb):   # второй вариант решения
    a = str(numb)
    for i in a:
        print(i)


def print_number3(numb):   # третий вариант решения
    a = int(numb)
    while a > 0:
        print(a % 10)
        a //= 10


numb = random.randint(100, 99999)
print("*** число ***")
print(numb)
print("*** 1 вариант решения ***")
print_number2(numb)
print("*** 2 вариант решения ***")
print_number(numb)
print("*** 3 вариант решения только арифметические операции***")
print_number3(numb)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


def exchange():
    a = input('Введите первое число a: ')
    b = input('Введите второе число b: ')
    c = a
    a = b
    b = c
    print("Замена произведена")
    print("Теперь первое число a: ", a)
    print("ыторое число b: ", b)


print('*** выполнение второго задания ***')
exchange()

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


def user_confirm():
    a = input('Введите ваш возраст: ')
    a = int(a)
    if a < 18:
        print("Извините, пользование данным ресурсом только с 18 лет")
    elif a > 100:
        print("Не верю")
    else:
        print('Досутп разрешен')


print('*** выполнение третьего задания ***')
user_confirm()