import random

class Tile:
    def __init__(self, letter=None, value=None):
        self.letter = letter
        self.value = value
    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.letter == other.letter and self.value == other.value
        return False
    def __repr__(self):
        return f"Tile(letter='{self.letter}', value={self.value})"
    def get_value(self):
        return self.value
    def get_letter(self):
        return self.letter


    LETTERS = {'A': [1, 12],
               'E': [1, 12],
               'O': [1, 9],
               'I': [1, 6],
               'S': [1, 6],
               'N': [1, 5],
               'L': [1, 4],
               'R': [1, 5],
               'U': [1, 5],
               'T': [1, 12],
               'D': [2, 5],
               'G': [2, 2],
               'C': [3, 4],
               'B': [3, 2],
               'M': [3, 2],
               'P': [3, 2],
               'H': [4, 2],
               'F': [4, 1],
               'V': [4, 1],
               'Y': [4, 1],
               'CH': [5, 1],
               'Q': [5, 1],
               'J': [6, 1],
               'LL': [6, 1],
               'Ñ': [6, 1],
               'RR': [6, 1],
               'X': [6, 1],
               'Z': [7, 1]}

class MasFichasdelopermitido(Exception):
    pass        
   
class Tilebag:
    def __init__(self):
        self.tiles = []
        for letter in Tile.LETTERS:
            tile = Tile(Tile.LETTERS, letter[0])
            for _ in range(letter[1]):
                self.tiles.append(tile)
        random.shuffle(self.tiles)

    def take(self, count):
        random.shuffle(self.tiles)
        tiles = []
        if count > len(self.tiles):
            raise MasFichasdelopermitido
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)