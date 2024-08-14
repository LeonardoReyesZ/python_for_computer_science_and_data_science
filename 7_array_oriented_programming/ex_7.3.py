# ex_7.3: Element-Wise array Multiplication
import numpy as np

array = np.full((10,10), 4)
array1 = np.arange(1, 101).reshape(10,10)

print( f"{array*array1}")