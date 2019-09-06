a=input()
for i in a:
  if(i==' '):
    b=a.index(i)
    print(a[b+1:],a[:b])
