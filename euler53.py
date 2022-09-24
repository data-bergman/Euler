def reverse(a):
    return(int(str(a)[::-1]))
def palindrome(b):
    return(str(b)[::-1]==str(b))
print(palindrome(1))
def lycrel_number(c,e):
    d=c+reverse(c)
    i=1
    while i<e and not palindrome(d) :
        d+=reverse(d)
        i+=1
    return(i==e)
print(lycrel_number(197,200))
def lycrel_in(f,g):
    m=0
    for i in range(f):
        if lycrel_number(i,g):
            m+=1
    print(m)
    return(m)
print(lycrel_in(10000,50)-lycrel_in(10000,2000))