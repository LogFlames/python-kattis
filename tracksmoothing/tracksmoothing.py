import math

t = int(input())

def f(m, cor, gl, r):
    tl = 0
    for i in range(len(cor)):
        tl += math.sqrt((m*(cor[(i+1)%n][0]-cor[i][0]))**2 + (m*(cor[(i+1)%n][1]-cor[i][1]))**2)

    tl += 2 * math.pi * r
    return tl - gl


for _ in range(t):
    r,n = map(int,input().split())
    cor = []
    for nn in range(n):
        cor.append([*map(int,input().split())])

    gl = 0
    for i in range(len(cor)):
        gl += math.sqrt((cor[(i+1)%n][0]-cor[i][0])**2 + (cor[(i+1)%n][1]-cor[i][1])**2)

    if gl < 2 * math.pi * r:
        print("Not possible")
        continue

    x0 = 0.3333
    fx0 = f(x0, cor, gl, r)
    x1 = 0.6666
    fx1 = f(x1, cor, gl, r)

    while abs(fx0 - fx1) > 1e-6:
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        x0,x1 = x1,x2
        fx0,fx1 = fx1,f(x2, cor, gl, r)

    print(x1)
