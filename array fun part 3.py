import numpy as np
np.random.seed(122)
matrix=np.random.randint(1,21,10)
np.random.shuffle(matrix)#it will shuffle the matrix values
print(matrix)
a=np.array([10,20,30,10,30,20,50])
print(np.unique(a.size))#UNIQUE function will remove the dupliicates from array,if we will give (.size) it will tell you the size of array#
print(np.unique(a,return_index=True,return_counts=True))#this function returns the index value and frequency of numbers of unique elements#