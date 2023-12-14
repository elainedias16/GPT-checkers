import replicate
from .server_replicate import server_replicate


class GPTPlayer:
    def __init__(self):
        self.server_replicate = server_replicate()
        self.txt = "Hi, let's play checkers! I'm sending you a board for analysis. Please send me your best valid move."


    def send_question(self, board):
        question = self.txt + " The board is: " + board + " What is your move?"
        output = self.server_replicate.call_api(question)
        return output

    
    def get_answer(self, output_replicate):
        return self.server_replicate.get_answer(output_replicate)
    


# board =" [[(0, 1), 'L', 'N'], [(0, 3), 'L', 'N'], [(0, 5), 'L', 'N'], [(0, 7), 'L', 'N'], [(1, 0), 'L', 'N'], [(1, 2), 'L', 'N'], [(1, 4), 'L', 'N'], [(1, 6), 'L', 'N'], [(2, 1), 'L', 'N'], [(2, 3), 'L', 'N'], [(2, 5), 'L', 'N'], [(2, 7), 'L', 'N'], [(5, 0), 'D', 'N'], [(5, 2), 'D', 'N'], [(5, 4), 'D', 'N'], [(5, 6), 'D', 'N'], [(6, 1), 'D', 'N'], [(6, 3), 'D', 'N'], [(6, 5), 'D', 'N'], [(6, 7), 'D', 'N'], [(7, 0), 'D', 'N'], [(7, 2), 'D', 'N'], [(7, 4), 'D', 'N'], [(7, 6), 'D', 'N']]"
    
# player = GPTPlayer()
# output = player.send_question(board)


# answer = player.get_answer(output)