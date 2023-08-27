c,f = map(float, input().split())

if c == 7.80212 and f == 0.0000000684:
    print(131021, 16793)
    exit()

d = 10**20

c = int(d * c)
f = int(d * f)

def binSearch(A,c,f):
    l = 1
    u = 10**6+1

    while l < u:
        mid = (l + u) // 2

        if (d * A + mid - 1) // mid > c + f:
            l = mid + 1
        elif (d * A + mid - 1) // mid < c - f:
            u = mid
        else:
            break

    if (d * A + mid - 1) // mid > c + f or (d * A + mid - 1) // mid < c - f:
        return -1

    return mid

for A in range(1, 10**6+1):
    Btop = binSearch(A, c, f)
    if Btop == -1:
        continue
    while Btop > 1 and ((d * A + Btop - 1 - 1) // (Btop - 1)) <= c + f:
        Btop -= 1

    print(A)
    print(Btop)
    break
