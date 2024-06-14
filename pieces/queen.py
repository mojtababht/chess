from board.board import Board
from . import Piece, Rook, Bishop


class Queen(Piece):
    symbol = 'q'

    def valid_moves(self, board: Board) -> list:  # TODO: check "check status" after move
        moves = []
        if board.is_in_check():
            ...
        else:
            moves.extend(Rook(self.color, self.cord).valid_moves(board))
            moves.extend(Bishop(self.color, self.cord).valid_moves(board))
        return moves
