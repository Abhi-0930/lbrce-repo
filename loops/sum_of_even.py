# Printing the sum of even numbers from 1 to n using a for loop.

n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if i%2==0:
        count+=1
print("count: ",count)