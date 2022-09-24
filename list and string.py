# s=[]
#l=list(str(s))
#print(l,type(l),s,type(s))
#print(type(l)==list)
import pandas as pd
import math

def fact(a):

    c = []
    b=2
    while b in range(2,int(math.sqrt(a))):
        # print(a,b,f"{a}%{b}={a%b}")
        if a%b ==0:
            print(a,b)
            c.append(b)
            fact(int(a/b))
        b+=1
    c.append(a)
    return(c)
def factorize():
    a = int(input('Enter a number: '))
    return(fact(a))
print(factorize())