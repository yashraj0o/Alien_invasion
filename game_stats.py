class GameStats():
    """Track Statistics for Alien Invasion."""

    def __init__(self, g_settings):
        """Initialize statistics."""
        self.g_settings = g_settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.g_settings.ship_limit
