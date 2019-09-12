n=int(input())
l,s,j=list(map(int,input().split()))[:n],0,0
for i in range(n):
  sc=0
  for k in range(j,n):
    sc=sc+l[k]
  j=j+1
  print(sc,end=" ")
 
