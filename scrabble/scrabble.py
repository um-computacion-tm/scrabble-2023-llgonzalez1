from scrabble.board import *
from scrabble.player import *
from scrabble.Tile import *
from scrabble.cell import *

class end_turn(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player())    
        self.current_player = None
        self.turn = 0
        
    def next_turn(self):
        self.turn += 1
        if self.current_player is None:
            self.current_player = self.players[0]   
        else:   
            index = self.players.index(self.current_player) + 1
            if index < len(self.players): 
                self.current_player = self.players[index]
            else:
                self.current_player = self.players[0]
    
    def actual_turn(self):
        while True:
            option = int(input(
                "Indique un número:\n"
                "0. Colocar palabra\n"
                "1. Mostrar Tiles\n"
                "2. Mostrar Tablero\n"
                "3. Mostrar Puntaje\n"
                "4. Intercambiar Fichas\n"
                "5. Terminar turno\n"
                " "
            ))
            try:    
                if option == 1:
                    print(self.current_player.tiles)
                elif option == 2:
                    self.board.print_board()
                elif option == 3:
                    print(self.current_player.score)
                elif option == 4:
                    pass
                elif option == 5:
                    raise end_turn
                else:
                    pass
            except end_turn:
                print("Fin del turno")
                break
"""   
    def validate_word(self, word, location, orientation):
        '''
        1- Validar que usuario tiene esas letras
        2- Validar que la palabra entra en el tablero
        '''
        valid = self.board.validate_word_place_board(word, location, orientation)
        valid_2 = self.current_player.has_letters(word)
        if valid_2 == True: 
            return True
        else:
            return False
                        
                        
            
                
            
            
             
    
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
    
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''
"""   