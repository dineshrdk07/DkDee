n=bin(int(input()))
a,b=str(n.lstrip('0b')),0
for i in range(0,len(a)):
  if(a[i]=='1'):
   b=i
print(len(a)-b)
