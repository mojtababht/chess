from functools import lru_cache


class Piece:
    symbol = ''

    def __init__(self, color, cord):
        self.color = color
        self.cord = cord
        self.image = None

    def possible_moves(self, board) -> set:
        return set()

    @lru_cache
    def valid_moves(self, board):
        valid_moves = set()
        self_square = board.get_square(self.cord)
        for square in self.possible_moves(board):
            if board.fake_move(self_square, square):
                valid_moves.add(square)
        return valid_moves

    def move(self, board, target):
        return None

    def __str__(self):
        return self.symbol
