import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, g_settings, screen, ship):
        """Create the bullet at ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, g_settings.bullet_width, g_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullets position as decimal value.
        self.y = float(self.rect.y)

        self.color = g_settings.bullet_color
        self.speed_factor = g_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
