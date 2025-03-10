# cardtotalordering.py
"""Card class that represents a playing card and its image file name."""
from functools import total_ordering

@total_ordering
class Card:
    FACES = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    SUITS = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit
        self._front = True  # 1 shows the front of the card, 0 shows the back

    @property
    def face(self):
        """Return the card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the card's self._suit value."""
        return self._suit

    @property
    def image_name(self):
        """Return the card's image file name."""
        return str(self).replace(' ', '_') + '.png' if self._front else 'back_of_card.png'

    def black_jack_value(self):
        """Return card's value for Black Jack scoring."""
        if not self._front:
            return 0  # return 0 if the card is face-down

        if self.face in ['jack', 'queen', 'king']:
            return 10

        elif self.face == 'ace':
            return 1  # ace will be treated as one for now and will be adjusted as needed

        else:
            return int(self.face)

    def __repr__(self):
        """Return string representation for repr()."""
        if self._front:
            return f"Card(face='{self.face}', suit='{self.suit}')"
        else:
            return f"Card(face='*****', suit='*****')"

    def __str__(self):
        """Return string representation for str()."""
        if self._front:
            return f'{self.face} of {self.suit}'
        else:
            return '*****'

    def __format__(self, format):
        """Return formatted string representation for str()."""
        return f'{str(self):{format}}'

    def __eq__(self, other):
        """Return True if self == other."""
        if not isinstance(other, Card):
            return NotImplemented
        return self.face == other.face and self.suit == other.suit

    def __lt__(self, other):
        """Return True if self < other."""
        if not isinstance(other, Card):
            return NotImplemented
        # compare based on the index in the FACES list
        return self.FACES.index(self.face) < self.FACES.index(other.face)