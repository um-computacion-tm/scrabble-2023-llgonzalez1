import unittest
from scrabble.player import Player
from scrabble.Tile import *

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            tile(letter='H', value=4),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
            tile(letter='C', value=3),
            tile(letter='U', value=1),
            tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = [
            tile(letter='H', value=4),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
        ]
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            tile(letter='P', value=3),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
            tile(letter='C', value=3),
            tile(letter='U', value=1),
            tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = [
            tile(letter='H', value=4),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
        ]
        

        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, False)
        
    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            tile(letter='H', value=4),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
            tile(letter='C', value=3),
            tile(letter='U', value=1),
            tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = "HOLA"
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)

    # def test_exchange_player_tiles(self):
    #     bag_tile = BagTiles()
    #     bag_tile.tiles = [
    #         Tile(letter='H', value=4),
    #         Tile(letter='A', value=1),
    #         Tile(letter='C', value=3),
    #         Tile(letter='I', value=1),
    #     ]
    #     player_1 = Player()
    #     for i in bag_tile.tiles:
    #         player_1.tiles.append(i)
          
    #     bag_tile.tiles = [
    #         Tile(letter='X', value=4),
    #         Tile(letter='Y', value=4),
    #     ]
    #     tiles_to_exchange = [
    #         Tile(letter='H', value=4),
    #         Tile(letter='A', value=1),
    #     ]
        
    #     player_1.exchange_tiles(bag_tile, tiles_to_exchange)
        
    #     self.assertEqual(player_1.tiles[0].letter, "X")
    #     self.assertEqual(player_1.tiles[1].letter, "Y")
    #     self.assertEqual(player_1.tiles[2].letter, "C")
    #     self.assertEqual(player_1.tiles[3].letter, "I")
        
        
        
        
if __name__ == '__main__':
    unittest.main()