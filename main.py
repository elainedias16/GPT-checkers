import pygame
from checkers.constants import WIDTH, HEIGHT, LIGHT, SQUARE_SIZE, DARK, GREY, GREEN
from checkers.board import Board
from checkers.game import Game

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

    while run:
        clock.tick(FPS)

        if (game.winner() != None):
            # font = pygame.font.Font(None, 36)
            # winner = game.winner()
            print(game.winner())
            # winner_text = winner + " wins!"
            # text = font.render(winner_text, True, (255, 255, 255))  # Render the text
            # text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text on the screen
            # WIN.blit(text, text_rect)  # Draw the text on the screen
            # pygame.display.update()  # Update the display
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_new_position_from_human(pos)
                game.select(row, col)

    
        game.update()


    pygame.quit()


main()