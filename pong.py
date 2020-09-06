# This code is based on the tutorial:
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

import pygame
pygame.init()

# Creating colors using RGB
pink = (188, 42, 209)
black = (0, 0, 0)

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Defining frame rate
frame_rate = 60

# Variable for finishing the game
is_finished = False

# Clock is used to control screen update
clock = pygame.time.Clock()

while not is_finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished = True

    # Drawing background
    screen.fill(black)

    pygame.draw.line(screen, pink, [size[0]/2 - 1, 0], [size[0]/2 - 1, size[1]], 5)

    pygame.display.flip()
    
    # Set the frame rate for 60 seconds
    clock.tick(frame_rate)

pygame.quit()