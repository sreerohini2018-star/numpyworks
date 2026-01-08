

import numpy as np
leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])

#task1: total leads generated each day
daywise_lead=np.sum(leads,axis=0)
print(daywise_lead)#[180 231 195 198  95]

#task2: total leads from each source
sourcewise_lead=np.sum(leads,axis=1) 
print(sourcewise_lead)#[ 60  93 105 121 140 183 197]

#task3: highest lead day
high_lead_day=np.sum(leads,axis=0)
high_day=np.max(high_lead_day)
print(np.argmax(high_lead_day))#ethramathe indexlan kitan #1
#print(high_lead_day)

#task4: avg leads per source
avg_lead_source=np.average(leads,axis=1)
print(avg_lead_source)#[12.  18.6 21.  24.2 28.  36.6 39.4]

#task5: avg leads per day
avg_lead_day=np.average(leads,axis=0)
print(avg_lead_day)#[25.71428571 33. 27.85714286 28.28571429 13.57142857]

#task6: highest lead source
highest_lsource=np.sum(leads,axis=1)
#high_source=np.max(highest_lsource)
print(np.argmax(highest_lsource))#6