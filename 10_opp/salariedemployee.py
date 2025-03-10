# salariedemployee.py
"""SalariedEmployee """
from decimal import Decimal

class SalariedEmployee:
    """An employee who get paid a fixed weekly salary."""

    def __init__(self, first_name, last_name, ssn, salary):
        """Initialize SalariedEmployee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self._salary = salary

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        """Set weekly salary or raise ValueError if invalid."""
        if salary < Decimal('0.00'):
            raise ValueError('Salary must be >= 0.00')

        self._salary = salary

    def earnings(self):
        """Calculate earnings."""
        return self.salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('Salaried Employee: ' + f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' + f'salary: {self.salary:.2f}\n')
