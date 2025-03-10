# deck.py
"""Deck class represents a deck of cards."""

import random
from card import Card

class DeckOfCards:
    NUMBER_OF_CARDS = 52 # constant number of cards

    def __init__(self):
        """Initialize the deck."""
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count%13], Card.SUITS[count//13]))

    def shuffle(self):
        """Shuffle deck."""
        random.shuffle(self._deck)

    def deal_card(self):
        """Deal a card from the deck (removes it from the deck)."""
        return self._deck.pop() if self._deck else None

    def remaining_card(self):
        """Returns the number of cards left in the deck."""
        return len(self._deck)

    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'

        return s