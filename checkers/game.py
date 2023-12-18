import random
import pygame
from checkers.constants import LIGHT, DARK, SQUARE_SIZE, GREY, GREEN, ROWS, COLS, NUM_CHANCES
from checkers.board import Board
from checkers.gpt_player import GPTPlayer

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
        self.gpt_player = GPTPlayer()


    def reset(self):
        self._init()

    def get_turn(self):
        if self.turn == LIGHT:
            return "LIGHT"
        else:
            return "DARK"
        # return self.turn


    def _move(self, row, col):
        piece = self.board.get_piece(row, col)

        if self.selected and piece == 0 and (row, col) in self.valid_moves: #if we selected and we clicked in an empty square and the click is in the valid moves
            #print("selected: ", self.selected)
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()


        else:
            return False

        return True


    # def select(self, row, col):
    #     if self.selected:
    #         result = self._move(row, col) # if the move is valid, then the piece will move
    #         if not result:  # if the move is not valid
    #             self.selected = None
    #             self.select(row, col)
        

    #     piece = self.board.get_piece(row, col)
    #     if piece != 0 and piece.color == self.turn:
    #         self.selected = piece
    #         self.valid_moves = self.board.get_valid_moves(piece)
    #         return True  #The selection was valid
    
    #     return False

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col) # if the move is valid, then the piece will move
            if not result:  # if the move is not valid
               
                if self.turn == LIGHT:
                    print("entrei no if light")
                    self.selected = None
                    self.select(row, col)
                elif self.turn == DARK:
                    gpt_board = self.board.capture_board_to_gpt()
                    gpt_board_str = repr(gpt_board)
                    gpt_moves = self.board.gpt_valid_moves()
                    gpt_moves_str = repr(gpt_moves)
                    out = self.gpt_player.send_question(gpt_board_str, gpt_moves_str) #false means that the move is not valid
                    answer = self.gpt_player.get_answer(out)
                    print("----answer no else----------")
                    print(str(answer))
                    row, col, piece_row, piece_col, is_queen = self.gpt_player.send_gpt_answer_to_game(str(answer))
                    self.ai_move(row, col, piece_row, piece_col, is_queen, gpt_moves)
                     
              
                    
        

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  #The selection was valid

        return False
    
        
    

    # Quando chama self.select ele analisa o valid_moves, porém ele é vazio, além de que já conferimos se ele é valid, ent podemos só chamar a move
    
    #[{(2, 1, 'N'): [(3, 0), (3, 2)]}, {(2, 3, 'N'): [( 3, 2), (3, 4)]}, {(2, 5, 'N'): [(3, 4), (3, 6)]}, {(2, 7, 'N'): [(3, 6)]}]
    def ai_move(self, row, col, piece_row, piece_col, is_queen, gpt_moves):
        self.selected = None
        self.select(piece_row, piece_col)      
        self.select(row, col)                     
        # for dict in gpt_moves:
        #     print("dict: ")
        #     print(dict)
        #     for key, value in dict.items():
        #         if key == (piece_row, piece_col, is_queen):
        #             for tupla in value:
        #                 if row == tupla[0] and col == tupla[1]:
        #                     self.selected = None
        #                     #self.selected = self.board.get_piece(piece_row, piece_col)
        #                     self.select(piece_row, piece_col)      
        #                     self.select(row, col)                     
        #                     break


    def ai_move_random(self, gpt_moves):
        #{(2, 1, 'N'): [(3, 0), (3, 2)]}
        dict_choice = random.choice(gpt_moves)
        print("dict_choice: ", dict_choice)
        
        moves_list = []

        for moves in dict_choice.values():
            moves_list.append(moves)
        #[( 3, 2), (3, 4)]
        moves_list = moves_list[0]
        print("moves_list: ", moves_list)
        move = random.choice(moves_list)
        print("moveeeeeeeee: ", move)
        row, col = move
        print("row, col: ", row, col)
       

        key = dict_choice.keys()
        key = (list(key))[0]
        print("key: ", key)
        piece_row, piece_col, is_queen = key
        print("piece_row, piece_col, is_queen: ", piece_row, piece_col, is_queen)

        self.selected = None
        self.select(piece_row, piece_col)    
        self.select(row, col)
  
        # items_list = list(dict_choice.items())
        # print("items_list: ", items_list)
        # if items_list:  # Verifica se a lista de itens não está vazia
        # # Escolhendo aleatoriamente um item (chave, valor) do dicionário selecionado
        #     move = random.choice(items_list)
        #     print("move: ", move)

        # for dict in gpt_moves:
        
        #     for key, value in dict.items():
        #         if key == (piece_row, piece_col, is_queen):
        #             for tupla in value:
        #                 if row == tupla[0] and col == tupla[1]:
        #                     self.selected = None
        #                     #self.selected = self.board.get_piece(piece_row, piece_col)
        #                     self.select(piece_row, piece_col)      
        #                     self.select(row, col)                     
        #                     break

       



    
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



    

        