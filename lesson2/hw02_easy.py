__author__ = 'Коваленко Алексей Иванович'

import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


def format_str(str_list):
    if type(str_list) == list:
        fruit_list = {}
        i = 1
        max_l = 0
        for a in str_list:
            if len(a) > max_l:
                max_l = len(a)
            fruit_list[str(i)] = a
            i += 1
        for key in fruit_list:
            mask = '{}.{:>' + str(max_l + 1) + '}'
            print(mask.format(key, fruit_list[key]))


str_list = ['яблоко', 'мыло', 'соль', 'решетка', 'оса']

print('\n*** задание 1 ***')
print('*** форматирование *** функцией format')
format_str(str_list)


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


def delete_m(list1, list2):
    list3 = []
    if type(list1) == list and type(list2) == list:
        for key in list1:
            if key not in list2:
                list3.append(key)
    return set(list3)   # выбрасываем повторяющиеся


def delete_m2(list1, list2):    # списки вариант 2
    list3 = []
    if type(list1) == list and type(list2) == list:
        list3 = [item for item in list1 if item not in list2]
    return set(list3)   # выбрасываем повторяющиеся


def delete_m3(list1, list2):    # множества
    list3 = []
    if type(list1) == list and type(list2) == list:
       list3 = set(list1) - set(list2)
    return list3


list1 = [str(random.randint(0, 20)) for n in range(10)]
list2 = [str(random.randint(0, 20)) for n in range(10)]
print('\n*** Задание 2 ***')
print('*** list 1 ***')
print(list1)
print('*** list 2 ***')
print(list2)
print('*** результат вычитания вариант 1***')
print(delete_m(list1, list2))
print('*** результат вычитания вариант 2***')
print(delete_m2(list1, list2))
print('*** результат вычитания вариант 3*** с множествами')
print(delete_m3(list1, list2))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


def create_m(list1):
    list2 = []
    if type(list1) == list:
        for key in list1:
            if key % 2 == 0:
                list2.append(key / 4)
            else:
                list2.append(key * 2)
    return list2


def create_m2(list1):   # данный вариант списки + тернарный оператор
    list2 = []
    if type(list1) == list:
        list2 = [x / 4 if x % 2 == 0 else x * 2 for x in list1]
    return list2


list1 = [random.randint(0, 20) for n in range(10)]
print('\n*** Задание 3 ***')
print('*** list 1 ***')
print(list1)
print('*** результат вариант 1***')
print(create_m(list1))
print('*** результат вариант 2***')
print(create_m2(list1))
