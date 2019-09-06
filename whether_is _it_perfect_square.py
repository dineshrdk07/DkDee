num1,num2=[int(i) for i in input().split()]
pr=num1*num2
num=int(pr**0.5)
if((num*num)==pr):
  print('yes')
else:
  print('no')
