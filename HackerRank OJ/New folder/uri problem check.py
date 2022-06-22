'''l = int(input())
m = input()
s = 0
for i in range(12):
    for j in range(12):
        f = float(input())

        if l == i:
            s += f
if m == "S":
    print("%.1f"%s)
else:
    print("%.1f"%(s/12))
'''
'''l = int(input())
m =  input()
s = []
for i in range(12):
    s.append([])
for i in range(12):
    for j in range(12):
        f = float(input())
        s[i].append(f)


if m == "S":
    t = 0
    for k in range(12):
        t += [k][l]
    print(t)
if m =="M":
    a = 0
    t = 0
    for k in range(12):
        t += m[k][l]
    a = t/12
    print("{:.1f}".format(a))
'''
for _ in range(int(input())):
    a,b = map(int,input().split())
    arr = list(map(int,input().split("")))



