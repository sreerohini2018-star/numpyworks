

import numpy as np
#np.loadtxt(file_path,delimeter=,skip_rows)
data=np.loadtxt("file_works\\sales_data\\sales.csv",delimiter=",",skiprows=2,dtype="str")
print(data)
units_sold=data[:,3].astype("int")
print(np.sum(units_sold),"total units sold")#79
print("max unit",np.max(units_sold))#15
print("min unit",np.min(units_sold))#3
print("avg unit",np.average(units_sold))#7.9
revenue=data[:,3].astype("int")*data[:,4].astype("float")
print(revenue)#[275000. 240000. 210000.  35000.  32000. 315000. 168000.  28800.  49200. 279000.]
print("total revenue=",np.sum(revenue))# 1632000.0


#unit sold>8
print("units sold gt8=",data[data[:,3].astype("int")>8])# [['2025-01-01' 'Mobile' 'Electronics' '12' '20000' 'North']
 #['2025-01-02' 'Chair' 'Furniture' '10' '3500' 'West']
 #['2025-01-03' 'Mobile' 'Electronics' '15' '21000' 'North']
 #['2025-01-05' 'Tablet' 'Electronics' '9' '31000' 'North']]


#category==electronics
category=data[:,2]
print("electronics=",data[category=="Electronics"])#[['2025-01-01' 'Laptop' 'Electronics' '5' '55000' 'South']
 #['2025-01-01' 'Mobile' 'Electronics' '12' '20000' 'North']
 #['2025-01-02' 'Tablet' 'Electronics' '7' '30000' 'East']
 #['2025-01-03' 'Mobile' 'Electronics' '15' '21000' 'North']
 #['2025-01-04' 'Laptop' 'Electronics' '3' '56000' 'East']
 #['2025-01-05' 'Tablet' 'Electronics' '9' '31000' 'North']]

#all product flat 100 offer
price=data[:,4].astype("int")-100
data[:,4]=price
print("discount=",data)

#total revenue of  north region
north=data[data[:,-1]=="North"]
#print(north)
revenue_north=north[:,3].astype("int")*north[:,4].astype("int")
print("total revenue=",np.sum(revenue_north))#830400