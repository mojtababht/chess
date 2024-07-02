from itertools import product
from pathlib import Path

from .piece import Piece

images_path = Path().parent.joinpath('imgs')


class King(Piece):
    symbol = 'K'
    moved = False

    def __init__(self, color, cord):
        super().__init__(color, cord)
        self.image = images_path.joinpath('w_king.png') if color == 'white' else images_path.joinpath('b_king.png')

    def possible_moves(self, board):
        moves = set()
        x = self.cord[0]
        y = self.cord[1]
        possible_x = list(filter(lambda i: 7 >= i >= 0, range(x - 1, x + 1)))
        possible_y = list(filter(lambda i: 7 >= i >= 0, range(y - 1, y + 1)))
        for cord in product(possible_x, possible_y): # combination of possible_x and possible_y
            square = board.get_square(cord)
            if square.piece:
                if square.piece.color == self.color:
                    continue
            moves.add(square)
        moves.update(self.get_castle_moves(board))
        return moves

    def get_castle_moves(self, board):
        moves = set()
        if not self.moved:
            for cord in [(i, self.cord[1]) for i in range(1, self.cord[0])]:
                if board.get_square(cord).piece:
                    break
            else:
                rook_square = board.get_square((0, self.cord[1]))
                if piece := rook_square.piece:
                    if piece.symbol == 'r':
                        if not piece.moved:
                            moves.add(board.get_square((1, self.cord[1])))
            for cord in [(i, self.cord[1]) for i in range(self.cord[0] + 1, 7)]:
                if board.get_square(cord).piece:
                    break
            else:
                rook_square = board.get_square((7, self.cord[1]))
                if piece := rook_square.piece:
                    if piece.symbol == 'r':
                        if not piece.moved:
                            moves.add(board.get_square((1, self.cord[1])))
        return moves

    def valid_moves(self, board):
        moves = super().valid_moves(board)
        next_turn_pieces = filter(lambda x: x.color != board.turn, board.pieces)
        next_turn_moves = set()
        for piece in next_turn_pieces:
            next_turn_moves.update(piece.possible_moves(board))
        valid_moves = set(moves) - set(next_turn_moves)
        return list(valid_moves)

    def move(self, board, target):
        self.cord = target.cord
        if not self.moved:
            if self.cord[0] - target.cord[0] == 2:
                board.get_square((0, self.cord[1])).piece.move(board, board.get_square((2, self.cord[1])))
            if self.cord[0] - target.cord[0] == -2:
                board.get_square((7, self.cord[1])).piece.move(board, board.get_square((4, self.cord[1])))
        self.moved = True
        return self
