# This code is based on the tutorial:
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

import pygame
from paddle import Paddle

pygame.init()

# Creating colors using RGB
pink = (188, 42, 209)
black = (0, 0, 0)

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Creating players' paddles
pos_paddle_x = 20

paddleA = Paddle(pink, 10, 100)
paddleA.rect.x = pos_paddle_x
paddleA.rect.y = 200

paddleB = Paddle(pink, 10, 100)
paddleB.rect.x = size[0] - pos_paddle_x
paddleB.rect.y = 200

# Adding sprites
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(paddleA)
all_sprite_list.add(paddleB)

# Variable for finishing the game
is_finished = False

# Clock is used to control screen update
clock = pygame.time.Clock()

while not is_finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_finished = True

    # Game Logic
    # Moving paddles with keyboard keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    if keys[pygame.K_UP]:
        paddleB.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB.move_down(5)

    # Add sprites
    all_sprite_list.update()    
    

    # Drawing background
    screen.fill(black)

    pygame.draw.line(screen, pink, [size[0]/2 - 1, 0], [size[0]/2 - 1, size[1]], 5)

    # Draw sprites
    all_sprite_list.draw(screen)

    pygame.display.flip()    

    

    # Set the frame rate for 60 seconds
    clock.tick(60)

pygame.quit()