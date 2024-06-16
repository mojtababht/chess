from board.board import Board


class Piece:
    symbol = ''

    def __init__(self, color, cord):
        self.color = color
        self.cord = cord

    def possible_moves(self, board: Board) -> list:
        return []


