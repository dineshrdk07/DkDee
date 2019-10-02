st_r,st_r1=input().split()
cnt=0
for i in range(len(st_r)):
  if st_r[i] in st_r1:
    cnt=cnt+1
if(cnt==len(st_r1)):print("true")
else:print("false")
