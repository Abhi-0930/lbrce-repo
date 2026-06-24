# Checking whether a number is an armstrong number or not

n = int(input())

sum = 0
temp = n
length = len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if n == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")