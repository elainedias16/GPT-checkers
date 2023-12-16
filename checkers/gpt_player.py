import re
import sys
sys.path.insert(1, '../server_replicate.py')
from server_replicate import server_replicate

class GPTPlayer:
    def __init__(self):
        self.server_replicate = server_replicate()
        self.rules = '''
        Hello,
        I propose a game of checkers between us. I will play with the light 
        pieces, and you will play with the dark pieces. Before we start, let me 
        outline the rules of checkers to ensure we are aligned:
            Objective: The aim is to capture all of your opponent's pieces.
            Board Setup: The game is played on an 8x8 with rows and columns ranging from 0 to 7 board, marked by 
        alternating dark and light squares. Each player begins with 12 pieces on
        the dark squares in the three rows closest to them. I will use the 
        light pieces, and you will use the dark pieces.
            Movement: Pieces move diagonally forward to an adjacent unoccupied 
        dark square.
            Capture: If an opponent's piece is diagonally adjacent and the next 
        space beyond it is vacant, you can jump over their piece, capturing it. 
        Sequential jumps are mandatory if possible.
            Queen Pieces: When a piece reaches the farthest row from its starting
        position, it is crowned a queen. Queen can move diagonally forward and 
        backward.
            Winning the Game: The game is won by capturing all of the opponent's
        pieces.
        The board from your perspective looks like this, where "D" represents 
        your dark pieces, "L" represents my light pieces.
            I will send you the board state for each move.
        '''
        self.txt = '''
        We're playing checkers and not chess.I'm playing as Light and you are playing as Dark. I'm sending you a board for analysis. 
        D means dark, L means light, N means not queen and Y means queen. 
        The first element of the tuple is the row and the second is the column. 
        Your answer should be "My move is "piece position(x1,y1,)" to "(x2,y2)"", nothing more.
        '''
        self.move_txt = '''
        I'm sending as well your possible moves in a array of dictionaries. 
        Each dictionary has a piece and its possible moves.
        The piece is the key and the value is an array of tuples. 
        Each tuple is a possible move. 
        Choose one piece and one of its moves.
        Answer with "My move is "piece position(x1,y1,)" to "(x2,y2)"", nothing more
        '''


    # def send_question(self, board):
    #     question = self.txt + "Board : " + board 
    #     output = self.server_replicate.call_api(question)
    #     return output
    def send_first_question(self):
        question = self.rules
        output = self.server_replicate.call_api(question)
        return output

        
    def send_question(self, board, moves):
        text = '''
        I'm sending as well your possible moves in a array of dictionaries. 
        Each dictionary has a piece and its possible moves.
        The piece is the key and the value is an array of tuples. 
        Each tuple is a possible move. 
        Choose one piece and one of its moves.
        Answer with "My move is "piece position" to "chosen move"", nothing more
        '''
        question = self.rules + "Board : " + board + text + "Moves : " + moves
        output = self.server_replicate.call_api(question)
        return output

    
    def get_answer(self, output_replicate):
        return self.server_replicate.get_answer(output_replicate)
    
    
    def send_gpt_answer_to_game(self, answer):
        numbers_and_char = re.findall(r'\d+|\b[NY]\b', answer)
        numbers = [int(num) for num in numbers_and_char if num.isdigit()]
        piece_row, piece_col = numbers[0:2]
        row, col = numbers[-2:]
        is_queen = ''.join(char for char in numbers_and_char if char in ['N', 'Y'])
        return row, col, piece_row, piece_col, is_queen
    


# board =" [[(0, 1), 'L', 'N'], [(0, 3), 'L', 'N'], [(0, 5), 'L', 'N'], [(0, 7), 'L', 'N'], [(1, 0), 'L', 'N'], [(1, 2), 'L', 'N'], [(1, 4), 'L', 'N'], [(1, 6), 'L', 'N'], [(2, 1), 'L', 'N'], [(2, 3), 'L', 'N'], [(2, 5), 'L', 'N'], [(2, 7), 'L', 'N'], [(5, 0), 'D', 'N'], [(5, 2), 'D', 'N'], [(5, 4), 'D', 'N'], [(5, 6), 'D', 'N'], [(6, 1), 'D', 'N'], [(6, 3), 'D', 'N'], [(6, 5), 'D', 'N'], [(6, 7), 'D', 'N'], [(7, 0), 'D', 'N'], [(7, 2), 'D', 'N'], [(7, 4), 'D', 'N'], [(7, 6), 'D', 'N']]"
    
# player = GPTPlayer()
# output = player.send_question(board)


# answer = player.get_answer(output)
