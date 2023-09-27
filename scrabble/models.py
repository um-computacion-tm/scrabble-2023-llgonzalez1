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
class DrawingMoreThanAvaliable(Exception):
    pass        
class BagTiles:
    def __init__(self):
        self.letter = []
        self.letter.extend([Tile('E', 1) for _ in range(12)]),
        self.letter.extend([Tile('I', 1) for _ in range(6)]),
        self.letter.extend([Tile('L', 1) for _ in range(4)]),
        self.letter.extend([Tile('N', 1) for _ in range(5)]),
        self.letter.extend([Tile('O', 1) for _ in range(9)]),
        self.letter.extend([Tile('R', 1) for _ in range(5)]),
        self.letter.extend([Tile('S', 1) for _ in range(6)]),
        self.letter.extend([Tile('T', 1) for _ in range(4)]),
        self.letter.extend([Tile('U', 1) for _ in range(5)]),
        self.letter.extend([Tile('N', 2) for _ in range(5)]),
        self.letter.extend([Tile('O', 2) for _ in range(2)]),
        self.letter.extend([Tile('B', 3) for _ in range(2)]),
        self.letter.extend([Tile('C', 3) for _ in range(4)]),
        self.letter.extend([Tile('M', 3) for _ in range(2)]),
        self.letter.extend([Tile('P', 3) for _ in range(2)]),
        self.letter.extend([Tile('F', 4) for _ in range(1)]),
        self.letter.extend([Tile('H', 4) for _ in range(2)]),
        self.letter.extend([Tile('V', 4) for _ in range(1)]),
        self.letter.extend([Tile('Y', 4) for _ in range(1)]),
        self.letter.extend([Tile('CH', 5) for _ in range(1)]),
        self.letter.extend([Tile('Q', 5) for _ in range(1)]),
        self.letter.extend([Tile('J', 8) for _ in range(1)]),
        self.letter.extend([Tile('LL', 8) for _ in range(1)]),
        self.letter.extend([Tile('Ñ', 8) for _ in range(1)]),
        self.letter.extend([Tile('RR', 8) for _ in range(1)]),
        self.letter.extend([Tile('X', 8) for _ in range(1)]),
        self.letter.extend([Tile('Z', 10) for _ in range(1)])

        random.shuffle(self.tiles)
    

    def __init__(self):
        self.tiles = []
        for letter in letter:
            tile = Tile(letter, letter[letter][0])
            for _ in range(letter[letter][1]):
                self.tiles.append(tile)
        random.shuffle(self.tiles)

    def take(self, count):
        random.shuffle(self.tiles)
        tiles = []
        if count > len(self.tiles):
            raise DrawingMoreThanAvaliable
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)