from board.board import Board
from board.square import Square


class Piece:
    symbol = ''

    def __init__(self, color, cord):
        self.color = color
        self.cord = cord

    def possible_moves(self, board: Board) -> list:
        return []

    def move(self, board: Board, target: Square):
        return None


