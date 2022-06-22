'''n = int(input())
a = set(map(int,input().split()))
b = set.intersection(a)
c = set.update(a)
e = set.symmetric_difference(a)
f = set.difference(a)
print(f)'''
'''for _ in range(int(input())):
    x,y,z = map(int,input().split())
    print((x+y+z)-min(x,y,z))'''

'''for _ in range(int(input())):
    a,b = map(int,input().split())

    if ((21-(a+b)) <= 10):
        print(21-(a+b))
    else:
        print(-1)'''

'''for _ in range(int(input())):
    a = int(input())
    if a%10==0:
        print(a/10)
    else:
        print((a//10)+1)'''

'''import math
for _ in range(int(input())):
    n = int(input())
    print(math.ceil(n/10))
'''
'''
for _ in range(int(input())):
    n = int(input())
    m = str(input())
    count = 0
    for i in range(n-1):
        if m[i+1] != m[i]:
            count += 1
    print(count+1)
'''

'''for _ in range(int(input())):
    b,c = map(int,input().split(' '))
    a = 1
    while (((a*b)%c)!=0):
        a +=1
    print(a)'''

'''def sulotion(b,c):
    if c == 0:
        return b
    return sulotion(c,b%c)
for _ in range(int(input())):
    b,c = map(int,input().split())
    print(c//sulotion(b,c))'''


for _ in range(int(input())):
    a = str(input())
    b = str(input())
    c= a[::-1],b[::-1]
    print(c)










