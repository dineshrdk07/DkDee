str_ing=input()
if(len(str_ing)%2==0):
 for i in range(0,len(str_ing)-1,2):
   print(str_ing[i+1]+str_ing[i],end='')
else:
  for i in range(0,len(str_ing)-1,2):
   print(str_ing[i+1]+str_ing[i],end='')
  print(str_ing[-1])
