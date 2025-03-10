# savingsaccount.py
"""SavingsAccount derived from Account"""

from account import Account
from decimal import Decimal

class SavingsAccount(Account):
    """An account which earns interest on savings."""

    def __init__(self, name, balance, interest_rate):
        """Initialize the account."""
        super().__init__(name, balance)
        self._interest_rate = interest_rate # validate via property

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Set the interest rate."""
        if interest_rate < 0 or interest_rate > 1:
            raise ValueError("Interest rate must be >= 0 and <= 1")

        self._interest_rate = interest_rate

    def calculate_interest(self):
        """Calculate the interest generated."""
        return Decimal(self.balance * self.interest_rate)

    def __repr__(self):
        """Return a string representation of the saving account."""
        return f'Saving ' + super().__repr__() + f', interest_rate={self.interest_rate*100}%'