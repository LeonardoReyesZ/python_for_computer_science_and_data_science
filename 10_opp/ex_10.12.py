# ex_10.12.py
"""Testing complex class"""

# creating two complex numbers
complex1 = 3+4j
complex2 = 1+2j

# a
sum = complex1 + complex2
print(f"sum: {sum}")

# b
difference = complex1 - complex2
print(f"difference: {difference}")

# c
print(f"complex 1: {complex1}")
print(f"complex 2: {complex2}")

# d
print(f"Complex 1 real part: {complex1.real}\n"
      f"Complex 1 imaginary part: {complex1.imag}")