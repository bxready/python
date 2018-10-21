__author__ = 'Алексей Коваленко'

import os
import sys
print('sys.argv = ', sys.argv)


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def input_dir_name():
    input('Введите название директории: ', dir_name)
    return dir_name


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("rm <dir_name> - Удаление директории")
    print("cd <dir_name> - смена текущей директории")
    print("list <dir_name> - список файлов директории")
    print("ping - тестовый ключ")


def make_dir():

    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def cd_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print(os.getcwd())
    except FileExistsError:
        print("Директория не существует")

def list_dir():
    print(os.listdir())

def rm_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return

    search_dir = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(search_dir):
        try:
            os.rmdir(search_dir)
            print('*** папка {} удалена ***'.format(dir_name))
        except OSError:
            print('Не удалось удалить {}'.format(dir_name))

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "rm": rm_dir,
    'cd': cd_dir,
    'list': list_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
    if not dir_name:
        dir_name = input_dir_name()
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")