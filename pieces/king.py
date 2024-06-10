from itertools import product

from board.board import Board
from .piece import Piece


class King(Piece):
    symbol = 'K'

    def valid_moves(self, board: Board) -> list:  #TODO: check "check status" after move
        moves = []
        x = self.cord[0]
        y = self.cord[1]
        possible_x = list(filter(lambda i: 7 >= i >= 0, (x - 1, x + 1)))
        possible_y = list(filter(lambda i: 7 >= i >= 0, (y - 1, y + 1)))
        if board.is_in_check():
            ...
        else:
            for cord in product(possible_x, possible_y):  #combination of possible_x and possible_y
                square = board.get_square(cord)
                if square.piece:
                    if not square.piece.color == self.color:
                        moves.append(square)
                    continue
                moves.append(square)
        return moves
