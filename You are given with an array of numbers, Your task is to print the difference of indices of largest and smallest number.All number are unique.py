n=int(input())
l=list(map(int,input().split()))[:n]
print(l.index(max(l))-l.index(min(l)))
