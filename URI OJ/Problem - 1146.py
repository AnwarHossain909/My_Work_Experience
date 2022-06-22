while True:
    n = int(input())
    if n == 0:
        break
    s = []
    for i in range(1,n+1):
        s.append(i)
    print(*s)
