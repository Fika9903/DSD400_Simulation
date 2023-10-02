## environment.py
import random

class Environment:
    def __init__(self, food_availability: int, predator_count: int):
        self.food_availability = food_availability
        self.predator_count = predator_count

    def change_conditions(self):
        """Simulate changing conditions by randomly adjusting food availability and predator count."""
        self.food_availability = self._adjust_property(self.food_availability)
        self.predator_count = self._adjust_property(self.predator_count)

    @staticmethod
    def _adjust_property(property_value: int) -> int:
        """Adjust a property by a random value and ensure it does not go below 0."""
        property_value += random.randint(-5, 5)
        return max(0, property_value)
