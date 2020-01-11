nu_m,l=input(),[]
for i in range(0,len(nu_m)):
  l.append(nu_m[i])
if(len(set(l))==2):print("Saturated")
else:print("Unsaturated")
