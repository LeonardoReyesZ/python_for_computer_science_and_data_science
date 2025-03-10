# ex_10.3.py
"""Testing the coin class"""
from coin import Coin

wallet = Coin(10, 20, 30, 40, 50)

print("Coins in the wallet:")
print(wallet.universal_str, end="\n\n")

print(f"Total amount of money: {wallet.total_amount()}")