

"""
[1*5+2*7 1*6+2*8
 3*5+4*7 3*6+4*8]
[5+14   6+16   
15+28  18+32]
[19  22
 43  50]
 """
import numpy as np
arr1=np.array([
    [1,2],
    [3,4]
])
arr2=np.array([
    [5,6],
    [7,8]
])
matrix_mul=np.dot(arr1,arr2)
print(matrix_mul)