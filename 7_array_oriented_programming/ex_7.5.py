# ex_7.5: Flattening arrays with flatten vs. ravel
import numpy as np

list = [[x for x in range(10,-1,-1) ], [x for x in range(11)]]

array = np.array(list)

flattened = array.flatten()
flattened[1] = 10
print( f"original array:\n{array}\n" )
print( f"flattened array:\n{flattened}\n\n" )

raveled = array.ravel() # view of the original array
raveled[1] = 10 # mdifies original array data
print( f"original array:\n{array}\n" )
print( f"raveled array:\n{raveled}\n" )
