n=1
p=0
while len(str(9**n))==n:
    for a in range(0,12):
        if len(str(a**n))==n:
            p+=1
    print(n,p)
    n+=1
print(p)