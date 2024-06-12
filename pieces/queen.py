from board.board import Board
from . import Piece, Rook, Bishop


class Queen(Piece):
    symbol = 'q'

    def valid_moves(self, board: Board) -> list:  #TODO: check "check status" after move
        moves = []
        # if board.is_in_check():
        #     ...
        # else:
        #     ...

        return moves