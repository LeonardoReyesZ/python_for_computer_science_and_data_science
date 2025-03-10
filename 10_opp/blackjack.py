# blackjack.py
"""Black Jack card game implementation."""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from deck import DeckOfCards

path = Path('.').joinpath('card_images') # folder that contains card images

class BlackJack:
    """Black Jack card game class."""
    def __init__(self):
        """Initialize the game."""
        self.deck = DeckOfCards()
        self.deck.shuffle()

        # initialize player's hands
        self.player_hand = [self.deck.deal_card(), self.deck.deal_card()]
        self.dealer_hand = [self.deck.deal_card(), self.deck.deal_card()]

        self.dealer_hand[-1]._front = False # set the second card face-down

    def get_hand_points(self, hand):
        """Calculate the points of a hand of cards, adjusting for Aces as needed."""
        points = sum(card.black_jack_value() for card in hand)
        # get the number of 'ace' in the hand
        ace_count = sum(1 for card in hand if (card.face == 'ace' and card._front))

        # Adjust for Aces (if any Aces, count them as 11 unless it busts the hand)
        while ace_count > 0 and points + 10 <= 21:
            points += 10
            ace_count -= 1

        return points # return the points

    def player_turn(self):
        """Player turn. Hit or Stand."""
        while True:
            option = input("\nDo you want to: hit(H) or stand(S)? ").lower()

            if option == 'h':
                self.player_hand.append(self.deck.deal_card())
                if self.get_hand_points(self.player_hand) > 21:
                    self.dealer_hand[-1]._front = True
                    self.show_hands()
                    print("\nYou busted! Dealer wins.")
                    return False
                self.show_hands()

            elif option == 's':
                return True

            else:
                print("Invalid option ... try again.")

    def dealer_turn(self):
        """Discover dealer's card and hit cards."""
        self.dealer_hand[-1]._front = True # discover card

        # while dealer hand's points are less than 17, hit cards
        while self.get_hand_points(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal_card())

        dealer_points = self.get_hand_points(self.dealer_hand)
        self.show_hands()

        if dealer_points > 21:
            print("\nDealer busts! Player win.")
            return False

        return True

    def determine_winner(self):
        """Determine the winner of the game."""
        player_points = self.get_hand_points(self.player_hand)
        dealer_points = self.get_hand_points(self.dealer_hand)

        if player_points == dealer_points:
            return "It's a tie (push)"

        return "Player wins" if player_points > dealer_points else "Dealer wins."

    def show_hands(self):
        """Show the hands of the player and the dealer."""
        # determine the maximum number of cards in either hand
        max_cards = max(len(self.player_hand), len(self.dealer_hand))

        # create a grid for displaying cards
        figure, axes_list = plt.subplots(nrows=2, ncols=max_cards)

        # hide axes for all subplots
        for axes in axes_list.ravel():
            axes.get_xaxis().set_visible(False)
            axes.get_yaxis().set_visible(False)

        # show player's hand
        for i, card in enumerate(self.player_hand):
            image_name = card.image_name
            img = mpimg.imread(str(path.joinpath(image_name).resolve()))
            axes_list[0, i].imshow(img)

        # show dealer's cards
        for i, card in enumerate(self.dealer_hand):
            image_name = card.image_name
            img = mpimg.imread(str(path.joinpath(image_name).resolve()))
            axes_list[1, i].imshow(img)

        # adjust layout
        figure.tight_layout()
        plt.show()