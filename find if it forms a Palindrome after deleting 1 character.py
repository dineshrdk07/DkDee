s,c=input(),0
for i in range(len(s)):
  a=s[:i]+s[i+1:]
  if(a==a[::-1]):
    c=c+1
    break
if(c==1):
  print("YES")
else:
  print("NO")
