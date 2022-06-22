b = int(input())
count = 0
out = 0
for _ in range(b):
    a = int(input())
    if a >= 10 and a <= 20:
        count += 1
    else:
        out += 1
print("%d in"%count)
print("%d out"%out)
