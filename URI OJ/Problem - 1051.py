t = float(input())
if t>0 and t<=2000:
    print("Isento")
elif t>2000 and t<=3000:
    n = t - 2000
    m = n * 0.08
    print("R$ %.2f" % m)
elif t>3000 and t<4500:
    n = t-3000
    m = (n * 0.18) + (1000*0.08)
    print("R$ %.2f" % m)
else:
    n = t-4500
    m = (n*0.28) + (1500 * 0.18) + (1000*0.08)
    print("R$ %.2f"%m)
