from pathlib import Path

from .piece import Piece
from .rook import Rook
from .bishop import Bishop


images_path = Path().parent.joinpath('imgs')


class Queen(Piece):
    symbol = 'q'

    def __init__(self, color, cord):
        super().__init__(color, cord)
        self.image = images_path.joinpath('w_queen.png') if color == 'white' else images_path.joinpath('b_queen.png')

    def possible_moves(self, board) -> set:
        moves = []
        moves.extend(Rook(self.color, self.cord).possible_moves(board))
        moves.extend(Bishop(self.color, self.cord).possible_moves(board))
        return set(moves)

    def move(self, board, target):
        self.cord = target.cord
        return self
