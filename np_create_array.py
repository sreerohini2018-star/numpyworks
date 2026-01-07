#creating a one dimensional array(function of numpy)
import numpy as np
one_d_array=np.array([1,2,3,4])
print("1D-array=" ,one_d_array)
print(type(one_d_array))
#display dimension of array->ndim(attribute)
print("dimension of array= ",one_d_array.ndim)
#multiply 2 with elements of array it wont change the original array
multiply_two=one_d_array*2
print("multiply_two_array= ",multiply_two)