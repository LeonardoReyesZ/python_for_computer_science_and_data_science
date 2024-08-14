# ex_7.13: Numpy broadcasting rules
import numpy as np

# Example 1: Adding a scalar to a 1D array
array_1d = np.array([1, 2, 3])
scalar = 2
result = array_1d + scalar
print("Example 1:\n", result)
# Broadcasting applies scalar addition to each element

# Example 2: Adding a 1D array to a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d = np.array([1, 2, 3])
result = array_2d + array_1d
print("\nExample 2:\n", result)
# Broadcasting matches the 1D array to each row of the 2D array

# Example 3: Broadcasting with different shapes
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
array_1d = np.array([1, 0, 1])
result = array_3d + array_1d
print("\nExample 3:\n", result)
# Broadcasting the 1D array across each "depth" of the 3D array

# Example 4: Scalar and a 2D array
array_2d = np.array([[1, 2], [3, 4]])
scalar = 10
result = array_2d * scalar
print("\nExample 4:\n", result)
# Broadcasting the scalar to each element in the 2D array

# Example 5: Different shapes, broadcasting over a new axis
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_1d_col = np.array([[1], [2]])
result = array_2d + array_1d_col
print("\nExample 5:\n", result)
# Broadcasting the 1D array as a column over the 2D array

# Example 6: Broadcasting with compatible shapes
array_1d = np.array([1, 2, 3])
array_2d = np.array([[1], [2], [3]])
result = array_1d + array_2d
print("\nExample 6:\n", result)
# Broadcasting 1D array across rows of 2D array
