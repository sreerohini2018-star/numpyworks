

"""
9. Let arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). Extract the first row.


10. From the same array, extract the last column.


11. From arr = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), select elements greater than 10.


12. Use advanced indexing to select elements at positions (0,0), (1,1), and (2,2) from the above array.


13. Given arr = np.array([[1, 2], [3, 4], [5, 6]]), multiply every element by 5 using broadcasting.


14. From arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), extract the subarray [[3,4],[7,8]].


15. Given arr = np.array([[2, 4], [6, 8], [10, 12]]), multiply only the first column by 10 using broadcasting.


"""


import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1[0])#[1 2 3]

print(arr1[:, -1])#[3 6 9]

arr2 = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
result = arr2[arr2 > 10]
print(result)#[12 14 16 18]

result = arr2[[0, 1, 2], [0, 1, 2]]
print(result)#[ 2 10 18]

arr3 = np.array([[1, 2], [3, 4], [5, 6]])
result = arr3 * 5
print(result)#[[ 5 10]
              #[15 20]
              #[25 30]]

arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
subarray = arr4[0:2, 2:4]  # rows 0-1, columns 2-3
print(subarray)#[[3 4]
                #[7 8]]

arr5 = np.array([[2, 4], [6, 8], [10, 12]])
arr5[:, 0] = arr5[:, 0] * 10
print(arr5)#[[ 20   4]
            #[ 60   8]
            #[100  12]]




