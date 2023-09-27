from scrabble.cell import Cell
class calulate_word_value:
    
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