# Calculating the sum of numbers from 1 to n using a for loop.

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)