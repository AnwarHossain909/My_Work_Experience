a,b,c = list(map(float,input().split()))
c = b**2-4*a*c
if a==0 or c<0:
    print("Impossivel calcular")
else:
    x1 = (-b + c**0.5)/(2*a)
    x2 = (-b - c ** 0.5)/(2*a)
    print("R1 = %.5f"%x1)
    print("R2 = %.5f" %x2)
