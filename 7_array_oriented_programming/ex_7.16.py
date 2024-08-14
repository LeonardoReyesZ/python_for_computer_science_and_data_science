# ex_7.16
import numpy as np

# create basic 4X4 block
block = np.array([[0,0,0,0],
                  [0,0,0,0],
                  [1,1,1,1],
                  [1,1,1,1]])

# create a checkerboard pattern
checkerboard = np.tile(block, (2,2))

print( "checkerboard patter with larger squares:" )
print( checkerboard )