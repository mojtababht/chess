from . import letter_alt
import copy
from functools import lru_cache

from .square import Square
from pieces.piece import Piece
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
    squares = {}
    selected_piece = None
    updated_squares = set()

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
                self.squares[(letter_alt[letter], number - 1)] = (Square(letter, number, piece))

    @lru_cache
    def get_square(self, cord: tuple) -> Square | None:
        if cord[0] > 7 or cord[0] < 0 or cord[1] > 7 or cord[1] < 0:
            return
            # raise ValueError('cord must be in (0-7, 0-7)')
        square = self.squares[cord]
        return square

    def get_pieces(self, color=None):
        if color:
            color = (color,)
        else:
            color = ('white', 'black')
        pieces = map(lambda s: s.piece, self.squares.values())
        pieces = filter(lambda p: p and p.color in color, pieces)
        return set(pieces)

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
                if piece.symbol == 'K':
                    if castle_data := piece.castle_data:
                        rook_start_square = self.get_square(castle_data['rook_start'])
                        rook_start_square.piece = None
                        rook_target_square = self.get_square(castle_data['rook_target'])
                        rook_target_square.piece = castle_data['rook']
                        king_target_square = self.get_square(castle_data['king_target'])
                        king_target_square.piece = piece
                        self.updated_squares = {start, rook_start_square, rook_target_square, king_target_square}
                else:
                    target.piece = piece
                    self.updated_squares = {start, target}
                start.piece = None
                self.rotate_turn()
                self.valid_moves.cache_clear()
                Piece.valid_moves.cache_clear()
                # self.get_square.cache_clear()
                return True
        return False

    def fake_move(self, start: Square, target: Square):
        fake_board = copy.deepcopy(self)
        fake_board.squares = copy.deepcopy(self.squares)
        # for piece in fake_board.pieces:
        #     fake_board.get_square(piece.cord).piece = piece
        start = fake_board.get_square(start.cord)
        target = fake_board.get_square(target.cord)
        if fake_board.move(start, target):
            fake_board.rotate_turn()
            if not fake_board.is_in_check():
                return True

    @lru_cache(1)
    def valid_moves(self):
        moves = []
        for piece in self.get_pieces(self.turn):
            if piece.valid_moves(self):
                moves.append((piece, piece.valid_moves(self)))
        return moves

    def is_in_check(self) -> bool:
        if self.turn == 'black':
            color = 'white'
        else:
            color = 'black'
        next_turn_pieces = self.get_pieces(color)
        king_square = next(filter(lambda s: s.piece and
                                            s.piece.symbol == 'K' and
                                            s.piece.color == self.turn,
                                  self.squares.values()))
        for piece in next_turn_pieces:
            if king_square in piece.possible_moves(self):
                return True
        return False

    def is_in_check_mate(self) -> bool:
        if self.is_in_check():
            if not self.valid_moves():
                return True
        return False

    def is_in_draw(self) -> bool: # TODO: add repeat for draw
        if not self.is_in_check():
            if not self.valid_moves():
                return True
        return False

    def __str__(self):
        view = [
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00'],
            ['00', '00', '00', '00', '00', '00', '00', '00']
        ]
        for square in self.squares:
            if piece := square.piece:
                x, y = piece.cord
                view[x][y] = piece.color[0] + piece.symbol
        ret = ''
        for row in view:
            ret += f'{str(row)}, \n'
        return ret
