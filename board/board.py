from . import letter_alt
from .square import Square
from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King


piece_alt = {
    'a': Rook,
    'b': Knight,
    'c': Bishop,
    'd': Queen,
    'e': King,
    'f': Bishop,
    'g': Knight,
    'h': Rook,
}


class Board:
    turn = 'white'

    def __init__(self):
        self.squares = []
        self.pieces = []
        for letter in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
            for number in range(1, 9):
                piece = None
                if number == 1:
                    cord = (letter_alt[letter], 0)
                    piece = piece_alt[letter]('white', cord)
                elif number == 2:
                    cord = (letter_alt[letter], 1)
                    piece = Pawn('white', cord)
                elif number == 7:
                    cord = (letter_alt[letter], 6)
                    piece = Pawn('black', cord)
                elif number == 8:
                    cord = (letter_alt[letter], 7)
                    piece = piece_alt[letter]('black', cord)
                if piece:
                    self.pieces.append(piece)
                self.squares.append(Square(letter, number, piece))

    def get_square(self, cord: tuple) -> Square:
        if cord[0] > 7 or cord[1] > 7:
            raise ValueError('cord must be in (0-7, 0-7)')
        square = next(filter(lambda x: x.cord == cord, self.squares))
        return square

    def move(self, start: Square, target: Square) -> bool:
        if not (piece := start.piece):
            return False

        ...

    def get_turn(self):
        return self.turn

    def is_in_check(self):
        ...

    def is_in_check_mate(self):
        ...