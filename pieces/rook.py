from pathlib import Path

from .piece import Piece


images_path = Path().parent.joinpath('imgs')


class Rook(Piece):
    symbol = 'r'
    moved = False

    def __init__(self, color, cord):
        super().__init__(color, cord)
        self.image = images_path.joinpath('w_rook.png') if color == 'white' else images_path.joinpath('b_rook.png')

    def possible_moves(self, board) -> list:
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

    def move(self, board, target):
        self.cord = target.cord
        self.moved = True
        return self
