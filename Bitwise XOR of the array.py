no=int(input())
a=list(map(int,input().split()))[:no]  
for i in range(len(a)-1):
  xo_r=a[i]^a[i+1]
print(xo_r)
