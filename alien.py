import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, g_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.g_settings = g_settings

        # load the alien image and set its rect attribute.
        self.image = pygame.image.load('Images/alien.BMP')
        self.rect = self.image.get_rect()

        # Start Each new alien near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien to right."""
        self.x += (self.g_settings.alien_speed_factor*
                   self.g_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


