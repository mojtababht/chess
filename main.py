import pygame
from board.board import Board


# color = (3, 255, 0)
# pygame.draw.rect(screen, (186, 202, 69), rect)
class Game:

    def __init__(self, board, screen_size=600):
        pygame.init()
        self.screen_size = screen_size
        self.square_size = self.screen_size / 8
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.board = board
        self.screen.fill("white")
        self.draw_rect_for_squares(*self.board.squares)
        pygame.display.update()

    def draw_rect_for_squares(self, *squares):
        for square in squares:
            color = (240, 217, 181) if square.color == 'white' else (181, 136, 99)
            rect = self.draw_rect(square.cord, color)
            if square.piece:
                self.blit_image(square.piece, rect)

    def highlight_squares(self, *squares):
        for square in squares:
            if square.piece:
                color = (236, 122, 96)
                rect = self.draw_rect(square.cord, color)
                self.blit_image(square.piece, rect)
            else:
                if square.color == 'black':
                    color = (182, 198, 65)
                else:
                    color = (200, 214, 80)
                self.draw_rect(square.cord, color)


    def handel_click(self, event):
        cord = (event.pos[0] // self.square_size, event.pos[1] // self.square_size)
        square = self.board.get_square(cord)
        if selected_piece := self.board.selected_piece:
            if square in selected_piece.valid_moves(self.board):
                valid_moves = selected_piece.valid_moves(self.board) # this for re drawing marked pieces not all of them
                selected_square = self.board.get_square(selected_piece.cord)
                self.board.move(selected_square, square)
                self.draw_rect_for_squares(selected_square, square, *valid_moves)
                pygame.display.update()
            else:
                old_selected_square = self.board.get_square(selected_piece.cord)
                self.draw_rect_for_squares(*selected_piece.valid_moves(self.board), old_selected_square)
                if square.piece and square.piece.color == self.board.turn:
                    square.selected = True
                    self.board.selected_piece = square.piece
                    rect = self.draw_rect(square.cord, (3, 255, 0))
                    self.blit_image(square.piece, rect)
                    self.highlight_squares(*square.piece.valid_moves(self.board))
                self.board.selected_piece = square.piece
                old_selected_square.selected = False
        else:
            if square.piece and square.piece.color == self.board.turn:
                square.selected = True
                self.board.selected_piece = square.piece
                rect = self.draw_rect(square.cord, (3, 255, 0))
                self.blit_image(square.piece, rect)
                self.highlight_squares(*square.piece.valid_moves(self.board))
                pygame.display.update()

    def blit_image(self, piece, rect):
        image = pygame.image.load(piece.image)
        image = pygame.transform.scale(image, (self.square_size, self.square_size))
        image_rect = image.get_rect()
        image_rect.center = rect.center
        self.screen.blit(image, image_rect)

    def draw_rect(self, cord, color):
        rect = pygame.Rect(cord[0] * self.square_size, cord[1] * self.square_size,
                           self.square_size, self.square_size)
        pygame.draw.rect(self.screen, color, rect)
        return rect




running = True
board = Board()
game = Game(board)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handel_click(event)


    pygame.display.flip()


pygame.quit()