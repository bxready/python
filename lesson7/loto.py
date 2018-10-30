__author__ = 'Алексей Коваленко'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

"""
Класс создает N карточек для лото 
"""
import random

class loto_card:

    cards = []

    def __init__(self, n, type_card = [0,3,5,15], columns = 9):
        self.a = type_card[0]
        self.b = type_card[1]
        self.na = type_card[2]
        self.ma = type_card[3]
        self.columns = columns
        for i in range(n):
            matrix, numbers = self.create()
            self.cards.append({
                'matrix': matrix,
                'numbers': numbers
            })
        pass

    """
    метод создает N карточек с полями, удовлетворящими условиям
    от A до B цифр в колонках, NS цифр в строках, и NA чисел в карточке
    Для типового лото параметры будут 0,3,5,15 
    Модель карты - матрица 5 * 3 с координатами ячеек, в которых располагаются цифры
    """
    def create(self):
        model = self.card_model([])
        model = self.fill(model)
        a = set([])
        for i, line in enumerate(model):
            a = set(line) | a
        return model, a

    def card_model(self, card = []):
        if len(card) > 0:
            model = card
        else:
            model = self._first_model()

        verify = self.veryfy(model)

        if type(verify) == bool:
            model = self.card_model([])

        if type(verify) == int:
            if verify < 15:
                stop_search = False
                while not stop_search:
                    x = random.randint(0, 2)
                    y = random.randint(0, 8)
                    if model[x][y] == 0:
                        model[x][y] = 1
                        stop_search = True
                model = self.card_model(model)
            elif verify > 15:
                model = self.card_model([])
            else:
                return model

        return model


    def _first_model(self):
        model = [[0 for j in range(self.columns)] for i in range(self.b)]
        return model


    """
    метод заполняет модель карты цифрами по правилам типового лото 
    в первой колонке цифры от 0 до 9, второй от 10 до 19 ... последней от 81 до 90
    """
    def fill(self, matrix):
        matrix_rotate = list(map(list, zip(*matrix)))
        for i, line in enumerate(matrix_rotate):
            n = sum(line)
            nc = set()
            while len(nc) < n:
                j = random.randint(1 * (i * 10), (i + 1) * 10 - 1)
                nc.add(j)
            nc = list(nc)
            nc.sort(reverse=True)

            for k in range(len(line)):
                if line[k] == 1:
                    matrix[k][i] = nc.pop()

        return matrix

    """
    метод рисует карту
    """
    def draw(self, loto_card):
        for i, line in enumerate(loto_card):
            print_line = [('-' if x == 0 else x) for x in line]
            print('{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}'.format(*print_line))

    """
    Проверяем модель карточки на соблюдение правил
    Если модель готова, то возвращается число MA, если не готова, число менее MA
    Если модель не соответсвует правилам - возврат False
    """
    def veryfy(self, matrix):
        if len(matrix) <= 0:
            return False
        s = 0
        for i in matrix:
            s += sum(i)
        if s > self.ma:
            return False
        for i in matrix:
            if sum(i) > self.na:
                return False
        return s


class game:

    def __init__(self):
        self.numbers = [i for i in range(1, 91)]
        self.victory = False
        self.victory_card = 0
        self.cards = loto_card(2, [0, 3, 5, 15], 9)

    def simple_generator(self):
        if len(self.numbers) > 0:
            i = random.randint(0, len(self.numbers)-1)
            val = self.numbers.pop(i)
            yield val


    def next_step(self):
        n = next(self.simple_generator())
        print('Новый бочонок: {} (осталось {})'.format(n, len(self.numbers)));
        print('\n***** карточка компьютера *****')
        self.cards.draw(self.cards.cards[0]['matrix'])
        print('\n***** карточка игрока *****')
        self.cards.draw(self.cards.cards[1]['matrix'])

        step = input('Зачеркнуть цифру? (y/n)')
        if (step.lower() == 'y' and not n in self.cards.cards[1]['numbers']):
            self.stop(0)
        if (step.lower() == 'n' and n in self.cards.cards[1]['numbers']):
            self.stop(0)

        self.redraw(n)


    def stop(self, victory_card = 0):
        self.victory = True
        self.victory_card = victory_card
        print('\n***** Игра окончена. Победитель {} *****'.format('Компьютер' if self.victory_card == 0 else 'Человек'))


    def start(self):
        while not self.victory:
            self.next_step()

    def redraw(self, n):
        for k in range(2):
            if n in self.cards.cards[k]['numbers']:
                for i, line in enumerate(self.cards.cards[k]['matrix']):
                    for j in range(len(line)):
                        if self.cards.cards[k]['matrix'][i][j] == n:
                            self.cards.cards[k]['matrix'][i][j] = 'X'
                self.cards.cards[k]['numbers'].remove(n)
                if len(self.cards.cards[k]['numbers']) < 2:
                    self.stop(k)



loto_game = game()
loto_game.start()
