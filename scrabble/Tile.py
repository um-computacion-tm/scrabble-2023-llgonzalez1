import random

class tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
    def __repr__(self):
        return f"({self.letter}, {self.value})"


class BagTiles:
    def __init__(self):
        self.tiles = []
        for _ in range(12):
            self.tiles.append(tile('A', 1))
            self.tiles.append(tile('E', 1))
        for _ in range(9):
            self.tiles.append(tile('O', 1))
        for _ in range(6):
            self.tiles.append(tile('I', 1))
            self.tiles.append(tile('S', 1))                         
        for _ in range(5):
            self.tiles.append(tile('N', 1))            
            self.tiles.append(tile('R', 1))
            self.tiles.append(tile('U', 1))
            self.tiles.append(tile('D', 2)) 
        for _ in range(4):
            self.tiles.append(tile('L', 1))
            self.tiles.append(tile('T', 1))
            self.tiles.append(tile('C', 3))
        for _ in range(2):
            self.tiles.append(tile('B', 3))
            self.tiles.append(tile('M', 3))
            self.tiles.append(tile('P', 3))
            self.tiles.append(tile('G', 2))
            self.tiles.append(tile('H', 4))
            self.tiles.append(tile(' ', 0))
        self.tiles.append(tile('F', 4))
        self.tiles.append(tile('V', 4))
        self.tiles.append(tile('Y', 4))
        self.tiles.append(tile('Ch', 5))
        self.tiles.append(tile('Q', 5))
        self.tiles.append(tile('J', 8))
        self.tiles.append(tile('LL', 8))
        self.tiles.append(tile('Ñ', 8))
        self.tiles.append(tile('RR', 8))
        self.tiles.append(tile('X', 8))
        self.tiles.append(tile('Z', 10))    
            
                                
        random.shuffle(self.tiles)


    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
        