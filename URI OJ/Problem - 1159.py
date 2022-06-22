while True:
    x = int(input())
    if x == 0:
        break
    s = 0
    c = 0
    while x:
        if x%2 == 0:
            s += x
            c += 1
            if c == 5:
                break
        x += 1
    print(s)
