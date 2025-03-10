# ex_10.7.py
"""Module datetime"""

import datetime

# part a
x = datetime.datetime.now()

# part b
y = datetime.datetime.now()

# part c
print("Date time x: ", x)
print("Date time y: ", y)

# part d
print("\nAttributes of x:")
print(f"year: {x.year}\n"
      f"month: {x.month}\n"
      f"day: {x.day}\n"
      f"hour: {x.hour}\n"
      f"minute: {x.minute}\n"
      f"second: {x.second}\n"
      f"microsecond: {x.microsecond}\n"
      f"timezone: {x.tzinfo}\n")


print("\nAttributes of y:")
print(f"year: {y.year}\n"
      f"month: {y.month}\n"
      f"day: {y.day}\n"
      f"hour: {y.hour}\n"
      f"minute: {y.minute}\n"
      f"second: {y.second}\n"
      f"microsecond: {y.microsecond}\n"
      f"timezone: {y.tzinfo}\n")

# part e
print("\nComparison of x and y:")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# part f
difference = y-x
print("\nDifference between y and x:")
print(f"Time difference: {difference}")