s=input().replace('.','').split()
l=[int(i) for i in s if i.isdigit()==True]
print(max(l))
