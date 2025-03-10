# ex_10.22.py
"""Card class with overloaded Comparison Operators test"""
from cardtotalordering import Card

card1 = Card('ace', 'clubs')
card2 = Card('king', 'spades')
card3 = Card('5', 'hearts')

print(f"{card1} == {card2}: {card1 == card2}")
print(f"{card3} != {card2}: {card3 != card2}")
print(f"{card3} < {card1}: {card3 < card1}")
print(f"{card2} > {card3}: {card2 > card3}")
print(f"{card1} <= {card3}: {card1 <= card3}")
print(f"{card1} >= {card2}: {card1 >= card2}")