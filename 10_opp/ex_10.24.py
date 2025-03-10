# ex_10.24.py
import pydealer

# rank order for comparison
rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def get_highest_card(hand):
    """Get the highest card in a hand based on rank."""
    # find the card with the highest rank
    highest_card = hand[0]
    for card in hand:
        if rank_order.index(card.value) > rank_order.index(highest_card.value):
            highest_card = card

    return highest_card

if __name__ == '__main__':
    # create a deck of cards and shuffle it
    deck = pydealer.Deck()
    deck.shuffle()

    # deal 5 cards to each player
    player1_hand = deck.deal(5)
    player2_hand = deck.deal(5)

    # print the hands
    print("Player 1's hand:")
    print(player1_hand)
    print("\nPlayer 2's hand:")
    print(player2_hand)

    # get the highest card in each hand
    player1_highest = get_highest_card(player1_hand)
    player2_highest = get_highest_card(player2_hand)

    # print the highest cards
    print(f"\nPlayer 1's highest card: {player1_highest}")
    print(f"Player 2's highest card: {player2_highest}")

    # determine the winner
    if rank_order.index(player1_highest.value) > rank_order.index(player2_highest.value):
        print("\nPlayer 1 wins!")
    elif rank_order.index(player1_highest.value) < rank_order.index(player2_highest.value):
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a draw!")