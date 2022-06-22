# First System:

a = int(input())
b = int(input())
count = 0
for i in range(b+1,a):
    if i%2 == 1:
        count += i
print(count)

# Second System:
# Not Accepted:
'''
a = int(input())
b = int(input())
if a>b and a%2 == 0:
    print(a-1)
#elif b>a and b%2 == 0:
    #print(b-1)
elif a>b and a%2 == 1:
    print(a-2)
#elif b>a and b%2 == 1:
    #print(a-2)
else:
    print(0)
    '''

