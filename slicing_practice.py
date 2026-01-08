
"""
slicing_practice:-

         maths  english  malayalam  cs  social

vipin     43      42        45      34   23

hari      23      45        45      34   37

cibin     37      38        39      40   45
"""
import numpy as np
arr=np.array([
    [43,42,45,34,23],
    [23,45,45,34,37],
    [37,38,39,40,45]
])
print(arr.ndim)
print(arr.size)
print(arr.shape)

#display marks of hari
print(arr[1])
#display maths mark of hari
print(arr[1,0])
#display malayalam marks of all students
print(arr[:,2])
#display malayalam and cs marks of all students
print(arr[:,2:4])
#display english and malayalam marks of hari and cibin
print(arr[1:3,1:3])
#update
arr[2,1]=36
print(arr)