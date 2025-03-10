# ex_10.8.py
"""Converting data class objects to tuples and dictionaries"""

from dataclasses import dataclass, field, astuple, asdict
from typing import ClassVar, List
from carddataclass import Card
import random

card = Card(face='ace', suit='hearts')

# convert the card object to a tuple
card_tuple = astuple(card)

# covert the card object to a dictionary
card_dict = asdict(card)

print("Card as a tuple: ", card_tuple)
print("Card as a dict: ", card_dict)