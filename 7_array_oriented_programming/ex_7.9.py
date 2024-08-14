# ex_7.9: Indexing and slicing arrays
import numpy as np

array = np.arange(1, 16).reshape(3,5)
print( array[2], end="\n\n" )
print( array[:, 4], end="\n\n" )
print( array[:, 1:3], end="\n\n" )
print( array[1,4], end="\n\n" )
#print( array[[1,2], [0,2,4]])
print( array[1:3, [0,2,4]])
