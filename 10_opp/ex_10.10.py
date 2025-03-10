# ex_10.10.py
"""Class player test."""

from player import Player

player1 = Player("Warrior", 5, 20, 500.00)
player2 = Player("Magician", 3, 25, 450.00)

# simulating a fight
result = player1.defence(player2)

print(f"{result}")