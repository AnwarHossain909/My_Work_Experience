n = int(input())
m = list(map(int,input().split()))
c = 0
p = m[0]
count = 0
for i in m:
    if (i<p):
        p = i
        c = count
    count += 1
print("Menor valor: %d"%p)
print("Posicao: %d"%c)



