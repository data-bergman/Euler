f=set()
for a in range(2,101):
    for b in range(2,101):
        f.add(a**b)
print(len(f))
