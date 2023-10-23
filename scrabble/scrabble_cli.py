import os
from scrabble.scrabble import *


def clean_terminal():
    os.system('clear')

def players_to_play():
    while True:
        try: 
            player = int(input("Enter the number of players(2-4): "))
            if player <= 1 or player > 4:
                raise ValueError
            return player
        except ValueError:
            print("Invalid number")
            
def clear_terminal():
    while True:
        try: 
            clear_terminal = input("Clear terminal after each turn?(Y/N): ")
            if clear_terminal != "Y" and clear_terminal != "N":
                raise InvalidWordException
            if clear_terminal == "Y":
                return True
            else:
                return False
        except InvalidWordException:
            print("Invalid Letter")

class ScrabbleCli:
    def __init__(self, players):
        self.game = ScrabbleGame(players)

    def name_players(self, players):
        for i in range(players):
            name = str(input(f"Enter name of player {i+1}: " ))
            self.game.players[i].name = name
                        
    def show_score(self):
        print(self.game.current_player.score)
    
    def show_tiles(self):
        print(self.game.current_player.tiles)
        
    def show_current_player(self):
        print(f"Turn of player {self.game.current_player.name}")
        
    def exchange_index_tile(self):
        index_exchange = int(input(f"Enter index of tile to change (0-{len(self.game.current_player.tiles)-1}): "))
        tile_exchange = self.game.current_player.tiles[index_exchange]
        self.game.current_player.exchange_tile(self.game.bag_tiles ,tile_exchange)
        
    def choose_wildcard(self):
        wildcard = self.game.check_wildcard()
        if wildcard:
            letter_for_wild = str(input("Enter letter for wildcard:"))
            letter_for_wild = letter_for_wild.upper()
            for i in self.game.current_player.tiles:
                if i.value == 0:
                    i.set_letter(letter_for_wild)
            
    def get_row(self):
        while True:
            try:
                row = int(input("Enter row(0-14): "))
                if row < 0 or row >= 15:
                    raise ValueError
                return row
            except ValueError:
                print("Invalid number of row")

    def get_col(self):
        while True:
            try:
                col = int(input("Enter col(0-14): "))
                if col < 0 or col >= 14:
                    raise ValueError
                return col
            except ValueError:
                print("Invalid number of col")
            
    def get_orientation(self):
        while True:
            try:
                orientation = str(input("Enter orientation(H/V): "))
                orientation = orientation.upper()
                if orientation == "H" or orientation == "V":
                    return orientation
                raise ValueError
            except ValueError:
                print("Invalid orientation")
                
    def enter_word(self):
        while True:    
            try:
                word = str(input("Enter word or type -go back- to return: "))
                if word == "go back":
                    break
                word = self.game.str_to_list(word)
                row = self.get_row()
                col = self.get_col()
                orientation = self.get_orientation()
                location = (row, col)
                self.game.put_words(word, location, orientation)
                self.game.add_score(word, location, orientation)
                if self.game.validate_word(word, location, orientation) is False:
                    raise InvalidWordException
                self.game.get_words(word, location, orientation)
                if self.game.get_words(word, location, orientation) is False:
                    raise InvalidWordException
                self.end_current_turn()
            except InvalidWordException:
                print("Invalid word")
            
    def end_current_turn(self):
        raise EndTurnException        
    
    def vote_to_end_game(self):
        vote = str(input("End game?(Y/N): "))
        self.game.votes.extend(vote)

                
    def actual_turn(self):
        self.game.fill_current_player_tiles()
        while True:
            print("\n")
            print("Tiles:")
            self.show_tiles() 
            print("Score:")
            self.show_score()
            option = input(
                "\n"
                "Enter a number:\n"
                "0. Put Word\n"
                "1. Show Board\n"
                "2. Exchange Tiles\n"
                "3. End current turn\n"
                "9. Vote to end game\n"
                "= "
            
            )
            
            try:
                if option == "0":   
                    self.choose_wildcard()
                    self.enter_word() 
                    
                elif option == "1":
                    self.game.board.print_board()                
                elif option == "2":
                    tile_changes = int(input("Enter hoy many tiles are you changing: "))
                    for _ in range(tile_changes):
                        self.exchange_index_tile()
                        self.show_tiles()
                    self.end_current_turn() 
                elif option == "3":
                    self.end_current_turn()
                elif option == "9":
                    self.vote_to_end_game()
                    self.end_current_turn()
                else:
                    pass
            except EndTurnException:
                print(
                    "End Turn"
                    "\n"
                    )
                break
            
    def show_results(self):
        print("The Game has ended")
        leaderboard = self.game.sort_players_by_score()
        print(leaderboard)
        print(f"The winner is: {leaderboard[0][0]}")
