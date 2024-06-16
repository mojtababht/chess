from board.board import Board
from . import Piece, Rook, Bishop


class Queen(Piece):
    symbol = 'q'

    def possible_moves(self, board: Board) -> list:
        moves = []
        moves.extend(Rook(self.color, self.cord).possible_moves(board))
        moves.extend(Bishop(self.color, self.cord).possible_moves(board))
        return moves
