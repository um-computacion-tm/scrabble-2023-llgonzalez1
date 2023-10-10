from scrabble.board import *
from scrabble.player import *
from scrabble.Tile import *
from scrabble.cell import *
from scrabble.dictionary import *

class end_game(Exception):
    pass

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
        self.board.add_multiplier()
        self.dictionary = Dictionary('dictionaries/dictionary.txt')
        
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
    
    def end_current_turn(self):
        raise end_turn
        
    def full_board(self):
        for row in self.board.grid:
            for cell in row:
                if cell.letter == None:
                    return False
        return True
    
    def end_game(self):
        full_board = self.full_board()
        if full_board:
            raise end_game
        elif len(self.bag_tiles.tiles)==0:
                if len(self.current_player.tiles)==0:
                    raise end_game
        else:
            pass
    
    
    def fill_current_player_tiles(self):
        self.current_player.tiles.extend(self.bag_tiles.take(7-len(self.current_player.tiles)))              
    
    def show_score(self):
        print(self.current_player.score)
    
    def show_tiles(self):
        print(self.current_player.tiles)
        
    def show_current_player(self):
        print(f"Turno del jugador {self.current_player.name}")
        
    def exchange_index_tile(self):
        index_exchange = int(input(f"Ingrese indice de ficha a cambiar (0-{len(self.current_player.tiles)-1}): "))
        tile_exchange = self.current_player.tiles[index_exchange]
        self.current_player.exchange_tile(self.bag_tiles ,tile_exchange)
                
    def actual_turn(self):
        self.fill_current_player_tiles()
        while True:
            option = int(input(
                "Indique un número:\n"
                "0. Colocar palabra\n"
                "1. Mostrar Tiles\n"
                "2. Mostrar Tablero\n"
                "3. Mostrar Puntaje\n"
                "4. Intercambiar Fichas\n"
                "5. Terminar turno\n"
                "= "
            ))
            try:
                if option == 0:   
                    pass
                elif option == 1:
                    self.show_tiles()                 
                elif option == 2:
                    self.board.print_board()
                elif option == 3:
                    self.show_score() 
                elif option == 4:
                    tile_changes = int(input("Indique la cantidad de cambios a realizar: "))
                    for _ in range(tile_changes):
                        self.exchange_index_tile()
                        self.show_tiles()
                    self.end_current_turn() 
                elif option == 5:
                    self.end_current_turn()
                else:
                    pass
            except end_turn:
                print("Fin del turno")
                break

   
    def validate_word(self, word, location, orientation):
        valid_place_word = self.board.validate_word_place_board(word, location, orientation)
        if  valid_place_word:
            valid_dict = self.dictionary.has_word(word)
            if valid_dict:
                valid_has_letters = self.current_player.has_letters(self.board.missing_letters)
                if valid_has_letters:
                    return True       
        return False
       
    def put_words(self, word, location, orientation):
        valid_word = self.validate_word(word, location, orientation)
        word = word.upper()
        if valid_word:
            for i in self.board.missing_letters:
                for j in self.current_player.tiles:
                    if i == j.letter:    
                        if orientation=="H":    
                            self.board.grid[self.board.position_row][self.board.position_col].add_letter(j)  
                            self.current_player.tiles.remove(j)                          
                            self.board.position_col += 1
                            break
                        elif orientation=="V":
                            self.board.grid[self.board.position_row][self.board.position_col].add_letter(j)  
                            self.current_player.tiles.remove(j) 
                            self.board.position_row += 1    
                            break            
        
        
    def add_score(self, word, location, orientation):
        valid_word = self.validate_word(word, location, orientation)
        row = location[0]
        col = location[1]
        cells = []
        if valid_word:
            for i in word:
                if orientation=="H":
                    cells.append(self.board.grid[row][col])
                    col += 1
                elif orientation=="V":
                    cells.append(self.board.grid[row][col])
                    row += 1
        value = calculate_word_value(cells)
        self.current_player.score += value.calculate_word()
        
"""  
  
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''

""" 
