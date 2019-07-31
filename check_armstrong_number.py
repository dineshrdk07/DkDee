number=input()
a_number=0
for i in range(0,len(number)):
 a_number=a_number+(int(number[i])**len(number))
if(number==str(a_number)):
 print("yes")
else:
 print("no")
