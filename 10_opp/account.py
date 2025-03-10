# account.py
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise and exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00.')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise and exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""

        # if amount is grater than the balance, raise and exception
        if amount > self.balance:
            raise ValueError("amount must be <= to balance.")
        elif amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance -= amount

    def __repr__(self):
        """Return a string representation of the account."""
        return f'Account: name={self.name}, balance={self.balance}'