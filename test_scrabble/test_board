import unittest
from scrabble.board import Board
from scrabble.Tile import *
from scrabble.cell import *

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    
    def test_word_inside_board(self):
        board = Board()
        word = "FACULTAD"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        
        assert word_is_valid == True
    
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "FACULTAD"
        location = (5, 4)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        
        assert word_is_valid == True

    def test_word_out_of_board(self):
        board = Board()
        word = "FACULTAD"
        location = (4, 14)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False
        
    def test_word_out_of_board_vertical(self):
        board = Board()
        word = "FACULTAD"
        location = (9, 8)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        
        self.assertEqual(
            word_is_valid,
            False,
        )
        
         
    def test_board_is_empty(self):
        board = Board()
        board.empty()
        assert board.is_empty == True
         
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(tile('C', 1))
        board.empty()
        assert board.is_empty == False
        

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "FACULTAD"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "FACULTAD"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
      
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "FACULTAD"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "FACULTAD"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
        
    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(tile('C', 1))
        board.grid[8][7].add_letter(tile('A', 1)) 
        board.grid[9][7].add_letter(tile('S', 1)) 
        board.grid[10][7].add_letter(tile('A', 1)) 
        word = "FACULTAD"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_not_empty_board_horizontal_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(tile('C', 1))
        board.grid[8][7].add_letter(tile('A', 1)) 
        board.grid[9][7].add_letter(tile('S', 1)) 
        board.grid[10][7].add_letter(tile('A', 1)) 
        word = "MISA"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
        
    def test_place_word_not_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(tile('C', 1))
        board.grid[7][8].add_letter(tile('A', 1)) 
        board.grid[7][9].add_letter(tile('S', 1)) 
        board.grid[7][10].add_letter(tile('A', 1)) 
        word = "Facultad"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_not_empty_board_vertical_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(tile('C', 1))
        board.grid[7][8].add_letter(tile('A', 1)) 
        board.grid[7][9].add_letter(tile('S', 1)) 
        board.grid[7][10].add_letter(tile('A', 1)) 
        word = "MISA"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False

    def test_x3_multiplier_cell(self):
        board = Board()
        board.add_multiplier()
        multiplier = board.grid[0][0].multiplier
        self.assertEqual(multiplier, 3)
        
    def test_word_multiplier_cell(self):
        board = Board()
        board.add_multiplier()
        multiplier_type = board.grid[0][0].multiplier_type
        self.assertEqual(multiplier_type, "W")
    
if __name__ == '__main__':
    unittest.main()
