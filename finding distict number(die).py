n=int(input())
die_roll=list(map(int,input().split()))[:n]
for i in die_roll:
  if(die_roll.count(i)==1):
    print(i)
