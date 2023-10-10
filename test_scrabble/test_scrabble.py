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

    def test_validate_word_current_player(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='H', value=3),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "Hola"
        orientation = "H"
        location = (7,7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate == True
        
    def test_validate_word_current_player_has_not_letters(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='M', value=3),
            tile(letter='O', value=1),
            tile(letter='P', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(3))
        word = "Hola"
        orientation = "H"
        location = (7,7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate == False
      
    def test_validate_word_is_not_in_dictionary(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='A', value=3),
            tile(letter='S', value=1),
            tile(letter='D', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(3))
        word = "asd"
        orientation = "H"
        location = (7,7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate == False
        
    def test_validate_word_dont_fit_board(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='D', value=3),
            tile(letter='E', value=1),
            tile(letter='P', value=1),
            tile(letter='A', value=3),
            tile(letter='R', value=1),
            tile(letter='T', value=1),
            tile(letter='A', value=3),
            tile(letter='M', value=1),
            tile(letter='E', value=1),
            tile(letter='N', value=3),
            tile(letter='T', value=1),
            tile(letter='O', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(12))
        word = "departamento"
        orientation = "H"
        location = (7,7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate == False
        
    def test_validate_word_missing_letter_in_board(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.board.grid[7][7].add_letter(tile("H",3))
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(3))
        word = "Hola"
        orientation = "H"
        location = (7,7)
        word_validate = scrabble_game.validate_word(word, location, orientation)
        assert word_validate == True
        
    def test_end_game(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = []
        scrabble_game.current_player = scrabble_game.players[0]
        with self.assertRaises(end_game) as context:
            scrabble_game.end_game()
            
    def test_end_game_fail(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = [
            tile(letter='H', value=3),
            tile(letter='O', value=1)
            ]
        game_finish = scrabble_game.end_game()
        self.assertFalse(game_finish, False) 
        
    def test_full_board(self):
        scrabble_game = ScrabbleGame(players_count=2)
        for row in  scrabble_game.board.grid:
            for cell in row:
                cell.letter = tile("A",1)
        complete_board = scrabble_game.full_board()
        self.assertEqual(complete_board,True)
    
    def test_put_word_horizontal(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='H', value=3),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "Hola"
        orientation = "H"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        self.assertEqual(scrabble_game.board.grid[7][7].letter.letter, "H") 
        self.assertEqual(scrabble_game.board.grid[7][8].letter.letter, "O") 
        self.assertEqual(scrabble_game.board.grid[7][9].letter.letter, "L") 
        self.assertEqual(scrabble_game.board.grid[7][10].letter.letter, "A")  
        self.assertEqual(scrabble_game.current_player.tiles,[])
    
    def test_put_word_vertical(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='H', value=3),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
            tile(letter='H', value=3),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(5))
        word = "Hola"
        orientation = "V"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        self.assertEqual(scrabble_game.board.grid[7][7].letter.letter, "H") 
        self.assertEqual(scrabble_game.board.grid[8][7].letter.letter, "O") 
        self.assertEqual(scrabble_game.board.grid[9][7].letter.letter, "L") 
        self.assertEqual(scrabble_game.board.grid[10][7].letter.letter, "A") 
        self.assertEqual(scrabble_game.current_player.tiles[0].letter,"H")
        self.assertEqual(scrabble_game.current_player.tiles[0].value,3)
        
    def test_fill_player_tiles(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter="H", value=3)  
            ]
        scrabble_game.fill_current_player_tiles()
        self.assertEqual(scrabble_game.current_player.tiles[0].letter, "H")
        self.assertEqual(scrabble_game.current_player.tiles[0].value, 3)
    
    def test_add_score(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='H', value=3),
            tile(letter='O', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
            tile(letter='H', value=3),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(5))
        word = "Hola"
        orientation = "V"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        scrabble_game.add_score(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score, 12)
        
    def test_add_score_horizontal(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='S', value=2),
            tile(letter='O', value=1),
            tile(letter='D', value=2),
            tile(letter='A', value=1),
            tile(letter='A', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(5))
        word = "asado"
        orientation = "H"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        scrabble_game.add_score(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score, 16)
        
    def test_add_score_2_multipliers(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            tile(letter='A', value=1),
            tile(letter='D', value=1),
            tile(letter='E', value=1),
            tile(letter='L', value=1),
            tile(letter='A', value=1),
            tile(letter='N', value=3),
            tile(letter='T', value=3),
            tile(letter='E', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(8))
        word = "adelante"
        orientation = "H"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        scrabble_game.add_score(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score, 78)
        
if __name__ == '__main__':
    unittest.main()
