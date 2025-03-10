# ex_10.23.py
"""Poker card game test."""
from poker import Poker
import random

names = ['You', 'Stacy', 'Miguel', 'Aoife', 'Bryan']
num_players = len(names)
budget = 1000
turn = random.choice(names)
turn = names.index(turn)
ante = 1

# initialize game
game = Poker(names, num_players, budget, turn, ante)

game.start()

print("\nend of the program...")