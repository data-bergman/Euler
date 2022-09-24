m=2
p=2
while m<=4000000:
    p=p+m
    m= round(((1.61803399)**3)*m)
    print(m)
print(p)


