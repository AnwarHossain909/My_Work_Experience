a = int(input())
for _ in range(a):
    b = int(input())
    if b>0:
        if b%2==0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif b==0:
        print("NULL")
    else:
        if b%2==0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
