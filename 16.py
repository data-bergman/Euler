x=2**100
f=0
t=0
while x!=0:
    f+=x%10
    x//=10
    t=t+1
print(f)
