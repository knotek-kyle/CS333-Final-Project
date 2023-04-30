# 7x6 board
board = [[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]

def print_board():
    # numbered header
    header = ' '
    for num in range(len(board)):
        header += ' ' + str(num+1) + '  '
    print(header)
    # print the board
    for row in range(len(board[0])):
        print('+---' * (len(board)) + '+')
        board_row = ''
        for col in range(len(board)):
            board_row += '| ' + board[col][row] + ' '
        print(board_row + '|')
    print('+---' * (len(board)) + '+')
    print('\n')

def player_select():
    valid = False
    while valid == False:
        player_1 = input('Choose your piece - O or X: ').upper()
        # piece validation
        if player_1 != 'O' and player_1 != 'X':
            print('Invalid piece. Select \'O\' or \'X\'.')
        else:
            valid = True
        if player_1 == 'O':
            player_2 = 'X'
        else:
            player_2 = 'O'
    return player_1, player_2

def column_select():
    valid = False
    while valid == False:
        try:
            column = int(input('Choose a column from 1 to 7: '))
        except:
            print('Invalid column.')
        if column > len(board) or column <= 0:
            print('The selected column is not on the board. Please select a column from 1 to 7.')
        elif board[column-1][0] != ' ':
            print('Column is full.')
        else:
            valid = True
    return column

def drop_piece(piece, column):
    dropped = False
    for row in reversed(range(len(board[0]))):
        if board[column-1][row] == ' ':
            board[column-1][row] = piece
            dropped = True
            break
    return dropped

def find_row(piece, column):
    row = 0
    for i in range(len(board[0])):
        if board[column-1][i] == piece:
            row = i
            break
    return row

def win_vertical(piece, column):
    row = find_row(piece, column)
    match = False
    for i in range(1,4):
        if row+i >= len(board[0]) or board[column-1][row+i] != piece:
            match = False
            break
        else:
            match = True
    return match

def win_diagonal(piece, column):
    row = find_row(piece, column)
    match_left = False
    match_right = False
    for i in range(1,4):
        #diagonal to the left
        if column-1-i < 0 or row+i >= len(board[0]) or board[column-1-i][row+i] != piece:
            match_left = False
            break
        else:
            match_left = True
    for i in range(1,4):
        #diagonal to the right
        if column-1+i >= len(board) or row+i >= len(board[0]) or board[column-1+i][row+i] != piece:
            match_right = False
            break
        else:
            match_right = True
    if match_left == True or match_right == True:
        return True
    return match_left

def win_horizontal(piece, column):
    row = find_row(piece, column)
    count = 0
    match = False
    for i in range(len(board)):
        if board[0+i][row] == piece:
            count += 1
        else:
            count = 0
        if count == 4:
            match =  True
            break
    return match

# Initial board print
print('\nConnect Four \n')
print_board()
game_over = False
round_count = 0
player_1,player_2 = player_select()

# gameplay
while game_over == False:
    round_count  += 1
    if round_count == 43:
        game_over = True
        print('GAME OVER! It is a tie :(')
        break
    print('Round: ', round_count)
    # player turn
    if round_count % 2 != 0:
        piece = player_1
    else:
        piece = player_2
    # get column from player
    column = column_select()
    drop_piece(piece, column)
    print('Piece dropped on column {col}, row {row}.'.format(col = column, row = find_row(piece, column)+1))
    print_board()
    # win check
    if win_vertical(piece, column) == True or win_diagonal(piece, column) == True or win_horizontal(piece, column) == True:
        game_over = True
        print('Congratulations Player {piece}! You WON!'.format(piece=piece))