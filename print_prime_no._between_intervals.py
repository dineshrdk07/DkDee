interval_1,interval_2=[int(i) for i in input().split()]
for i in range(interval_1+1,interval_2):
 count=0
 for j in range(1,i+1):
  if(i%j==0):
   count=count+1
 if(count==2):
  print(i,end=" ")
   
