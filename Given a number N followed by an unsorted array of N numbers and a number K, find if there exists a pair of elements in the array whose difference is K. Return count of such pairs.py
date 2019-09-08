n,k=[int(i) for i in input().split()]
a=list(map(int,input().split()))[:n]
l,l1,l2,l3=[],[],[],[]
cnt,cnt1=0,0
for i in range(len(a)-1):
  for j in range(1,len(a)):
    if(a[i]-a[j]==k or a[i]-a[j]==-k):
      cnt+=1
      l.append(a[i])
      l1.append(a[j])
l2=list(zip(l,l1))
l3=list(zip(l1,l))
for i in range(len(l2)):
  for j in range(len(l2)):
    if(l2[i]==l3[j]):
      cnt1+=1
cnt1/=2
print(cnt-int(cnt1))

