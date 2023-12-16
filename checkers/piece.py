
from .constants import DARK,LIGHT, SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.queen =  False

        # if self.color == DARK:
        #     self.direction = -1   # Dark pieces move up, so they decrease in numbers on pygame board
        # else:    
        #     self.direction = 1    # Light pieces move down, so they increase in numbers on pygame board

        self.x = 0
        self.y = 0
        self.calc_pos()


    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2



    def make_queen(self):
        self.queen = True
        

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.OUTLINE)
        if self.queen:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2 ))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


    def __repr__(self):
        return str(self.color)
    

    def show_piece_to_gpt(self):
        return self.row, self.col, self.color, self.queen
        



## LIGHT PIECES ARE AT THE TOP OF THE BOARD
## DARK PIECES ARE AT THE BOTTOM OF THE BOARD
## PYGAME BOARD 

# 00


# 800




