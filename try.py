s = input()
print(s)
n = input()
t = []

for i in range(0, int(n)):
    t.append(input())

count = 0
minnum = 0
num = 0

mark = []

for i in range(0, int(n)):
    count = 0
    for j in range(0, len(t[i])):
        for k in range(count, len(s)):
            if t[i][j] == s[k]:
                count = count+1
                print(k)
    if count == 0:
        num = len(t[i])+len(s)
    else:
        num = len(t[i])+len(s) - count*2
    print(j)

    if minnum < num:
        minnum = num
        mark = []
        mark.append(i)
    elif minnum == num:
        mark.append(i)
        print(i)


for i in range(0, len(mark)):
    print(t[mark[i]])
