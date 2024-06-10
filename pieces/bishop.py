from board.board import Board
from .piece import Piece


class Bishop(Piece):
    symbol = 'b'

    def valid_moves(self, board: Board) -> list:  #TODO: check "check status" after move
        moves = []
        if board.is_in_check():
            ...
        else:
            for x, y in zip(range(self.cord[0] + 1, 8), range(self.cord[2] + 1, 8)):
                square = board.get_square((x, y))
                if square.piece:
                    if not square.piece.color == self.color:
                        moves.append(square)
                    break
                moves.append(square)
            for x, y in zip(range(self.cord[0] - 1, -1, -1), range(self.cord[2] - 1, -1, -1)):
                square = board.get_square((x, y))
                if square.piece:
                    if not square.piece.color == self.color:
                        moves.append(square)
                    break
                moves.append(square)
            for x, y in zip(range(self.cord[0] + 1, 8), range(self.cord[2] - 1, -1, -1)):
                square = board.get_square((x, y))
                if square.piece:
                    if not square.piece.color == self.color:
                        moves.append(square)
                    break
                moves.append(square)
            for x, y in zip(range(self.cord[0] - 1, -1, -1), range(self.cord[2] + 1, 8)):
                square = board.get_square((x, y))
                if square.piece:
                    if not square.piece.color == self.color:
                        moves.append(square)
                    break
                moves.append(square)
        return moves
