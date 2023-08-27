input()
sizes = [0] + [*map(int, input().split())]
req = [0] * (len(sizes) + 10)

req[0] = 1

l = 0


for i in range(len(sizes)):
    if req[i] > sizes[i]:
        req[i + 1] = (req[i] - sizes[i]) * 2
        l += req[i + 1] * 2 ** ((-(3 + 2 * i) / 4) - 1)

if req[len(sizes)] > 0:
    print("impossible")
    exit()
print(l)





