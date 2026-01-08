
#array creation methods
#np.array()
#np.ones((r,c))
#np.zeros((r,c))#by default float aayirkm datatype kodknm
#np.full((r,c),value)
#np.random.rand(size)
#np.random.randint(low,high,(size))

import numpy as np

zero_array=np.zeros((2,3),dtype="int16")
print(zero_array)#[[0 0 0]
                  #[0 0 0]]

ones_array=np.ones((3,3),dtype="int16")
print(ones_array)#[[1 1 1]
                  #[1 1 1]
                  #[1 1 1]]

five_array=np.full((2,3),5)
print(five_array)#[[5 5 5]
                  #[5 5 5]]

random_array=np.random.rand(3,4)
print(random_array)#[[0.56767252 0.69138753 0.74013075 0.41477569]
                    #[0.20302336 0.32015377 0.2447585  0.95973895] output changes in each run due to random func()
                    #[0.79589968 0.08923141 0.89285878 0.9930827 ]]

randint_array=np.random.randint(10,15,(2,3))
print(randint_array)#[[11 14 12]
                     #[13 10 11]]

