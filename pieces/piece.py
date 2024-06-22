class Piece:
    symbol = ''

    def __init__(self, color, cord):
        self.color = color
        self.cord = cord
        self.image = None

    def possible_moves(self, board) -> list:
        return []

    def valid_moves(self, board):
        return list(set(self.possible_moves(board)).intersection(board.valid_moves()))

    def move(self, board, target):
        return None


