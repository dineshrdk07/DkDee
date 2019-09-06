n=int(input())
a=list(map(int,input().split()))[:n]
an_d=1
for i in range(n):
  an_d=an_d&a[i]
print(an_d)
