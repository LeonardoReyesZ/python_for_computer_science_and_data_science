# ex_7.19
import numpy as np
from scipy import stats

def median(arr, axis=None):
    if axis is None:
        # Flatten the array to make it 1D if no axis is specified
        arr_flat = arr.flatten()
        return np.median(arr_flat)
    else:
        # Compute median along the specified axis
        return np.median(arr, axis=axis)
# end median

def mode(arr, axis=None):
    if axis is None:
        # Flatten the array to make it 1D if no axis is specified
        arr_flat = arr.flatten()
        mode_result = stats.mode(arr_flat)
        # Check if the result is a scalar or an array
        if mode_result.mode.size == 1:
            return mode_result.mode, mode_result.count
        else:
            return mode_result.mode[0], mode_result.count[0]
    else:
        # Compute mode along the specified axis
        mode_result = stats.mode(arr, axis=axis)
        return mode_result.mode, mode_result.count
# end mode

# Test the functions on arrays of different shapes
arrays_to_test = [
    np.array([1, 2, 2, 3, 4]),
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    np.array([[1, 1, 2], [3, 4, 4], [5, 6, 7], [8, 9, 9]])
]

for i, arr in enumerate(arrays_to_test):
    print(f"Array {i+1}:\n{arr}")
    print(f"Median (overall): {median(arr)}")
    mode_value, mode_count = mode(arr)
    print(f"Mode (overall): {mode_value} (appears {mode_count} times)")

    if arr.ndim == 2:
        print(f"Median (axis=0): {median(arr, axis=0)}")
        print(f"Median (axis=1): {median(arr, axis=1)}")
        mode_values, mode_counts = mode(arr, axis=0)
        print(f"Mode (axis=0): {mode_values} (appears {mode_counts} times)")
        mode_values, mode_counts = mode(arr, axis=1)
        print(f"Mode (axis=1): {mode_values} (appears {mode_counts} times)")
    print()
