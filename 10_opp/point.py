# point.py
"""Class point"""

import math

class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def distance(self):
        """Calculate the distance from the origin"""
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"({self.x}, {self.y})"
