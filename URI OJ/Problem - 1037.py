a = float(input())
if a<0 or a>100:
    print("Fora de intervalo")
elif a<=25:
    print("Intervalo [0,25]")
elif a<=50:
    print("Intervalo (25,50]")
elif a<=75:
    print("Intervalo (50,75]")
elif a<=100:
    print("Intervalo (75,100]")
else:
    print("Out of Interval")
