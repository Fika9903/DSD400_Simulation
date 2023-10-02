## game_state.py
class GameState:
    def __init__(self, organism, environment):
        self.game_over = False
        self.organism = organism
        self.environment = environment

    def update_state(self):
        """Update the game state based on the organism and environment conditions."""
        # Update organism and environment
        self.organism.mutate()
        self.environment.change_conditions()

        # Check if the game is over
        if not self.organism.is_alive:
            self.game_over = True

    def reset_game(self):
        """Reset the game state to its initial conditions."""
        self.game_over = False
        self.organism = None
        self.environment = None
