leap_yr=int(input())
if(leap_yr%4==0 and leap_yr%100!=0 or leap_yr%400==0):
 print("yes")
else:
 print("no")
