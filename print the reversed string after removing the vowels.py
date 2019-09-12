n=int(input())
s,vs=input()[:n],''
for i in s:
  if i not in ['a','e','i','o','u']:
    vs=vs+i
print(vs[::-1])
  
