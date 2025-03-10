from enum import Enum, auto
from functools import total_ordering

# Define an Enum for card faces
class CardFace(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

# Define an Enum for card suits
class CardSuit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()

@total_ordering
class Card:
    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        if not isinstance(face, CardFace):
            raise ValueError("face must be a CardFace enum.")
        if not isinstance(suit, CardSuit):
            raise ValueError("suit must be a CardSuit enum.")

        self._face = face
        self._suit = suit
        self._front = True  # 1 shows the front of the card, 0 shows the back

    @property
    def face(self):
        """Return the card's face."""
        return self._face

    @property
    def suit(self):
        """Return the card's suit."""
        return self._suit

    @property
    def image_name(self):
        """Return the card's image file name."""
        return str(self).replace(' ', '_') + '.png' if self._front else 'back_of_card.png'

    def black_jack_value(self):
        """Return card's value for Black Jack scoring."""
        if not self._front:
            return 0  # return 0 if the card is face-down

        if self.face in [CardFace.JACK, CardFace.QUEEN, CardFace.KING]:
            return 10

        elif self.face == CardFace.ACE:
            return 1  # ace will be treated as one for now and will be adjusted as needed

        else:
            # Convert face to integer value (e.g., CardFace.TWO -> 2)
            return self.face.value

    def __repr__(self):
        """Return string representation for repr()."""
        if self._front:
            return f"Card(face={self.face.name}, suit={self.suit.name})"
        else:
            return "Card(face='*****', suit='*****')"

    def __str__(self):
        """Return string representation for str()."""
        if self._front:
            return f'{self.face.name.lower()} of {self.suit.name.lower()}'
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
        # Compare based on the face's value (order in the enum)
        return self.face.value < other.face.value