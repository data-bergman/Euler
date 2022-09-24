import math
def smallest(function , f):
    n=0
    while function(n+1)<f:
        n+=1
    return(n)
def cube(n):
    return n**3
for a in range(7,30):
    s={}
    t={}
    c=math.ceil(10**(a/3))
    d=math.ceil(10**((a+1)/3))
    for b in range (c,d):
        s[b]=b**3
        t[b]=1
        for i in range(c,b):
            if sorted(str(s[i]))==sorted(str(s[b])):
                t[i]+=1
    print(max(t, key=t.get),t[max(t, key=t.get)])
    print(s)