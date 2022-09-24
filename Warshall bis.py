import numpy as np
def warshall(M):
    n = len(M)
    W = M
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = (W[i][j] or (W[i][k] and W[k][j]))
    return W
W=[
    [1,0],
    [0,1]
]
print(warshall( W ))