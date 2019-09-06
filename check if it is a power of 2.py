n=int(input())
cnt=0
for i in range(n):
  if(2**i==n):
    cnt+=1
if(cnt>0):
  print('yes')
else:print('no')  
