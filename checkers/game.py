import pygame
from checkers.constants import LIGHT, DARK, SQUARE_SIZE, GREY, GREEN
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win


    def winner(self):
        return self.board.winner()


    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()



    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = LIGHT 
        self.valid_moves = {}


    def reset(self):
        self._init()


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves: #if we selected and we clicked in an empty square and the click is in the valid moves
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()

        else:
            return False

        return True


    def select(self, row, col):
        if self.selected:
            print("selected: ", self.selected)
            result = self._move(row, col) # if the move is valid, then the piece will move
            if not result:  # if the move is not valid
                self.selected = None
                self.select(row, col)
            print("result: ", result)
        

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  #The selection was valid
        
        return False
    
    

    def ai_move(self, row, col):
        result = self._move(row, col)
        if not result:
            print("AI move not valid")
            #self.ai_move(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  #The selection was valid
        
        return False
       



    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == DARK:
            self.turn = LIGHT
        else:
            self.turn = DARK


    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)