i = 0
j = 0
while True:
    a = int(input())
    if a<0:
        break
    else:
        i += a
        j += 1
print("%.2f"%(i/j))
