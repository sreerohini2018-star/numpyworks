
"""
1D Array Practice

1. Given arr = np.array([3, 6, 9, 12, 15, 18]), extract the 3rd element.


2. From arr = np.array([5, 10, 15, 20, 25, 30]), extract elements from index 2 to 4.


3. Given arr = np.array([2, 4, 6, 8, 10, 12]), extract all even-indexed elements.


4. From arr = np.array([11, 22, 33, 44, 55]), select elements greater than 30.


5. Given arr = np.array([7, 14, 21, 28, 35]), replace all numbers greater than 20 with -1.


6. From arr = np.array([1, 2, 3, 4, 5]), pick elements at positions [0, 2, 4] using advanced indexing.


7. Let arr = np.array([10, 20, 30, 40]). Multiply every element by 2 using broadcasting.


8. Given arr = np.array([100, 200, 300, 400, 500]), reverse the array using advanced indexing.



"""

import numpy as np
arr1 = np.array([3, 6, 9, 12, 15, 18])
print(arr1[2])

arr2 = np.array([5, 10, 15, 20, 25, 30])
print(arr2[2:5])

arr3 = np.array([2, 4, 6, 8, 10, 12])
even_indexed_elements = arr3[::2]
print(even_indexed_elements)

arr4 = np.array([11, 22, 33, 44, 55])
result = arr4[arr4 > 30]
print(result)

arr5 = np.array([7, 14, 21, 28, 35])
arr5[arr5 > 20] = -1
print(arr5)

arr6 = np.array([1, 2, 3, 4, 5])
#indices = [0, 2, 4]
#result = arr[indices]
#print(result)
print(arr6[[0, 2, 4]])

arr7 = np.array([10, 20, 30, 40])
print(arr7 * 2)

arr8 = np.array([100, 200, 300, 400, 500])
print(arr8[::-1])




