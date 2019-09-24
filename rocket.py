import pygame


class Rocket():

    def __init__(self,g_settings, screen):
        """Initialise rocket and set its starting position."""
        self.screen = screen
        self.g_settings = g_settings
        # Load the rocket image and get its rect.
        self.image = pygame.image.load("Images/spaceship_1.PNG")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start rocket at the bottom of the ship.
        """self.rect.bottom = self.screen_rect.left
        self.rect.bottom = self.screen_rect.centery"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Rocket speed factor.
        self.roc_speed = 1.5

        # Store decimal value for rocket.
        self.horizontal = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.horizontal += self.roc_speed
        if self.moving_left and self.rect.left > 0:
            self.horizontal -= self.roc_speed
        if self.moving_up and self.rect.top > 0:
            self.vertical -= self.roc_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.roc_speed
        # Update rect object from self.horizontal and self.vertical
        self.rect.centerx = self.horizontal
        self.rect.centery = self.vertical

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
