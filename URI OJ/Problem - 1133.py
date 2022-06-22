a = int(input())
b = int(input())
if b>a:
    for i in range(a+1,b):
        if i%5 == 2 or i%5 == 3:
            print(i)
else:
    for j in range(b+1,a):
        if j%5 == 2 or j%5 == 3:
            print(j)
