'''for t in range(int(input())):
    n = str(input())
    a = abs(int(n[:2])-9)*60
    b = int(n[2:])+a
    x = (b//5)*8
    y = (b//15)*8
    print(x-y)

'''

a,b = map(str,input().split())
a = int(a)
b = float(b)
if a%5==0 and (a+0.50)<=b:
    print("%.2f"%(b-a-0.50))
else:
    print("%.2f"%b)
