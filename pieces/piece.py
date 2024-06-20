class Piece:
    symbol = ''

    def __init__(self, color, cord):
        self.color = color
        self.cord = cord
        self.image = None

    def possible_moves(self, board) -> list:
        return []

    def valid_moves(self, board):
        moves = []
        for move in self.possible_moves(board):
            if move in board.valid_moves():
                moves.append(move)
        return moves

    def move(self, board, target):
        return None


