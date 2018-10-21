__author__ = 'Алексей Коваленко'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def get_delimiter():
    return '/' if os.name == 'linux' else '\\';

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <dir_name> - удаляет указанный файл")
    print("cd <dir_name> - смена текущей директории на указанную")
    print("ls <dir_name> - отображение полного пути текущей директории")
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


def cp_file():
    if not dir_name:
        print("Необходимо указать имя файла, который надо скопировать")
        return

    search_file = '{}{}{}'.format(os.getcwd(), get_delimiter(), dir_name)
    if os.path.isfile(search_file):
        fname, extension = os.path.splitext(dir_name)
        new_filename = '{}_copy{}'.format(fname, extension)
        try:
            shutil.copyfile(dir_name, new_filename);
            print('*** копирование файла {} в {} произведено успешно ***'.format(dir_name, new_filename))
        except IOError:
            print('Не удалось скопировать {}'.format(dir_name))
    else:
        print('*** файл {} не найдет ***'.format(dir_name))
        return


def ping():
    print("pong")


def list_dir():
    print(os.getcwd())


def rm_file():
    if not dir_name:
        print("Необходимо указать имя файла")
        return

    delete_flag = input('Подтвердите удаление файла [y/n]')
    if delete_flag.lower() !=  'y':
        return

    delimiter = '/' if os.name == 'linux' else '\\';

    search_file = '{}{}{}'.format(os.getcwd(), get_delimiter(), dir_name)
    if os.path.isfile(search_file):
        try:
            os.unlink(search_file)
            print('*** файл {} удален ***'.format(dir_name))
        except OSError:
            print('Не удалось удалить {}'.format(dir_name))


def cd_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print('Перешли в директорию {}'.format(os.getcwd()))
    except FileExistsError:
        print("Директория не существует")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "rm": rm_file,
    "cp": cp_file,
    "cd": cd_dir,
    "ls": list_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
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