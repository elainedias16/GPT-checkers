import pygame
from checkers.constants import WIDTH, HEIGHT, LIGHT, SQUARE_SIZE
from checkers.board import Board

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
    board = Board()
    board.show_board()

    # piece = board.get_piece(0, 1)
    # board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # pos = pygame.mouse.get_pos()
                # row, col = get_new_position_from_human(pos)
                # piece = board.get_piece(row, col)
                # board.move(piece, 4, 3)
    
        board.draw(WIN)
        pygame.display.update()


    pygame.quit()


main()