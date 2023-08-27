input()

a = list(map(int,input().split()))
ass = sorted(a)

c= 0
for i in range(len(a)):
    if a[i] != ass[i]:
        c += 1
print(c)
