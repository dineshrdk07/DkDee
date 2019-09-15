n,k=[int(i) for i in input().split()]
l,l1=list(map(int,input().split()))[:n],[]
for i in l:
  if(l.count(i)<k):
    l1.append(i)
l1=sorted(set(l1))
print(*l1)
