def num(a):
  count=0
  for i in range(1,a):
    if a%i==0:
      count+=1
  if count>=2:
    return False
  else:
    return True
a=int(input("enter a number:"))
num(a)