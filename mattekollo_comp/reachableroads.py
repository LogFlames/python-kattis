def find(n):
    ko = []
    while roots[n] != n:
        n = roots[n]
        ko.append(n)

    for node in ko:
        roots[node] = n

    return n

def union(n, m):
    nr = find(n)
    mr = find(m)

    if nr == mr:
        return False

    if depth[nr] > depth[mr]:
        roots[mr] = nr
    elif depth[mr] > depth[nr]:
        roots[nr] = mr
    else:
        roots[mr] = nr
        depth[nr] += 1

def fg():
    for a in range(len(roots)):
        ar = find(a)
        roots[a] = ar

    gr = set()
    for a in roots:
        gr.add(a)

    return len(gr) - 1

n = int(input())

ans = []

for city in range(n):
    m = int(input())

    roots = [i for i in range(m)]
    depth = [1 for i in range(m)]

    r = int(input())

    for con in range(r):
        a, b = list(map(int, input().split()))
        union(a, b)

    ans.append(str(fg()))


print("\n".join(ans))

