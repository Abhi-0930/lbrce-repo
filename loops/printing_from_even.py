# Printing whether numbers from 1 to 500 are even or odd using a while loop.

i=1
while i<500:
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i+=1