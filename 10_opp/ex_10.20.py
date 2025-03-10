# ex_10.20.py
"""Solitaire card game test."""

from card import Card
from solitaire import Solitaire

def play_game():
    """Play solitaire game."""
    game = Solitaire()

    while True:
        print("\n")
        game.print_status()

        if game.check_winner():
            print("\n\nCongratulations!!! You have won the game.\n\n")
            break # end of the game

        action = input("\nChose an action: (1: Draw from stock, 2: Move a card between columns, "
                       "3: Move a card from a column to foundation,\n\t4: Move a card from waste to a column,   "
                       "5: Move a card from waste to foundation, 6: Move a card from foundation to a column, "
                       "\n\t7: Move cards between columns, q: Quit\nAction: ").lower()

        if action == '1': # draw a card from stock to waste
            game.draw_from_stock()

        elif action == '2': # move a card between columns
            while True:
                try:
                    from_column = int(input("\nWhich column to move from (1-7): ")) - 1
                    to_column = int(input("Which column to move to (1-7): ")) - 1
                    break
                except ValueError:
                    print("\nThe column must be an integer !\n")

            if 0 <= from_column < 7 and 0 <= to_column < 7:
                game.move_card(game.columns[from_column], game.columns[to_column])
            else:
                print("\nInvalid columns.")

        elif action == '3': # move a card from a column to foundation
            while True:
                try:
                    from_column = int(input("\nWhich column to move from (1-7): ")) - 1
                    break
                except ValueError:
                    print("\nThe column must be an integer!\n")
            if 0 <= from_column < 7:
                game.move_column_to_foundation(from_column)
            else:
                print("\nInvalid column.")

        elif action == '4': # move a card from waste to a column
            while True:
                try:
                    to_column = int(input("\nWhich column to move to (1-7): ")) - 1
                    break
                except ValueError:
                    print("\nThe column must be an integer!\n")
            if 0 <= to_column < 7:
                game.move_waste_to_column(to_column)
            else:
                print("\nInvalid column.")

        elif action == '5': # move a card from waste to foundation
            game.move_waste_to_foundation()

        elif action == '6': # move a card from foundation to a column
            while True:
                try:
                    suit = int(input("\nSelect the suit from foundation: "
                                     "1:'hearts', 2:'diamonds', 3:'clubs', 4:'spades'\nsuit: ")) - 1
                    to_column = int(input("Which column to move to (1-7):")) - 1
                    break
                except ValueError:
                    print("\nThe selection values must be integers.")

            if 0 <= to_column < 7 and 0 <= suit < 4:
                game.move_foundation_to_column(Card.SUITS[suit], to_column)

            else:
                print("\nInvalid column.")

        elif action == '7': # move cards between columns
            while True:
                try:
                    from_column = int(input("\nWhich column to move from (1-7): ")) - 1
                    to_column = int(input("Which column to move to (1-7): ")) - 1
                    n = int(input("How many cards do you want to move? "))
                    break
                except ValueError:
                    print("\nThe values must be integers.")

            if 0 <= from_column < 7 and 0 <= to_column < 7:
                game.move_cards_between_columns(game.columns[from_column], game.columns[to_column], n)
            else:
                print("\nInvalid column")

        elif action == 'q': # finish the game
            print("\n\n\nGame over.")
            break

        else:
            print("\nInvalid action.")
# end of play_game()


# start playing the game
if __name__ == '__main__':
    play_game()