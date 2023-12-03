import pygame

# Window Settings
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
# Board colors
BROWN = (139, 69, 19)            
LIGHT_BROWN = (222, 184, 135)
# Piece colors
DARK = (101, 67, 33)
LIGHT = (255, 235, 176)

GREY = (128, 128, 128)
# GREEN = (144, 238, 144)
GREEN = (34, 139, 34)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (44, 25))




