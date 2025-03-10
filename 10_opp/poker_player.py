# poker_player.py
"""Poker player class implementation."""
from hand import Hand
import random

class Player:
    def __init__(self, name, balance, cards, carry=0):
        """Initialize a poker player."""
        self.name = name
        self.balance = balance
        self.cards = cards
        self.fold = False
        self.last_move = ''
        self.invalid_move = False
        self.sb_position = False
        self.carry = carry # track the carry(ante) value to bet
        self.increment = 0 # track the player's raise value
        self.raise_flag = False # track if the player has risen the bet
        self.hand = Hand
        self.options = ['1', '2', '3'] # option for automatic moves
        self.weights = [10, 70, 20] # probabilities -> 10%, 70%, 20%

    def move(self, previous_move, current_bet, min_bet):
        """Fold, Raise, Call or Check move."""
        # next move based on player's previous move -> check if check | call if (ante or raise)
        check_or_call = 'Check' if previous_move == 'CHECK' else 'Call'

        while True:
            if self.name.lower() == 'you':
                option = input(f"\n{self.name}'s turn.\n1. Fold, 2. {check_or_call}, 3. Raise.\tMove: ")
            else:
                option = random.choices(self.options, weights=self.weights, k=1)[0]
            if option == '1': # fold
                self.fold = True
                print(f"{self.name} fold.")
                self.last_move = 'FOLD'
                self.invalid_move = False
                return 0
            elif option == '2': # check or call
                if check_or_call.upper() != 'CHECK':
                    self.last_move = 'CALL'
                    return self.bet(current_bet)
                else:
                    print(f"{self.name} check.")
                    self.last_move = 'CHECK'
                    self.invalid_move = False
                    return 0
            elif option == '3': # raise
                self.last_move = 'RAISE'
                return self.raise_bet(current_bet, min_bet)
            else:
                print("Invalid option... try again.")

    def raise_bet(self, current_bet, min_bet):
        """Raise move, increase the current bet."""
        if self.name.lower() != 'you':
            increment = float(random.randint(min_bet, int(self.balance/10)))

        else:
            while True:
                try:
                    increment = int(input(f"Insert raise amount (min: {min_bet}): $"))
                    if increment < min_bet or increment > self.balance:
                        raise ValueError('raise must be equal or higher than the minimum.')
                    break
                except ValueError:
                    print("Invalid value.")

        print(f"{self.name} raises the bet ${increment}")
        self.increment = increment  # save player's raise value
        increment += current_bet  # increase the bet
        return self.bet(increment)

    def bet(self, amount):
        """Take the amount to bet from the player's balance."""
        amount += self.carry # player's ante value

        if amount>self.balance or amount<0:
            print("invalid value.")
            self.invalid_move = True
            return 0

        self.balance -= amount
        print(f"{self.name} bets ${amount}")
        self.invalid_move = False
        return amount

    def __repr__(self):
        if not self.fold:
            return f"Player(name='{self.name}', cards='{self.cards}', balance='{self.balance}', carry='{self.carry}')"
        return f"Player(name='{self.name}', fold)"

    def __str__(self):
        return f"{self.name}, {self.cards}, {self.balance}"