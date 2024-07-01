from pathlib import Path
from .piece import Piece

images_path = Path().parent.joinpath('imgs')

class Bishop(Piece):
    symbol = 'b'

    def __init__(self, color, cord):
        super().__init__(color, cord)
        self.image = images_path.joinpath('w_bishop.png') if color == 'white' else images_path.joinpath('b_bishop.png')

    def possible_moves(self, board) -> list:
        moves = set()
        for x, y in zip(range(self.cord[0] + 1, 8), range(self.cord[1] + 1, 8)):
            square = board.get_square((x, y))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.add(square)
                break
            moves.add(square)
        for x, y in zip(range(self.cord[0] - 1, -1, -1), range(self.cord[1] - 1, -1, -1)):
            square = board.get_square((x, y))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.add(square)
                break
            moves.add(square)
        for x, y in zip(range(self.cord[0] + 1, 8), range(self.cord[1] - 1, -1, -1)):
            square = board.get_square((x, y))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.add(square)
                break
            moves.add(square)
        for x, y in zip(range(self.cord[0] - 1, -1, -1), range(self.cord[1] + 1, 8)):
            square = board.get_square((x, y))
            if square.piece:
                if not square.piece.color == self.color:
                    moves.add(square)
                break
            moves.add(square)
        return moves

    def move(self, board, target):
        self.cord = target.cord
        return self
