def sumfact(a):
    y=1
    z=0
    for i in range(1,a+1):
        y*=i
        z+=y
    return(z)

def fact(a):
    y=1
    for i in range(1,a+1):
        y*=i
    return(y)
print(fact(100))

def sum_digits(b):
    c=str(b)
    z=0
    for i in range(len(c)):
        z+=int(c[i])
    return(z)

print(sum_digits(fact(100)))