import time
import pygame
from checkers.constants import NUM_CHANCES, WIDTH, HEIGHT, LIGHT, SQUARE_SIZE, DARK, GREY, GREEN
from checkers.board import Board
from checkers.game import Game

from checkers.gpt_player import GPTPlayer
import json


FPS = 60
WIN = pygame.display.set_mode((WIDTH , HEIGHT))

pygame.display.set_caption('Checkers')


def get_new_position_from_human(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def get_new_position_from_gpt(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
 
    # gptPlayer = GPTPlayer()
    # res = gptPlayer.send_first_question()
    # out = gptPlayer.get_answer(res)
    # print(out)
    # # print("-------------------------")
    game.gpt_player.send_first_question()
    count = 0
    
    while run:
        clock.tick(FPS)

        if (game.winner() != None):
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = pygame.mouse.get_pos()
            #     row, col = get_new_position_from_human(pos)
            #     game.select(row, col)
            # if game.turn == (101, 67, 33):
            #     print("dark turn")
            # elif game.turn == (255, 255, 255):
            #     print("light turn")

            print("turn: ", game.get_turn())
            if game.turn == LIGHT:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_new_position_from_human(pos)
                    game.select(row, col)
                count = 0
            elif game.turn == DARK:
                gptBoard = game.board.capture_board_to_gpt()
                gptBoard_str = repr(gptBoard)
                gpt_moves = game.board.gpt_valid_moves()
                gpt_moves_str = repr(gpt_moves)
                # out = gptPlayer.send_question(gptBoard_str, gpt_moves_str)
                # answer = gptPlayer.get_answer(out)
                # print("----answer----------")
                # print(str(answer))
                # row, col, piece_row, piece_col, is_queen = gptPlayer.send_gpt_answer_to_game(str(answer))
                # count = 0
                # game.ai_move(row, col, piece_row, piece_col, is_queen, gpt_moves, count)
                out = game.gpt_player.send_question(gptBoard_str, gpt_moves_str)
                answer = game.gpt_player.get_answer(out)
                print("----answer----------")
                print(str(answer))
                row, col, piece_row, piece_col, is_queen =  game.gpt_player.send_gpt_answer_to_game(str(answer))
                # game.ai_move(row, col, piece_row, piece_col, is_queen, gpt_moves)
             
                if(count < NUM_CHANCES):
                    game.ai_move(row, col, piece_row, piece_col, is_queen, gpt_moves)
                    count += 1
                else:
                    print("errie mais de 3x")
                    game.ai_move_random(gpt_moves)
              

       
                
        game.update()
     




    pygame.quit()


main()

# board =" [[(0, 1), 'L', 'N'], [(0, 3), 'L', 'N'], [(0, 5), 'L', 'N'], [(0, 7), 'L', 'N'], [(1, 0), 'L', 'N'], [(1, 2), 'L', 'N'], [(1, 4), 'L', 'N'], [(1, 6), 'L', 'N'], [(2, 1), 'L', 'N'], [(2, 3), 'L', 'N'], [(2, 5), 'L', 'N'], [(2, 7), 'L', 'N'], [(5, 0), 'D', 'N'], [(5, 2), 'D', 'N'], [(5, 4), 'D', 'N'], [(5, 6), 'D', 'N'], [(6, 1), 'D', 'N'], [(6, 3), 'D', 'N'], [(6, 5), 'D', 'N'], [(6, 7), 'D', 'N'], [(7, 0), 'D', 'N'], [(7, 2), 'D', 'N'], [(7, 4), 'D', 'N'], [(7, 6), 'D', 'N']]"
