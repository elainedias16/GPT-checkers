import sys 
sys.path.insert(1, '../server_replicate.py')
from server_replicate import server_replicate

class GPTPlayer:
    def __init__(self):
        self.server_replicate = server_replicate()
        self.txt = "Hi, let's play checkers! I'm sending you a board for analysis. D means dark, L means light, N means not queen and Y means queen. The first element of the tuple is the row and the second is the column."


    def send_question(self, board):
        print("entrei no send question")
        question = self.txt + " The board is: " + board + " You're playing as dark. Choose the row and column where you want to go."
        print('question')
        print(question)
        output = self.server_replicate.call_api(question)
        return output

    
    def get_answer(self, output_replicate):
        return self.server_replicate.get_answer(output_replicate)
    


# board =" [[(0, 1), 'L', 'N'], [(0, 3), 'L', 'N'], [(0, 5), 'L', 'N'], [(0, 7), 'L', 'N'], [(1, 0), 'L', 'N'], [(1, 2), 'L', 'N'], [(1, 4), 'L', 'N'], [(1, 6), 'L', 'N'], [(2, 1), 'L', 'N'], [(2, 3), 'L', 'N'], [(2, 5), 'L', 'N'], [(2, 7), 'L', 'N'], [(5, 0), 'D', 'N'], [(5, 2), 'D', 'N'], [(5, 4), 'D', 'N'], [(5, 6), 'D', 'N'], [(6, 1), 'D', 'N'], [(6, 3), 'D', 'N'], [(6, 5), 'D', 'N'], [(6, 7), 'D', 'N'], [(7, 0), 'D', 'N'], [(7, 2), 'D', 'N'], [(7, 4), 'D', 'N'], [(7, 6), 'D', 'N']]"
    
# player = GPTPlayer()
# output = player.send_question(board)


# answer = player.get_answer(output)
