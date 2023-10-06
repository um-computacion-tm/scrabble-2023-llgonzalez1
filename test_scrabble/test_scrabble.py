import unittest
from scrabble.scrabble import *



class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn() 
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[1]
    
    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    # def test_validate_word_current_player(self):
    #     scrabble_game = ScrabbleGame(players_count=2)
    #     scrabble_game.current_player = scrabble_game.players[0]
    #     bag_tile = [
    #         Tile(letter='H', value=3),
    #         Tile(letter='O', value=1),
    #         Tile(letter='L', value=1),
    #         Tile(letter='A', value=1),
    #     ]
    #     for i in bag_tile:
    #         scrabble_game.current_player.tiles.append(i)
    #     word = "Hola"
    #     orientation = "H"
    #     location = (7,7)
    #     word_validate = scrabble_game.validate_word(word, location, orientation)
    #     assert word_validate == True
      
        
if __name__ == '__main__':
    unittest.main()