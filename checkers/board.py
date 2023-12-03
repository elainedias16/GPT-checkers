import pygame
from .constants import BROWN,LIGHT_BROWN, DARK, LIGHT, ROWS, COLS, SQUARE_SIZE
from .piece import Piece

class Board():
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.dark_left = self.light_left = 12
        self.dark_queens = self.light_queens = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, LIGHT_BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  # if the current column if we are on is divisible by 2, and if is that equal to the remainder of the current row + 1 divided by 2
                    if row < 3:
                        self.board[row].append(Piece(row, col, LIGHT))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, DARK))
                    else:
                        self.board[row].append(0)   # This square starts with no piece
                else:
                    self.board[row].append(0)   # This square starts with no piece


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

 