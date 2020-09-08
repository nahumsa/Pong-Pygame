import pygame
from random import randint

black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    """Creates the ball class.
    """

    def __init__(self, color, width, height):
        """Pong ball.

        Args:
            color (tuple): color for the paddle.
            width (int): widht of the paddle.
            height (int): height of the paddle.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Create a random velocity
        self.velocity = [randint(4,8), randint(-8,8)] 

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]