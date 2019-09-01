a,b=[int(i) for i in input().split()]
l,l1=[],[]
for i in range(1,a+1):
  if(a%i==0):
   l.append(i)
for i in range(1,b+1):
  if(b%i==0):
   l1.append(i)
sme_value=[i for i in l if i in l1]
print(max(sme_value))
