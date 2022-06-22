e = 0
f = 0
g = 0
while True:
    a = int(input())
    if a == 4:
        break
    if a == 8:
        print("MUITO OBRIGADO")
    if a == 1:
        e += 1
    if a == 2:
        f += 1
    if a == 3:
        g += 1
print("Alcool: %d"%e)
print("Gasolina: %d"%f)
print("Diesel: %d"%g)
