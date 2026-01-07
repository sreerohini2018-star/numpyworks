#numpy means numerical python
import numpy as np
array=np.array([
    [33,32,25],
    [32,35,29],
    [30,36,31]
      
])
print(array.ndim)
print(array.size)
print(array.shape)
#fetch 0th row
print(array[0])
print(array[2])
#syntax arr[row,col]
#row slicing
print(array[1:3])#row matre changechythllu
#fetching rows from 0 to 1
print(array[0:2])#[[33 32 25]
                 #[32 35 29]]
#coloumn slicing
print(array[:,1:3])#[[32 25]
                    #[35 29]
                    #[36 31]]

print(array[:,0:2])#[[33 32]
                    #[32 35]
                    #[30 36]]
#or print(array[:,1:2]) 
print(array[:,1])#[32 35 36]  
#2nd row vnda 
print(array[::2]) #start:stop:step   # [[33 32 25]
                                       #[30 36 31]]           
print(array[2,1]) #36  
print(array[1:3,1:3])  #[[35 29]
                        #[36 31]] 
#skipping 2nd column
print(array[:,::2])   #[[33 25]
                       #[32 29]
                       #[30 31]]                                                      