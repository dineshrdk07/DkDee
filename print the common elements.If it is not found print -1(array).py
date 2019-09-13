n=int(input())
l,l1,cnt=[[i for i in input().split(" ",5)]for i in range(2)],[],0
for i in l[0]:
  for j in l[1]:
   if(i==j):
     cnt=cnt+1
     l1.append(i)
if(cnt>0):print(' '.join(sorted(set(l1))))
else:print('-1')
    
