## ui.py
import pygame

class UI:
    def __init__(self, game_state):
        self.game_state = game_state
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        """Draw the game state on the screen."""
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw organism information
        organism_info = f"Species: {self.game_state.organism.species}, Health: {self.game_state.organism.health}, Speed: {self.game_state.organism.speed}, Strength: {self.game_state.organism.strength}"
        text = self.font.render(organism_info, True, (255, 255, 255))
        self.screen.blit(text, (20, 20))

        # Draw environment information
        environment_info = f"Food availability: {self.game_state.environment.food_availability}, Predator count: {self.game_state.environment.predator_count}"
        text = self.font.render(environment_info, True, (255, 255, 255))
        self.screen.blit(text, (20, 60))

        # Update the display
        pygame.display.flip()

    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.game_state.reset_game()
                    self.draw()  # Update the UI after resetting the game state
