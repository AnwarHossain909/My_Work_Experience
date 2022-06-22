a = []
b = []
for i in range(15):
    c = int(input())
    if c%2==0:
        a.append(c)
    else:
        b.append(c)

    if (len(a)==5):
        i = 0
        for j in a:
            print("par[%d] = %d"%(i,j))
            i+=1
        a = []
    if (len(b)==5):
        i = 0
        for j in b:
            print("impar[%d] = %d"%(i,j))
            i += 1
        b = []
if (len(b)>0):
    i = 0
    for j in b:
        print("impar[%d] = %d"%(i,j))
        i += 1
if (len(a)>0):
    i = 0
    for j in a:
        print("par[%d] = %d"%(i,j))
        i += 1
