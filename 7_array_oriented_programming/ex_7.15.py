# ex_7.15: Numpy's Concatenate Function
import numpy as np

array1 = np.array([[0,2], [4,6]])
array2 = np.array([[1,3], [5,7]])

# horizontal stacking to create array3 using concatenate
array3 = np.concatenate((array1, array2), axis=1)
print( f"array3:\n{array3}\n" )

array4, array5 = np.vsplit(array3, 2)
array6 = np.concatenate( (np.sort(array4), np.sort(array5)), axis=1 )
print( f"array6:\n{array6}\n" )

array7 = np.concatenate( (array6, array6*10), axis=0 )
print( f"array7:\n{array7}\n" )