import random
import numpy as np
def simpict(n,r,p):
    f=r*p
    l= [0] * n
    y=list(range(n))
    for i in range(f):
        random.shuffle(y)
        x=y[0:3]
        g=l.index(min([l[i] for i in x]))
        l[g]+=1
    return(sum([l[i]-int(bool(l[i])!=0)for i in range(n)]))
m=[0]*1000
for i in range(1000):
    m[i]=simpict(72,10,7)
print(np.mean(m))
print(m)
