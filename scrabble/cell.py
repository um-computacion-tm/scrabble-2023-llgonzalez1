from scrabble.models import Tile

class Cell:
    def __init__(self, letter, multiplier=1, multiplier_type= None):
        self.letter = letter
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
              
    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
