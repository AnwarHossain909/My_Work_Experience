n = int(input())
m = 0
while True:
    m = int(input())
    if m>n:
        break
t = n
a = 1
while t<m:
    t += n + a
    a += 1
print(a)
