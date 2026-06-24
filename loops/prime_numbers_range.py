# Program to check prime numbers in a given range

start = int(input())
end = int(input())

for i in range(start, end + 1):
    is_prime = True
    if i <= 1:
        is_prime = False
    for j in range(2, i):
        if (i % j) == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        print(f"{i} is a prime number")