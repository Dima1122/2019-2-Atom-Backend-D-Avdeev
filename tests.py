# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:16:06 2019

@author: User
"""
import sys
import os
from unittest import mock, TestCase, main
from crestiki_noliki import MyGame, main_menu, check_size_input

class HiddenPrints:
    '''скрываем принты'''
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class MyGameTest(TestCase):
    def test_size_matrix(self):
        with HiddenPrints():        
            original_input = mock.builtins.input
            mock.builtins.input = lambda _: "s"
            self.assertEqual(check_size_input(), None)
            mock.builtins.input = lambda _: "5"
            self.assertEqual(check_size_input(), 5)
            mock.builtins.input = lambda _: "1"
            self.assertEqual(check_size_input(), None)
            mock.builtins.input = original_input
            
    @mock.patch('builtins.input')
    def test_choose_mark(self, m_input):
        m_input.side_effect = ['x','o']
        result = MyGame.choose_mark()
        self.assertEqual(result, ['x', 'o'])

if __name__ == '__main__':
    main()