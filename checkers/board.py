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

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        # if row == ROWS or row == 0:  #if pieces achieves the the first or the last rows it becomes a queen
        if row == ROWS - 1 or row == 0:  #if pieces achieves the the first or the last rows it becomes a queen
            piece.make_queen()
            if piece.color == LIGHT:
                self.light_queens += 1
            else:
                self.dark_queens += 1

    def get_piece(self, row, col):
        return self.board[row][col]
    
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

    
    def show_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece_str = "Piece: ({}, {}) - Color: {} - Queen: {}".format(
                        row, col, "Light" if piece.color == LIGHT else "Dark", "Yes" if piece.queen else "No"
                    )
                    print(piece_str)
                else:
                    print("No piece at ({}, {})".format(row, col))
            print("\n")


    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == DARK or piece.queen: 
            #row -1 :  if is DARK, is moving up, do row-1
            #max(row-3, -1) :  how much of rows we gonna lock, we gonna until 2 rows of where we are, -3 is because we start at -1. The other -1 is to move up
            #left is where we gonna start for our columnand what we are gonna subtract
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))
        
        if piece.color == LIGHT or piece.queen:
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))

        return moves 

  
    
    #step says if we go up or down
    #skipped is a list of pieces that we have skipped
    #left where we starting in therms to the column when we tranversiong to the left
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0: #we find an empty square
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped #we have to add the last piece we found and the skipped pieces
                     
                else:
                    moves[(r, left)] = last

                if last: #we have something to skip over, so we have to check if we can do dobble jump or triple...
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color: #has a piece of the same color
                break  # we can't jump over it
            else:
                last = [current]  


            left -= 1

        return moves
            
    
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0: #we find an empty square
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped #we have to add the last piece we found and the skipped pieces
                     
                else:
                    moves[(r, right)] = last

                if last: #we have something to skip over, so we have to check if we can do dobble jump or triple...
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color: #has a piece of the same color
                break  # we can't jump over it
            else:
                last = [current]  


            right += 1

        return moves



    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0 :
                if piece.color == DARK:
                    self.dark_left -= 1
                else :
                    self.light_left -= 1


    def winner(self):
        if self.dark_left <= 0:
            return "LIGHT"
        elif self.light_left <= 0:
            return "DARK"
        else :
            return None




    # def get_valid_moves(self, piece):
    #     moves = {}
    #     left = piece.col - 1
    #     right = piece.col + 1
    #     row = piece.row

    #     if piece.color == DARK:
    #         if piece.queen:
    #             moves.update(self._traverse_all_left(row, -1, piece.color, left))
    #             moves.update(self._traverse_all_right(row, -1, piece.color, right))
    #         else:
    #             moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
    #             moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

    #     if piece.color == LIGHT:
    #         if piece.queen:
    #             moves.update(self._traverse_all_left(row, 1, piece.color, left))
    #             moves.update(self._traverse_all_right(row, 1, piece.color, right))
    #         else:
    #             moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
    #             moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

    #     return moves

    # def _traverse_all_left(self, start, step, color, left, skipped=[]):
    #     moves = {}
    #     last = []
    #     for r in range(start, -1 if step == -1 else COLS, step):
    #         if left < 0:
    #             break
            
    #         current = self.board[r][left]
    #         if current == 0:
    #             if skipped and not last:
    #                 break
    #             elif skipped:
    #                 moves[(r, left)] = last + skipped
    #             else:
    #                 moves[(r, left)] = last
                
    #             if last:
    #                 moves.update(self._traverse_all_left(r + step, step, color, left - 1, skipped=last))
    #                 moves.update(self._traverse_all_right(r + step, step, color, left + 1, skipped=last))
    #             break
    #         elif current.color == color:
    #             break
    #         else:
    #             last = [current]

    #         left -= 1
        
    #     return moves

    # def _traverse_all_right(self, start, step, color, right, skipped=[]):
    #     moves = {}
    #     last = []
    #     for r in range(start, -1 if step == -1 else COLS, step):
    #         if right >= COLS:
    #             break
            
    #         current = self.board[r][right]
    #         if current == 0:
    #             if skipped and not last:
    #                 break
    #             elif skipped:
    #                 moves[(r, right)] = last + skipped
    #             else:
    #                 moves[(r, right)] = last
                
    #             if last:
    #                 moves.update(self._traverse_all_left(r + step, step, color, right - 1, skipped=last))
    #                 moves.update(self._traverse_all_right(r + step, step, color, right + 1, skipped=last))
    #             break
    #         elif current.color == color:
    #             break
    #         else:
    #             last = [current]

    #         right += 1
        
    #     return moves

    
   


        # (4,4) : [(3,3)] #if we got go square 4,4 (valid move), we have to remove piece 3,3, cause we capture it


 