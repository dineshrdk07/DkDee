n,l=input(),[]
for i in n:
  l.append(n.count(i))
print(n[l.index(max(l))])
