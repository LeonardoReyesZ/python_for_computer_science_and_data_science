# complex.py
"""Frozen Complex class"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Complex:
    """Complex class that represents a complex number
    with real and imaginary parts."""

    real: float
    imaginary: float

    def __add__(self, right):
        """Overrides the + operator."""
        return Complex(self.real + right.real, self.imaginary + right.imaginary)

    def __sub__(self, right):
        """Overrides the - operator."""
        return Complex(self.real - right.real, self.imaginary - right.imaginary)

    def __repr__(self):
        """Return string representation for repr()."""
        return (f'({self.real} ' + ('+' if self.imaginary >= 0 else '-') +
                f' {abs(self.imaginary)}i)')