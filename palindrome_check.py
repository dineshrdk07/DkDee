number=input()
numb_pattern=[number.count(i) for i in number]
reverse_num=number[::-1]
reverse_num_pattern=[reverse_num.count(i) for i in reverse_num]
if(numb_pattern==reverse_num_pattern):
 print("yes")
else:
 print("no")
