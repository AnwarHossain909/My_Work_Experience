n = int(input())
j = 1
k = 1
for i in range(1,n+1):
    j = i*i
    k = i*i*i
    print("%d %d %d"%(i,j,k))
    j += 1
    k += 1
    print("%d %d %d"%(i,j,k))
