for _ in range(int(input())):
    a,b,c,d = input().split()
    a = int(a)
    b = int(b)
    c = float(c)
    d = float(d)
    s = 0
    while a<=b:
        aa = int(a*(c/100))
        bb = int(b*(d/100))
        s +=1
        a += aa
        b += bb
        if (s>100):
            break
    if (s>100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos."%s)
