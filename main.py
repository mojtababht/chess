import pygame
from board.board import Board
import datetime

pygame.init()
SCREEN_SIZE = 600
SQUARE_SIZE = SCREEN_SIZE / 8
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
running = True
board = Board()
screen.fill("white")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cord = (event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE)
            board.selected_piece = None
            for square in board.squares:
                square.selected = False
                if square.cord == cord:
                    if square.piece:
                        square.selected = True
                        board.selected_piece = square.piece

    # fill the screen with a color to wipe away anything from last frame

    for square in board.squares:
        color = (240, 217, 181) if square.color == 'white' else (181, 136, 99)
        if square.selected:
            color = (3, 255, 0)
        rect = pygame.Rect(square.cord[0] * SQUARE_SIZE, square.cord[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, color, rect)
        if square.piece:
            image = pygame.image.load(square.piece.image)
            image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            image_rect = image.get_rect()
            image_rect.center = rect.center
            screen.blit(image, image_rect)
        if square.selected:
            for moves in square.piece.possible_moves(board):
                rect = pygame.Rect(moves.cord[0] * SQUARE_SIZE, moves.cord[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, (186, 202, 69), rect)



    # RENDER YOUR GAME HERE
    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()