t,b = map(int,input().split())
np = list(map(int,input().split()))
latest = {}
for tt in range(t):
    p,v = input().split()
    latest[p] = int(v)
    
for s in range(b):
    tu = 0
    for p in range(np[s]):
        pp,v = input().split()
        tu += max(0, latest[pp] - int(v))
    print(tu)
