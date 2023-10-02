## main.py
from organism import Organism
from environment import Environment
from game_state import GameState
from ui import UI
import time

def main():
    # Create an organism
    organism = Organism("Organism1", health=100, speed=10, strength=10)

    # Create an environment
    environment = Environment(food_availability=100, predator_count=5)

    # Create a game state
    game_state = GameState(organism, environment)

    # Create a UI
    ui = UI(game_state)
    update =0
    # Game loop
    while not game_state.game_over:
        ui.handle_events()
        if game_state.game_over:
            hej=input('')
            break
        game_state.update_state()
        update+=1
        if update%500 == 0:
            ui.draw()
            time.sleep(1)
        print(update)
        

    # Reset the game
    game_state.reset_game()

if __name__ == "__main__":
    main()
