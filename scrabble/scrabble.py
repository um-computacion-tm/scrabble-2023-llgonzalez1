from scrabble.board import Board
from scrabble.players import Player
from scrabble.models import Tilebag


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = Tilebag()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())
