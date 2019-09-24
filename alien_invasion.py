import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.screen_width, g_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(g_settings, screen)
    # Make a group of bullets and aliens in.
    bullets = Group()
    aliens = Group()

    # Create fleet of aliens.
    gf.create_fleet(g_settings, screen, ship, aliens)

    # Make an alien.
    alien = Alien(g_settings, screen)

    # Create an instance to store game stats.
    stats = GameStats(g_settings)

    # Start the main loop for the game.
    while True:
        gf.check_events(g_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(g_settings, screen, ship, aliens, bullets)
            gf.update_aliens(g_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(g_settings, screen, ship, aliens, bullets)


run_game()
