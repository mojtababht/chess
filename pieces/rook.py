from board.board import Board
from .piece import Piece


class Rook(Piece):
    symbol = 'r'

    def possible_moves(self, board: Board) -> list:
        moves = []
        for i in range(self.cord[0] + 1, 8):
            square = board.get_square((i, self.cord[1]))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.append(square)
                break
            moves.append(square)
        for i in range(self.cord[0] - 1, -1, -1):
            square = board.get_square((i, self.cord[1]))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.append(square)
                break
            moves.append(square)
        for i in range(self.cord[1] + 1, 8):
            square = board.get_square((self.cord[0], i))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.append(square)
                break
            moves.append(square)
        for i in range(self.cord[1] - 1, -1, -1):
            square = board.get_square((self.cord[0], i))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.append(square)
                break
            moves.append(square)
        return moves
