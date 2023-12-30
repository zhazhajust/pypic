import numpy as np
from typing import Tuple

def downsample_nd_array(arr: np.ndarray, factor: Tuple[int, ...]) -> np.ndarray:
    """
    Downsample a NumPy array by averaging neighboring values.

    Parameters:
    - arr: NumPy array of any dimension
    - factor: Downsampling factor as a tuple of positive integers

    Returns:
    - Downsampled NumPy array
    """
    if not all(f > 0 and isinstance(f, int) for f in factor):
        raise ValueError("Factors should be positive integers.")

    if len(factor) != arr.ndim:
        raise ValueError("Factor should have the same length as the number of array dimensions.")

    if not all(s % f == 0 for s, f in zip(arr.shape, factor)):
        raise ValueError("Each factor should evenly divide the corresponding array dimension.")

    new_shape = tuple(s // f for s, f in zip(arr.shape, factor))

    # Reshape the array into blocks
    reshaped_arr = arr.reshape(new_shape + tuple(factor))

    # Take the mean along each block
    downsampled_arr = reshaped_arr.mean(axis=tuple(range(len(arr.shape), len(arr.shape) + len(new_shape))))

    return downsampled_arr

# Function to reduce array size by averaging neighboring elements
def reduce_array(arr):
    m, n = arr.shape
    return arr.reshape(m//2, 2, n//2, 2).mean(axis=(1, 3))
    