t,n = map(int,input().split())

s = list(map(int,input().split()))

s.sort(reverse=True)

a = 0
l = 0
while a < t * 60 and len(s) > 0:
    l = s.pop()
    a += l

if len(s) == 0:
    l = 0

print(a-l)

