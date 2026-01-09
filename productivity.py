
import numpy as np
productivity=np.array([
    [8,7,8,6,7,8,9,8,7,8],
    [6,7,6,7,6,7,8,7,6,7],
    [9,8,9,8,9,9,8,9,8,9],
    [5,6,5,6,5,6,6,5,6,5],
    [7,8,7,8,7,8,7,8,7,8],
    [8,9,8,9,8,9,8,9,8,9]
])

#calculate the total number of hoursbworked by each emplooyee over 10 days
print(np.sum(productivity,axis=1))#[76 67 86 55 75 85]
#calculate the total work hours for each day across all employees
print(np.sum(productivity,axis=0))#[43 45 43 44 42 47 46 46 42 46]
#find the avg working hour per emplooyee
print(np.average(productivity,axis=1))#[7.6 6.7 8.6 5.5 7.5 8.5]
#find the avg working hour per day
print(np.average(productivity,axis=0))#[7.16666667 7.5 7.16666667 7.33333333 7. 7.83333333 7.66666667 7.66666667 7. 7.66666667]
#identify the emplooyee index who worked the maximum total hours
emp_index=np.sum(productivity,axis=1)
print(np.argmax(emp_index))#2
#identify the emplooyee index who worked the minimum total hours
emp_min_index=np.sum(productivity,axis=1)
print(np.argmin(emp_min_index))#3
#find the day index with the highest total working hour
emp_index=np.sum(productivity,axis=0)
print(np.argmax(emp_index))#5
#identify emplooyees who are overworked if average hours exceed 8 per day
#calculate the difference between the most productive and least productive emplooyee
