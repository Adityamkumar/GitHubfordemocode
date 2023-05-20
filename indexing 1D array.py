import numpy as np
a=[]
size=int(input("Enter size of list:"))
for i in range(size):
    val=int(input("Enter list element:"))
    a.append(val)
    b=np.array(a)
    for i in range(b.size):
        print(b[i])
        sum=0
        for i in range(b.size):
            sum=sum+b[i]
        print("sum of array element:",sum)
        
    