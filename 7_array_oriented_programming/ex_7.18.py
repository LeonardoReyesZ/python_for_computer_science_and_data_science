# ex_7.18
import numpy as np
from scipy import stats

def median(arr):
    # Flatten the array to make it 1D
    arr_flat = arr.flatten()
    # Sort the array
    arr_sorted = np.sort(arr_flat)
    # Find the median
    n = len(arr_sorted)
    if n % 2 == 0:
        med = (arr_sorted[n//2 - 1] + arr_sorted[n//2]) / 2.0
    else:
        med = arr_sorted[n//2]
    return med

def mode(arr):
    # Flatten the array to make it 1D
    arr_flat = arr.flatten()
    # Calculate the mode using scipy's stats.mode
    mode_result = stats.mode(arr_flat)
    # Check if the result is a scalar or an array
    if mode_result.mode.size == 1:
        return mode_result.mode, mode_result.count
    else:
        return mode_result.mode[0], mode_result.count[0]


# Test the functions on arrays of different shapes
arrays_to_test = [
    np.array([1, 2, 2, 3, 4]),
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    np.array([[1, 1, 2], [3, 4, 4], [5, 6, 7], [8, 9, 9]])
]

for i, arr in enumerate(arrays_to_test):
    print(f"Array {i+1}:\n{arr}")
    print(f"Median: {median(arr)}")
    mode_value, mode_count = mode(arr)
    print(f"Mode: {mode_value} (appears {mode_count} times)\n")
