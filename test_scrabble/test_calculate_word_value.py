import unittest
from scrabble.cell import Cell, calculate_word_value
from scrabble.models import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        
        word = [
            Cell(multiplier=1, multiplier_type='', letter=Tile('C', 1), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('S', 2), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
        ]
        values = calculate_word_value(word)
        self.assertEqual(values.calculate_word(), 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(multiplier=1, multiplier_type='', letter=Tile('C', 1), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
            Cell(multiplier=2, multiplier_type='L',letter=Tile('S', 2), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
        ]
        values = calculate_word_value(word)
        self.assertEqual(values.calculate_word(), 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(multiplier=1, multiplier_type='', letter=Tile('C', 1), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
            Cell(multiplier=2, multiplier_type='W',letter=Tile('S', 2), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
        ]
        values = calculate_word_value(word)
        self.assertEqual(values.calculate_word(), 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(multiplier=3, multiplier_type='L', letter=Tile('C', 1), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
            Cell(multiplier=2, multiplier_type='W',letter=Tile('S', 2), active=True),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
        ]
        values = calculate_word_value(word)
        self.assertEqual(values.calculate_word(), 14)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(multiplier=3, multiplier_type='L', letter=Tile('C', 1), active=False),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
            Cell(multiplier=2, multiplier_type='W',letter=Tile('S', 2), active=False),
            Cell(multiplier=1, multiplier_type='',letter=Tile('A', 1), active=True),
        ]
        values = calculate_word_value(word)
        self.assertEqual(values.calculate_word(), 5)


if __name__ == '__main__':
    unittest.main()