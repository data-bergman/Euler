import math
p=1
s={}
s[0]=2
s[1]=3
m=4
n=0
y=5
while m<100:
    while s[n]<=math.sqrt(m) and m % s[n]!=0:
        n=n+1
        if s[n]> math.sqrt(m):
            p=p+1
            s[p] = m
            y += m
            print(p,s[p])
    m = m + 1
    n=0

for f in range(s):
    if 1000%(s[f]+(s[f]^2))==0 :
        print (s[f],((s[f]^2)-1)/2,((s[f]^2)+1)/2)
    else:
        print(s[f])
