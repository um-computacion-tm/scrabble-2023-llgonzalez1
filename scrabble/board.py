from scrabble.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '', None, True) for _ in range(15) ]
            for _ in range(15)
        ]



