__author__ = 'Алексей Коваленко'

import random
import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

M = {0: 1, 1: 1}


def fib(n):     # сделаем функцию для расчета числа фибоначи на определенной позиции с запоминанием в словарь M
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]


def fibonacci(n, m):
    min_f = fib(n)
    return list(filter(lambda x: x > min_f, [fib(i) for i in range(m)]))


# для удобства напишем цикл проверки
print('Задание 1 (фибоначчи)')
for i in range(10):
    n = random.randint(0, 10)
    m = random.randint(11, 50)
    print('*** ищем числа на позициях в диапазоне [{} : {}]'.format(n, m))
    print(fibonacci(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


# для удобства напишем цикл проверки
print('\nЗадание 2 (сортировка)')
for i in range(10):
    list1 = [random.randint(-20, 20) for n in range(10)]
    print('*** Пример {}: Исходная последовательность - {}'.format(i, list1))
    print('*** Результат {}: {}'.format(i, sort_to_max(list1)))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(function, slice):
    filter_slice = []
    for i in slice:
        if function(i):
            filter_slice.append(i)
    return filter_slice


print('\nЗадание 3 (Собственный фильтр)')
for i in range(5):
    list1 = [random.randint(-20, 20) for n in range(10)]
    print('*** Пример {} : Исходная последовательность - {}'.format(i, list1))
    print('*** Ищем только четные: {}'.format(my_filter(lambda x: x % 2 == 0, list1)))
    print('*** Ищем только положительные: {}'.format(my_filter(lambda x: x > 0, list1)))
    print('*** Кратные трем: {}'.format(my_filter(lambda x: x % 3 == 0, list1)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_pg(coords):
    AB = math.sqrt((coords.get('A2')[0] - coords.get('A1')[0]) ** 2 + (coords.get('A2')[1] - coords.get('A1')[1]) ** 2)
    DC = math.sqrt((coords.get('A4')[0] - coords.get('A3')[0]) ** 2 + (coords.get('A4')[1] - coords.get('A3')[1]) ** 2)
    AD = math.sqrt((coords.get('A4')[0] - coords.get('A1')[0]) ** 2 + (coords.get('A4')[1] - coords.get('A1')[1]) ** 2)
    BC = math.sqrt((coords.get('A3')[0] - coords.get('A2')[0]) ** 2 + (coords.get('A3')[1] - coords.get('A2')[1]) ** 2)
    if AB == DC and BC == AD:
        return True
    else:
        return False


coords = {
    'A1': (1, 3),
    'A2': (4, 7),
    'A3': (2, 8),
    'A4': (-1, 4),
}
print('\nЗадание 4 (параллелограмм)\nКоординаты {} {} вершинами параллелограмма'.format(coords, 'являются' if is_pg(coords) else 'не могут быть'))
