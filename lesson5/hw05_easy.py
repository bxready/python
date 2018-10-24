__author__ = 'Алексей Коваленко'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

print('*** Задание 1 ***')

for i in range(1,10):
    new_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i));
    try:
        os.mkdir(new_dir)
        print('*** папка {} создана ***'.format('dir_{}'.format(i)))
    except FileExistsError:
        print('директория {} уже существует'.format('dir_{}'.format(i)))



delete_mode = False #  запутить режим удаления

if delete_mode:
    for i in range(1,10):
        search_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        if os.path.isdir(search_dir):
            try:
                os.rmdir(search_dir)
                print('*** папка {} удалена ***'.format('dir_{}'.format(i)))
            except OSError:
                print('Не удалось удалить {}'.format('dir_{}'.format(i)))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\n*** Задание 2 ***')
print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n*** Задание 3 ***')

path, filename = os.path.split(__file__)
fname, extension = os.path.splitext(filename)
new_filename = '{}_copy{}'.format(fname, extension)

try:
    shutil.copyfile(filename, new_filename);
    print('*** копирование файла {} в {} произведено успешно ***'.format(filename, new_filename))
except IOError:
    print('Не удалось скопировать {}'.format(filename))


