from .piece import Piece
from .rook import Rook
from .bishop import Bishop


class Queen(Piece):
    symbol = 'q'

    def possible_moves(self, board) -> list:
        moves = []
        moves.extend(Rook(self.color, self.cord).possible_moves(board))
        moves.extend(Bishop(self.color, self.cord).possible_moves(board))
        return moves

    def move(self, board, target):
        self.cord = target.cord
        return self
