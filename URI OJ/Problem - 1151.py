a = int(input())
n1 = 0
n2 = 1
l = []
for i in range(n1,a):
    l.append(n1)
    t = n1+n2
    n1 = n2
    n2 = t
print(*l)
