
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
total_hours_per_employee = np.sum(productivity, axis=1)
print("Total hours per employee:", total_hours_per_employee)#[76 67 86 55 75 85]

#calculate the total work hours for each day across all employees
total_hours_per_day = np.sum(productivity, axis=0)
print("Total hours per day:", total_hours_per_day)#[43 45 43 44 42 47 46 46 42 46]

#find the average working hours per employee
avg_hours_per_employee = np.average(productivity, axis=1)
print("Average hours per employee:", avg_hours_per_employee)#[7.6 6.7 8.6 5.5 7.5 8.5]

#find the average working hours per day
avg_hours_per_day = np.average(productivity, axis=0)
print("Average hours per day:", avg_hours_per_day)##[7.16666667 7.5 7.16666667 7.33333333 7. 7.83333333 7.66666667 7.66666667 7. 7.66666667]

#identify the employee index who worked the maximum total hours
#emp_index=np.sum(productivity,axis=1)
max_emp_index = np.argmax(total_hours_per_employee)
print("Employee with max hours (index):", max_emp_index)
# 2

#identify the employee index who worked the minimum total hours
#emp_min_index=np.sum(productivity,axis=1)
min_emp_index = np.argmin(total_hours_per_employee)
print("Employee with min hours (index):", min_emp_index)
# 3

#find the day index with the highest total working hours
#emp_index=np.sum(productivity,axis=0)
#print(np.argmax(emp_index))#5
max_day_index = np.argmax(total_hours_per_day)
print("Day with highest total hours (index):", max_day_index)
# 5

#Identify overworked employees (average hours > 8)
#identify emplooyees who are overworked if average hours exceed 8 per day
overworked_employees = np.where(avg_hours_per_employee > 8)[0]
print("Overworked employees (index):", overworked_employees)
# [2 5]

# 9. Difference between the most productive and least productive employee
#calculate the difference between the most productive and least productive emplooyee

difference = np.max(total_hours_per_employee) - np.min(total_hours_per_employee)
print("Difference in total hours:", difference)
# 31


