
import numpy as np
prices=np.array([100,120,450,75])
discount_price=prices-10
print("discount price =",discount_price)#[ 90 110 440  65]
new_price=prices+10
print("new price =",new_price)#[110 130 460  85]


arr1=np.array([[1,2],
               [3,4]])
arr2=np.array([[10,20],
               [30,40]])
print(arr1+arr2)#[[11 22]
                 #[33 44]]


arr3=np.array([[1,2],
               [3,4]])
arr4=np.array([10,20])
print(arr3+arr4)#[[11 22]
                 #[13 24]]                 