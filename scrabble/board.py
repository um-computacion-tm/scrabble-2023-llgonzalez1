from scrabble.cell import Cell
from scrabble.Tile import *

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '', None, True) for _ in range(15) ] 
            for _ in range(15)
        ]
        self.is_empty = None
        
    def print_board(self):
        print('  ', end='')  
        for col_num in range(15):
            print(f'{col_num:4}', end=' ')
        print()  

        for row_num, row in enumerate(self.grid):
            print(f'{row_num:2} ', end='')   
            for cell in row:
                print(cell, end=' ')
            print()    

    
    def validate_word_inside_board(self, word, location, orientation):
        self.word = word.upper()
        self.orientation = orientation
        self.position_row = location[0]
        self.position_col = location[1] 
        if orientation == 'H' and len(self.word)<=15-self.position_col:
            return True
        elif orientation == 'V' and len(self.word)<=15-self.position_row:
            return True
        else:
            return False
        
        
    def empty(self):
        if self.grid[7][7].letter == None:
            self.is_empty = True
        else:
            self.is_empty = False
            
    def validate_word_place_board(self, word, location, orientation):
        self.word = word.upper()
        valid = self.validate_word_inside_board(word, location, orientation)
        self.empty()
        if self.is_empty == False:
            if valid == True:
                if orientation == "H":
                    for i in self.word:
                        index = self.position_col
                        if self.grid[self.position_row][index].letter is not None:
                            if i != self.grid[self.position_row][index].letter.letter:
                                return False
                        self.position_col += 1
                    return True
                else:
                    for i in self.word:
                        index = self.position_row
                        if self.grid[index][self.position_col].letter is not None:
                            if i != self.grid[index][self.position_col].letter.letter:    
                                return False
                        self.position_row += 1
                    return True
        else:
            if valid == True:
                for i in self.word:
                    if orientation == "H":
                        index = self.position_col
                        if self.position_row == 7 and index == 7:
                            return True
                        self.position_col += 1 
                    else:
                        index = self.position_row
                        if self.position_col == 7 and index == 7:
                            return True
                        self.position_row += 1 
                return False
    
    def add_multiplier(self):
        x3_word = [
            (0,0),(7,0),(14,0),(0,7),(14,7),(0,14),(7,14),(14,14)
            ]
    
        x2_word = [(1,1),(2,2),(3,3),(4,4),(10,10),(11,11),(12,12),
            (13,13),(1,13),(2,12),(13,11),
            (4,10),(7,7),(13,1),(12,2),(11,3),(10,4)
               ]
    
        x3_letter = [(1,5),(1,9),(5,1),(5,5),(5,9),(5,13),
            (9,1),(9,5),(9,9),(9,13),(13,5),(13,9)
                ]
        x2_letter = [
            (0,3),(0,11),(2,6),(2,8),
            (3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),
            (7,3),(7,11),(8,2),(8,6),(8,8),(8,12),
            (11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11)
                ]
        for position in x3_word:     
            self.grid[position[0]][position[1]].multiplier = 3
            self.grid[position[0]][position[1]].multiplier_type = "W"
            
        for position in x2_word:     
            self.grid[position[0]][position[1]].multiplier = 2
            self.grid[position[0]][position[1]].multiplier_type = "W"
            
        for position in x3_letter:     
            self.grid[position[0]][position[1]].multiplier = 3
            self.grid[position[0]][position[1]].multiplier_type = "L"
        
        for position in x2_letter:     
            self.grid[position[0]][position[1]].multiplier = 2
            self.grid[position[0]][position[1]].multiplier_type = "L"
    
