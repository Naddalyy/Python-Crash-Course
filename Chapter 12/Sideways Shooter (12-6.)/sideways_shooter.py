import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializes the game and creates game recources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        """Responds to keypresses."""
        if event.key == pygame.K_UP:
            # Move the ship up.
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the ship down.
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            # Close the game on ESCAPE.
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up(self, event):
        """Responds to keyreleases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """Updates images on the screen, and flips it to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Make the most recently drawn screen visable. 
        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets."""
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that have disappeared. 
        for bullet in self.bullets.copy():
            print(len(self.bullets))
            if bullet.bullet_rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)


sidewayshooter = SidewaysShooter()
sidewayshooter.run_game()