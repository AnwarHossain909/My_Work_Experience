rabit = 0
rat = 0
frog = 0
for _ in range(int(input())):
    a,b = input().split()
    a = int(a)
    if b == "C":
        rabit += a
    elif b == "R":
        rat += a
    elif b == "S":
        frog += a
c = rabit+rat+frog
r1 = (rabit*100)/c
r2 = (rat*100)/c
r3 = (frog*100)/c
print("Total: %d cobaias"%c)
print("Total de coelhos: %d"%rabit)
print("Total de ratos: %d"%rat)
print("Total de sapos: %d"%frog)
print("Percentual de coelhos: %.2f"%r1,"%")
print("Percentual de ratos: %.2f"%r2,"%")
print("Percentual de sapos: %.2f"%r3,"%")
