s,l=input().split(),[]
for i in s:
  l.append(sorted(i))
for i in l:
  print(*i,sep='',end=' ')
