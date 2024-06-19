import pygame
from board.board import Board

pygame.init()
SCREEN_SIZE = 600
SQUARE_SIZE = SCREEN_SIZE / 8
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
running = True
board = Board()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    for square in board.squares:
        color = (240, 217, 181) if square.color == 'white' else (181, 136, 99)
        rect = pygame.Rect(square.cord[0] * SQUARE_SIZE, square.cord[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, color, rect)
        if square.piece:
            image = pygame.image.load(square.piece.image)
            image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            image_rect = image.get_rect()
            image_rect.center = rect.center
            screen.blit(image, image_rect)

    # RENDER YOUR GAME HERE
    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()