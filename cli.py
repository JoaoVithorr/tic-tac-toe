from board import *

COLOR_WHITE = "\033[37m"
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = "\033[33m"
COLOR_RED = "\033[31m"


def color_text(text, color):
    return f"{color}{text}{COLOR_WHITE}"


def display_title():         
    print(" _______ _        _______           _______")
    print("|__   __(_)      |__   __|         |__   __|")
    print("   | |   _  ___     | | __ _  ___     | | ___   ___")
    print("   | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\")
    print("   | |  | | (__     | | (_| | (__     | | (_) |  __/")
    print("   |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|\n")

def display_board(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            end = " | " if x < 2 else "\n"
            text = color_text(board[y][x], COLOR_YELLOW) if board[y][x] != "X" or board[y][x] != "O" else board[y][x]
            print(text, end=end)
        if y < 2:
            print("---------")
    print()