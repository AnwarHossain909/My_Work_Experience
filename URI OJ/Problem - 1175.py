a = []
for i in range(20):
    x = int(input())
    a.append(x)
p = 0
for l in a[::-1]:
    print("N[%d] = %d"%(p,l))
    p += 1
