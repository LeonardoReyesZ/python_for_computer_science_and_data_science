# car.py
"""Car class"""

class Car:
    def __init__(self, model, year, speed=0):
        """Initialize car class"""
        self._model = model
        self._year = year
        self._speed = speed

    @property
    def model(self):
        """Return the car's self._model value."""
        return self._model

    @property
    def year(self):
        """Return the car's self._year value."""
        return self._year

    @property
    def speed(self):
        """Return the car's self._speed value."""
        return self._speed

    def accelerate(self, increment):
        """method to drive the car faster"""
        if increment > 0:
            print("accelerating...")
            self._speed += increment
        else:
            print('speed increment must be positive')

    def decelerate(self, decrement):
        """method to drive the car slower"""
        if decrement > 0 and self._speed - decrement >= 0:
            print('decelerating..')
            self._speed -= decrement
        else:
            print('speed decrement must be positive and not exceed current speed.')

    def __str__(self):
        """Return a string representation of the car"""
        return f'Model: {self.model}\nYear: {self.year}\nSpeed: {self.speed} km/h'