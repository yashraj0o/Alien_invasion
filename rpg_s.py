import pygame
from pygame.sprite import Sprite


class Rpg(Sprite):
    """  A class to manage rpg fired from ship."""

    def __init__(self, g_settings, screen, roc):
        """Create RPG object at the ships current position."""
        super(Rpg, self).__init__()
        self.screen = screen

        # Create a RPG rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, g_settings.rpg_width, g_settings.rpg_height)
        self.rect.centerx = roc.rect.centerx
        self.rect.top = roc.rect.top
        """self.rect.top = roc.rect.right"""

        # Store the RPG's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = g_settings.rpg_color
        self.speed_factor = g_settings.rpg_speed_factor

    def update(self):
        """Move the RPG right across the screen."""
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_rpg(self):
        """Draw RPG to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
