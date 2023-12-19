import random
import time
import pygame
from checkers.constants import HEIGHT, LIGHT, DARK, SCREEN_FINAL_GAME, SQUARE_SIZE, GREY, GREEN, ROWS, COLS, NUM_CHANCES, WIDTH
from checkers.board import Board
from checkers.gpt_player import GPTPlayer

class Game:
    def __init__(self, win):
        self._init()
        self.win = win


    def winner(self):
        return self.board.winner()
    
    def set_winner(self, winner):
        self.winner = winner


    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()



    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = LIGHT 
        self.valid_moves = {}
        self.gpt_player = GPTPlayer()


    def reset(self):
        self._init()

    def get_turn(self):
        if self.turn == LIGHT:
            return "LIGHT"
        else:
            return "DARK"


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
            result = self._move(row, col) # if the move is valid, then the piece will move
            if not result:  # if the move is not valid
               
                if self.turn == LIGHT:
                    self.selected = None
                    self.select(row, col)
                elif self.turn == DARK:
                    print('to no select do dark')
                    self.ai_make_move(0, False)


              
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  #The selection was valid

        return False
    
        
    

    #Example of gpt_moves, is array of dictionaries:
    #[{(2, 1, 'N'): [(3, 0), (3, 2)]}, {(2, 3, 'N'): [( 3, 2), (3, 4)]}, {(2, 5, 'N'): [(3, 4), (3, 6)]}, {(2, 7, 'N'): [(3, 6)]}]
    #GPT has already chosen the move, so we just need to click on the piece and make the move."
    def ai_move(self, row, col, piece_row, piece_col, is_queen, gpt_moves):
        self.selected = None #clean the selection first
        self.select(piece_row, piece_col)      
        self.select(row, col)    

                    
    def ai_move_random(self, gpt_moves):
        dict_choice = random.choice(gpt_moves)  #choose a random dictionary    
        moves_list = []
        for moves in dict_choice.values():
            moves_list.append(moves)

        moves_list = moves_list[0]
        move = random.choice(moves_list)  #choose a random move in array os valid moves in the dictionary
        row, col = move

        #Capture the piece to send to select
        key = dict_choice.keys()
        key = (list(key))[0]
        piece_row, piece_col, is_queen = key

        self.selected = None
        self.select(piece_row, piece_col)  #click on the piece  
        self.select(row, col)   #make the move

  
            
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



    def ai_make_move(self, count, is_main=True):
        gpt_board = self.board.capture_board_to_gpt()
        gpt_board_str = repr(gpt_board)
        gpt_moves = self.board.gpt_valid_moves()
        gpt_moves_str = repr(gpt_moves)
        out = self.gpt_player.send_question(gpt_board_str, gpt_moves_str) #false means that the move is not valid
        answer = self.gpt_player.get_answer(out)
        print("---------GPt answer----------")
        print(str(answer))
        row, col, piece_row, piece_col, is_queen = self.gpt_player.send_gpt_answer_to_game(str(answer))
  
        if(is_main):
            print("count: ", count)
            if(count+1 < NUM_CHANCES):
                self.ai_move(row, col, piece_row, piece_col, is_queen, gpt_moves)
                # count += 1
            else:
                print("I was wrong more than 3x")
                self.ai_move_random(gpt_moves)
        else:
            print("count: ", count)
            self.ai_move(row, col, piece_row, piece_col, is_queen, gpt_moves)
            

    def get_new_position_from_human(self,pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

       

 
        

 