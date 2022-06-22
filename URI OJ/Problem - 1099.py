for _ in range(int(input())):
    a,b = map(int,input().split())
    sum = 0
    if a>b:
        for i in range(b+1,a):
            if i%2 == 1:
                sum = sum + i
    else:
        for j in range(a+1,b):
            if j%2 == 1:
                sum = sum + j
    print(sum)
