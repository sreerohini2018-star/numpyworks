"""
methods_practice
4  4   4   4  4
4  1   1   1  4
4  1  100  1  4
4  1   1   1  4
4  4   4   4  4
"""
import numpy as np
four_arr=np.full((5,5),4)
print(four_arr)
ones_arr=np.ones((3,3),dtype="int16")
ones_arr[1,1]=100
print(ones_arr)
four_arr[1:4,1:4]=ones_arr
print(four_arr)