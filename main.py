import pygame
from board.board import Board


# color = (3, 255, 0)
# pygame.draw.rect(screen, (186, 202, 69), rect)
class Game:

    def __init__(self, board, screen_size=600):
        pygame.init()
        pygame.init()
        self.screen_size = 600
        self.square_size = self.screen_size / 8
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.board = board
        self.screen.fill("white")
        for square in self.board.squares:
            color = (240, 217, 181) if square.color == 'white' else (181, 136, 99)
            rect = pygame.Rect(square.cord[0] * self.square_size, square.cord[1] * self.square_size, self.square_size, self.square_size)
            pygame.draw.rect(self.screen, color, rect)
            if square.piece:
                image = pygame.image.load(square.piece.image)
                image = pygame.transform.scale(image, (self.square_size, self.square_size))
                image_rect = image.get_rect()
                image_rect.center = rect.center
                self.screen.blit(image, image_rect)
        pygame.display.update()

    def handel_click(self, event):
        if self.board.selected_piece:
            ...
        else:
            cord = (event.pos[0] // self.square_size, event.pos[1] // self.square_size)
            square = self.board.get_square(cord)
            if square.piece and square.piece.color == self.board.turn:
                square.selected = True
                self.board.selected_piece = square.piece
                color = (3, 255, 0)
                rect = pygame.Rect(square.cord[0] * self.square_size, square.cord[1] * self.square_size,
                                   self.square_size, self.square_size)
                pygame.draw.rect(self.screen, color, rect)
                image = pygame.image.load(square.piece.image)
                image = pygame.transform.scale(image, (self.square_size, self.square_size))
                image_rect = image.get_rect()
                image_rect.center = rect.center
                self.screen.blit(image, image_rect)
                pygame.display.update()


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