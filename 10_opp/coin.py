# coin.py
"""Coin class"""

class Coin:
    def __init__(self, two_euro=0, one_euro=0, fifty_cent=0, twenty_cent=0, ten_cent=0):
        """Initialize coin class"""
        self._two_euro = two_euro
        self._one_euro = one_euro
        self._fifty_cent = fifty_cent
        self._twenty_cent = twenty_cent
        self._ten_cent = ten_cent

    @property
    def universal_str(self):
        """Return a string representation of the number of each coin"""
        return (f"2 Euro: {self._two_euro}\n"
                f"1 Euro: {self._one_euro}\n"
                f"50 cents: {self._fifty_cent}\n"
                f"20 cents: {self._twenty_cent}\n"
                f"10 cents: {self._ten_cent}" )

    def total_amount(self):
        """Return the total amount of money"""
        return (self._two_euro*2 + self._one_euro + self._fifty_cent*0.5 + self._twenty_cent*0.20 + self._ten_cent*.10 )