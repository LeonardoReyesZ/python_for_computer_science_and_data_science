# solitaire.py
"""Solitaire card game implementation."""

from card import Card
from deck import DeckOfCards

class Solitaire:
    """Solitaire card game class."""
    def __init__(self):
        """Initialize the game."""
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.columns = [[] for _ in range(7)] # 7 columns in Klondike
        self.foundation = {suit: [] for suit in Card.SUITS}  # Foundation piles for each suit
        self.stock = [] # stock pile to draw from
        self.waste = [] # waste pile
        self.movements = 0 # track the number of movements

        # deal cards into columns (7 piles) and set up stock
        self.deal_cards_to_columns()

    def deal_cards_to_columns(self):
        """Deal cards into the 7 columns, with the last card in each column face-up. And set up stock pile."""
        for i in range(7):
            for j in range(i, 7):
                card = self.deck.deal_card()
                if card:
                    self.columns[j].append(card)

            # set all cards as face-down but, the last ones.
            for card in self.columns[i][:-1]: # all but the last card
                card._front = False # show the back of the card

        # initialize the stock after dealing cards to the columns
        self.stock = self.deck._deck # all remaining cards are in the stock

    def draw_from_stock(self):
        """Draw a card from the stock pile and add it to the waste."""
        if not self.stock: # reset the stock from waste
            if self.waste:
                self.stock = self.waste
                self.waste = []
                self.movements += 1

        if self.stock:
            card = self.stock.pop(0)
            self.waste.append(card)
            self.movements += 1
            return True

        return False

    def move_card(self, from_pile, to_pile, pile_type='column'):
        """Move a card from one pile to another (either column or foundation)."""
        if not from_pile:
            print("No card to move in source pile")
            return False

        card_to_move = from_pile[-1] # last card (face-up)

        if pile_type == 'column':
            can_stack = self._can_stack_column(card_to_move, to_pile[-1] if to_pile else None)

        elif pile_type == 'foundation':
            can_stack = self._can_stack_foundation(card_to_move, to_pile[-1] if to_pile else None)

        # move a card after validation
        if can_stack:
            to_pile.append(from_pile.pop())
            print(f">>> Moved {card_to_move} to {pile_type}"
                  f"{' '+str(self.columns.index(to_pile)+1) if pile_type == 'column' else ''}")
            if from_pile:
                from_pile[-1]._front = True # face-up the new last card

            self.movements += 1
            return True

        print("Invalid move.")
        return False

    def move_cards_between_columns(self, from_pile, to_pile, n):
        """Move cards from one column to another."""
        if not from_pile:
            print("There are no cards to move in the source column.")
            return False

        try:
            if not from_pile[-n]._front:
                print("Invalid move.")
                return False

            cards_to_move = from_pile[-n:] # last n cards to move (face-up)

            can_stack = self._can_stack_column(cards_to_move[0], to_pile[-1] if to_pile else None)

            # move cards after validation
            if can_stack:
                to_pile.extend(cards_to_move)
                print(f">>> Moved {', '.join([str(card) for card in cards_to_move])} "
                      f"to column {self.columns.index(to_pile)+1}")

                for _ in range(n):
                    from_pile.pop() # remove cards from the source pile

                if from_pile:
                    from_pile[-1]._front = True # face-up new last card

                self.movements += 1
                return True

            else:
                print("Invalid move.")
                return False

        except IndexError:
            print("Invalid number of cards.")

    def _can_stack_column(self, card_to_move, card_on_top=None):
        """Check if a card can be stacked on another column on descending order and alternating colors."""
        if card_on_top:
            return (Card.FACES.index(card_to_move.face) == Card.FACES.index(card_on_top.face) - 1 and
            ((card_to_move.suit in ['hearts', 'diamonds'] and card_on_top.suit in ['clubs', 'spades']) or
             (card_to_move.suit in ['clubs', 'spades'] and card_on_top.suit in ['hearts', 'diamonds'])))

        return card_to_move.face == 'king' # if the column is empty, only a king can be place

    def _can_stack_foundation(self, card_to_move, card_on_top=None):
        """Check if a card can be stacked on foundation on ascending order with the same suit."""
        if card_on_top:
            return Card.FACES.index(card_on_top.face) == Card.FACES.index(card_to_move.face)-1

        return card_to_move.face == 'ace' # foundation starts with Ace

    def move_column_to_foundation(self, column_index):
        """Move a card from a column to foundation."""
        try:
            return self.move_card(self.columns[column_index], self.foundation[self.columns[column_index][-1].suit],
                                  'foundation')
        except IndexError:
            print("Invalid move(out of range)")
            return False

    def move_foundation_to_column(self, suit, column_index):
        """Move a card from foundation to a column."""
        return self.move_card(self.foundation[suit], self.columns[column_index], 'column')

    def move_waste_to_foundation(self):
        """Move a card from waste to foundation."""
        if not self.waste:
            print("invalid move.")
            return False
        return self.move_card(self.waste, self.foundation[self.waste[-1].suit], 'foundation')

    def move_waste_to_column(self, to_column):
        """Move a card from waste to a column."""
        return self.move_card(self.waste, self.columns[to_column], 'column')

    def print_status(self):
        """Print current game state."""
        print("\nFoundations:")
        for suit, pile in self.foundation.items():
            print(f"{suit}: {', '.join([str(card) for card in pile]) if pile else 'Empty'}")

        print("\nColumns:")
        for i, column in enumerate(self.columns):
            print(f"Column {i+1}: {', '.join([str(card) for card in column]) if column else 'Empty'}")

        print("\nWaste")
        print(f"Waste: {', '.join([str(card) for card in self.waste]) if self.waste else 'Empty'}")

        print("\nStock")
        print(f"Stock: {len(self.stock)} cards remaining")
        print(f"\nMovements: {self.movements}")

    def check_winner(self):
        """Check if the player has completed the game."""
        return all(len(pile) == 13 for pile in self.foundation.values())