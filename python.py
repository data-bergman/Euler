n = 1
a = 111111
while 1 != a :
  x = a%2
  if 0 == x:
      a = int(a/2)
  else:
       a = 3*a+1
  n = n+1
  print(a)

print("n")
print(n)