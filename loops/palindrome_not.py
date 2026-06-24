# Checking whether a number is palindrome or not

n = int(input())

temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")