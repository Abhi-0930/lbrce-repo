# Calculating the sum of even numbers from 1 to n using a for loop.

n = int(input())
even_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i

print(even_sum)