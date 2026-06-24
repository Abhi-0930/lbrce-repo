def armstrong(num):
  temp = num 
  sum = 0
  length = len(str(num))
  while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10
  if num == sum:
    print("armstrong")
  else:
    print("not armstrong")
num = int(input())
armstrong(num)