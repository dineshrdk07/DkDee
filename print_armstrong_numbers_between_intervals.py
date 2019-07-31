interval_1,interval_2=[int(i) for i in input().split()]
for i in range(interval_1+1,interval_2):
 number=0
 for j in range(0,len(str(i))):
  d=str(i)
  number=number+(int(d[j])**len(str(i)))
 if(i==number):
  print(number,end=" ")
