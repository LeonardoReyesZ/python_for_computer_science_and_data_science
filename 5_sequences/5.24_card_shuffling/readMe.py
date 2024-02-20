5.24 (Card Shuffling and Dealing) In Exercises 5.24 through 5.26, you’ll use lists of tu-
ples in scripts that simulate card shuffling and dealing. Each tuple represents one card in
the deck and contains a face (e.g., 'Ace', 'Deuce', 'Three', ..., 'Jack', 'Queen', 'King')
and a suit (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades'). Create an initialize_deck
function to initialize the deck of card tuples with 'Ace' through 'King' of each suit, as in
deck = [('Ace', 'Hearts'), ..., ('King', 'Hearts'),
('Ace', 'Diamonds'), ..., ('King', 'Diamonds'),
('Ace', 'Clubs'), ..., ('King', 'Clubs'),
('Ace', 'Spades'), ..., ('King', 'Spades')]

Before returning the list, use the random module’s shuffle function to randomly order the
list elements. Output the shuffled cards in the following four-column format.

(Card Playing: Evaluating Poker Hands) Modify Exercise 5.24 to deal a five-card
poker hand as a list of five card tuples. Then create functions (i.e., is_pair, is_two_pair,
is_three_of_a_kind, ...) that determine whether the hand they receive as an argument
contains groups of cards, such as:
a) one pair
b) two pairs
c) three of a kind (e.g., three jacks)
d) a straight (i.e., five cards of consecutive face values)
e) a flush (i.e., all five cards of the same suit)
f) a full house (i.e., two cards of one face value and three cards of another)
g) four of a kind (e.g., four aces)
h) straight flush (i.e., a straight with all five cards of the same suit)
i) ... and others.
See https://en.wikipedia.org/wiki/List_of_poker_hands for poker-hand types and
how they rank with respect to one another. For example, three of a kind beats two pairs.

5.26
(Card Playing: Determining the Winning Hand) Use the methods developed in
Exercise 5.25 to write a script that deals two five-card poker hands (i.e., two lists of five
card tuples each), evaluates each hand and determines which wins. As each card is dealt, it
should be removed from the list of tuples representing the deck.
