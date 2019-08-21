stri=input()
odd_pos_char,even_pos_char='',''
for i in range(len(stri)):
  if(i%2==0):
    odd_pos_char=odd_pos_char+stri[i]
  else:
    even_pos_char=even_pos_char+stri[i]
print(odd_pos_char,even_pos_char,sep=" ")
