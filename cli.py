from board import *

COLOR_YELLOW = "\033[0;33;40m"
COLOR_WHITE = "\033[0;37;40m"

def color_text(text, color):
    return f"{color}{text}{COLOR_WHITE}"

def print_title():         
    print(" _______ _        _______           _______")
    print("|__   __(_)      |__   __|         |__   __|")
    print("   | |   _  ___     | | __ _  ___     | | ___   ___")
    print("   | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\")
    print("   | |  | | (__     | | (_| | (__     | | (_) |  __/")
    print("   |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|\n")

def print_board(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            end = " | " if x < 2 else "\n"
            text = color_text(board[y][x], COLOR_YELLOW) if board[y][x].isnumeric() else board[y][x]
            print(text, end=end)
        if y < 2:
            print("---------")

print_title()
board = Board()
print_board(board.board)  
