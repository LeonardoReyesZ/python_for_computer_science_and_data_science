# ex_8.13: replacing substrings
import re

# Original line from the poem
line = "Jennifer, you are more beautiful than the most beautiful rose"

# Using a regular expression to replace the name "Jennifer" with a new name
names = ["Stacy", "Samantha", "Alisse"]

for name in names:
    new = re.sub(r'\bJennifer\b', name, line)
    print( f"{new}" )