# ex_7.14: horizontal and vertical stacking and splitting
import numpy as np

array1 = np.array([[0,2], [4,6]])
array2 = np.array([[1,3], [5,7]])

array3 = np.hstack((array1, array2))
print(f"array3:\n{array3}\n" )

array4, array5 = np.vsplit(array3,2)
print( f"array4:\n{array4}\n" )
print( f"array5:\n{array5}\n" )

array6 = np.hstack( (np.sort(array4), np.sort(array5)) )
print( f"array6:\n{array6}\n" )

array7 = np.vstack( (array6, array6*10) )
print( f"array7:\n{array7}\n" )