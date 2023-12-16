import pygame
from checkers.constants import LIGHT, DARK, SQUARE_SIZE, GREY, GREEN, ROWS, COLS
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

    def get_turn(self):
        return self.turn


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves: #if we selected and we clicked in an empty square and the click is in the valid moves
            print("selected: ", self.selected)
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()

        else:
            return False

        return True


    def select(self, row, col):
        print('entrei no select')
        if self.selected:
            print("self.selected: ", self.selected)
            result = self._move(row, col) # if the move is valid, then the piece will move
            if not result:  # if the move is not valid
                self.selected = None
                self.select(row, col)
        

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  #The selection was valid
        
        return False
    
    
    #[{(2, 1, 'N'): [(3, 0), (3, 2)]}, {(2, 3, 'N'): [(3, 2), (3, 4)]}, {(2, 5, 'N'): [(3, 4), (3, 6)]}, {(2, 7, 'N'): [(3, 6)]}]
    def ai_move(self, row, col, piece_row, piece_col, is_queen, gpt_moves):
        for dict in gpt_moves:
            for key, value in dict.items():
                if key == (piece_row, piece_col, is_queen):
                    for tupla in value:
                        if row == tupla[0] and col == tupla[1]:
                            self.selected = self.board.get_piece(piece_row, piece_col)
                            # print("selected gpttt: ", self.selected)
                            self.board.move(self.board.get_piece(piece_row, piece_col), row, col)
                            # self.select(row, col)
                            # print("self.selected :  ", self.select(row, col))
                            # self._move(row, col)
                            print("me mexiiiiiiiiiiiiiiiiiii")
                            break
        #piece = self.board.get_piece(piece_row, piece_col)
        # self.board.move(piece, row, col)

        # Separação entre os dicionários
        #     for key in move:
        #         print("key: ", key)
                # if key == (piece_row, piece_col, is_queen):
                #     for move in move[key]:
                #         if move == (row, col):
                #             self.board.move(self.board.get_piece(piece_row, piece_col), row, col)
                #             skipped = self.board.get_skipped(piece_row, piece_col, row, col)
                #             if skipped:
                #                 self.board.remove(skipped)
                #             self.change_turn()
                #             return True
       



    
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



    

        