# Checking if a triangle is valid based on the lengths of its sides.

a = int(input())
b = int(input())
c = int(input())

if a+b>c and a+c>b and b+c>a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")