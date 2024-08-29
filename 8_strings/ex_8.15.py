# ex_8.15: Count number of ocurrences of a letter
import re

text = "The mouse that the cat that the dog that the man frightened and chased ran away"

# find 'a' occurrences
a_ocurrences = re.findall(r'a', text)

# print the number of occurrences
print( f"The letter 'a' occurs {len(a_ocurrences)} times in the text." )