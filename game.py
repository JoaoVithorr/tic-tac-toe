from board import Board
from cli import *


def start_game():
    board = Board()
    # Jogador X sempre começa o jogo 
    current_player = "X"

    display_title()

    while True:
        display_board(board.board)
        position = input(f"Jogador {current_player}, escolha uma casa (1-9): ")

        try:
            position = int(position)
        except:
            print(color_text("Digite apenas números, outros caracteres são inválidos.\n", COLOR_RED))
            continue

        print("-----------------------------------------")

        if position < 1 or position > 9:
            print(color_text("Casa inválida, escolha outra casa (1-9).", COLOR_RED))
            continue

        if not board.is_valid_position(position):
            print(color_text("Casa já ocupada, escolha outra casa.", COLOR_RED))
            continue
        
        board.play(current_player, position)

        win = board.check_winning_positions()
        draw = board.check_draw_positions()
        
        if win:
            print(color_text(f"Parabéns jogador {current_player}, você venceu!", COLOR_GREEN))
            display_board(board.board)
            break

        if draw:
            print(color_text("Foi um empate :(", COLOR_YELLOW))
            display_board(board.board)
            break
         
        #  Alternando entre os jogadores
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        
start_game()