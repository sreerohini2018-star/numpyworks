
import numpy as np
productivity=np.array([
    [8,7,8,6,7,8,9,8,7,8],
    [6,7,6,7,6,7,8,7,6,7],
    [9,8,9,8,9,9,8,9,8,9],
    [5,6,5,6,5,6,6,5,6,5],
    [7,8,7,8,7,8,7,8,7,8],
    [8,9,8,9,8,9,8,9,8,9]
])
print(productivity[productivity<8])#[7 6 7 7 6 7 6 7 6 7 7 6 7 5 6 5 6 5 6 6 5 6 5 7 7 7 7 7]verthe productivity<8 kodthal boolean value kitm


#working hors btw 5 to 7
print(productivity[(productivity>=5) & (productivity<=7)])#[7 6 7 7 6 7 6 7 6 7 7 6 7 5 6 5 6 5 6 6 5 6 5 7 7 7 7 7]


#print working hours of first emplooyee with working hrs<8
first_emp=productivity[:,0]
print(first_emp[first_emp<8])


#print last two emplooyees working hours<7
last2_emp=productivity[:,8:10]
print(last2_emp[last2_emp<7])#[6 6 5]


#mark employee working hr<8 to 0
productivity[productivity<8]=0
print(productivity)#[[8 0 8 0 0 8 9 8 0 8]
                    #[0 0 0 0 0 0 8 0 0 0]
                    #[9 8 9 8 9 9 8 9 8 9]
                    #[0 0 0 0 0 0 0 0 0 0]
                    #[0 8 0 8 0 8 0 8 0 8]
                    #[8 9 8 9 8 9 8 9 8 9]]