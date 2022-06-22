a = int(input())
b = a//60
a %= 60
c = b//60
b %= 60
print(f"{c}:{b}:{a}")
