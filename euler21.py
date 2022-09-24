import math
def divisors(a):
    A={}
    A[0]=1
    m=0
    n=1
    for i in range(2,a):
        if a%i==0:
            m+=1
            A[m]=i
            n+=i
    m=0
    return(n)
divisors(126)
m=0
A={}
n=0
for h in range(10000):
    if divisors(divisors(h))== h and not divisors(h)==h :
        if divisors(divisors(divisors(h)))==divisors(h):
          m += divisors(h)+h
          A[n]=h
          n+=1
          A[n]=divisors(h)
          n+=1
print(A)
print(int(m/2))