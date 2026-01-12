"""
flattening methods
np.ravel
arr.flatten
"""
import numpy as np
arr=np.array([[10,20],[30,40],[50,60]])
#new_array=np.ravel(arr)
#print(new_array)#[10 20 30 40 50 60]
new_array=arr.flatten()
print(new_array)#[10 20 30 40 50 60]


arr1=np.array([[1,2,3],[4,5,6]])
#print(np.ravel(arr1))#[1 2 3 4 5 6]
print(arr1.flatten())#[1 2 3 4 5 6]


