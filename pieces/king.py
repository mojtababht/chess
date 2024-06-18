from itertools import product

from board.board import Board
from board.square import Square
from .piece import Piece


class King(Piece):
    symbol = 'K'
    moved = False

    def possible_moves(self, board: Board) -> list:
        moves = []
        x = self.cord[0]
        y = self.cord[1]
        possible_x = list(filter(lambda i: 7 >= i >= 0, (x - 1, x + 1)))
        possible_y = list(filter(lambda i: 7 >= i >= 0, (y - 1, y + 1)))
        for cord in product(possible_x, possible_y):  # combination of possible_x and possible_y
            square = board.get_square(cord)
            if square.piece:
                if square.piece.color == self.color:
                    continue
            moves.append(square)
        moves.extend(self.get_castle_moves(board))
        return moves

    def get_castle_moves(self, board:Board) -> list:
        moves = []
        if not self.moved:
            for cord in [(i, self.cord[1]) for i in range(1, self.cord[0])]:
                if board.get_square(cord).piece:
                    break
            else:
                rook_square = board.get_square((0, self.cord[1]))
                if piece := rook_square.piece:
                    if piece.symbol == 'r':
                        if not piece.moved:
                            moves.append(board.get_square((1, self.cord[1])))
            for cord in [(i, self.cord[1]) for i in range(self.cord[0] + 1, 7)]:
                if board.get_square(cord).piece:
                    break
            else:
                rook_square = board.get_square((7, self.cord[1]))
                if piece := rook_square.piece:
                    if piece.symbol == 'r':
                        if not piece.moved:
                            moves.append(board.get_square((1, self.cord[1])))
        return moves

    def move(self, board: Board, target: Square) -> bool:
        self.cord = target.cord
        if not self.moved:
            if self.cord[1] - target.cord[1] == 2:
                board.get_square((0, self.cord[1])).piece.move(board, board.get_square((2, self.cord[1])))
            if self.cord[1] - target.cord[1] == -2:
                board.get_square((7, self.cord[1])).piece.move(board, board.get_square((4, self.cord[1])))
        self.moved = True
        return True
