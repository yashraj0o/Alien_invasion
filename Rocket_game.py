import roc_game_function
import pygame
from rocket import Rocket
from pygame.sprite import Group
from setttings_0 import Settings


def run_rocket():
    """Initialise game and create screen object."""
    pygame.init()
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.screen_width, g_settings.screen_height))
    pygame.display.set_caption("Rocket")

    # Make a rocket.
    roc = Rocket(g_settings, screen)
    # Make a group to store RPG.
    bullets = Group()

    while True:
        roc_game_function.check_events(g_settings, screen, roc, bullets)
        roc.update()
        bullets.update()
        roc_game_function.update_screen(g_settings, screen, roc, bullets)


run_rocket()
