from board.board import Board
from board.square import Square
from .piece import Piece


class Pawn(Piece):
    symbol = 'p'
    initial = True
    en_passant = False

    def possible_moves(self, board: Board) -> list:
        moves = []
        x = self.cord[0]
        y = self.cord[1]
        square = board.get_square((x, y + 1))
        if not square.piece:
            moves.append(square)
        if self.initial:
            square = board.get_square((x, y + 2))
            if not square.piece:
                moves.append(square)
        moves.append(self.get_attack_moves(board))
        return moves

    def get_attack_moves(self, board: Board) -> list:
        moves = []
        # diagonal attack
        square = board.get_square((self.cord[0] + 1, self.cord[1] + 1))
        if square.piece and square.piece.color != self.color:
            moves.append(square)
        square = board.get_square((self.cord[0] - 1, self.cord[1] + 1))
        if square.piece and square.piece.color != self.color:
            moves.append(square)
        # en passant
        square = board.get_square((self.cord[0] + 1, self.cord[1]))
        if square.piece and square.piece.color != self.color and square.piece.symbol == 'p' and square.piece.en_passant:
            moves.append(square)
        square = board.get_square((self.cord[0] - 1, self.cord[1]))
        if square.piece and square.piece.color != self.color and square.piece.symbol == 'p' and square.piece.en_passant:
            moves.append(square)
        return moves

    def move(self, board: Board, target: Square) -> bool:
        self.cord = target.cord
        return True


# TODO: this is a sample of async await for promotion
# async def a():
#     return input('input: ')
#
# async def mmd():
#     x = await a()
#     print('hi')
#     return x
#
# import asyncio
#
#
# print(asyncio.run(mmd()))