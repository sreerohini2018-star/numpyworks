
#np.where(condition,true_value,false_value)
#return the condition meeting index

import numpy as np
arr=np.array([10,20,18,25,35,11])
print(np.where(arr>=20,"adult","teen"))#['teen' 'adult' 'teen' 'adult' 'adult' 'teen']


