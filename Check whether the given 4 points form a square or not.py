l=[[int(i) for i in input().split()]for i in range(4)]
a=((((l[0][1])-(l[0][0]))**2)-(((l[1][1])-(l[1][0]))**2))**0.5
b=((((l[2][1])-(l[2][0]))**2)-(((l[3][1])-(l[3][0]))**2))**0.5
if(a==b):
  print('yes')
else:
  print('no')
