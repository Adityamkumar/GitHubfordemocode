import numpy as np
matrix1=[]
row=int(input("Enter number of rows:"))
col=int(input("Enter number of col:"))
for i in range(row):
    a=[]
    for j in range(col):
        val=int(input("Enter number:"))
        a.append(val)
    matrix1.append(a)
a=np.array(matrix1)
for i in range(row):
    for j in range(col):
        print(a[i][j],end="  ")
    print()
    
    matrix2=[]
row=int(input("Enter number of rows:"))
col=int(input("Enter number of col:"))
for i in range(row):
    b=[]
    for j in range(col):
        val=int(input("Enter number:"))
        b.append(val)
    matrix2.append(b)
b=np.array(matrix2)
for i in range(row):
    for j in range(col):
        print(b[i][j],end="  ")
    print()

    matrix3=[]
for i in range(row):
    c=[]
    for j in range(col):
        d=a[i][j]+b[i][j]  
        c.append(d)  
    matrix3.append(c)
c=np.array(matrix3)
print("Addition of matrix=")
print(c)



    

    