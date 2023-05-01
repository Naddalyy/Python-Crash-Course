class Settings:
    """A class to manage the settings for Sideway Shooter."""

    def __init__(self):
        """Initiliaze the game settings."""
        # Screen settings
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3.5

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_speed = 5.0