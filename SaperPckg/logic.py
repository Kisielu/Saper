__author__ = 'pkisielewicz $ igawenda'

import random


class Saper():

    #bombs = 10
    #board = {}
    #boardWidth = 8
    #boardHeight = 8

    def __init__(self):
        self.bombs = 10
        self.board = {}
        self.boardWidth = 8
        self.boardHeight = 8

    def init_board(self):
        for row in range(0, self.boardHeight):
            for column in range(0, self.boardWidth):
                self.board[row, column] = 0
        print(self.board)

    def generate_bombs(self):
        self.bombs = 10
        while self.bombs > 0:
            bomb_col_place = random.randrange(0, self.boardWidth)
            bomb_row_place = random.randrange(0, self.boardHeight)
            if self.board[bomb_row_place, bomb_col_place] != 9:  # 9 means there is bomb on this place
                self.board[bomb_row_place, bomb_col_place] = 9
                self.count_bombs(bomb_row_place, bomb_col_place)
                self.bombs -= 1
        print(self.board)

    def count_bombs(self, bomb_row_place, bomb_col_place):
        if bomb_row_place > 0:
            if bomb_col_place > 0:
                self.board[bomb_row_place - 1, bomb_col_place - 1] += 1
            self.board[bomb_row_place - 1, bomb_col_place] += 1
            if bomb_col_place < (self.boardWidth - 1):
                self.board[bomb_row_place - 1, bomb_col_place + 1] += 1
        if bomb_row_place < (self.boardHeight - 1):
            if bomb_col_place > 0:
                self.board[bomb_row_place + 1, bomb_col_place - 1] += 1
            self.board[bomb_row_place + 1, bomb_col_place] += 1
            if bomb_col_place < (self.boardWidth - 1):
                self.board[bomb_row_place + 1, bomb_col_place + 1] += 1
        if bomb_col_place > 0:
            self.board[bomb_row_place, bomb_col_place - 1] += 1
        if bomb_col_place < (self.boardWidth - 1):
            self.board[bomb_row_place, bomb_col_place + 1] += 1

    def left_click(self, row, col):
        if self.board[row, col] >= 9:
            self.show_all_bombs()
        elif self.board[row, col] > 0:
            pass# Placeholder
        else:
            # Pokazanie wszystkich wspólnych zer i otaczających numerów
            pass
            """if row > 0:
                if col > 0:
                    self.left_click(row-1, col - 1)
                self.left_click(row-1, col)
                if col < (self.boardWidth - 1):
                    self.left_click(row-1, col + 1)
            if row < (self.boardHeight - 1):
                if col > 0:
                    self.left_click(row+1, col - 1)
                self.left_click(row+1, col)
                if col < (self.boardWidth - 1):
                    self.left_click(row+1, col + 1)
            if col > 0:
                self.left_click(row, col - 1)
            if col < (self.boardWidth - 1):
                self.left_click(row, col + 1)"""

    def show_all_bombs(self):
        for row in range(0, self.boardHeight):
            for column in range(0, self.boardWidth):
                if self.board[row, column] >= 9:
                    pass# Placeholder

    def right_click(self, row, col):
        print ("Right click")
        # Ustawia flagę

    def new_game(self):
        self.init_board()
        self.generate_bombs()

#saper = Saper()

#saper.new_game()

