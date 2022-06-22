i=j=k=l=0
m = 1
while True:
    if m == 2:
        break
    x,y = map(int,input().split())
    i += 1
    if x>y:
        j += 1
    elif x<y:
        k += 1
    else:
        l += 1
    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if n == 2:
        m +=1
print("%d grenais"%i)
print("Inter:%d"%j)
print("Gremio:%d"%k)
print("Empates:%d"%l)
if j>k:
    print("Inter venceu mais")
elif j<k:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
