
def cont(a,b):
    m=0
    for c in range(len(str(a))):
        if str(b)==str(a)[c]:
            m=m+1
    return(m)
print(cont(123222,2))
def samedig(a,b):
    m=0
    for i in range(0,10):
        if cont(a,i)==cont(b,i):
            m+=1
    return(m==10)
print(samedig(121,112))
def is_permuted(a,b) :
    return(samedig(a,b*a))
m=1
while not is_permuted(m,2) or not is_permuted(m,3)or not is_permuted(m,4)or not is_permuted(m,5)or not is_permuted(m,6):
    m=m+1
print(m,2*m,3*m,4*m,5*m,6*m)


