c,l=input(),[]
for i in c:
  if(ord(i)==88):
    l.append('A')
  elif(ord(i)==89):
    l.append('B')
  elif(ord(i)==90):
    l.append('C')
  elif(ord(i)==120):
    l.append('a')
  elif(ord(i)==121):
    l.append('b')
  elif(ord(i)==122):
    l.append('c')
  else:
    l.append(chr(ord(i)+3))
print(*l,sep='')
