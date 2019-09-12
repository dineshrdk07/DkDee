n,cnt=int(input()),0
l=list(input() for i in range(n))
for i in l:
  a=0
  for j in i:
    if j in ['a','e','i','u','o']:    
      a=1
  cnt=cnt+a
if(cnt==len(l)):print('yes')
else:print('no')
