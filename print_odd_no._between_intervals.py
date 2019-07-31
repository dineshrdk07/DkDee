interval_1,interval_2=[int(i) for i in input().split()]
for i in range(interval_1+1,interval_2):#the incrementation is due to get rid of first interval count
 if(i%2!=0):
  print(i,end=" ")
