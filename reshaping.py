import numpy as np
arr=np.random.randint(1,50,12)
print(arr)
print(arr.shape)
arr=arr.reshape(6,-1)
print("After reshaping=",arr)
