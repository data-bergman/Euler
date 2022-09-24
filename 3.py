import math
p=0
nth_prime_number={}
nth_prime_number[0]=2
m=3
n=0
x=600851475143
y = math.sqrt(x)
while m<y:
    while n>=0 and m % nth_prime_number[n]!=0:
        n=n-1
        if n == -1:
            p=p+1
            nth_prime_number[p] = m
            q=maths.sqrt(m)
            t=0
            while nth_prime_number[t]>=q:
                t=t-1
    n=p
    m=m+1

for x in range(len(nth_prime_number)):
	print (x,nth_prime_number[x])
while p>0 and x%nth_prime_number[p]!=0:
    p=p-1

    print(p)
