S=input()
X=input()
if(X in S):
 S=S.replace(X,'')
 print(S.strip())
else:print(S)
