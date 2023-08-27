a = [input().split() for _ in range(3)]

acanwin = False
bcanwin = False


def place(b):
    X = sum([row.count("X") for row in b])
    O = sum([row.count("O") for row in b])

    hasWon(b)
    if acanwin and bcanwin:
        return

    turn = "XO"[X > O]
    for i in range(3):
        for j in range(3):
            if b[i][j] == "_":
                b[i][j] = turn
                place(b)
                b[i][j] = "_"

def hasWon(a):
    global acanwin
    global bcanwin
    for i in range(3):
        first = a[i][0]
        if first == "_":
            continue
        for j in range(3):
            if a[i][j] != first:
                break
        else:
            if first == "X":
                acanwin = True
                return
            else:
                bcanwin = True
                return

    for j in range(3):
        first = a[0][j]
        if first == "_":
            continue
        for i in range(3):
            if a[i][j] != first:
                break
        else:
            if first == "X":
                acanwin = True
                return
            else:
                bcanwin = True
                return

    if a[0][0] == a[1][1] == a[2][2] == "X":
        acanwin = True
        return
    if a[0][0] == a[1][1] == a[2][2] == "O":
        bcanwin = True
        return

    if a[0][2] == a[1][1] == a[2][0] == "X":
        acanwin = True
        return
    if a[0][2] == a[1][1] == a[2][0] == "O":
        bcanwin = True
        return

place(a)

if not acanwin and not bcanwin:
    print("ingen kan vinna")
elif acanwin and not bcanwin:
    print("Johan kan vinna")
elif bcanwin and not acanwin:
    print("Abdullah kan vinna")
elif bcanwin and acanwin:
    print("Abdullah och Johan kan vinna")

