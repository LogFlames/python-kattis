from collections import deque

N = int(input())

def isway(h):
    vis = [[-1 for _ in range(N)] for _ in range(N)]

    vis[0][0] = 0
    
    qu = deque([])
    qu.append((0,0))

    while len(qu) > 0:
        x,y = qu.popleft()
        if x > 0     and grid[x - 1][y] < h and (vis[x - 1][y] == -1 or vis[x - 1][y] > vis[x][y] + 1):

            vis[x - 1][y] = vis[x][y] + 1
            qu.append((x - 1, y))

        if x < N - 1 and grid[x + 1][y] < h and (vis[x + 1][y] == -1 or vis[x + 1][y] > vis[x][y] + 1):

            vis[x + 1][y] = vis[x][y] + 1
            qu.append((x + 1, y))

        if y > 0     and grid[x][y - 1] < h and (vis[x][y - 1] == -1 or vis[x][y - 1] > vis[x][y] + 1):

            vis[x][y - 1] = vis[x][y] + 1
            qu.append((x, y - 1))

        if y < N - 1 and grid[x][y + 1] < h and (vis[x][y + 1] == -1 or vis[x][y + 1] > vis[x][y] + 1):

            vis[x][y + 1] = vis[x][y] + 1
            qu.append((x, y + 1))

    return vis[N - 1][N - 1] > -1

grid = [[*map(int,input().split())] for _ in range(N)]
    
hl = 1
hh = max(sum(grid,[])) + 1

while hl < hh:
    hm = (hl + hh) // 2
    if isway(hm):
        hh = hm
    else:
        hl = hm + 1

print(hl - 1)
