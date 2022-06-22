'''for t in range(int(input())):
    n,x,y = map(int,input().split())

    res = 1e5
    if (n>100):
        bus =n//100
        r = n%100
        car = r//4
        if (r%4):car += 1
        if (bus*x + car*y)<res:
            res = bus *x +car*y

    fs = n//100
    if(n%100): fs += 1
    if (fs*x)<res: res= fs*x
    sf = n//2
    if (n%4): sf+=1
    if (sf*y)<res: res=sf*y
    print(res)
'''

'''def linear_searchr(arr, t):
    n = len(arr)
    for book in range(n):
        if arr[book]==t:
            print(book)
            break
    else:
        print("sorry is not found")

if __name__== "__main__":
    arr = ['a','b','m','s','p','x','y']
    #t = "m"
    #t = 'i'
    #t = 'y'
    t = "b"
    linear_searchr(arr,t)

'''

'''

c = 0
while True:
    try:
        s = str(input()).lower()
        c += s.count("m")
    except EOFError:
        break
print(c)


'''
'''

def solve(n):
    if n & 1:
        return (n//2+1)
    else:
        return (n//2)
a,b = map(int,input().split())
print(solve(b)-solve(a-1))


'''
'''

n = int(input())
arr = list(map(int,input().split()))[:n]
c = 0
for i in arr:
    if i >= 80:
        c += 1
print(c)


'''
'''

for i in range(int(input())):
    a,b = map(int,input().split())
    c = int(str(int(a+b))+str(abs(int(a-b))))
    print("Case %d: %d"%(i+1,c))

'''
'''

for _ in range(int(input())):
    n = int(input())
    a,b,c = map(int,input().split())
    

'''


'''#E

a,b,c = map(int,input().split())
print(int((a**0.5)+(b**0.5)+(c**0.5)))


'''

'''#A

a = int(input())
print((a//2)-5)

'''
'''#C

a,b = map(int,input().split())
for i in range(a,b+1,a):
    print(i,end=" ")
print()'''


'''#G

a = int(input())
b = int(input())
print(a*b)

'''


'''#D

n = int(input())
print(*(list(map(int,input().split()))[:n])[::-1])

'''
'''#B

print("I am with BdGCC.")
print("Are you?")


'''
'''#F

n = int(input())
arr= list(map(int,input().split()))[:n]
for i in arr:
    if i%2 == 0:
        print("0",end=" ")
    else:
        print("1",end=" ")



'''
'''n = int(input())
arr = list(map(int,input().split()))[:n]
#for i in arr:
if n == 1:
    print("Hard")
elif n == 0:
    print("Easy")

'''

'''for _ in range(int(input())):
    n = int(input())
    if n<=15:
        print("Yes")
    else:
        print("No")
'''

'''for _ in range(int(input())):
    n = int(input())
    if n%4==0:
        print("Good")
    else:
        print("Not Good")
'''
'''for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    a = abs(x1-x2)
    b = abs(y1-y2)
    print(max(a,b))
'''
'''a,b = map(int,input().split())
p = b//2
t = a-p
print(t)

'''
'''x,y = map(int,input().split())
print(x*y)


'''

'''for _ in range(int(input())):
    n = int(input())
    aa = list(map(int,input().split()))[:n]
    c = 0
    for i in aa:
        if i>9 and i<60:
            c += 1
    print(c)'''



'''for _ in range(int(input())):
    l = list(map(int,input().split()))
    a,b,c = 0,1,2
    if l[b]*1 + l[c]*2 >=l[a]:
        print("Qualify")
    else:
        print("NotQualify")
'''
'''for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    arr = [a, b, c, d]
    c = 0
    c2 = 0

    for i in range(len(arr)):
        c += arr[2]/arr[0]
        c2 += arr[3]/arr[1]
    if c==c2:
        print(0)
    elif c>c2:
        print(1)
    else:
        print(-1)
'''
'''
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    arr2 = [6,7,13,14,20,21,27,28]
    print(len(set(arr+arr2)))'''

# aigola holo codecheF ar problem sulotion
'''for _ in range(int(input())):
    n,m = map(int,input().split())
    if (n*m)%2==0:
        print("YES")
    else:
        print("NO")
'''
'''for _ in range(int(input())):
    a = int(input())
    print(int(a/2+1))'''

'''
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in arr:
        if i <= k:
            print(1,end="")
            k =k-i
        else:
            print(0,end="")
    print()
'''
'''t = int(input())
for i in range(t):
    a,b,a1,b1,a2,b2 = map(int,input().split())
    if (a==a1 or a==b1) and (b==a1 or b ==b1):
        print("1")
    elif (a==a2 or a==b2) and (b==a2 or b==b2):
        print("2")
    else:
        print("0")
'''
'''for _ in range(int(input())):
    arr = list(map(int,input().split()))
    c1 = 0
    c2 = 0
    for i in arr:
        if (i==1):
            c1 += 1
        else:
            c2 += 1
    if c1>c2:
        print("YES")
    else:
        print("NO")
'''
'''for _ in range(int(input())):
    a,b,c = map(int,input().split())
    d = a*b
    p = a+c
    print(min(d,p))
'''


'''for _ in range(int(input())):
    x,y,z= map(int,input().split())
    if ((z*2)+x>=y) or ((z*1)+x>=y):
        print("Yes")
    else:
        print("No")
'''

'''for _ in range(int(input())):
    a,b,c = map(int,input().split())
    result = min(a,b,c)
    if result == a:
        print("Draw")
    elif result == b:
        print("Bob")
    else:
        print("Alice")
'''

'''for _ in range(int(input())):
    n = int(input())
    if n%4==0:
        print("No")
    else:
        print("Yes")'''

'''for _ in range(int(input())):
    x,y = map(int,input().split())
    print(min(x//2,y))
'''

'''for _ in range(int(input())):
    a = int(input())
    if a==7 and a<=10:
        print("Yes")
    else:
        print("N0")'''

'''for _ in range(int(input())):
    a,b = map(int,input().split())
    if (a+b)%2==0:
        print("Janmansh")
    else:
        print("Jay")
'''
'''
for _ in range(int(input())):
    x,a,b,c = map(int,input().split())
    if a<=b and a<=c:
        if b<=c:
            print((x-1)*a+b)
        else:
            print((x-1)*a+c)
    elif b<=a and b<=c:
        if a<=c:
            print((x-1)*b+a)
        else:
            print((x-1)*b+c)
    elif c<=a and c<=b:
        if b<=a:
            print((x-1)*c+b)
        else:
            print((x-1)*c+a)
'''


'''for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    s = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            s += 1
    print(max(s,n-s))
'''
'''
Janmansh and coins
for _ in range(int(input())):
    a,b = map(int,input().split())
    print((a*10)+(b*5))'''

'''for _ in range(int(input())):
    a = int(input())
    if (a+3)<=10:
        print("Yes")
    else:
        print("No")
.'''























