g_num=int(input())
c_ount=0
for a in range(1,g_num):
  for b in range(1,g_num):
    if((a+b)==g_num):
      c_ount+=1
print(c_ount)
