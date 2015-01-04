__author__ = 'pkisielewicz'

import random

bombs = 10
board = {}
boardWidth = 8
boardHeight = 8


def init_board():
    global board
    for row in range(0,boardHeight):
        for column in range(0,boardWidth):
            board[row,column] = 0
    print(board)


def generate_bombs():
    global bombs
    while bombs > 0:
        bomb_col_place = random.randrange(0,boardWidth)
        bomb_row_place = random.randrange(0,boardHeight)
        if board[bomb_row_place, bomb_col_place] != 9:  # 9 means there is bomb on this place
            board[bomb_row_place, bomb_col_place] = 9
            bombs -= 1


init_board()
generate_bombs()
print(board)