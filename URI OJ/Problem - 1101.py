while True:
    a,b = map(int,input().split())
    sum = 0
    li = []
    if a<b:
        if a>0 and b>0:
            for i in range(a,b+1):
                li.append(i)
                sum += i
        else:
            break
    else:
        if a>0 and b>0:
            for j in range(b,a+1):
                li.append(j)
                sum += j
        else:
            break
    print(*li,"Sum=%d"%(sum))
