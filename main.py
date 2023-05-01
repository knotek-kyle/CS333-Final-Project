# 7x6 board
from checkWins import checkWins
from checkWins import inputActions
from printBoard import *
import sys

#Kyle Knotek - CS 333 Final Project

#Original connect 4 project from user "mrcosciug" Link: https://github.com/k2rbpz/codecademy-completed/blob/33b7a72dcbbd95020eafdfc1b950de9bb552c4ff/connect_four.py
#All unit and integration test were written by me. Connect 4 game is heavily edited to account for testing, automated gameplay test script, and more modularization.

Lines = []
if (len(sys.argv) == 2):
        inputFile = open(sys.argv[1], 'r')
        #Lines = inputFile.readlines()
        Lines = [line[:-1] for line in inputFile]
        print("Test script input: ", Lines)
        #print(Lines)
        inputFile.close()
        
# Initial board print
print('\nConnect Four \n')
print_board()
game_over = False
round_count = 0
if (len(sys.argv) == 2):
    while inputActions.valid == False:
        player = Lines[0]
        player_1,player_2 = inputActions.player_select(player)
else:
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
        if (len(sys.argv) == 2):
            try:
                inputColumn = int(Lines[round_count])
            except:
                print("Not a valid column.") 
        else:
            try:
                inputColumn = int(input('Choose a column from 1 to 7: '))
            except:
                print("Not a valid column.")
            
        column = inputActions.column_select(inputColumn)
        
    inputActions.drop_piece(piece, column)
    print('Piece dropped on column {col}, row {row}.'.format(col = column, row = find_row(piece, column)+1))
    print_board()
    # win check
    if checkWins.win_vertical(piece, column) == True or checkWins.win_diagonal(piece, column) == True or checkWins.win_horizontal(piece, column) == True:
        game_over = True
        print('Congratulations Player {piece}! You WON!'.format(piece=piece))