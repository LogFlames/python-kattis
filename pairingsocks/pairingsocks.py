from collections import deque

input()
ns = deque(map(int,input().split()))
a = deque()

m = 0

while len(ns) > 0:
    m += 1
    if len(a) == 0:
        a.appendleft(ns.popleft())
        continue

    if ns[0] == a[0]:
        ns.popleft()
        a.popleft()
        continue

    a.appendleft(ns.popleft())

if len(a) == 0:
    print(m)
else:
    print("impossible")

