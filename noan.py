print((3**12)%35)
d=35
def boo(c):
    if c==1:
        return True
    else:
        return False
def order(b):
    a=b
    f=[]
    while a not in(f):
        f.append(a)
        c=a
        a=(b*a)%d
    return(len(f),boo(c))
g={}
for b in range(d):
    g[b]=order(b)
    print(b,order(b))

b=7
a=b
f=[]
while a not in(f):
    f.append(a)
    c=a
    a=(b*a)%d
    print(a)
print(len(f),boo(c))