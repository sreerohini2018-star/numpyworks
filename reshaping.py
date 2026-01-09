

#reshape(arr,shape)
#to change dimension.but the shape should match with the number of elements.
#for and (3,3) array the number of elements shpould be 9.
import numpy as np
arr1=np.array([1,2,3,4,5,6])
new_arr=np.reshape(arr1,shape=(3,2))
print(new_arr)#[[1 2]
               #[3 4]
               #[5 6]]