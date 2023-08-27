n,a,b,c = map(int,input().split())

dp = {}

def t(forbs,de):
    if (forbs,de) in dp:
        return dp[(forbs,de)]
    if de == 0:
        return 1
    ans = (
            (a * t(0,de-1) if (forbs != 0 and a > 0) else 0) +
            (b * t(1,de-1) if (forbs != 1 and b > 0) else 0) + 
            (c * t(2,de-1) if (forbs != 2 and c > 0) else 0)
            )
    dp[(forbs,de)] = ans
    return ans

sols = t(-1,n)

print(sols%(10**9+7))
