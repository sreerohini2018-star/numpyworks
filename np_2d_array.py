
"""
2d-array=rows and columns
1 2 3
4 5 6 
7 8 9
"""
import numpy as np
two_dimensional_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("dimension = ",two_dimensional_array.ndim)
#size attribute will return total number of elements
print("size of array = ",two_dimensional_array.size)
#shape attribute will return number ofrows and columns
print("rows and coloumns = ",two_dimensional_array.shape)