import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, g_settings, screen, ship, bullets):
    """Respond to keypress."""
    if event.key == pygame.K_RIGHT:
        # making movement flag True in this if block
        ship.moving_right = True
        # So when right arrow key is pressed movement flag is made True for continuous motion
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(g_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullets(g_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < g_settings.bullets_allowed:
        new_bullet = Bullet(g_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(g_settings, alien_width):
    """Determine the number of aliens that fit in a row. """
    alien2_width = 2 * alien_width
    available_space_x = g_settings.screen_width - alien2_width
    number_aliens_x = int(available_space_x / alien2_width)
    return number_aliens_x


def get_number_rows(g_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on screen."""
    available_space_y = (g_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(g_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row."""
    alien = Alien(g_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(g_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create aliens and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(g_settings, screen)
    number_aliens_x = get_number_aliens_x(g_settings, alien.rect.width)
    number_rows = get_number_rows(g_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(g_settings, screen, aliens, alien_number, row_number)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(g_settings, screen, ship, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, g_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(g_settings, screen, ship, aliens, bullets):
    # Redraw the screen during each pass through the loop
    screen.fill(g_settings.bg_color)
    # Redraw all the bullets behind from the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(g_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullets.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(g_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(g_settings, screen, ship, aliens, bullets):
    """Respond to bullet alien collisions."""
    # Check for any bullets that have hit aliens.
    # If so then remove that bullet and that alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        """Destroy existing bullets and create new fleet."""
        bullets.empty()
        create_fleet(g_settings, screen, ship, aliens)


def ship_hit(g_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        """Decrement ships_left."""
        stats.ships_left -= 1
        """Empty the list of aliens and bullets."""
        aliens.empty()
        bullets.empty()

        # Create new fleet and ship.
        create_fleet(g_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False


def update_aliens(g_settings, stats, screen, ship, aliens, bullets):
    """Check if the fleet is at edge, and then Update the positions of the fleet of aliens."""
    check_fleet_edges(g_settings, aliens)
    aliens.update()

    # look for alien ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(g_settings, stats, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_alien_bottom(g_settings, stats, screen, ship, aliens, bullets)
    check_alien_bottom(g_settings, stats, screen, ship, aliens, bullets)


def check_alien_bottom(g_settings, stats, screen, ship, aliens, bullets):
    """Check if any alien hit the ground."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(g_settings, stats, screen, ship, aliens, bullets)
            break


def check_fleet_edges(g_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(g_settings, aliens)
            break


def change_fleet_direction(g_settings, aliens):
    """Change the direction of the fleet and drop the entire fleet."""
    for alien in aliens.sprites():
        alien.rect.y += g_settings.fleet_drop_speed
    g_settings.fleet_direction *= -1
