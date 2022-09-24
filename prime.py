import math
p=1
s={}
s[0]=2
s[1]=3
m=4
n=0
y=5
while m<100000000:
    while s[n]<=math.sqrt(m) and m % s[n]!=0:
        n=n+1
        if s[n]> math.sqrt(m):
            p=p+1
            s[p] = m
            print(p,s[p])
    m = m + 1
    n=0

