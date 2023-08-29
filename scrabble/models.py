import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = []
        self.tiles.extend([Tile('E', 1) for _ in range(12)]),
        self.tiles.extend([Tile('I', 1) for _ in range(6)]),
        self.tiles.extend([Tile('L', 1) for _ in range(4)]),
        self.tiles.extend([Tile('N', 1) for _ in range(5)]),
        self.tiles.extend([Tile('O', 1) for _ in range(9)]),
        self.tiles.extend([Tile('R', 1) for _ in range(5)]),
        self.tiles.extend([Tile('S', 1) for _ in range(6)]),
        self.tiles.extend([Tile('T', 1) for _ in range(4)]),
        self.tiles.extend([Tile('U', 1) for _ in range(5)]),
        self.tiles.extend([Tile('N', 2) for _ in range(5)]),
        self.tiles.extend([Tile('O', 2) for _ in range(2)]),
        self.tiles.extend([Tile('B', 3) for _ in range(2)]),
        self.tiles.extend([Tile('C', 3) for _ in range(4)]),
        self.tiles.extend([Tile('M', 3) for _ in range(2)]),
        self.tiles.extend([Tile('P', 3) for _ in range(2)]),
        self.tiles.extend([Tile('F', 4) for _ in range(1)]),
        self.tiles.extend([Tile('H', 4) for _ in range(2)]),
        self.tiles.extend([Tile('V', 4) for _ in range(1)]),
        self.tiles.extend([Tile('Y', 4) for _ in range(1)]),
        self.tiles.extend([Tile('CH', 5) for _ in range(1)]),
        self.tiles.extend([Tile('Q', 5) for _ in range(1)]),
        self.tiles.extend([Tile('J', 8) for _ in range(1)]),
        self.tiles.extend([Tile('LL', 8) for _ in range(1)]),
        self.tiles.extend([Tile('Ñ', 8) for _ in range(1)]),
        self.tiles.extend([Tile('RR', 8) for _ in range(1)]),
        self.tiles.extend([Tile('X', 8) for _ in range(1)]),
        self.tiles.extend([Tile('Z', 10) for _ in range(1)])

        random.shuffle(self.tiles)

    def take(self, count):
        if count > len(self.tiles):
            return None  # No hay suficientes fichas disponibles
        taken_tiles = random.sample(self.tiles, count)
        for tile in taken_tiles:
            self.tiles.remove(tile)
        return taken_tiles

    def put(self, tiles):
        self.tiles.extend(tiles)