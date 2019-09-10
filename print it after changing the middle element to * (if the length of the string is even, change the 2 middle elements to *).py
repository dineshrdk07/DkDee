c=input()
if(len(c)%2==0):
  mid=int((len(c)/2)-1)
  print(c[:mid]+'*'+'*'+c[mid+2:])
else:
  mid=int((len(c)/2))
  print(c[:mid]+'*'+c[mid+1:])
