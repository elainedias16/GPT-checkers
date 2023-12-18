import time
import pygame
from checkers.constants import NUM_CHANCES, WIDTH, HEIGHT, LIGHT, SQUARE_SIZE, DARK, GREY, GREEN, SCREEN_FINAL_GAME, BROWN
from checkers.board import Board
from checkers.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH , HEIGHT))


pygame.display.set_caption('Checkers')



def msg_winner(winner):
    font = pygame.font.Font(None, 80)
    victory_text = font.render(winner + ' WINS!!!!', True, LIGHT) 
    text_rect = victory_text.get_rect(center=(WIDTH// 2, HEIGHT // 2))
    WIN.fill(SCREEN_FINAL_GAME)
    WIN.blit(victory_text, text_rect) 
    pygame.display.set_caption('***********************************  ' + winner + ' WINS   ********************************')
    pygame.display.flip()
    time.sleep(5)


def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
 
    answer = game.gpt_player.send_first_question()
    out = game.gpt_player.get_answer(answer)
    print("---------first answer----------")
    print(str(out))
    count = 0
    pygame.font.init()

    
    while run:
        clock.tick(FPS)

        # game.board.set_dark_left(0)
        if (game.winner() != None):
            winner = game.winner()
            msg_winner(winner)
            run = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            turn = game.get_turn()
            print("Turn: ", game.get_turn())
            pygame.display.set_caption('*********************************   TURN:  ' + str(turn) + '   ********************************')

            if game.turn == LIGHT:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = game.get_new_position_from_human(pos)
                    game.select(row, col)
                count = 0
            elif game.turn == DARK:
                game.ai_make_move(count)
                count += 1
              

       
                
        game.update()
     

    pygame.quit()


main()

