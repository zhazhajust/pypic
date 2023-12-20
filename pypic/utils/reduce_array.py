# Function to reduce array size by averaging neighboring elements
def reduce_array(arr):
    m, n = arr.shape
    return arr.reshape(m//2, 2, n//2, 2).mean(axis=(1, 3))