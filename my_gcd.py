a=list(map(int,input().split()))
b,c=[],[]
for i in a:
  for j in range(1,i+1):
    if(i%j==0):
      b.append(j)
for i in b:
  if(b.count(i)>1):
    c.append(i)
print(max(c))


