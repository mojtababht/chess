class Piece:
    symbol = ''

    def __init__(self, color, cord):
        self.color = color
        self.cord = cord
        self.image = None

    def possible_moves(self, board) -> set:
        return set()

    def valid_moves(self, board):
        valid_moves = set()
        for piece, moves in board.valid_moves():
            if piece == self:
                return moves
        return valid_moves

    def move(self, board, target):
        return None
