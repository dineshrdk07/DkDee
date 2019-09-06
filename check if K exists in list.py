n,k=[int(i) for i in input().split()]
a=list(map(int,input().split()))[:n]
if(a.count(k)>=1):
  print('yes')
else:
  print('no')
