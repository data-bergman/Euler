n=4
m=4
a=[[1 for l in range(m)] for f in range(n)]

print(a)


def is_play(y, x, a):
    try:
        return (a[x][y] == 1)
    except IndexError:
        return (False)


def play(y,x,a):
    if(is_play(y,x,a)):
        b=[a[p] for p in range(x)]+[[a[p][l] for l in range(y)]+[0 for l in range(len(a[1])-y)] for p in range(len(a)-x)]
        return(b)
    else:
        return("invalid_move")


# print(*play(3,2,a),sep='\n')
c=play(1,2,a)
print(*c,sep='\n')

def plays(a):
    b=[]
    for x in range(len(a)):
        y=0
        while is_play(x,y,a) and not((y,x) in b):
            b.append((y, x))
            y += 1

    return(b)

print(*plays(c),sep='\n')




l=[[1 for l in range(m)] for f in range(n)]
def same(a,b):
    o=0
    for n in range(len(a)):
        for m in range(len(a[1])):
            o+=int(a[n][m]==b[m][n])
    return(bool(o) or a==b)

d=play(2,1,a)
print(same(c,d))

