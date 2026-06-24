# Printing numbers from 1 to n and counting them using a for loop.

n=int(input("enter a number:"))
count=0
i=1
for i in range(1,n+1):
    print(i)
    count+=1
print("count:",count)