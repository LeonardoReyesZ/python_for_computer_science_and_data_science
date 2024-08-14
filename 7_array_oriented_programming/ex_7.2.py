# ex_7.2: Broadcasting
import numpy as np

array = np.arange(0,4).reshape(2,2)
print( array, end="\n\n" )

print( f"Cube:\n{array**3}\n\n")
print( f"Add 7:\n{array+7}\n\n")
print( f"Multiply by 2:\n{array*2}")
