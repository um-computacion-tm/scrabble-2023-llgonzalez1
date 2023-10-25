import unittest
from scrabble.scrabble_cli import *
from unittest.mock import patch
from io import StringIO

class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["Y"])
    def test_clear_terminal_with_Y(self, mock_input):
        result = clear_terminal()
        self.assertTrue(result) 

    @patch('builtins.input', side_effect=["N"])
    def test_clear_terminal_with_N(self, mock_input):
        result = clear_terminal()
        self.assertFalse(result)  

   
    @patch('builtins.input', side_effect=["X", "Y"])
    @patch('builtins.print')
    def test_clear_terminal_invalid_then_valid(self, mock_input, mock_print):
        result = clear_terminal()
        self.assertTrue(result)
        
    @patch('os.system') 
    def test_clean_terminal_calls_os_system_clear(self, mock_os_system):
        clean_terminal()  
        mock_os_system.assert_called_once_with('clear')
    
    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(
            players_to_play(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', "10", '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(
            players_to_play(),
            3,
        )
        
    @patch('builtins.input', return_value="3")
    def test_init(self, mock_input):
        cli = ScrabbleCli(mock_input)
        self.assertIsInstance(cli.game, ScrabbleGame)
    
       
    @patch('builtins.input', side_effect=['Alice', 'Bob', 'Charlie'])
    def test_scrabble_cli_with_names(self, mock_input):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.name_players(3)        
        expected_names = ['Alice', 'Bob', 'Charlie']
        for i in range(3):
            self.assertEqual(scrabble_cli.game.players[i].name, expected_names[i])
            
    @patch('builtins.print')
    def test_show_score(self, print_patched):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.score = 40
        scrabble_cli.show_score()
        
    @patch('builtins.print')
    def test_show_player_tiles(self, print_patched):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile("A",1),
            tile("B",2)
        ]
        scrabble_cli.show_tiles()
        
    @patch('builtins.print')
    def test_show_current_player(self, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.name = "Juan"
        scrabble_cli.show_current_player()
        
    @patch('builtins.input', return_value='2')
    def test_exchange_tiles(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile("A",1),
            tile("B",2),
            tile("C",3),
            tile("D",4),
            tile("E",5),
            tile("F",6),
            tile("G",7)
        ]
        scrabble_cli.exchange_index_tile()
        
    @patch('builtins.input', return_value="H")
    def test_choose_wildcard(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile(" ",0),
        ]
        scrabble_cli.choose_wildcard()
        self.assertEqual(scrabble_cli.game.current_player.tiles[0].letter, "H")
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', "16", '3'])
    def test_get_row(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_row()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['F', "-3", '7'])
    def test_get_col(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_col()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['F', "3", 'H'])
    def test_get_orientation_horizontal(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_orientation()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', "Vertical", 'V'])
    def test_get_orientation_vertical(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_orientation()
        
    def test_end_current_turn(self):
        scrabble_cli = ScrabbleCli(2)

        with self.assertRaises(EndTurnException):
            scrabble_cli.end_current_turn()
        
    @patch('builtins.input', return_value="Y")
    def test_vote_to_end_game(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.vote_to_end_game()
        self.assertEqual(scrabble_cli.game.votes, ["Y"])
        
       
    @patch('builtins.input', side_effect=["perro", "7", "7", "H", "go back"])
    @patch('builtins.print')
    def test_enter_word_valid_input_and_go_back(self, mock_input, mock_print):
        

        scrabble_cli = ScrabbleCli(2)  
        
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile("A",1),
            tile("H",1),
            tile("O",1),
            tile("L",1),
        ]
        
        scrabble_cli.enter_word()  
            
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["0", "hola", "7", "7", "V"])
    def test_actual_turn_put_word(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile("A",1),
            tile("H",1),
            tile("O",1),
            tile("L",1),
        ]

    
        scrabble_cli.actual_turn()
        
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["5","1","3"])
    def test_actual_turn_miss_and_print_board(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile("A",1),
            tile("H",1),
            tile("O",1),
            tile("L",1),
        ]

        scrabble_cli.actual_turn()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["2","1","3"])
    def test_actual_turn_exchange_tiles(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            tile("A",1),
            tile("H",1),
            tile("O",1),
            tile("L",1),
        ]

        scrabble_cli.actual_turn()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["9","Y"])
    def test_actual_turn_cote_to_end(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]

        scrabble_cli.actual_turn()
               
               
    
    def test_show_results(self):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.players[0].name = "pepe"
        scrabble_cli.game.players[0].score = 100
        scrabble_cli.game.players[1].name = "julia"
        scrabble_cli.game.players[1].score = 200
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            scrabble_cli.show_results()

            expected_output = "The Game has ended\n[('julia', 200), ('pepe', 100)]\nThe winner is: julia\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    
            
    
        
        


if __name__ == '__main__':
    unittest.main()
