# SalariedEmployee.py
"""SalariedCommissionEmployee derived from Employee."""
from Employee import Employee

class SalariedEmployee(Employee):
    """An employee who gets paid a fix weekly salary."""
    def __init__(self, first_name, last_name, ssn, weekly_salary):
        """Initialize SalariedCommissionEmployee's attributes."""
        super().__init__(first_name, last_name, ssn)
        self.weekly_salary = weekly_salary # validate via property

    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary must be positive.")

        self._weekly_salary = salary

    def earnings(self):
        """Calculate the employee's earnings."""
        return self.weekly_salary

    def __repr__(self):
        return (f'SalariedEmployee: ' + super().__repr__() + f'\nWeekly salary: ${self.weekly_salary}')
