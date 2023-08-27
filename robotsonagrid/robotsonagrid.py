N = int(input())

M = 2147483647

grid = []
gc = []
gc2 = []
for _ in range(N):
    grid.append(input())
    gc.append([0 for _ in range(N)])
    gc2.append([0 for _ in range(N)])


gc2[0][0] = 1
for x in range(N):
    for y in range(N):
        if x == 0 and y == 0:
            continue
        if grid[x][y] == ".":
            if x - 1 >= 0:
                gc2[x][y] += gc2[x - 1][y]
            if y - 1 >= 0:
                gc2[x][y] += gc2[x][y - 1]

if gc2[N - 1][N - 1] == 0:
    found = False
    q = []
    q.append((0, 0))
    while len(q) > 0:
        x,y = q.pop()

        if x == N - 1 and y == N - 1:
            found = True
            break

        if x + 1 < N and gc[x + 1][y] == 0 and grid[x + 1][y] == ".":
            gc[x + 1][y] = 1
            q.append((x + 1, y))
        if y + 1 < N and gc[x][y + 1] == 0 and grid[x][y + 1] == ".":
            gc[x][y + 1] = 1
            q.append((x, y + 1))
        if x - 1 >= 0 and gc[x - 1][y] == 0 and grid[x - 1][y] == ".":
            gc[x - 1][y] = 1
            q.append((x - 1, y))
        if y - 1 >= 0 and gc[x][y - 1] == 0 and grid[x][y - 1] == ".":
            q.append((x, y - 1))
            gc[x][y - 1] = 1

    if found:
        print("THE GAME IS A LIE")
    else:
        print("INCONCEIVABLE")
else:
    print(gc2[N - 1][N - 1] % M)

