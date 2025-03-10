# ex_10.15
"""Immutable data class objects"""

from complex import Complex

# example usage of frozen complex class
c1 = Complex(3,4)
c2 = Complex(1,2)

c3 = c1+c2
print(c3)

# attempting to modify c1's attributes would raise an error
try:
    c1.real = 5 # this will raise a FrozenInstanceError
except Exception as e:
    print(f'Error: {e}')