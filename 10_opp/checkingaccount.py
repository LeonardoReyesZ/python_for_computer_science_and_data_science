# checkingaccount.py
"""CheckingAccount derived from Account"""

from account import Account
from decimal import Decimal

class CheckingAccount(Account):
    """An account that charges a fee for each transaction."""

    def __init__(self, name, balance, fee):
        super().__init__(name, balance)
        self._fee = fee # validate via property

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Set the fee for each transaction."""
        if fee < 0 or fee > 1:
            raise ValueError("Fee must be >= 0 and <= 1")

        self._fee = fee

    def deposit(self, amount):
        """Deposit money to the account cnd charge a fee for the transaction."""
        if amount < Decimal('0.00'):
            raise ValueError("amount must be positive")

        self.balance += amount - amount*self.fee

    def withdraw(self, amount):
        """Withdraw money from the account and charge a fee fo the transaction."""
        if amount < 0:
            raise ValueError("amount must be positive.")

        elif amount+(amount*self.fee) > self.balance:
            raise ValueError("amount must not exceed the balance.")

        self.balance -= amount + amount*self.fee

    def __repr__(self):
        """Return a string representation of the checking account."""
        return f'Checking ' + super().__repr__() + f', fee={self.fee*100}%'