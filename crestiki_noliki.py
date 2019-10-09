# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:55:19 2019
@author: User
"""


class MyGame():
    '''Самые лучшие крестики-нолики'''

    def __init__(self, size):
        self._size = size
        self.coord = self._fill_field()

    def _fill_field(self):
        '''for local use'''
        tmp = []
        k = 1
        for _ in range(self._size):
            tmp_2 = []
            for _ in range(self._size):
                tmp_2.append(k)
                k += 1
            tmp.append(tmp_2)
        return tmp

    def draw_field(self):
        '''it draws the field'''
        print("---" * self._size)
        for i in range(self._size):
            for j in range(self._size):
                if self._size > 3:
                    if len(str(self.coord[i][j])) == 1:
                        print(f'|{self.coord[i][j]} ', end='')
                    else:
                        print(f'|{self.coord[i][j]}', end='')
                else:
                    print(f'|{self.coord[i][j]}', end='')
            print('|')
            print("---" * self._size)

    def make_turn(self, turn, mark):
        '''it enters your mark in the entered position'''
        for i in range(self._size):
            for j in range(self._size):
                if self.coord[i][j] == turn:
                    self.coord[i][j] == mark
                    return True
        return False

    def choose_mark():
        mark = []
        m_1 = input('Игрок1, пожалуйста, выберите вашу метку: ')
        m_2 = input('Игрок2, пожалуйста, выберите вашу метку: ')
        mark.append(m_1)
        mark.append(m_2)
        return mark

    def _check_turn(self, player_num):
        while True:
            try:
                turn = int(input(f'Ваш ход, Игрок{player_num}: '))
                for row in self.coord:
                    for element in row:
                        if element == turn:
                            return turn
                print(
                    'Вы можете ввести только те числа, что есть на поле!!!')
            except ValueError:
                print(
                    'Вы можете ввести только те числа, что есть на поле!!!')

    def check_win(self):
        '''check if someone has won'''
        for i in range(self._size):
            tmp = list(str(self.coord[i][0])) * self._size
            if tmp == self.coord[i]:
                return True
        for i in range(self._size):
            tmp = list(str(self.coord[i][0])) * self._size
            tmp2 = []
            for j in range(self._size):
                tmp2.append(self.coord[j][i])
            if tmp == tmp2:
                return True
        tmp = list(str(self.coord[0][0])) * self._size
        tmp2 = []
        for i in range(self._size):
            for j in range(self._size):
                if i == j:
                    tmp2.append(self.coord[i][j])
        if tmp == tmp2:
            return True
        tmp = list(str(self.coord[self._size - 1][0])) * self._size
        tmp2 = []
        for i in range(self._size):
            for j in range(self._size):
                if (self._size - 1 - i) == j:
                    tmp2.append(self.coord[i][j])
        if tmp == tmp2:
            return True
        return False


def check_size_input():
    '''checks if the nymber for matrix is correct '''
    try:
        size = int(input('Введите размер таблицы: '))
        if size < 2:
            print('Введите число не меньше 2 !!!')
            return None
        return size
    except ValueError:
        print('Введите корректное число !!!')


def main_menu():
    '''main menu'''
    size = check_size_input()
    while size is None:
        size = check_size_input()
    game = MyGame(size)
    mark = MyGame.choose_mark()
    k = 0
    while True:
        game.draw_field()
        if k % 2 == 0:
            turn = game._check_turn(1)
        else:
            turn = game._check_turn(2)
        for i in range(game._size):
            for j in range(game._size):
                if turn == game.coord[i][j]:
                    game.coord[i][j] = mark[k % 2]
        if game.check_win():
            print(f'Поздравляем тебя, игрок{(k%2)+1}, ты выиграл')
            break
        if k + 1 == game._size ** 2:
            print('Похоже, соперники одинаково сильны')
            break
        k += 1

# main_menu()
