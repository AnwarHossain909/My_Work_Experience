x = float(input())
y =x
a = y/100
b = y%100
c = b/50
d = b%50
e = d/20
f = d%20
g = f/10
h = f%10
i = h/5
j = h%5
k = j/2
l = j%2
m = x*100
n = int(m)
o = n%100
p = o/50
q = o%50
r = q/25
s = q%25
t = s/10
u = s%10
v = u/5
w = u%5

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%(int(a)))
print("%d nota(s) de R$ 50.00"%(int(c)))
print("%d nota(s) de R$ 20.00"%(int(e)))
print("%d nota(s) de R$ 10.00"%(int(g)))
print("%d nota(s) de R$ 5.00"%(int(i)))
print("%d nota(s) de R$ 2.00"%(int(k)))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%(int(l)))
print("%d moeda(s) de R$ 0.50"%(int(p)))
print("%d moeda(s) de R$ 0.25"%(int(r)))
print("%d moeda(s) de R$ 0.10"%(int(t)))
print("%d moeda(s) de R$ 0.05"%(int(v)))
print("%d moeda(s) de R$ 0.01"%(int(w)))
