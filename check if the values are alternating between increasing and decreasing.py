n=int(input())
a=list(map(int,input().split()))[:n]
cnt=0
for i in a:
  if(i>i+1):
    print('NO')
    break
  cnt+=1
if(cnt==n):
  print('yes')

