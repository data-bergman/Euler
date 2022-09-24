import math
def P3(n):
    return(int(n*(n+1)/2))
def P5(n):
    return(int(n*(3*n-1)/2))
def P6(n):
    return(int(n*(2*n-1)))

pentagonal = []
hexagonal = []
k=10
n=1
while P5(n)<10**k:
    pentagonal.append(P5(n))
    n+=1
n=1
while P6(n)<10**k:
    hexagonal.append(P6(n))
    n+=1
n=287
while P3(n) not in pentagonal or P3(n) not in hexagonal:
    n+=1
    if n%100==0:
        print(n, math.log(P3(n), 10))
print(n,P3(n))

