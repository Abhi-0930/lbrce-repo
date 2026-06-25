def square_root(n): 
    i = 1    
    while i * i <= n:
        if i * i == n:
            return i
        i += 1
    return None

n = int(input())
print(square_root(n))