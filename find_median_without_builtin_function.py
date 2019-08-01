size=int(input())     
ls=list(map(int,input().split()))[:size]
ls.sort()
if(size%2==0):
  middle=int(size/2)
  median=(ls[middle]+ls[middle+1])/2
  print(median)
else:
  middle=int(size/2)
  print(ls[middle])

