import math
def c_f(n):
    x=[n]
    y=[]
    a=[]
    i=0
    while True:
        a.append(math.floor(x[i]))
        c=1/(x[i]-a[i])
        d=round(c,5)
        if d in y:
            break
        y.append(d)
        i+=1
        x.append(c)
    return(len(y))
print(c_f(math.sqrt(7)))
f=0
for n in range(1,10000):
    if not int(math.sqrt(n))==math.sqrt(n):
        if c_f(math.sqrt(n))%2==1:
            f+=1
            print(n/10000,f/n)
print(f)


