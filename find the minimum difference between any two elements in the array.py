n=int(input())
l,l1=[int(i) for i in input().split()],[]
for i in range(len(l)-1):
  for j in range(i+1,len(l)):
    l1.append(abs(l[i]-l[j]))
print(min(l1))
