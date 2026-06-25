def buzz_number(start,end):
    for i in range(start, end + 1):
        if i % 7 == 0 or '7' in str(i):
            print(i, end = ' ')
    return None

start, end = map(int, input().split())
buzz_number(start, end)