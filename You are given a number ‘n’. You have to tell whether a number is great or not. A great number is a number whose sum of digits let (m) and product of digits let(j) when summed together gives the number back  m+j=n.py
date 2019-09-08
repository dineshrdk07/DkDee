n=input()
a,b,s,p=int(n),list(map(int,n)),0,1
for i in range(len(n)):
  s+=b[i]
  p*=b[i]
if((s+p)==a):
  print('Great')
else:
  print('Not')
