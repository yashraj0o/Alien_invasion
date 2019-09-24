import sys
import pygame
from rpg_s import Rpg


def keydown_events(event, g_settings, screen, roc, bullets):
    """Respond to key presses."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            roc.moving_right = True
        elif event.key == pygame.K_LEFT:
            roc.moving_left = True
        elif event.key == pygame.K_UP:
            roc.moving_up = True
        elif event.key == pygame.K_DOWN:
            roc.moving_down = True
        elif event.type == pygame.K_SPACE:
            # Create a new RPG and add it to Group.
            new_rpg = Rpg(g_settings, screen, roc)
            bullets.add(new_rpg)


def keyup_events(event, roc):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            roc.moving_right = False
        elif event.key == pygame.K_LEFT:
            roc.moving_left = False
        elif event.key == pygame.K_UP:
            roc.moving_up = False
        elif event.key == pygame.K_DOWN:
            roc.moving_down = False


def check_events(g_settings, screen, roc, bullets):
    """Watch for keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, g_settings, screen, roc, bullets)
        elif event.type == pygame.KEYUP:
            keyup_events(event, roc)


def update_screen(g_settings, screen, roc, bullets):
    # Redraw the screen during each pass through the loop
    screen.fill(g_settings.bg_color)
    # Redraw all the rpgs behind the ship.
    for bullet in bullets.sprites():
        bullet.draw_rpg()
    roc.blitme()
    # Make the most recent drawn screen visible.
    pygame.display.flip()
