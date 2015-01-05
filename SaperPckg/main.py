__author__ = 'pkisielewicz'

import random

bombs = 10
board = {}
boardWidth = 8
boardHeight = 8


def init_board():
    global board
    for row in range(0, boardHeight):
        for column in range(0, boardWidth):
            board[row, column] = 0
    print(board)


def generate_bombs():
    global bombs
    while bombs > 0:
        bomb_col_place = random.randrange(0, boardWidth)
        bomb_row_place = random.randrange(0, boardHeight)
        if board[bomb_row_place, bomb_col_place] != 9:  # 9 means there is bomb on this place
            board[bomb_row_place, bomb_col_place] = 9
            count_bombs(bomb_row_place, bomb_col_place)
            bombs -= 1


def count_bombs(bomb_row_place, bomb_col_place):
    global board
    if bomb_row_place > 0:
        if bomb_col_place > 0:
            board[bomb_row_place - 1, bomb_col_place - 1] += 1
        board[bomb_row_place - 1, bomb_col_place] += 1
        if bomb_col_place < (boardWidth - 1):
            board[bomb_row_place - 1, bomb_col_place + 1] += 1
    if bomb_row_place < (boardHeight - 1):
        if bomb_col_place > 0:
            board[bomb_row_place + 1, bomb_col_place - 1] += 1
        board[bomb_row_place + 1, bomb_col_place] += 1
        if bomb_col_place < (boardWidth - 1):
            board[bomb_row_place + 1, bomb_col_place + 1] += 1
    if bomb_col_place > 0:
        board[bomb_row_place, bomb_col_place - 1] += 1
    if bomb_col_place < (boardWidth - 1):
        board[bomb_row_place, bomb_col_place + 1] += 1


def left_click(row, col):
    global board
    if board[row, col] >= 9:
        show_all_bombs()
    elif board[row, col] > 0:
        left_click(row, col) # Placeholder
    else:
        # Pokazanie wszystkich wspólnych zer i otaczających numerów
        if row > 0:
            if col > 0:
                left_click(row - 1, col - 1)
            left_click(row - 1, col)
            if col < (boardWidth - 1):
                left_click(row - 1, col + 1)
        if row < (boardHeight - 1):
            if col > 0:
                left_click(row + 1, col - 1)
            left_click(row + 1, col)
            if col < (boardWidth - 1):
                left_click(row + 1, col + 1)
        if col > 0:
            left_click(row, col - 1)
        if col < (boardWidth - 1):
            left_click(row, col + 1)


def show_all_bombs():
    for row in range(0, boardHeight):
        for column in range(0, boardWidth):
            if board[row, column] >= 9:
                left_click(row, column) # Placeholder


def right_click(row, col):
    global board
    # Ustawia flagę


init_board()
generate_bombs()
print(board)
