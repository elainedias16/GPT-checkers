import pygame
from checkers.constants import WIDTH, HEIGHT, LIGHT, SQUARE_SIZE, DARK, GREY, GREEN
from checkers.board import Board
from checkers.game import Game

from checkers.gpt_player import GPTPlayer


FPS = 60
WIN = pygame.display.set_mode((WIDTH , HEIGHT))

pygame.display.set_caption('Checkers')


def get_new_position_from_human(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    gptPlayer = GPTPlayer()

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
                
            if game.turn == LIGHT:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_new_position_from_human(pos)
                    game.select(row, col)
                print("light turn")
            else:
                print("dark turn")
                # if event.type == pygame.MOUSEBUTTONDOWN:
                    # pos = pygame.mouse.get_pos()
                    # row, col = get_new_position_from_human(pos)
                    # game.select(row, col)
                gptBoard = game.board.capture_board_to_gpt()
                gptBoard_str = repr(gptBoard)
                out = gptPlayer.send_question(gptBoard_str)
                answer = gptPlayer.get_answer(out)
                print(answer)
                # game.select(answer[0], answer[1])
                # print("dark turn end")
                
        game.update()
     




    pygame.quit()


main()

# board =" [[(0, 1), 'L', 'N'], [(0, 3), 'L', 'N'], [(0, 5), 'L', 'N'], [(0, 7), 'L', 'N'], [(1, 0), 'L', 'N'], [(1, 2), 'L', 'N'], [(1, 4), 'L', 'N'], [(1, 6), 'L', 'N'], [(2, 1), 'L', 'N'], [(2, 3), 'L', 'N'], [(2, 5), 'L', 'N'], [(2, 7), 'L', 'N'], [(5, 0), 'D', 'N'], [(5, 2), 'D', 'N'], [(5, 4), 'D', 'N'], [(5, 6), 'D', 'N'], [(6, 1), 'D', 'N'], [(6, 3), 'D', 'N'], [(6, 5), 'D', 'N'], [(6, 7), 'D', 'N'], [(7, 0), 'D', 'N'], [(7, 2), 'D', 'N'], [(7, 4), 'D', 'N'], [(7, 6), 'D', 'N']]"
    
# player = GPTPlayer()
# output = player.send_question(board)


# # answer = player.get_answer(output)
