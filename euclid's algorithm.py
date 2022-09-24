a = int(input("a="))
b = int(input("b="))
d=a
f=b
set_n={}
m=0
c = 1

while a%b != 0:
    c = a % b
    n = a // b
    if a>b:
        a=b
        b=c
    else:
        c=b
        b=a
        a=c

    print(b)
    set_n[m] = n
    m=m+1
print(set_n)
n=m
g=1
m=m-1
e = set_n[m]
m=m-1
while m!=-1:
    if ((n-m)%2)==1:
        e=e+g*set_n[m]
    else:
        g=g+e*set_n[m]
    m=m-1

z=b
if n%2==1:
    print(str(-g) + "*" + str(d) + " + " + str(e) + "*" + str(f) + " = " + str(b))
    print(str(int(d/z))+"*"+str(z)+"="+str(d))
    print(str(int(f / z)) + "*" + str(z) + "=" + str(f))

else:
    print(str(-e) + "*" + str(d) + " + " + str(g) + "*" + str(f)  + " = " + str(b))
    print(str(int(f / z)) + "*" + str(z) + "=" + str(f))
    print(str(int(d / z)) + "*" + str(z) + "=" + str(d))
