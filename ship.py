import pygame


class Ship():
    """loading the ship image and setting the starting position of ship on screen"""

    def __init__(self, g_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.g_settings = g_settings

        # Load ship and get its rect.
        self.image = pygame.image.load("Images/spaceship_1.PNG")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating the ship's position based on the movement flag."""
        # Update the ships center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.g_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.g_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
