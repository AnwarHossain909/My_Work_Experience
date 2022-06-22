i = 0
a = 1
b = 2
c = 3
d = 0
while i<=2:
    if d == 0:
        print("I=%.0f J=%.0f"%(i,a))
        print("I=%.0f J=%.0f"%(i,b))
        print("I=%.0f J=%.0f"%(i,c))
    else:
        print("I=%.1f J=%.1f"%(i,a))
        print("I=%.1f J=%.1f"%(i,b))
        print("I=%.1f J=%.1f"%(i,c))
    d += 1
    if d == 5:
        d = 0
    i += 0.2
    a += 0.2
    b += 0.2
    c += 0.2
