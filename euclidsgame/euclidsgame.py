import sys
sys.setrecursionlimit(100000000)

dp = {}

def ww(a, b, p):
    a,b = max(a, b), min(a,b)
    if b == 0:
        return not p
    if (a,b,p) in dp:
        return dp[(a,b,p)]
    for i in range(a//b, 0, -1):
        if ww(a - b * i, b, not p) == p:
            dp[(a, b,p)] = p
            return p
    dp[(a,b,p)] = not p
    return not p

while True:
    a,b = map(int, input().split())
    if a == b == 0:
        break

    print(("Stan" if ww(a,b,True) else "Ollie") + " wins")
