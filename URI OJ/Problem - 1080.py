li = []
for i in range(100):
    li.append(int(input()))
m = max(li)
print(m)
print(li.index(m)+1)
