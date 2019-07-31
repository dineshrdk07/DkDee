interval_1,interval_2=[int(i) for i in input().split()]
for i in range(interval_1+1,interval_2):#to get rid of first count I incremented the first interval( should be between)
 if(i%2==0):
  print(i,end=" ")
