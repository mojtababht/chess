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

    def __init__(self):
        squares = []
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
                squares.append(Square(letter, number, piece))