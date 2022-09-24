k=4
import math
triangle = []
square = []
pentagonal = []
hexagonal = []
heptagonal = []
octogonal = []
def P3(n):
    return(int(n*(n+1)/2))
def P4(n):
    return(int(n**2))
def P5(n):
    return(int(n*(3*n-1)/2))
def P6(n):
    return(int(n*(2*n-1)))
def P7(n):
    return(int(n*(n*5-3)/2))
def P8(n):
    return(int(n*(n*3-2)))
def smallest(function , f):
    n=0
    while function(n)<f:
        n+=1
    return(n)
n=smallest(P3,10**(k-1))
while P3(n)<10**k:
    triangle.append(P3(n))
    n+=1
n=smallest(P4,10**(k-1))
while P4(n)<10**k:
    square.append(P4(n))
    n+=1
n=smallest(P5,10**(k-1))
while P5(n)<10**k:
    pentagonal.append(P5(n))
    n+=1
n=smallest(P6,10**(k-1))
while P6(n)<10**k:
    hexagonal.append(P6(n))
    n+=1
n=smallest(P7,10**(k-1))
while P7(n)<10**k:
    heptagonal.append(P7(n))
    n+=1
n=smallest(P8,10**(k-1))
while P8(n)<10**k:
    octogonal.append(P8(n))
    n+=1
l=math.ceil(k/2)
def ord(n,m):
    return(str(n)[k-l:k]==str(m)[0:l])
f=0
for n in triangle:
    for m in square:
        if ord(n,m):
            for o in pentagonal:
                if ord(m,o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1

                            for q in octogonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in hexagonal:
                if ord(m, o):
                    for p in pentagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in heptagonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in octogonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
    for m in pentagonal:
        if ord(n, m):
            for o in square:
                if ord(m,o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in hexagonal:
                if ord(m, o):
                    for p in square :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in heptagonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in octogonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
    for m in hexagonal:
        if ord(n, m) :
            for o in square:
                if ord(m,o):
                    for p in pentagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in pentagonal:
                if ord(m, o):
                    for p in square :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in heptagonal:
                if ord(m, o):
                    for p in pentagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in octogonal:
                if ord(m, o):
                    for p in pentagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
    for m in heptagonal:
        if ord(n, m):
            for o in square:
                if ord(m,o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in hexagonal:
                if ord(m, o):
                    for p in square :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in pentagonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in octogonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in octogonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in octogonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in octogonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
    for m in octogonal:
        if ord(n, m):
            for o in square:
                if ord(m,o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in hexagonal:
                if ord(m, o):
                    for p in square :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in heptagonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in square:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in pentagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in pentagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in pentagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
            for o in pentagonal:
                if ord(m, o):
                    for p in hexagonal :
                        if ord(o,p):
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in heptagonal :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in square:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in square:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                    for p in square :
                        if ord(o,p):
                            for q in hexagonal:
                                if ord(p,q):
                                    for r in heptagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
                            for q in heptagonal:
                                if ord(p,q):
                                    for r in hexagonal:
                                        if ord(q,r) and ord(r,n):
                                            print(n,m,o,p,q,r,n+m+o+p+q+r)
                                            f+=1
print(f)