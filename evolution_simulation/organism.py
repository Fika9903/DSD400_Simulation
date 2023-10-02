## organism.py
import random

class Organism:
    def __init__(self, species: str, health: int, speed: int, strength: int):
        self.species = species
        self.health = health
        self.speed = speed
        self.strength = strength
        self.is_alive = True

    def mutate(self):
        """Simulate a mutation by randomly changing one of the organism's properties."""
        mutation_choice = random.choice(['health', 'speed', 'strength'])
        mutation_value = random.randint(-5, 5)
        
        if mutation_choice == 'health':
            self.health += mutation_value
        elif mutation_choice == 'speed':
            self.speed += mutation_value
        elif mutation_choice == 'strength':
            self.strength += mutation_value

        # Ensure properties do not go below 0
        self.health = max(0, self.health)
        self.speed = max(0, self.speed)
        self.strength = max(0, self.strength)

        # Check if the organism is still alive
        if self.health == 0:
            self.is_alive = False

    def reproduce(self):
        """Simulate reproduction by creating a new organism with similar properties."""
        child_health = max(0, self.health + random.randint(-5, 5))
        child_speed = max(0, self.speed + random.randint(-5, 5))
        child_strength = max(0, self.strength + random.randint(-5, 5))

        return Organism(self.species, child_health, child_speed, child_strength)
