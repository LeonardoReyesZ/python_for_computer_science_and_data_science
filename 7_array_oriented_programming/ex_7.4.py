# ex_7.4: array from List of Lists
import numpy as np

list = [[x for x in range(10,-1,-1) ], [x for x in range(11)]]

array = np.array(list)
print( array )