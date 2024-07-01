from itertools import product
from pathlib import Path

from .piece import Piece


images_path = Path().parent.joinpath('imgs')


class Knight(Piece):
    symbol = 'k'

    def __init__(self, color, cord):
        super().__init__(color, cord)
        self.image = images_path.joinpath('w_knight.png') if color == 'white' else images_path.joinpath('b_knight.png')

    def possible_moves(self, board):
        moves = set()
        x = self.cord[0]
        y = self.cord[1]
        possible_cords = list(product(filter(lambda i: 7 >= i >= 0, (x - 1, x + 1)),
                                      filter(lambda i: 7 >= i >= 0, (y - 2, y + 2)))) + list(
            product(filter(lambda i: 7 >= i >= 0, (x - 2, x + 2)), filter(lambda i: 7 >= i >= 0, (y - 1, y + 1))))
        for cord in possible_cords:
            square = board.get_square(cord)
            if square.piece:
                if square.piece.color != self.color:
                    moves.add(square)
                continue
            moves.add(square)
        return moves

    def move(self, board, target):
        self.cord = target.cord
        return self
