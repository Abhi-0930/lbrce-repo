# Calculating the profit or loss based on cost price and selling price.

cp = int(input())
sp = int(input())

if sp > cp:
    print("Profit")
elif sp < cp:
    print("Loss")
elif sp == cp:
    print("No Profit No Loss")