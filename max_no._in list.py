size=int(input())
ls=list(map(int,input().split()))[:size]
maximum=ls[0]
for i in range(1,size):
  if(ls[i]>maximum):
    maximum=ls[i]
print(maximum)
