import numpy as np
a=np.array([2,5,7,8,9,])
x=np.searchsorted(a,6,side='right')
print(x)