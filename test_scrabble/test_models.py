import unittest
from scrabble.models import (
    Tilebag,
    Tile,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tiles = Tile('A', 1) 
        self.assertEqual(tiles.letter, 'A')
        self.assertEqual(tiles.value, 1)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = Tilebag()
        self.assertEqual(
            len(bag.tiles),
            86,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = Tilebag()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            84,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = Tilebag()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            88,
        )


if __name__ == '__main__':
    unittest.main()
