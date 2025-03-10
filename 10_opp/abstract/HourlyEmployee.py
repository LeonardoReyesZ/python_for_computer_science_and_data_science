# HourlyEmployee.py
"""HourlyEmployee derived from Employee."""
from Employee import Employee

class HourlyEmployee(Employee):
    """An employee who gets paid per hour, also receives overtime pay."""
    def __init__(self, first_name, last_name, ssn, hours, wages):
        super().__init__(first_name, last_name, ssn)
        self.hours = hours # validate via property
        self.wages = wages # validate via property

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        if hours < 0 or hours > 168:
            raise ValueError('hours must be in range (0-168')

        self._hours = hours

    @property
    def wages(self):
        return self._wages

    @wages.setter
    def wages(self, wages):
        if wages < 0:
            raise ValueError('wages must be positive.')

        self._wages = wages

    def earnings(self):
        """Calculate the employee's earnings."""
        if self.hours <= 40:
            return self.hours * self.wages

        elif self.hours > 40:
            return self.wages*40 + ((self.hours - 40) * (self.wages * 1.5))

    def __repr__(self):
        return (f'HourlyEmployee: ' + super().__repr__() + f'\nHours worked: {self.hours}\nWages: {self.wages}')