N = int(input())
MOD = 10**9+7

def pow(M, a):
    X = [1, 0, 0, 1]

    while a:
        if a % 2:
            X = [X[0]*M[0] + X[1]*M[2], X[0]*M[1] + X[1]*M[3], X[2]*M[0] + X[3]*M[2], X[2]*M[1] + X[3]*M[3]]
        M = [M[0]*M[0] + M[1]*M[2], M[0]*M[1] + M[1]*M[3], M[2]*M[0] + M[3]*M[2], M[2]*M[1] + M[3]*M[3]]
        X = [X[0] % MOD, X[1] % MOD, X[2] % MOD, X[3] % MOD]
        M = [M[0] % MOD, M[1] % MOD, M[2] % MOD, M[3] % MOD]
        a //= 2

    return X

a = [1, 1, 1, 0]
x = pow(a, N-1)

mult = [2,1]

ans = x[0]*mult[0] + x[1]+mult[1]

if N < 3:
    print(N)
else:
    print((ans-2) % MOD)


