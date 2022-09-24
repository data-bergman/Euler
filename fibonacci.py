n={0:1,1:1}
m=1
while n[m]<=4000000:
    m=m+1
    n[m]=n[m-1]+n[m-2]
    print(m,n[m])
answer=0
for i in range(len(n)):
    if n[i]%2==0: answer += n[i]
print(answer)



