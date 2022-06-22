for _ in range(int(input())):
    n = int(input())
    a = []
    n1 = 0
    n2 = 1
    for i in range(61):
        t = n1 + n2
        a.append(n1)
        n1 = n2
        n2 = t
    print("Fib(%d) = %d"%(n,a[n]))
