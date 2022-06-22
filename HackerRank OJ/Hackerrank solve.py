'''def minion_game(string):
    n = len(string)
    count_of_kev = 0
    count_of_stu = 0
    for i in range(n):
        if string[i] in "AEIOU":
            count_of_kev += (n-i)
        else:
            count_of_stu += (n-i)
    if count_of_kev > count_of_stu:
        print("Kevin " + str(count_of_kev))
    elif count_of_stu > count_of_kev:
        print("Stuart " + str(count_of_stu))
    else:
        print("Draw")
if __name__ == "__main__":
    s = input()
    minion_game(s)'''

from collections import Counter
n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
t = []
for i in range(x):
    a,b = map(int,input().split())
    if s[a]>0:
        t.append(b)
        s.subtract(Counter([a]))

print(sum(t))

