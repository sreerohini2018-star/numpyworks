#two dimensional stacking
import numpy as np
arr1=np.array([[1,2],
               [3,4]])
arr2=np.array([[10,20],
               [30,40]])

#vertical stacking
v_stack=np.vstack([arr1,arr2])
print("vstack=",v_stack)#[[ 1  2]
                         #[ 3  4]
                         #[10 20]
                         #[30 40]]

#horizontal stacking
h_stack=np.hstack([arr1,arr2])
print("hstack=",h_stack)#[[ 1  2 10 20]
                         #[ 3  4 30 40]]
