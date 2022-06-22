A,B,C = list(map(float,input().split()))
a = 0.5*A*C
b = 3.14159*C*C
c = 0.5*(A+B)*C
d = B*B
e = A*B
print("TRIANGULO: %0.3f"%a)
print("CIRCULO: %0.3f"%b)
print("TRAPEZIO: %0.3f"%c)
print("QUADRADO: %0.3f"%d)
print("RETANGULO: %0.3f"%e)
