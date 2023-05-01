import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets."""

    def __init__(self, ss_game):
        """Create a bullet object at the ship's current position."""
        # call super() to inherit from Sprite
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midleft = ss_game.ship.ship_rect.midleft

        # Store the bullets position as a float.
        self.x = float(self.bullet_rect.x) 

    def update(self):
        """Move the bullet across the screen."""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position
        self.bullet_rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)