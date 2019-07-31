number=int(input())
count=0
for i in range(1,number+1):
 if((number%i)==0):
  count=count+1
if(count==2): #Because the prime number is divisible by 1 and itself
 print("yes")
else:
 print("no")
