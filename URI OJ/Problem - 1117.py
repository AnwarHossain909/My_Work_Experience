arr = []
while True:
    n = float(input())
    if n<=10 and n>=0:
        arr.append(n)
        if len(arr) == 2:
            break
    else:
        print("nota invalida")
print("media = %.2f"%(sum(arr)/2))
