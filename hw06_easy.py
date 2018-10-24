__author__ = 'Алексей Коваленко'


import os
import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:

    def __init__(self, coords):
        self._a = math.sqrt((coords['x2'] - coords['x1']) ** 2 + (coords['y2'] - coords['y1']) ** 2)
        self._b = math.sqrt((coords['x3'] - coords['x2']) ** 2 + (coords['y3'] - coords['y2']) ** 2)
        self._c = math.sqrt((coords['x1'] - coords['x3']) ** 2 + (coords['y1'] - coords['y3']) ** 2)
        self.Pr = self._a + self._b + self._c
        self._p = self.Pr / 2
        self.Sq = round(math.sqrt((self._p * (self._p - self._a) * (self._p - self._b) * (self._p - self._c))), 2)
        self.h = {
            'h1': round(2 / self._a * self.Sq, 2),
            'h2': round(2 / self._b * self.Sq, 2),
            'h3': round(2 / self._c * self.Sq, 2)
        }

    @property
    def S(self):
        return self.Sq

    @property
    def P(self):
        return self.Pr


    @property
    def all_h(self):
        return self.h

coords = [
    {'x1': 0, 'y1': 0, 'x2': 4, 'y2': 4, 'x3': 0, 'y3': 8,},
    {'x1': 0, 'y1': 0, 'x2': 4, 'y2': 4, 'x3': 0, 'y3': 8,}
]

print('*** Задание 1 ***')

for i in coords:
    print('\n*** Для треугольника с координатами вершин: {} ***'.format(i))
    iTriangle = Triangle(i);
    print('Площадь треугольника: {}'.format(iTriangle.Sq))
    print('Периметр: {}'.format(iTriangle.Sq))
    print('Длины высот треугольника: {}'.format(iTriangle.all_h))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:

    def __init__(self, coords):
        self.is_trapeze = False

        self._a = math.sqrt((coords['x2'] - coords['x1']) ** 2 + (coords['y2'] - coords['y1']) ** 2)
        self._b = math.sqrt((coords['x3'] - coords['x2']) ** 2 + (coords['y3'] - coords['y2']) ** 2)
        self._c = math.sqrt((coords['x4'] - coords['x3']) ** 2 + (coords['y4'] - coords['y3']) ** 2)
        self._d = math.sqrt((coords['x1'] - coords['x4']) ** 2 + (coords['y1'] - coords['y4']) ** 2)

        self.h = {
            'A': self._a,
            'B': self._b,
            'C': self._c,
            'D': self._d,
        }

        if (self._a == self._c or self._b == self._d):
            self.is_trapeze = True
            self.p = self._a + self._b + self._c + self._c
            self.Sq = (self._a + self._b) / 4 * math.sqrt(4 * self._c ** 2 - (self._a - self._b) ** 2)

    @property
    def S(self):
        return self.Sq

    @property
    def P(self):
        return self.p

    @property
    def all_h(self):
        return self.h

    def verify(self):
        return self.is_trapeze

coords = [
    {'x1': 0, 'y1': 0, 'x2': 4, 'y2': 2, 'x3': 4, 'y3': 6, 'x4': 0, 'y4': 8},
    {'x1': 7, 'y1': 0, 'x2': 9, 'y2': 0, 'x3': 11, 'y3': 4, 'x4': 5, 'y4': 4}
]

print('\n*** Задание 2 ***')

for i in coords:
    iTrapeze = Trapeze(i);
    if (iTrapeze.verify()):
        print('\n*** Для трапеции с координатами вершин: {} ***'.format(i))
        print('Площадь: {}'.format(iTrapeze.Sq))
        print('Длины сторон: {}'.format(iTrapeze.all_h))
        print('Периметр: {}'.format(iTrapeze.P))
    else:
        print('\n*** Фигура с координатами вершин: {}  не может быть равнобокой трапецией ***'.format(i))

