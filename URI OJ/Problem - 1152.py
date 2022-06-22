a = int(input())
n1 = 0
n2 = 1
c = 0
while c < a:
    print(n1,end=" ")
    t = n1+n2
    n1 = n2
    n2 = t
    c += 1
print()
