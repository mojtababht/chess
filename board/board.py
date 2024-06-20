from . import letter_alt
import copy

from .square import Square
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King



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
    squares = []
    pieces = []
    selected_piece = None

    def __init__(self):
        for letter in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
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

    def get_square(self, cord: tuple) -> Square | None:
        if cord[0] > 7 or cord[0] < 0 or cord[1] > 7 or cord[1] < 0:
            return
            # raise ValueError('cord must be in (0-7, 0-7)')
        square = next(filter(lambda x: x.cord == cord, self.squares))
        return square

    def rotate_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

    def move(self, start: Square, target: Square) -> bool:
        if not start.piece:
            return False
        if self.turn == start.piece.color:
            if piece := start.piece.move(self, target):
                target.piece = piece
                start.piece = None
                self.rotate_turn()
                return True
        return False

    def valid_moves(self) -> list:
        moves = []
        for piece in filter(lambda x: x.color == self.turn, self.pieces):
            for square in piece.possible_moves(self):
                fake_board = copy.deepcopy(self)
                fake_board.pieces = copy.deepcopy(self.pieces)
                fake_board.squares = copy.deepcopy(self.squares)
                fake_piece = fake_board.get_square(piece.cord).piece
                fake_piece.cord = square.cord
                fake_board.get_square(square.cord).piece = fake_piece
                fake_board.get_square(piece.cord).piece = None
                if fake_board.is_in_check():
                    continue
                if piece.symbol == "K":
                    if piece.cord[0] - square.cord[0] == -2:
                        fake_board = copy.deepcopy(self)
                        fake_square = fake_board.get_square(piece.cord)
                        fake_square.piece.cord = (4, piece.cord[1])
                        fake_board.get_square((4, piece.cord[1])).piece = fake_square.piece
                        fake_square.piece = None
                        if fake_board.is_in_check():
                            continue
                moves.append(square)
        return moves

    def is_in_check(self) -> bool:
        next_turn_pieces = filter(lambda x: x.color != self.turn, self.pieces)
        king = next(filter(lambda x: x.color == self.turn and x.symbol == 'K', self.pieces))
        king_square = self.get_square(king.cord)
        next_turn_moves = []
        for piece in next_turn_pieces:
            next_turn_moves.extend(piece.possible_moves(self))
        if king_square in next_turn_moves:
            return True
        return False

    def is_in_check_mate(self) -> bool:
        if self.is_in_check():
            if not self.valid_moves():
                return True
        return True

    def is_in_draw(self) -> bool: # TODO: add repeat for draw
        if not self.is_in_check():
            if not self.valid_moves():
                return True
        return False
