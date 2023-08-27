queue = []

n, k = list(map(int, input().split()))

visited = [False for i in range(2**k)]

for line in range(n):
    inp = int(input(), 2)
    visited[inp] = True
    queue.append(inp)

cnt = 0
while len(queue) > cnt:
    for i in range(k):
        b = queue[cnt] ^ (2**i)
        if not visited[b]:
            queue.append(b)
            visited[b] = True

    cnt += 1

val = bin(queue[-1])[2:]
val = "0" * (k - len(val)) + val
print(val)

