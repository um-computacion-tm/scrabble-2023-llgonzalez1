from scrabble.board import *
from scrabble.player import *
from scrabble.Tile import *
from scrabble.cell import *
from scrabble.dictionary import *

class end_game(Exception):
    pass

class EndTurnException(Exception):
    pass

class InvalidWordException(Exception):
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
        self.votes = []
        
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
    
        
    def full_board(self):
        for row in self.board.grid:
            for cell in row:
                if cell.letter == None:
                    return False
        return True
    
    def sort_players_by_score(self):
        score_board = {}
        for player in self.players:
            score_board[player.name] = player.score
        sorted_score = sorted(score_board.items(), key=lambda item: item[1], reverse=True)
        return sorted_score
            
    
    def fill_current_player_tiles(self):
        self.current_player.tiles.extend(self.bag_tiles.take(7-len(self.current_player.tiles)))
        
          
    
    def end_game(self):
        full_board = self.full_board()
        if full_board:
            raise end_game
        elif len(self.bag_tiles.tiles)==0:
                if len(self.current_player.tiles)==0:
                    raise end_game
        if len(self.votes)==len(self.players):
            if all(vote == "Y" for vote in self.votes):
                raise end_game
            else:
                self.votes = []
        
        
    def move_position(self, orientation, row, col):
        if orientation == "H":
            col += 1
        elif orientation == "V":
            row += 1
        return row, col
    
    def str_to_list(self, string):
        consecutive_group = ""
        word = []
        for letter in string:
            if ((consecutive_group == "" or letter == consecutive_group[-1]) 
                or (letter=="h" and consecutive_group[-1]=="c")):
                consecutive_group += letter
            else:
                word.append(consecutive_group)
                consecutive_group = letter

        if consecutive_group:
            word.append(consecutive_group)      
        return word
   
    def validate_word(self, word, location, orientation):
        valid_place_word = self.board.validate_word_place_board(word, location, orientation)
        if  valid_place_word:
            valid_dict = self.dictionary.has_word(word)
            if valid_dict:
                valid_has_letters = self.current_player.has_letters(self.board.missing_letters)
                if valid_has_letters:
                    return True       
        return False   
    
    def check_wildcard(self):
        for i in self.current_player.tiles:
            if i.value == 0:
                return True

        
    def put_words(self, word, location, orientation):
        valid_word = self.validate_word(word, location, orientation)
        row, col = location
        if valid_word:
            if isinstance(word, list): 
                for i in word:
                    word = [letter.upper() for letter in word]
            else:    
                word = word.upper()
            for letter in word:
                matching_tile = next((tile for tile in self.current_player.tiles if tile.letter == letter), None)
                if matching_tile:
                    self.board.grid[row][col].add_letter(matching_tile)
                    self.current_player.remove_tile(matching_tile)
                row, col = self.move_position(orientation, row, col)                   
         
    def deactivate_cells_letters(self, cells):
        for i in cells:
            i.deactivate_cell()           
        
    def add_score(self, word, location, orientation):
        valid_word = self.validate_word(word, location, orientation)
        row = location[0]
        col = location[1]
        cells = []
        if valid_word:
            for i in word:
                cells.append(self.board.grid[row][col])
                row, col = self.move_position(orientation, row, col)
        value = calculate_word_value(cells)
        self.current_player.score += value.calculate_word()
        self.deactivate_cells_letters(cells)   
  
    def check_word_to_str(self, cell_list):
        word_from_list = ""
        if cell_list is not False:
            for cell in cell_list:
                tile = cell.letter
                word_from_list += tile.get_letter()
        return word_from_list

    def validate_check_word(self, word_from_list):
        word_from_list = word_from_list.lower()
        return self.dictionary.has_word(word_from_list)
    
    
    def get_words(self, word, location, orientation):
        row, col = location
        cell_0 = [Cell(1,None,None,True)]
        cell_list = []
        list_word = []
        for i in word:
            if orientation == "V":
                if self.board.check_word_horizontal(row, col)!=False:
                    cell_list.append(self.board.check_word_horizontal(row, col))
            elif orientation == "H":
                if self.board.check_word_vertical(row, col)!=False:
                    cell_list.append(self.board.check_word_vertical(row, col))
            row, col = self.move_position(orientation, row, col)
        for lists in cell_list:
            list_word.append(self.check_word_to_str(lists))
        for words in list_word:
            if self.validate_check_word(words)==False:
                return False
        for lists in cell_list:
            for cell in lists:
                no_sum = False
                if cell.active:
                    break
                else:
                    no_sum = True
            if no_sum:
                value = calculate_word_value(cell_0)
                self.current_player.score += value.calculate_word()
            else:
                value = calculate_word_value(lists)
                self.current_player.score += value.calculate_word()
        