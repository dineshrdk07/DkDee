n=int(input())
l,l1,l2=list(map(int,input().split()))[:n],[],[]
for i in l:
  if(l.count(i)>1):
    l1.append(i)
    l2.append(l.count(i))
print(l1[l2.index(max(l2))])
