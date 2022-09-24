import math
p=1
s={}
s[0]=2
s[1]=3
m=4
n=0
y=5
while m<50000:
    while s[n]<=math.sqrt(m) and m % s[n]!=0:
        n=n+1
        if s[n]> math.sqrt(m):
            p=p+1
            s[p] = m
    m = m + 1
    n=0
def not_coprime(a,c):
    b=[]
    i=0
    while s[i]<int(math.sqrt(a)):
        if a % s[i]==0 and c % s[i]==0:

            return(True)
        i+=1
    return(False)
def phi(a):
    n=0
    for h in range(a):
        if not_coprime(a,h):
            n+=1
    return(a/(a-n))
print(not_coprime(8,19))
print(phi(10))
b=1
for g in range(30030,100001):
    print(g,b)
    b=max(b,phi(g))
print(b)