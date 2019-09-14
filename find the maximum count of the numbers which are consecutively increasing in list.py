n,cnt=int(input()),0
l=list(map(int,input().split()))[:n]
for i in range(len(l)-1):
  if(l[i]<l[i+1]):
    cnt=cnt+1
  else:
    cnt=0
print(cnt+1)
