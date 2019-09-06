no=int(input())
a=list(map(int,input().split()))[0:no]
o_r=0
for i in range(no):
  o_r|=a[i]
print(o_r)

  
