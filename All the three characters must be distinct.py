c,cnt=input(),0
if(len(c)==3):
  for i in range(len(c)-1):
    if(c[i]!=c[i+1]):
      cnt+=1
else:
  print('0')
if(cnt==2):
  print('1')

