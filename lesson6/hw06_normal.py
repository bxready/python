__author__ = 'Алексей Коваленко'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:

    def __init__(self, surname, name, fname, teacher = False):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.is_teacher = teacher


class Student:

    def __init__(self, surname, name, fname, father, mother):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.father = father
        self.mother = mother


class Klass:

    def __init__(self, name, subjects, students):
        self.name = name
        self.subjects = subjects
        self.students = students


class Subject:

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


class School:

    def __init__(self, name, klasses):
        self.name = name
        self.klasses = {}
        for i in klasses:
            self.klasses[i.name] = i


    def klass_list(self):
        result = []
        for i in self.klasses:
            result.append(i)
        result.sort()
        return result

    def student_list(self, klass):
        result = []
        for student in self.klasses[klass].students:
            result.append('{} {}. {}.'.format(student.surname, student.name[0], student.fname[0]))
        result.sort()
        return result

    def subject_list(self, klass):
        result = []
        for subject in self.klasses[klass].subjects:
            result.append(subject)
        return result


    def klass_by_student(self, surname, name, fname):
        result = False
        student = False
        all_klasses = self.klass_list()
        for i in all_klasses:
            for student in self.klasses[i].students:
                if student.name == name and student.surname == surname and student.fname == fname:
                    result = i
        return result, student


    def subjects_by_student(self, surname, name, fname):
        result = False
        klass, student = self.klass_by_student(surname, name, fname)
        if type(klass) != 'bool':
            result = self.klasses[klass].subjects
        return result


print('*** Задача про школу ***')

Sc = School('№ 155',[
    Klass(
        '5A',
        [
            Subject('математика', Person('Иванова', 'Мария', 'Петровна', True)),
            Subject('физика', Person('Иванова', 'Мария', 'Сергеевна', True)),
            Subject('физкультура', Person('Петров', 'Сергей', 'Федорович', True)),
        ],
        [
            Student('Иванов', 'Иван', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True), Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов2', 'Иван2', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True), Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов3', 'Cван3', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True), Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов4', 'Dван4', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True), Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов5', 'Иван5', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True), Person('Иванова', 'Мария', 'Петровна', True)),
        ]
    ),
    Klass(
        '5Б',
        [
            Subject('математика', Person('Иванова', 'Мария', 'Петровна', True)),
            Subject('физика', Person('Иванова', 'Мария', 'Сергеевна', True)),
            Subject('физкультура', Person('Петров', 'Сергей', 'Федорович', True)),
        ],
        [
            Student('Иванов', 'Иван', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True),
                    Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов2', 'Иван', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True),
                    Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов3', 'Иван', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True),
                    Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов4', 'Иван', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True),
                    Person('Иванова', 'Мария', 'Петровна', True)),
            Student('Иванов5', 'Иван', 'Вениаминович', Person('Иванов', 'Вениамин', 'Иванович', True),
                    Person('Иванова', 'Мария', 'Петровна', True)),
        ]
    )
]);

all_klasses = Sc.klass_list()

print ('\nЧасть 1 "Список учеников"')
print ('Список классов школы {}: {}'.format(Sc.name, all_klasses))

print ('\nЧасть 2 "Список учеников"')
for i in all_klasses:
    print ('\nСписок учеников {} класса: '.format(i))
    students = Sc.student_list(i)
    for j in students:
        print(j)


print ('\nЧасть 3 "Список предметов ученика"')
name = 'Иван'
surname = 'Иванов2'
fname = 'Вениаминович'
print ('Список предметов ученика {} {} {}: '.format(surname, name, fname))
subjects = Sc.subjects_by_student(surname, name, fname)
for i in subjects:
    print('{} , преподает: {} {} {}'.format(i.name, i.teacher.surname, i.teacher.name, i.teacher.fname))

print ('\nЧасть 4 "Родители ученика"')
name = 'Иван'
surname = 'Иванов4'
fname = 'Вениаминович'
print ('Список родителей ученика {} {} {}: '.format(surname, name, fname))
klass, student_ = Sc.klass_by_student(surname, name, fname)
print(' мама: {} {} {}'.format(student_.mother.surname, student_.mother.name, student_.mother.fname))
print(' папа: {} {} {}'.format(student_.father.surname, student_.father.name, student_.father.fname))

print ('\nЧасть 5 "Список учетилей"')
for i in all_klasses:
    print ('\nСписок учителей {} класса: '.format(i))
    subjects = Sc.subject_list(i)
    for j in subjects:
        print('{} {} {}: предмет {}'.format(j.teacher.surname, j.teacher.name, j.teacher.fname, j.name))
