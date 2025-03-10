# ex_10.11.py
"""testing class Fraction"""

from fractions import Fraction

fraction1 = Fraction(2,4)
fraction2 = Fraction(3,4)

# a
sum = fraction1+fraction2
print(f"Sum: {sum}")

# b
difference = fraction1-fraction2
print(f"Difference: {difference}")

# c
product = fraction1*fraction2
print(f"Product: {product}")

# d
quotient = fraction1/fraction2
print(f"Quotient: {quotient}")

# e
print(f"Fraction 1: {fraction1}")
print(f"Fraction 2: {fraction2}")

# f
float1 = float(fraction1)
float2 = float(fraction2)

print(f"Fraction 1 (float): {float1}")
print(f"Fraction 2 (float): {float2}")