__author__ = 'pkisielewicz $ igawenda'

import random


class Saper():
    bombs = 10
    board = {}
    boardWidth = 8
    boardHeight = 8

    def init_board(self):
        global board
        for row in range(0, Saper.boardHeight):
            for column in range(0, Saper.boardWidth):
                board[row, column] = 0
        print(board)

    def generate_bombs(self):
        global bombs
        while bombs > 0:
            bomb_col_place = random.randrange(0, Saper.boardWidth)
            bomb_row_place = random.randrange(0, Saper.boardHeight)
            if board[bomb_row_place, bomb_col_place] != 9:  # 9 means there is bomb on this place
                board[bomb_row_place, bomb_col_place] = 9
                Saper.count_bombs(self, bomb_row_place, bomb_col_place)
                bombs -= 1

    def count_bombs(self, bomb_row_place, bomb_col_place):
        global board
        if bomb_row_place > 0:
            if bomb_col_place > 0:
                board[bomb_row_place - 1, bomb_col_place - 1] += 1
            board[bomb_row_place - 1, bomb_col_place] += 1
            if bomb_col_place < (Saper.boardWidth - 1):
                board[bomb_row_place - 1, bomb_col_place + 1] += 1
        if bomb_row_place < (Saper.boardHeight - 1):
            if bomb_col_place > 0:
                board[bomb_row_place + 1, bomb_col_place - 1] += 1
            board[bomb_row_place + 1, bomb_col_place] += 1
            if bomb_col_place < (Saper.boardWidth - 1):
                board[bomb_row_place + 1, bomb_col_place + 1] += 1
        if bomb_col_place > 0:
            board[bomb_row_place, bomb_col_place - 1] += 1
        if bomb_col_place < (Saper.boardWidth - 1):
            board[bomb_row_place, bomb_col_place + 1] += 1

    def left_click(self, row, col):
        global board
        if board[row, col] >= 9:
            Saper.show_all_bombs()
        elif board[row, col] > 0:
            Saper.left_click(row, col)# Placeholder
        else:
            # Pokazanie wszystkich wspólnych zer i otaczających numerów
            if row > 0:
                if col > 0:
                    Saper.left_click(self, row-1, col - 1)
                Saper.left_click(self, row-1, col)
                if col < (Saper.boardWidth - 1):
                    Saper.left_click(self, row-1, col + 1)
            if row < (Saper.boardHeight - 1):
                if col > 0:
                    Saper.left_click(self, row+1, col - 1)
                Saper.left_click(self, row+1, col)
                if col < (Saper.boardWidth - 1):
                    Saper.left_click(self, row+1, col + 1)
            if col > 0:
                Saper.left_click(self, row, col - 1)
            if col < (Saper.boardWidth - 1):
                Saper.left_click(self, row, col + 1)

    def show_all_bombs(self):
        for row in range(0, Saper.boardHeight):
            for column in range(0, Saper.boardWidth):
                if board[row, column] >= 9:
                    Saper.left_click(self, row, column)# Placeholder

    def right_click(self, row, col):
        global board
        Saper.right_click(self, row, col)
        # Ustawia flagę

    #Saper.init_board()
    #Saper.generate_bombs()
    #print(board)
