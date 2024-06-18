from board.board import Board
from board.square import Square
from . import Queen
from .piece import Piece


class Pawn(Piece):
    symbol = 'p'
    initial = True
    en_passant = False

    def possible_moves(self, board: Board) -> list:
        moves = []
        x = self.cord[0]
        y = self.cord[1]
        if self.color == 'white':
            square = board.get_square((x, y + 1))
            if not square.piece:
                moves.append(square)
            if self.initial:
                square = board.get_square((x, y + 2))
                if not square.piece:
                    moves.append(square)
        else:
            square = board.get_square((x, y - 1))
            if not square.piece:
                moves.append(square)
            if self.initial:
                square = board.get_square((x, y - 2))
                if not square.piece:
                    moves.append(square)
        moves.extend(self.get_attack_moves(board))
        return moves

    def get_attack_moves(self, board: Board) -> list:
        moves = []
        # diagonal attack
        if self.color == 'white':
            square = board.get_square((self.cord[0] + 1, self.cord[1] + 1))
            if square.piece and square.piece.color != self.color:
                moves.append(square)
            square = board.get_square((self.cord[0] - 1, self.cord[1] + 1))
            if square.piece and square.piece.color != self.color:
                moves.append(square)
            # en passant
            square = board.get_square((self.cord[0] + 1, self.cord[1]))
            if square.piece and square.piece.color != self.color and square.piece.symbol == 'p' and square.piece.en_passant:
                moves.append(board.get_square((self.cord[0] + 1, self.cord[1] + 1)))
            square = board.get_square((self.cord[0] - 1, self.cord[1]))
            if square.piece and square.piece.color != self.color and square.piece.symbol == 'p' and square.piece.en_passant:
                moves.append(board.get_square((self.cord[0] - 1, self.cord[1] + 1)))
        else:
            square = board.get_square((self.cord[0] + 1, self.cord[1] - 1))
            if square.piece and square.piece.color != self.color:
                moves.append(square)
            square = board.get_square((self.cord[0] - 1, self.cord[1] - 1))
            if square.piece and square.piece.color != self.color:
                moves.append(square)
            # en passant
            square = board.get_square((self.cord[0] + 1, self.cord[1]))
            if square.piece and square.piece.color != self.color and square.piece.symbol == 'p' and square.piece.en_passant:
                moves.append(board.get_square((self.cord[0] + 1, self.cord[1] - 1)))
            square = board.get_square((self.cord[0] - 1, self.cord[1]))
            if square.piece and square.piece.color != self.color and square.piece.symbol == 'p' and square.piece.en_passant:
                moves.append(board.get_square((self.cord[0] - 1, self.cord[1] - 1)))
        return moves

    def move(self, board: Board, target: Square):
        if self.initial:
            self.en_passant = True
        else:
            self.en_passant = False
        self.cord = target.cord
        self.initial = False
        if self.cord[1] == 7 or self.cord[1] == 0:
            return self.promotion()
        return self

    def promotion(self): # TODO: get actual choice from user later
        new_piece = Queen(self.color, self.cord)
        return new_piece


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