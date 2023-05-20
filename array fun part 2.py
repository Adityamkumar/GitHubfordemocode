import numpy as np
np.random.seed(122)
matrix=np.random.randint(1,21,9).reshape(3,3)
print(matrix)
print(np.sum(matrix,axis=0))#for colomun wise sum
print(np.cumsum(matrix))
print(np.sum(matrix,axis=1))#for row wise sum
print(np.max(matrix,axis=1))#for max value in our matrix for row wise
print(np.min(matrix,axis=0))#for min value in our matrix for colomun wise
