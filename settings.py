class Settings():
    """A class to store all the settings of the game Alien Invasion """

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (200, 200, 200)
        # how fast the ship will move here 2 means 2 pixel at a time.
        self.ship_speed_factor = 2
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents righr and -1 represents left.
        self.fleet_direction = 1
        self.ship_limit = 3
