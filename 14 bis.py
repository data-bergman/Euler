r=1000000
p={1: 1}
for c in range(r):
    n={}
    n[0]=c+1
    t=0
    while n[t]!=1 and not(c+1 in p.keys()) :
        if n[t]%2 ==0:
            n[t+1]=int(n[t]/2)
        else: n[t+1]= n[t]*3+1
        t+=1
    if not(c+1 in p.keys()):
        for s in range(t):
            p[n[s]]=(len(n)-s)
for x in range(r):
	print (x+1,p[x+1])
w = max(p, key=p.get)
print(w,p[w])


