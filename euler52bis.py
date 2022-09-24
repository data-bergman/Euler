
def product(a,b,c,d,e,f,g,h,i):
    m=1
    while not sorted(str(a*m))==sorted(str(b*m))==sorted(str(c*m))==sorted(str(d*m))==sorted(str(e*m))==sorted(str(f*m))==sorted(str(g*m))==sorted(str(h*m))==sorted(str(i*m)):
        m+=1
    print(m,m*a,b*m,c*m,d*m,e*m,f*m,g*m,h*m,i*m)
product(1,2,3,4,5,6,6,6,6)
def product([]):
    