li = list(map(int,input().split()))
n = "T"
s = 0
t = 0
for i in li:
    if n == "T":
        n = i
    else:
        if i>0:
            s = i
            break
for i in range(s):
    t += n
    n += 1
print("%d"%t)
