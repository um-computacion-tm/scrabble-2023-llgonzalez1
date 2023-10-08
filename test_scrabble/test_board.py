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


######
    def test_validate_word_inside_board_horizontal(self):
            board = Board()
            word = "HELLO"
            location = (0, 5)
            orientation = "H"

            is_valid = board.validate_word_inside_board(word, location, orientation)

            self.assertTrue(is_valid)

    def test_validate_word_inside_board_vertical(self):
        board = Board()
        word = "WORLD"
        location = (5, 0)
        orientation = "V"

        is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(is_valid)

    def test_validate_word_outside_board_horizontal(self):
        board = Board()
        word = "OUTSIDE"
        location = (0, 10)
        orientation = "H"

        is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertFalse(is_valid)

    def test_validate_word_outside_board_vertical(self):
        board = Board()
        word = "VERTICAL"
        location = (10, 0)
        orientation = "V"

        is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertFalse(is_valid)

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
