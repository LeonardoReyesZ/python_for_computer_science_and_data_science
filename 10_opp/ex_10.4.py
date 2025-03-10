# ex_10.4.py
"""Testing Time class with internal data modified."""
from timewithproperties import Time

wake_up = Time(hour=6, minute=30)

print(wake_up)
print(wake_up.hour)  # call to an hour method

wake_up.set_time(hour=7, minute=45)
print(wake_up.__str__)

wake_up.hour = 5  # hour method that takes an argument
print(wake_up)

# wake_up.hour = 100 # call hour method that validates the argument
print(wake_up)

t = Time()
print(f'\n{t}')
t.time = (12, 30, 45)
print(t)


