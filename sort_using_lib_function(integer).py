size=int(input())
ls=list(map(int,input().split()))[:size]
ls.sort()
for i in ls:
  print(i,end=" ")
