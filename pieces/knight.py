from itertools import product

from board.board import Board
from .piece import Piece


class Knight(Piece):
    symbol = 'k'

    def valid_moves(self, board: Board) -> list:  #TODO: check "check status" after move
        moves = []
        x = self.cord[0]
        y = self.cord[1]
        possible_cords = list(product(filter(lambda i: 7 >= i >= 0, (x - 1, x + 1)),
                                      filter(lambda i: 7 >= i >= 0, (y - 2, y + 2)))) + list(
            product(filter(lambda i: 7 >= i >= 0, (x - 2, x + 2)), filter(lambda i: 7 >= i >= 0, (y - 1, y + 1))))
        if board.is_in_check():
            ...
        else:
            for cord in possible_cords:
                square = board.get_square(cord)
                if square.piece:
                    if square.piece.color == self.color:
                        moves.append(square)
                    continue
                moves.append(square)
        return moves
