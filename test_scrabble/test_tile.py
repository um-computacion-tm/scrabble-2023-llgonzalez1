import unittest
from scrabble.Tile import (
    tile,
    BagTiles,
)
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tiles = tile('A', 1)
        self.assertEqual(tiles.letter, 'A')
        self.assertEqual(tiles.value, 1)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
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
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [tile('Z', 1), tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            102,
        )



if __name__ == '__main__':
    unittest.main()