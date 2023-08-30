from scrabble.cell import Cell
from scrabble.models import Tile

def calculate_word_value(word):
    cell = Cell(letter=Tile('C', 1))
    value = 0
    for cell in word:
        return value