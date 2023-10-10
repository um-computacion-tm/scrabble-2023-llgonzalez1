from scrabble.cell import *
from scrabble.board import *
from scrabble.Tile import *
from scrabble.scrabble import *
from scrabble.player import *

def players_to_play():
    while True:
        try: 
            player = int(input("Indique la cantidad de jugadores(2-4): "))
            if player <= 1 or player > 4:
                raise ValueError
            return player
        except ValueError:
            print("Valor invalido")
            
    
def main():
    player = players_to_play()
    scrabble_game = ScrabbleGame(player)
    for i in range(player):
        nombre = str(input(f"Indique nombre de jugador {i+1}: " ))
        scrabble_game.players[i].name = nombre
    while True:
        try:
            scrabble_game.next_turn()
            scrabble_game.end_game()
            scrabble_game.show_current_player()  
            scrabble_game.actual_turn()

        except end_game:
            print("FIN DEL JUEGO")
            break
main()
    
    
