m=1000
for i in range(1,m):
    for o in range(i,m):
        if i*o % 12==0:
            for p in range(o,m) :
                    if i+o+p==m and (p)**2 == (o)**2+(i)**2:
                        print(i,o,p,(i)*(o)*(p))