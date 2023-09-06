from scrabble.cell import Cell
from scrabble.models import Tile
class calulate_word_value:
    
    def calculate_word_value(word):
        total_value = 0
        for cell in word:
            total_value += cell.calculate_value()
        return total_value
