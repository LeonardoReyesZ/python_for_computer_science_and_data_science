# poker.py
"""Poker card game implementation."""
from decktotalordering import DeckOfCards
from poker_player import Player
from hand import Hand
from itertools import combinations

class Poker:
    def __init__(self, names, num_players, budget, turn, ante):
        """Initialize the poker game."""
        self.NUM_PLAYERS = num_players
        self.ANTE = ante
        self.players = []

        # initialize poker players -> set names, set balance and carry(ante) values
        for i in range(num_players):
            if i == turn: # small blind player
                self.players.append(Player(names[i], budget,[], ante))
            else: # ante is the double for the rest of the players
                self.players.append(Player(names[i], budget, [], ante*2))

        self.initial_game_variable_values(turn)
        self.make_first_two_bets()
        self.stock = self.deck._deck # remaining cards in the deck

    @property
    def bet_balance(self):
        return self._bet_balance

    @bet_balance.setter
    def bet_balance(self, bet):
        if bet < 0:
            raise ValueError("Bet must be a positive number.")

        self._bet_balance = bet

    def initial_game_variable_values(self, turn):
        """Default values to start a poker match."""
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.turns_remaining = self.NUM_PLAYERS
        self.players_standing = self.NUM_PLAYERS
        self.current_player = turn
        self.round = 1
        self.big_blind_flag = False  # track if bb_player has to finish the first round
        self.end_round_flag = False
        self.raise_bet_flag = False
        self.community_cards = []
        self.game_over_flag = False
        self.min_amount_to_bet = self.ANTE * 2  # track the minimum amount to bet per round
        self.bet_balance = 0
        self.current_bet = 0
        self.players[turn].sb_position = True  # set small blind position player
        self.sb_match_position = turn # track sb position for the next matches

        # deal cards to the players and set the carry(ante) values and reset player's fold flags
        for i in range(self.NUM_PLAYERS):
            self.players[i].fold = False
            self.players[i].cards = [self.deck.deal_card(), self.deck.deal_card()]
            if i == turn:
                self.players[i].carry = self.ANTE
            else:
                self.players[i].carry = self.ANTE * 2
        self.set_cards_face_down()

    def set_cards_face_down(self):
        """Face down player's cards."""
        for player in self.players:
            if player.name.lower() != 'you':
                for card in player.cards:
                    card._front = False

    def set_cards_face_up(self):
        """Face up player's cards."""
        for player in self.players:
            if player.name.lower() != 'you': # you's cards already face up
                for card in player.cards:
                    card._front = True

    def next_player(self):
        """Move the turn to the next player."""
        # create a loop through the players
        self.current_player = (self.current_player+1) % self.NUM_PLAYERS
        self.turns_remaining -= 1 # reduce a turn tracking the end for a round

    def make_first_two_bets(self):
        """Collect the first two bets from the first two players."""
        self.bet_balance += self.players[self.current_player].bet(self.current_bet)
        self.next_player()
        self.bet_balance += self.players[self.current_player].bet(self.current_bet)
        self.players[self.current_player].carry = 0  # reset bb_player_carry after use
        self.next_player()

        self.previous_move = 'ANTE'
        print(f"bet balance: ${self.bet_balance}")

    def start(self):
        """Start a match, track player moves, the end of each round and start a new match if it is require."""
        # loop to track the end of each round and the end of the match
        while self.turns_remaining > -1:
            self.set_amount_to_bet()

            # evaluate the end of each round
            if self.turns_remaining == 0:
                self.handle_round_end()

            # skip fold players or end the round if there are no more turns left
            if self.players[self.current_player].fold:
                self.next_player()
                continue  # skip fold players

            if self.game_over_flag:
                if self.start_new_match(): # start a new match
                    continue
                else:
                    break # finish the game

            # make player's move and evaluate them
            self.handle_player_turn()
            pause = input("pause...")
            self.evaluate_move()

            if self.game_over_flag:
                if self.start_new_match(): # start a new match
                    continue
                else:
                    break # finish the game

            self.next_player()
            self.show_status()

        pause = input("end of the game")

    def start_new_match(self):
        """Reset the default values and flags to start a new match."""
        option = input("Enter any character to dial again. 'no' to finish the game: ").lower()
        if option != 'no':
            print("\n\nDefault settings for a new match..")
            # reset current sb_player flag
            while True:
                if self.players[self.current_player].sb_position:
                    self.players[self.current_player].sb_position = False # previous(['default']) sb_player
                    break # new sb player found
                self.next_player()

            # default variable values to start a match -> sb default player + 1
            self.initial_game_variable_values((self.sb_match_position+1) % self.NUM_PLAYERS)
            self.show_status()
            print("\n\nNew match started...")
            self.make_first_two_bets()
            return True
        else:
            return False

    def handle_player_turn(self):
        """Adjust bet balance for the next turn. Make player's move and add the player's bet to bet balance."""
        while True:  # loop until the player makes a valid move
            player_bet = self.players[self.current_player].move(self.previous_move, self.current_bet, self.min_amount_to_bet)
            self.bet_balance += player_bet

            if not self.players[self.current_player].invalid_move:
                break

    def set_amount_to_bet(self):
        """Subtract raise increment from current_bet once the rest of the players had met the bet."""
        if self.players[self.current_player].raise_flag:
            bet_update = self.players[self.current_player].increment
            self.players[self.current_player].increment = 0  # reset the increment variable after use
            self.players[self.current_player].raise_flag = False  # reset raise flag after use

            if self.current_bet - bet_update > 0:  # bet can not be <= 0
                self.current_bet -= bet_update

    def evaluate_move(self):
        """Evaluate player's move(fold or raise) and make the corresponding changes."""
        if self.players[self.current_player].last_move == 'FOLD':
            self.players_standing -= 1
            if self.players_standing < 2:  # just one player remaining
                self.set_default_winner()  # winner by default
                return # finish the evaluation
            # if the sb_player fold, find a new sb_player
            if self.players[self.current_player].sb_position:
                new_sb = self.current_player
                while True:
                    new_sb = (new_sb + 1) % self.NUM_PLAYERS
                    if not self.players[new_sb].fold:
                        self.players[new_sb].sb_position = True
                        break
                self.players[self.current_player].sb_position = False # previous(default) sb_player
            if self.previous_move == 'RAISE':  # avoid raise evaluation redundancy
                self.previous_move = 'CALL'
        else:
            self.previous_move = self.players[self.current_player].last_move

        # when a player raises the bet, all the players has to met or increase the bet
        if self.previous_move == 'RAISE':
            self.turns_remaining = self.NUM_PLAYERS  # give a turn to each player
            self.current_bet += self.players[self.current_player].increment
            self.raise_bet_flag = True
            self.players[self.current_player].raise_flag = True

        self.players[self.current_player].carry = 0  # reset the carry after use

    def handle_round_end(self):
        """Handle the end of each round of the game."""
        if self.raise_bet_flag:
            self.end_round()  # finish the current round once all the players met the bet
        elif self.round == 1:  # arrange the end of the first round if the bet was not raised
            self.handle_preflop()
            return
        else: # for the next rounds
            self.end_round()

    def handle_preflop(self):
        """SmallBlindPlayer penultimate turn and BigBlindPlayer last turn before the flop if none of the players
        has risen the bet."""
        if self.end_round_flag:  # once sb and bb players had made their moves
            self.end_round()  # finish the first round and show the flop

        elif self.big_blind_flag:
            self.turns_remaining += 1  # bb_player has the last turn of the round
            self.previous_move = 'CHECK'  # bb_player -> check or raise before the flop
            self.end_round_flag = True  # the round will finish in the next turn
            return  # continue to bb_player's turn

        else:
            self.turns_remaining += 1  # turn for sb_player
            self.big_blind_flag = True
            return  # continue to sb_player's turn

    def end_round(self):
        """Display the corresponding stage at the end of each round."""
        if self.round == 1:
            self.display_flop()
        elif self.round == 2:
            self.display_turn()
        elif self.round == 3:
            self.display_river()
        elif self.round == 4:
            self.showdown() # final stage

        self.reset_turns()

    def display_flop(self):
        """Display the flop. Add the three first cards to the community cards."""
        for i in range(3):
            self.community_cards.append(self.deck.deal_card())
        community_cards = [card.__str__() for card in self.community_cards]
        print("\n\nFlop:\n", community_cards)

    def display_turn(self):
        """Display the turn. Add another card to the community cards."""
        self.community_cards.append(self.deck.deal_card())
        community_cards = [card.__str__() for card in self.community_cards]
        print("\n\nTurn:\n", community_cards)

    def display_river(self):
        """Display the river. Add another card to the community cards."""
        self.community_cards.append(self.deck.deal_card())
        community_cards = [card.__str__() for card in self.community_cards]
        print("\n\nRiver:\n", community_cards)

    def showdown(self):
        """Final stage. Compare the highest-ranking five-card set of each player and set the winner."""
        winner_hand = None
        community_cards = [card.__str__() for card in self.community_cards]
        print(f"\n\ncommunity cards:\t{community_cards}\n")
        self.set_cards_face_up()

        for i in range(self.NUM_PLAYERS):
            if not self.players[self.current_player].fold:
                # find the highest-ranking five-card set per player
                self.generate_highest_hand()
                if winner_hand == None:
                    winner_hand = self.players[self.current_player].hand # assume current player has the best hand
                    winner = self.current_player
                elif winner_hand < self.players[self.current_player].hand:
                    winner_hand = self.players[self.current_player].hand # find the winner's hand
                    winner = self.current_player

                print(f"{self.players[self.current_player].name}'s hand:\t{self.players[self.current_player].hand}")
            self.next_player()

        self.set_winner(winner)

    def generate_highest_hand(self):
        """Get the highest hand combination using player and community cards."""
        # generate all possible hand combinations
        all_cards = self.players[self.current_player].cards + self.community_cards
        combinations_list = combinations(all_cards, 5)
        hand_combinations = [Hand(combination) for combination in combinations_list]

        # get the highest hand
        self.players[self.current_player].hand = max(hand_combinations)

    def reset_turns(self):
        """Reset turns and flags to start a new round."""
        while True: # sb_player is the first turn of every round
            if self.players[self.current_player].sb_position:
                break
            self.next_player()

        self.turns_remaining = self.NUM_PLAYERS  # new round of turns
        self.current_bet = 0
        self.round += 1 # move to the next round
        if self.round == 3:
            self.min_amount_to_bet *= 2
        self.raise_bet_flag = False
        self.previous_move = 'CHECK' # check is one of the options for the first turn of a new round

    def set_default_winner(self):
        """Set the winner by default."""
        while True:
            self.next_player()
            if not self.players[self.current_player].fold:
                self.set_winner(self.current_player)
                break

    def set_winner(self, player):
        """Add bet_balance to the winner's balance and set the flag to finish the current game."""
        print(f"\n{self.players[player].name} wins ${self.bet_balance:.2f} !!!\n")
        self.players[player].balance += self.bet_balance
        self.game_over_flag = True

    def show_status(self):
        """Show the status of the game."""
        print("\nPlayers standing: ",self.players_standing)
        print("current bet: $",self.current_bet)
        print("bet balance: $",self.bet_balance)
        print("current player: ",self.players[self.current_player].name, end="\n\n")

        for player in self.players:
            print(player.__repr__())

        print()