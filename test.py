import unittest
import checkWins
import printBoard
from checkWins import checkWins
from checkWins import inputActions
from printBoard import Board
from printBoard import *

class TestGameInputActions(unittest.TestCase):
    
    def test_playerSelectInvalid(self):
        testObj = inputActions
        testObj.player_select('A')
        self.assertEqual(testObj.valid, False)
        
    def test_playerSelectValid(self):
        testObj = inputActions
        testObj.player_select('B')
        self.assertEqual(testObj.valid, True)
        
    def test_columnSelectFull(self):
        testBoard = [['X',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ']]
        testObj = inputActions
        Board.board = testBoard
        testObj.column_select(1)
        self.assertEqual(testObj.cValid, False)
        
    def test_columnSelectValid(self):
        testBoard = [['X',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' '],['O',' ',' ',' ',' ',' '],['X',' ',' ',' ',' ',' ']]
        testObj = inputActions
        Board.board = testBoard
        testObj.column_select(3)
        self.assertEqual(testObj.cValid, False)
        
    def test_columnSelectInvalid(self):
        testObj = inputActions
        testObj.column_select(10)
        self.assertEqual(testObj.cValid, False)
        
    def test_dropPiece(self):
        testBoard = [['X','X',' ','O',' ',' '],[' ','O',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
        testObj = inputActions
        Board.board = testBoard
        testObj.drop_piece('X', 2)
        self.assertEqual(testObj.dropped, True)
        
    def test_printBoard(self):
        testBoard = [[' ',' ',' ',' ',' ','X'],[' ',' ',' ',' ','O','X'],[' ',' ',' ',' ',' ','O'],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ','X'],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
        Board.board = testBoard
        print_board()
        self.assertEqual(printBoard.printed, True)
        
        
class TestWinCases(unittest.TestCase):
    
    def test_winVertical(self):
        testBoard = [['X','X',' ','O',' ',' '],['X','O',' ',' ',' ',' '],['X',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
        testObj = checkWins
        Board.board = testBoard
        testObj.win_vertical('X', 1)
        self.assertEqual(testObj.vMatch, True)
        
    def test_winDiagonal(self):
        testBoard = [['X','X','O','O',' ',' '],['O','X','O','X',' ',' '],['X','O','X','X',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ']]
        testObj = checkWins
        Board.board = testBoard
        testObj.win_diagonal('X', 3)
        self.assertEqual(testObj.dMatch, True)
        
    def test_winHorizontal(self):
        testBoard = [['X','X','X',' ',' ',' '],['X','X','X',' ',' ',' '],['X','X','X',' ',' ',' '],['X','X','X',' ',' ',' '],['X','X','X',' ',' ',' '],['X','X','X',' ',' ',' '],['X','X','X',' ',' ',' ']]
        testObj = checkWins
        Board.board = testBoard
        testObj.win_horizontal('X', 3)
        self.assertEqual(testObj.hMatch, True)
        
        
if __name__ == '__main__':
    unittest.main()