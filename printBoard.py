printed = False
class Board:

    board = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]

def print_board():
    # numbered header
    header = ' '
    for num in range(len(Board.board)):
        header += ' ' + str(num+1) + '  '
    print(header)
    # print the board
    for row in range(len(Board.board[0])):
        print('+---' * (len(Board.board)) + '+')
        Board.board_row = ''
        for col in range(len(Board.board)):
            Board.board_row += '| ' + Board.board[col][row] + ' '
        print(Board.board_row + '|')
    print('+---' * (len(Board.board)) + '+')
    print('\n')

printed = True
    
def find_row(piece, column):
    row = 0
    for i in range(len(Board.board[0])):
        if Board.board[column-1][i] == piece:
            row = i
            break
    return row