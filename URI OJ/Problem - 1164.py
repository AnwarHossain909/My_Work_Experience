for _ in range(int(input())):
    n = int(input())
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s += i
    if s == n:
        print("%d eh perfeito"%s)
    else:
        print("%d nao eh perfeito"%n)
