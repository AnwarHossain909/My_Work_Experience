n,m = list(map(int,input().split()))
f = 1
for i in range(1,(m//n)+1):
    a = ""
    for j in range(n):
        a += str(f) + " "
        f += 1
    print(a[:-1])
