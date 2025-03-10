# ex_10.21.py
"""Black Jack card game."""

from blackjack import BlackJack

def play_game():
    """Play black jack game."""
    game = BlackJack()

    game.show_hands()

    # check for black jack
    if game.get_hand_points(game.player_hand) == 21:
        game.dealer_hand[-1]._front = True # face-up card
        if game.get_hand_points(game.dealer_hand) == 21:
            game.show_hands()
            print("It's a tie (push)")
            return
        game.show_hands()
        print("Black Jack! player win.")
        return

    if not game.player_turn():
        return

    if not game.dealer_turn():
        return

    print(game.determine_winner())


# start playing the game
if __name__ == '__main__':
    play_game()