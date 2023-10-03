from Tile import tile

class Cell:
    def __init__(self, multiplier, multiplier_type, letter, active):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active
    
    def __repr__(self):
        if self.multiplier == 1:
            return f"[  ]"
        else:
            return f"[{self.multiplier} ]"

    def add_letter(self, letter:tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'L' and self.active == True:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
class calculate_word_value:
    def __init__(self,word):
        self.word = word
        
    def calculate_word(self):
        values = 0
        for cell in self.word:
            values += Cell.calculate_value()
        for cell in self.word:
            if Cell.multiplier_type == 'W' and Cell.active == True:
                values = values * Cell.multiplier

        return values
