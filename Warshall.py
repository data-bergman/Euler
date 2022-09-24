import numpy as np
?np.array()
A= np.array([
    [0,0,0,1,0],
    [0,0,1,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
])
B=np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
])
C=A
for i in range(len(A)):
    for j in range(len(A[i])):
        for k in range(len(A)):
            if A[i,j]==1 or (A[i,k]==1 and A[k,j]==1):
                B[i,j]=1
    print(B[i],A[i])
A= np.array([
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,0,1,1],
    [0,0,0,0,1],
    [1,0,0,1,0],
])
B+= -C
for i in range(len(B)):
    print(B[i])
