__author__ = 'Алексей Коваленко'

import time
import random


class CrossZero:

    _messages = {
        'wait':[
            'Думаю...',
            'Хмм...',
            'Ух ты...',
            'Ну ну...',
            'И что мне теперь делать...'
        ]
    }

    def __init__(self, params):
        if type(params) != dict:
            params = {}
        self.field_width = 3 if 'width' not in params else params['width']
        self.line_for_victory = 3 if 'line' not in params else params['line']
        self.gamers = {
            1: {
                'type': 'AI',
                'figure': 'X',
                'concurrent': '0',
                'name': 'Computer1'
            } if 'gamer1' not in params else params['gamer1'],
            2: {
                'type': 'AI',
                'figure': '0',
                'concurrent': 'X',
                'name': 'Computer2'
            } if 'gamer2' not in params else params['gamer2'],
        }
        self.board = ['']*10
        # self.board = ['', '', '', 'X', 'X', 'X', '', '0', '', '']
        self.win_combination = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
        self.step = 1
        self.step_count = 0
        self.stop_game = False


    def next_step(self):

        gamer = self.current_gamer()
        print('*** Шаг {} ***'.format(self.step_count))

        if gamer['type'] == 'AI':
            self.step_AI(gamer)
        else:
            self.step_H(gamer)

        self.step_count += 1


    def current_gamer(self, inverse = True):
        if self.step_count % 2 == 0:
            return self.gamers[1 if inverse else 2]
        else:
            return self.gamers[2 if inverse else 1]


    def play(self):
        self.draw_board()
        while True:

            strval = self.next_step()
            if self.stop_game:
                break

            self.draw_board()

            win, figure = self.win_analize(self.board)
            if win:
                self.stop('win', self.current_gamer(False))
                break
            empty_cells = self.empty_cells(self.board)
            if len(empty_cells) == 0:
                self.stop('nowin')
                break


    def step_AI(self, gamer):
        print(self._messages['wait'][random.randint(0, len(self._messages['wait'])-1)])
        next_step = self.search_combination(gamer)
        time.sleep(2)
        self.board[next_step] = gamer['figure']



    def step_H(self, gamer):
        cell = int(input('Введите номер ячейки, в которую надо вписать крестик (1-9) или 0, если хотите закончить игру'))
        if cell == 0:
            self.stop_game = True
            self.stop('close')
            return
        if cell not in range(1,9):
            print('Такой ячейки нет.')
        elif self.board[cell] == 'X' or self.board[cell] == '0':
            print('Данная ячейка уже занята символом {}'.format(self.board[cell]))
            self.step_H()
        else:
            self.board[cell] = gamer['figure']


    def search_combination(self, gamer):
        """
        есть несколько простых правил в крестиках ноликах 3 на 3
        первым легче выиграть сходив в центр
        второй игрок ни в коем случае не должен занимать недиагональные клетки вторым ходом иначе это 100% проигрыш
        проверим данные правила на первом и втором ходе
        """
        if self.step_count == 0:
            return 5
        if self.step_count == 1 and len(self.board[5]) == 0:
            return 5
        if self.step_count == 1:
            while True:
                i = random.randint(1,9)
                if i % 2 > 0 and i != 5:
                    break;
            return i

        """
        если мы ходили первыми в центр и противник не закрыл диагональ, 
        вычисляем клетку с выигрышной комбинацией
        """
        if self.step_count == 2:
            figure = gamer['concurrent']
            if figure in [self.board[2], self.board[4], self.board[6], self.board[8]]:
                while True:
                    i = random.randint(1, 9)
                    if i % 2 > 0 and i != 5:
                        break;
                return i

        """
        все остальное
        играем по принципу - лишь бы не дать выиграть противнику и не упустить свою удачу
        проверяем нет ли выигрышной комбинации и не выиграет ли соперник следующим ходом
        тогда надо будет перекрыть ему клетку
        """

        empty_cells = self.empty_cells(self.board)

        for i in empty_cells:
            new_board = self.board.copy()
            new_board[i] = gamer['figure']
            win, figure = self.win_analize(new_board)
            if win and figure == gamer['figure']:
                return i

        for i in empty_cells:
            new_board = self.board.copy()
            new_board[i] = gamer['concurrent']
            win, figure = self.win_analize(new_board)
            if win and figure == gamer['concurrent']:
                return i

        """
        далее просто играем проверяя ходы на возможный выигрыш, считая потенциальные победы
        выбираем комбинацию с двумя победами или любую с одной потенциально возможной
        """

        # для выигрыша ищем не первую попавшуюся клетку, а клетку с несколькими потенциальными победами

        win_cell = 0
        max_win = 0
        for i in empty_cells:
            new_board = self.board.copy()
            new_board[i] = gamer['figure']
            win, figure = self.win_analize(new_board)
            if win and figure == gamer.figure:
                win_count = self.win_count(new_board, gamer['figure'])
                if win_count > max_win:
                    max_win = win_count
                    win_cell = i
        if max_win > 0:
            return i

        if (len(empty_cells) > 1):
            i = empty_cells[random.randint(1, len(empty_cells)-1)]
        else:
            i = empty_cells[0]
        return i


    def empty_cells(self, board):
        cells = []
        for i in range(1,10):
            if len(self.board[i]) == 0:
                cells.append(i)
        return cells

    def win_analize(self, board):
        for i in self.win_combination:
            if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and ( board[i[0]] == 'X' or board[i[0]] == '0' ):
                return True, board[i[0]]
        return False, False

    def win_count(self, board, figure):
        count = 0
        for i in self.win_combination:
            win = True
            for j in i:
                if j != '' and j != figure:
                    win = False
            if win:
                count += 1
        return count

    def stop(self, state, winner = False):
        if state == 'win':
            print('Игра окончена. Победитель: ', winner['name'])
        elif state == 'close':
            print('Очень жаль')
        else:
            print ('Ничья!')

    def draw_board(self):
        matrix = [' ' if len(x) == 0 else x for x in self.board]

        print('*** Поле ***    *** Схема ячеек по номерам'.format(self.step_count))
        print(' {} | {} | {}         1 | 2 | 3'.format(matrix[1], matrix[2], matrix[3]))
        print(' ----------        ---------')
        print(' {} | {} | {}         4 | 5 | 6'.format(matrix[4], matrix[5], matrix[6]))
        print(' ----------        ---------')
        print(' {} | {} | {}         7 | 8 | 9'.format(matrix[7], matrix[8], matrix[9]))


class game:

    def __init__(self):
        pass


    def start(self, params):
        new_game = CrossZero(params)
        new_game.play()
        self.input_vars(True)

    def input_vars(self, repeat = False):
        params = {
            'gamer1': {
                'type': 'AI',
                'figure': 'X',
                'concurrent': '0',
                'name': 'Computer1'
            },
            'gamer2': {
                'type': 'AI',
                'figure': '0',
                'concurrent': 'X',
                'name': 'Computer2'
            },
        }
        st = input('Рубанемся в кресты и баранки{}? (y/n)'.format(' еще разок' if repeat else ''))
        if st.lower() == 'y':
            print('Сами играть изволите, али на железных монстров поглядите?')
            print('Возможные варианты:')
            print('1 - схватка компьютеров')
            print('2 - человек против машины')
            while True:
                v = input('Введите вариант: ')
                if v in ['1', '2']:
                    break
                else:
                    print('Такого варианта нет')
            if (v == '2'):
                while True:
                    print('Крестики ходят первыми, нолики вторыми.')
                    print('За кого играть будете? 1 - крестики, 2 - нолики')
                    d = input('Введите вариант: ')
                    if d in ['1', '2']:
                        break
                    else:
                        print('Такого варианта нет')
                if d == '1':
                    human = 'gamer1'
                    comp = 'gamer2'
                else:
                    human = 'gamer2'
                    comp = 'gamer1'
                params[human]['name'] = 'Человек'
                params[human]['type'] = 'H'
                params[comp]['name'] = 'Железный человек'
                params[comp]['type'] = 'AI'
                print(params)
            else:
                params = {}
            self.start(params)
        else:
            print('Ага! Кишка тонка!')
            print('Ну пока!')


my_game = game()
my_game.input_vars(False)