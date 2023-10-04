from scrabble.Tile import *

class Player:
    def __init__(self):
        self.tiles = []
        self.name = None
        self.score = 0
   
    def has_letters(self, tiles_group):
        match = len(tiles_group)
        if isinstance(tiles_group, str):
            for i in tiles_group:
                for j in self.tiles:
                    if i == j.letter:
                        match -= 1
        else:   
            for i in tiles_group:
                for j in self.tiles:
                    if i.letter == j.letter:
                        match -= 1
        if match == 0:
            return True
        else:
            return False

    # def exchange_tiles(self, bag:BagTiles, tiles_to_exchange):
    #     for i in tiles_to_exchange:
    #         for j in self.tiles:
    #             if i.letter == j.letter:
    #                 break
    #             self.tiles.remove(j)
    #             tiles = bag.take(1) 
    #             if tiles:
    #                 self.tiles.append(tiles[0])
    #             else:
    #                 pass
                    
    #     bag.put(tiles_to_exchange)