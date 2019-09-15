class stk:
  def __init__(self):
    self.i=[]
  def push(self,d):
    self.i.append(d)
  def pop(self):
    return self.i.pop()
s,l=input(),[]
st=stk()
for i in s:
  st.push(i)
for i in range(len(s),0,-1):
  l.append(st.pop())
a="".join(l)
if(s==a):
  print('yes')
else:
  print('no')
