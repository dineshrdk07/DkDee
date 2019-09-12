n,k=[int(i) for i in input().split()]
l=list(map(int,input().split()))[:n]
if k in l:
  print('yes')
else:
  print('no')
