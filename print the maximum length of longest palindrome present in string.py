from itertools import permutations
s,l,l1=input(),[],[]
for i in range(2,len(s)+1):
  for j in permutations(s,i):
    l.append("".join(j))
for i in l:
  if(i==i[::-1]):
    l1.append(i)
print(len(l1[-1]))
