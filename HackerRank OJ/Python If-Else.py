# Nested If else:

n = int(input())
if n%2 == 1:
    print("Weird")
else:
    if 2<=n and 5>=n:
        print("Not Weird")
    elif 6<=n and 20>=n:
        print("Weird")
    elif 20<n:
        print("Not Weird")
    else:
        print("sorry!")
