# -*- coding: utf-8 -*-

__author__ = 'Алексей Коваленко'

import re

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

workers = {

}

class Person:

    __pattern = '^([\w\S]+)\s+([\w\S]+)\s+(\d+)\s+([\w\S]+)\s+(\d+)'
    __report_pattern = '^([\w\S]+)\s+([\w\S]+)\s+(\d+)'
    __print_pattern = '{:<15} {:<15} {:>6} {:>6} {:>10} {:>10} {:>10}\n'

    def __init__(self, data):
        self.parse(data)
        self.index = self.surname + ' ' + self.name
        workers[self.index] = self

    def parse(self, data):
        if re.fullmatch(self.__pattern, data):
            match = re.findall(self.__pattern, data)[0]
            self.surname = match[1]
            self.name = match[0]
            self.salary = int(match[2])
            self.state = match[3]
            self.plan = int(match[4])
            self.sum = 0
            self.fact = 0

    def add_report(data):
        if re.fullmatch(Person.__report_pattern, data):
            match = re.findall(Person.__report_pattern, data)[0]
            person = '{} {}'.format(match[1], match[0])
            if person in workers:
                workers[person].fact = int(match[2])
                if (workers[person].fact < workers[person].plan):
                    workers[person].sum = round(workers[person].fact / workers[person].plan * workers[person].salary, 2)
                    workers[person].premium = 0
                else:
                    hour = workers[person].salary / workers[person].plan
                    delta = workers[person].fact - workers[person].plan
                    workers[person].premium = round(delta * hour * 2, 2)
                    workers[person].sum = workers[person].premium + workers[person].salary
    @property
    def sal(self):
        result = 0
        return result


    def ls(self):
        return


    def print_header(file):
        line = ('Фамилия', 'Имя', 'Зарплата', 'План', 'Факт', 'Премия', 'Итого начислено')
        # to file
        file.write(Person.__print_pattern.format(*line))
        # to screen
        print(Person.__print_pattern.format(*line))


    def print_row(self, file):
        line = (self.surname, self.name, self.salary, self.plan, self.fact, self.premium, self.sum)
        # to file
        file.write(self.__print_pattern.format(*line))
        # to screen
        print(self.__print_pattern.format(*line))


def buh():

    with open("data/workers", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        lines.pop(0)
        for i in lines:
            worker = Person(i)
            workers[worker.index] = worker

    # загрузим по отработанному времени
    with open("data/hours_of", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        lines.pop(0)
        for i in lines:
            Person.add_report(i);

    # рассчитаем зарплату и выгрузим данные
    with open("data/vedomost.txt", "w", encoding="utf-8") as f:
        Person.print_header(f)
        for i in workers:
            workers[i].print_row(f)


buh()
print('\nРезультат выполнения Задания также выведен в ведомость "data/vedomost.txt"')