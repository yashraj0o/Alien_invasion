class Settings():
    """A class to store the settings of the game."""

    def __init__(self):
        """Initialize the game's settings. """
        # screen settings
        self.screen_width = 1480
        self.screen_height = 800
        self.bg_color = (130, 130, 130)
        # how fast the ship will move here 2 means 2 pixel at a time.
        self.ship_speed_factor = 2
        # Bullet settings
        self.rpg_speed_factor = 1
        self.rpg_width = 3
        self.rpg_height = 15
        self.rpg_color = 60, 60, 60
        self.rpg_allowed = 3
