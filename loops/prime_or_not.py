# Checking if a number is prime or not using a for loop.

n = int(input())

is_Prime = True

if n <= 1:
    is_Prime = False
for i in range(2,n):
    if (n % i) == 0:
        is_Prime = False
        break
    else:
        is_Prime = True

if is_Prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")