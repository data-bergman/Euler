import math
def smallestcommonfactor(c):
    p=1
    s={}
    s[0]=2
    s[1]=3
    m=4
    n=0
    y=5
    while m<c:
        while s[n]<=math.sqrt(m) and m % s[n]!=0:
            n=n+1
            if s[n]> math.sqrt(m):
                p=p+1
                s[p] = m
        m = m + 1
        n=0
    p=1
    for m in range(len(s)):
        p*= s[m] ** (math.floor(int(math.log(c,s[m]))))
        if math.floor(int(math.log(c,s[m])))!=1 or m==len(s)-1:
            print(s[m],math.floor(int(math.log(c,s[m]))),s[m] ** (math.floor(int(math.log(c,s[m])))),p)
    m=0
    for i in range(1,c+1):
        if p%i==0:
            m += 1
    print(m==c)
    return(p)

smallestcommonfactor(20000)



