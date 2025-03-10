# player.py
"""Class player"""

from decimal import Decimal
import random

class Player:

    def __init__(self, name, level=0, strength=0, health_points=Decimal('0.00') ):
        self._name = name
        self._level = level
        self._strength = strength
        self._health_points = health_points

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level < 0:
            raise ValueError("Level must be positive.")

        self._level = level

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, health_points):
        if health_points < 0:
            raise ValueError("Health points must be positive.")

        self._health_points = health_points

    def defence(self, attacker):
        intensity = (attacker.strength / random.randint(1,3)) - (self.strength * self.level)

        if intensity <= 0:
            self._health_points -= abs(intensity)
            if self.health_points < 0:
                self._health_points = Decimal('0')
                return f"{self.name} has been defeated."

            return f"{self.name} was hit! health is now {self.health_points:.2f}"

        return f"{self.name} successfully defended the attack!"