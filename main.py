# 7x6 board
from checkWins import checkWins
from checkWins import inputActions
from printBoard import *

# Initial board print
print('\nConnect Four \n')
print_board()
game_over = False
round_count = 0
while inputActions.valid == False:
    player = input('Choose your piece - O or X: ').upper()
    player_1,player_2 = inputActions.player_select(player)

# gameplay
while game_over == False:
    inputActions.cValid = False
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
    while inputActions.cValid == False:
        try:
            inputColumn = int(input('Choose a column from 1 to 7: '))
        except:
            print("Not a valid column.")
        column = inputActions.column_select(inputColumn)
        print(inputColumn)
        
    inputActions.drop_piece(piece, column)
    print('Piece dropped on column {col}, row {row}.'.format(col = column, row = find_row(piece, column)+1))
    print_board()
    # win check
    if checkWins.win_vertical(piece, column) == True or checkWins.win_diagonal(piece, column) == True or checkWins.win_horizontal(piece, column) == True:
        game_over = True
        print('Congratulations Player {piece}! You WON!'.format(piece=piece))