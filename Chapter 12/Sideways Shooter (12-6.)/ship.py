import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ss_game):
        """Initializes the ship and sets its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Loading the ship image, getting its rect
        self.ship_image = pygame.image.load('images/ship.bmp')
        self.ship_rect = self.ship_image.get_rect()

        # Start each new ship on the left center of the screen
        self.ship_rect.centery = self.screen_rect.centery

        # Movement flag
        self.moving_up = False
        self.moving_down = False

        # Storing the position of the ship in a float
        self.y = float(self.ship_rect.y) 

    def update(self):
        """Update the ships position based on a movement flag."""
        if self.moving_up and self.ship_rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Updating rect object from self.y
        self.ship_rect.y = self.y

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.ship_image, self.ship_rect)