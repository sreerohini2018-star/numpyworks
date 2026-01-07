
"""
slicing of onedimensional array
lst=[10,20,30,40,50]
arr=np.array(lst)

fetching a specific element:-
arr[index]
arr[3]=40

slicing syndax:-
arr[start:end] * end excluded
"""
import numpy as np
lst=[10,20,30,40,50,60]
#     0  1  2  3  4  5
arr=np.array(lst)
#getting specific elemnt
print(arr[3])#40
#slicing syndax
#arr[start:end] * end excluded
print(arr[1:4])#[20 30 40]
print(arr[3:6])#[40 50 60]