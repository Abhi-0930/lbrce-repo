# Counting the number of even and odd numbers from 1 to n using a for loop.

n=int(input("enter a number:"))
odd_count=0
even_count=0
for i in range(1,n+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even_count",even_count)
print("odd_count",odd_count)
