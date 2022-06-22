e = o = p = n = 0
for _ in range(5):
    x = int(input())
    if x%2==0:
        e += 1
    if x%2==1:
        o += 1
    if x>0:
        p += 1
    if x<0:
        n += 1
print("%d valor(es) par(es)"%e)
print("%d valor(es) impar(es)"%o)
print("%d valor(es) positivo(s)"%p)
print("%d valor(es) negativo(s)"%n)
