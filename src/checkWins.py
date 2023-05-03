from printBoard import Board
from printBoard import *

class checkWins:
    currentBoard = Board
    vMatch = False
    dMatch = False
    hMatch = False

    def win_vertical(piece, column):
        row = find_row(piece, column)
        match = False
        for i in range(1,4):
            if row+i >= len(Board.board[0]) or Board.board[column-1][row+i] != piece:
                match = False
                break
            else:
                match = True
                checkWins.vMatch = True
        return match

    def win_diagonal(piece, column):
        row = find_row(piece, column)
        match_left = False
        match_right = False
        for i in range(1,4):
            #diagonal to the left
            if column-1-i < 0 or row+i >= len(Board.board[0]) or Board.board[column-1-i][row+i] != piece:
                match_left = False
                break
            else:
                match_left = True
                checkWins.dMatch = True
        for i in range(1,4):
            #diagonal to the right
            if column-1+i >= len(Board.board) or row+i >= len(Board.board[0]) or Board.board[column-1+i][row+i] != piece:
                match_right = False
                break
            else:
                match_right = True
                checkWins.dMatch = True
        if match_left == True or match_right == True:
            return True
        return match_left

    def win_horizontal(piece, column):
        row = find_row(piece, column)
        count = 0
        match = False
        for i in range(len(Board.board)):
            if Board.board[0+i][row] == piece:
                count += 1
            else:
                count = 0
            if count == 4:
                match =  True
                checkWins.hMatch = True
                
                break
        return match
    
class inputActions:
    valid = False
    cValid = False
    dropped = False

    def player_select(player_1): 
        # piece validation
        if player_1 != 'O' and player_1 != 'X':
            print('Invalid piece. Select \'O\' or \'X\'.')
        else:
            inputActions.valid = True
        if player_1 == 'O':
            player_2 = 'X'
        else:
            player_2 = 'O'
        return player_1, player_2

    def column_select(column):

        if column > len(Board.board) or column <= 0:
            print('The selected column is not on the Board.board. Please select a column from 1 to 7.')
        elif Board.board[column-1][0] != ' ':
            print('Column is full.')
        else:
            inputActions.cValid = True
            return column

    def drop_piece(piece, column):
        for row in reversed(range(len(Board.board[0]))):
            if Board.board[column-1][row] == ' ':
                Board.board[column-1][row] = piece
                inputActions.dropped = True
                break
        return inputActions.dropped