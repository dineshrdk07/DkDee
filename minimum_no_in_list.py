size=int(input())
ls=list(map(int,input().split()))[:size]
minimum=ls[0]
for i in range(1,size):
  if(ls[i]<minimum):
    minimum=ls[i]
print(minimum)
