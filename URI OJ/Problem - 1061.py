d1 = int(input().split()[-1])
h1,m1,s1 = map(int,input().split(" : "))
d2 = int(input().split()[-1])
h2,m2,s2 = map(int,input().split(" : "))
d = d2 - d1
h = h2 - h1
m = m2 - m1
s = s2 - s1
if s<0:
    s = s+60
    m = m-1
if m<0:
    m = m+60
    h = h-1
if h<0:
    h = h+24
    d = d-1
print("%d dia(s)"%d)
print("%d hora(s)"%h)
print("%d minuto(s)"%m)
print("%d segundo(s)"%s)
