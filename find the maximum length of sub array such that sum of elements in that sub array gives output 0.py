from itertools import permutations
n,pl,al=int(input()),[],[]
l=list(map(int,input().split()))[:n]
for i in range(2,n+1):
  for j in permutations(l,i):
    pl.append(j)
for i in range(len(pl)):
  s=0
  for j in range(len(pl[i])):
    s=s+pl[i][j]
  if(s==0):
   al.append(pl[i])
print(len(al[-1]))
