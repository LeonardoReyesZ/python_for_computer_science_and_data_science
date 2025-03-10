# Employee.py
"""Employee abstract class."""
from abc import ABC, abstractmethod

class Employee(ABC):
    """An employee abstract class."""
    def __init__(self, first_name, last_name, ssn):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @abstractmethod
    def earnings(self):
        raise NotImplementedError("Subclasses must implement the 'earnings' method.")

    def __repr__(self):
        return (f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self._ssn}')