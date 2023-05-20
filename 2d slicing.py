import numpy as np
np.random.seed(111)
a=np.random.randint(1,500,30).reshape(6,5)
b=a[4:,0:2]
print(b)