

import numpy as np
attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
#   

]
arr=np.array(attendance)
#functions
#sum,max,min,avg
#axis=0->coloumn
#axis=1->row

#studentwise attendance
print(np.sum(arr,axis=1))#[5 4 4 3 4 3 4 3 3 4]

#daywise attendace
print(np.sum(arr,axis=0))#[8 7 7 8 7]

#update
arr[9,1]=1
print(arr)#[[1 1 1 1 1]
            #[1 0 1 1 1]
            #[1 1 0 1 1]
            #[0 1 1 1 0]
            #[1 1 1 0 1]
            #[1 0 0 1 1]
            #[1 1 1 1 0]
            #[0 1 1 0 1]
            #[1 1 0 1 0]
            #[1 1 1 1 1]]

#studentwise absent count
#count_nonzero
student_wise_absent_count=np.count_nonzero(arr==0,axis=1)
print(student_wise_absent_count)#[0 1 1 2 1 2 1 2 2 0]

day_wise_absent_count=np.count_nonzero(arr==0,axis=0)
print(day_wise_absent_count)#[2 2 3 2 3]