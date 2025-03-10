# vector.py
"""Vector class"""

import math
from point import Point

class Vector:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def magnitude(self):
        """Calculate the magnitude of the vector"""
        return math.sqrt((self.end.x-self.start.x) ** 2 + (self.end.y-self.start.y) ** 2)

    def __repr__(self):
        return (f"Vector(start={self.start}, end={self.end})\n"
                f"magnitude={self.magnitude():.2f}")