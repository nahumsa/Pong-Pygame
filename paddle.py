import pygame

black = (50,50,50)

class Paddle(pygame.sprite.Sprite):
    """Class for the pong paddle.    
    """
    def __init__(self, color, width, height):
        """Pong paddle.

        Args:
            color (tuple): color for the paddle.
            width (int): widht of the paddle.
            height (int): height of the paddle.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0,0,width, height])

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        """Method to move the paddle up.

        Args:
            pixels (int): Number of pixels that we want to move.
        """
        
        self.rect.y -= pixels

        # Correct if the paddle is off-screen
        if self.rect.y < 0:
            self.rect.y = 0
    
    def move_down(self, pixels):
        """Method to move the paddle down.

        Args:
            pixels (int): Number of pixels that we want to move.
        """

        self.rect.y += pixels

        # Correct if the paddle is off-screen
        if self.rect.y > 400:
            self.rect.y = 400