t = int(input())

dp = {}

def solve(k, lo, hi):
    if k == 0:
        return 9999999999
    if hi <= lo:
        return 0
    if (k,lo,hi) in dp:
        return dp[(k,lo,hi)]
    ma = 9999999999
    for num in range(lo, hi):
        m = max(solve(k, num + 1, hi), solve(k - 1, lo, num) * (lo != num))
        ma = min(ma, m + num)

    dp[(k,lo,hi)] = ma
    return ma

for _ in range(t):
    k,m = map(int,input().split())
    print(solve(k, 0, m + 1))
